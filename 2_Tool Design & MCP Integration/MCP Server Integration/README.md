# 2.4 MCP Server Integration

**Domain:** 2. Tool Design & MCP Integration
**Exam task statement:** Integrate MCP servers into Claude Code and agent workflows.

## Learning objectives

- Configure MCP servers at the correct scope.
- Keep credentials out of version control.
- Use MCP resources as well as tools.

## Concepts to study

- Scopes: local (default; private to you in this project), project (`.mcp.json`, committed and shared with the team), user (`~/.claude.json`, all your projects).
- Environment variable expansion in `.mcp.json`, for example `${GITHUB_TOKEN}` and `${VAR:-default}`.
- Transports: stdio and HTTP. SSE is deprecated.
- MCP primitives: tools, resources (catalogues of content that reduce exploratory tool calls), and prompts.
- Tools from all configured servers are available at the same time. Prefer existing community servers for standard integrations and build custom servers for team-specific workflows.
- `/mcp` shows server status and handles authentication.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** MCP configuration exercises in Claude Code and an Agent SDK script.

**Steps**

1. Add a community MCP server at project scope with `claude mcp add --scope project`. Inspect the generated `.mcp.json`.
2. Replace any literal credential with `${VAR}` expansion and confirm the server still connects.
3. Connect your server from lab 2.2 at user scope and verify it with `/mcp`.
4. Add a resource to your server that lists valid order IDs. Compare the number of exploratory tool calls before and after.
5. Connect an MCP server to an Agent SDK script through its MCP server option.

**Done when**

- [ ] No secret appears in any committed file.
- [ ] You can explain which scope a teammate would need for a shared server.

## Exam traps

- Committing secrets in `.mcp.json`.
- Configuring a team-shared server at user scope, so teammates do not receive it.

## Self-check questions

1. A team wants every developer to get the same Jira MCP server automatically. Which scope and file?
2. How do you reference a token in `.mcp.json` without committing it?
3. When does an MCP resource reduce tool calls?

## Working with Claude on this module

- `start 2.4`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 2.4 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 2.4`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
