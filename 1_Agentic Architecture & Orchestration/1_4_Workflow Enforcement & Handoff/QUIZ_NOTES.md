# Quiz Notes: 1.4 Workflow Enforcement and Handoff

Socratic quiz session held on 11 November 2026, covering Domain 1, Task Statement 1.4 (Workflow Enforcement and Handoff). This file records the questions, the key concepts tested, the model answers, and the areas identified for revision.

---

## Key concepts

### 1. Enforcement spectrum

| Approach | Mechanism | Reliability |
|---|---|---|
| Prompt-based guidance | Instructions in the system prompt, few-shot examples | Probabilistic. Followed in most cases, but the failure rate is never zero and the failing session cannot be predicted. |
| Programmatic enforcement | Hooks, prerequisite gates, checks inside tool handlers | Deterministic. The check runs outside the model's reasoning, so the model cannot argue past it. |

A prompt can make an outcome likely. Only code can make it certain.

### 2. Decision rule

The test is the consequence of a single failure, not the accuracy of an answer. Code enforces actions and their order; it cannot make prose accurate.

| Category | Examples | Approach |
|---|---|---|
| Financial | Refunds, transfers, payments | Programmatic |
| Security | Identity verification, access control | Programmatic |
| Compliance | AML checks, regulatory steps | Programmatic |
| Low-stakes | Formatting, tone, style | Prompt is acceptable |

If one violation would be costly, irreversible or a breach of policy, the rule belongs in code.

### 3. Prerequisite gates

A programmatic check that blocks a tool until a prior condition is met. For "verify the customer before any refund":

| Design point | Correct approach |
|---|---|
| Where the check lives | At the point of execution: the first lines of the `process_refund` handler, or a `PreToolUse` hook matching `process_refund`. Not "at the start of the flow", because the model controls the order of calls. |
| What it remembers | Session state holding the verified customer ID, not a boolean flag. The refund check confirms that the order belongs to that customer. |
| What happens on an early call | A structured error returned as the tool result (for example `prerequisite_not_met`, "call `get_customer` first"), not an exception that ends the loop. The model reads the reason and can recover. |

Expected violation rate with a correct gate: zero by construction. A non-zero count indicates a defect in the gate, such as an unguarded second code path, state leaking between sessions, or a missing ownership check.

### 4. Multi-concern requests

1. Decompose the message into distinct items.
2. Share common context. Verify identity once and use it for every item. An address change is security-sensitive and also falls under the verification gate.
3. Investigate independent items in parallel. Do not impose an order the task does not require.
4. Send one reply that resolves every item or explicitly defers it with a next step.

### 5. Structured handoff

The human agent does not see the transcript, so the payload must be self-contained.

| Field | Purpose |
|---|---|
| Customer ID and verification status | Locate the account; confirm identity has been checked |
| Order number and amount | Facts of the case |
| Issue summary | What the customer asked for |
| Actions already taken | Prevent repeated lookups or a second refund |
| Root cause, or best current understanding | Where to start |
| Reason for escalation | Why the agent could not finish |
| Recommended next action | A decision-ready step |
| Status of other concerns | Avoid repeated or missed work on the other items |

Test: could a human act on this payload without asking anyone a question? Enforcing the fields through a required schema makes completeness deterministic.

### Anti-patterns

- Strengthening the system prompt or adding few-shot examples as the fix for a rule that must be guaranteed.
- Handling a multi-concern request one item at a time across separate replies.
- Handoff messages that say "see conversation above".
- Handoff summaries missing root cause or recommended action.

---

## Questions and model answers

### Question 1: Enforcement spectrum

**Question.** What is the difference between prompt-based guidance and programmatic enforcement for controlling an agent's behaviour?

**Model answer.** Prompt-based guidance is probabilistic: it is followed in most cases but has a non-zero failure rate. Programmatic enforcement is deterministic: a hook, gate or code check runs outside the model and blocks the action whatever the model decides.

### Question 2: Decision rule

**Question.** How would you decide which approach to use for a particular rule?

**Model answer.** By the consequence of a single failure. Financial, security and compliance rules need programmatic enforcement. Presentation preferences can stay in the prompt.

### Question 3: Classifying rules

**Question.** Which of these need programmatic enforcement? (1) Address the customer by first name. (2) Never issue a refund above £500 without supervisor approval. (3) Summarise the resolution in bullet points.

**Model answer.** Rule 2 is programmatic because it is a financial control and a breach is a real loss. Rules 1 and 3 are presentation preferences, so a prompt is sufficient.

### Question 4: Designing the gate

**Question.** How would you build a gate that stops `process_refund` until `get_customer` has verified the caller? Where does the check live, what does it remember, and what happens on an early call?

**Model answer.** The check lives at the tool's point of execution (handler or `PreToolUse` hook). It remembers the verified customer ID and checks that the order belongs to that customer. An early call receives a structured error naming the missing prerequisite, so the model can verify and retry.

### Question 5: The 8% to 0.5% proposal

**Question.** Few-shot examples reduced unverified refunds from 8% to 0.5%. Should the issue be closed? What rate should the gate produce?

**Model answer.** No. The rate is lower but not zero, and it can rise with model changes, prompt edits, longer contexts or adversarial wording. At volume, 0.5% is still many unverified refunds. A correct gate produces zero violations by construction.

### Question 6: Multi-concern request

**Question.** A customer asks for a refund of a duplicate charge and an address change in one message. How should the agent handle it, and what is the common failure?

**Model answer.** Decompose into two items, verify once for both, handle the independent items in parallel, and send one reply covering both. The common failure is resolving the first item, replying, and losing the second or pushing it to a follow-up.

### Question 7: Handoff payload

**Question.** What fields must the escalation payload contain, and why does "Customer has a billing issue, see conversation above" fail?

**Model answer.** It fails because the human agent has no transcript. The payload needs the customer ID, order and amount, issue summary, actions taken, root cause, reason for escalation, recommended next action, and the status of any other concerns.

### Final scenario: Guaranteeing the order of steps

**Question.** In 8% of cases an agent processes refunds without verifying account ownership, occasionally refunding the wrong account. The system prompt already says to check ownership first, and the company needs that order to hold on every refund. What is the fix, and why are enhanced prompts or few-shot examples insufficient?

**Model answer.** A programmatic prerequisite gate, either a `PreToolUse` hook on `process_refund` or a check in its handler. It confirms that a customer was verified in the session and that the order belongs to that customer, and returns a structured error otherwise. Enhanced prompts and few-shot examples reduce the failure rate but cannot reduce it to zero, so they cannot provide the guarantee the company requires.

---

## Assessment from this session

| Concept | Assessment |
|---|---|
| Enforcement spectrum | Strong. Deterministic versus probabilistic identified at once. |
| Decision rule | Partial. Initially framed as "when accuracy matters"; the criterion is the consequence of a single failure. Classification question answered correctly. |
| Prerequisite gates | Partial. Correct idea of a programmatic, state-based block. Placement ("beginning of the flow"), the stored state (a flag rather than the customer ID), and the failure mode (structured error) needed refinement. |
| Rejecting a lower prompt failure rate | Strong. The expected rate after the gate (zero) was not stated. |
| Multi-concern handling | Weakest area. Proposed sequential handling ("refund first, then address") and did not name the common failure. |
| Structured handoff | Partial. Factual fields correct; actions taken, root cause, escalation reason, recommended action and other-concern status were missing. |
| Final scenario | Correct. |

## Areas to revise

1. **The decision criterion:** the consequence of a single failure, not the accuracy of an answer.
2. **Gate placement:** at the tool's point of execution, because the model controls the order of calls.
3. **Gate state:** store the verified customer ID and check order ownership, not a boolean flag.
4. **Multi-concern handling:** decompose first, share verification, run independent items in parallel, reply once.
5. **Handoff fields:** in particular root cause and recommended next action, which the exam emphasises.
