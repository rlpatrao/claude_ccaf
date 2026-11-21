# Cheat Sheet — 4.3 Structured Output with Tool Use

## Reliability hierarchy
`tool_use` + JSON schema **eliminates syntax errors** > prompt-based JSON (missing brackets, trailing commas, unquoted keys).
Current API also has `strict: true` and `output_config.format` — exam uses the two-tier framing.

## tool_choice
| Mode | Guarantee | Use |
|---|---|---|
| `auto` | None — may return text | General |
| `any` | Some tool called | Structured output, **unknown doc type** |
| `{type:"tool",name}` | That tool | Mandatory first step (e.g. metadata) |
(`none` exists in API; exam names three.) Newer models reject `any`/forced → `auto` + `strict: true`.

## Schemas do NOT prevent semantic errors
- Sums that don't match totals
- Values in the wrong field
- **Fabrication** for required fields
→ validate separately (see 4.4).

## Schema design
- Fields the source may lack → **optional / nullable** (required = pressure to fabricate).
- Enums: add **`"unclear"`** for ambiguity; **`"other"` + detail string** for extensibility.
- Put format-normalisation rules in the prompt alongside the schema.

## Wrong answers
"tool_use prevents all errors"; all fields required; `auto` for guaranteed output; enums without unclear/other.
