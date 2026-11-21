# 3.3 Path-Specific Rules

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Apply path-specific rules for conditional loading of conventions.

## Learning objectives

- Write rules that load only for matching files.
- Choose between path rules and subdirectory CLAUDE.md files.

## Concepts to study

- `.claude/rules/*.md` files with YAML frontmatter `paths:` containing glob patterns load only when Claude works with matching files.
- Rules without `paths` load unconditionally.
- Path rules suit conventions that cut across directories, such as test files spread throughout the tree. Subdirectory CLAUDE.md suits conventions bound to one directory.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Two path-scoped rules in a scratch repository.

**Steps**

1. Create one rule for `**/*.test.*` (test conventions) and one for `src/api/**/*.py`.
2. Ask Claude to edit test files in two different directories and confirm the test rule applies to both.
3. Edit a file that matches neither pattern and confirm neither rule is loaded.

**Done when**

- [ ] Rules load only for matching files.
- [ ] Your notes explain when you would use each mechanism.

## Exam traps

- Using subdirectory CLAUDE.md files for conventions that apply to files scattered across many directories.

## Self-check questions

1. Test conventions apply to `*.test.ts` files in 30 directories. Which mechanism fits?
2. What happens to a rule file with no `paths` frontmatter?
3. Write a glob that matches every Terraform file in the repository.

## Working with Claude on this module

- `start 3.3`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.3 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.3`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
