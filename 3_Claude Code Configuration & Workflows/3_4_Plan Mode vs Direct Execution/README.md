# 3.4 Plan Mode versus Direct Execution

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Determine when to use plan mode versus direct execution.

## Learning objectives

- Select plan mode or direct execution for a given task.
- Combine planning and execution.

## Concepts to study

- Plan mode performs read-only exploration and proposes a plan before any edit. Use it for multi-file changes, architectural decisions, unfamiliar code, and tasks with several valid approaches.
- Direct execution suits well-scoped changes with a clear fix, such as a stack trace that points to one line.
- Toggle with Shift+Tab, or start with `--permission-mode plan`.
- The Explore subagent keeps verbose discovery out of the main context.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A set of tasks of different scope in a sample repository.

**Steps**

1. Pick four tasks: a typo fix, adding validation to one function, migrating a logging library across the repository, and restructuring a module.
2. Predict plan mode or direct execution for each and write down why.
3. Execute each task and record rework, surprises, and context usage.
4. Compare outcomes with your predictions.

**Done when**

- [ ] Your predictions and outcomes are recorded side by side.

## Exam traps

- Using plan mode for a one-line fix.
- Using direct execution for a change that spans dozens of files.

## Self-check questions

1. A migration touches 45 files and there are two candidate approaches. Which mode, and why?
2. A failing test's traceback points to a missing null check. Which mode?
3. How does the Explore subagent help during planning?

## Working with Claude on this module

- `start 3.4`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.4 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.4`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
