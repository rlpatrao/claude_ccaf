# 1.6 Task Decomposition Strategies

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Design task decomposition strategies for complex workflows.

## Learning objectives

- Compare fixed prompt chaining with dynamic, adaptive decomposition.
- Select a strategy based on how predictable the task is.

## Concepts to study

- Prompt chaining: a fixed sequence of focused steps. It is predictable and testable, and suits processes with known stages.
- Dynamic decomposition: the model generates subtasks based on intermediate findings. It suits open-ended investigation.
- Per-file passes followed by a cross-file integration pass avoid attention dilution in large reviews.
- Programmatic gate checks between chain steps.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Two implementations that process the same input set of five source files or five documents.

**Steps**

1. Fixed chain: per-file analysis, then cross-file integration analysis, then a summary.
2. Dynamic: give the model a goal such as 'find why test X fails' and let it plan, investigate, and re-plan.
3. Run each version three times. Compare token cost, run-to-run consistency, and coverage.
4. Write a short comparison in your notes stating which tasks suit which strategy.

**Done when**

- [ ] Both implementations run end to end.
- [ ] Your notes contain measured results, not impressions.

## Exam traps

- Reviewing 20 files in a single pass and expecting consistent depth.
- Using dynamic decomposition for a stable, well-defined process.

## Self-check questions

1. A weekly compliance review always follows the same five checks. Which strategy fits, and why?
2. What is attention dilution, and how does a multi-pass design address it?
3. Give an example task where a fixed chain would fail.

## Working with Claude on this module

- `start 1.6`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.6 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.6`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
