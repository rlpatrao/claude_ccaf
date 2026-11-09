# 4.6 Multi-Instance and Multi-Pass Review

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Design multi-instance and multi-pass review architectures.

## Learning objectives

- Use an independent model instance for review.
- Split large reviews into local and integration passes.

## Concepts to study

- Self-review in the same session is limited because the model retains the reasoning that produced the output.
- An independent instance without the generation context reviews more effectively.
- Multi-pass design: per-file local analysis followed by a cross-file integration pass.
- Attention dilution reduces depth when many files are reviewed in one pass.
- Per-finding confidence can route uncertain findings to human review.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A review pipeline for a six-file change that you prepare, containing at least one cross-file defect.

**Steps**

1. Review all six files in a single pass. Record the findings.
2. Run per-file passes followed by an integration pass. Compare the findings.
3. Have the generating session review its own code, then an independent instance. Compare.

**Done when**

- [ ] Your notes show which design found the cross-file defect.

## Exam traps

- Choosing 'ask the model to double-check its work in the same conversation'.

## Self-check questions

1. A 25-file pull request review misses an interface mismatch between two files. What design change helps?
2. Why is an independent reviewer instance more effective than self-review?
3. What is the purpose of the integration pass?

## Working with Claude on this module

- `start 4.6`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.6 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.6`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
