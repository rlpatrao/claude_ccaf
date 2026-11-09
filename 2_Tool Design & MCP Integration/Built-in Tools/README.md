# 2.5 Built-in Tools

**Domain:** 2. Tool Design & MCP Integration
**Exam task statement:** Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively.

## Learning objectives

- Choose the correct built-in tool for a given question.
- Explore a codebase incrementally.

## Concepts to study

- Grep searches file contents (callers of a function, error strings, imports).
- Glob finds files by name or path pattern (for example `**/*.test.ts`).
- Read and Write operate on whole files. Edit performs targeted replacement and requires a unique match; fall back to Read and Write when the anchor is not unique.
- Incremental exploration: Grep for entry points, then Read selected files. Do not read every file up front.
- Bash runs tests, builds, and git commands.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** An exploration exercise in an unfamiliar open-source repository that you clone.

**Steps**

1. Ask Claude Code to find every caller of a specific function. Note which tools it uses.
2. Ask it to find all test files.
3. Request an Edit where the anchor text appears twice. Observe the failure and the recovery.
4. Write a decision table in your notes mapping question types to tools.

**Done when**

- [ ] Your decision table covers all six tools.
- [ ] You can predict which tool Claude will use for a given request.

## Exam traps

- Using Glob to search file contents.
- Reading the entire codebase before forming a hypothesis.

## Self-check questions

1. Which tool finds all files that import a module? Which finds all files named `*_test.py`?
2. Why does Edit fail, and what is the fallback?
3. Describe an incremental exploration sequence for locating a bug from an error message.

## Working with Claude on this module

- `start 2.5`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 2.5 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 2.5`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
