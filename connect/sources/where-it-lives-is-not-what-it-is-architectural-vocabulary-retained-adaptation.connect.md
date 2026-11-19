---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/where-it-lives-is-not-what-it-is-architectural-vocabulary-retained-adaptation.md"
source_has_frontmatter: true
date: "2026-05-28"
depth: standard
---

# Connection Report: Where It Lives Is Not What It Is — An Architectural Vocabulary for Retained Adaptation in Agentic Systems

**Source:** [Where It Lives Is Not What It Is](../../../sources/where-it-lives-is-not-what-it-is-architectural-vocabulary-retained-adaptation.md)

This source is an **immutable snapshot** (`type: kb/sources/types/snapshot.md`). Per `kb/sources/COLLECTION.md`, snapshots never author outbound links; their authored surface is the matching `.ingest.md` (not yet created), and the load-bearing connect signal is **reverse-edge** — which library notes should add `evidence`/`derived-from` links pointing at this snapshot. The snapshot's outbound destinations authorised for sources are: `notes` (evidence, derived-from, rationale, defined-in, see-also) and `sources`/`agent-memory` (compares-with).

Dominant finding: this paper is the academic write-up of the exact four-field vocabulary (storage substrate, representational form, lineage, behavioral authority) that this KB has already codified across its definition notes and `axes-of-artifact-analysis.md`. No note in the KB currently links to this snapshot (`grep` for the slug returned nothing outside the snapshot itself). The strongest, near-mandatory candidates are reverse `derived-from`/`evidence` edges from those notes.

## Discovery Trace

**Index scan:**
- Read `kb/notes/definitions/` listing — all four field terms exist as definition notes (`storage-substrate.md`, `representational-form.md`, `lineage.md`, `behavioral-authority.md`), plus the supporting vocabulary the paper introduces (`retained-artifact.md`, `operative-part.md`, `knowledge-artifact.md`, `system-definition-artifact.md`). Each is a direct reverse-edge candidate.
- Confirmed `kb/agent-memory-systems/README.md` + `dir-index.md` and `kb/sources/dir-index.md` exist for compares-with prospecting.

**Frontmatter scan of definition notes:**
- Read frontmatter `description`/`status` of all eight vocabulary definitions. All `status: current` except none flagged seedling/speculative. Each `description` restates the paper's claim almost verbatim (e.g. storage-substrate "records where retained state persists, as an operational field distinct from form, lineage, and authority"). High-confidence reverse-edge targets.
- `grep -n "where-it-lives-is-not-what-it-is"` inside each definition note → `(none)` for all. Confirms no edge exists yet.

**Body search:**
- `grep -rln "architectural-vocabulary\|four-field\|behavior-shaping" kb/notes/` → surfaced `axes-of-artifact-analysis.md`, `memory-design-adds-operational-axes-to-artifact-analysis.md`, `designing-agent-memory-systems.md`, `system-definition-artifacts-are-crystallized-reasoning-under-context.md`, plus the four definition notes and several indexes. Read frontmatter of each: `axes-of-artifact-analysis.md` is the central synthesis note recording the four-field record exactly as the paper does.
- `grep -rln "sovereignty\|sovereign" kb/notes/` → no hits. The paper's sovereignty-risk framing (Couture & Toupin; Dale) is not yet represented in any note — noted as a gap, not a connection.
- `grep -rln "behavioral probe\|inspection method\|review evidence" kb/notes/` → `axes-of-artifact-analysis.md`, `definitions/operative-part.md`, `definitions/representational-form.md`, `continual-learning-open-problem-is-behaviour-not-knowledge.md`, `treat-continual-learning-as-substrate-coevolution.md`. Matches the paper's form→inspection-method claim (read / test / probe).
- `grep -rln "prompt-injection\|prompt injection\|data and instruction" kb/notes/` → `llm-context-is-composed-without-scoping.md`. Matches the paper's prose-artifact / data-instruction-blur security claim (Greshake et al.).
- `grep -l "type: kb/sources/types/snapshot"` for compares-with prospecting → reviewed `agent-workflow-memory.md`, `a-mem-agentic-memory-for-llm-agents.md`, `agentic-memory-learning-unified-long-term-and-short-term-memory.md` (all cited or directly parallel to the paper's survey landscape).

**Link following:**
- From `axes-of-artifact-analysis.md` and `representational-form.md` followed one hop into the definition cluster and `treat-continual-learning-as-substrate-coevolution.md` (prose/symbolic/distributed-parametric forms) — confirmed the coevolution note tracks the paper's representational-form families.

## Connections Found

None. The source is an immutable snapshot; per `kb/sources/COLLECTION.md` it authors no outbound links. Outbound candidates below would belong to the matching `.ingest.md` once authored — recorded under Reverse-edge / Off-authorisation for that future author.

## Bidirectional Candidates

None. (No outbound edges from the snapshot, so no return edges to pair.)

## Reverse-edge Candidates

These library notes should author links **to** this snapshot under `kb/notes/`'s own rules (`evidence` = source corroborates the claim; `derived-from` = claim abstracted from this source). All are high-value because the snapshot currently has zero inbound edges and this paper is the published statement of the KB's core vocabulary.

- [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md) → source — **derived-from**: this note's entire claim (record retained artifacts by storage substrate, representational form, lineage, behavioral authority so review evidence, invalidation, and rollback follow how artifacts act) is the position the paper argues; it should cite the paper as the source it abstracts.
- [storage-substrate](../../../../notes/definitions/storage-substrate.md) → source — **derived-from**: definition matches the paper's Section 4 ("Storage Substrate: Where Retained State Lives"); the "operational field, not a sufficient classification" framing is the paper's.
- [representational-form](../../../../notes/definitions/representational-form.md) → source — **derived-from**: prose / symbolic / distributed-parametric three-form split and the form→inspection-method mapping come directly from the paper's Section 5.
- [lineage](../../../../notes/definitions/lineage.md) → source — **derived-from**: "review-relevant source dependencies needed to invalidate, regenerate, retire" matches the paper's Section 6 lineage definition.
- [behavioral-authority](../../../../notes/definitions/behavioral-authority.md) → source — **derived-from**: consumer / channel / force triple is the paper's Section 6 behavioral-authority decomposition.
- [retained-artifact](../../../../notes/definitions/retained-artifact.md) → source — **derived-from**: "retained state a later agentic loop can consume in a behavior-shaping way; boundary is behavioral consequence not storage label" is the paper's Section 2 inclusion-boundary definition.
- [operative-part](../../../../notes/definitions/operative-part.md) → source — **derived-from**: "the behavior-affecting content/structure/parameterization/mechanism … classify the operative part when an object bundles parts" is the paper's operative-part definition (Section 2).
- [knowledge-artifact](../../../../notes/definitions/knowledge-artifact.md) → source — **evidence**: the paper's advice/instruction/enforcement force gradation corroborates the knowledge-artifact (advice/reference/context/explanation) authority family; this is supporting evidence rather than the term's origin.
- [system-definition-artifact](../../../../notes/definitions/system-definition-artifact.md) → source — **evidence**: the paper's instruction/enforcement/routing/validation/configuration/learning forces corroborate this note's authority-path family.
- [memory-design-adds-operational-axes-to-artifact-analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) → source — **evidence**: this note builds operational policy axes *on top of* substrate/form/lineage/authority; the paper is the corroborating statement of the four-field base it extends. (Note is `status: seedling`; `evidence` is additive, so no load-bearing-label flag needed.)
- [continual-learning-open-problem-is-behaviour-not-knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source — **evidence**: the note's claim that behaviour change depends on behavioral authority, with distributed-parametric updates expensive and readable artifacts cheap, is corroborated by the paper's form/authority tradeoff analysis.
- [treat-continual-learning-as-substrate-coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source — **evidence**: the three-representational-form framing (distributed-parametric / prose / symbolic) is the paper's Section 5 taxonomy applied to the coevolution question.

## Off-authorisation Candidates

- [system-definition-artifacts-are-crystallized-reasoning-under-context](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — connects because the paper's "should a lesson stay prose, become symbolic control, be retrieved, or be learned?" design question is the same promotion axis this note analyses (heuristic prose collapsing into knowledge artifacts vs. authority-bearing constraints persisting). `evidence` is the closest authorised label and likely fits (the paper corroborates the form-choice framing); listed here only because the relationship is conceptual-overlap rather than direct derivation — the ingest author should confirm whether `evidence` is warranted or whether it is too thematic to author. Not an authorisation gap.
- [llm-context-is-composed-without-scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — connects because the paper's prose-artifact limitation ("blur the line between data and instructions", prompt-injection risk, effect varies with prompt position/retrieval order) restates this note's flat-concatenation / no-scoping pathology. `evidence` could fit, but the note is `status: seedling` and the link is one specific shared observation rather than the note's whole claim; the ingest author should decide whether to author `evidence` or leave it. Not an authorisation gap.

## Raw Text Candidates

None.

## Rejected Candidates

- [designing-agent-memory-systems](../../../../notes/designing-agent-memory-systems.md) — rejected as a direct reverse edge: it derives agent-memory *design pressures* and points to a requirements inventory; it overlaps thematically but does not restate the four-field record, so a derived-from/evidence edge would be a weak topical association better carried by `axes-of-artifact-analysis.md`.
- `kb/sources/agent-workflow-memory.md`, `kb/sources/a-mem-agentic-memory-for-llm-agents.md`, `kb/sources/agentic-memory-learning-unified-long-term-and-short-term-memory.md` — rejected as `compares-with` candidates. The paper *cites* these (Wang et al. 2025; the A-MEM/agentic-memory line; Yu et al. 2026) as instances classified by its vocabulary, but it is a position paper proposing a classification, not a parallel memory system. `compares-with` reader-need is "covers a similar/parallel system" — these are mechanisms the paper analyses, not systems it parallels. The relationship is better expressed as the future `.ingest.md` citing them inline, not as a snapshot-to-snapshot compares-with.

## Index Membership

- [learning-theory-index](../../../notes/learning-theory-index.md) — the source carries `tags: [academic-paper]` but its content is squarely learning-theory / retained-adaptation; a future writer could surface it from this index's source/evidence section. (Connect does not add the entry.)
- [agent-memory-index](../../../notes/agent-memory-index.md) — the paper's vocabulary is the analytic backbone for agent-memory artifact classification; a curated entry pointing readers to the source paper would help navigation.

## Synthesis Opportunities

The paper raises sovereignty risk (dependence on artifacts the owner cannot inspect, regenerate, delete, or roll back — vendor checkpoints, hosted retrieval indexes) as a first-class architectural concern. `grep` found no note covering sovereignty. Combined with the existing efficiency (recurring prompt/retrieval cost) and security (poisoned high-authority artifacts) framings already present across the artifact-analysis cluster, this implies a candidate note: "the four-field record exposes efficiency, security, and sovereignty risk as a triad." Do not create it during connect; flagged for a future writer.

## Maintenance Observations

- No `.ingest.md` companion exists for this snapshot yet. Per `kb/sources/COLLECTION.md`, the active outbound surface for a source belongs to its ingest report; until one is authored, all the outbound-direction relationships above have no home except the reverse edges. A future ingest run would let the analysis cite `axes-of-artifact-analysis.md` and the definitions inline.
- The four definition notes plus `axes-of-artifact-analysis.md` collectively reproduce this paper's vocabulary with zero attribution links to the published source. This is a durable lineage gap: the KB's core vocabulary lacks a `derived-from` edge to its academic statement. Worth promoting via the reverse-edge author.

## Flags

- **Split candidate:** the source connects to five-plus notes across more than three areas (vocabulary definitions, artifact-analysis synthesis, continual-learning, context-scoping) and makes multiple independent assertions (four-field record; form→inspection method; efficiency/security/sovereignty risk triad; the prose/symbolic/learned promotion design question). When the `.ingest.md` is authored, treat it as a high-fan-out source and distribute citations across the relevant notes rather than concentrating them.
- This snapshot has zero inbound edges despite being the published source of the KB's central vocabulary — the highest-priority follow-up is authoring the reverse `derived-from` edges, especially from `axes-of-artifact-analysis.md` and the four field definitions.
