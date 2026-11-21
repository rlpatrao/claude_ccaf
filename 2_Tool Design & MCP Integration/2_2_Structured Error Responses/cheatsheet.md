# Cheat Sheet — 2.2 Structured Error Responses

## isError
`isError: true` tells the model the tool **failed** — so it reasons about recovery instead of treating error text as data.

## Four categories
| Category | Examples | isRetryable | Recovery |
|---|---|---|---|
| **Transient** | Timeout, 503, rate limit | **true** | Retry after delay |
| **Validation** | Bad format, missing field | false | Agent fixes input, sends a *new* call |
| **Business** | Policy/limit exceeded | false | Alternative workflow / escalate |
| **Permission** | Access denied | false | Escalate / different credentials |

`isRetryable` = "would resending **this exact call** work?" — `false` ≠ abandon task.

## Required metadata
`errorCategory`, `isRetryable`, `description` (with recovery guidance).

## Critical distinction
| | Access failure | Valid empty result |
|---|---|---|
| Meaning | Couldn't reach source | Queried fine, no matches |
| isError | true | **false** |
| Retry? | Consider | **Never** |

## Multi-agent propagation
- Subagents handle transient errors locally.
- Propagate only unresolved errors, **with partial results + what was attempted**.
- Don't: suppress errors as empty success; kill the whole workflow on one failure.

## Wrong answers
Generic "Operation failed"; retrying empty results; retrying business errors; validation marked retryable.
