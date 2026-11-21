# Cheat Sheet — 2.4 MCP Server Integration

## Config scopes
| File | Scope | VCS | Use for |
|---|---|---|---|
| `.mcp.json` (repo root) | Project | **Committed, shared** | Team servers: Jira, GitHub, internal APIs |
| `~/.claude.json` | User | Personal, not shared | Experimental / personal servers |

All servers' tools are discovered at connect time and available together — no activation step. (Current Claude Code lazy-loads full definitions via tool search; exam answer unchanged.)

## Credentials
- Use `${GITHUB_TOKEN}`-style expansion in `.mcp.json`; each dev sets values locally.
- Safe to commit, per-user creds, rotate without config changes.
- "Private repo" is **not** a secret store.

## Resources vs tools
- **Resources** = content catalogues (schemas, issue summaries, doc trees) visible up front → no exploratory `list_tables`/`describe_table` calls.
- **Tools** = act on the data.

## Build vs use
**Evaluate community servers first** (Jira, GitHub, Slack, Notion). Build custom only for team-specific workflows or proprietary systems with no server.

## Agent ignores your MCP tool, uses Grep?
Sparse description. **Enrich the MCP tool description** (what, returns, when, vs built-ins). Not a prompt rule, not removing built-ins.

## Wrong answers
Team servers in `~/.claude.json`; hard-coded tokens; custom build for Jira; system-prompt rule to force MCP use.
