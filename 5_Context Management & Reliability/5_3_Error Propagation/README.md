# 5.3 Error Propagation in Multi-Agent Systems

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Implement error propagation strategies across multi-agent systems.

## Learning objectives

- Return structured error context from subagents.
- Let the coordinator make recovery decisions.

## Concepts to study

- Subagents should return the failure type, what was attempted, any partial results, and possible alternatives.
- Distinguish an access failure (timeout) from a valid empty result.
- Anti-patterns: silently returning empty results as success, and terminating the whole workflow because one source failed.
- The coordinator decides whether to retry, use an alternative source, or continue with partial results annotated with the coverage gap.
- Subagents recover locally from transient errors and propagate only what they cannot resolve.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Extend the research system from lab 1.2.

**Steps**

1. Inject a timeout into one subagent.
2. Version A: the subagent returns an empty list. Observe the coordinator and the final report.
3. Version B: the subagent returns a structured error. Observe again.
4. Require the final report to state any coverage gap explicitly.

**Done when**

- [ ] Version B produces a report that names the gap.
- [ ] The workflow continues despite one failed source.

## Exam traps

- Suppressing errors by returning empty results.
- Aborting the entire workflow on a single subagent failure.

## Self-check questions

1. A report omits a topic because its search subagent timed out and returned nothing. What should the subagent have returned?
2. Which component should decide whether to proceed with partial results?
3. What belongs in a structured error from a subagent?

## Working with Claude on this module

- `start 5.3`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.3 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.3`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
