# 4.3 Structured Output with Tool Use and JSON Schemas

**Domain:** 4. Prompt Engineering & Structured Output
**Exam task statement:** Enforce structured output using tool use and JSON schemas.

## Learning objectives

- Obtain schema-conformant output reliably.
- Design schemas that discourage fabrication.

## Concepts to study

- A tool with an `input_schema`, combined with `tool_choice` that forces the call, produces schema-conformant output. This removes JSON syntax errors but not semantic errors (wrong values, values in the wrong field, totals that do not add up).
- The API also offers a structured outputs feature with JSON schema; check the documentation for its current status and parameters.
- Make fields nullable when the information may be absent, so the model can return null instead of inventing a value.
- Use enums with an `other` value plus a free-text detail field, and an `unclear` value where appropriate.
- Use `{"type": "any"}` when several extraction schemas exist and the document type is unknown.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** An invoice extractor applied to five invoice texts that you write, including one without a due date and one in an unusual currency.

**Steps**

1. Ask for JSON in plain text. Count parse failures across ten runs.
2. Switch to a forced extraction tool with a schema. Count again.
3. Make `due_date` nullable and confirm the model no longer invents a date for the invoice that lacks one.
4. Add a currency enum with `other` and a `currency_other` field.

**Done when**

- [ ] Zero parse failures with the forced tool.
- [ ] No fabricated values for absent fields.

## Exam traps

- Believing schema enforcement guarantees correct values.
- Marking fields required when the information may be absent, which encourages fabrication.

## Self-check questions

1. Tool use eliminated JSON errors, but some totals are wrong. Why, and what addresses it?
2. How does a nullable field reduce hallucination?
3. Why pair an `other` enum value with a detail field?

## Working with Claude on this module

- `start 4.3`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 4.3 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 4.3`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
