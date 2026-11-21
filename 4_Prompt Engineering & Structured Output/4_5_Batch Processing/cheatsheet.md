# Cheat Sheet — 4.5 Batch Processing Strategies

## Message Batches API
- **50% cheaper** than sync
- Up to **24h**, **no latency SLA**
- **No multi-turn tool calling** in one request
- `custom_id` correlates requests ↔ results

## Matching rule (most tested)
| Sync API | Batch API |
|---|---|
| Something is **waiting**: pre-merge checks, live code review, live support | Consumed **later**: overnight reports, weekly audits, nightly test gen, bulk extraction |

Sample Q11: "switch everything to batch to save money" → **wrong**; keep blocking work synchronous.

## SLA maths
Always plan for the full 24h. 30h SLA → 6h buffer → submit every 4–6h; submit ≥30h before deadline.

## Failures
Find by `custom_id` → resubmit **only failures**, with targeted fixes (chunk large docs, simplify prompt, add format examples). Never resubmit the whole batch.

## Refine first
Tune prompt on **5–10 representative docs** before the full run. 90% vs 60% first-pass on 1,000 docs = 100 vs 400 retries.

## Tools in batch
Your own (client) tool needed mid-request → **sync API** (or resolve before/between batches). Server tools now run in batch, but exam = guide wording.
