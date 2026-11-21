"""Lab 1.2: hub-and-spoke research coordinator (Step 1 skeleton).

The coordinator is the hub. It decomposes a topic into subtopics, delegates each
subtopic to a subagent (a spoke), and aggregates what comes back. Subagents never
talk to each other and never see the coordinator's conversation: each one is a
separate Messages API call that receives only the prompt the coordinator builds.

Orchestration is code-driven: the phases below are Python functions, so the
coverage map and refinement loop are ordinary data and control flow.

Status of each phase:
    decompose()          Step 2  done: draft call, then a coverage-review call
    delegate()           Step 3  stub, returns placeholder findings
    evaluate_coverage()  Step 4  stub, returns an empty coverage map
    refinement loop      Step 5  not started (see research())

Usage:
    python coordinator-a.py "renewable energy technologies"
"""

import json
import logging
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# .env lives at the repository root, two levels above this lab folder.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

MAX_TOKENS = 2048
MIN_SUBTOPICS = 5             # Step 2 acceptance criterion
COVERAGE_THRESHOLD = 0.9      # Step 5: re-delegate while completeness is below this
MAX_REFINEMENT_ROUNDS = 3     # Step 5: hard stop for the refinement loop

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
log = logging.getLogger("coordinator")


# ---------------------------------------------------------------------------
# Data contracts. Every phase passes these shapes, so define them first.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SubagentDefinition:
    """Static description of one spoke. This is data, not a running agent."""

    name: str
    description: str      # what the coordinator uses to choose this subagent
    system_prompt: str    # the subagent's role; it sees nothing else by default
    tools: tuple = ()     # tool schemas, if Step 3 gives this subagent stub tools


@dataclass
class Finding:
    """One claim returned by a subagent.

    `subtopic` is what lets Step 4 map findings back to the decomposition.
    """

    subtopic: str
    claim: str
    source: str
    confidence: str       # "high" | "medium" | "low"
    subagent: str         # which spoke produced it


@dataclass
class ResearchResult:
    topic: str
    subtopics: list[str]
    findings: list[Finding] = field(default_factory=list)
    coverage: dict = field(default_factory=dict)
    rounds: int = 0


# Output format both subagents must follow. It is included in every delegation
# prompt, because a subagent cannot know it otherwise.
FINDING_FORMAT = (
    "Return ONLY a JSON array. Each element is an object with the keys "
    '"claim" (one factual sentence), "source" (where it came from), and '
    '"confidence" ("high", "medium" or "low"). Return [] if you found nothing.'
)


# ---------------------------------------------------------------------------
# Hub and spokes
# ---------------------------------------------------------------------------

COORDINATOR_SYSTEM_PROMPT = (
    "You are the coordinator of a research team. You do not research topics "
    "yourself. Your responsibilities are: (1) decompose a research topic into "
    "distinct subtopics that together cover its full breadth; (2) assign each "
    "subtopic to a subagent with a self-contained brief; (3) aggregate the "
    "findings that subagents return; and (4) identify subtopics that lack "
    "substantive findings so that they can be re-assigned. Subagents cannot "
    "see this conversation or each other's work."
)

SUBAGENTS = {
    "web_search": SubagentDefinition(
        name="web_search",
        description="Finds recent public information on one subtopic: news, statistics, deployments.",
        system_prompt=(
            "You are a web research specialist. You research exactly one subtopic, "
            "described in the brief you receive. Report only claims you can attribute "
            "to a source. Follow the output format in the brief exactly."
        ),
    ),
    "doc_analysis": SubagentDefinition(
        name="doc_analysis",
        description="Extracts technical and quantitative claims on one subtopic from reference documents.",
        system_prompt=(
            "You are a document analyst. You extract technical and quantitative claims "
            "about exactly one subtopic, described in the brief you receive. Do not "
            "speculate beyond the material. Follow the output format in the brief exactly."
        ),
    ),
}


def make_client():
    """Return (client, model_id). Same provider selection as lab 1.1."""
    bedrock_model = os.getenv("AWS_BEDROCK_MODEL_ID")
    if bedrock_model:
        client = anthropic.AnthropicBedrock(
            aws_region=os.getenv("AWS_REGION"),
            aws_profile=os.getenv("AWS_PROFILE"),
        )
        log.info("provider=bedrock region=%s model=%s", os.getenv("AWS_REGION"), bedrock_model)
        return client, bedrock_model

    if os.getenv("ANTHROPIC_API_KEY"):
        model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5")
        log.info("provider=anthropic model=%s", model)
        return anthropic.Anthropic(), model

    sys.exit(
        "No credentials configured. Set AWS_BEDROCK_MODEL_ID (with AWS_REGION and "
        "AWS_PROFILE) or ANTHROPIC_API_KEY in the .env file at the repository root."
    )


class Coordinator:
    def __init__(self, client, model, subagents=SUBAGENTS):
        self.client = client
        self.model = model
        self.subagents = subagents
        self.system_prompt = COORDINATOR_SYSTEM_PROMPT

    # -- Model call helper ---------------------------------------------------
    def _ask_json(self, system: str, prompt: str):
        """Send one user message and return the reply parsed as JSON.

        Raises if the model stopped for any reason other than finishing its turn,
        or if the reply is not valid JSON, so bad output never reaches later phases.
        """
        response = self.client.messages.create(
            model=self.model,
            max_tokens=MAX_TOKENS,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        if response.stop_reason != "end_turn":
            raise RuntimeError(f"model stopped early: stop_reason={response.stop_reason}")

        # The reply can contain thinking blocks before the text block.
        text = next((b.text for b in response.content if b.type == "text"), "")
        # Models sometimes wrap JSON in a code fence despite the instruction.
        text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(f"reply is not valid JSON: {text[:300]!r}") from exc

    @staticmethod
    def _as_string_list(value, what: str) -> list[str]:
        if not (isinstance(value, list) and all(isinstance(s, str) for s in value)):
            raise ValueError(f"{what}: expected a JSON array of strings, got {value!r}")
        return [s.strip() for s in value if s.strip()]

    # -- Phase 1: decomposition (Step 2) -----------------------------------
    def decompose(self, topic: str) -> list[str]:
        """Return at least MIN_SUBTOPICS distinct subtopics covering `topic`.

        Two model calls. The first lists broad categories across established,
        emerging and experimental areas. The second reviews that list as a domain
        expert would and returns only the major areas it is missing. Narrow
        decomposition is the usual root cause of coverage gaps, so the review
        step is a separate call rather than an instruction inside the first.
        """
        log.info("phase=decompose topic=%r", topic)

        draft = self._as_string_list(
            self._ask_json(
                self.system_prompt,
                f"Research topic: {topic!r}\n\n"
                f"Decompose this topic into at least {MIN_SUBTOPICS} distinct subtopics "
                "that together cover its full breadth. Start from the broad categories "
                "of the topic, and include established, emerging and experimental areas. "
                "Each subtopic must be a short noun phrase that a researcher could "
                "investigate on its own. Do not overlap subtopics.\n\n"
                "Return ONLY a JSON array of strings, with no other text.",
            ),
            "draft decomposition",
        )
        log.info("phase=decompose draft=%s", draft)

        missing = self._as_string_list(
            self._ask_json(
                self.system_prompt,
                f"Research topic: {topic!r}\n\n"
                f"Proposed subtopics:\n{json.dumps(draft, indent=2)}\n\n"
                "Review this list as a domain expert would. Identify any major area of "
                "the topic that is not covered by any subtopic. Do not repeat or rename "
                "existing subtopics, and do not split them into smaller ones.\n\n"
                "Return ONLY a JSON array of strings naming the missing areas, "
                "or [] if nothing major is missing.",
            ),
            "coverage review",
        )
        log.info("phase=decompose review_added=%s", missing)

        # Merge, dropping case-insensitive duplicates while keeping order.
        seen, subtopics = set(), []
        for s in draft + missing:
            if s.lower() not in seen:
                seen.add(s.lower())
                subtopics.append(s)

        if len(subtopics) < MIN_SUBTOPICS:
            raise ValueError(f"only {len(subtopics)} subtopics after review: {subtopics}")
        log.info("phase=decompose subtopics=%s", subtopics)
        return subtopics

    # -- Phase 2: delegation (Step 3) --------------------------------------
    def delegate(
        self,
        subagent: SubagentDefinition,
        subtopic: str,
        topic: str,
        prior_findings: list[Finding],
    ) -> list[Finding]:
        """Run one subagent on one subtopic and return its findings.

        The parameters are the ONLY context the subagent gets. The brief you
        build in Step 3 must contain: the subtopic, the broader research goal
        (`topic`), FINDING_FORMAT, and any relevant `prior_findings`.

        TODO Step 3: build the brief, call the model with subagent.system_prompt,
        log the full brief, parse the JSON reply into Finding objects.
        """
        log.info(
            "phase=delegate subagent=%s subtopic=%r prior_findings=%d",
            subagent.name, subtopic, len(prior_findings),
        )
        return [
            Finding(
                subtopic=subtopic,
                claim="placeholder claim",
                source="placeholder",
                confidence="low",
                subagent=subagent.name,
            )
        ]

    # -- Phase 3: aggregation and coverage (Step 4) ------------------------
    def evaluate_coverage(self, subtopics: list[str], findings: list[Finding]) -> dict:
        """Map each subtopic to its findings and compute completeness.

        TODO Step 4: decide what counts as "substantive" (not just "any
        finding"), then fill covered, gaps and completeness.
        """
        log.info("phase=evaluate subtopics=%d findings=%d", len(subtopics), len(findings))
        return {"covered": [], "gaps": list(subtopics), "completeness": 0.0}

    # -- Orchestration ------------------------------------------------------
    def research(self, topic: str) -> ResearchResult:
        result = ResearchResult(topic=topic, subtopics=self.decompose(topic))

        for subtopic in result.subtopics:
            for subagent in self.subagents.values():
                result.findings.extend(
                    self.delegate(subagent, subtopic, topic, prior_findings=[])
                )

        result.coverage = self.evaluate_coverage(result.subtopics, result.findings)

        # TODO Step 5: while completeness < COVERAGE_THRESHOLD and
        # result.rounds < MAX_REFINEMENT_ROUNDS, re-delegate only the gaps,
        # then re-evaluate coverage.

        log.info(
            "done completeness=%.0f%% gaps=%s",
            result.coverage["completeness"] * 100, result.coverage["gaps"],
        )
        return result


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python coordinator-a.py "<research topic>"')
    topic = " ".join(sys.argv[1:])

    client, model = make_client()
    result = Coordinator(client, model).research(topic)

    print(f"\nTopic: {result.topic}")
    print(f"Subtopics ({len(result.subtopics)}): {result.subtopics}")
    print(f"Findings: {len(result.findings)}")
    print(f"Coverage: {result.coverage}")


if __name__ == "__main__":
    main()
