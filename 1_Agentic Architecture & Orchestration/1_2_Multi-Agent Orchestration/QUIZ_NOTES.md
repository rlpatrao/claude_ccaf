# Quiz Notes: 1.2 Orchestration Patterns

Socratic quiz session held on 9 November 2026, covering Domain 1, Task Statement 1.2 (Orchestration Patterns). This file records the questions, the key concepts tested, the model answers, and the areas identified for revision.

---

## Key concepts

### 1. Hub-and-spoke architecture

A coordinator agent sits at the centre (the hub). Subagents are the spokes and each handles a specialised task. All communication flows through the coordinator. Subagents never communicate directly with each other.

Centralising communication provides three benefits:

| Benefit | Meaning |
|---|---|
| Observability | Every message passes through one point, so it can be logged, monitored and traced there. |
| Consistent error handling | The coordinator applies one recovery policy (retry, re-delegate, or report the gap) to every subagent failure. |
| Controlled information flow | The coordinator decides what context each subagent receives. Nothing moves between agents without passing through it. |

### 2. Isolation principle

- Subagents do not inherit the coordinator's conversation history.
- Subagents do not share memory between invocations. A second call to the same subagent has no knowledge of the first.
- Everything a subagent needs must be written into its prompt explicitly.

Note on current tooling (checked 29 October 2026): Claude Code and the Agent SDK provide one exception, a fork, which copies the coordinator's conversation at start. Forks are on by default from Claude Code v2.1.302. Every other subagent, including a custom one, starts fresh. The exam tests the fresh-start case.

### 3. Coordinator responsibilities

| Responsibility | Description |
|---|---|
| Dynamic subagent selection | Analyse what the query requires and invoke only the subagents it needs, rather than always running the full pipeline. |
| Research scope partitioning | Assign distinct subtopics to each subagent, with explicit boundaries, to reduce duplication. |
| Iterative refinement loop | Evaluate combined output for gaps and re-delegate with specific, self-contained prompts before passing results on. |
| Centralised communication routing | Route all messages through the coordinator for observability and error handling. |

### 4. Narrow decomposition failure

When a coordinator decomposes a broad topic too narrowly, entire categories are never assigned and therefore never researched. The root cause is the coordinator's decomposition, not any downstream subagent. The fix is better decomposition: identify the major categories of the topic first, then partition the work across them.

### Anti-patterns

- Direct subagent-to-subagent communication (breaks observability).
- Assuming subagents share context or memory.
- Running every query through the full pipeline regardless of complexity.
- Adding more subagents to fix a decomposition problem.

---

## Questions and model answers

### Question 1: Hub-and-spoke

**Question.** In a multi-agent orchestration system, what is the hub-and-spoke architecture, and what role does the coordinator play?

**Model answer.** The coordinator sits at the centre and the subagents are spokes. The coordinator plans and decomposes the task, decides what context each subagent receives, and aggregates the results. All communication flows through the coordinator; subagents never communicate directly with each other.

### Question 2: Benefits of centralised routing

**Question.** A research subagent finds sources that the analysis subagent will need. A colleague proposes letting the research subagent send its findings directly to the analysis subagent, because that would be faster. What would be lost? Name three benefits of routing everything through the coordinator.

**Model answer.** Observability, consistent error handling, and controlled information flow. A direct link hides traffic from the coordinator, requires per-pair error logic, and removes the coordinator's control over what context each agent receives.

### Question 3: Isolation (conversation history)

**Question.** After a long conversation establishing the user's requirements, the coordinator calls a web search subagent with "Find recent sources on the topic we discussed." What will the subagent do, and why?

**Model answer.** The subagent does not inherit the coordinator's conversation history, so "the topic we discussed" refers to nothing it knows. It will guess or return generic results. A subagent run non-interactively usually cannot ask a clarifying question. The coordinator must state the topic explicitly in the prompt.

### Question 4: Isolation (memory between invocations)

**Question.** The coordinator receives ten sources from the web search subagent, then calls it again with "Find five more sources, but do not repeat any you found last time." What goes wrong, and how should the second call be worded?

**Model answer.** Each invocation starts fresh, so "last time" has no meaning and duplicates are likely. The coordinator holds the state and must pass the list of sources already found, asking for five that are not on it. An external memory store is a valid design, but the coordinator must still tell the subagent what to read from it.

### Question 5: Dynamic subagent selection

**Question.** A system has four subagents (web search, document analysis, synthesis, report writing), and the coordinator sends every query through all four in order. A user asks, "What is the current version of the Python `requests` library?" What is wrong, and what should the coordinator do instead?

**Model answer.** The coordinator is not analysing the query before selecting subagents. A single factual lookup needs only the web search subagent. Running the full pipeline adds latency and token cost and pads a one-line answer into a report. The coordinator should select subagents according to what the query requires.

### Question 6: Research scope partitioning

**Question.** For "How is AI being regulated around the world?", the coordinator starts three parallel web search subagents with the same prompt: "Research AI regulation worldwide." What problem will this cause, and how should the subagents be briefed?

**Model answer.** Identical prompts produce overlapping results and duplicated cost. The coordinator should partition the topic into distinct subtopics (for example EU, US, and China with the wider Asia-Pacific region) and state each subagent's boundaries in its prompt.

### Question 7: Iterative refinement loop

**Question.** The EU and US findings are detailed, but the Asia-Pacific findings contain two short paragraphs on China only, with no mention of Japan, South Korea, India or Singapore. What should the coordinator do before passing findings to the report writer?

**Model answer.** Evaluate the output for gaps and re-delegate with a specific, self-contained prompt, for example: "Research AI regulation in Japan, South Korea, India and Singapore. China is already covered; do not repeat it." A more thorough first-round prompt is good practice but does not replace the evaluate-and-re-delegate loop.

### Question 8: Narrow decomposition failure

**Question.** For "the impact of AI on creative industries", the coordinator decomposes the topic into digital illustration, graphic design and photography. Each subagent does thorough work, but the report omits music, writing and film. A team member proposes adding two more search subagents. Will that fix the problem? Where does the failure originate?

**Model answer.** The failure originates in the coordinator's decomposition, which covered only visual arts. Adding subagents will not fix it; with the same decomposition, extra subagents would only research visual arts in more depth. The fix is to identify the major categories first (visual arts, music, writing, film, and so on) and then partition.

### Final scenario: Tracing the root cause

**Question.** A multi-agent system produces a report on renewable energy that covers only solar and wind. Each subagent did thorough work on its assigned topic. Which option addresses the root cause?

- A. Improve the web search subagent's queries.
- B. Add a fact-checking subagent.
- C. Give the synthesis subagent a larger context window.
- D. Revise how the coordinator decomposes the topic.

**Answer.** D.

- A is wrong: better queries improve the solar and wind research but still cover only solar and wind.
- B is wrong: fact-checking verifies what is present, not what is missing. This is the "add another agent" anti-pattern.
- C is wrong: a larger context window cannot hold findings that were never produced. Hydroelectric, geothermal, biomass and tidal power were never assigned.
- D is correct: the coordinator split the topic into only two categories. It should identify the main categories first and then partition the research across them.

The phrase "each subagent did thorough work" signals that the failure is upstream, in the coordinator.

---

## Assessment from this session

| Concept | Assessment |
|---|---|
| Hub-and-spoke and coordinator role | Sound on planning, context passing and aggregation. Initially omitted that subagents never communicate directly. |
| Three benefits of centralised routing | Partial. Controlled information flow identified; observability and consistent error handling were supplied. |
| Isolation principle | Strong. Both questions answered correctly with the correct fix. |
| Dynamic subagent selection | Partial. Noted the sequential delay but not the need to match subagents to query complexity. |
| Research scope partitioning | Strong. |
| Iterative refinement loop | Strong. |
| Narrow decomposition failure | Correct in the open question (Question 8); missed in the multiple-choice final scenario. |

## Areas to revise

1. **The three benefits, by name:** observability, consistent error handling, controlled information flow. Exam options often paraphrase them.
2. **Dynamic selection:** for any scenario describing a fixed pipeline, ask whether this query needs every stage.
3. **Tracing failures to their origin under option pressure:** when subagents worked well but the output is incomplete, look for the coordinator-level option first. Be cautious of options that improve a downstream component (more context, better queries, an extra agent).
