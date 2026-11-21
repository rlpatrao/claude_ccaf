# Cheat Sheet — 5.4 Codebase Exploration & Context Degradation

## Symptom
Long session → agent talks about "typical patterns" instead of the specific classes/paths it found. **Not a token-limit problem** — verbose discovery output buries earlier findings. Bigger context window doesn't help.

## Mitigations
| Technique | Purpose |
|---|---|
| **Scratchpad file** (primary) | Write key findings (classes, paths, dependency chains) to a file; re-read before each step. Use from the start. |
| **Subagent delegation** | Isolate verbose investigation; main benefit = **context isolation**, not just parallelism |
| **Summary injection between phases** | Summarise Phase 1 → inject into Phase 2 subagents' initial context (they don't inherit history) |
| **`/compact`** | Use **proactively**; add focus text (`/compact keep the pricing call chain`); critical facts still go in scratchpad |
| **State manifests** | Export explored paths, findings, next steps; coordinator loads + injects on resume (crash recovery) |

Current Claude Code can resume subagents with full history; exam answer = **state manifest**.

## Wrong answers
Bigger context window; restarting without saving state; giving subagents the full transcript; `/compact` only at the limit; main agent doing all exploration.
