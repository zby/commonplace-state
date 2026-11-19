---
description: "Connection discovery for Rosebud Journal's LLM memory design-space essay"
type: kb/cache/types/connect-report.md
source: "kb/sources/everything-you-need-to-know-about-llm-memory.md"
source_has_frontmatter: true
date: "2026-04-13"
depth: standard
---

# Connection Report: Everything you need to know about LLM memory

**Source:** [Everything you need to know about LLM memory](../../../sources/everything-you-need-to-know-about-llm-memory.md)

## Discovery Trace

**Index scan:**
- Read [notes index](../../../notes/dir-index.md) -- flagged candidates:
  - [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) because the source decomposes LLM memory into storage, retrieval/activation, derivation, forgetting, and curation decisions rather than treating memory as a single subsystem.
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) because the source argues infinite context is not enough: cost, attention degradation, retrieval, and compression remain binding constraints.
  - [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) because the source repeats the soft-degradation claim in the specific frame of conversational memory.
  - [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) because the source distinguishes stored history from memory that is surfaced at the right turn.
  - [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md) because the source's raw-vs-derived axis is the same store-more-than-you-load separation applied to long conversational memory.
  - [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) because the source's write triggers, curator roles, forgetting policy, and post-retrieval processing map to memory-management policy choices.
  - [files-not-database](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) because the source explicitly compares filesystem, SQL, NoSQL, vector, and graph backends.
  - [automated-linking-improves-retrieval-but-may-degrade-navigability](../../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md) because the source's evaluation-paradox section says retrieval benchmarks do not capture the full memory problem.
- Read [agent memory systems index](../../../agent-memory-systems/dir-index.md) -- flagged candidates:
  - [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) because it already classifies memory systems across storage unit, agency model, link structure, temporal model, curation operations, and extraction schema; the Rosebud source independently proposes a broader practitioner map with overlapping and new axes.

**Topic indexes:**
- No source tags were present in the snapshot frontmatter, so no tag-specific index was read. The source is best routed by content terms rather than existing tags.

**Semantic search:** via qmd
- query "LLM memory raw derived summaries forgetting retrieval context" -- top hits:
  - [distillation](../../../notes/definitions/distillation.md) (92%) -- relevant background for raw-to-derived compression, but the source does not add a new definition-level distinction beyond existing distillation vocabulary.
  - [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) (56%) -- accepted: the source turns policy choices into a practitioner design map.
  - [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (44%) -- accepted: the source is a direct concrete instance of the decomposition.
  - [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) (43%) -- accepted: the source's "memory is not just recall" claim depends on activation, not storage.
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (39%) -- accepted: the source's infinite-context objection is a concrete context-efficiency argument.
- query "agent memory storage retrieval activation learning context engineering" -- top hits:
  - [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (93%) -- accepted as the strongest theory connection.
  - [three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative](../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) (47%) -- rejected as too broad; the source has memory-axis taxonomy, not the self/knowledge/operational lifecycle split.
  - [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) (47%) -- accepted as a background rationale, but weaker than the crosscutting-memory note for the report.
  - [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) (45%) -- rejected as too narrow; the source includes always-injected memory but is not mainly about harness startup surfaces.
  - [files-not-database](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) (45%) -- accepted as a backend trade-off connection.
- query "memory systems filesystem graph vector database curator what to remember" -- top hits:
  - [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (93%) -- accepted.
  - [mem0-memory-layer](../../../sources/mem0-memory-layer.md) (56%) -- rejected as sibling raw source; its ingest and comparative review already absorb the relevant architecture.
  - [databricks-memory-scaling-ai-agents](../../../sources/databricks-memory-scaling-ai-agents.md) (36%) -- accepted as a sibling source only for comparison, not a durable note connection.
  - [letta-memgpt-stateful-agents-ingest](../../../../sources/letta-memgpt-stateful-agents.ingest.md) (35%) -- rejected as one example already covered by the comparative review.
- query "evaluation paradox ground truth full conversation history memory benchmark retrieval not memory" -- top hits:
  - [prompt-ablation-converts-human-insight-to-deployable-framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) (88%) -- rejected: both discuss ground truth, but the prompt-ablation note needs a known miss; the source argues long-horizon conversational memory lacks a tractable ground truth.
  - [the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../../../notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) (50%) -- rejected as background; [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md) carries the more direct mechanism.
  - [quality-signals-for-kb-evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) (32%) -- accepted as a weak connection: both separate retrieval accuracy from deeper system-quality/navigability evaluation.
- query "forgetting policy memory delete derived artifacts provenance cascade deletes" -- top hits:
  - [notes-need-quality-scores-to-scale-curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) (50%) -- rejected: decay policy appears there, but the source's forgetting section is about provenance and derived-artifact propagation.
  - [novel-memory-forgetting-techniques-autonomous-ai-agents-ingest](../../../../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) (39%) -- accepted as sibling evidence for forgetting-as-policy but not a primary theory note.
  - [distilled-artifacts-need-source-tracking-at-the-source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) (36%) -- accepted as a useful propagation/provenance connection: both say derived artifacts need source tracking because source changes or deletion do not automatically propagate.

**Keyword search:**
- rg "memory|forget|retrieval|raw|derived|context window|graph DB|vector DB|curator|write trigger" across `kb/notes` and `kb/agent-memory-systems` -- many hits; high-signal hits were the crosscutting-memory note, comparative review, REM/Zikkaron reviews, files-not-database, and knowledge-storage activation note. Sibling system reviews were mostly rejected because the source itself already surveys examples at the category level.
- rg "LongMem|ground truth|benchmark|activation gap|memory.*benchmark|retrieval isn't memory" across `kb/` -- flagged REM's benchmark limitation, the A-MEM automation-quality report, Databricks memory-scaling ingest, and soft-degradation benchmark ingests. Accepted the A-MEM automation-quality report as the closest existing note on retrieval benchmarks measuring a narrower target than navigability/memory.

**Link following:**
- From [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), followed links to [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md), [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md), and [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md). This confirmed the main cluster.
- From [files-not-database](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md), followed the Graphiti boundary discussion. This confirmed that the source's backend taxonomy should connect as a backend-tradeoff example, but not override the existing files-first argument.
- From [a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality](../../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md), followed the retrieval-vs-navigability distinction. This confirmed that the source's "retrieval isn't memory" claim fits an existing evaluation gap rather than needing a wholly new benchmark note.

## Connections Found

- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **evidence**: the source independently decomposes conversational LLM memory into storage substrate, derivation, write triggers, retrieval timing, curator identity, post-retrieval processing, and forgetting, supporting the note's claim that "memory" is a bundle of storage, context engineering, and learning problems.
- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- **extends**: the source provides a practitioner design map that overlaps the review's dimensions while adding explicit axes for derivation timing, retrieval timing, post-retrieval processing, and forgetting propagation.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: the source argues that infinite or very large context does not remove memory-system design because cost, attention degradation, and raw-history inertness still force selective loading and compression.
- [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **evidence**: the source's "degradation" objection to infinite context is the conversational-memory instance of the soft-bound thesis.
- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **evidence**: the source distinguishes storing full transcripts from the system actually remembering what matters on a later turn; that is the activation gap in conversational form.
- [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- **evidence**: the source's raw/derived trade-off and "raw is lossless but inert" framing reinforces the store-more-than-you-load principle.
- [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **extends**: the source broadens memory policy from AgeMem's operation-selection problem into a full practitioner taxonomy: what to store, when to derive, what triggers writes, who curates, when retrieval happens, and how forgetting propagates.
- [files-not-database](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -- **evidence**: the source's storage-backend section is a compact external map of filesystem, SQL, NoSQL, vector, and graph trade-offs, aligning with the note's claim that backend choice follows access patterns and desired retrieval/navigation capabilities.
- [distilled-artifacts-need-source-tracking-at-the-source](../../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) -- **evidence**: the source's forgetting-propagation section makes the same provenance claim for deletion: raw-source changes or deletion do not automatically update derived summaries, graph facts, or other artifacts.
- [automated-linking-improves-retrieval-but-may-degrade-navigability](../../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md) -- **extends**: the source's evaluation paradox says long-horizon memory is not captured by needle-in-haystack retrieval benchmarks; the automation-quality report makes the adjacent distinction that QA retrieval scores do not measure navigability.

## Bidirectional Candidates

- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) <-> source -- **evidence**: the note could cite this source as a compact practitioner articulation of the same decomposition, especially because the source enumerates concrete axes agents and builders can inspect.
- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) <-> source -- **extends**: the review's six dimensions could be cross-checked against the source's map to decide whether derivation timing, retrieval timing, post-retrieval processing, and forgetting propagation should become explicit dimensions in future reviews.
- [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) <-> source -- **extends**: the source's write-trigger and curator taxonomy gives policy vocabulary beyond AgeMem's six operations.

## Raw Text Candidates

None.

## Rejected Candidates

- [distillation](../../../notes/definitions/distillation.md) -- relevant background, but the source does not change the definition; it supplies examples of raw-to-derived compression.
- [three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative](../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) -- both are memory taxonomies, but the source maps architectural axes rather than lifecycle-separated memory spaces.
- [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- the source includes always-injected retrieval as one mode, but does not focus on harness startup or always-loaded surfaces.
- [prompt-ablation-converts-human-insight-to-deployable-framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- the shared "ground truth" vocabulary is misleading; prompt ablation starts from known misses, while the source argues that long-horizon conversational memory lacks scalable ground truth.
- [notes-need-quality-scores-to-scale-curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) -- decay is adjacent, but the source's forgetting value is mostly about derived-artifact provenance, not quality-score prioritization.
- [mem0-memory-layer](../../../sources/mem0-memory-layer.md), [letta-memgpt-stateful-agents](../../../sources/letta-memgpt-stateful-agents.md), [databricks-memory-scaling-ai-agents](../../../sources/databricks-memory-scaling-ai-agents.md) -- sibling memory sources with overlapping examples; useful context, but the comparative review is the cleaner connection.

## Index Membership

- [Learning theory index](../../../notes/learning-theory-index.md) -- the source contributes to memory policy, distillation, accumulation, and forgetting/lifecycle management, but it is a source snapshot rather than a note; any promoted note should join this index if it argues a transferable mechanism.
- [Evaluation index](../../../notes/evaluation-index.md) -- the evaluation-paradox argument could support an eventual note on long-horizon memory evaluation, but the source alone is not enough to create a new index entry.
- [Agent memory systems directory](../../../agent-memory-systems/dir-index.md) -- not directly; the source is not a review of one system. It is more useful as a source for a future comparative/theory note.

## Synthesis Opportunities

Potential note: "LLM memory design is a policy stack, not a storage problem." It would synthesize this source with [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [memory-management-policy-is-learnable-but-oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md). The thesis: after storage is chosen, every meaningful memory capability is a policy decision over lossy transformations: when to write, what to derive, how to retrieve, what to inject, how to reconcile supersession, and how to propagate forgetting through derived artifacts.

Potential note: "Memory evaluation has a ground-truth horizon." It would connect this source's evaluation paradox with [automated-linking-improves-retrieval-but-may-degrade-navigability](../../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md), [quality-signals-for-kb-evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md). The thesis: memory benchmarks become less valid as the target shifts from direct recall to changing arcs, supersession, and significance recognition, because the ground truth moves outside any cheap judge's context.

## Flags

- Load-bearing links to [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md) point to seedling notes; treat them as useful but not fully settled theory.
