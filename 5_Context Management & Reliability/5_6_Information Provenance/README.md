# 5.6 Information Provenance and Uncertainty

**Domain:** 5. Context Management & Reliability
**Exam task statement:** Preserve information provenance and handle uncertainty in multi-source synthesis.

## Learning objectives

- Keep claim-to-source mappings through summarisation.
- Represent conflicting information accurately.

## Concepts to study

- Each claim carries its source, location, and date through every summarisation step.
- When sources conflict, present both with attribution instead of silently choosing one. Include dates, because a difference may be temporal rather than a contradiction.
- Separate well-established findings from contested ones in the report structure.
- Use the format suited to the content: tables for figures, prose for narrative.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Extend the synthesis step of the research system from lab 1.2.

**Steps**

1. Provide two sources with conflicting figures from different years.
2. Require subagents to output structured claims (claim, source, location, date).
3. Require the synthesis to annotate the conflict with dates and attribution.
4. Verify that every claim in the final report traces to a source.

**Done when**

- [ ] Every claim in the final report is traceable.
- [ ] The conflict is presented with both sources and dates.

## Exam traps

- Summarisation that drops source references.
- Silently selecting the 'more authoritative' source.

## Self-check questions

1. Two reports give different market sizes. How should the synthesis present them?
2. Why include publication dates with each claim?
3. At which step is provenance most often lost?

## Working with Claude on this module

- `start 5.6`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 5.6 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 5.6`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
