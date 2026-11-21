# Cheat Sheet — 5.3 Error Propagation in Multi-Agent Systems

## Structured error context (4 elements)
1. **Failure type** — transient / validation / business / permission
2. **What was attempted** — query, params, target system
3. **Partial results** gathered before failure
4. **Alternative approaches** the coordinator could try

## Two anti-patterns
| Anti-pattern | Why bad |
|---|---|
| **Silent suppression** — timeout returned as `{results: [], status: "success"}` | Coordinator thinks "found nothing" → never retries; worst one |
| **Workflow termination** — kill pipeline on one failure | Throws away other subagents' completed work |

Also wrong: generic "search unavailable" (hides query, partials, alternatives).

## Access failure vs valid empty
| | Access failure | Valid empty |
|---|---|---|
| Meaning | Couldn't reach source | Reached it, no matches |
| Retry? | Consider | **No — that's the answer** |

## Local recovery
Subagent retries/fallbacks transient errors **locally**; propagate only what survives, with attempts + partials.

## Coverage annotations
Say where coverage is thin ("geothermal limited — journal access unavailable") rather than silently omitting.
