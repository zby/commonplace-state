---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/claude-code-dynamic-workflows-docs.md"
source_has_frontmatter: true
date: "2026-06-03"
depth: standard
---

# Connection Report: Orchestrate subagents at scale with dynamic workflows

**Source:** [Claude Code dynamic workflows docs](../../../sources/claude-code-dynamic-workflows-docs.md)

This source is an **immutable snapshot** under `kb/sources/`. Per the sources `COLLECTION.md`, the snapshot itself never authors outbound links; its active connection surface would be a future `claude-code-dynamic-workflows-docs.ingest.md` (which does not yet exist). The load-bearing signal for a snapshot is therefore **reverse-edge candidates** — library notes that should add `evidence` / `derived-from` links pointing at this snapshot. `Connections Found` below records outbound edges for whoever authors the ingest report.

## Discovery Trace

**Index scan:**
- Read [notes dir-index](../../../notes/dir-index.md) — flagged the orchestration/scheduler-persistence cluster: `rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents`, `orchestration-strategies-and-run-state-have-opposite-persistence`, `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence`, `the-practical-scheduler-is-the-host-language`, `agent-orchestration-occupies-a-multi-dimensional-design-space`, `agent-orchestration-needs-coordination-guarantees`, `bounded-context-orchestration-model`. Also flagged `the-chat-history-model-trades-context-efficiency`, `session-history-should-not-be-the-default-next-context`, `synthesis-is-not-error-correction`, `error-correction-works-above-chance-oracles-with-decorrelated-checks`, `conversation-vs-prompt-refinement`.
- Read [agent-memory-systems dir-index](../../../agent-memory-systems/dir-index.md) — no system-review match; this is a product-feature doc, not a memory system. No candidate.

**Topic indexes:**
- Source `tags: [documentation]` carries no KB topic tag, so no tag-index lookups. Cluster located via the dir-index scan instead.

**Body search:**
- `rg -i "dynamic workflow|ultracode|deep-research" kb/notes/ kb/reference/` — **no hits**. No existing note names this feature; the source is fresh coverage.
- `rg -i "orchestrat" kb/notes/` — returned the scheduler cluster above (llm-mediated-schedulers, codified-scheduling-patterns, tool-loop-optional, scheduler-llm-separation, bounded-context-orchestration-model, rlm*, the-practical-scheduler, orchestration-strategies-and-run-state).

**Link following:**
- From `rlm-has-the-model-write-ephemeral-orchestrators` followed links to `orchestration-strategies-and-run-state-have-opposite-persistence`, `ephemeral-computation-prevents-accumulation`, `deploy-time-learning-is-the-missing-middle`, `the-practical-scheduler-is-the-host-language`. This cluster is the strongest match: the docs describe an LLM-authored orchestration script (RLM-style) whose intermediate results live in **script variables, not Claude's context** (docs "How a workflow runs" + the comparison table row "Where intermediate results live → Script variables"), and which can be **saved as a reusable command** (`/workflows` → `s`) — a concrete product instance of the "promote the recurring `select`-fragment" move in `orchestration-strategies-and-run-state`.
- Confirmed a parallel snapshot exists: [a-harness-for-every-task-dynamic-workflows-in-claude-code](../../../sources/a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md) (an X article on the same feature), which already has its own connect report.

## Connections Found

(Recommended outbound edges for a future `claude-code-dynamic-workflows-docs.ingest.md`; labels from the sources→notes authorised set: `evidence`, `derived-from`, `rationale`.)

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — **evidence**: a shipped system where the model writes the orchestrator as code and intermediate results live in script variables rather than the conversation, corroborating the "model writes the orchestrator rather than being it" claim — and unlike RLM, the workflow script is saveable, making it the non-ephemeral counterpoint.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — **evidence**: the save-script-as-command flow promotes the recurring `select`-strategy to durable library code while per-run results stay ephemeral in script variables — a real product realising the note's lifecycle split. Note is `status: seedling`; `evidence` is additive, not load-bearing, so no flag needed.
- [The chat-history model trades context efficiency for implementation simplicity](../../../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) — **evidence**: workflows keep intermediate agent results out of Claude's context window (only the final answer lands there), a concrete design that avoids the chat-history default the note critiques.

## Bidirectional Candidates

None. The source is an immutable snapshot and authors no links; return paths are covered by Reverse-edge Candidates.

## Reverse-edge Candidates

(Notes that should author an `evidence`/`derived-from`/`compares-with` link **to** this snapshot under their own `COLLECTION.md` rules. This is the primary signal for a snapshot.)

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) → source — **evidence/contrast**: this snapshot is a shipped instance of model-authored orchestration over sub-agents; the note's "Ephemerality" section would gain a real-world contrast (workflows make the orchestrator saveable, the exact path RLM opts out of).
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) → source — **evidence**: the docs' save-as-command + script-variable model is the clearest deployed example of the note's persistence split (promote recurring `select`, keep run-state `K` ephemeral); a strong candidate to cite as evidence for the "third mode on the authorship axis".
- [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](../../../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) → source — **evidence**: dynamic workflows are a fourth placement point (model-authored, but promotable to a durable command), worth citing where the note maps the persistence-boundary spectrum.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source — **evidence**: the docs' own comparison table (subagents / skills / agent teams / workflows across "who decides next", "where results live", "what's repeatable", "scale", "interruption") is a practitioner instance of the multi-axis framing the note argues for, not a single ladder.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) → source — **evidence**: `/deep-research` "votes on each claim" and filters claims that "didn't survive cross-checking" — a shipped product choosing voting/filtering over merge-everything synthesis, exactly the distinction the note draws.

## Off-authorisation Candidates

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) — connects because workflows run agents in an isolated environment whose results stay in script variables rather than becoming the next context, instancing the note's claim that storing history and loading it next are separable decisions. The sources→notes authorised set (`evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, `see-also`) does cover this with `evidence`; it is recorded here only because the overlap is weaker than the three `Connections Found` above (the docs never frame this as a context-loading choice). Suggest the ingest author include it as a secondary `evidence` edge if the framing holds, otherwise drop as too oblique. No authorisation gap.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the docs' "independent agents adversarially review each other's findings" and `/deep-research` cross-checking are an applied case of decorrelated checks, but the docs give no oracle/TPR-FPR detail, so the link is thematic rather than evidential. `evidence` is authorised; recorded here as a judgment call — include only if the ingest author judges the adversarial-review description concrete enough to count as evidence. No authorisation gap.

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — surfaced via the orchestration scan, but the docs do not discuss conversation-vs-prompt handoff between agents; the "results in script variables" point is already better captured by the chat-history and RLM edges. Keyword-adjacent only.
- [agent-orchestration-needs-coordination-guarantees-not-just](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — the docs describe coordination *channels* (script variables, shared task lists in the comparison table) but make no claim about coordination *guarantees*; following the link would not give a reader anything the docs support.
- [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md) — the formal select/call model is upstream of the RLM note rather than a direct match for a product doc; the RLM edge already routes a reader here one hop. Too abstract to author directly from the snapshot.

## Index Membership

None. Snapshots are not added to curated notes indexes; the source belongs to the auto-generated [sources dir-index](../../../sources/dir-index.md), which regenerates on refresh.

## Synthesis Opportunities

The two dynamic-workflow snapshots ([this docs capture](../../../sources/claude-code-dynamic-workflows-docs.md) and the [X-article harness capture](../../../sources/a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md)) together with the RLM cluster could ground a note that dynamic workflows are the **saveable** counterpoint to RLM's ephemeral orchestrators — a deployed instance of the "self-populating host-language scheduler" / test-gated orchestrator cache that `orchestration-strategies-and-run-state-have-opposite-persistence` predicts. The save-as-command flow is the missing real-world example that note currently lacks. Do not create the note during connect; flagged for a future writer.

## Maintenance Observations

- Two snapshots now cover the same Claude Code dynamic-workflows feature from different angles (official docs vs. an X practitioner article). Not a duplication problem (different capture sources, both legitimately immutable), but a future ingest pass should cross-reference them with `compares-with` so a reader landing on one finds the other. Recorded here, not authored.

## Flags

- **No existing note names this feature** — `rg` for "dynamic workflow", "ultracode", "deep-research" returned zero hits across `kb/notes/` and `kb/reference/`. The feature is fresh source material; the strongest action is the Synthesis Opportunity above plus the reverse-edge `evidence` citations into the RLM/persistence cluster.
- Source `type` is `kb/sources/types/snapshot.md` with no `.ingest.md` companion yet — the `Connections Found` edges have no authored surface to live on until an ingest report is written.
