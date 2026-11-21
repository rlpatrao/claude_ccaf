# Cheat Sheet — 3.4 Plan Mode vs Direct Execution

## Decide on **ambiguity**, not difficulty
| Mode | When | Examples |
|---|---|---|
| **Plan** | Multiple valid approaches, architecture, many files | Monolith → microservices; library migration across 30–45+ files; choosing integration approach |
| **Direct** | Clear scope, known fix | Single-file bug with clear stack trace; add a validation conditional |

Plan mode = read and analyse, **no file changes**.

## Hybrid (common exam answer)
**Plan THEN direct** — investigate & design, then implement. Not plan *or* direct.

## Explore subagent
Runs verbose discovery in isolation, returns **summaries** → protects main context window.

## Upfront recognition
Complexity stated in requirements → **plan from the start**. "Start direct, switch if it gets hard" is wrong.

## Wrong answers
- Direct execution for multi-file architectural change
- Plan mode for a clear one-line fix
- Verbose discovery in main conversation
- Late switch to plan when complexity was known
