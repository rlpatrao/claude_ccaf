# 3.5 Iterative Refinement

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Apply iterative refinement techniques for progressive improvement.

## Learning objectives

- Use concrete examples, tests, and interviews to converge on correct output.

## Concepts to study

- Concrete input and output examples are more reliable than prose when results are inconsistent.
- Test-driven iteration: write tests first, have Claude iterate until they pass, and share failures verbatim.
- Interview pattern: ask Claude to question you about requirements before it implements anything.
- Report interacting issues together in one message; report independent issues sequentially.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Refinement exercises on a small data-transformation function.

**Steps**

1. Describe a data transformation in prose only. Record mismatches in the result.
2. Provide three input and output examples instead. Compare.
3. Write failing tests yourself and ask Claude to make them pass without changing the tests.
4. Use the interview pattern for a small new feature.

**Done when**

- [ ] Your notes compare the three techniques with concrete observations.

## Exam traps

- Repeating the same prose request with more emphasis instead of supplying examples.
- Allowing tests to be modified to make them pass.

## Self-check questions

1. Output formatting varies between runs despite detailed prose instructions. What is the most effective next step?
2. When should related issues be reported in one message?
3. What does the interview pattern prevent?

## Working with Claude on this module

- `start 3.5`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.5 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.5`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
