# 1.1 Agentic Loops

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Design and implement agentic loops for autonomous task execution.

## Learning objectives

- Explain the request, tool_use, tool_result, response cycle of the Messages API.
- Use `stop_reason` as the loop control signal.
- Recognise loop termination anti-patterns.

## Concepts to study

- `stop_reason` values: `tool_use`, `end_turn`, `max_tokens`, `stop_sequence`, `pause_turn`, `refusal`. Know what your loop should do for each.
- History ordering: the assistant turn containing `tool_use` blocks must be followed by a user turn containing `tool_result` blocks with matching `tool_use_id` values.
- Parallel tool use: one response can contain several `tool_use` blocks; all results go back in a single user turn.
- An iteration cap is a safety net. The primary termination signal is `stop_reason`.
- Model-driven tool selection versus a pre-configured decision tree.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A command-line agent that uses the Anthropic Python SDK directly (no framework) with two local tools, for example `get_weather(city)` returning stub data and `convert_units(value, from_unit, to_unit)`.

**Steps**

1. Define both tool schemas with a JSON Schema `input_schema` and a clear description.
2. Send a user request that needs both tools to answer.
3. Write a loop that inspects `stop_reason`. On `tool_use`, execute every requested tool and append the results. On `end_turn`, print the final text and exit.
4. Log every iteration: `stop_reason`, tool names, and tool inputs.
5. Add a maximum-iteration guard and log a warning when it triggers.
6. Make one tool raise an exception, return the failure as a `tool_result` with `is_error: true`, and observe how Claude recovers.

**Done when**

- [ ] The agent completes a two-tool request without hard-coded tool ordering.
- [ ] The loop terminates on `end_turn`, not by searching the response text for a phrase.
- [ ] Every `tool_use` block in a multi-tool response receives a `tool_result`.

## Exam traps

- Ending the loop when the text contains a phrase such as 'task complete'. Use `stop_reason`.
- Treating an iteration cap as the main stop condition.
- Sending `tool_result` blocks without the preceding assistant `tool_use` turn, which causes an API error.
- Inspecting only the first content block; text blocks often precede `tool_use` blocks.

## Self-check questions

1. Claude returns one text block and two `tool_use` blocks. What exactly must the next request contain?
2. Why is 'stop after five iterations' a poor primary termination strategy?
3. What should your loop do when `stop_reason` is `max_tokens` in the middle of a task?

## Working with Claude on this module

- `start 1.1`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.1 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.1`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
