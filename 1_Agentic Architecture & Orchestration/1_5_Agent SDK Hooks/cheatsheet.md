# Cheat Sheet — 1.5 Agent SDK Hooks

## The two hooks
| Hook | When it runs | Sees | Use for | Wrong for |
|---|---|---|---|---|
| **PreToolUse** | **Before** tool executes | Outgoing call | **Block / modify / redirect** — policy enforcement | Normalising results (no result yet) |
| **PostToolUse** | **After** tool executes, before model sees result | Tool result | **Normalise / transform** data | Blocking (action already happened) |

## Examples
- PreToolUse: block refunds > $500 → escalate to human; block transfers until AML passes.
- PostToolUse: Unix / DD/MM/YYYY → ISO 8601; numeric status codes → readable strings.

## Decision framework
- Must hold **100%** (money, legal, security) → **hook** (deterministic).
- Preferences / soft rules → **prompt** (probabilistic).

## Wrong answers
- PostToolUse to block a violating action — too late
- Prompt instructions for 100% compliance
- Letting the model normalise mixed formats itself
- PreToolUse to clean results

## Exam tip
AML-check scenario with 100% requirement → **PreToolUse hook**.
