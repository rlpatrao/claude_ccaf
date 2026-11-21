# Cheat Sheet — 1.3 Subagent Invocation and Context Passing

## Task tool
- Coordinator's `allowedTools` **must include `"Task"`** — otherwise it cannot spawn subagents.
- Exam says "Task tool" (current code may say Agent) — answer "Task".
- `AgentDefinition` = **description** (used for selection) + **system prompt** + **tool restrictions**.

## Context passing rules
1. Pass **complete findings** from prior agents — subagents can't "look up" anything.
2. Use **structured data** separating content from metadata: `claim, source_url, document_name, page_number, confidence`.
3. Coordinator prompts state **goals + quality criteria**, not step-by-step procedures.

## Attribution failure
- Unsourced claims in synthesis output → coordinator passed content **without metadata**.
- Fix: structured context passing. **Not** the synthesis prompt, **not** giving it tool access.

## Parallel spawning
- Multiple Task calls **in a single coordinator response** = parallel. Separate turns = needless latency.
- Exam cue words: "in a single response", "simultaneously".

## Sessions
| Control | Use |
|---|---|
| `--resume` | Continue the same session |
| `fork_session` | Branch from a shared baseline to explore divergent approaches |

## Wrong answers
- Subagents auto-see coordinator history
- Sequential calls for independent tasks
- Rigid step-by-step subagent prompts
