---
description: "Iceberg connection discovery: snapshot publication and guarded retries compared with KB coordination, storage choice, and recovery boundaries."
type: types/connect-report.md
source: "kb/sources/apache-iceberg-reliability.ingest.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Apache Iceberg reliability

**Source:** [Ingest: Apache Iceberg reliability](../../../../sources/apache-iceberg-reliability.ingest.md)

Discovery-only candidates produced with `cp-skill-connect` after `cp-skill-ground` validated five retained excerpts. No edges were authored. The ingest's two existing note links remain unchanged; recommendations below identify useful formal roles and possible return paths, not missing outbound navigation.

## Discovery Trace

**Authority and indexes:**
- Read `kb/sources/COLLECTION.md` and `kb/types/connect-report.md` before discovery. Authorized local destinations are notes, reference, sources, agent-memory-systems, agentic-systems, and definitions within notes. Tags are an explicitly named scan surface but have no authorized source-to-tag formal label. Instructions and work are excluded.
- Read `README.md` in notes, reference, agent-memory-systems, agentic-systems, tags, and sources. Read the architecture tag head and tags collection contract. The source has domains but no tags, so no by-tag membership search or completeness skip applies. Sources are outside participating tag membership.
- Generated a fresh complete title listing for each of those six scan surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. The combined console output was truncated; inspected the notes title surface and a focused selection from the complete output using `rg '^kb/(reference|agent-memory-systems|agentic-systems|tags)/.*(storage|freshness|review-architecture|tracecraft|beads|rchitecture|rchestr|recover|concurr|transaction)'`. No semantic-search scores were used.

**Description and body searches, per destination:**
- In each of notes, reference, agent-memory-systems, agentic-systems, tags, and sources, ran `rg '^description:.*(concurren|atomic|retry|retries|transaction|coordination|shared.state|snapshot|publication|storage|recovery)' kb/<destination>/ --glob '*.md'` and `rg -l 'optimistic concurrency|atomic (swap|publication|commit)|consistent snapshot|assumptions.*actions|retries|shared.state' kb/<destination>/ --glob '*.md'`.
- **Notes:** title and description scans selected coordination-guarantees, edge ownership/storage choice, recovery, and orchestration design-space notes. Read all four, plus canonical-files/schema deferral and LLM debugging. Retained the first two as strongest outbound candidates; recovery is a useful inbound illustration. Rejected schema deferral as redundant with the more precise storage-choice destination, and design-space as already routed through coordination-guarantees. Debugging retries concern a different failure mechanism.
- **Reference:** selected and fully read freshness and review architectures. Freshness provides the precise existing stale-work guard comparison. Review architecture supplies atomic-finalization context but is a weaker additional direct edge. Did not treat Iceberg as an implementation dependency of either subsystem.
- **Agent-memory-systems:** selected and fully read the code-grounded Tracecraft review. Retained comparison of S3 conditional-create claims and per-key writes with table-level snapshot publication. The collection landing is historical and frozen; no roster update is proposed.
- **Agentic-systems:** selected and fully read beads_rust. Retained its route-specific local transactional admission as a comparison. Other retry search hits predominantly concerned model search or archived execution reports rather than shared-state commit semantics; no keyword-only edges were retained.
- **Sources:** selected and fully read Airflow best practices, Verified Tool Calls, Flywheel local repository quickstart, and the older Tracecraft ingest. Retained the first three on distinct axes: stable rerun inputs, ambiguous external effects, and inspected-state identity. Preferred the code-grounded Tracecraft review over its earlier README ingest because the latter makes conflicting claims about claiming atomicity.
- **Tags:** architecture head routes to the storage-choice and schema-deferral notes. Used it for discovery, not tag assignment or a formal source-to-tag edge. No source index membership is proposed: sources are not a participating tag collection.
- **External:** the already-known canonical Iceberg URL is the source identity, not a new discovery edge. Open-web prospecting was skipped.

**Link following and focused checks:**
- Followed coordination-guarantees → orchestration design-space and Tracecraft review; followed edge ownership/storage choice → schema deferral, freshness architecture, and review architecture; followed the source-neighborhood recovery links to the recovery note. These revealed the shared-state versus semantic/governance boundary and the Tracecraft discrepancy recorded below.
- Ran `rg -n 'snapshot|atomic|concurren|retry|retries|stale|publication'` over freshness architecture, review architecture, Tracecraft review, beads_rust, architecture head, and Airflow ingest to inspect publication and guard boundaries.
- Ran `rg -n 'concurrent|stale.work|publication|accepted|retry'` over edge ownership/storage choice, schema deferral, and recovery notes. Confirmed that storage preference needs an actual workload comparison, and that recovery should specify a permitted next transition rather than blindly replay.
- Read `kb/notes/COLLECTION.md` for every proposed note-to-source edge. Its `evidenced-by` label permits qualification or bounding, but corroboration requires an attempted refutation; none of the return links below claims corroboration. Verified all evaluated candidate paths exist.

## Connections Found

- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **is-evidence-for**: Iceberg's documented snapshot visibility, atomic publication, and conflict admission provide a bounded engineering illustration of explicit shared-state guarantees. They do not establish semantic agreement, context isolation, or delegation accountability. The existing inline link already supplies navigation.
- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — **compares-with**: Iceberg describes file-backed data coordinated through metadata and an atomic reference update, making the publication machinery part of the concrete storage alternative. It supplies neither an edge-state implementation nor a workload comparison selecting Commonplace's substrate. The existing inline link already supplies navigation.
- [Freshness architecture](../../../../reference/freshness-architecture.md) — **see-also**: compare Iceberg's current-state assumption check with Commonplace's baseline-revision and generation guards. Both reject work whose admission assumptions changed; Commonplace's guard protects baseline concurrency, not live-file currency or semantic truth.
- [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md) — **compares-with**: distinguish atomic creation of one claim object from a coherent snapshot of a multi-file table. S3 conditional-create claims and HuggingFace's check-then-write fallback have different guarantees; neither should be conflated with Iceberg's table commit protocol.
- [beads_rust](../../../../agentic-systems/reviews/beads-rust.md) — **compares-with**: its CLI checks claim and workflow predicates within a local SQLite mutation transaction, whereas Iceberg documents preparation followed by optimistic metadata publication. This comparison exposes the importance of keeping checks on every operative write route; it does not equate local exclusion with distributed branch safety.
- [Ingest: Apache Airflow best practices](../../../../sources/apache-airflow-best-practices.ingest.md) — **compares-with**: Airflow prescribes stable inputs and duplicate-safe task outcomes; Iceberg explains admission against a changed current state. Fixed replay inputs and revalidated commit assumptions are separate requirements, not interchangeable definitions of safe retry.
- [Ingest: Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) — **compares-with**: a known failed metadata swap differs from an ambiguous tool response that may conceal an applied external effect. Iceberg's conflict retry cannot justify blind replay after timeout or partial success.
- [Ingest: Flywheel local repository quickstart](../../../../sources/flywheel-local-repository-quickstart.ingest.md) — **compares-with**: Flywheel identifies inspected staging and committed state and requires renewed inspection after change; Iceberg rebuilds against current state and validates operation assumptions. This distinguishes identifying stale work from deciding which prepared work remains admissible. Flywheel's observation is partial and neither ingest independently tests deployed reliability.

## Bidirectional Candidates

- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) ↔ source — return label **evidenced-by**: add a body-level bounded example of snapshot visibility, atomic publication, and guarded conflict retry to the shared-mutable-memory row. This qualifies that row with a concrete documented mechanism; it is not an independent test of the general coordination claim and supplies no semantic adjudication.
- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) ↔ source — return label **evidenced-by**: add a body-level file-backed publication example that bounds any inference from substrate alone. Name the atomic-reference premise and the absent Commonplace workload/cost comparison. Iceberg is not evidence that edge keys require either files or a database.

## Reverse-edge Candidates

- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) → source — **evidenced-by**: illustrate recovery after an explicitly detected commit conflict: rebuild metadata against current state, check assumptions, then reapply only admitted actions. This bounds the corrective-action branch to a supplied state predicate and known conflict; it does not establish automatic semantic repair or safe retry after ambiguous external effects. The useful direction is from the recovery argument to its concrete example, not an additional broad outbound link from the ingest.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Canonical files may defer a shared schema while database authority remains a separate commitment](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — Iceberg says little about the timing of schema commitment or transfer of authority for agent-authored knowledge. The sharper storage-choice note already carries the useful comparison.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — Iceberg is not an agent orchestrator and supplies no scheduler or context-policy characterization. The existing coordination-guarantees route is more precise.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — stochastic output retries and known metadata conflicts require different diagnosis. Shared vocabulary alone does not justify a link.
- [Review system architecture](../../../../reference/review-architecture.md) — atomic finalization is useful context, but freshness architecture already supplies the closest stale-work comparison and links to it. Avoid a redundant reference link.
- [Ingest: tracecraft](../../../../sources/arrmlet-tracecraft.ingest.md) — older README-grounded analysis conflicts internally about claim guarantees and with the later code-grounded review. Prefer the review for the proposed comparison, without silently resolving the historical discrepancy.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The coordination-guarantees note's Tracecraft footer calls task claiming non-atomic. The older Tracecraft ingest both describes collision prevention and alleges check-then-write claiming, while the later code-grounded review at `7d77daaaf17d3f18b7718e3ddfc8ee2576446adc` identifies S3 `IfNoneMatch` enforcement and a racy HuggingFace fallback. A future maintenance pass should scope claims by backend and observation date rather than carrying a blanket non-atomic characterization forward. Discovery did not inspect the external implementation or edit these artifacts.

## Flags

- The occasion leaves “all of these interactions” unspecified. Treat read–prepare–validate–publish as a shared-state candidate model, not a complete interaction model.
- Iceberg is official design documentation, not independently verified deployment evidence. Its atomic metadata-reference operation is a premise; its retry predicates do not decide whether agent-authored claims remain justified.
- Comparisons using neighboring ingests are discovery judgments based on their authored analyses. This run grounded only the requested Iceberg proposition; it did not ground or revise those sources.
