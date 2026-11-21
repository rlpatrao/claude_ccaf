"""Lab 1.1: command-line agent with a hand-written agentic loop.

Uses the Anthropic Python SDK directly, with no agent framework, so that every
step of the loop (stop_reason check, tool execution, tool_result) is visible.

Usage:
    python agent.py "What's the weather in Paris in Fahrenheit?"   # single question
    python agent.py                                                # interactive mode
"""

import json
import logging
import os
import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv

from tools import TOOLS, convert_units, get_weather

# .env lives at the repository root, two levels above this lab folder.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

MAX_TOKENS = 1024
# Safety net only. The loop normally ends when stop_reason == "end_turn".
MAX_ITERATIONS = 10

SYSTEM_PROMPT = (
    "You answer questions about weather and unit conversion using the provided tools. "
    "If a tool returns an error, read the error message and either retry with corrected "
    "input or explain the limitation to the user."
)

# Dispatch table: tool name (as sent by Claude) -> Python function.
DISPATCH = {
    "get_weather": get_weather,
    "convert_units": convert_units,
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("agent")


def make_client():
    """Return (client, model_id).

    Amazon Bedrock is used when AWS_BEDROCK_MODEL_ID is set; requests are signed with
    the AWS profile and region from AWS_PROFILE / AWS_REGION (requires boto3:
    pip install "anthropic[bedrock]"). Otherwise the Anthropic API is used with
    ANTHROPIC_API_KEY. The client exposes the same messages.create() in both cases,
    so the agent loop does not change.
    """
    bedrock_model = os.getenv("AWS_BEDROCK_MODEL_ID")
    if bedrock_model:
        client = anthropic.AnthropicBedrock(
            aws_region=os.getenv("AWS_REGION"),
            aws_profile=os.getenv("AWS_PROFILE"),
        )
        log.info("provider=bedrock region=%s profile=%s model=%s",
                 os.getenv("AWS_REGION"), os.getenv("AWS_PROFILE"), bedrock_model)
        return client, bedrock_model

    if os.getenv("ANTHROPIC_API_KEY"):
        model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5")
        log.info("provider=anthropic model=%s", model)
        return anthropic.Anthropic(), model

    sys.exit(
        "No credentials configured. Set AWS_BEDROCK_MODEL_ID (with AWS_REGION and "
        "AWS_PROFILE) or ANTHROPIC_API_KEY in the .env file at the repository root."
    )


def run_tool(block):
    """Execute one tool_use block and return the matching tool_result block."""
    if block.name not in DISPATCH:
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": f"Unknown tool: {block.name}",
            "is_error": True,
        }
    try:
        output = DISPATCH[block.name](**block.input)
        # tool_result content must be a string (or content blocks), so serialise dicts.
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": json.dumps(output),
        }
    except Exception as exc:  # any tool failure is reported back to Claude, not raised
        log.warning("tool %s failed: %s", block.name, exc)
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": str(exc),
            "is_error": True,
        }


def final_text(response):
    """Join all text blocks in a response."""
    return "".join(block.text for block in response.content if block.type == "text")


def run_agent(client, model, messages):
    """Run the agentic loop until Claude ends its turn. Mutates `messages` in place."""
    for iteration in range(1, MAX_ITERATIONS + 1):
        response = client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        # print(response.content)  # for debugging, not logged
        print(block for block in response.content)  # for debugging, not logged

        tool_calls = [block for block in response.content if block.type == "tool_use"]
        log.info(
            "iteration %d: stop_reason=%s tool_calls=%s",
            iteration,
            response.stop_reason,
            [(block.name, block.input) for block in tool_calls],
        )

        # Append the full assistant turn (text and tool_use blocks) before any tool results.
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            return final_text(response)

        if response.stop_reason == "tool_use":
            # Every tool_use block gets a tool_result, all in ONE user message.
            results = [run_tool(block) for block in tool_calls]
            messages.append({"role": "user", "content": results})
            continue

        # max_tokens, refusal, or anything else: stop and report rather than loop.
        log.error("stopping: stop_reason=%s", response.stop_reason)
        return final_text(response) + f"\n[stopped: stop_reason={response.stop_reason}]"

    log.warning("iteration cap of %d reached without end_turn", MAX_ITERATIONS)
    return None


def main():
    client, model = make_client()

    if len(sys.argv) > 1:
        messages = [{"role": "user", "content": " ".join(sys.argv[1:])}]
        print(run_agent(client, model, messages) or "[no final answer]")
        return

    # Interactive mode: history is kept so follow-up questions have context.
    messages = []
    print("Interactive mode. Type 'exit' to quit.")
    while True:
        try:
            question = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        messages.append({"role": "user", "content": question})
        print(run_agent(client, model, messages) or "[no final answer]")


if __name__ == "__main__":
    main()
