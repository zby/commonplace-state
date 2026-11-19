---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Memory design adds operational axes to artifact analysis

**Source:** [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md)

## Discovery Trace

**Source setup and outbound rules:**
- Read [kb/cache/types/connect-report.md](../../../../types/connect-report.md), [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md), the full source note, and [kb/sources/COLLECTION.md](../../../../sources/COLLECTION.md) for reverse-edge label authorization.
- Source collection authorizes prospecting into `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `kb/work/` is excluded. `external` is authorized in principle but was not prospected because no external target was supplied in context.

**Destination: `kb/notes/`**
- Curated heads read: [README](../../../../notes/README.md), [agent-memory-README](../../../../tags/agent-memory-README.md), [context-engineering-README](../../../../tags/context-engineering-README.md), [learning-theory-README](../../../../tags/learning-theory-README.md), [artifact-analysis-README](../../../../tags/artifact-analysis-README.md).
- Skip recorded: [artifact-analysis-README](../../../../tags/artifact-analysis-README.md) declares `complete: true`, so the by-tag `rg` sweep for `artifact-analysis` was skipped.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`
  - Flagged from title scan: `knowledge-storage-does-not-imply-contextual-activation`, `create-memory-directly`, `serve-multiple-consumers`, `trace-extracted-memory-earns-authority-per-operation-not-at-capture`, `promote-only-when-value-exceeds-cost`.
- Description scans:
  - `rg '^description:' kb/notes/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|compiled|policy|retrieval|studying'`
  - `rg -l '^tags:.*\\bagent-memory\\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`
  - `rg -l '^tags:.*\\bcontext-engineering\\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`
  - `rg -l '^tags:.*\\blearning-theory\\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`
  - Kept after description scan: [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md), [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md), [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md), [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md).
- Body searches:
  - `rg -n 'capture policy|derivation policy|activation policy|authority policy|lifecycle policy|evaluation policy|signal-timing|compiled views|trace extraction|read-back|retire|redact|supersede|memory management policy|corpus-only|pre-task|post-session|curator' kb/notes/ --glob '*.md'`
  - `rg -n 'capture|activation|authority|lifecycle|evaluation|consumer|cue|read-back|retrieval|signal-timing|trace extraction' kb/notes/ --glob '*.md'`
  - Kept:
    - [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) because it gives the missing mechanism for the source note's claim that activation remains open even when artifact identity and capture choices are fixed.
    - [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md) because it gives the complementary live-understanding capture path to the source note's post hoc extraction examples.
    - [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) because the source's operational axes imply differentiated read surfaces, and this note states that downstream requirement directly.
  - Rejected:
    - [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) because the source already links it in `## Detailed notes`; stronger as a target-side return link than as another outbound recommendation.
    - [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) because promotion economics is adjacent but less load-bearing for this framing note than the capture/activation/consumer-surface candidates.
    - [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) because the source already routes readers to [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md); this note sharpens the same area but does not beat the existing route.
- Link following:
  - Followed [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md); kept because it decomposes the source note's activation row into storage-to-context and context-to-action failure.
  - Followed [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md) and contrasted it with the already-linked [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md); kept only the direct-creation note as new outbound signal.
  - Followed [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md); kept because it names the multi-surface consequence only implied in the source.

**Destination: `kb/reference/`**
- Curated head read: [README](../../../../reference/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`
- Description scan: `rg '^description:' kb/reference/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|compiled|policy|retrieval|signal'`
- Body search: `rg -n 'memory|artifact analysis|activation|authority|lifecycle|evaluation|capture|derivation|trace-learning|read-back|compiled views|lineage|retire|supersede|review' kb/reference/ --glob '*.md'`
- Kept: [Agent memory coverage](../../../../reference/agent-memory-coverage.md) because it is a shipped-system worked case mapping Commonplace onto direct creation, activation, promotion, lifecycle, authority, and evaluation.
- Rejected: [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) because it is a derivative implementation roadmap; the coverage note is the stronger first stop.

**Destination: `kb/agent-memory-systems/`**
- Curated head read: [README](../../../../agent-memory-systems/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`
- Description scan: `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal'`
- Body search: `rg -n 'capture|derivation|activation|authority|lifecycle|evaluation|trace-learning|read-back|curation|retire|supersede|corpus|pre-task|signal' kb/agent-memory-systems/ --glob '*.md'`
- Kept: [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) because it compares real systems on ingestion pattern, representational form, behavioral authority, and reinjection path, giving cross-system evidence for the source's operational split.
- Rejected: [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) because it is about survey instrumentation rather than the memory-design axes themselves.

**Destination: `kb/sources/`**
- Curated head read: [README](../../../../sources/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`
- Description scan: `rg '^description:' kb/sources/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal|study|studying'`
- Body search: `rg -n 'memory|capture|derivation|activation|authority|lifecycle|evaluation|trace|retrieval|curation|forget|study|studying|signal' kb/sources/ --glob '*.md'`
- Kept:
  - [Ingest: From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md) because its `construction/management/retrieval/usage` staging independently converges on operational distinctions beyond storage alone.
  - [Ingest: How we built our knowledge base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md) because it is a practitioner case where ingress shaping, activation, and multiple consumer surfaces all matter together.
- Rejected:
  - [Machine Studying](../../../../sources/machine-studying.ingest.md) because the source already cites it directly for the corpus-only signal-timing pole.
  - [Everything you need to know about LLM memory](../../../sources/everything-you-need-to-know-about-llm-memory.md) because the source already cites it directly for the practitioner design-map role.

**Destination: `kb/instructions/`**
- Curated head read: [README](../../../../instructions/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`
- Description scan: `rg '^description:' kb/instructions/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal'`
- Body search: `rg -n 'memory|capture|derivation|activation|authority|lifecycle|evaluation|trace|retrieval|policy|signal' kb/instructions/ --glob '*.md'`
- Result: no plausible `operationalized-from` candidate. The source note is a framing note, and the instruction pass surfaced procedures about writing, review, ingest, and maintenance rather than a procedure that clearly adds ordering/defaults/stopping conditions for this six-axis frame.

**Destination: `kb/types/`**
- Curated head read: [README](../../../../types/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`
- Description scan: `rg '^description:' kb/types/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal'`
- Body search: `rg -n 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal' kb/types/ --glob '*.md'`
- Result: no candidate kept. The type specs discuss global artifact contracts and review surfaces, but none improved traversal from this note better than the local definition and requirement links the source already carries.

**Destination: `kb/agentic-systems/`**
- Curated head read: [README](../../../../agentic-systems/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`
- Description scan: `rg '^description:' kb/agentic-systems/ --glob '*.md' | rg 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal'`
- Body search: `rg -n 'memory|artifact|context|learning|activation|authority|lifecycle|evaluation|capture|derivation|trace|policy|retrieval|signal' kb/agentic-systems/ --glob '*.md'`
- Result: no candidate kept. The whole-system analyses surfaced memory-adjacent material, but none improved traversal from this note better than the focused memory-system review and source-ingest candidates already kept.

**Path verification:**
- Verified every path named in `Connections Found`, `Bidirectional Candidates`, `Reverse-edge Candidates`, and `Rejected Candidates` with an explicit `test -f ...` pass before writing the report.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **mechanism**: the source says activation remains open even when retained artifacts and capture choices are fixed; this note explains the missing storage-to-context and context-to-action mechanism.
- [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md) -- **extends**: the source's capture and derivation axis includes post hoc extraction paths, and this note adds the complementary write-while-understanding-is-live path.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) -- **extends**: the source's operational axes imply different activation and governance surfaces for different consumers, and this note states that consequence directly.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- **evidenced-by**: Commonplace's shipped-memory map is a worked case showing capture, activation, lifecycle, authority, and evaluation as separable design choices inside one system.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **evidenced-by**: the survey gives cross-system evidence that ingestion pattern, promoted form, and reinjection path vary independently in exactly the way the source's operational axes predict.
- [Ingest: From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md) -- **evidenced-by**: the survey's `construction/management/retrieval/usage` staging independently converges on operational distinctions beyond storage form.
- [Ingest: How we built our knowledge base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md) -- **evidenced-by**: the Cerebras case is a practitioner instance where ingress shaping, retrieval/activation policy, and multi-consumer surfaces all matter at once.

## Bidirectional Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source -- **extends**: the activation note would benefit from a return link to the broader six-axis frame it instantiates on the read-side.
- [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md) <-> source -- **extends**: the requirement note names one concrete capture/derivation pole and would gain a router link back to the broader operational-axis map.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) <-> source -- **extends**: the requirement note gives the consumer-surface consequence of the source's operational split and would benefit from linking back to that framing note.

## Reverse-edge Candidates

- [Ingest: How we built our knowledge base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md) → source -- **is-evidence-for**: under `kb/sources/COLLECTION.md` rules, this ingest already argues that ingress, retrieval, activation, and multiple consumer surfaces matter together; linking to the source note would make that evidence placement explicit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) -- strong fit, but already linked from the source's `## Detailed notes`; better as a target-side return link than as another outbound recommendation.
- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- adjacent promotion-economics note, but weaker traversal gain than the direct capture, activation, and multi-consumer candidates.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- sharpens authority policy, but the source already routes to a stronger existing authority note.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- derivative implementation roadmap; [Agent memory coverage](../../../../reference/agent-memory-coverage.md) is the tighter first stop for a reader following the source note.
- [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) -- concerns review instrumentation rather than the operational memory axes themselves.

## Index Membership

None

## Synthesis Opportunities

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Create Memory Directly](../../../../notes/agent-memory-requirements/create-memory-directly.md), and [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) together suggest a still-unwritten claim: memory-system design needs one timing axis for when evidence is captured and another for when retained material is reactivated into action.

## Maintenance Observations

None

## Flags

- None
