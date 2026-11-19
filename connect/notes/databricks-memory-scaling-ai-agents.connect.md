---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/databricks-memory-scaling-ai-agents.md"
source_has_frontmatter: true
date: "2026-04-11"
depth: standard
---

# Connection Report: Memory Scaling for AI Agents

**Source:** [Memory Scaling for AI Agents](../../sources/databricks-memory-scaling-ai-agents.md)

## Discovery Trace

**Index scan:**
- Read [notes index](../../notes/index.md) -- flagged candidates:
  - [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- direct match: the source decomposes memory scaling into storage, retrieval/activation, distillation/learning, and action improvement.
  - [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- direct match: the source contrasts long context with selective retrieval and reports fewer reasoning steps as memory grows.
  - [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- direct match: the source names the failure mode where useful memory exists but the agent does not query it.
  - [Distillation](../../notes/definitions/distillation.md) -- direct match: the source's episodic-to-semantic memory pipeline is an automated distillation case.
  - [In-context learning presupposes context engineering](../../notes/in-context-learning-presupposes-context-engineering.md) -- direct match: the source argues external memory makes frozen-weight in-context use effective only when selection/retrieval works.
  - [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- candidate: the source reports gains from filtered logs and memory use, but does not show a learned policy like AgeMem.
  - [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md) -- candidate: the source is a new data point in the agent-memory design space, especially around organizational memory and governance.
  - [xMemory](../../notes/related-systems/xMemory.md) -- candidate: both use multi-resolution memory from traces, but xMemory is benchmark dialogue retrieval while the source is enterprise agent memory.

**Topic indexes:**
- Read [Learning theory](../../notes/learning-theory-index.md) -- reinforced candidates around deploy-time learning, distillation, reach, memory architecture, and oracle-dependent memory policy.

**Semantic search:** via qmd
- query "external memory scaling agents episodic semantic memory retrieval distillation governance" -- top hits:
  - [xMemory](../../notes/related-systems/xMemory.md) (93%) -- kept as comparative neighbor: both use trace-derived memory layers, but with different evaluation targets and governance.
  - [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md) (55%) -- kept: the source adds empirical enterprise-memory evidence to this design-space split.
  - [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) (46%) -- rejected as weaker: the source uses episodic/semantic/personal/organizational distinctions, but the note's lifecycle separation is not the source's central contribution.
  - [Distillation](../../notes/definitions/distillation.md) (45%) -- kept: episodic-to-semantic memory is a concrete distillation pipeline.
  - [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (43%) -- kept: the source strongly instantiates the crosscutting decomposition.
- query "agent memory storage retrieval activation learning context engineering" -- top hits:
  - [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md) (93%) -- kept.
  - [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (56%) -- kept.
  - [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) via [Learning theory](../../notes/learning-theory-index.md) (47%) -- kept as a contrast around policy learning and oracle availability.
  - [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (46%) -- kept.
  - [xMemory](../../notes/related-systems/xMemory.md) (46%) -- kept as comparative neighbor.
- query "MemAlign memory scaling enterprise knowledge store agent performance" against sources -- qmd reranker failed with "Failed to create any rerank context"; used grep-only fallback for source-neighbor checking.

**Keyword search:**
- rg "memory scaling|MemAlign|episodic|semantic memor|continual learning|long context|organizational knowledge|memory store|memory management|governance|retrieval" -- found the new snapshot plus relevant prior ingests on A-MEM, multi-agent memory, psychology memory, and notes on retrieval/activation; no prior MemAlign ingest was found.
- rg "memory decomposes|activation gap|right knowledge|distillation|context budget|memory management|retrieval/activation|who decides what to remember|memory is not a separable|continuous learning" -- confirmed the main candidate cluster in learning theory and related-system notes.
- rg "long context|context window|selective retrieval|right knowledge|bounded context|soft degradation" -- confirmed the long-context/selective-retrieval connection to context-efficiency, soft-degradation, context-engineering, and in-context-learning notes.

**Link following:**
- From [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), followed links to [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Context engineering](../../notes/definitions/context-engineering.md), [Distillation](../../notes/definitions/distillation.md), [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md).
- From [xMemory](../../notes/related-systems/xMemory.md), checked the four-resolution retrieval ladder and trace-derived learning placement; this source is similar enough to compare but not a direct duplicate because Databricks focuses on enterprise agent memory scaling, governance, and Genie/knowledge-store experiments.
- From [Learning theory](../../notes/learning-theory-index.md), checked reach and memory-architecture sections to assess whether the source contributes high-reach mechanism or mostly benchmark-specific evidence.

## Connections Found

- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **exemplifies**: the source's "memory scaling" proposal only becomes coherent when decomposed across storage, retrieval/activation, distillation/learning, governance, and action efficiency; it is not a standalone memory layer story.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **extends**: the source adds practitioner/experimental evidence that better memory retrieval can reduce reasoning steps, not just improve answer quality, which fits context efficiency as the binding agent-system constraint.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **extends**: the source names the same activation gap from the memory-system side: correct memories can remain useless unless the agent predicts that querying memory will help and asks the right query.
- [Distillation](../../notes/definitions/distillation.md) -- **exemplifies**: MemAlign's episodic-to-semantic memory pipeline and the organizational knowledge-store pipeline are direct cases of compressing raw traces/assets into context-usable artifacts.
- [In-context learning presupposes context engineering](../../notes/in-context-learning-presupposes-context-engineering.md) -- **extends**: the source gives a positive version of the argument; frozen-weight agents improve when context-selection machinery supplies the right deployment-specific memory at inference time.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **contrasts**: AgeMem learns an opaque memory policy against task-completion rewards, while Databricks uses external memory pipelines and LLM-judged log filtering; both show memory policy matters, but the oracle and substrate choices differ.
- [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md) -- **extends**: the source adds an enterprise deployment axis absent from the comparative review: memory scope and governance become first-class design determinants when memories span users and organizational assets.
- [xMemory](../../notes/related-systems/xMemory.md) -- **compares**: both systems build multi-resolution memory from traces, but xMemory optimizes dialogue-memory QA while Databricks emphasizes business-schema grounding, expert-instruction replacement, governance, and production storage.

## Bidirectional Candidates

- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) <-> source -- **exemplifies**: the Databricks source is a compact public example of why memory must be evaluated as storage + retrieval/activation + learning + governance, not as one plug-in subsystem.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) <-> source -- **extends**: the reported reasoning-step reductions are a useful concrete data point for context efficiency producing speed/cost gains.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source -- **extends**: the source's "agent has to discover memory exists before querying it" framing is a production-memory version of the activation gap.
- [The fundamental split in agent memory is not storage format but who decides what to remember](../../notes/related-systems/agentic-memory-systems-comparative-review.md) <-> source -- **extends**: enterprise governance and organizational scope should be represented in future memory-system comparison work.

## Raw Text Candidates

None

## Rejected Candidates

- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) -- rejected as a primary connection: the source does use episodic/semantic and personal/organizational categories, but the note's main claim is about lifecycle separation and the risk of decorative cognitive analogy.
- [Cludebot](../../notes/related-systems/cludebot.md) -- rejected: qmd surfaced memory-type decay similarities, but the source does not discuss decay or dream-cycle-style consolidation.
- [MentisDB](../../notes/related-systems/mentisdb.md) -- rejected: both involve memory storage and governance, but the source's storage argument is generic enterprise infrastructure rather than append-only ledger or signed skill registry design.
- [CrewAI Memory](../../notes/related-systems/crewai-memory.md) -- rejected: both address agent memory at scale, but the source's novelty is empirical memory-scaling behavior and enterprise governance, not crew-scoped memory consolidation.
- [A knowledge base should support fluid resolution-switching](../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) -- rejected as a direct connection: the source's memory layers imply resolution switching, but it does not make that the central evaluative criterion.

## Index Membership

- [Learning theory](../../notes/learning-theory-index.md) -- the source belongs as a reference under Memory & Architecture and Deploy-time Learning because it supplies fresh enterprise evidence for external-memory scaling, trace distillation, and system-layer adaptation without weight updates.
- [Related Systems](../../notes/related-systems/related-systems-index.md) -- the source is not a repo review, but it is a relevant source for future memory-system comparison notes because it adds enterprise governance and organizational-memory scope.

## Synthesis Opportunities

- Potential note: "Memory scaling is context-engineering scaling, not just storage scaling" -- would synthesize [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and the Databricks source. It would argue that memory scaling only happens when retrieval/activation policy and distillation quality scale with the store; raw accumulation alone predicts degradation.
- Potential note/update: enterprise governance may be a missing axis in the [agentic memory systems comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md), because personal vs organizational memory introduces access-control and distillation-leakage constraints that the current six dimensions only partially capture.

## Flags

- The snapshot is a structured paraphrase rather than a verbatim article capture for copyright compliance; use the source URL when exact wording matters.
- Several strongest candidate notes are `seedling`; use additive links or cite as prompts for revision rather than as load-bearing foundations.
