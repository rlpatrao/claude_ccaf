# Cheat Sheet — 2.5 Built-in Tools

## Grep vs Glob
| Tool | Searches | Use for |
|---|---|---|
| **Grep** | File **contents** | Callers, error messages, imports, assignments |
| **Glob** | File **paths/names** | `**/*.test.tsx`, `**/config.*`, by extension/dir |

Grep = what's **inside**; Glob = files by **name**.

## Edit vs Read + Write
1. **Edit first** — targeted, unique-match, low context.
2. Edit fails (non-unique anchor) → **Read + Write** (exam answer).
- Real-world today: widen `old_string` or `replace_all: true`; but exam = Read + Write.
- Never default to Read + Write.

## Incremental exploration
Grep entry points → Read to trace imports → Grep again for wrappers/re-exports → Read only what's justified. **Never read everything upfront.**

## Wrapper/barrel tracing
Grep definition → Read to find exported names → Grep each exported name → Grep the barrel module name.

## Deprecation scenario
**Grep** (find callers) **→ Glob** (find their test files). Not the reverse.

## Notes
- Current Claude Code on macOS/Linux/WSL omits Grep/Glob by default (uses `find`/`grep` via Bash); exam treats them as built-ins.

## Wrong answers
Glob for callers; Grep for filename patterns; reading all files; Read + Write by default.
