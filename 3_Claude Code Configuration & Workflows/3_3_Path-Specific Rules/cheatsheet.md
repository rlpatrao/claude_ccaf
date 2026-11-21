# Cheat Sheet — 3.3 Path-Specific Rules

## Mechanism
```yaml
# .claude/rules/testing.md
---
paths: ["**/*.test.tsx"]
---
Test conventions here…
```
Rule loads **only** when Claude reads/edits a matching file.

## Why it wins
- Globs match **across the whole codebase** — co-located tests in 50+ dirs covered by one file.
- **Token-efficient** — Terraform rules don't load while editing React.

## Comparison
| Option | Loads | Problem for file-type conventions |
|---|---|---|
| Root CLAUDE.md | Every session | Wastes tokens on irrelevant rules |
| Directory CLAUDE.md | That directory only | Need one per directory |
| **Path-specific rule** | Matching files only | ✅ correct answer |
| Skill | On demand (task workflow) | Not always-on guidance |

## Verify
Exam: `/memory`. Reality: `/context` + "Loaded" notice when a path rule triggers.

## Exam rule of thumb
Test files spread next to source in many dirs → **always** path-specific rules with globs.
