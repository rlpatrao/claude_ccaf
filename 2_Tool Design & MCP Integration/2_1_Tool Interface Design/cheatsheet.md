# Cheat Sheet — 2.1 Tool Interface Design

## Descriptions = the selection mechanism
Not metadata — **the** thing the model uses to pick a tool. A good description has 5 parts:
1. What it does
2. Inputs (formats, types, constraints)
3. Example queries it handles
4. Edge cases / limitations
5. **Boundaries** — when to use this vs similar tools

## Misrouting
- `get_customer` vs `lookup_order` with one-line descriptions → wrong tool chosen.
- Small toolkit → **expand descriptions** (low effort, high impact, fixes root cause).

## Count tools first
- Workable count, two tools confusable → descriptions.
- Too many tools (guide: 18 vs 4–5; docs now say 30–50) → **2.3 work**: split by role or consolidate into a parameterised tool.

## Other fixes
- **Splitting**: `analyze_document` → `extract_data_points`, `summarize_content`, `verify_claim_against_source`.
- **Renaming**: `analyze_content` → `extract_web_results` (+ web-specific description).
- **System prompt check**: keyword instructions ("always check customer details") can override good descriptions — review after every description change.

## Wrong first steps
| Option | Why wrong |
|---|---|
| Few-shot examples | Token overhead, treats symptoms |
| Routing classifier | Over-engineered, bypasses LLM understanding |
| Tool consolidation | Valid long-term, too much effort as first fix |

Exam bias: **low-effort, high-impact fixes first**.
