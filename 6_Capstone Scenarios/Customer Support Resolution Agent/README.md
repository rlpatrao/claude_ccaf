# Capstone: Customer Support Resolution Agent

**Domains exercised:** 1 (Agentic Architecture), 2 (Tool Design and MCP), 5 (Context and Reliability)

## Scenario

A support agent built on the Claude Agent SDK resolves customer issues (returns, billing disputes, account problems) using tools exposed through MCP. The goal is a high first-contact resolution rate while escalating the cases that require a human.

## Build brief

Build the agent with an MCP server exposing `get_customer`, `lookup_order`, `process_refund`, and `escalate_to_human`, all backed by stub data.

**Components to integrate from earlier labs**

- Agentic loop (1.1) and prerequisite gate for refunds (1.4).
- PreToolUse refund ceiling and PostToolUse normalisation hooks (1.5).
- Tool descriptions and structured errors (2.1, 2.2).
- Case-facts block for long conversations (5.1).
- Escalation criteria and identity disambiguation (5.2).

## Acceptance criteria

- [ ] Refunds never execute for unverified customers or above the ceiling.
- [ ] Escalations contain a self-contained structured summary.
- [ ] Explicit requests for a human are honoured.
- [ ] Exact amounts and IDs survive a 30-turn conversation.

## Exam practice with Claude

- `quiz me on the customer support scenario, 10 questions`
- `review my customer support design note against domains 1, 2 and 5`

## My notes

_Record design decisions, trade-offs you considered, and the exam concepts each decision maps to._
