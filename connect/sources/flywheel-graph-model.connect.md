---
description: "Discovery inputs for ingesting Flywheel's research graph: ancestry, alternatives, evidence attachment, and limits of provenance."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/flywheel-graph-model.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Flywheel — Graph Model

**Source:** [Flywheel — Graph Model](../../../../sources/.snapshots/flywheel-graph-model.md)

Produced with `cp-skill-connect` by the delegated Codex worker. These are candidate edges for the future name-paired ingest, not edits to the immutable snapshot.

## Discovery Trace

**Scope and authority:** Read the source fully, `sources/COLLECTION.md`, `reports/COLLECTION.md`, and the connect-report type. Prospected all five authorized local destinations. Excluded instructions and work. The source has no tags, so matching-tag head reads and by-tag searches do not apply. `agent-memory` in the label table is interpreted as the expressly named `agent-memory-systems` destination.

**Curated heads and title surface:** Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Generated fresh title listings with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Broad command displays exceeded output limits; focused description and body searches below recovered the relevant neighborhoods. No semantic scores were used.

**Description scan:** Ran `rg -n '^description:.*(lineage|graph|commit|staging|transaction|provenance|decision|audit|alternative)'` over those five destinations with `--glob '*.md'`. Candidate evaluation by destination:

- **Notes:** decision-surface capture and lineage were useful; structural/epistemic/implementation lineages was a false friend about intellectual antecedents, not research ancestry.
- **Reference:** design-rationale management identifies the exact contrast between explicit graph ancestry and Commonplace's distributed rationale records.
- **Agent memory systems:** the curated head and descriptions exposed Semiont and AutoSci. Semiont offers a useful comparison of the durable graph unit; AutoSci's inspected scope excludes its paper-branch DAG, so it cannot establish the apparent close match.
- **Agentic systems:** the curated head and `rg -n -m2 'branch|ancestry|lineage|merge'` on `reviews/eigenius.md` exposed branch/merge machinery, but the selected evidence concerns capability and authorization boundaries rather than preservation of research alternatives; no edge retained.
- **Sources:** Agora is the strongest comparison because contribution parentage carries research dependence and negative outcomes. Read its complete ingest rather than treating the improved task score as evidence for graph benefits.

**Body search:** Ran `rg -l 'ancestry|failed experiment|competing explanation|research graph'` over the same five destinations. Agora survived; generic graph, research, and branch hits did not independently justify edges. Also ran `rg -n -m2 'branch|ancestry|lineage|merge'` against the selected theory-lineage note, decision-capture note, AutoSci review, Agora ingest, Eigenius review, and design-rationale reference.

**Link following:** Followed decision-surface capture to the lineage definition and `history-has-one-chance-to-become-checkable.md`, reading both. The history note supplied the narrower corroboration target. Followed the memory index's event/projection discussion into Semiont: source-anchored annotation events differ concretely from Flywheel's durable work nodes. Read Agora's connection neighborhood, including its stated Git/SQLite boundary, to keep domain ancestry distinct from ordinary file version history.

**External:** Evaluated the source URL already present in the snapshot. Other source-page links are navigation companions; no web prospecting occurred.

## Connections Found

- [Agora: Git as Shared Memory for Collective AutoResearch](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) — **compares-with**: both retain branching research ancestry and unsuccessful work; Agora makes immutable commits and “builds on” parentage its contribution record, whereas this Flywheel page describes work nodes, divergent branches, and merged decisions. Agora's sustained trace also exposes attention-allocation failures that graph availability alone does not settle.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) — **is-evidence-for**: Flywheel explicitly recommends attaching evidence to work and preserving alternatives and merged outcomes so later readers can inspect how a conclusion arose. This is a documented capture design, not empirical confirmation that users actually retain enough evidence.
- [Lineage](../../../../notes/definitions/lineage.md) — **defined-in**: prevents conflating Flywheel's broad ancestry of research work with Commonplace's narrower review-relevant source-dependency field. This page alone does not establish invalidation or regeneration obligations.
- [Design rationale management](../../../../reference/design-rationale-management.md) — **see-also**: gives the ingest reader a concrete Commonplace comparison for retaining alternatives, evidence, and decisions; the reference explicitly says Commonplace does not guarantee end-to-end rationale continuity.
- [Semiont](../../../../agent-memory-systems/reviews/semiont.md) — **compares-with**: contrasts the durable unit and evidence attachment: Flywheel work nodes carry claims, tasks, results, and artifact evidence; Semiont retains source-anchored annotations and canonical events with graph projections. This is a representation comparison, not a claim of equivalent research workflows.
- [Original Flywheel graph-model page](https://docs.flywheel.paradigma.inc/concepts/graph-model) — **derived-from**: the future ingest's analysis is worked out from this captured external page.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) → the future tracked ingest — **evidenced-by**: `notes/COLLECTION.md` authorizes sources as observations corroborating or bounding a claim. The documented evidence-and-ancestry practice is a bounded design example. Wait until the ingest exists; never author the edge to the snapshot, and retain quotes or require the snapshot according to the source-grounding contract.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflective theory refinement has separate structural, epistemic, and implementation lineages](../../../../notes/reflective-theory-refinement-has-three-separate-lineages.md) — shared word “lineage” names intellectual antecedents; it does not explain Flywheel research ancestry.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) — its review explicitly excludes the paper-branch SciDAG system; treating it as a DAG comparison would cross the evidence boundary.
- [Bottom-up structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — useful discovery route, but Flywheel's page does not require the inputs, constraints, approvals, or explanatory receipts needed for this stronger claim. The narrower history-retention edge is sufficient.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The source declares `capture_scope: partial-source`; the excerpt describes product design and modeling advice, not implementation inspection or measured research improvement.
- Keep graph ancestry, evidence sufficiency, and epistemic acceptance distinct. Neither a branch nor a merge establishes that a claim was tested or that conflicting evidence was resolved correctly.
- The authored connection surface is the future ingest. No durable link may target the ignored snapshot.
