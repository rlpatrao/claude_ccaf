import asyncio
import json
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition
from claude_agent_sdk import (
    query, AssistantMessage, UserMessage, ResultMessage,
    TextBlock, ToolUseBlock, ToolResultBlock,
)

options = ClaudeAgentOptions(
    allowed_tools=["Task","WebSearch", "WebFetch"],              # coordinator must have Task to spawn subagents
    agents={
        "web-researcher": AgentDefinition(
            description="Searches the web and returns cited findings.",
            prompt="You are a research specialist. Return concise, sourced results.",
            tools=["WebSearch", "WebFetch"],
        ),
        "doc-analyzer": AgentDefinition(
            description="Analyzes documents and extracts key points.",
            prompt="You extract structured findings from documents.",
            tools=["Read", "Grep"],
        ),
    },
    system_prompt=(
        "You are a coordinator. When subtasks are independent, "
        "issue ALL Task calls in a single response so they run in parallel."
    ),
)

def pp(msg):
    if isinstance(msg, (AssistantMessage, UserMessage)):
        role = "assistant" if isinstance(msg, AssistantMessage) else "user"
        blocks = msg.content if isinstance(msg.content, list) else [TextBlock(text=msg.content)]
        out = []
        for b in blocks:
            if isinstance(b, TextBlock):
                out.append({"type": "text", "text": b.text})
            elif isinstance(b, ToolUseBlock):
                out.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
            elif isinstance(b, ToolResultBlock):
                out.append({"type": "tool_result", "tool_use_id": b.tool_use_id,
                            "content": str(b.content)[:200]})   # truncate long results
        print(json.dumps({"role": role, "content": out}, indent=2))
    elif isinstance(msg, ResultMessage):
        print(f"--- done | turns={msg.num_turns} cost=${msg.total_cost_usd}")


async def main():
    async for msg in query(prompt="Brief me on the AI governance market.", options=options):
        print("---"*20)
        pp(msg)
asyncio.run(main())