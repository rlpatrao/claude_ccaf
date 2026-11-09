# 0. Environment Setup

Complete this module before any lab. You run every command yourself; ask Claude for help interpreting errors.

## Prerequisites

| Requirement | Purpose | Check |
|---|---|---|
| Python 3.11 or later | API, Agent SDK, and MCP labs | `python3 --version` |
| Node.js 18 or later | MCP Inspector and some community MCP servers | `node --version` |
| Claude Code | Domain 3 labs and Claude Code exercises elsewhere | `claude --version` |
| Anthropic API key | All API and Agent SDK labs | Present in `.env` |
| GitHub account and test repository | Lab 3.6 and the CI/CD capstone | Able to push and open pull requests |

## Steps

1. Create a virtual environment at the repository root (`.venv/`) and activate it.
2. Install the packages you will need: `anthropic`, `claude-agent-sdk`, `mcp`, and `python-dotenv`. Record installed versions in your notes; API details referenced in the labs depend on them.
3. Copy `.env.example` to `.env` and add your API key. Confirm `.env` is listed in `.gitignore`.
4. Write a short script in this folder that loads `.env` and sends one message to Claude. Run it and confirm you receive a response.
5. Run `npx @modelcontextprotocol/inspector` and confirm the Inspector opens.
6. In Claude Code, run `/help`, `/memory`, `/context`, `/agents`, and `/mcp`, and note what each one shows.

## Done when

- [ ] The test script returns a response from Claude.
- [ ] `git status` does not list `.env`.
- [ ] The MCP Inspector starts.
- [ ] You have noted the purpose of each Claude Code command listed in step 6.

## Study resources

- Anthropic Academy: the CCA-F exam guide and preparation courses. Read the exam guide first and compare its task statements with the sub-module list in this repository.
- Anthropic documentation: Messages API, tool use, Message Batches, Claude Agent SDK, Claude Code, and Model Context Protocol.

## My notes

_Record installed versions and any setup problems with their fixes._
