# Capstone: Structured Data Extraction

**Domains exercised:** 4 (Prompt Engineering and Structured Output), 5 (Context and Reliability)

## Scenario

A system extracts structured data from unstructured documents, validates it against JSON schemas, maintains high accuracy, and integrates with downstream systems.

## Build brief

Build an extraction pipeline for one document type with validation, retry, batch processing, and human review routing.

**Components to integrate from earlier labs**

- Forced tool use with nullable fields and enums (4.3).
- Validation and retry with specific feedback (4.4).
- Batch submission and partial-failure handling (4.5).
- Few-shot examples for varied formats (4.2).
- Field-level confidence and stratified review sampling (5.5).

## Acceptance criteria

- [ ] Zero parse failures and no fabricated values for absent fields.
- [ ] Accuracy is reported per field and per document type.
- [ ] Low-confidence items route to a review queue.

## Exam practice with Claude

- `quiz me on the structured data extraction scenario, 10 questions`
- `review my extraction schema for fabrication risks`

## My notes

_Record design decisions, trade-offs you considered, and the exam concepts each decision maps to._
