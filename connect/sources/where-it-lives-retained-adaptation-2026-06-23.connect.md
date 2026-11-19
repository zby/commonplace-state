---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/where-it-lives-retained-adaptation-2026-06-23.md"
source_has_frontmatter: true
date: "2026-06-23"
depth: standard
---

# Connection Report: Where It Lives Is Not What It Is

**Source:** [Where It Lives Is Not What It Is](../../../sources/where-it-lives-retained-adaptation-2026-06-23.md)

This source is an immutable snapshot. Per [kb/sources/COLLECTION.md](../../../../sources/COLLECTION.md), authored links belong in the companion ingest report, not in the snapshot. The source collection authorizes ingest-report links to `notes` with `evidence`, `derived-from`, `rationale`, `defined-in`, and `see-also`; to `sources` and external-system collections with `compares-with`; and forbids linking into `kb/work/` or `kb/instructions/`.

Dominant finding: the new capture is still the KB owner's externalized artifact-analysis vocabulary, but the June 23 version adds corpus evidence from the 141 code-grounded agent-memory review matrix. The source direction is mostly paper-from-KB: the four-field vocabulary comes from the notes and review contract, while the paper compresses the agent-memory matrix into a publication-facing argument that storage substrate alone discriminates poorly.

## Discovery Trace

**Description listing scan:**
- Ran `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'` and flagged the artifact-analysis cluster, especially [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md), the four field definitions, [the risk-triad note](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md), and [agent-memory comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md).
- Read [kb/notes/artifact-analysis-README.md](../../../../tags/artifact-analysis-README.md). It is `complete: true`, so this report did not need a separate by-tag `rg` sweep for `artifact-analysis`; the curated head already lists the relevant vocabulary and application notes.
- Read [kb/agent-memory-systems/README.md](../../../../agent-memory-systems/README.md). It states that every review applies the same four-field vocabulary and that the ASISAS-2026 frozen corpus is pinned separately, making it the natural current-collection context for the paper's Section 8.

**Topic indexes:**
- [artifact-analysis README](../../../../tags/artifact-analysis-README.md) kept [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md), [the risk-triad note](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md), [memory design adds operational axes](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md), and the definition cluster.
- [agent-memory-systems README](../../../../agent-memory-systems/README.md) kept [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md), [systems-table](../../../../agent-memory-systems/systems-table.md), and [agent-memory-system-review type spec](../../../../agent-memory-systems/types/agent-memory-system-review.md) as the matrix and review-contract surface behind the paper's corpus claim.

**Body search:**
- `rg -n "Where It Lives|where-it-lives|ASIS|ASIS&S|ASISAS|position paper|141" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob '*.md'` found the older ingest, the current risk-triad note's mention that the position paper sharpened sovereignty, [adaptation-agentic-ai-analysis](../../../../notes/research/adaptation-agentic-ai-analysis.md)'s see-also link to the older ingest, and the 141-system matrix pages.
- `rg -n "storage substrate|representational form|behavioral authority|lineage|141|98 of 141|files/repository|acts as an enforced gate|distributed-parametric|pull-only|trace-extracted" kb/notes kb/agent-memory-systems kb/reference kb/sources --glob '*.md'` confirmed that the paper's vocabulary is already current in [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md), the field definitions, the review type spec, and the agent-memory matrix.
- `diff -u kb/sources/where-it-lives-architectural-vocabulary-retained-adaptation.md kb/sources/where-it-lives-retained-adaptation-2026-06-23.md` showed the substantive new material: an "Applying the Vocabulary to a System Corpus" section, a Karpathy seed/corpus-bias caveat, and counts for 98 file/repo systems split by enforcement, distributed-parametric parts, pull-only activation, and trace-extracted lineage.

**Link following:**
- From [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md), followed the definition cluster: [storage substrate](../../../../notes/definitions/storage-substrate.md), [representational form](../../../../notes/definitions/representational-form.md), [lineage](../../../../notes/definitions/lineage.md), [behavioral authority](../../../../notes/definitions/behavioral-authority.md), [retained artifact](../../../../notes/definitions/retained-artifact.md), and [operative part](../../../../notes/definitions/operative-part.md). These are the paper's source vocabulary rather than notes derived from this snapshot.
- From [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md), followed [systems-table](../../../../agent-memory-systems/systems-table.md), [systems.csv](../../../agent-memory-systems/systems.csv), and [agent-memory-system-review type spec](../../../../agent-memory-systems/types/agent-memory-system-review.md). These are the current living surfaces behind the paper's 141-system claim.
- From the old ingest, followed [the risk-triad note](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md). It already promotes the old ingest's recommended sovereignty synthesis, so the new ingest should not recommend that as still-open work.

## Connections Found

- [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md) -- **see-also**: the paper's compact four-field vocabulary is distilled from this note and its definition cluster; the ingest should record paper-from-notes lineage in prose rather than use `derived-from`, whose source-collection meaning runs note-from-source.
- [the four-field record exposes an efficiency, security, and sovereignty risk triad](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) -- **see-also**: the paper sharpened the sovereignty-risk axis and this note has already imported that refinement back into the KB.
- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- **see-also**: Section 8 compresses the current 141-review matrix into an external-facing argument that substrate alone predicts little; the source relation is paper-from-matrix, not matrix-from-paper.
- [systems-table](../../../../agent-memory-systems/systems-table.md) -- **see-also**: the paper's corpus counts and "one storage family dominates, other fields still discriminate" claim depend on the code-grounded systems table/matrix.
- [agent-memory-system-review type spec](../../../../agent-memory-systems/types/agent-memory-system-review.md) -- **see-also**: the paper's corpus is assignable because every review was written under the fixed four-field artifact-analysis contract in this type spec.
- [adaptation signals choose pressure; artifact analysis chooses the retained surface](../../../../notes/research/adaptation-agentic-ai-analysis.md) -- **see-also**: this note already points to the older ingest as the external-facing statement of the vocabulary; it should eventually point at the dated/current ingest if we keep only one current source reference.

## Bidirectional Candidates

None. The snapshot itself should not be edited, and reverse links from notes to this self-authored paper should be deferred until there is a publication/acceptance event that gives the source citable-authority value beyond internal lineage.

## Reverse-edge Candidates

- [the four-field record exposes an efficiency, security, and sovereignty risk triad](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) -> source -- **see-also**: the note already states that the ASISAS position paper sharpened the sovereignty axis; once the paper is accepted or otherwise externally citable, this note is the strongest place for a reference to the dated snapshot or final publication.
- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -> source -- **see-also**: if the paper is accepted, the comparison note may cite it as the frozen external publication of one matrix slice, while keeping the living matrix as the authority for current counts.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- The four field definition notes ([storage substrate](../../../../notes/definitions/storage-substrate.md), [representational form](../../../../notes/definitions/representational-form.md), [lineage](../../../../notes/definitions/lineage.md), [behavioral authority](../../../../notes/definitions/behavioral-authority.md)) were rejected as reverse `derived-from` candidates. The paper is derived from the definitions, not the other way around.
- Individual agent-memory system reviews were rejected as direct connections. The paper's Section 8 uses aggregate matrix fields, not individual systems; direct links to many reviews would be noisy. The comparison note, table, CSV, and review type spec are the right intermediate surfaces.
- [adaptation-of-agentic-ai-survey-post-training-memory-skills](../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.md) was rejected as `compares-with`. It is cited background for adaptation mechanisms, but the paper's new value is the four-field retained-artifact record and matrix application, not a parallel survey classification.

## Index Membership

- [artifact-analysis README](../../../../tags/artifact-analysis-README.md) -- the source is the external-facing version of the tag's central vocabulary, but source snapshots are not added during connect.
- [agent-memory-systems README](../../../../agent-memory-systems/README.md) -- the source belongs as historical/frozen publication context for the 141-system matrix, near the existing ASISAS-2026 dataset note.

## Synthesis Opportunities

The paper now suggests a focused synthesis claim that differs from the old sovereignty follow-up: a storage-dominant corpus can still empirically support a non-storage taxonomy when other fields vary sharply inside the dominant substrate. This may warrant a future note or an addition to [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), but the existing [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) already carries much of it.

## Maintenance Observations

- The old connect report filename uses a title slug that does not match the actual old snapshot basename. The new report uses the actual dated snapshot basename.
- The old ingest's recommended sovereignty synthesis has been completed as [the risk-triad note](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md). A revised ingest should not repeat it as the live next action.

## Flags

- **High-fan-out source:** the paper touches the artifact-analysis vocabulary, the risk-triad synthesis, the agent-memory review contract, and the 141-system matrix. Keep the ingest focused on what changed in this version rather than re-extracting every field definition.
