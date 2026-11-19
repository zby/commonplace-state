---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/building-a-good-vertical-agent-2065190286519906657.md"
source_has_frontmatter: true
date: "2026-06-12"
depth: standard
---

# Connection Report: Building a Good Vertical Agent

**Source:** [Building a Good Vertical Agent](../../../sources/building-a-good-vertical-agent-2065190286519906657.md)

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/sources --glob '*.md'` -- flagged [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md), [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), [in-context-learning-presupposes-context-engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md), [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md), and [frontloading-spares-execution-context](../../../../notes/frontloading-spares-execution-context.md) because their descriptions name context scarcity, loading hierarchy, context activation, and context scheduling.
- The same scan flagged sibling source/review candidates: [components-of-a-coding-agent-raschka.ingest](../../../../sources/components-of-a-coding-agent-raschka.ingest.md), [lessons-from-building-ai-agents-for-financial-services.ingest](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md), [context-engineering-ai-agents-oss.ingest](../../../../sources/context-engineering-ai-agents-oss.ingest.md), [multi-agent-memory-computer-architecture-perspective.ingest](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md), [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md), and [Fintool](../../../../agent-memory-systems/lightweight/fintool.md).

**Topic indexes:**
- Read [kb/notes/README.md](../../../../notes/README.md) -- confirmed the notes collection foregrounds deploy-time learning, constraining, and context-engineering mechanisms.
- Read [kb/reference/README.md](../../../../reference/README.md) -- no direct shipped-system target needed beyond navigation/control-plane context; the source is theory/practice evidence rather than reference documentation.
- Read [kb/agent-memory-systems/README.md](../../../../agent-memory-systems/README.md) -- confirmed the relevant external-system frame is progressive disclosure and read-back, but this source is a practitioner report rather than a reviewable system.

**Body search:**
- `rg -n "context compression|context quality|context hierarchy|memory hierarchy|cache hierarchy|L1|L2|L3|deferred tool|deferred tools|tool schema|single tool|execute_code|raw API|curated spec|skills" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob '*.md'` -- found strong hits in context-efficiency, instruction-specificity, always-loaded-context, bounded-context orchestration, symbolic context engineering, Agent Skills, Fintool, and existing source ingests. Kept candidates where the source contributes a new mechanism or evidence; rejected hits that only shared the word "skills" or "tools."

**Link following:**
- From [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), followed links to [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md), and Raschka's ingest. This showed the source adds a new cache-placement optimization frame rather than merely repeating "context matters."
- From [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md), followed [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md). This kept the L1/L2/L3 hierarchy as a stronger connection than a generic AGENTS.md/router match.
- From [lessons-from-building-ai-agents-for-financial-services.ingest](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md), followed [Fintool](../../../../agent-memory-systems/lightweight/fintool.md) and [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md). Fintool is a sibling vertical-agent product report; Agent Skills is an architectural comparison for skill routing and progressive disclosure.

## Connections Found

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: the source provides a production practitioner argument that agent accuracy is a function of context quality and that context should be allocated according to task-distribution frequency, with L1/L2/L3 placement as the operational method.
- [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- **evidence**: the source independently states the same frequency-placement rule in a product setting: common operations belong in always-resident prompt/API wrappers, occasional capabilities in one-step curated specs, and rare capabilities behind a search skill over raw references.
- [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **evidence**: the source's "bloated context buries the signal" claim and tool-count warning are practitioner observations of degradation from volume, schema overlap, and interference before hard context limits bind.
- [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **extends**: the source adds a concrete vertical-agent allocation pattern across always-loaded prompt/API descriptions, on-demand capability specs, deferred tool schemas, and raw API search skills.
- [frontloading-spares-execution-context](../../../../notes/frontloading-spares-execution-context.md) -- **exemplifies**: the source's L1 read/write wrappers precompute compression, semantic enrichment, style grouping, and consequence triage so every common spreadsheet task avoids rediscovering or re-reading raw state.
- [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md) -- **evidence**: the source offers a product-scale example of symbolic code/tool execution plus bounded model calls, where the system minimizes context spent per task and pushes long-tail lookup into explicit search over external state.
- [definitions/distillation](../../../notes/definitions/distillation.md) -- **defined-in**: the source's "context compression" is a domain-specific instance of directed context compression; the definition helps a reader distinguish compression-for-use from generic summarization.

## Bidirectional Candidates

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) <-> source -- **evidence**: the note already uses external practitioner reports as evidence; this source is strong enough to join the existing evidence list because it contributes a sharper optimization target, "minimize context spent per task averaged over the task distribution."
- [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) <-> source -- **evidence**: the source is a near-direct independent restatement of the note's core claim, but in agent-product terms rather than Commonplace loading-surface terms.

## Reverse-edge Candidates

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -> source -- **evidence**: should cite this source as practitioner evidence for context quality and task-distribution-aware context allocation.
- [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -> source -- **evidence**: should cite this source as evidence that loading frequency can be operationalized as a cache hierarchy, not only as a CLAUDE.md/skill-body convention.
- [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -> source -- **evidence**: should cite this source where it discusses capability descriptions and on-demand skill/tool loading.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [symbolic-context-engineering-is-bounded-by-symbol-availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) -- rejected as a primary connection: the source uses symbolic handles for L2/L3 loading, but it does not foreground the "symbol must already be available" constraint.
- [in-context-learning-presupposes-context-engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) -- rejected as too broad: the source supports context engineering generally, but the stronger local connections are context-efficiency and loading-frequency placement.
- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected as adjacent: L2/L3 lookup helps storage-to-context read-back, but the source does not address context-to-action activation.
- [multi-agent-memory-computer-architecture-perspective.ingest](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) -- rejected as a direct connection: both use computer architecture analogies, but the source is single-agent context placement while the paper is multi-agent memory consistency.
- [Fintool](../../../../agent-memory-systems/lightweight/fintool.md) -- rejected as a primary target: it is a sibling vertical-agent product report, useful for comparison in the ingest report but not a stronger target than the underlying Fintool source ingest.

## Index Membership

- [learning-theory-README](../../../../tags/learning-theory-README.md) -- future index membership could place this source near context engineering, deploy-time learning, and distillation if a note is promoted from it.
- [agent-memory-systems README](../../../../agent-memory-systems/README.md) -- no direct index edit recommended; the source may become lightweight coverage only if Shortcut itself is later reviewed as an external system.

## Synthesis Opportunities

- A note titled `Agent context should be organized as a cache hierarchy` could synthesize [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [instruction-specificity-should-match-loading-frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md), [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), and this source. The new claim would be that context placement should optimize expected cost across a task distribution, using resident wrappers, one-step specs, and bounded raw-reference search as tiers.

## Maintenance Observations

None

## Flags

- The source is a practitioner report with a strong authorial thesis and many concrete spreadsheet examples; it should be ingested as evidence and synthesis material, not decomposed into atomic claims during ingestion.
