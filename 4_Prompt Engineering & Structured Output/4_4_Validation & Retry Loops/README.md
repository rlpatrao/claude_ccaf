# 4.4 Validation, Retry, and Feedback Loops

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Implement validation, retry, and feedback loops for extraction quality.

## Learning objectives

- Validate output semantically in code.
- Retry with specific feedback.
- Recognise when retries cannot help.

## Concepts to study

- Validate in code (line items sum to the total, dates are in a valid range), then retry with the original document, the failed output, and the exact validation error.
- Retries fix format and consistency errors. They do not help when the information is not in the source.
- Self-check fields: ask for `calculated_total` alongside `stated_total` so discrepancies are explicit.
- Track recurring failure patterns to find prompt or schema defects.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Extend the extractor from lab 4.3.

**Steps**

1. Write a validator that checks line-item sums and date validity.
2. On failure, retry at most twice, including the specific error message in the retry.
3. Include one document where the required information is absent. Confirm retries do not resolve it, and route it to review instead.
4. Log retry outcomes and compute the retry success rate.

**Done when**

- [ ] Retries include the specific validation error.
- [ ] Documents with absent information stop retrying and are flagged.

## Exam traps

- Retrying with a generic 'try again'.
- Retrying indefinitely for information that is not present.

## Self-check questions

1. What three things should a retry request contain?
2. Which failure type will a retry never fix?
3. How does a `calculated_total` field help?

## Working with Claude on this module

- `start 4.4`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.4 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.4`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
