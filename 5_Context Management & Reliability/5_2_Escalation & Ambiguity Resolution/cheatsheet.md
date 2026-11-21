# Cheat Sheet — 5.2 Escalation & Ambiguity Resolution

## Valid escalation triggers (3)
1. **Explicit human request** → escalate **immediately**, no investigation first
2. **Policy gap** (policy silent, e.g. competitor price match) → escalate. *Violation* (policy says no) → documented answer, no escalation
3. **Can't make progress** (tool errors, no access, bug)

## Unreliable triggers (2)
- **Sentiment** — frustration ≠ complexity
- **Self-reported confidence** — poorly calibrated (escalates easy cases, attempts hard ones)

## Frustration nuance
| Situation | Action |
|---|---|
| Frustrated, resolvable issue | Acknowledge + resolve |
| Re-asks for human after your offer | Escalate |
| "I want a human" from the start | Escalate now |

## Ambiguous customer match
Multiple matches → **ask for another identifier** (email, phone, order #). Never pick "most recent/active" — privacy risk.

## First fix for bad escalation
**Explicit criteria + few-shot examples** in system prompt, before classifiers or sentiment models.

## Wrong answers
Sentiment thresholds; confidence scores; investigating before honouring a human request; heuristic matching; classifier first.
