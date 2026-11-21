# Cheat Sheet — 5.1 Context Window Management

## Problems → fixes
| Problem | Fix |
|---|---|
| **Progressive summarisation** loses $ amounts, dates, order #s | **Persistent case facts block** — structured, prepended every turn, never summarised (one entry per issue) |
| **Lost in the middle** — findings buried mid-input missed | **Structural**: key-findings summary at the **start** + explicit section headers |
| Verbose tool results (40+ fields, 5 relevant) | **Trim before** they enter history (PostToolUse hook or in the tool) |
| Upstream agents return long reasoning chains | Return **structured data** (facts, citations, relevance, metadata) |

## Stateless API
Every request needs **full history**. Ad-hoc truncation loses facts. (Docs now add deliberate *context editing*.)

## Most important pattern
**Persistent case facts block.**

## Wrong answers
- Summarisation is "safe" for transactional data
- "Tell the model to pay attention to everything"
- Keep full tool results "just in case"
- Drop old messages to save tokens
- Bigger context window as the fix

Scope note: prompt caching — only know it exists and its purpose.
