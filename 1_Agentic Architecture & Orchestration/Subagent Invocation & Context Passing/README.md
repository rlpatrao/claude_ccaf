# 1.3 Subagent Invocation and Context Passing

**Domain:** 1. Agentic Architecture & Orchestration
**Exam task statement:** Configure subagent invocation, context passing, and spawning.

## Learning objectives

- Define subagents in the Claude Agent SDK and in Claude Code.
- Pass context to subagents explicitly and in structured form.
- Spawn independent subagents in parallel.

## Concepts to study

- A coordinator can spawn subagents only if the subagent tool (`Task`, named `Agent` in newer releases; check your version) is in its allowed tools.
- Agent SDK `AgentDefinition` fields: `description` (used for routing), `prompt`, `tools`, `model`.
- Claude Code subagents: Markdown files in `.claude/agents/` (project) or `~/.claude/agents/` (user) with YAML frontmatter (`name`, `description`, `tools`, `model`). Inspect them with `/agents`.
- Parallel spawning: the coordinator emits several subagent tool calls in a single response.
- Structured context passing: keep content separate from metadata (source URL, date, page number) so provenance survives.
- Restrict each subagent's tools to its role.

## Hands-on lab

You write all code and configuration for this lab inside this folder. Claude reviews your work and gives hints; it does not write the solution.

**Build:** Two variants. (a) A read-only reviewer subagent in Claude Code, defined in a scratch repository. (b) An Agent SDK script with a coordinator and two subagent definitions spawned in parallel.

**Steps**

1. In Claude Code, run `/agents` and review the options. Write a `code-reviewer` subagent restricted to Read, Grep, and Glob.
2. Invoke it and confirm it cannot edit files.
3. In the Agent SDK, define two subagents with distinct descriptions. Confirm from logs that the coordinator routes each request to the correct one.
4. Remove the subagent tool from the coordinator's allowed tools and record the resulting behaviour.
5. Request two independent analyses and confirm both subagents are spawned in the same coordinator turn.

**Done when**

- [ ] Subagent tool restrictions are enforced.
- [ ] You can explain, from logs, which subagent was selected and why.

## Exam traps

- Omitting the subagent tool from the coordinator's `allowedTools`.
- Vague subagent descriptions that cause incorrect routing.
- Passing a prose summary that discards source metadata.

## Self-check questions

1. A coordinator never delegates even though subagents are defined. What do you check first?
2. How do you make two subagents run concurrently?
3. Why should content and metadata be passed to a subagent as separate fields?

## Working with Claude on this module

- `start 1.3`: Claude restates the objective and asks how you plan to approach it.
- `hint`: the next step on the hint ladder (concept, then API or documentation section, then pseudocode).
- `review my 1.3 lab`: Claude reads your files and reports gaps against this guide.
- `quiz me on 1.3`: scenario-based multiple-choice questions in the exam style.

## My notes

_Record what you built, what failed, the traceback, and the fix._
