# 1.2 Coordinator and Subagent Orchestration

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Orchestrate multi-agent systems using coordinator-subagent (hub-and-spoke) patterns.

## Learning objectives

- Describe the responsibilities of a coordinator and of a subagent.
- Explain subagent context isolation and its consequences.
- Decide when a multi-agent design is justified over a single agent.

## Concepts to study

- The coordinator decomposes the task, selects subagents, passes context, aggregates results, and handles errors.
- Subagents do not inherit the coordinator's conversation history. They see only what is passed in their prompt.
- All inter-agent communication routes through the coordinator, which gives one place for observability and error handling.
- Overly narrow decomposition by the coordinator causes coverage gaps even when every subagent performs well.
- Iterative refinement: the coordinator evaluates the synthesis for gaps and re-delegates.
- Cost and latency increase with each additional agent.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A research coordinator with two subagents (a web-search stub and a document-analysis stub) and a synthesis step. Use the Claude Agent SDK or plain Messages API calls.

**Steps**

1. Write the coordinator system prompt: decompose the question into subtasks and assign each one.
2. Implement each subagent as a separate model call with its own system prompt and tool set.
3. Pass each subagent only the context it needs: the subtask, relevant prior findings, and the required output format.
4. Require subagents to return structured results (claim, source, confidence).
5. Have the coordinator check coverage against the original question and re-delegate when it finds a gap.
6. Deliberately make the coordinator decompose too narrowly once, and observe the effect on the final output.

**Done when**

- [ ] Each subagent input is visible in your logs and is self-sufficient.
- [ ] The coordinator detects at least one deliberately introduced gap and re-delegates.

## Exam traps

- Assuming subagents share memory with the coordinator.
- Letting subagents call each other directly, bypassing the coordinator.
- Attributing missing coverage to the subagents when the root cause is the coordinator's decomposition.

## Self-check questions

1. A final report covers two of five expected sub-topics, and each subagent completed its assigned work correctly. Where is the defect?
2. Why should all communication route through the coordinator?
3. What information must a subagent prompt contain that would be implicit in a single-agent design?

## Working with Claude on this module

- `start 1.2`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.2 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.2`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
