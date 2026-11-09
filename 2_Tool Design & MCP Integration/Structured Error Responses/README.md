# 2.2 Structured Error Responses for MCP Tools

**Domain:** 2. Tool Design & MCP Integration
**Exam task statement:** Implement structured error responses for MCP tools.

## Learning objectives

- Return errors that let Claude decide whether to retry, fix input, or escalate.
- Distinguish a failed query from a successful query with no results.

## Concepts to study

- MCP tool results use `isError: true`; Messages API tool results use `is_error: true`.
- Error categories: transient (timeout, 503; retryable), validation (bad input; correct and retry), permission (escalate), business rule (for example a refund limit; explain to the user).
- Include a retryable flag, a readable message, and a suggested next action.
- 'No results found' is a successful, empty result. 'The query failed' is an error. Never conflate them.
- Recover locally from transient errors inside a subagent; propagate what cannot be resolved, with context, to the coordinator.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A minimal MCP server using the Python `mcp` SDK (FastMCP) with one tool, `lookup_order`, that can simulate each error category based on its input.

**Steps**

1. Return the generic text 'Operation failed' for every error. Observe and record Claude's behaviour.
2. Replace it with structured errors: category, retryable flag, message, and suggested action.
3. Return an empty result set as a success with zero records. Confirm Claude does not treat it as a failure.
4. Test the server with the MCP Inspector (`npx @modelcontextprotocol/inspector`) and then from Claude Code with `claude mcp add`.

**Done when**

- [ ] Claude retries transient errors, corrects validation errors, and stops on permission and business-rule errors.
- [ ] Empty results and failures produce different, correct responses.

## Exam traps

- Returning an empty result when the query actually failed, which hides the failure.
- Using the same error message for every failure.
- Retrying errors that are not retryable.

## Self-check questions

1. A tool times out. What should its response contain?
2. Why is returning `[]` on a database timeout harmful in a multi-agent system?
3. Which error category should lead to escalation instead of a retry?

## Working with Claude on this module

- `start 2.2`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 2.2 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 2.2`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
