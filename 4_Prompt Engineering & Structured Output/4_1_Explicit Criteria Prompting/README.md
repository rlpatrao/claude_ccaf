# 4.1 Explicit Criteria Prompting

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Design prompts with explicit criteria to improve precision and reduce false positives.

## Learning objectives

- Replace vague instructions with explicit inclusion and exclusion criteria.
- Measure precision and recall of a prompt.

## Concepts to study

- Vague instructions such as 'be conservative' or 'report only high-confidence issues' do not reliably reduce false positives.
- Explicit criteria state what to report and what not to report, by category, with examples of each.
- Categories with high false-positive rates erode trust; disable them temporarily while refining their criteria.
- Severity levels need definitions with concrete examples.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A code-review prompt evaluated against ten snippets that you label in advance: some contain real defects and some contain acceptable code that looks suspicious.

**Steps**

1. Baseline: 'Review this code for issues; be conservative.' Measure precision and recall against your labels.
2. Rewrite the prompt with explicit report and do-not-report criteria. Measure again.
3. Add severity definitions with one example per level. Measure again.

**Done when**

- [ ] A table of precision and recall for each prompt version is in your notes.

## Exam traps

- Choosing 'ask the model to report only high-confidence findings' over explicit criteria.
- Adding a numeric confidence threshold based on the model's self-reported confidence.

## Self-check questions

1. Developers ignore review comments because many are style nitpicks. What prompt change addresses this most directly?
2. Why does 'be conservative' fail to improve precision?
3. What should a severity definition contain?

## Working with Claude on this module

- `start 4.1`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.1 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.1`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
