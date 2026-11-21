# Cheat Sheet — 4.2 Few-Shot Prompting

## Rule
Inconsistent output → **add few-shot examples**, not more instructions, not confidence thresholds, not temperature.

## Three triggers
1. Inconsistent **formatting** (list vs table vs prose)
2. Inconsistent **judgement calls** on ambiguous cases
3. **Missed extraction** — data in narrative text returned as null

## Construction
- **2–4** targeted examples (exam). Docs now say 3–5.
- Each shows **reasoning** — *why* this choice over alternatives → teaches the principle, not literal pattern-matching.
- Vary document structures (inline citations vs bibliography, narrative vs table) → less hallucination.

## Problem → technique (memorise)
| Problem | Technique |
|---|---|
| Inconsistent formatting | Few-shot examples |
| Malformed JSON | `tool_use` + JSON schema |
| Fabricated values for missing fields | Optional / nullable fields |
| Wrong tool selected | Better tool descriptions **first**, then few-shot |
| Misses info in narrative text | Few-shot showing narrative extraction |
| Line items ≠ total | Validation-retry loop |

## Wrong answers
"Add more detailed instructions"; dozens of examples; examples without reasoning; confidence thresholds.
