# 1.7 Session State, Resumption, and Forking

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Manage session state, resumption, and forking.

## Learning objectives

- Resume sessions in Claude Code and in the Agent SDK.
- Fork a session to explore alternative approaches.
- Decide when to resume and when to start fresh with a summary.

## Concepts to study

- Claude Code CLI: `claude --continue`, `claude --resume`, `--fork-session`, and `/resume` inside a session.
- Agent SDK: capture `session_id` from the init message, pass it as `resume`, and set `fork_session` to branch.
- Stale context: after files change, a resumed session still holds old tool results. Tell it what changed, or start fresh with a structured summary.
- Name sessions so they can be found later.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Session exercises in a sample repository and an Agent SDK script that persists its session ID.

**Steps**

1. In Claude Code, start an exploration session in a sample repository, exit, and resume it with `--resume`.
2. Fork from the same point and try two different refactoring approaches.
3. In the Agent SDK, persist `session_id` to a file and resume from it in a second run.
4. Modify a file between sessions. Record whether the resumed session notices, and what you had to tell it.

**Done when**

- [ ] You can resume and fork in both Claude Code and the Agent SDK.
- [ ] Your notes describe when resuming was harmful because of stale context.

## Exam traps

- Resuming a session with stale tool results and not informing Claude what changed.
- Confusing forking (a new branch from a point) with continuing (the same thread).

## Self-check questions

1. You want to compare two refactoring strategies from the same analysis. Which feature do you use?
2. Three days and many commits have passed since a session. Resume it or start fresh? Justify.
3. Where does the Agent SDK expose the session ID?

## Working with Claude on this module

- `start 1.7`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.7 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.7`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
