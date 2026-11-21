# Cheat Sheet — 3.1 CLAUDE.md Hierarchy, Scoping, and Modular Organisation

## Three levels
| Level | Location | Shared via git? | Use for |
|---|---|---|---|
| User | `~/.claude/CLAUDE.md` | **No** | Personal prefs (verbosity, style) |
| Project | `.claude/CLAUDE.md` **or** root `CLAUDE.md` | **Yes** | Team standards: naming, testing, architecture |
| Directory | `<subdir>/CLAUDE.md` | Yes | Package-specific conventions |

## Modularity
- `@path/to/file.md` on its own line imports a file — **not** `@import`.
- `.claude/rules/` → topic files (`testing.md`, `api-conventions.md`), optional `paths:` frontmatter.
- Prefer importing a shared file over duplicating across directory CLAUDE.md files.

## /memory
- Exam: shows which memory files are loaded — **diagnostic only**, loads nothing.
- Current Claude Code: `/memory` lists locations; `/context` shows what loaded. Exam answer = `/memory`.

## Classic trap
"Works for Dev A for months, new joiner gets inconsistent results" → conventions are in Dev A's **user-level** file. Fix: move to **project-level**.

## Wrong answers
- Team standards in `~/.claude/CLAUDE.md`
- One giant monolithic CLAUDE.md
- `/memory` "loads" config
- Directory CLAUDE.md for conventions spanning many dirs → use path-specific rules (3.3)
