# Cheat Sheet — 1.7 Session State and Resumption

## Three options
| Option | What it does | Use when |
|---|---|---|
| `--resume <name>` | Restores history (compacted sessions from last summary) | Context still valid, files unchanged |
| `fork_session` | Independent branches from a shared baseline | Comparing divergent approaches |
| **Fresh start + summary injection** | New session seeded with structured summary; no stale tool results | Files changed, APIs updated, long cluttered session |

## Stale context problem
Resuming after edits keeps **old tool results** in history → contradictory advice (suggests changes already made, cites deleted code).

## Targeted re-analysis
3 of 50 files changed → re-analyse **only those 3**; the summary covers the rest. Never full re-exploration.

## Decision matrix
- No changes, continuing → **resume**
- Two strategies to compare → **fork**
- Files modified / degraded history → **fresh + summary**

## Wrong answers
- Resume + "re-read the changed files" when most reasoning is stale (stale results still in history)
- `fork_session` to fix stale context (fork inherits it)
- `fork_session` to continue one line of work
- Full codebase re-read
