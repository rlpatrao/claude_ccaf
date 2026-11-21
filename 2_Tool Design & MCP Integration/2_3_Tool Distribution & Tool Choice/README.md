# 2.3 Tool Distribution and tool_choice

**Domain:** 2. Tool Design & MCP Integration
**Exam task statement:** Distribute tools appropriately across agents and configure tool choice.

## Learning objectives

- Scope tools to agent roles.
- Use `tool_choice` to control whether and which tool is called.

## Concepts to study

- Selection reliability degrades as the tool count grows. Give each agent the small set of tools its role needs (roughly four to five).
- A narrowly scoped cross-role tool (for example `verify_fact` for a synthesis agent) can replace frequent round trips through the coordinator.
- `tool_choice` options: `{"type": "auto"}` (default; may answer in text), `{"type": "any"}` (must call some tool), `{"type": "tool", "name": "..."}` (must call that tool), `{"type": "none"}`.
- Force a specific tool for a mandatory first step, then return to `auto`.
- Check the documentation for constraints on forced tool choice when extended thinking is enabled.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A comparison between one agent with many tools and several role-specific agents.

**Steps**

1. Give one agent 15 tools. Run 20 prompts and measure incorrect selections.
2. Split the tools across three role-specific agents. Rerun and compare.
3. Use `any` to guarantee a structured tool call where the model would otherwise reply in text.
4. Force a specific tool on the first turn, then switch to `auto`.

**Done when**

- [ ] Misselection rates for both designs are recorded.
- [ ] You can state which `tool_choice` value fits a given requirement.

## Exam traps

- Giving every agent every tool.
- Using `auto` when a tool call must be guaranteed.

## Self-check questions

1. Several extraction schemas exist and the document type is unknown. Which `tool_choice` guarantees structured output?
2. A synthesis agent frequently needs simple fact checks. What tool design reduces latency?
3. What does `auto` permit that `any` does not?

## Working with Claude on this module

- `start 2.3`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 2.3 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 2.3`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
