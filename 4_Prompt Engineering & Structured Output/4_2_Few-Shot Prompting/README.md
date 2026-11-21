# 4.2 Few-Shot Prompting

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Apply few-shot prompting to improve output consistency and quality.

## Learning objectives

- Select examples that target ambiguous cases.
- Measure consistency across runs.

## Concepts to study

- Few-shot examples are the most effective technique for consistent formatting and for handling ambiguous cases.
- Use two to four targeted examples that cover ambiguous cases, including the reasoning for the chosen action.
- For extraction, show examples across varied document formats (inline citations versus a bibliography, for example).
- Wrap examples in XML tags. Avoid examples so uniform that the model copies surface features.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A support-ticket classifier (category and priority) evaluated on 30 tickets that you label, eight of them deliberately ambiguous.

**Steps**

1. Run zero-shot. Measure accuracy overall and on the ambiguous subset.
2. Add three examples that target the ambiguous cases, each with reasoning. Measure again.
3. Run each version three times and measure run-to-run consistency.

**Done when**

- [ ] Accuracy and consistency, before and after, are recorded.

## Exam traps

- Adding more prose instructions when inconsistency is the problem.
- Choosing examples that cover only easy cases.

## Self-check questions

1. Classification of borderline tickets varies between runs. What is the most effective change?
2. What should each few-shot example include besides input and output?
3. What is the risk of near-identical examples?

## Working with Claude on this module

- `start 4.2`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.2 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.2`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
