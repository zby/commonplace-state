---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/the-agent-loop-architecture-2067677007140278630.md"
source_has_frontmatter: true
date: "2026-06-19"
depth: standard
---

# Connection Report: The Agent Loop Architecture

**Source:** [The Agent Loop Architecture](../../../sources/the-agent-loop-architecture-2067677007140278630.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/sources/COLLECTION.md`; snapshots are immutable, and active authored connections belong in the matching `.ingest.md`. Authorised destinations are notes, sources, agent-memory-systems, and agentic-systems, with `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and sparse `see-also` labels.
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agentic-systems/README.md`, and `kb/agent-memory-systems/README.md`.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ kb/agent-memory-systems/ --glob '*.md'`. Flagged candidates around tool loops, deploy-time learning, runtime decomposition, durable run-state, diagnostic richness, GBrain, Claude Code dynamic workflows, and repo-backed skill systems.

**Topic indexes:**
- Read [tool-loop](../../../../tags/tool-loop-README.md). Kept the local cluster around [the practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md), [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md), [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), and [orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md).
- The source carries `tags: [x-article]`; no matching source-family topic README exists, so no tag README shortcut applied.

**Body search:**
- `rg -n "durable|orchestrat|checkpoint|agent loop|tool loop|loop|skill|skills|deploy-time|cron|observability|self-modif|sidecar|workflow|workflow" kb/notes kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'` -- found strong matches in tool-loop theory and external agentic-system analyses; broad memory-system hits were mostly rejected unless they concerned skills as durable behavior-shaping artifacts or runtime self-modification.
- `rg -n "Inngest|utah|durable execution|step\\.run|step.invoke|agent loop architecture|Farrelly|djfarrelly" kb --glob '*.md'` -- only this snapshot matched, so there is no existing Inngest/Utah coverage.

**Link following:**
- From [the practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md), followed links to [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md), and [orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md). Kept the first and third as direct candidates; the framework note is useful context but less directly changed by this source.
- From [deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), followed to [continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md). Kept deploy-time learning; continual learning is already covered by that broader note for this source.
- From [diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), kept the connection because the source's step-level run history and failed-skill review loop give a practitioner operationalization of retained diagnostic evidence.
- From [agentic-systems/README.md](../../../../agentic-systems/README.md), opened [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) and [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md). Kept both as `compares-with` candidates: each is already an inspected shipped instance of the same loop/orchestrator/durable-skill design space.

## Connections Found

- [the practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) -- **evidence**: the source gives production failure cases for the note's lifetime-mismatch boundary: once a loop must survive restarts, avoid duplicate side effects, and resume from last successful step, operative `K` can no longer live only in host-language locals.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) -- **evidence**: the source distinguishes checkpointed run history from durable skills that persist beyond a conversation, supporting the split between within-run run-state durability and cross-task promotion of reusable control strategies.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**: the source frames deployed skills as institutional knowledge encoded in executable infrastructure that survives process restarts and model swaps, a concrete practitioner instance of durable system-definition artifacts updated during deployment.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **evidence**: the source's observability claims make run history, step inputs, outputs, retries, and failure hooks the trust substrate for agents that author and revise skills.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **evidence**: the source independently decomposes production agent loops into loop, skill, and orchestrator; this maps mostly to scheduler plus execution substrate and adds a durable-execution emphasis not foregrounded in the existing runtime taxonomy.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- **compares-with**: GBrain's dream cycle, Minions durable job queue, crash-resumable subagent loops, and SkillOpt self-modification are a code-inspected instance of the architecture the source describes at a practitioner/product level.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: dynamic workflows expose model-authored orchestrators over sub-agents with session-local journaling and save-as-command promotion, which contrasts with the source's stronger durable-execution and hot-deployed function model.

## Bidirectional Candidates

- [the practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) <-> source -- **evidence**: a future edit could cite this source exactly at the note's scope boundary about lifetime mismatch forcing `K` to become checkpointable external state.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) <-> source -- **evidence**: a future edit could use the source as a practitioner example of why autonomous skill authorship makes step-level traces and retry history part of the learning substrate, not just monitoring.

## Reverse-edge Candidates

- [the practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) → source -- **evidence**: under the notes collection rules, the note should cite this snapshot as corroborating evidence for the within-run durability boundary.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) → source -- **evidence**: the note should cite this snapshot where it separates checkpointed run state from promoted reusable skills/control strategies.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) → source -- **evidence**: the note should cite this snapshot as another practitioner runtime taxonomy, especially for the execution-substrate role of durable orchestration.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) -- rejected as a primary connection because the source assumes durable orchestration rather than arguing the API exposure question this note centers; useful background, but weaker than the practical-scheduler and runtime-decomposition links.
- [Stateful tools recover control by becoming hidden schedulers](../../../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) -- rejected because the source is about explicit durable orchestration, not the covert stateful-tool escape hatch.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- rejected as redundant with [deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), which is the better landing point for skills as durable behavior-changing artifacts.
- [getsentry/skills review](../../../../agent-memory-systems/reviews/getsentry-skills.md) -- rejected as too distribution-focused: it covers repo-backed skill packages, but not durable loop execution or orchestrator-owned run state.

## Index Membership

- [tool-loop](../../../../tags/tool-loop-README.md) -- source could be cited in the downstream consequences or related approaches area as a practitioner argument for durable execution below agent loops.
- [Agentic Systems](../../../../agentic-systems/README.md) -- if Inngest/Utah receives a code-grounded review later, it belongs here as an external agentic harness/orchestration system.

## Synthesis Opportunities

- Existing notes distinguish three persistence questions that the source bundles together: within-run run-state checkpointing, cross-task promotion of reusable skills/control strategies, and retained diagnostic history for skill-improvement loops. A future synthesis note could argue that durable agent-loop infrastructure must separate these three persistence targets instead of treating "durability" as one property.

## Maintenance Observations

None

## Flags

- No Inngest/Utah code-grounded review exists. If the project is important, snapshot or review `github.com/inngest/utah` separately before promoting source claims about the implementation.
