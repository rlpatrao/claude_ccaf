# Cheat Sheet — 1.4 Workflow Enforcement and Handoff

## Enforcement spectrum
| Approach | Nature | Use for |
|---|---|---|
| Prompt guidance (system prompt, few-shot) | Probabilistic — non-zero failure | Low stakes: formatting, style |
| Programmatic enforcement (hooks, prerequisite gates, code checks) | Deterministic — 100% | **Money, security, compliance** |

## Decision rule
Refunds/transfers/payments, identity/access, AML/regulatory → **always programmatic**.

## Prerequisite gate
- Code blocks a tool until a condition is met — e.g. `process_refund` blocked until `get_customer` returns a verified ID.
- Model cannot bypass it.

## Multi-concern requests
Decompose → investigate items **in parallel** with shared context → **one unified** resolution.

## Structured handoff (human escalation)
Human has **no transcript**. Must include: **customer ID, conversation summary, root cause analysis, refund amount (if any), recommended action**.

## Wrong answers
- "Stronger system prompt" / "add few-shot examples" for high-stakes failures (e.g. 8% skipped verification)
- Routing classifier to fix an in-agent compliance issue (routing ≠ execution sequence)
- Handling concerns one at a time across replies
- Handoffs missing required fields
