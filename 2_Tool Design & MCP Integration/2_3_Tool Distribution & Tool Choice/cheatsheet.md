# Cheat Sheet — 2.3 Tool Distribution & Tool Choice

## Tool count
- 18 tools on one agent → unreliable selection. Guide: **4–5 per agent**, scoped to role. (Docs now: degrades past 30–50; exam uses 18 vs 4–5.)
- Agents with out-of-role tools misuse them.

## Oversized toolkit: split or consolidate
| Situation | Fix |
|---|---|
| Genuinely different jobs | **Split** across role-scoped agents |
| Variants of one job | **Consolidate** into a parameterised tool (19 transforms → `transform_data(operation)`) |
| Never | Move tools to a second MCP server — model still sees one combined list |

## tool_choice
| Mode | Behaviour | Use for |
|---|---|---|
| `"auto"` (default) | Tool or text | General operation |
| `"any"` | Must call *some* tool | Guaranteed structured output, multiple schemas |
| `{type:"tool", name:X}` | Must call X | Mandatory first step |

Note: newer models reject `any`/forced (400) → docs say `auto` + strict tool use. Exam still tests all three.

## Scoped cross-role tools
- Coordinator round trip = 2–3 hops, up to **40% latency**.
- Give synthesis agent scoped `verify_fact` for the **85%** simple lookups; **15%** complex still via coordinator.

## Least privilege
`fetch_url` (anything) → `load_document` (validated doc URLs only).

## Reference distribution
Web search: `search_web, fetch_page, extract_links, save_snippet` · Doc analysis: `extract_metadata, extract_data_points, summarize_content, verify_claim` · Synthesis: `compile_report, verify_fact (scoped), format_citation, assess_coverage` · Coordinator: `Task, review_output, request_revision`.

## Wrong answers
Sharper descriptions for a too-large set; everything via coordinator; generic tools; `auto` when structured output required.
