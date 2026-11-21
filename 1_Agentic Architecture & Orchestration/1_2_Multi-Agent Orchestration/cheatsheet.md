# Cheat Sheet — 1.2 Multi-Agent Orchestration

## Hub-and-spoke
- Coordinator at centre; subagents are spokes. **All** traffic goes through the coordinator.
- Benefits: **observability**, **consistent error handling**, **controlled information flow**.

## Isolation principle (most-tested)
- Subagents do **not** inherit coordinator history, system prompt or other subagents' results.
- No memory between invocations — pass everything explicitly in the prompt.
- Current Claude Code has **forks** (copy coordinator conversation; default since v2.1.302) — exam still tests the isolation rule.

## Coordinator responsibilities
1. **Dynamic selection** — invoke only the subagents a query needs
2. **Scope partitioning** — distinct subtopics, minimal overlap
3. **Iterative refinement** — check gaps, re-delegate
4. **Central routing** — logging + error handling

## Failure tracing
- Coverage gap (e.g. only solar + wind) → root cause is **coordinator decomposition**, not subagents.
- Fix = better decomposition, not more subagents.

## Wrong answers
- Direct subagent-to-subagent messaging "for efficiency"
- Assuming shared memory/context
- Running the full pipeline for every query (even with caching)
- Blaming subagents for narrow scope
- Confusing fork (subagent) with `fork_session` (1.3) or skill `context: fork` (3.2)
