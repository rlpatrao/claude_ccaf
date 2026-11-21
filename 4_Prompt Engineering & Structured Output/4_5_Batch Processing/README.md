# 4.5 Batch Processing

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Design efficient batch processing strategies.

## Learning objectives

- Decide when the Message Batches API is appropriate.
- Correlate results and handle partial failures.

## Concepts to study

- The Message Batches API costs roughly 50% less than synchronous calls, is asynchronous, and can take up to 24 hours. It has no latency guarantee.
- `custom_id` correlates requests with results; results can arrive in any order.
- Suitable for overnight reports, weekly audits, and bulk extraction. Not suitable for blocking workflows such as pre-merge checks.
- Each batch request is a single Messages call. A multi-turn tool loop does not run inside a batch.
- Resubmit only the failed `custom_id` values, modified if needed (for example, chunking an oversized document).
- Refine the prompt on a small synchronous sample before submitting a large batch.
- Schedule submissions against an SLA: with a 30-hour SLA and up to 24 hours of processing, submit at least every 6 hours.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A batch run of your lab 4.3 extractor over 50 synthetic documents.

**Steps**

1. Create a batch with meaningful `custom_id` values.
2. Poll the batch status and download results when complete.
3. Map results back to inputs by `custom_id`.
4. Include one invalid request deliberately; resubmit only the failure.
5. Compare cost and wall-clock time with synchronous processing.

**Done when**

- [ ] All 50 results are mapped to their inputs.
- [ ] Only failed items were resubmitted.

## Exam traps

- Using batches for a check that blocks a developer.
- Assuming results return in submission order.

## Self-check questions

1. A team wants pre-merge review on every pull request at half the cost. Is the Batches API appropriate? Why?
2. How do you identify which input a batch result belongs to?
3. An SLA is 36 hours. What is the maximum interval between batch submissions?

## Working with Claude on this module

- `start 4.5`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.5 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.5`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
