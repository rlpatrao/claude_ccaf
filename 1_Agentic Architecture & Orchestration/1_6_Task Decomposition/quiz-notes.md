# Quiz Notes: 1.6 Task Decomposition Strategies

Socratic quiz session, 17 November 2026. Domain 1, Task Statement 1.6.

## 1. The two decomposition patterns

| | Fixed sequential pipeline (prompt chaining) | Dynamic adaptive decomposition |
|---|---|---|
| How it works | Predetermined steps executed in order; each step takes the previous step's output. | Subtasks are generated from what is discovered at each step; the plan evolves. |
| Best for | Predictable, structured tasks where the steps are known in advance. | Open-ended investigation with unknown scope. |
| Examples | Multi-file code review, document processing, data extraction. | Legacy codebase exploration, debugging an unfamiliar system, security audit. |
| Advantages | Consistent, reliable, easy to debug. | Adapts to the problem; more thorough for open-ended tasks. |
| Limitation | Cannot adapt to unexpected findings partway through execution. | Less predictable; harder to estimate time. |

Note the distinction: "unsuitable for unknown tasks" is a selection rule. The limitation of the fixed pipeline itself is that it cannot change course once a step reveals something unexpected (for example, a credit note arriving in an invoice-extraction pipeline).

## 2. Selecting the pattern

| Scenario | Pattern | Reason |
|---|---|---|
| Understanding an undocumented 15-year-old billing system | Dynamic | Scope unknown; each discovery decides where to look next. |
| Extracting fields from scanned insurance claim forms | Fixed | Same fields and steps for every form. |
| Reviewing every file in a pull request against coding standards | Fixed | Steps known in advance. Multi-file code review is the standard fixed-pipeline example. |
| Intermittent outage in a service nobody on the team built | Dynamic | Unfamiliar system, unknown cause; each finding redirects the investigation. |

Anti-patterns:
- Fixed pipeline for open-ended investigation: cannot adapt.
- Dynamic decomposition for structured tasks: adds unpredictability and cost, and produces inconsistent output across near-identical inputs (for example, the same ten fields from thousands of contracts).

## 3. Attention dilution

Cause: too many items processed in a single pass, so the model's attention is spread thinly and depth becomes inconsistent.

Symptoms:
1. Detailed feedback for early files, shallow feedback for later files.
2. The same pattern flagged in one file but approved in another.
3. Obvious bugs missed in some files.

Attention dilution is structural. The following do not fix it:
- A larger context window. Capacity was never the problem.
- A better or more emphatic prompt ("review every file equally thoroughly").

## 4. Multi-pass architecture (the fix)

1. Per-item local passes: each file is reviewed in its own pass with the full attention budget. Catches local issues consistently.
2. Cross-item integration pass: a separate pass across files for cross-cutting concerns:
   - Data flow, for example file 7 now returns `null` and file 19 uses the result without checking.
   - Pattern consistency, for example the same `forEach` code flagged in one file and approved in another.

Per-item passes alone miss cross-file relationships. Batching (for example, 5 files per batch) without an integration pass still misses relationships between files in different batches.

A PostToolUse hook (sub-module 1.5) is not a substitute for the integration pass. It processes individual tool results deterministically and does not reason across items.

## 5. Model answer: the 14-file scenario

> An agent reviews 14 files and produces detailed feedback for the first 5 but misses obvious bugs in files 10 to 14. It also flags a `forEach` loop in one file but approves identical code elsewhere.

This is attention dilution. Fourteen files in a single pass spread the model's attention too thinly, so depth is inconsistent. The symptoms match: detailed feedback for files 1 to 5, missed bugs in files 10 to 14, and the `forEach` pattern flagged in one file but approved in another. The fix is a multi-pass architecture: per-file local passes so each file gets the full attention budget, plus a cross-file integration pass to check data flow and pattern consistency. A larger context window or a more emphatic prompt would not fix it, and batching without an integration pass would still miss cross-file issues.

## 6. Assessment

Secure:
- The two patterns and when to use each.
- Scenario classification (4 of 4 correct).
- Recognising attention dilution and its inconsistency symptom.
- Why larger context or better prompts do not fix it.
- Why batching without integration fails.

Partly secure:
- The fixed pipeline's limitation (cannot adapt to unexpected findings) as distinct from the selection rule.
- Multi-pass architecture has two parts; per-file passes alone are an exam distractor.

To revise:
1. Name the integration pass's responsibilities: data flow and pattern consistency.
2. Do not offer a hook as a fix for an architectural problem.
3. State the reason with every answer; distractors often pair the right pattern with the wrong reason.
4. Use the exam guide's terms: fixed sequential pipeline / prompt chaining, dynamic adaptive decomposition, consistent, reliable, easy to debug, structural.
