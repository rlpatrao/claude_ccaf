# 1.4 Workflow Enforcement and Human Handoff

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Implement multi-step workflows with enforcement and handoff patterns.

## Learning objectives

- Distinguish programmatic enforcement from prompt-based guidance.
- Implement a prerequisite gate between tools.
- Design a structured handoff to a human agent.

## Concepts to study

- Prompt instructions are followed with high but not guaranteed reliability. Mandatory business rules (identity verification before a refund) belong in code.
- Prerequisite gate: tool B is blocked until tool A has succeeded, enforced through session state or a hook.
- Multi-concern requests: decompose into separate items, resolve each, then respond once.
- Handoff summary: customer ID, issue, actions taken, root cause, recommended next action. The human agent should not need the transcript.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A customer-support agent with stub tools `get_customer`, `lookup_order`, `process_refund`, and `escalate_to_human`.

**Steps**

1. Enforce 'verify the customer before any refund' through the system prompt only. Run 20 varied prompts, including adversarial ones, and count violations.
2. Enforce the same rule in code: `process_refund` returns a structured error unless `get_customer` succeeded earlier in the session.
3. Rerun the same 20 prompts and compare violation counts.
4. Require `escalate_to_human` to accept a structured summary that matches a schema you define.
5. Test one message containing two concerns, for example a refund and an address change.

**Done when**

- [ ] Zero gate violations with programmatic enforcement.
- [ ] The handoff payload is self-contained.
- [ ] Both concerns in a multi-concern message are resolved or explicitly deferred.

## Exam traps

- Choosing 'strengthen the wording in the system prompt' when a business rule must be guaranteed.
- Handoff messages that say 'see conversation above'.

## Self-check questions

1. A refund was processed for an unverified caller in 3% of sessions. Which fix provides a guarantee?
2. List the fields a human agent needs in an escalation summary.
3. When is prompt-based guidance sufficient on its own?

## Working with Claude on this module

- `start 1.4`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.4 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.4`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
