# Quiz Notes: 1.5 Agent SDK Hooks

Socratic quiz session held on 11 November 2026, covering Domain 1, Task Statement 1.5 (Agent SDK Hooks). This file records the questions, the key concepts tested, the model answers, and the areas identified for revision.

---

## Key concepts

### 1. Two tool hooks and their position in the lifecycle

```
model decides to call tool -> [PreToolUse] -> tool executes -> [PostToolUse] -> model reads result
```

| Hook | Runs | Can do | Typical use |
|---|---|---|---|
| `PreToolUse` | After the model decides to call the tool, before it executes | Allow, deny with a reason, or modify the input | Policy enforcement |
| `PostToolUse` | After the tool executes, before the model sees the result | Transform or trim the result; cannot undo the action | Data normalisation |

The Agent SDK has further hook events (for example `Stop`, `SubagentStop`, `PreCompact`). The exam compares these two directly.

### 2. `PostToolUse` for data normalisation

Different tools return the same kind of data in different formats. A `PostToolUse` hook converts them to one representation before the model reads them.

| Source | Raw value | Normalised |
|---|---|---|
| A | `"2026-11-03T14:20:00Z"` | ISO 8601 |
| B | `1793710800` (Unix epoch) | ISO 8601 |
| C | `"11/03/2026"` | ISO 8601 |

Why a prompt instruction ("dates may arrive in different formats") is insufficient:

- `11/03/2026` is ambiguous (3 November in US format, 11 March in UK format). The code knows each backend's convention; the model does not.
- Epoch conversion is arithmetic, which models occasionally get wrong.
- Rules such as "within 30 days of purchase" depend on comparing dates across sources.

The same applies to numeric status codes, which should be mapped to labels such as `active`, `suspended` and `closed`. If you own the tool, normalising inside it is also valid. The hook matters when the tools are third-party MCP servers.

### 3. `PreToolUse` for policy enforcement

For "refunds above $500 go to a human":

| Design point | Correct approach |
|---|---|
| What it inspects | The amount in `tool_input`, with a matcher on `process_refund`. A missing or non-numeric amount is denied (fail closed). |
| What it returns | `permissionDecision: "deny"` with a `permissionDecisionReason`. The SDK returns the reason to Claude in place of the tool output. (`is_error: true` is the shape of a tool result, used when the check is inside the tool handler.) |
| What the reason says | The next step, for example "Refunds above $500 need human approval. Call `escalate_to_human` with the customer ID, order, amount and reason." |

The deny guarantees that the refund does not execute. The subsequent escalation is still the model's choice. If escalation must always happen, the code creates it when denying (block and redirect).

### 4. Decision framework

Hooks provide deterministic guarantees and suit business rules that must hold every time. Prompts provide probabilistic guidance and suit preferences and soft rules. If a single failure would cost money or create legal risk, use a hook.

### Critical distinction: direction

- `PostToolUse` is correct for normalisation and wrong for blocking, because the action has already happened.
- `PreToolUse` is correct for blocking and wrong for normalisation, because no result exists yet.

### Anti-patterns

- Using `PostToolUse` to block a policy-violating action.
- Using prompts for mandatory compliance.
- Leaving heterogeneous tool outputs unnormalised.
- Confusing hook directions.
- Testing an enforcement hook by what the model said rather than by backend state.

---

## Questions and model answers

### Question 1: Hook lifecycle

**Question.** What are the two hooks that act on tool calls, and when does each run relative to the tool executing?

**Model answer.** `PreToolUse` runs after the model decides to call the tool and before it executes; it can still stop the action. `PostToolUse` runs after the tool executes and before the model sees the result; it can change what the model reads but cannot undo the action.

### Question 2: Normalising three date formats

**Question.** Three backends return dates as ISO 8601, Unix epoch and `MM/DD/YYYY`. A colleague proposes a prompt line asking the model to interpret them carefully. What is wrong with this, and what should be done instead?

**Model answer.** A prompt is guidance, not a guarantee. The `MM/DD/YYYY` value is ambiguous to the model, epoch conversion is error-prone, and date comparisons depend on consistency. A `PostToolUse` hook should convert every value to ISO 8601 before the model reads it.

### Question 3: Enforcing a $500 refund limit

**Question.** How does a `PreToolUse` hook enforce "refunds above $500 go to a human"? What does it inspect, what does it return, and what happens next?

**Model answer.** It inspects the amount in `tool_input` for `process_refund` and denies missing or invalid values. Above the limit it returns `permissionDecision: "deny"` with a reason that directs escalation. The model receives the reason and calls `escalate_to_human` with a self-contained summary. The hook guarantees that the refund does not run; escalation is guaranteed only if the code performs it.

### Question 4: Classifying rules

**Question.** Choose a `PreToolUse` hook, a `PostToolUse` hook or a prompt for each rule: (1) reply in the customer's language; (2) never refund to a payment method other than the original; (3) map numeric CRM status codes to labels; (4) prefer `lookup_order` over `search_orders` when the order ID is known.

**Model answer.** (1) Prompt: a preference that code cannot easily check. (2) `PreToolUse`: a financial and fraud control that must hold every time. (3) `PostToolUse`: output normalisation before the model reads it. (4) Prompt: an efficiency preference; a miss still reaches the right answer.

### Question 5: Blocking with `PostToolUse`

**Question.** A colleague implements the $500 limit as a `PostToolUse` hook that replaces the result with "Refund denied" so the model escalates. Testing shows the model always escalates. What is wrong, and what would finance find?

**Model answer.** The refund has already executed before the hook runs. Finance would find paid refunds above $500 that every record describes as denied, with a risk of a second payment when a human approves the escalation. The design hides violations rather than preventing them. The test checked the conversation rather than whether the refund stub ran.

### Final scenario: AML enforcement

**Question.** An agent occasionally processes international transfers without AML checks. The compliance team requires 100% enforcement. Should you use a `PostToolUse` hook, a `PreToolUse` hook, or enhanced prompt instructions?

**Answer.** A `PreToolUse` hook.

- `PreToolUse` is correct: it runs before the transfer executes, checks that an AML check passed for this customer and this transfer, and denies the call otherwise.
- `PostToolUse` is wrong: the transfer has already executed when it runs, so it can only conceal the violation.
- Enhanced prompts are wrong: they reduce the failure rate but cannot reach zero, and one missed check is a regulatory breach.

This is the 1.4 prerequisite gate implemented as a hook. A pass recorded for a different customer or transfer must not satisfy the gate.

---

## Assessment from this session

| Concept | Assessment |
|---|---|
| Hook direction | Strong. Never confused across the session. |
| `PostToolUse` normalisation | Strong. Correctly rejected the prompt-based approach. |
| `PreToolUse` enforcement | Partial. Correct mechanism; used `is_error: true` instead of a deny decision with a reason, and did not separate what the deny guarantees from what the model does next. |
| Decision framework | Strong. All four classifications correct, though reasons were not given. |
| `PostToolUse` used for blocking | Strong. Identified at once that the action has already occurred. |
| Final scenario | Correct choice; the distractors were not explained. |

## Areas to revise

1. **How a hook denies:** `permissionDecision: "deny"` with `permissionDecisionReason`. `is_error: true` belongs to a tool result.
2. **What a deny guarantees:** only that the blocked action does not execute. Follow-up actions are guaranteed only if the code performs them.
3. **Explaining why distractors fail:** practise a one-line reason for each wrong option, for example "`PostToolUse` is too late: the tool has already run."
4. **Testing enforcement:** verify backend state (did the tool run?), not only the model's reply.
