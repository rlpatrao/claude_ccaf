# CCA-F Hands-On Study Workspace

This repository structures hands-on preparation for the Claude Certified Architect – Foundations (CCA-F) exam. It contains one folder per exam domain and one folder per sub-module, each with a lab guide. The learner writes all lab code; Claude Code, guided by `CLAUDE.md`, acts as a tutor and reviewer and does not write solutions.

## Quick start

1. Open this folder in Claude Code (`claude` from the repository root, or the VS Code extension).
2. Complete [0_Environment Setup](./0_Environment%20Setup/README.md): virtual environment, packages, `.env`, and a first API call.
3. Ask Claude `what next` to get the recommended sub-module, then `start <n.n>`.
4. Write your lab code in the sub-module folder, run it, and ask Claude to `review my <n.n> lab`.
5. Ask Claude to `mark <n.n> complete` once the done criteria are met.

## Structure

| Folder | Content |
|---|---|
| `0_Environment Setup/` | Prerequisites and environment checks |
| `1_Agentic Architecture & Orchestration/` | Sub-modules 1.1 to 1.7 |
| `2_Tool Design & MCP Integration/` | Sub-modules 2.1 to 2.5 |
| `3_Claude Code Configuration & Workflows/` | Sub-modules 3.1 to 3.6 |
| `4_Prompt Engineering & Structured Output/` | Sub-modules 4.1 to 4.6 |
| `5_Context Management & Reliability/` | Sub-modules 5.1 to 5.6 |
| `6_Capstone Scenarios/` | Six integrated builds matching the exam scenarios |
| `docs/` | `PRD.md` and `ARCHITECTURE.md` for this workspace |
| `PROGRESS.md` | Completion tracker |
| `CLAUDE.md` | Tutor rules that Claude Code loads in every session |

## Commands

These are phrases to use with Claude Code in this repository. They are defined in `CLAUDE.md`.

| Command | Result |
|---|---|
| `start <n.n>` | Claude restates the objective and asks for your approach. |
| `hint` | Next hint: concept, then API or documentation reference, then pseudocode. |
| `explain <concept>` | Explanation with an example scenario. |
| `review my <n.n> lab` | Review of your files against the lab guide. |
| `quiz me on <n.n \| domain n \| scenario>` | Exam-style multiple-choice quiz. |
| `mark <n.n> complete` | Updates `PROGRESS.md`. |
| `what next` | Recommends the next sub-module from `PROGRESS.md`. |

## Environment variables

| Variable | Required | Used by |
|---|---|---|
| `ANTHROPIC_API_KEY` | Yes | All API, Agent SDK, and batch labs |
| `GITHUB_TOKEN` | Optional | Lab 2.4 (GitHub MCP server) and lab 3.6 (CI/CD) |

Copy `.env.example` to `.env` and fill in values. `.env` is git-ignored.

## Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| `AuthenticationError` or 401 | API key missing or not loaded | Confirm `.env` contains the key and that your script loads it before creating the client. |
| `tool_use ids were found without tool_result blocks` | The assistant `tool_use` turn or a matching `tool_result` is missing from history | Append the full assistant message, then one user message with a `tool_result` for every `tool_use_id`. |
| MCP server shows as failed in `/mcp` | Wrong command path, missing dependency, or unset environment variable | Run the server command directly in a terminal and read stderr. |
| Claude writes code for you | The request overrode the tutor rules | Restate that you want hints only; `CLAUDE.md` rule 1 applies. |
| Claude Code in CI never exits | Interactive mode | Use `-p` for non-interactive runs. |
| Folder paths fail in the shell | Folder names contain spaces and `&` | Quote paths, for example `cd "1_Agentic Architecture & Orchestration"`. |
