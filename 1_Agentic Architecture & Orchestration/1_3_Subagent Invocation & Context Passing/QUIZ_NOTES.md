# Quiz Notes: 1.3 Subagent Invocation and Context Passing

Socratic quiz session held on 10 November 2026, covering Domain 1, Task Statement 1.3 (Subagent Invocation and Context Passing). This file records the questions, the key concepts tested, the model answers, and the areas identified for revision.

Naming note: the exam material calls the subagent-spawning tool **Task**. In current Claude Code and the Agent SDK the same tool appears as **Agent**. The exact version of the change, and whether "Task" remains an accepted alias, were not confirmed in this session. Check the current Agent SDK documentation before writing the lab. For the exam, read "Task" as the subagent-spawning tool.

---

## Key concepts

### 1. Task tool and AgentDefinition

- The Task tool is the mechanism a coordinator uses to spawn subagents.
- "Task" must be in the coordinator's `allowedTools`. This is a hard requirement: without it the coordinator cannot spawn any subagent, however many are defined.
- Subagents are declared separately, each in an AgentDefinition. The Task tool does not define which subagents exist.

| AgentDefinition field | Purpose |
|---|---|
| description | What the subagent does and when to use it. The coordinator uses this field to select a subagent. |
| prompt | The subagent's system prompt (instructions and role). |
| tools | The tools the subagent may use, restricted to its role. |

In the Agent SDK, a subagent's name is usually the key under which its definition is registered, not a field of the definition. An optional model field also exists. Check the current SDK documentation for the exact shape.

### 2. Context passing rules

| Rule | Statement |
|---|---|
| Rule 1: complete findings | Include the complete findings from prior agents in the subagent's prompt. A subagent cannot look up another agent's results. |
| Rule 2: structured metadata | Pass findings as structured data that separates content from metadata: claim, source_url, document_name, page_number, confidence. Without metadata, downstream agents cannot attribute claims. |
| Rule 3: goal-oriented prompts | Specify goals and quality criteria, not step-by-step procedures. Goal-oriented prompts let the subagent adapt to inputs the coordinator did not anticipate. |

### 3. Attribution failure pattern

When a synthesis agent produces unsourced claims, the root cause is usually that the coordinator passed content without structured metadata. The synthesis agent cannot cite sources it was never given. The fix is context passing with metadata. Changing the synthesis agent's prompt or giving it direct tool access does not fix it.

### 4. Parallel spawning

Emit multiple Task tool calls in a single coordinator response to spawn independent subagents at the same time. Spawning them one per turn adds unnecessary latency. Tasks that depend on another task's output must remain sequential.

### 5. `fork_session` and `--resume`

| Option | Behaviour | Use for |
|---|---|---|
| `fork_session` | Creates an independent branch from a shared session baseline. Branches do not see each other's work. | Divergent exploration from a common starting point |
| `--resume` | Continues the same session with its full history. | Continuation, for example after an interruption |

`fork_session` (branching a whole session) is a different feature from the subagent fork discussed in 1.2 (a subagent that starts with a copy of the coordinator's conversation).

### Anti-patterns

- "Task" missing from the coordinator's `allowedTools`.
- Passing content without metadata, which causes attribution failures.
- Procedural coordinator prompts instead of goal-oriented ones.
- Spawning independent subagents sequentially across separate turns.
- Confusing `fork_session` with `--resume`.

---

## Questions and model answers

### Question 1: The Task tool

**Question.** What is the Task tool, and why must it be included in the coordinator's `allowedTools`?

**Model answer.** The Task tool is the mechanism a coordinator uses to spawn subagents. Without it in `allowedTools`, the coordinator cannot spawn any subagent, regardless of how many AgentDefinitions exist. The Task tool does not define which subagents are available; AgentDefinitions do. A common exam distractor describes a coordinator with well-written subagent definitions that never delegates; the cause is a missing Task entry in `allowedTools`.

### Question 2: AgentDefinition fields

**Question.** What are the three key fields of an AgentDefinition, what does each do, and which does the coordinator use for selection?

**Model answer.** description (what the subagent does and when to use it; used by the coordinator for selection), prompt (the system prompt), and tools (tools restricted to the subagent's role). A vague description such as "Helps with research" leads to poor routing; "Searches the web for recent sources and returns claims with URLs" tells the coordinator exactly when to use the subagent.

### Question 3: Rule 1, complete findings

**Question.** The coordinator invokes the synthesis subagent with "Write a report synthesising the findings returned by the web search agent." The synthesis subagent has file reading and web search tools. What is likely to happen, and which rule has been broken?

**Model answer.** The prompt refers to the findings but does not contain them. The synthesis subagent cannot access another agent's output, so it will either write a report with nothing behind it or run its own searches, duplicating work with sources that may differ from the verified ones. The coordinator has broken Rule 1: include the complete findings in the subagent's prompt. Over-broad tool access makes the failure worse but is not its cause.

### Question 4: Rule 2, structured metadata

**Question.** The coordinator now passes the findings as a block of summarised prose. The report is fluent, but a reviewer complains about one specific weakness. What is it, and how should the findings have been formatted?

**Model answer.** Claims have no source attribution, because summarising into prose discards URLs, document names and page numbers. The coordinator should pass structured records that separate content from metadata:

| Field | Example |
|---|---|
| claim | Solar capacity grew 30% last year, mainly in China |
| source_url | https://example.org/solar-report-2025 |
| document_name | Global Solar Outlook 2025 |
| page_number | 14 |
| confidence | high |

### Question 5: Rule 3, goal-oriented prompts

**Question.** Compare Prompt A ("Step 1: Read the first finding. Step 2: Write a paragraph about it. Step 3: Add its citation. Step 4: Repeat for each finding. Step 5: Write a conclusion.") with Prompt B ("Produce a report for policy analysts on renewable energy trends. Every claim must cite its source from the findings provided. Flag claims marked low confidence. Group related findings by theme and highlight where sources disagree."). Which is better, and why?

**Model answer.** Prompt B. Prompt A is procedural: it fixes the steps but does not define a good result, so when two sources contradict each other it produces two correctly cited but conflicting paragraphs without noticing the conflict. Prompt B states the goal and quality criteria, so the subagent can adapt to inputs the coordinator did not anticipate. Rule 3: specify goals and quality criteria, not step-by-step procedures.

### Question 6: Attribution failure pattern

**Question.** A synthesis agent's report contains uncited claims. The team proposes Fix 1 (add "You must always cite a source for every claim" to the synthesis prompt) and Fix 2 (give the synthesis agent web search to find sources itself). The coordinator's logs show it passed findings as plain prose with no URLs or document references. Will either fix work? What is the root cause and the correct fix?

**Model answer.** Neither fix works.

- Fix 1: instructing the agent to cite sources it does not have is likely to produce fabricated citations. It is acceptable as reinforcement once metadata is passed, but it is not the fix.
- Fix 2: the agent would attach newly found sources to claims that originated elsewhere, producing plausible but possibly unsupported citations and duplicating work.

Root cause: the coordinator passed content without metadata. Correct fix: change the coordinator's context passing to send structured findings (claim, source_url, document_name, page_number, confidence).

### Question 7: Parallel spawning

**Question.** A coordinator needs three independent research tasks (EU, US, Asia-Pacific regulation). Its logs show one Task call per turn, each waited on before the next. Each subagent takes about two minutes. What is wrong, and how should it spawn them?

**Model answer.** Sequential spawning of independent tasks takes about six minutes instead of about two. The coordinator should emit three Task tool calls in a single response so the subagents run at the same time, then collect all three results. This applies only to independent tasks; dependent steps must remain sequential.

### Question 8: `fork_session` and `--resume`

**Question.** After a long analysis of a codebase, you want to explore two competing refactoring approaches (microservices and modular monolith) from the same analysis, without either affecting the other. Do you use `--resume` or `fork_session`?

**Model answer.** `fork_session`. It creates independent branches from the shared analysis, and neither branch sees the other's work. `--resume` continues the same session, so the second exploration would carry the first's reasoning and any bias it introduced. Fork for divergent exploration; resume for continuation.

### Final scenario: Tracing the attribution failure

**Question.** A synthesis agent produces a report in which several claims have no source attribution. Its prompt and tool set are unchanged from when its reports were fully cited. The web search and document analysis subagents are working correctly and return well-sourced results in the same format as always. What is the most likely root cause?

**Model answer.** The coordinator. Elimination along the chain:

```
Web search / document analysis  →  Coordinator  →  Synthesis agent  →  Report
```

1. The subagents return well-sourced results, so the sources exist when the findings leave them.
2. The synthesis agent is unchanged and previously produced fully cited reports, so it can cite when given sources.
3. The only remaining component is the coordinator. It is most likely passing the findings as prose or as claim text only, dropping the metadata fields. Typical causes are a coordinator prompt edit (for example "summarise the findings before passing them on"), a change to how it builds the synthesis prompt, or truncation added to save tokens.

Confirmation: check the coordinator's logs for the exact input the synthesis agent received. Centralised routing means this input is recorded in one place. Fix: restore structured context passing in the coordinator.

---

## Assessment from this session

| Concept | Assessment |
|---|---|
| Task tool and `allowedTools` | Partial. Knew subagents cannot run without it, but described Task as defining which subagents exist. |
| AgentDefinition fields | Strong. Identified description as the selection field. |
| Rule 1: complete findings | Missed initially. Focused on tool scope rather than the missing findings. |
| Rule 2: structured metadata | Good. Identified missing citations; the field-level format was supplied. |
| Rule 3: goal-oriented prompts | Correct choice, partial reasoning (grouping rather than goals and quality criteria). |
| Attribution failure pattern | Partial. Recognised the need for metadata but placed the fix in the synthesis prompt. |
| Parallel spawning | Concept correct; mechanism (multiple Task calls in one response) missing. |
| `fork_session` and `--resume` | Strong. |
| Final scenario | Correct with scaffolding. |

## Areas to revise

1. **Fix failures upstream, at the coordinator.** This recurred in 1.2 and 1.3. When a downstream agent is capable and unchanged but its output is wrong, examine what it was given. Options that change the downstream agent's prompt or tools are usually distractors.
2. **Mechanism versus definition.** The Task tool (Agent in current tooling) spawns subagents. AgentDefinitions declare them. Both are required.
3. **Exact mechanisms.** Learn the precise wording: "multiple Task calls in a single coordinator response" for parallel spawning; "goals and quality criteria, not step-by-step procedures" for Rule 3.
4. **Apply Rule 1 first.** When a subagent prompt refers to earlier work ("the findings", "the topic we discussed", "last time"), check whether that content is actually included in the prompt.
