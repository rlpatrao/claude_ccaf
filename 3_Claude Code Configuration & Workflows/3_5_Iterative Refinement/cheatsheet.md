# Cheat Sheet — 3.5 Iterative Refinement Techniques

## Situation → technique
| Situation | Technique |
|---|---|
| Prose interpreted differently each time | **2–3 concrete input/output examples** |
| Complex transformation, many edge cases | **Test-driven iteration** (tests first, share failures) |
| Unfamiliar domain | **Interview pattern** (Claude asks questions first) |
| Issues that affect each other | **Batch** — one message |
| Independent issues | **Sequential** feedback |

## Key points
- Examples beat "more precise prose" — model generalises from examples.
- Test failures = unambiguous feedback ("Expected X, got Y").
- Interview pattern ≠ examples: interview finds **unknown considerations**; examples fix a **known transformation being misread**.

## Scenario
Error-response shape + logging format (interdependent) → one message. Naming convention (independent) → separately.

## Wrong answers
Rewriting prose more carefully; interview pattern when you know the exact transform; sending interacting fixes one at a time; batching unrelated fixes.
