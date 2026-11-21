"""Lab 1.2: hub-and-spoke research coordinator built with the Claude Agent SDK.

Architecture (model-driven orchestration):

    coordinator (main query)      built-in tools: Agent only
        |  Agent tool              writes a self-contained brief per call
        +--> searcher              mcp__research__search_sources
        +--> analyst               mcp__research__get_document
                 \\_____ in-process MCP server "research" (corpus.py) _____/

Subagents never see the coordinator's conversation or each other. The only
context a subagent receives is the `prompt` the coordinator writes when it
calls the Agent tool, and this script logs every one of those briefs in full.

The hub rule is enforced, not only requested: a PreToolUse hook denies the
research tools whenever the caller is the coordinator itself (no agent_id).

After the run, verify() checks the report against acceptance criteria that the
coordinator never sees (REQUIRED_CATEGORIES), so the coordinator cannot pass
the test simply by being told the answer.

Usage (from this folder, with the project venv):
    ../../.venv/bin/python coordinator.py                    # renewable energy test
    ../../.venv/bin/python coordinator.py "some other topic"
    ../../.venv/bin/python coordinator.py --narrow           # deliberate narrow decomposition
"""

import argparse
import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

from claude_agent_sdk import (
    AgentDefinition,
    AssistantMessage,
    ClaudeAgentOptions,
    HookMatcher,
    ResultMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
    query,
)

from corpus import DOCUMENTS
from research_tools import GET_DOCUMENT_TOOL, SEARCH_TOOL, SERVER_NAME, research_server

# .env lives at the repository root, two levels above this lab folder.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

DEFAULT_TOPIC = "renewable energy technologies"
MIN_SUBTOPICS = 5
COVERAGE_THRESHOLD = 0.9
MAX_REFINEMENT_ROUNDS = 2

# Test oracle for Step 6. Deliberately NOT given to the coordinator.
REQUIRED_CATEGORIES = {
    "solar": ["solar", "photovoltaic"],
    "wind": ["wind"],
    "geothermal": ["geothermal"],
    "tidal": ["tidal"],
    "biomass": ["biomass", "bioenergy", "biogas"],
    "fusion": ["fusion"],
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("hub")


# ---------------------------------------------------------------------------
# Spokes
# ---------------------------------------------------------------------------

SEARCHER_PROMPT = """\
You find candidate sources for exactly one subtopic. The brief you receive from the
coordinator is the only context you have.

Use search_sources with two or three different short queries: the subtopic name, a
synonym, and a key technology term. Do not read documents or summarise content.

Return ONLY this JSON, with no other text:
{"subtopic": "<as given>", "queries_tried": ["..."],
 "sources": [{"source_id": "...", "title": "...", "date": "YYYY-MM-DD"}]}
Return an empty "sources" list if nothing matched."""

ANALYST_PROMPT = """\
You extract factual claims from specific sources. The brief you receive from the
coordinator names the research goal, the subtopic and the source IDs to read; it is
the only context you have.

Read each listed source with get_document. Extract only claims stated in the source
text; do not add outside knowledge. Confidence is "high" for a specific dated figure
or result, "medium" for a qualitative statement, "low" if the source is only
tangentially relevant.

Return ONLY this JSON, with no other text:
{"subtopic": "<as given>",
 "findings": [{"claim": "...", "source_id": "...", "date": "YYYY-MM-DD",
               "confidence": "high|medium|low"}],
 "notes": "<unknown or irrelevant source IDs, or empty>"}"""

SUBAGENTS = {
    "searcher": AgentDefinition(
        description=(
            "Finds source IDs in the research corpus for ONE subtopic. Use before "
            "analyst. Does not read or summarise documents."
        ),
        prompt=SEARCHER_PROMPT,
        tools=[SEARCH_TOOL],
        model="inherit",
    ),
    "analyst": AgentDefinition(
        description=(
            "Reads specific source IDs for ONE subtopic and extracts dated, "
            "source-attributed claims. Needs the source IDs in its brief."
        ),
        prompt=ANALYST_PROMPT,
        tools=[GET_DOCUMENT_TOOL],
        model="inherit",
    ),
}


# ---------------------------------------------------------------------------
# Hub
# ---------------------------------------------------------------------------

BROAD_DECOMPOSITION = f"""\
1. Decompose. First list every major category of the topic, covering established,
   emerging and experimental areas. Then review the list and ask which major area a
   domain expert would say is missing; add it. Produce at least {MIN_SUBTOPICS}
   distinct subtopics."""

# Experiment for the lab's "deliberate narrow decomposition" criterion.
NARROW_DECOMPOSITION = """\
1. Decompose. Choose only the 2 most commercially significant subtopics."""


def coordinator_prompt(narrow: bool) -> str:
    decomposition = NARROW_DECOMPOSITION if narrow else BROAD_DECOMPOSITION
    return f"""\
You are the coordinator (hub) of a research team. You do not research directly and
you have no research tools. All research is done by subagents that you invoke with
the Agent tool. A subagent cannot see this conversation, other subagents, or earlier
results unless you include them in the prompt you write for it.

Subagents:
- searcher: finds source IDs for one subtopic.
- analyst: reads given source IDs and extracts claims.

Procedure:
{decomposition}
2. Search. Invoke searcher once per subtopic. Issue all searcher calls in the same
   turn so that they run in parallel. Each brief must state the overall research
   goal, the one subtopic, and that the reply must follow the searcher's JSON format.
3. Analyse. Invoke analyst once per subtopic that has sources, in parallel. Each
   brief must state the research goal, the subtopic, and the exact source IDs that
   the searcher returned.
4. Coverage. Build a coverage map. A subtopic is "covered" if it has at least one
   high or medium confidence claim, "superficial" if it has only low confidence
   claims, and "missing" if it has none. Completeness = covered / total.
5. Refine. If completeness is below {COVERAGE_THRESHOLD:.0%}, re-delegate only the
   superficial and missing subtopics with targeted briefs (for example, alternative
   search terms). Repeat at most {MAX_REFINEMENT_ROUNDS} times. Do not re-delegate
   covered subtopics.
6. Report. Return the final structured output. Every claim must cite a source_id
   that an analyst returned; do not add claims of your own. Record any figures that
   disagree between sources in "conflicts"."""


FINDING_SCHEMA = {
    "type": "object",
    "properties": {
        "claim": {"type": "string"},
        "source_id": {"type": "string"},
        "date": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
    "required": ["claim", "source_id", "date", "confidence"],
}

REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "topic": {"type": "string"},
        "subtopics": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "status": {"type": "string", "enum": ["covered", "superficial", "missing"]},
                    "findings": {"type": "array", "items": FINDING_SCHEMA},
                },
                "required": ["name", "status", "findings"],
            },
        },
        "completeness": {"type": "number"},
        "refinement_rounds": {"type": "integer"},
        "conflicts": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
    },
    "required": ["topic", "subtopics", "completeness", "refinement_rounds", "conflicts", "summary"],
}


async def enforce_hub(input_data, tool_use_id, context):
    """PreToolUse hook: research tools may be called only from inside a subagent."""
    if input_data.get("agent_id"):
        return {}
    log.warning("HUB VIOLATION blocked: coordinator called %s directly", input_data["tool_name"])
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "The coordinator must not research directly. Delegate with the Agent tool."
            ),
        }
    }


def bedrock_env() -> dict:
    """Environment for the Claude Code CLI. The CLI signs AWS requests itself.

    CLAUDE_CODE_DISABLE_BACKGROUND_TASKS makes every Agent call synchronous, so
    the Agent tool_result is the subagent's answer. Without it the CLI launches
    subagents asynchronously, the hub receives only a launch notice, and it may
    write its report before the findings arrive. (AgentDefinition(background=False)
    did not change this in CLI 2.1.294 / SDK 0.2.180.)
    """
    env = {"CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1"}
    if os.getenv("AWS_BEDROCK_MODEL_ID"):
        return env | {
            "CLAUDE_CODE_USE_BEDROCK": "1",
            "AWS_REGION": os.environ.get("AWS_REGION", ""),
            "AWS_PROFILE": os.environ.get("AWS_PROFILE", ""),
        }
    if os.getenv("ANTHROPIC_API_KEY"):
        return env
    sys.exit(
        "No credentials configured. Set AWS_BEDROCK_MODEL_ID (with AWS_REGION and "
        "AWS_PROFILE) or ANTHROPIC_API_KEY in the .env file at the repository root."
    )


def build_options(narrow: bool, max_turns: int, max_budget_usd: float) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        system_prompt=coordinator_prompt(narrow),
        model=os.getenv("AWS_BEDROCK_MODEL_ID") or os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5"),
        env=bedrock_env(),
        tools=["Agent"],                       # coordinator's only built-in tool
        agents=SUBAGENTS,
        mcp_servers={SERVER_NAME: research_server},
        allowed_tools=["Agent", SEARCH_TOOL, GET_DOCUMENT_TOOL],  # no permission prompts
        hooks={"PreToolUse": [HookMatcher(matcher=f"{SEARCH_TOOL}|{GET_DOCUMENT_TOOL}",
                                          hooks=[enforce_hub])]},
        output_format={"type": "json_schema", "schema": REPORT_SCHEMA},
        setting_sources=[],                    # do not load this repo's tutor CLAUDE.md
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
    )


# ---------------------------------------------------------------------------
# Run and trace
# ---------------------------------------------------------------------------

async def run(topic: str, options: ClaudeAgentOptions) -> tuple[dict | None, dict]:
    agent_calls: dict[str, str] = {}   # Agent tool_use_id -> subagent type
    # The SDK emits one AssistantMessage per content block, so count Agent calls
    # per model turn (message_id), not per message, to detect parallel delegation.
    calls_per_turn: dict[str, int] = {}
    stats = {"delegations": 0, "max_parallel": 0, "turns": None, "cost_usd": None}
    report = None
    result_text = ""

    prompt = f"Research topic: {topic}"
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage) and message.parent_tool_use_id is None:
            # A coordinator turn. Every Agent tool_use here is one delegation.
            delegations = [b for b in message.content
                           if isinstance(b, ToolUseBlock) and b.name == "Agent"]
            for block in message.content:
                if isinstance(block, TextBlock) and block.text.strip():
                    log.info("[hub] %s", block.text.strip()[:300])
            for block in delegations:
                agent_type = block.input.get("subagent_type", "?")
                agent_calls[block.id] = agent_type
                stats["delegations"] += 1
                log.info("[hub -> %s] brief (%s):\n%s\n", agent_type, block.id[-8:],
                         block.input.get("prompt", ""))
            if delegations:
                turn = message.message_id or id(message)
                calls_per_turn[turn] = calls_per_turn.get(turn, 0) + len(delegations)
                stats["max_parallel"] = max(stats["max_parallel"], calls_per_turn[turn])
                log.info("[hub] delegation %d in model turn %s",
                         calls_per_turn[turn], str(turn)[-8:])

        elif isinstance(message, AssistantMessage):
            # Activity inside a subagent.
            who = agent_calls.get(message.parent_tool_use_id, "subagent")
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    log.info("    [%s] %s %s", who, block.name.split("__")[-1], block.input)

        elif isinstance(message, UserMessage) and message.parent_tool_use_id is None:
            # Subagent results come back to the hub as tool_result blocks.
            content = message.content if isinstance(message.content, list) else []
            for block in content:
                if isinstance(block, ToolResultBlock) and block.tool_use_id in agent_calls:
                    text = block.content if isinstance(block.content, str) else json.dumps(block.content)
                    log.info("[%s -> hub] %s%s", agent_calls[block.tool_use_id],
                             "ERROR " if block.is_error else "", text[:400])

        elif isinstance(message, ResultMessage):
            stats["turns"] = message.num_turns
            stats["cost_usd"] = message.total_cost_usd
            report = message.structured_output
            result_text = message.result or ""
            if message.is_error:
                log.error("run ended with error: subtype=%s %s", message.subtype, result_text[:400])

    if report is None and result_text:
        report = _parse_json(result_text)
    return report, stats


def _parse_json(text: str) -> dict | None:
    """Fallback if structured output was not returned: take the last JSON object."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------------------
# Acceptance checks (Step 6)
# ---------------------------------------------------------------------------

def verify(report: dict, stats: dict) -> bool:
    subtopics = report.get("subtopics", [])
    corpus_text = " ".join(
        [s["name"] for s in subtopics]
        + [f["claim"] for s in subtopics for f in s.get("findings", [])]
    ).lower()
    cited = {f["source_id"] for s in subtopics for f in s.get("findings", [])}
    missing_categories = [c for c, words in REQUIRED_CATEGORIES.items()
                          if not any(w in corpus_text for w in words)]
    unknown_sources = sorted(cited - DOCUMENTS.keys())

    checks = [
        (f"decomposition has >= {MIN_SUBTOPICS} subtopics", len(subtopics) >= MIN_SUBTOPICS,
         f"{len(subtopics)}: {[s['name'] for s in subtopics]}"),
        ("all required categories covered", not missing_categories,
         f"missing: {missing_categories}" if missing_categories else "solar, wind, geothermal, tidal, biomass, fusion"),
        ("every cited source exists in the corpus", not unknown_sources,
         f"unknown: {unknown_sources}" if unknown_sources else f"{len(cited)} sources cited"),
        ("work was delegated through the hub", stats["delegations"] > 0,
         f"{stats['delegations']} Agent calls"),
        ("parallel delegation observed", stats["max_parallel"] > 1,
         f"max {stats['max_parallel']} Agent calls in one turn"),
    ]
    print("\nAcceptance checks")
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    print(f"\n  Coordinator's own completeness figure: {report.get('completeness')}"
          f"  (refinement rounds: {report.get('refinement_rounds')})")
    if report.get("conflicts"):
        print(f"  Conflicts reported: {report['conflicts']}")
    return all(ok for _, ok, _ in checks[:4])


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("topic", nargs="*", help=f"research topic (default: {DEFAULT_TOPIC!r})")
    parser.add_argument("--narrow", action="store_true",
                        help="deliberately decompose into only 2 subtopics")
    parser.add_argument("--max-turns", type=int, default=40)
    parser.add_argument("--max-budget-usd", type=float, default=3.0)
    args = parser.parse_args()
    topic = " ".join(args.topic) or DEFAULT_TOPIC

    options = build_options(args.narrow, args.max_turns, args.max_budget_usd)
    log.info("topic=%r narrow=%s model=%s", topic, args.narrow, options.model)
    report, stats = asyncio.run(run(topic, options))
    log.info("turns=%s cost_usd=%s", stats["turns"], stats["cost_usd"])

    if report is None:
        sys.exit("No structured report was returned. See the log above for the error.")
    print("\nReport\n" + json.dumps(report, indent=2))
    sys.exit(0 if verify(report, stats) else 1)


if __name__ == "__main__":
    main()
