# Cheat Sheet — 1.1 Agentic Loops

## Core loop
1. Send request (with full conversation history) via Messages API
2. Check `stop_reason`
3. `tool_use` → run tools, **append tool results to history**, send again
4. `end_turn` → done

## Key rules
- `stop_reason` is the **only** authoritative loop signal — deterministic, not heuristic.
- Tool results must go back into history; the API has no server-side memory of the turn.
- Model-driven tool selection is preferred — except where business rules need **programmatic enforcement**.
- Production loops also see `pause_turn`, `max_tokens`, `stop_sequence`, `refusal`, `model_context_window_exceeded` — treat anything other than `end_turn` as "not finished, check why". Exam tests only `tool_use` / `end_turn`.

## Anti-patterns (always wrong answers)
| Anti-pattern | Why wrong |
|---|---|
| Parsing "I'm done" / "task complete" | Natural language is ambiguous |
| Iteration cap as primary stop | Cuts off work or wastes turns; OK only as safety net |
| `content[0].type == "text"` as completion | Text can appear alongside `tool_use` blocks |
| Dropping/summarising tool results to save tokens | Model has nothing new to reason over; shrink tool output instead |
| `tool_choice="any"` to stop text replies | Creates infinite loops |

## Exam tip
Iteration caps fix **runaway** loops, not **premature** exits. Premature termination → fix the `stop_reason` check.
