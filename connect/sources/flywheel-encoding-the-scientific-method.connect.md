---
description: "Connection discovery for Flywheel encoding the scientific method, for downstream source ingest"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/flywheel-encoding-the-scientific-method.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Flywheel — Encoding the Scientific Method

**Source:** [Flywheel — Encoding the Scientific Method](../../../../sources/.snapshots/flywheel-encoding-the-scientific-method.md)

## Discovery Trace

**Setup and scope:** Read `AGENTS.md`, `kb/instructions/cp-skill-connect/SKILL.md`, `kb/reports/types/connect-report.md`, and the sources and reports collection contracts. Source frontmatter is present. The authored edge surface is the eventual matching ingest, never the immutable snapshot. Both inputs were read fully; shared navigation was reused, with source-specific evaluations below. Instruction and workshop destinations are excluded. External discovery was skipped; only the original supplied URL is retained.

**Curated heads:** Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. No source tags exist, so no tag-based README or by-tag search was applicable.

**Titles and descriptions:** Generated `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The broad output exceeded tool display limits; reran notes separately and narrowed other destinations with `rg -i 'research|science|artifact|storage|execution|provenance|hypothes|agora|flywheel|summary|summaries|autora|evidence'`. Ran `rg '^description:.*(hypothes|evidence|research|execution|provenance|summary|summar|claim|artifact)'` over all five destinations, then recovered focused descriptions with `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'hypothes|counterevidence|episode evidence|active work|summary|summaries|workshop'` and the other four destinations filtered by `storage|research wiki|Academic Research|AutoRA|Karnofsky|Flywheel`. There are no semantic-search scores.

**Body queries across all five destinations:** `rg -n 'counterevidence|competing hypothes|evidence artifacts|run history' ... --glob '*.md'` found the discovery-lifecycle definition, trace-retention cases, and research comparators. A second focused query, `rg -n 'summary|hypothes|evidence|execution'`, covered Storage, Academic Research Skills, AutoSci, AutoRA, and Learning By Writing. Candidate bodies and their caveats, rather than term overlap alone, determined the decisions below.

**Source-specific evaluation by destination:** Notes: kept discovery lifecycle, retained episode evidence, and active work for their distinct testing, reconsideration, and current-state roles. Reference: inspected Storage and rejected a separate link because it adds implementation orientation rather than clarifying this page's hypothesis practice. Agent-memory-systems: kept AutoSci's typed research-state comparator. Agentic-systems: kept Academic Research Skills as a precise comparison of prescribed and checked scientific discipline. Sources: kept Learning By Writing; AutoRA was inspected but deferred because its experiment-function interfaces are a closer connection for the records page.

**Link following:** From retained episode evidence followed its discovery-lifecycle and lineage links; the lifecycle directly explains the status limitation, while source-change lineage is not established here. From active work followed its workshop-layer link; it clarifies why next decisions are live work, but Flywheel's page does not establish the workshop's closure and promotion regime. From claim-title maintenance followed title-as-claim traversal and rejected both as claims about a title convention Flywheel does not require. Read the notes collection outbound rules for the reverse candidate.

## Connections Found

- [Original method documentation](https://docs.flywheel.paradigma.inc/how-to-use-flywheel/encoding-the-scientific-method) — **derived-from**: the ingest analyzes this captured guidance.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **compares-with**: Flywheel keeps support, counterevidence, next steps, and research-state tags together; the lifecycle supplies a comparison that separates testing, named acceptance criteria, and integration. A supported tag is not itself an acceptance gate.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — **compares-with**: artifacts retain inspectable premises behind a changing summary; the note explains why retaining that route enables reconsideration without guaranteeing correct reinterpretation.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — **is-evidence-for**: this documented design explicitly gives current interpretation, operational tags, and next decisions separate roles from the longer reasoning trail. It supplies a design example, not evidence that closure is enforced.
- [Learning By Writing](../../../../sources/learning-by-writing.ingest.md) — **compares-with**: both retain a current written view that changes with evidence, but Flywheel branches competing explanations while Karnofsky emphasizes rewriting a provisional view to direct further inquiry.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) — **compares-with**: compare research-state representation: Flywheel recommends Markdown and operational tags without a special claim schema; AutoSci supplies typed entities and selected executable lifecycle and graph checks.
- [Academic Research Skills](../../../../agentic-systems/reviews/academic-research-skills.md) — **compares-with**: compare evidential standing and its enforcement: Flywheel prescribes evidence-backed writing, whereas the review distinguishes prompt protocols from narrow executable integrity checks.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Active work state](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) → this source’s future tracked ingest — potential **evidenced-by**: use as a documentation-level example of keeping current interpretation and next decisions separate from an audit trail. Confirm the ingest exists and cite it, never the snapshot.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Title as claim exposes commitments](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — Flywheel recommends putting the claim near the top, but does not require a propositional title; it cannot establish the target’s index-scanning mechanism.
- [Storage](../../../../reference/storage-architecture.md) — separation of storage authority is useful for the records companion, but too indirect for this hypothesis-writing page.

## Index Membership

None. These are source-document ingests, not whole-system analyses eligible for the system rosters.

## Synthesis Opportunities

None. The existing notes already distinguish retained evidence, current interpretation, and work state; these documents add design comparators without yet establishing a new general claim.

## Maintenance Observations

None

## Flags

- Both snapshots declare `capture_scope: partial-source`. Claims below concern the captured documentation, not verified implementation or measured outcomes.
- Broad title and description output was truncated; focused recovery covered the selected neighborhoods, so this standard pass does not claim exhaustive recall.
- The document presents a connected research-writing method rather than five independent theoretical claims; no split is proposed. Do not infer automated hypothesis testing, research-state validation, or effectiveness from the recommendations.
