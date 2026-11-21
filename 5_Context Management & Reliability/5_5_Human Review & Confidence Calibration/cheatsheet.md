# Cheat Sheet — 5.5 Human Review & Confidence Calibration

## Aggregate metrics trap
97% overall can hide: standard invoices 99.5%, handwritten receipts 60%, scanned PDFs 72%, international docs 45%. Validate **by document type AND field** before automating.

## Stratified random sampling
- Sample every stratum (doc type, confidence band, field).
- **Must include high-confidence items** — they're automated, so they're the blind spot for novel errors.

## Calibration
- Raw confidence ≠ accuracy: 0.90 may be 94% on dates, 82% on amounts.
- Calibrate per field × doc type using **labelled validation sets** (ground truth).

## Reviewer capacity
Limited → route **highest-uncertainty first**, dynamically. Not even spread, not chronological.

## Wrong answers
- "97% accurate, automate everything"
- Sampling only low-confidence items
- Using raw confidence thresholds
- Spreading reviewers evenly
