# Cheat Sheet — 4.4 Validation, Retry, and Feedback Loops

## Retry with error feedback
Send back **3 things**: original document + failed extraction + **specific validation error** (e.g. "line items sum to £450, stated total £500"). Naive retries repeat the mistake.

## Retry boundary (most tested)
| Retry works | Retry doesn't |
|---|---|
| Format mismatch, structural errors, misplaced values, maths (missed line items) | Info **absent** from source → human review or null |
| | Source **contradicts itself** → capture both, flag, route to review |

## Self-correction schema fields
- `calculated_total` + `stated_total` → auto-flag discrepancies
- `conflict_detected` boolean → contradictory source (net 30 vs net 60)
- `detected_pattern` → which construct triggered a finding → analyse dismissal patterns, refine prompts

## Syntax vs semantic
| Error | Fixed by |
|---|---|
| Syntax: malformed JSON, missing fields, wrong types | `tool_use` + `strict: true` |
| Semantic: wrong sums, misplaced values, fabrication | Validation logic + retry loop |

**Pydantic**: schema parsing + custom validators for cross-field rules; `ValidationError` messages feed the retry prompt. Not redundant with tool_use.

## Wrong answers
Retries without the error; retrying for missing info; picking one value when source conflicts; schema-only validation.
