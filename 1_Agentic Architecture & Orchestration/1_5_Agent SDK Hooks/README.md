# 1.5 Agent SDK Hooks

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Apply Agent SDK hooks for tool call interception and data normalisation.

## Learning objectives

- Use PreToolUse hooks to block or modify tool calls.
- Use PostToolUse hooks to normalise tool output before the model sees it.
- Choose hooks over prompt instructions when behaviour must be deterministic.

## Concepts to study

- Hook events include PreToolUse, PostToolUse, UserPromptSubmit, Stop, SubagentStop, PreCompact, and SessionStart. Confirm the current list in the Agent SDK documentation.
- Matchers select which tools a hook applies to.
- PreToolUse can allow, deny with a reason that is returned to Claude, or ask for confirmation.
- PostToolUse can normalise heterogeneous formats (Unix timestamps versus ISO 8601, numeric status codes versus labels) and trim verbose output.
- Claude Code supports the same events as shell-command hooks configured in `settings.json`.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Add hooks to the support agent from lab 1.4.

**Steps**

1. PreToolUse: deny `process_refund` when the amount exceeds 500 and return a reason that directs Claude to escalate.
2. PostToolUse: normalise dates from three stub data sources (ISO string, Unix epoch, 'MM/DD/YYYY') to ISO 8601.
3. PostToolUse: reduce a 40-field order record to the five fields the task needs.
4. In a throwaway repository, configure a Claude Code PreToolUse hook in `.claude/settings.json` that blocks Bash commands containing `rm -rf`.

**Done when**

- [ ] Refunds above the limit never execute, and Claude receives the reason.
- [ ] Claude only ever sees normalised dates.
- [ ] The Claude Code hook blocks the dangerous command and allows ordinary commands.

## Exam traps

- Using a prompt instruction for a policy that must never be violated.
- Telling the model 'dates may be in different formats' instead of normalising in code.

## Self-check questions

1. Which hook event enforces a refund ceiling, and why not PostToolUse?
2. Three backends return timestamps in different formats. Where should normalisation happen?
3. What happens to the deny reason returned by a PreToolUse hook?

## Working with Claude on this module

- `start 1.5`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.5 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.5`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
