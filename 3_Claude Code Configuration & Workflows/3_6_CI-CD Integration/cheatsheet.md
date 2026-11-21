# Cheat Sheet — 3.6 CI/CD Integration

## The #1 fact
CI job hangs waiting for input → **`claude -p "…"`** (`--print`, non-interactive).
Fake distractors: `CLAUDE_HEADLESS=true`, `--batch`, stdin from `/dev/null`.

## Structured output
`--output-format json` + `--json-schema` → machine-parseable findings (inline PR comments, severity filters, tracking).

## Independent review
Same session that wrote the code is **biased** reviewing it. Use a **separate `claude -p` instance**.

## Re-runs after new commits
Pass **prior findings** into a **fresh whole-PR run**; ask for **only new or unaddressed** issues. Not: diff-only review, not resuming the old session (stale results).

## CLAUDE.md in CI
Read in CI too — document testing standards, fixtures, review criteria, coverage. (Note: `--bare` skips it; may become default for `-p`. Exam answer = CLAUDE.md.)

## Batch vs real-time
| | Message Batches API | Real-time API |
|---|---|---|
| Latency | Up to 24h, no SLA | Immediate |
| Use | Overnight reports, weekly audits | **Pre-merge blocking checks** |

## Beyond the guide
GitHub Actions (reported 4–5 exam questions) and worktrees for parallel sessions — worth knowing.
