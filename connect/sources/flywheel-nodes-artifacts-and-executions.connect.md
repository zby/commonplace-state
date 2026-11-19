---
description: "Connection discovery for Flywheel nodes, artifacts, and executions, for downstream source ingest"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/flywheel-nodes-artifacts-and-executions.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Flywheel — Nodes, Artifacts, And Executions

**Source:** [Flywheel — Nodes, Artifacts, And Executions](../../../../sources/.snapshots/flywheel-nodes-artifacts-and-executions.md)

## Discovery Trace

**Setup and scope:** Read `AGENTS.md`, `kb/instructions/cp-skill-connect/SKILL.md`, `kb/reports/types/connect-report.md`, and the sources and reports collection contracts. Source frontmatter is present. The authored edge surface is the eventual matching ingest, never the immutable snapshot. Both inputs were read fully; shared navigation was reused, with source-specific evaluations below. Instruction and workshop destinations are excluded. External discovery was skipped; only the original supplied URL is retained.

**Curated heads:** Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. No source tags exist, so no tag-based README or by-tag search was applicable.

**Titles and descriptions:** Generated `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The broad output exceeded tool display limits; reran notes separately and narrowed other destinations with `rg -i 'research|science|artifact|storage|execution|provenance|hypothes|agora|flywheel|summary|summaries|autora|evidence'`. Ran `rg '^description:.*(hypothes|evidence|research|execution|provenance|summary|summar|claim|artifact)'` over all five destinations, then recovered focused descriptions with `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'hypothes|counterevidence|episode evidence|active work|summary|summaries|workshop'` and the other four destinations filtered by `storage|research wiki|Academic Research|AutoRA|Karnofsky|Flywheel`. There are no semantic-search scores.

**Body queries across all five destinations:** `rg -n 'counterevidence|competing hypothes|evidence artifacts|run history' ... --glob '*.md'` found the discovery-lifecycle definition, trace-retention cases, and research comparators. A second focused query, `rg -n 'summary|hypothes|evidence|execution'`, covered Storage, Academic Research Skills, AutoSci, AutoRA, and Learning By Writing. Candidate bodies and their caveats, rather than term overlap alone, determined the decisions below.

**Source-specific evaluation by destination:** Notes: kept multiple consumers, active work, and evidence preservation because each identifies a distinct consequence of separating record kinds. Reference: kept Storage, whose evidence/state boundary is a direct architecture comparator. Agent-memory-systems: kept AutoSci's separate raw, wiki, graph, and checkpoint records. Agentic-systems: inspected Academic Research Skills but rejected it here because its Passport protocol and integrity gates are more specific than the record separation being claimed. Sources: kept AutoRA's research state/function comparison; rejected Learning By Writing here because inquiry selection is not this page's distinctive subject.

**Link following:** From active work followed the workshop-layer note; its transient-work versus enduring-knowledge distinction limits any interpretation that a durable node automatically supplies closure. From evidence-preservation and multiple-consumers notes followed their workshop and activation links; storage-to-context distinctions explain why this page cannot establish effective read-back. From Storage followed its authored separation of review evidence and store protocol state within the page. All retained local targets have frontmatter. Read the notes collection outbound rules for the reverse candidate.

## Connections Found

- [Original records documentation](https://docs.flywheel.paradigma.inc/concepts/nodes-artifacts-executions) — **derived-from**: the ingest analyzes this captured record model.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) — **is-evidence-for**: Flywheel explicitly separates graph/work state, evidence outputs, and compute history so people, agents, hooks, and exports can inspect them independently. This is a documented design example, not a consumer-effect evaluation.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — **compares-with**: nodes hold tasks, hypotheses, and current conclusions, while executions hold run history; the target clarifies what further closure and evidence-gate requirements are not specified here.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **compares-with**: artifacts and execution records preserve inspectable evidence separately from compact node summaries. The page does not specify default context assembly, so it does not prove the capture/loading requirement is met.
- [Storage](../../../../reference/storage-architecture.md) — **see-also**: Commonplace provides a concrete local counterpart distinguishing authored knowledge, evidence files, and canonical operational state; compare roles without equating Flywheel records with Commonplace retention areas.
- [AutoRA](../../../../sources/autora-automated-research-assistant.ingest.md) — **compares-with**: both expose research state and produced observations separately from execution responsibilities, but AutoRA specifies a loop of component functions while Flywheel describes durable record kinds and interfaces.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) — **compares-with**: compare how research objects and outputs remain independently addressable: Flywheel uses nodes, attached artifacts, and executions; AutoSci separates raw inputs, typed wiki pages, graph records, and checkpoints.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Serve Multiple Consumers](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) → this source’s future tracked ingest — potential **evidenced-by**: the documented independent inspection of work, outputs, and run history is a concrete design example for avoiding one undifferentiated retrieval surface. Add only after the tracked ingest exists.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Academic Research Skills](../../../../agentic-systems/reviews/academic-research-skills.md) — its Passport resume and integrity gates invite unsupported comparisons with recovery guarantees absent from this page.
- [Learning By Writing](../../../../sources/learning-by-writing.ingest.md) — the current-view mechanism is useful for the method companion, but does not illuminate separate execution and artifact records.

## Index Membership

None. These are source-document ingests, not whole-system analyses eligible for the system rosters.

## Synthesis Opportunities

None. The existing notes already distinguish retained evidence, current interpretation, and work state; these documents add design comparators without yet establishing a new general claim.

## Maintenance Observations

None

## Flags

- Both snapshots declare `capture_scope: partial-source`. Claims below concern the captured documentation, not verified implementation or measured outcomes.
- Broad title and description output was truncated; focused recovery covered the selected neighborhoods, so this standard pass does not claim exhaustive recall.
- Hosted, local repository, and MCP attachment/commit sequences are explicitly different. Do not synthesize one universal mutation transaction or infer artifact reuse guarantees beyond the documented ability to cite shared evidence. The named method companion is already supplied as a snapshot; a later writer may link its ingest once present.
