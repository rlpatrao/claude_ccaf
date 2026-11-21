# 3.1 CLAUDE.md Hierarchy and Scoping

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organisation.

## Learning objectives

- Place instructions at the correct level.
- Diagnose why an instruction does or does not apply.
- Split large instruction files with imports.

## Concepts to study

- Levels: user (`~/.claude/CLAUDE.md`, personal, not shared through git), project (`./CLAUDE.md` or `./.claude/CLAUDE.md`, shared), subdirectory (loaded when Claude works in that directory), and organisation-managed policy.
- Personal project-specific overrides: check the current documentation for `CLAUDE.local.md` support versus imports from your home directory.
- `@path/to/file` imports keep CLAUDE.md modular.
- `/memory` shows which memory files are loaded; `/init` bootstraps a project CLAUDE.md.
- Common diagnosis: a new teammate does not receive an instruction because it was written in a user-level file.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A CLAUDE.md hierarchy in a small project of your own.

**Steps**

1. Write a project CLAUDE.md with build and test commands and coding conventions.
2. Add one instruction only to your user-level file. Use `/memory` to confirm which files load.
3. Add a subdirectory CLAUDE.md under `api/` and confirm it applies only when working in that directory.
4. Move a long section into `docs/conventions.md` and import it with `@docs/conventions.md`.
5. Read the root CLAUDE.md of this study workspace and identify which level it is and what it controls.

**Done when**

- [ ] You can predict which instructions load for a given working directory.
- [ ] No team-wide standard lives only in a user-level file.

## Exam traps

- Placing team standards in `~/.claude/CLAUDE.md`.
- One monolithic CLAUDE.md covering unrelated areas of the codebase.

## Self-check questions

1. A new hire's Claude Code session ignores the team's commit-message convention. Most likely cause?
2. When should a convention go in a subdirectory CLAUDE.md?
3. What does `@` import syntax provide?

## Working with Claude on this module

- `start 3.1`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.1 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.1`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
