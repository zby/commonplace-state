---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md"
source_has_frontmatter: true
date: "2026-04-20"
depth: standard
---

# Connection Report: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

**Source:** [From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence](../../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md)

## Discovery Trace

**Index scan:**
- Read [sources index](../../sources/dir-index.md) -- flagged the target snapshot and ingest, [On the "Induction Bias" in Sequence Models](../../sources/induction-bias-sequence-models-ebrahimi-2026.md) because architecture-dependent extraction from the same data is the source-level empirical neighbor, [SuperARC](../../sources/superarc-ait-benchmark-llm-compression-abstraction.md) because it contrasts Shannon entropy and compression with algorithmic abstraction, and [Maximum Effective Context Window](../../sources/paulsen-maximum-effective-context-window-mecw.md) because it empirically bounds usable context.
- Read [notes index](../../notes/dir-index.md) -- flagged [Information value is observer-relative](../../notes/information-value-is-observer-relative.md), [Distillation](../../notes/definitions/distillation.md), [Reverse compression is when LLM output expands without adding information](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md), [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md), [Codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), and [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md).
- Read collection list for other indexes (`find kb -maxdepth 2 -name dir-index.md`) -- available indexes: instructions, work, notes, sources, tasks, agent-memory-systems, reference. No stronger candidates appeared in non-notes indexes for this source.

**Topic indexes:**
- Source tag is `academic-paper`; no curated `academic-paper` tag index was found.
- Read curated section of [learning theory index](../../notes/learning-theory-index.md) because candidate notes are tagged `learning-theory`. It confirmed an "Information & Bounded Observers" cluster containing [information-value-is-observer-relative](../../notes/information-value-is-observer-relative.md), the epiplexity ELI5 work artifact, and [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md). It also placed [distillation](../../notes/definitions/distillation.md), [discovery](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md), and [agent context soft degradation](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) as adjacent mechanisms.

**Semantic search:** grep-only fallback.
- `qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed` failed with `SQLITE_CANTOPEN: unable to open database file`; semantic search was unavailable.

**Keyword search:**
- `rg -n "epiplexity|entropy|information|computationally bounded|bounded observer|extractable|structural information|MDL|prequential|synthetic data|data ordering|AlphaZero" kb/notes kb/sources kb/reference kb/instructions --glob '*.md'` -- strongest hits were [information-value-is-observer-relative](../../notes/information-value-is-observer-relative.md), [reverse-compression](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md), [distillation](../../notes/definitions/distillation.md), [codification-and-relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), and [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md). These were kept because they use epiplexity or bounded-observer extraction as a load-bearing argument, not merely as vocabulary.
- `rg -n "complexity|bounded|observer|extraction|distillation|structure|training distribution|bitter lesson|information value|context cost|context efficiency" kb/notes/dir-index.md kb/notes/definitions/dir-index.md kb/sources/dir-index.md --glob '*.md'` -- flagged [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [agent-context-soft-degradation](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md), and [discovery](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md). Context-efficiency and soft-degradation were kept; the structured-prompt note was secondary because it uses epiplexity as an analogy rather than evidence that identifies the prompting mechanism.

**Link following:**
- Followed [information-value-is-observer-relative](../../notes/information-value-is-observer-relative.md): it directly links the epiplexity paper as a related formalization and routes to distillation, discovery, reverse-compression, minimum viable vocabulary, and structure-activated training distributions. This made it the central connection.
- Followed [distillation](../../notes/definitions/distillation.md): it links the epiplexity ingest as theoretical grounding for directed compression under bounded context. Kept as a direct connection because the paper explains why deterministic restructuring can increase usable information for a bounded consumer.
- Followed [reverse-compression](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md): it uses epiplexity as the proposed test for whether expansion adds extractable structure. Kept as a direct application.
- Followed [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md): it proposes prequential coding from epiplexity as a possible evaluation method. Kept as an application of the paper's measurement angle.
- Followed [codification-and-relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md): it cites the epiplexity framework as a way to judge whether codified regularities are genuine structure or observer-relative artifacts. Kept as an extension into codification decisions.
- Followed [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [agent-context-soft-degradation](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md): both use bounded context and complexity-sensitive usable information. Context-efficiency is kept as a direct architectural application; soft-degradation is kept as a broader foundation the paper sharpens.

## Connections Found

- [Information value is observer-relative](../../notes/information-value-is-observer-relative.md) -- **grounds**: The source gives a formal, ML-facing measure for the note's central claim that information value depends on observer capacity; epiplexity covers the pattern-extraction side of that observer relativity. The target is `seedling`, so this load-bearing grounding relationship should be reviewed carefully before becoming a durable library link.
- [Distillation](../../notes/definitions/distillation.md) -- **grounds**: The source explains why a deterministic transformation that discards classical information can still create usable structure for a bounded consumer, which is exactly the operational claim behind directed context compression.
- [Reverse compression is when LLM output expands without adding information](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md) -- **grounds**: The source supplies the paper-level measure the note invokes to distinguish verbose expansion from added extractable structure. The target is `seedling`, so the grounding role should be treated as provisional.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md) -- **enables**: The source's prequential/requential coding proposals give the note a concrete candidate method for comparing vocabularies by extractability rather than intuition.
- [Codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **extends**: Epiplexity adds a bounded-observer test for whether an extracted regularity is learnable structure worth codifying or a low-reach artifact likely to fail under scale or distribution shift.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **grounds**: The source formalizes why context cost is not just token volume; the same content can expose different usable structure depending on ordering, framing, and computational budget.
- [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) -- **extends**: The source gives the soft-bound argument an information-theoretic mechanism: degradation is partly a failure to extract structure from available tokens under bounded computation, not simply a hard-window or attention-volume problem.

## Bidirectional Candidates

- [Information value is observer-relative](../../notes/information-value-is-observer-relative.md) <-> source -- **grounds**: The note already links to the epiplexity paper as a related formalization; the source-side ingest should reciprocally identify this note as the central KB landing point.
- [Distillation](../../notes/definitions/distillation.md) <-> source -- **grounds**: The definition already cites the paper; the source ingest should preserve that reciprocal relationship because it is a key operational application of the paper.
- [Reverse compression is when LLM output expands without adding information](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md) <-> source -- **grounds**: The note explicitly uses epiplexity as the right measure for its validation question; future source readers should discover that downstream application.

## Raw Text Candidates

None

## Rejected Candidates

- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) -- rejected as a direct connection because the note uses epiplexity only as an analogy for bounded extraction and explicitly denies that it identifies the inference-time prompting mechanism; [information-value-is-observer-relative](../../notes/information-value-is-observer-relative.md) and [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) carry the broader mechanism more directly.
- [Discovery is seeing the particular as an instance of the general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) -- rejected as direct for this ingest because it is one step downstream: epiplexity helps explain recognition cost, but the current source more directly grounds the observer-relative note that already links discovery.
- [On the "Induction Bias" in Sequence Models](../../sources/induction-bias-sequence-models-ebrahimi-2026.md) -- rejected as a primary connection because it is a source-to-source empirical neighbor rather than a durable KB-theory landing point; useful context, but not necessary for this ingest report.
- [SuperARC](../../sources/superarc-ait-benchmark-llm-compression-abstraction.md) -- rejected as direct because it shares algorithmic-information vocabulary, but its extraction target is benchmark design rather than KB methodology.

## Index Membership

- [Learning theory](../../notes/learning-theory-index.md) -- The source belongs in the "Information & Bounded Observers" section as the formal source behind epiplexity, observer-relative extractability, and possible measurement methods.
- [Foundations](../../notes/foundations-index.md) -- Candidate only if the KB promotes observer-relative information value from a seedling note into foundational theory; the source itself is too paper-specific to be a foundation without that synthesis.

## Synthesis Opportunities

The source, [information-value-is-observer-relative](../../notes/information-value-is-observer-relative.md), [distillation](../../notes/definitions/distillation.md), [reverse-compression](../../notes/reverse-compression-is-when-llm-output-expands-without-adding-information.md), and [minimum-viable-vocabulary](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md) imply a higher-order claim already partly present but still underdeveloped: KB artifacts should be evaluated by how much extractable structure they create for a bounded target reader, not by token count, novelty, or classical information preservation.

## Flags

- Load-bearing `grounds` connections to `seedling` notes should remain provisional until those notes mature.
