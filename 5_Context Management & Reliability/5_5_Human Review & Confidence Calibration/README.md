# 5.5 Human Review and Confidence Calibration

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Design human review workflows and calibrate confidence.

## Learning objectives

- Evaluate accuracy at the right granularity.
- Route the right items to human reviewers.

## Concepts to study

- Aggregate accuracy (for example 97%) can hide poor accuracy for particular document types or fields. Measure by type and by field before reducing human review.
- Use stratified random sampling of high-confidence output for ongoing verification.
- Field-level confidence must be calibrated against a labelled validation set.
- Route low-confidence or conflicting items to reviewers and prioritise limited reviewer capacity.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Extend the extractor from labs 4.3 and 4.4 with field-level confidence.

**Steps**

1. Label 30 documents across three document types.
2. Compute accuracy per document type and per field.
3. Calibrate a confidence threshold against your labels.
4. Write a sampling plan for ongoing verification of high-confidence output.

**Done when**

- [ ] Accuracy by type and field is recorded.
- [ ] A calibrated threshold and a sampling plan are documented.

## Exam traps

- Automating based on overall accuracy alone.
- Trusting uncalibrated self-reported confidence.

## Self-check questions

1. Overall accuracy is 97%, but handwritten forms are 70%. What should you do before removing human review?
2. What is stratified sampling, and why use it here?
3. How do you calibrate a confidence score?

## Working with Claude on this module

- `start 5.5`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.5 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.5`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
