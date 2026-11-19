---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/agent-memory-systems/reviews/stash.md"
source_has_frontmatter: true
date: "2026-04-25"
depth: standard
---

# Connection Report: Stash

**Source:** [Stash](../../../../agent-memory-systems/reviews/stash.md)

## Discovery Trace

**Source and rules read:**
- Read [Stash](../../../../agent-memory-systems/reviews/stash.md). The review describes a Go MCP memory service using Postgres/pgvector, raw embedded episodes, incremental consolidation into typed facts, relationships, causal links, goals, failures, hypotheses, contradictions, confidence decay, and a namespaced `/self` convention.
- Read [agent-memory-systems collection rules](../../../../agent-memory-systems/COLLECTION.md). Authorised outbound destinations include `kb/agent-memory-systems/`, `kb/reference/`, `kb/notes/`, `kb/sources/`, and sparse `kb/instructions/`. Useful labels for this pass: `compares-with`, `see-also`, `rationale`, `evidence`, `defined-in`, and `derived-from`.
- Read [connect report type](../../../../types/connect-report.md). This report is discovery-only and does not mutate the source note, target notes, or indexes.

**Indexes read:**
- Read [agent-memory-systems review index](../../../agent-memory-systems/reviews/dir-index.md) and [agent-memory-systems root index](../../../agent-memory-systems/dir-index.md). Kept candidates around service-owned trace backends, Postgres/pgvector memory services, MCP surfaces, typed memory roles, confidence decay, and failure/procedural learning.
- Read [notes directory index](../../../notes/dir-index.md). Kept candidates around agent memory requirements, activation, crosscutting memory, continual learning, distillation/source tracking, and automatic context injection.
- Read [reference directory index](../../../reference/dir-index.md) and [instructions directory index](../../../instructions/dir-index.md). Kept [Agent memory coverage](../../../../reference/agent-memory-coverage.md) as the strongest Commonplace implementation analogue; rejected most instructions because the source review is descriptive rather than procedural.

**Body searches run:**
- `rg -n "trace-derived|episode|episodes|episodic|consolidat|failure|failures|hypoth|confidence decay|causal links|MCP|pgvector|Postgres|service-owned|source.*provenance|fact_sources|typed operational" kb/agent-memory-systems --glob '*.md'`
- `rg -n "trace-derived|episode|episodes|episodic|consolidat|failure|failures|hypoth|confidence decay|causal links|MCP|pgvector|Postgres|service-owned|provenance|activation|operational memory|typed operational" kb/notes --glob '*.md'`
- `rg -n "MCP|memory|review|validation|storage|SQLite|reports|connect|provenance|activation|lifecycle" kb/reference --glob '*.md'`
- `rg -n "alash3al|stash|github.com/alash3al/stash" kb/sources kb/agent-memory-systems --glob '*.md'`
- `rg -n "hypothes|failure-pattern|failure pattern|causal link|fact_sources|provenance|confidence decay|stage.*checkpoint|service-owned" kb/notes kb/reference kb/agent-memory-systems --glob '*.md'`

**Candidate reads and link following:**
- Read [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md), [SAGE](../../../../agent-memory-systems/reviews/sage.md), [cass-memory](../../../../agent-memory-systems/reviews/cass_memory_system.md), and [ClawVault](../../../../agent-memory-systems/reviews/clawvault.md). These are the strongest neighboring reviews for Stash's storage substrate, MCP interface, fact extraction, typed links, confidence decay, and failure/procedural-memory handling.
- Read [Agent memory coverage](../../../../reference/agent-memory-coverage.md), [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md), [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md), and [Agent statelessness means the context engine should inject context automatically](../../../notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md).
- The source already links the trace-derived survey, REM, SignetAI, OpenViking, and the most relevant general memory-theory notes in its Relevant Notes footer. Those were treated as already encoded rather than re-proposed below.

## Connections Found

- [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md) -- **compares-with**: both systems are Postgres/pgvector service-owned memory backends with LLM fact extraction, fact/observation layers, entity or causal links, and consolidation. Hindsight is the production-grade, evidence-grounded, multi-retriever version; Stash is the leaner MCP-first typed-operational-object version.
- [SAGE](../../../../agent-memory-systems/reviews/sage.md) -- **compares-with**: both expose memory through MCP and support Postgres/pgvector deployments plus confidence decay. SAGE invests in signed validation, quorum, RBAC, and provenance gates; Stash invests in richer extracted memory roles and staged consolidation.
- [cass-memory](../../../../agent-memory-systems/reviews/cass_memory_system.md) -- **compares-with**: both treat failures as first-class learned material. cass-memory turns coding-agent traces into confidence-decayed playbook rules and anti-patterns; Stash stores failures as typed DB records with reason, lesson, and repeat-pattern extraction.
- [ClawVault](../../../../agent-memory-systems/reviews/clawvault.md) -- **compares-with**: both split raw trace capture from promoted structures and maintain typed observation/fact-like artifacts. ClawVault keeps inspectable vault files and bitemporal facts; Stash keeps service-owned Postgres rows and fact-source joins.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- **see-also**: this reference maps Commonplace's shipped memory surfaces against requirements. It is the best local analogue for comparing Stash's service-owned database memory with Commonplace's file-backed contracts, reports, validation, activation, and lifecycle gaps.
- [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) -- **rationale**: Stash's `fact_sources` join table preserves source episodes for consolidated facts; this note states the analogous KB-side maintenance rule that distilled outputs need source-side tracking to support staleness review.
- [Agent statelessness means the context engine should inject context automatically](../../../notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) -- **contrasts**: Stash exposes explicit recall, context, facts, relationships, and self-memory tools, but it does not solve automatic situation-triggered injection; the contrast sharpens the difference between available memory and context-engine activation.

## Bidirectional Candidates

- [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md) <-> source -- **compares-with**: Hindsight's evidence-grounded observations and Stash's `fact_sources` provenance are close enough that both reviews would benefit from reciprocal comparison if either is revised.
- [SAGE](../../../../agent-memory-systems/reviews/sage.md) <-> source -- **compares-with**: the shared MCP/database/confidence-decay surface makes the contrast between validation-gated writes and consolidation-rich writes useful in both directions.
- [cass-memory](../../../../agent-memory-systems/reviews/cass_memory_system.md) <-> source -- **compares-with**: both reviews can illuminate the design choice between procedural playbook learning and typed operational-object learning for failures.

## Reverse-edge Candidates

- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -> source -- **evidence**: Stash is a concrete example for the note's requirements around trace-derived extraction, evidence retention through provenance, multiple memory roles, activation limits, lifecycle, and weak oracles.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -> source -- **evidence**: Stash spans storage, retrieval, learning, goals, failures, hypotheses, and MCP interaction, making it a compact example of memory as a crosscutting runtime concern.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -> source -- **evidence**: Stash stores and retrieves many structured memory roles, but downstream activation still depends on the agent or host calling the right MCP tools at the right time.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -> source -- **evidence**: Stash demonstrates the solved half of continual learning well: durable knowledge accumulation in database rows. It does not by itself prove behavior change without activation or evaluation.
- [Distilled artifacts need source tracking at the source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) -> source -- **evidence**: Stash's `fact_sources` table is an external implementation of source-side tracking for distilled facts, though in a database substrate rather than markdown links.

## Off-authorisation Candidates

- The cloned repository under `related-systems/alash3al--stash` is useful evidence for the source review but is outside the KB's authored link graph. No links to that local checkout are proposed.
- Work-in-flight artifacts under `kb/work/agent-memory-design/` may be topically relevant, but collection rules exclude links into `kb/work/` from durable reviews.

## Raw Text Candidates

- "Stage-checkpointed consolidation" -- Stash has a clear mechanism for saving per-stage progress across episode-to-fact, relationship, causal, goal, failure, hypothesis, and decay passes. No local note names this pattern directly.
- "Typed operational memory objects" -- Stash's goals, failures, hypotheses, causal links, and contradictions are neither plain facts nor prose notes. A future synthesis could distinguish this object class from semantic facts, episodes, and procedural rules.
- "Hypotheses as first-class memory state" -- Stash models hypothesis status and promotion to facts; the KB has Popperian/hypothesis maintenance notes, but no agent-memory-specific note on hypothesis records as an operational memory role.

## Rejected Candidates

- [REM](../../../../agent-memory-systems/reviews/REM.md), [SignetAI](../../../../agent-memory-systems/reviews/signetai.md), [OpenViking](../../../../agent-memory-systems/reviews/openviking.md), and [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- already encoded in the Stash review's Relevant Notes; no duplicate proposal needed.
- [Atomic](../../../../agent-memory-systems/reviews/atomic.md) -- database-backed and derived-layer relevant, but its tag/wiki unit is less direct than Hindsight, SAGE, cass-memory, or ClawVault for Stash's memory-service shape.
- [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md) -- relevant to incremental derived-index maintenance, but it is data-pipeline infrastructure rather than an agent memory system with typed memory roles.
- [Storage](../../../../reference/storage-architecture.md) -- relevant to the database-versus-files contrast, but [Agent memory coverage](../../../../reference/agent-memory-coverage.md) is the stronger Commonplace-side comparison target.
- [MCP bundles stateless tools with a stateful runtime](../../../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- Stash is MCP-first, but the review does not make a protocol-complexity claim strong enough to warrant this edge.
- `kb/sources/` -- searched for Stash and `alash3al`; no source snapshot or ingest exists for this repository, so no `derived-from` edge is available.

## Index Membership

- [Agent memory systems README](../../../../agent-memory-systems/README.md) -- already contains a Stash entry.
- [Agent memory systems review index](../../../agent-memory-systems/reviews/dir-index.md) -- already contains a Stash entry.
- No new index membership is required from this connect pass.

## Synthesis Opportunities

- **Service-owned memory backends with typed roles:** Stash, Hindsight, SAGE, and REM could support a synthesis note separating storage substrate, extraction schema, validation gate, and activation mechanism for service-owned memory systems.
- **Failure memory as operational object:** Stash, cass-memory, ClawVault, and Synapptic could support a focused note on failures/anti-patterns as memory artifacts, contrasting DB failure records, playbook anti-patterns, observation ledgers, and behavioral guards.
- **Source tracking for distilled memories:** Stash's `fact_sources`, Hindsight's evidence-grounded observations, and the KB's source-side distilled-artifact rule could support a cross-substrate note on provenance patterns for extracted memories.
- **Hypothesis memory lifecycle:** Stash's hypothesis state machine plus Popperian KB maintenance notes could support a note on hypothesis records as reviewable memory, distinct from facts, tasks, or failures.

## Flags

- [Agent statelessness means the context engine should inject context automatically](../../../notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) is `status: speculative`; use it as a contrastive activation candidate, not as grounding.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) and [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) are `status: seedling`, but they are already linked by the source review and remain appropriate reverse-edge candidates.
