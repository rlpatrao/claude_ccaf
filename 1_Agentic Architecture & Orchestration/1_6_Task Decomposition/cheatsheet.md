# Cheat Sheet — 1.6 Task Decomposition Strategies

## Two patterns
| Pattern | How | Best for | Trade-off |
|---|---|---|---|
| **Fixed sequential pipeline** (prompt chaining) | Predetermined steps, each feeds the next | Known, structured tasks: code review, doc processing, extraction | Reliable, debuggable; can't adapt |
| **Dynamic adaptive decomposition** | Subtasks generated from what each step finds | Open-ended: legacy exploration, debugging unknown systems, security audits | Adaptive; less predictable |

Match the pattern to the **task**, not to what sounds sophisticated.

## Attention dilution
- Too many items in one pass → inconsistent depth.
- Symptoms: early files detailed, late files shallow; same pattern flagged in one file, approved in another; obvious bugs missed.
- It's **structural** — bigger model/context/prompt doesn't fix it.

## Fix: multi-pass architecture
- **Per-item local passes** (full attention each) → catch local bugs
- **+ one cross-item integration pass** → data flow, pattern consistency
- 14-file review → 14 per-file passes + 1 integration pass.

## Wrong answers
- Bigger model / context window / more detailed prompt for dilution
- Batching **without** an integration pass
- Fixed pipeline for open-ended work; dynamic for structured work
