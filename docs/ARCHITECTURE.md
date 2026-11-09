# Architecture: CCA-F Hands-On Study Workspace

## System overview

```
                 +-------------------------------+
                 |           Learner             |
                 +---------------+---------------+
          writes code, runs it   |   asks: start / hint / review / quiz
                                 v
+-----------------+     +----------------------+     +-------------------+
| Sub-module      |<--->| Claude Code (tutor)  |<--->| CLAUDE.md         |
| folder          |     | reads guides and     |     | tutor rules,      |
| README.md guide |     | learner code; never  |     | commands, layout  |
| learner code    |     | writes solutions     |     +-------------------+
+--------+--------+     +----------+-----------+
         |                         | updates on confirmation
         | calls                   v
         v                 +-------------------+
+-----------------+        | PROGRESS.md       |
| Anthropic API,  |        +-------------------+
| Agent SDK, MCP, |
| GitHub Actions  |
+-----------------+
```

## Components

| Component | Responsibility |
|---|---|
| `CLAUDE.md` | Defines Claude's tutor role, the hint ladder, review and quiz behaviour, the command vocabulary, and the study order. Loaded in every session. |
| Domain `README.md` | Lists sub-modules and the approximate exam weight. |
| Sub-module `README.md` | Lab guide for one exam task statement. |
| Capstone `README.md` | Integration brief for one exam scenario. |
| `PROGRESS.md` | Completion state, dates, and quiz scores. |
| `.env` / `.env.example` | Secrets and their template. |

## Data flow

1. The learner asks Claude to `start` a sub-module. Claude reads that folder's README and asks for the learner's approach.
2. The learner writes code in the sub-module folder and runs it against the Anthropic API, the Agent SDK, an MCP server, or Claude Code.
3. The learner pastes output or errors, or asks for a review. Claude reads the files and the guide and reports gaps.
4. When the done criteria are met, the learner asks Claude to mark the item complete, and Claude updates `PROGRESS.md`.

## Design decisions and trade-offs

- **Domain folders follow exam numbering; the recommended study order differs.** Numbering keeps traceability to the exam guide. The study order in `CLAUDE.md` puts API fundamentals (Domain 4) before agent architecture (Domain 1).
- **Sub-module folders are not numbered.** This matches the convention of the folder created before the scaffold (`5_Context Management & Reliability/Context Window Management`). Order is given in each domain README and in `PROGRESS.md`.
- **Guidance in per-folder READMEs, not in `CLAUDE.md`.** `CLAUDE.md` is loaded in every session, so keeping it short preserves context. READMEs are read only when a lab is active.
- **Labs extend earlier labs.** For example, 1.5 adds hooks to the 1.4 agent and 5.3 extends the 1.2 research system. This reduces repeated setup and mirrors how the capstones combine components.
- **Folder names contain spaces and `&`.** They are readable but must be quoted in the shell.

## External dependencies

- Anthropic Messages API and Message Batches API
- Claude Agent SDK (Python or TypeScript)
- Model Context Protocol SDK and MCP Inspector
- Claude Code CLI
- GitHub and GitHub Actions (lab 3.6 and the CI/CD capstone)

## Deployment model

Local only. The repository runs on the learner's machine. The CI/CD lab uses a separate personal GitHub repository, with the API key stored as a repository secret.
