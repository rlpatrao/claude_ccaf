# Cheat Sheet — 3.2 Custom Slash Commands and Skills

## File structures (not interchangeable)
| Type | Path | Command name from |
|---|---|---|
| Skill | `.claude/skills/deploy/SKILL.md` (directory) | Directory name |
| Command | `.claude/commands/deploy.md` (flat file) | File name |
| ❌ | `.claude/skills/review.md` (flat in skills/) | **Creates nothing** |

`.claude/skills/` is canonical; `.claude/commands/` kept for back-compat.

## Scope
| Scope | Paths | Shared? |
|---|---|---|
| Project | `.claude/skills/…`, `.claude/commands/…` | Yes (git) — team `/review`, `/lint` |
| User | `~/.claude/skills/…`, `~/.claude/commands/…` | No — personal workflows |

## SKILL.md frontmatter (exam's three)
- `context: fork` → runs in isolated sub-agent; verbose output stays out of main context.
- `allowed-tools` → **exam: restricts tool access**. (Reality: pre-approves; `disallowed-tools` is the boundary.)
- `argument-hint` → **exam: prompts for required args**. (Reality: autocomplete hint.)

## Skills vs CLAUDE.md
| | Skills | CLAUDE.md / rules |
|---|---|---|
| Loading | On demand | Always / automatic |
| Content | Task-specific workflows | Universal standards |

## Scenario
Team `/review` → project path. Personal verbose `/brainstorm` → `~/.claude/skills/brainstorm/SKILL.md` with `context: fork`.

## Wrong answers
Flat file in `skills/`; team command in `~/`; task procedures in CLAUDE.md; standards in skills; verbose skill without `context: fork`.
