# Capstone: Developer Productivity with Claude

**Domains exercised:** 1 (Agentic Architecture), 2 (Tool Design and MCP), 3 (Claude Code Configuration)

## Scenario

An agent built with the Claude Agent SDK helps engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate, and automate repetitive tasks, using built-in tools and MCP servers.

## Build brief

Build an exploration agent that answers architecture questions about a cloned open-source repository and writes its findings to a scratchpad file.

**Components to integrate from earlier labs**

- Built-in tool selection and incremental exploration (2.5).
- MCP server integration, for example a GitHub server (2.4).
- Session resumption and forking (1.7).
- Exploration delegated to subagents (1.3, 5.4).

## Acceptance criteria

- [ ] The agent answers five architecture questions with file and line references.
- [ ] Sessions can be resumed with a findings file that survives context resets.

## Exam practice with Claude

- `quiz me on the developer productivity scenario, 10 questions`
- `review my agent's tool configuration`

## My notes

_Record design decisions, trade-offs you considered, and the exam concepts each decision maps to._
