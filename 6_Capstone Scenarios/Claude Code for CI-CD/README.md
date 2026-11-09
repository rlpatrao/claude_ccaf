# Capstone: Claude Code for CI/CD

**Domains exercised:** 3 (Claude Code Configuration), 4 (Prompt Engineering and Structured Output)

## Scenario

Claude Code runs in a CI/CD pipeline to review pull requests, generate tests, and provide feedback. Output must be actionable and must keep false positives low.

## Build brief

Build a GitHub Actions workflow that reviews each pull request and posts structured findings.

**Components to integrate from earlier labs**

- Non-interactive invocation with JSON output (3.6).
- Explicit review criteria and severity definitions (4.1).
- Schema-enforced findings (4.3).
- Independent review instance and multi-pass review (4.6).

## Acceptance criteria

- [ ] The workflow never hangs and posts schema-valid findings.
- [ ] Measured false-positive rate on a labelled pull request is recorded.
- [ ] Re-runs do not duplicate earlier findings.

## Exam practice with Claude

- `quiz me on the CI/CD scenario, 10 questions`
- `review my workflow YAML for unattended-run risks`

## My notes

_Record design decisions, trade-offs you considered, and the exam concepts each decision maps to._
