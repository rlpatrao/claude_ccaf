# 3.2 Slash Commands and Skills

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Create and configure custom slash commands and skills.

## Learning objectives

- Create project and personal commands.
- Author skills with appropriate frontmatter.
- Choose between CLAUDE.md, a command, and a skill.

## Concepts to study

- Commands: `.claude/commands/<name>.md` (project, shared) and `~/.claude/commands/` (personal). Arguments through `$ARGUMENTS`, `$1`, and so on.
- Skills: `.claude/skills/<name>/SKILL.md` with frontmatter such as `name`, `description` (drives automatic invocation), `allowed-tools`, `argument-hint`, `context: fork` (runs in an isolated subagent context), and `disable-model-invocation`.
- Skills can bundle supporting files such as templates and reference documents.
- CLAUDE.md is always loaded. A skill is loaded on demand, so long, occasional procedures belong in skills.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A command and a skill in a scratch repository.

**Steps**

1. Create a project `/review` command that accepts a file path argument.
2. Convert it into a skill with `allowed-tools` limited to Read, Grep, and Glob, and with `context: fork`.
3. Write a personal skill in `~/.claude/skills/`.
4. Compare main-session context usage with `/context` with and without `context: fork`.

**Done when**

- [ ] The command works with arguments.
- [ ] The forked skill leaves the main context smaller than the non-forked version.

## Exam traps

- Putting a team command in `~/.claude/commands/`.
- Putting a long, rarely used procedure in CLAUDE.md instead of a skill.

## Self-check questions

1. A verbose codebase-analysis skill fills the main session context. Which frontmatter setting addresses this?
2. Where should a command live so every teammate gets it on clone?
3. What decides whether Claude invokes a skill automatically?

## Working with Claude on this module

- `start 3.2`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.2 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.2`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
