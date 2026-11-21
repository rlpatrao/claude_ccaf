# Cheat Sheet — 5.6 Information Provenance & Multi-Source Synthesis

## Claim-source mapping (5 fields)
`claim` · `source_url` · `document_name` · `excerpt` · `publication_date`
Subagents emit these as **data**; synthesis agent **preserves and merges** them. Synthesis is the #1 failure point.

## Conflicting sources
Two credible values → **annotate both** with source + date; let the reader decide.
❌ pick most recent · ❌ average · ❌ pick "most authoritative".

## Temporal awareness
2023: 8% vs 2024: 12% = **trend, not contradiction**. Require publication/collection dates in all outputs.

## Content-appropriate rendering
| Content | Format |
|---|---|
| Financial data | Tables |
| News | Prose |
| Technical findings | Structured lists |
Never flatten everything into one format.

## Wrong answers
Paraphrasing without mappings; resolving conflicts by picking one; missing dates; uniform formatting.
