---
description: "Connection discovery for Qwenputer: compiled execution, recurrent-state retention, and model-integrated memory comparisons."
type: types/connect-report.md
source: kb/sources/qwenputer.ingest.md
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Qwenputer

**Source:** [Ingest: Qwenputer — a deterministic RISC-V CPU inside Qwen3.5](../../../../sources/qwenputer.ingest.md)

Purpose: post-acceptance ingest connection discovery. All entries below are candidates for future authoring. No library artifact or index was changed. Discovery used the accepted ingest's analysis, not an independent inspection of Qwenputer's implementation or benchmarks.

## Discovery Trace

### Contracts and search method

Read the source and reports collection contracts, the connect-report type and schema, and the ingest-report type. The source contract authorizes prospecting theory, reference, agent-memory-systems, agentic-systems, tags, and other sources. It excludes work and instructions. Its labels were filtered by destination; in particular, tags has no authorized formal label. External targets may be evaluated only when already known.

Read every destination's root `README.md`. Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the six destinations. Recovered truncated tool output before evaluation. Sources titles were also scanned as a complete sorted title-only surface with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' | sort | cut -d: -f2-`.

For every destination, ran this scoped description listing:

`rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'recurrent|parametric|symbolic|substrate|selective revision|exact storage|activation|compiled|persistent.*state|weight.*prompt|memory.*operation|knowledge.*reasoning'`

For every destination, ran both body passes:

- `rg -n -i 'qwenputer|deltanet|recurrent.state|compiled (cpu|circuit)|context.conditioned' kb/<destination>/ --glob '*.md'`
- `rg -l -i 'selective revision|storage.*(activation|faithful)|parametric.*(record|reproduction)|named.file|save/load|save.*reload' kb/<destination>/ --glob '*.md'`

These are lexical searches; no semantic-search scores were available. The source has `domains`, not `tags`, so there was no source-tag membership query. No external search or delegation was used.

### Theory

The landing and title/description scans identified the two already-linked primary notes, representational-form and storage-substrate definitions, the authoritative-record note, and the storage/activation distinction. The exact-mechanism query found the explicit-retention note's context-conditioned-state row, but no pre-existing Qwenputer account. Fully read these candidates and the theory collection contract before judging return edges.

Followed the symbolic-operation note's links to representational form and exact implementation; followed explicit retention to reflective coverage; followed representational form to operative part and storage substrate. These neighborhoods separate assigned execution, editing handles, and storage location. Kept the two primary source-to-theory associations and their independently useful returns. Kept representational form as an inbound-only boundary example. Rejected a separate authoritative-record edge because Qwenputer does not demonstrate record-governance substitution. Storage/activation and exact-implementation notes supply useful interpretive checks, but their mechanisms are already recoverable through the two primary notes; no additional outbound spray is proposed.

`rg -n 'symbolic|operations|revision' kb/theory/code-complements-weight-prompt-with-symbolic-operations.brief.md` also checked the associated brief's discovery signal. The candidate remains the document, never its brief.

### Reference

The root landing and title scan routed to storage architecture and agent-memory coverage. The description query surfaced memory coverage and the gap plan, but the exact-mechanism search found no Qwenputer or recurrent-store account. Fully read storage architecture: its claim concerns Commonplace's selected authority and lifecycle roles, not alternative physical memory implementations. Rejected it as an unnecessary `see-also` destination. The gap-plan and coverage descriptions likewise offer no source-specific operational change supported by this ingest. No reference edge retained.

### Agent memory systems

The root landing explicitly describes a frozen historical corpus. Title scanning and descriptions identified KBLaM as the strongest model-integrated memory comparison. The broad adjacent-concept query matched many review contracts and reviews; generic storage/activation mentions were not treated as sufficient evidence. Fully read KBLaM and kept the named comparison between learned attention-tensor injection and assigned file operations over recurrent state. Followed KBLaM's links to representational form and storage/activation, already read in the theory pass. No return edit is proposed to the frozen review.

### Agentic systems

The landing and complete title scan showed current reviews and archived analyses, but no Qwenputer coverage. The exact-mechanism query returned no match. Description and adjacent searches surfaced execution substrates and compilation accounts, not an exact recurrent file interface. Fully read the archived JEPA-Anything review and checked `rg -n -i 'memory|checkpoint|state' kb/agentic-systems/reviews-archive/jepa-anything.md`: its compiler emits scaffolds and does not expose an accumulated-memory recall path. Rejected compilation as a sufficient shared axis. No agentic-system edge retained, and no archived analysis or comparison population is proposed for modification.

### Tags

Read the tags landing and collection contract. The descriptions and body matches routed to artifact analysis and computational model; fully read both heads as discovery aids. Artifact analysis led to the primary notes and definitions, and computational model reinforced the symbolic-operation neighborhood. `artifact-analysis` declares `complete: true`, so no by-tag `rg` was run for that head. The source has no tags to drive further tag queries. Sources is not a participating collection in the tag contract, and its outbound label table authorizes no tags label; therefore no source membership or formal head connection is proposed.

### Sources

The root landing and full title scan surfaced Nested Learning, the full Mobius paper ingest, runtime-independent persistent agents, and several broad memory surveys. Description scanning and the exact-mechanism query distinguished the full Mobius ingest from its abstract-only companion and identified Nested Learning's recurrent-state discussion. Fully read Nested Learning, the full Mobius ingest, and RIPA. Kept the first two on explicit mechanism axes; rejected RIPA because its governed workflow continuation is not what Qwenputer's file persistence demonstrates. Followed Mobius's KBLaM connection and Nested Learning's explicit-retention connection, both assessed above. Broad memory surveys were not retained merely for sharing the memory topic.

### External and verification

The external source URL is already the ingest's provenance. Its `derived-from` relationship is known, not a new discovery; no redundant footer edge is proposed. External prospecting was skipped.

`rg -n 'qwenputer\.ingest\.md' kb/theory/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'` found no incumbent inbound Markdown citation. Candidate paths were verified on disk, and relative report links were checked before validation.

## Connections Found

The first two relationships already appear in the ingest's prose. They are retained here to identify their candidate labels and return needs, not to recommend duplicate links.

- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md) — **is-evidence-for**: Qwenputer supplies a reported boundary case in which compiler-assigned rules execute a selected calculation inside forward passes. The reader gains a concrete way to separate physical executor placement from learned interpretation. This qualifies the implementation range; it does not corroborate a universal reliability advantage.
- [Explicit retention provides direct targets for selective revision](../../../../theory/only-explicit-retention-is-durable-writable-and-addressable.md) — **is-evidence-for**: reported named put/append/get/list/delete operations and explicit state reload supply a concrete persistence and writability profile for numerical recurrent state. The case makes the note's operation-based comparison usable without claiming commitment-level selective revision.
- [KBLaM](../../../../agent-memory-systems/reviews/KBLaM.md) — **compares-with**: both integrate memory into model computation, but KBLaM uses learned encoders and attention tensors while Qwenputer reports exact named-file access through compiled operations. Readers can compare access and update semantics rather than treating all model-integrated memory as one architecture. The KBLaM account is code-grounded; Qwenputer remains creator-reported.
- [Nested Learning](../../../../sources/nested-learning-the-illusion-of-deep-learning-architecture.ingest.md) — **compares-with**: both discuss recurrent or numerical memory, but Hope's multi-frequency adaptive state lacks the explicit file handles that Qwenputer reports. The comparison separates update cadence and persistence from an interface for targeting stored text; neither result establishes selective revision of semantic commitments.
- [Intern-S2-Mobius, full paper and implementation ingest](../../../../sources/intern-s2-mobius-arxiv-v1.ingest.md) — **compares-with**: Mobius separates architectural knowledge and reasoning roles while retaining learned expert weights; Qwenputer separates learned interpretation, assigned CPU execution, and writable recurrent files. This comparison prevents role separation or placement inside a model from deciding the mechanism's classification. It is not a common-benchmark performance comparison.

## Bidirectional Candidates

These are new return-edge candidates under the theory contract, independently useful despite the source already linking outward.

- [Symbolic-operation note](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md) → source — **evidenced-by**: add a bounded implementation example showing that assigned symbolic execution need not reside in an external Python process. The source qualifies the implementation range; its combined arithmetic comparisons do not isolate placement as the cause and are not a refutation attempt against the note.
- [Explicit-retention note](../../../../theory/only-explicit-retention-is-durable-writable-and-addressable.md) → source — **evidenced-by**: use the reported recurrent file store to make the context-conditioned-state row concrete: persistence depends on save/load, and named operations provide file-level handles. This qualifies the operation profile, not the note's general claim through corroboration; storage access is not demonstrated semantic selectivity.

## Reverse-edge Candidates

- [Representational form](../../../../theory/definitions/representational-form.md) → source — **evidenced-by**: a bounded misuse-case example could distinguish compiler-assigned circuit weights, learned Qwen weights, and stored text in one numerical implementation. The reader gains a concrete check against classifying solely by checkpoint location or numerical encoding. The theory contract authorizes this source destination. This would qualify application of the existing definition, not refute it or establish a fourth form; the reported one-hot file interface does not demonstrate non-localized vector-symbolic content.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Parametric reproduction alone cannot replace an authoritative record](../../../../theory/parametric-reproduction-cannot-replace-an-authoritative-record.md) — the ingest correctly leaves governed authority unestablished. Exact byte retention is not a source observation of authority transfer, so the candidate adds less than the explicit-retention comparison and risks implying that Qwenputer's files are parametric reproduction.
- [Storage architecture](../../../../reference/storage-architecture.md) — describes Commonplace's chosen canonical and reconstructable roles; Qwenputer does not supply a concrete change to those boundaries. Shared storage vocabulary is insufficient.
- [JEPA-Anything](../../../../agentic-systems/reviews-archive/jepa-anything.md) — compiling a research scaffold and executing a compiled CPU are different causal jobs. The reviewed compiler also has no accumulated-memory recall path; compilation alone does not justify a useful comparison.
- [Runtime-Independent Persistent Agents](../../../../sources/runtime-independent-persistent-agents.ingest.md) — checkpointing is a real shared term, but RIPA's governed successor authority and executable workflow continuation exceed Qwenputer's demonstrated file-state save/load. No task-continuation equivalence should be inferred.

## Index Membership

None

Sources is outside the declared tag participation set. No system-review roster or analysis matrix membership is proposed for this ingest.

## Synthesis Opportunities

None

## Maintenance Observations

The [authoritative-record note](../../../../theory/parametric-reproduction-cannot-replace-an-authoritative-record.md) and [Nested Learning ingest](../../../../sources/nested-learning-the-illusion-of-deep-learning-architecture.ingest.md) still use older exclusivity-shaped link text for the explicit-retention note, whose current title and body explicitly reject that exclusivity. These are stale descriptions of a live target, not broken paths. A later maintenance pass can align the link text without changing the source observations.

## Flags

- The ingest is creator-reported and has no retained source quotes. Before authoring a load-bearing theory-side example, retain supporting source wording through the grounding workflow or explicitly require the pinned snapshot for that use. This report does not perform grounding or independently verify exactness, benchmark outcomes, or memory reliability.
- No contradiction or split candidate is asserted. The retained connections concern two coupled mechanisms: assigned execution and writable state. File-level addressing does not establish criticism, selective semantic revision, or a learning loop.
