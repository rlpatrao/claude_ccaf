# 3.6 CI/CD Integration

**Domain:** 3. Claude Code Configuration & Workflows
**Exam task statement:** Integrate Claude Code into CI/CD pipelines.

## Learning objectives

- Run Claude Code non-interactively.
- Produce machine-readable output.
- Design an independent review step.

## Concepts to study

- `-p` (`--print`) runs non-interactively. Without it, a CI job waits for input.
- `--output-format json` or `stream-json`; check the current CLI reference for schema-validated output (`--json-schema`).
- `--allowedTools`, `--max-turns`, and permission modes control unattended runs.
- The project CLAUDE.md supplies context such as test standards and review criteria to CI runs.
- A session that generated code is a weaker reviewer of that code. Use a separate invocation for review.
- Pass previous findings into re-runs to avoid duplicate comments.
- GitHub Actions integration is available through the Claude Code GitHub Action.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A pull-request review workflow in a personal test repository on GitHub.

**Steps**

1. Locally, run `claude -p` with a review prompt and `--output-format json`. Inspect the output structure.
2. Define a JSON schema for findings (file, line, severity, message) and enforce it.
3. Run the review in a GitHub Actions workflow on `pull_request` and post findings as a comment.
4. On a re-run, pass the earlier findings so duplicates are suppressed.
5. Store the API key as a repository secret, never in the workflow file.

**Done when**

- [ ] The workflow completes without hanging.
- [ ] Findings are valid JSON matching your schema.
- [ ] Re-runs do not repeat earlier findings.

## Exam traps

- Omitting `-p`, which causes the job to hang.
- Having the same session generate and review code.

## Self-check questions

1. A CI job running Claude Code never finishes. Most likely cause?
2. Why should review run in a separate invocation from generation?
3. How does CLAUDE.md improve CI review quality?

## Working with Claude on this module

- `start 3.6`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 3.6 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 3.6`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
