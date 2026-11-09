# 5.1 Context Window Management

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Manage conversation context to preserve critical information across long interactions.

## Learning objectives

- Preserve exact facts across long conversations.
- Reduce context consumption from tool output.

## Concepts to study

- Progressive summarisation loses specifics such as amounts, dates, and order IDs. Keep a persistent case-facts block outside the summarised history.
- Lost in the middle: models attend most reliably to the beginning and end of long inputs. Put key findings first and use clear section headings.
- Trim verbose tool output to relevant fields before adding it to history.
- Subagents should return condensed, structured results with metadata.
- Claude Code: `/context` shows usage, `/compact` accepts focus instructions, `/clear` resets between unrelated tasks.
- The token counting endpoint measures prompt size before sending.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A long-running support conversation simulator.

**Steps**

1. Script a 30-turn conversation where turn 2 contains specific facts (order ID, amount, date).
2. Summarise the history every 10 turns. Check whether the facts survive at turn 30.
3. Add a persistent case-facts block included in every request. Compare.
4. Trim tool output to the needed fields. Measure token savings with the token counting endpoint.

**Done when**

- [ ] Facts from turn 2 are exact at turn 30.
- [ ] Token savings from trimming are measured.

## Exam traps

- Relying on summaries to retain exact values.
- Appending full raw tool output to the history.

## Self-check questions

1. After many turns, the agent quotes the wrong refund amount. What design change prevents this?
2. Where should the most important information go in a long prompt?
3. What should you remove from a tool result before it enters the history?

## Working with Claude on this module

- `start 5.1`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.1 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.1`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
