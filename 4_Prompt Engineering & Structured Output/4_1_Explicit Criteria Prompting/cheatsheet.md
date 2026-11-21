# Cheat Sheet — 4.1 System Prompts with Explicit Criteria

## Explicit criteria > vague instructions
- ❌ "Be conservative", "only report high-confidence findings", "use your judgement" → no decision boundary.
- ✅ Define exactly **what to flag** (bugs, security vulns) and **what to skip** (style, local patterns).

## False positives destroy trust everywhere
- 40% wrong "doc mismatch" findings → devs ignore 98%-accurate security findings too.
- Trust is **not category-specific**.

## Fix: disable and iterate
**Temporarily disable** high-FP categories → improve their prompts with code examples → re-enable when precise.

## Severity calibration
Define severities with **concrete code examples** (e.g. unsanitised SQL snippet = Critical), not prose.

## Confidence filtering
Self-reported confidence is **poorly calibrated**. Order: **explicit criteria first**, confidence routing second.

## Wrong answers
"Only report high-confidence findings"; confidence thresholds as the fix; prose-only severity definitions; keeping noisy categories on while tuning.
