# 2.1 Tool Interface Design

**Domain:** 2. Tool Design & MCP Integration
**Exam task statement:** Design effective tool interfaces with clear descriptions and boundaries.

## Learning objectives

- Write tool descriptions that state purpose, inputs, outputs, and when not to use the tool.
- Resolve overlapping or ambiguous tools.
- Measure tool-selection accuracy.

## Concepts to study

- The tool description is the primary signal Claude uses to select a tool.
- A good description covers what the tool does, input formats with examples, edge cases, what it returns, and how it differs from similar tools.
- Overlapping tools (for example `analyze_content` and `analyze_document`) cause misrouting. Rename, split, or consolidate them.
- Parameter design: enums for constrained values, required versus optional fields, descriptive names.
- Keyword-heavy system prompt instructions can override otherwise good descriptions.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** A set of four tools with deliberately weak descriptions, followed by an improved version.

**Steps**

1. Write four tools with one-line descriptions; make two of them overlap.
2. Write 20 test prompts, each labelled with the tool you expect. Measure selection accuracy.
3. Rewrite the descriptions using the criteria above. Rerun and record accuracy.
4. Rename or split the overlapping pair and measure again.

**Done when**

- [ ] Accuracy before and after is recorded in your notes.
- [ ] No two tools have overlapping descriptions.

## Exam traps

- Choosing few-shot examples or a separate routing classifier as the first fix when the descriptions are the root cause.
- Merging everything into one generic tool.

## Self-check questions

1. Claude calls `get_customer` when it should call `lookup_order`. What is the first, lowest-effort fix?
2. What belongs in a description beyond 'what the tool does'?
3. When is consolidating two tools better than splitting them?

## Working with Claude on this module

- `start 2.1`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 2.1 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 2.1`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
