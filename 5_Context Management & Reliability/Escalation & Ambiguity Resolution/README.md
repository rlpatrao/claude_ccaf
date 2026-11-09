# 5.2 Escalation and Ambiguity Resolution

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Design effective escalation and ambiguity resolution patterns.

## Learning objectives

- Define reliable escalation triggers.
- Resolve ambiguity by asking instead of guessing.

## Concepts to study

- Reliable triggers: the customer explicitly requests a human, policy is silent or ambiguous on the request, or the agent cannot make progress.
- Unreliable triggers: sentiment analysis and the model's self-reported confidence.
- An explicit request for a human is honoured. A frustrated customer with a resolvable issue can be offered the resolution first, with escalation if they repeat the request.
- Ambiguous identity (several matching customers): ask for an additional identifier; do not pick the most likely match.
- Write explicit escalation criteria with few-shot examples in the system prompt.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Extend the support agent from lab 1.4.

**Steps**

1. Write escalation criteria with one example per trigger.
2. Test cases: an explicit request for a human; frustration about a simple issue; a policy gap (for example, a competitor price-match request); two customers with the same name.
3. Record the agent's action for each case and compare with the expected action.

**Done when**

- [ ] All test cases produce the expected action.

## Exam traps

- Escalating based on sentiment scores.
- Escalating based on self-reported confidence.
- Choosing the most likely match when several customers match.

## Self-check questions

1. A customer asks for a price match, and the policy does not mention competitors. What should the agent do?
2. Why is sentiment a poor escalation trigger?
3. Two accounts match the caller's name. What is the correct next step?

## Working with Claude on this module

- `start 5.2`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.2 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.2`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
