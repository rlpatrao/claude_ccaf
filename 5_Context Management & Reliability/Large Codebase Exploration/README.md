# 5.4 Context Management in Large Codebase Exploration

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Manage context effectively in large codebase exploration.

## Learning objectives

- Recognise context degradation.
- Persist findings outside the context window.
- Delegate verbose exploration.

## Concepts to study

- Degradation in long sessions: the model begins to describe 'typical patterns' instead of the specific classes it read earlier.
- Scratchpad files: write key findings to a file and refer to it across context resets.
- Delegate verbose exploration to subagents (for example the Explore subagent) and receive summaries.
- Use `/compact` with focus instructions, and `/clear` between unrelated tasks.
- Export structured state (a manifest of findings) to recover from interruptions.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** An architecture-mapping exercise on a medium-sized open-source repository that you clone.

**Steps**

1. Ask Claude Code to map the architecture in one long session. Record signs of degradation.
2. Repeat using a `findings.md` scratchpad, subagent delegation, and `/compact` with focus instructions.
3. Compare the accuracy and specificity of both results.

**Done when**

- [ ] Your notes list concrete degradation signs and the effect of each mitigation.

## Exam traps

- Continuing a degraded session instead of compacting or resetting with a summary.
- Running verbose exploration in the main context.

## Self-check questions

1. Late in a session, Claude refers to generic patterns instead of the classes it read. What is happening, and what do you do?
2. How does a scratchpad file help across `/clear`?
3. When should exploration be delegated to a subagent?

## Working with Claude on this module

- `start 5.4`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.4 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.4`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
