# Cheat Sheet — 4.6 Multi-Instance and Multi-Pass Review

## Independent instance > self-review
Same session keeps its reasoning → won't question its own decisions. Use a **separate invocation** with no prior context.
❌ "Please review carefully" in same session · ❌ extended thinking in the generating session.

## Multi-pass architecture
- Single pass over many files → **attention dilution**: uneven depth, missed bugs mid-set, contradictory findings.
- Fix: **per-file local passes** + **cross-file integration pass** (data flow, contradictions).
- Larger context window / higher-tier model does **not** fix it — attention quality, not size.

## Confidence routing
- High confidence → straight to devs; low → human review.
- Raw self-reported confidence is **poorly calibrated**.
- **Calibrate thresholds on labelled validation sets** before automated routing.

| | Raw confidence | Calibrated threshold |
|---|---|---|
| Reliable for automation? | No | Yes |

## Wrong answers
Same-session self-review; single pass for big PRs; skipping integration pass; bigger context window; uncalibrated routing.
