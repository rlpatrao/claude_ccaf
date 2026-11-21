# Capstone: Multi-Agent Research System

**Domains exercised:** 1 (Agentic Architecture), 2 (Tool Design and MCP), 5 (Context and Reliability)

## Scenario

A coordinator delegates to specialised subagents (search, document analysis, synthesis, report generation) to produce a cited research report.

## Build brief

Build the coordinator and four subagents. The final report must cite a source for every claim.

**Components to integrate from earlier labs**

- Coordinator decomposition and coverage checking (1.2).
- Parallel subagent spawning with structured context (1.3).
- Role-scoped tools and a scoped `verify_fact` tool for synthesis (2.3).
- Structured error propagation with coverage-gap annotation (5.3).
- Claim-source mappings and conflict annotation (5.6).

## Acceptance criteria

- [ ] Independent subagents run in parallel.
- [ ] A simulated source failure produces a report that names the gap.
- [ ] Every claim traces to a source; conflicts appear with dates.

## Exam practice with Claude

- `quiz me on the multi-agent research scenario, 10 questions`
- `trace a claim in my final report back to its source and check provenance`

## My notes

_Record design decisions, trade-offs you considered, and the exam concepts each decision maps to._
