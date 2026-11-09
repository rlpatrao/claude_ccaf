# Product Requirements: CCA-F Hands-On Study Workspace

## Problem statement

The CCA-F exam tests applied judgement through scenario-based questions across five domains. Reading documentation alone does not build the practical understanding the scenarios require. The learner needs a structured, hands-on path that maps each exam task statement to a lab, and a tutor that guides without supplying solutions.

## Goals and success metrics

| Goal | Metric |
|---|---|
| Cover every exam task statement with a hands-on lab | 30 sub-module labs, each mapped to one task statement |
| Build working understanding, not copied solutions | All lab code written by the learner |
| Integrate knowledge across domains | Six capstones completed |
| Exam readiness | Consistent quiz scores of 80% or higher in every domain before booking the exam |

## Users and stakeholders

- **Learner:** an engineer or architect preparing for CCA-F who writes the lab code.
- **Claude Code (tutor):** explains concepts, gives graduated hints, reviews code, runs quizzes, and tracks progress, following `CLAUDE.md`.

## Functional requirements

1. One folder per exam domain, numbered to match the exam guide.
2. One folder per sub-module, containing a lab guide with objectives, concepts, a build brief, steps, done criteria, exam traps, and self-check questions.
3. A capstone folder with one integrated build per exam scenario.
4. Tutor rules in `CLAUDE.md` that prohibit solution code and define a hint ladder, review behaviour, quiz format, and progress tracking.
5. A progress tracker in `PROGRESS.md`.

## Non-functional requirements

- **Security:** secrets are held only in `.env`, which is git-ignored. No credential appears in committed files, including `.mcp.json` and CI workflow files.
- **Context efficiency:** `CLAUDE.md` stays short because it loads in every session. Detailed guidance lives in per-folder README files that are read on demand.
- **Accuracy:** product details (CLI flags, SDK parameters) change over time. Lab guides direct the learner to confirm details in current documentation.
- **Cost:** labs use small inputs; batch labs use synthetic data sets of about 50 items.

## Out of scope

- Generated solution code for any lab.
- Reproductions of actual exam questions.
- Hosted infrastructure; everything runs locally or in a personal GitHub repository.
