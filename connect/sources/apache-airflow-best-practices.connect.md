---
description: "Discovery before Airflow ingest drafting: retry-safe effects, stable replay inputs, task handoffs, and failure-preserving terminal status."
type: types/connect-report.md
source: "kb/sources/.snapshots/apache-airflow-best-practices.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Apache Airflow best practices

**Source:** [Apache Airflow best practices](../../../../sources/.snapshots/apache-airflow-best-practices.md)

Discovery only, produced with `cp-skill-connect` by `gpt-6.1-sol`. The snapshot was read completely, including the continuation after line 793. It has frontmatter; this is not a provisional raw-text report. No implementation or external source was inspected beyond the supplied capture.

The snapshot is immutable. Outbound suggestions below belong in the future authored companion `kb/sources/apache-airflow-best-practices.ingest.md`, which does not currently exist. This report's snapshot link identifies a local input, not a proposed durable citation. Future durable citations of Airflow's statements should use its original URL, or the tracked ingest once authored.

## Discovery Trace

### Setup and search surfaces

- Read `kb/types/connect-report.md`, its schema, `kb/sources/COLLECTION.md`, and `kb/reports/COLLECTION.md`. Source authorization permits prospecting notes, reference, legacy agent-memory systems, agentic systems, tags, and other sources. It excludes work and instructions. Those excluded destinations were not searched for candidates.
- Read each destination's curated `README.md`: notes, reference, agent-memory-systems, agentic-systems, tags, and sources.
- Generated the full fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each destination. Counts: notes 423, reference 212, agent-memory-systems 175, agentic-systems 142, tags 32, sources 511. For sources, `| cut -d: -f2-` reduced output to titles while retaining complete recall. Recovered the omitted beginning of the truncated notes output from the tool's full output. Titles include contracts and auxiliary artifacts, not just candidate library claims.
- For each of the six destinations, scanned descriptions with `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'retry|retries|idempoten|atomic|transaction|orchestrat|checkpoint|recovery|coordination|isolation|pinned|fixed input|failure|durable execution'`.
- For each destination, ran the focused body query `rg -n -i -m2 'idempoten|UPSERT|retry.safe|fixed.input|input.partition|incomplete.results|non.atomic' kb/<destination>/ --glob '*.md'`, followed by the adjacent-concept query `rg -l -i 'replay|retry|retries|shared.filesystem|remote.storage|failure.propagation|partial.output|partial.result' kb/<destination>/ --glob '*.md'`. Recovered the truncated first search output. The second query enumerated paths; strong candidates were then read in full.
- No search scores were available. No external semantic search, web browsing, workers, or commits were used.

### Notes

- The notes landing routes theory through tags. Description/body searches identified explicit replay-state limits in **LLM↔code boundaries**, rerun safety limits in **A checked outcome**, and the channel/guarantee distinction in **Agent orchestration needs coordination guarantees**. Read all three fully and kept scoped candidates.
- Read **Final task success does not establish intended-path health**, reached through the observability head and the checked-outcome neighborhood. Kept a comparison with Airflow's watcher pattern: successful cleanup can determine terminal success despite an earlier failed task. This is not the same mechanism as successful model-generated fallback.
- Read **LLM debugging separates specification gaps, instruction violations, and run-to-run variation** and **Execution indeterminism**. Rejected direct connections that equate changing database partitions or wall-clock inputs with model sampling variation.
- Followed the coordination note's link to **Agent orchestration occupies a multi-dimensional design space**. It supplied useful form/guarantee context, but was too broad for another source-side link.
- Read `kb/notes/COLLECTION.md` for reverse-edge authorization. Its `evidenced-by` label permits sources and external targets, but documentation here qualifies a boundary; it does not corroborate a general theory through a refutation test.

### Reference

- The reference landing and title/description scans identified **Review system architecture** and **Replaceable workflow orchestrators**. Read both fully. Kept sparse `see-also` candidates for all-or-nothing accepted outputs and interruption/replay requirements.
- Followed review architecture to **ADR 035**, read it fully, and confirmed the distinction between fatal evidence-file failure and nonfatal derived-manifest failure. Prefer the architecture page over an additional ADR link.
- Rejected initialization/migration idempotence hits: installation retries are not a sufficiently useful task-execution comparison for this ingest.

### Agent-memory-systems

- The landing identifies this as a frozen historical survey. Title and description scans found many storage and retry mentions; most were acquisition or indexing details, not a strong shared mechanism.
- The focused body search singled out **kgai**: immutable decision events, deterministic identity, atomic graph mutations, and an applied-event watermark. Read its review fully. Kept one historical comparison of replay inputs and duplicate-effect suppression, without treating ingestion identity as semantic deduplication or current-system evidence.
- Rejected an indiscriminate list of vector upserts, installer idempotence, and generic memory-store persistence. These would add traversal cost without clarifying Airflow's task-authoring rule.

### Agentic-systems

- The landing and listings supplied **Agno AgentOS**; the body search found its explicit warning that checkpoint granularity does not make external mutations transactional. Read the review fully and kept a comparison of recovery boundaries and tool-author obligations.
- Search also returned many archived retained analyses. No archived run report was added merely because it mentioned retries; the authored AgentOS review provides the relevant mechanism and caveat directly.

### Sources

- Read the sources landing and scanned the complete titles and filtered descriptions. Strong hits were **Verified Tool Calls**, **Flywheel — Hooks And Automations**, and **ToolGate**.
- Read Verified Tool Calls and Flywheel fully. Kept named-axis comparisons: retry-safe external effects versus verification after uncertain acknowledgement; run deduplication versus effect idempotency.
- Followed Verified Tool Calls' existing link to ToolGate and read that ingest fully. Kept a separate comparison because trusted-state commit and external-output publication are different transaction boundaries. Do not infer that rejected tool output rolls back a remote effect.
- The generic “agent loop” and scheduler-paper titles were not retained: they concern scheduling more broadly and add less than these specific boundary comparisons.
- Checked the paired Airflow ingest and the safe-retry note proposed by Verified Tool Calls. Neither exists. Missing proposed files are not linked as candidates.

### Tags and external

- Read the tags landing and full title surface, descriptions, and both body queries. Then read the architecture, observability, and LLM-reliability heads plus `kb/tags/COLLECTION.md`.
- The source has no `tags:` field, so no matching-tag or by-tag search was required. None of the three selected heads declares `complete: true`; no completeness-based search skip was used.
- Architecture routes state/ownership questions; observability routes terminal-status information loss; LLM reliability makes the sampling-versus-mutable-state boundary visible. Tags are named as a prospecting destination by the source contract but have no authorized source→tags label. A useful navigation candidate is therefore placed under Off-authorisation Candidates rather than assigned `see-also`.
- External prospecting was skipped. The original Airflow URL is already present in the supplied snapshot and is evaluated below as `derived-from`. Other loaded external links are source-local how-to/API references, not useful additional KB connections.
- Verified every local candidate and traversal path before inclusion. No candidate is a write brief or frontmatter-free text target.

## Connections Found

These are candidate edges for the future ingest, not additions to the snapshot. The first group is most useful for drafting; comparisons afterward are optional, not a required footer inventory.

- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) — **is-evidence-for**: Airflow's instruction to read a specific partition rather than “latest,” and avoid `now()` in critical computation, provides a concrete source-side reason for the note's replay scope: visible arguments are insufficient when relevant state changes. This is a documented boundary example, not a test of the general claim.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — **is-evidence-for**: INSERT duplication and changed inputs illustrate the note's narrower warning that retaining a successful episode does not authorize safe literal re-execution. Airflow says nothing about whether an agent's explanation was faithful; do not use it to support that stronger claim.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: compare task handoff guarantees. Airflow distinguishes small XCom messages from remote payload storage and warns that a downstream task may not share a local filesystem; the note distinguishes channels from visibility, ownership, and consistency guarantees. The benefit is a concrete handoff-design check, not a claim that XCom solves semantic consistency.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: compare information loss in terminal status. Airflow's successful teardown leaf can mask an upstream failure unless a watcher depends directly on every monitored task. The note's primary-path/fallback ambiguity is different, but both require preserving intermediate execution evidence rather than inferring path health from final success.
- [Review system architecture](../../../../reference/review-architecture.md) — **see-also**: Commonplace's all-or-nothing review finalization is a local companion for Airflow's “never produce incomplete results” rule. It shows which outputs are accepted evidence and which are reconstructable inspection artifacts; it does not claim cross-system atomicity or retry equivalence.
- [Replaceable workflow orchestrators](../../../../reference/proposals/replaceable-workflow-orchestrators.md) — **see-also**: the unadopted proposal names portable interruption guarantees and warns that replayable `step` is not generally idempotent. Airflow supplies task-author responsibilities a workflow contract could test: stable inputs, duplicate-safe effects, complete outputs, and accessible handoffs. The proposal remains a design option, not operative authority.
- [Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) — **compares-with**: Airflow prescribes duplicate-safe task outputs; the simulation evaluates checking whether an external action already happened before retrying after an ambiguous response. Readers gain the distinction between making a repeated effect safe and deciding whether another execution is needed. The study's bounded simulator and bundled treatment do not establish production reliability.
- [Flywheel — Hooks And Automations](../../../../sources/flywheel-hooks-and-automations.ingest.md) — **compares-with**: compare enqueue/run cardinality with effect idempotency. Flywheel's hook/event deduplication and unchanged-input suppression do not guarantee safe retried HTTP effects; Airflow's UPSERT and partition guidance places that obligation at the task's output boundary.
- [ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) — **compares-with**: compare transaction boundaries. ToolGate checks a returned value before trusted-state commit, whereas Airflow asks tasks not to leave incomplete external results. Guarding downstream context does not itself undo a remote mutation or ensure safe replay.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) — **compares-with**: compare duplicate-safe replay of fixed inputs. The historical review describes immutable content-addressed events and an applied-hash watermark for graph projection; Airflow recommends fixed partitions and UPSERT-style writes. The shared mechanism is stable replay identity plus duplicate-effect suppression, not semantic deduplication or a shared implementation.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — **compares-with**: compare runtime recovery support with task/tool-author obligations. AgentOS explicitly leaves external effects as idempotent as their author makes them; Airflow supplies concrete output and input rules showing why persisted run state or checkpoints alone are insufficient.
- [Original Airflow best-practices page](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) — **derived-from**: the future ingest's analysis is worked out from this supplied official documentation capture. The URL is already in hand; it was not browsed during discovery.

## Bidirectional Candidates

None. No reciprocal edge is useful merely because an outbound comparison exists. The more precise inbound uses are listed below.

## Reverse-edge Candidates

These recommendations concern source-side claims in notes. Under `kb/notes/COLLECTION.md`, **evidenced-by** permits an external citation now or an authored ingest citation later. Neither should target the ignored snapshot. The evidence qualifies the named scope; it is not empirical corroboration of the general note.

- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) → Airflow source — **evidenced-by**: add a concrete boundary example beside “Replay requires the state and external dependencies”: reading “latest” can change a deterministic task's result on retry. Cite the original URL for Airflow's wording, or wait for the paired ingest and its retained support.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) → Airflow source — **evidenced-by**: the warning that a retained episode does not authorize literal re-execution can point to INSERT duplication and fixed-partition guidance. Keep this use limited to rerun safety, not causal explanation or abstraction validity.

## Off-authorisation Candidates

- [Architecture](../../../../tags/architecture-README.md) — the head gives a concrete route from Airflow's task communication and runtime-isolation choices into KB state/ownership theory. The source contract explicitly asks discovery to scan tags but authorizes no source→tags relationship label. Reject this as a formal ingest edge under the current contract; use the head as drafting/navigation context. Extend the contract only if a recurring source-reader need justifies it.

## Raw Text Candidates

None.

## Rejected Candidates

- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — a changing partition or wall-clock input is not token-sampling variation. Airflow is not evidence for the note's claims about decoding or model variability.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — shared retry vocabulary is insufficient. Airflow chiefly addresses effect safety and state stability, not discrimination among three model-output defects.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — useful one-hop context but too broad for another ingest edge; the coordination-guarantees note supplies the concrete handoff comparison.
- [ADR 035](../../../../reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — strong all-or-nothing overlap, but redundant with the kept review-architecture companion. This is rejection of an additional link, not rejection of its technical relevance.
- [LLM reliability](../../../../tags/llm-reliability-README.md) — Airflow alone does not substantively diagnose LLM output deviation. Do not turn infrastructure retry guidance into tag membership for model reliability.

## Index Membership

None. Neither the snapshot nor the future sources ingest belongs to the declared participating collections for tag membership. The sources landing is a collection orientation page, not an ingest roster. No generated index or tag tail is available for editing.

## Synthesis Opportunities

A scoped retry-safety note could combine [the checkpoint note](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) and [the checked-outcome note](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) with Airflow and [Verified Tool Calls](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md). The candidate distinction is: stable inputs make computation replay comparable; complete publication governs visible outputs; idempotency or effect-state verification governs safe repeated external action. These are separate obligations, and none alone establishes safe recovery.

Verified Tool Calls already recommends a safe-retry note, but that proposed path does not exist. Airflow adds fixed-input and incomplete-output mechanisms to that existing follow-up rather than proving a new universal rule. Keep stochastic model calls and genuinely changed input observations outside claims of identical rerun outcomes. No synthesis note was created.

## Maintenance Observations

None.

## Flags

- This is pre-ingest discovery. The paired ingest has not been authored; reverse-edge candidates cannot yet cite it as a local durable target.
- The official page contains independent guidance on retries, task communication, scheduler parsing cost, watcher status, testing, and dependency isolation. Prefer a focused ingest contribution over importing every practice. Only four theory-note connections were retained, so the connect type's five-notes/three-topic split threshold is not met.
- “Treat tasks as transactions” is authoring guidance, not evidence that Airflow provides an atomic transaction over arbitrary HDFS/S3/database effects. Likewise, XCom plus remote storage does not establish delivery, semantic consistency, or exactly-once execution.
- The watcher comparison is bounded: it concerns terminal aggregation masking a failed task, not proof that Airflow synthesized a successful fallback. Its trigger rule only examines direct parents.
- Dependency-isolation and parse-time performance advice remain source content. No additional connection was retained merely to import general Python/deployment engineering into KB methodology.
