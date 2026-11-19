---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/reference/agent-memory-coverage.md"
source_has_frontmatter: true
date: "2026-04-25"
depth: standard
---

# Connection Report: Agent memory coverage

**Source:** [Agent memory coverage](../../../../reference/agent-memory-coverage.md)

## Discovery Trace

**Source and rules read:**
- Read [Agent memory coverage](../../../../reference/agent-memory-coverage.md). The source is a descriptive coverage map for how Commonplace realizes agent-memory requirements through control-plane files, contracts, validation, review, activation, promotion, lifecycle, and IDE-compatible files.
- Read [reference COLLECTION.md](../../../../reference/COLLECTION.md). Authorised destinations: `reference`, `notes`, `agent-memory-systems`, `sources`, and `instructions`; `kb/work/` is explicitly excluded. Main useful labels here: `part-of`/`contains`, `implements`/`implemented-by`, `rationale`, `defined-in`, `derived-from`, `evidence`, `procedure`, and sparse `see-also`.

**Index scan:**
- Read [reference dir-index](../../../reference/dir-index.md). Existing source links already cover [architecture](../../../../reference/architecture.md), [storage](../../../../reference/storage-architecture.md), [control-plane goals](../../../../reference/control-plane-goals.md), [collections and types](../../../../reference/collections-and-types.md), [type loading](../../../reference/type-loading.md), [review architecture](../../../../reference/review-architecture.md), and [instruction generation](../../../../reference/instruction-generation.md). Kept [commands](../../../../reference/commands.md) because the source names commands, validation, indexing, snapshots, promotion candidates, and review commands as memory surfaces but does not yet point to the consolidated command reference. Kept [link vocabulary](../../../../reference/link-vocabulary.md) because the source's composability row depends on collection-owned link labels and reader-need labels, which this page documents for collection authors. Rejected [available types](../../../reference/available-types.md) as already covered by the broader collections/types and type-loading links unless the source later expands its type-system row.
- Read [instructions dir-index](../../../instructions/dir-index.md). Kept [cp-skill-connect](../../../../instructions/cp-skill-connect/SKILL.md) for report-based connection discovery, [cp-skill-ingest](../../../../instructions/cp-skill-ingest/SKILL.md) for source import/evidence workflows, [cp-skill-validate](../../../../instructions/cp-skill-validate/SKILL.md) for deterministic validation, and [evaluate log entry](../../../../instructions/evaluate-log-entry-for-note-creation.md) for the manual observation-to-artifact promotion path. Rejected broad review wrapper instructions because [review architecture](../../../../reference/review-architecture.md) and [REVIEW-SYSTEM](../../../instructions/REVIEW-SYSTEM.md) already cover the load-bearing review surface more directly.
- Read [agent-memory-systems dir-index](../../../agent-memory-systems/dir-index.md) and [agent-memory-systems README](../../../../agent-memory-systems/README.md). No outbound `derived-from`/`evidence` candidates kept: the source is a description of Commonplace, not a design abstracted from one external memory system. The reviewed systems remain better targets from the theory note.
- Read [sources dir-index](../../../sources/dir-index.md) and [sources README](../../../../sources/README.md). No outbound source candidates kept: the source makes no specific external-evidence claim that needs a `sources` link.

**Topic indexes:**
- Source has `tags: []`; no tag index was applicable. Read [agent-memory index](../../../notes/agent-memory-index.md) for possible reverse/index membership because the source describes implementation coverage of agent-memory theory.

**Body search:**
- `rg -n "agent memory|contextual competence|discoverable|composable|trusted|trustworthy|memory system|bounded context" kb/notes kb/reference kb/agent-memory-systems kb/instructions --glob "*.md"` -- confirmed the strongest reverse candidates are [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md), [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](../../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md), and [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md). Also surfaced external-system reviews, but those are not direct outbound targets for this source.
- `rg -n "promotion|promote|lifecycle|cue|activation|generated index|validation|validator|contract|quality goal|review gate|script validation|frontmatter|heading" kb/notes kb/reference kb/instructions --glob "*.md"` -- kept [commands](../../../../reference/commands.md), [link vocabulary](../../../../reference/link-vocabulary.md), [cp-skill-validate](../../../../instructions/cp-skill-validate/SKILL.md), and [evaluate log entry](../../../../instructions/evaluate-log-entry-for-note-creation.md) as concrete implementation/procedure surfaces. Rejected many note hits as theoretical rationale already represented by the source's existing [Designing a Memory System](../../../../notes/designing-agent-memory-systems.md) link.

**Link following:**
- Followed existing source links into [architecture](../../../../reference/architecture.md), [instruction generation](../../../../reference/instruction-generation.md), [collections and types](../../../../reference/collections-and-types.md), [type loading](../../../reference/type-loading.md), [storage](../../../../reference/storage-architecture.md), and [review architecture](../../../../reference/review-architecture.md). These confirmed current coverage but did not create new candidate edges.
- Followed the source's theory link to [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md). That note already links back to [architecture](../../../../reference/architecture.md) and [instruction generation](../../../../reference/instruction-generation.md), but not to the new single-page coverage map; kept a reverse candidate from the theory note to this source.
- Followed [link vocabulary](../../../../reference/link-vocabulary.md) to [ADR 019](../../../../reference/adr/019-collection-owned-link-vocabulary.md). Rejected a direct source link to the ADR: the source needs the current shipped catalogue surface more than the decision history.

## Connections Found

- [Commonplace CLI commands](../../../../reference/commands.md) -- **implemented-by**: the source names commands, deterministic validation, generated indexes, source snapshots, promotion candidates, and review commands as memory surfaces; the command reference is the concrete shipped command surface.
- [Link vocabulary](../../../../reference/link-vocabulary.md) -- **implements**: the source's composability row depends on collection-owned link labels and reader-need semantics; this reference page documents the shared label catalogue and authoring guidance that make those contracts usable.
- [Connect skill](../../../../instructions/cp-skill-connect/SKILL.md) -- **procedure**: the source says automated connection discovery is report-based rather than continuously maintained; this skill is the how-to for producing those reports.
- [Ingest skill](../../../../instructions/cp-skill-ingest/SKILL.md) -- **procedure**: the source's import/evidence row names snapshots and ingest reports as the path from external material into internal memory artifacts.
- [Validate skill](../../../../instructions/cp-skill-validate/SKILL.md) -- **procedure**: the source's trust row names script-based validation of frontmatter, links, enums, required sections, and template headings; this skill is the agent-facing procedure for running that validation.
- [Evaluate a log entry for note creation](../../../../instructions/evaluate-log-entry-for-note-creation.md) -- **procedure**: the source's lifecycle and promotion rows name `kb/log.md` review as a partial candidate-to-artifact path; this instruction is the shipped triage procedure for that path.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -> source -- **evidence** or **see-also**: the theory note contains Commonplace status lines across the requirements; this source is the compact descriptive page showing how those status lines map to shipped system surfaces.
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](../../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) -> source -- **evidence**: the source is a concrete Commonplace implementation map for the note's discoverable/composable/trusted properties.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -> source -- **evidence**: the source describes Commonplace as a memory system distributed across storage, context/routing surfaces, and learning/promotion surfaces rather than as one memory backend.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Available types](../../../reference/available-types.md) -- rejected for now because the source already links the stronger explanatory surfaces [collections and types](../../../../reference/collections-and-types.md) and [type loading](../../../reference/type-loading.md); add only if the type-system row becomes more explicit.
- [Reference README](../../../../reference/README.md) -- rejected as an outbound connection because it is the containing operator guide rather than a specific implementation mechanism; better represented under Index Membership.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) -- rejected as an outbound connection because the source is a Commonplace implementation description, not a comparison against external systems.
- [Sources directory](../../../../sources/README.md) -- rejected as an outbound connection because no specific source or ingest report grounds the descriptive claims in this source.
- [ADR 019 -- collection-owned link vocabulary](../../../../reference/adr/019-collection-owned-link-vocabulary.md) -- rejected in favor of [link vocabulary](../../../../reference/link-vocabulary.md), which is the current operational surface for collection authors.

## Index Membership

- [Reference README](../../../../reference/README.md) -- candidate entry in the reference section: the source is a useful top-level map for readers asking how Commonplace realizes agent-memory requirements as a shipped system.
- [Agent memory index](../../../notes/agent-memory-index.md) -- candidate related-reference entry, not a generated note membership: the index currently points to theory and related systems; this source supplies the Commonplace realization side.

## Synthesis Opportunities

None

## Flags

- The source is intentionally a multi-row coverage map. It touches many surfaces across reference and instructions; that is acceptable while the table remains compact, but if future edits add detailed prose per row, split candidates may emerge around import/evidence, activation, lifecycle, and validation/review.
