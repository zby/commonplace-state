---
description: "Connection discovery for Airflow best practices: stable retry inputs, task-boundary guarantees, effect safety, and failure-preserving status."
type: types/connect-report.md
source: "kb/sources/apache-airflow-best-practices.ingest.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Apache Airflow best practices

**Source:** [Ingest: Apache Airflow best practices](../../../../sources/apache-airflow-best-practices.ingest.md)

Discovery-only output from `cp-skill-connect`, following `cp-skill-ground`. The ingest's three retained excerpts establish the requested transaction analogy, same-outcome rerun obligation, and specific-partition input rule. Other ingest analysis remains useful for discovery but is not retained verbatim evidence. No candidate links were authored into library artifacts. The three note connections already described by the ingest are evaluated below, not reported as newly discovered edges.

## Discovery Trace

**Authorization and breadth:** Read `sources/COLLECTION.md` and the ingest fully. Prospected notes, reference, agent-memory-systems, agentic-systems, and sources under the destination-filtered labels table. Work and instructions are excluded. Tags are named in the scan guidance but have no authorized edge label in the table; the ingest has domains, not tags, so no tag-membership or by-tag search was performed. External prospecting was skipped; the already-loaded official URL supplies provenance, not an additional discovery candidate.

**Topic indexes:** Read `notes/README.md`, `reference/README.md`, `agent-memory-systems/README.md`, `agentic-systems/README.md`, and `sources/README.md`. Notes route to theory; reference separates live proposals from shipped state; the memory-system landing marks that corpus historical; the agentic-system landing routes to ordinary authored accounts and warns that generated archives are historical; the source landing describes ingest ownership rather than a topical roster. No index membership follows from these operational landings.

**Title and description scans:** Generated the complete title surface once for each destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. For each of the same five destinations ran `rg '^description:.*([Rr]etr|[Rr]eplay|[Tt]ransaction|[Cc]heckpoint|[Cc]oordination|[Oo]rchestrat|[Ff]ailure|[Pp]ublication)' kb/<destination>/ --glob '*.md'`. Read the truncated command outputs from their full output files.

- **Notes:** Selected checkpoints, coordination guarantees, and terminal-success health from claim titles and descriptions. The body pass additionally found the checked-outcome note's explicit mutable-state/non-idempotent-action qualification. Retained that as an inbound-only candidate. Broader orchestration taxonomy and structured recovery were read through links but rejected as additional outbound edges: the more specific checkpoint and guarantee notes already serve the reader need.
- **Reference:** Selected code-scheduled workflows and replaceable workflow orchestrators for full reading. Both distinguish replay from effects; their useful direction is toward an external task-authoring example from their own retry/interruption discussions, not a source-side account of Commonplace architecture. No architecture or ADR connection was inferred solely from the word transaction.
- **Agent-memory systems:** Selected CocoIndex, which its curated landing describes as incremental infrastructure rather than a primary memory agent. Full reading establishes freshness, memoization, and target reconciliation, but no specific fixed-partition retry comparison. Rejected a broad pipeline association. Other idempotency hits in GBrain, KGAI, and Dense-mem concern particular acquisition/event/promotion paths; no extra edge was retained merely because they use an idempotency mechanism. This corpus remains historical.
- **Agentic systems:** The body pass selected the ordinary Agno AgentOS account, whose recovery paragraph explicitly distinguishes checkpoints from external-effect transactionality. Retained a comparison on author obligations. Generated archived reports also matched idempotency; they were not treated as current system characterizations or additional candidate targets.
- **Sources:** Selected Iceberg reliability and Verified Tool Calls for full reading. Iceberg makes snapshot visibility, atomic publication, and assumption-checked retry explicit; Verified Tool Calls addresses the separate acknowledgement/effect gap. Both add concrete distinctions beyond Airflow's authoring guidance. Flywheel hooks surfaced in the search and existing context, but its unspecified effect guarantees do not add a stronger comparison than these two.

**Body searches:** For each of the five destinations ran `rg -n -m2 'idempoten|fixed.partition|stable.input|UPSERT|atomic.*publish|mask.*failure' kb/<destination>/ --glob '*.md'`. The `-m2` cap limits per-file display, not the set of matching files. Follow-up query: `rg -n 'apache-airflow-best-practices|Airflow|retry|replay|partition' kb/notes/llm-code-boundaries-are-natural-checkpoints.md kb/notes/checked-outcome-licenses-episode-retention-not-abstraction.md kb/reference/proposals/replaceable-workflow-orchestrators.md kb/sources/flywheel-hooks-and-automations.ingest.md`. This confirmed replay qualifications and the proposal's non-idempotent `step` distinction; none of these four files currently links the Airflow ingest. No semantic-search scores were available.

**Link following:** Followed coordination guarantees to the multi-dimensional orchestration note and final-success health to the checked-outcome and structured-recovery notes; read all four. Read Verified Tool Calls, whose comparison paragraph points to ToolGate and GBrain; evaluated those neighboring mechanisms at that paragraph's resolution without asserting uninspected implementation facts. Read both workflow proposals in full. Read `notes/COLLECTION.md`, `reference/COLLECTION.md`, and `agentic-systems/COLLECTION.md` before assigning return/inbound labels. Checked that every included candidate path exists.

## Connections Found

- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) — **is-evidence-for**: Airflow's documented changing-input failure qualifies the note's replay operation: capturing visible arguments is insufficient when the underlying input data can change. This is an official design warning illustrating the scope boundary, not an independent test corroborating the general checkpoint claim. Already described in the ingest.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: Airflow separates retry-input identity, complete results, and accessible payload handoffs from the existence of a task graph or communication channel; the note supplies the broader composition-specific guarantee question. This does not equate task transactions with semantic reconciliation or delegated accountability. Already described in the ingest.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: Airflow's watcher discussion and the note both distinguish intermediate failure evidence from a terminal success flag. Successful cleanup masking failure is not the same mechanism as a model synthesizing a fallback. Already described in the ingest; further grounding is needed for the watcher passage before a load-bearing source use.
- [Ingest: Apache Iceberg reliability](../../../../sources/apache-iceberg-reliability.ingest.md) — **compares-with**: Airflow prescribes retry-stable task inputs and complete outputs; Iceberg describes explicit snapshot reads, atomic metadata publication, and retry admission after checking current assumptions. Reading both prevents treating a transaction analogy or a named partition as an implemented commit protocol.
- [Ingest: Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) — **compares-with**: Airflow's stable-input rule addresses one source of changed rerun outputs; the simulation examines already-applied effects behind ambiguous responses. Stable inputs do not by themselves prevent duplicated external actions. The simulation's fixed tasks and supplied verifiers bound the comparison.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — **compares-with**: Agno's persisted run/checkpoint recovery does not make arbitrary tool mutations transactional; Airflow likewise places same-outcome and complete-output obligations on task authors. This separates runtime recovery facilities from task/effect semantics without asserting equivalent implementations.

## Bidirectional Candidates

- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) → source — **evidenced-by** under `notes/COLLECTION.md`: add a body-level example to the replay scope paragraph using the retained partition quote. The documented update-between-reruns case bounds replay from arguments alone; it is an illustration, not corroboration by an attempted refutation. The return path gives checkpoint readers a concrete input-identity failure case.
- [Ingest: Apache Iceberg reliability](../../../../sources/apache-iceberg-reliability.ingest.md) → source — **compares-with** under `sources/COLLECTION.md`: let readers of the commit protocol distinguish storage-level snapshot/publication guarantees from workflow-author retry obligations. Airflow does not establish immutability merely by naming a partition.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) → source — **see-also** under `agentic-systems/COLLECTION.md`: the recovery caveat could point to official task-authoring guidance as an adjacent example of the obligations checkpoint machinery leaves to authors. Airflow is not evidence for Agno implementation behavior; no source-derived lineage is asserted.

## Reverse-edge Candidates

- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) → source — **evidenced-by** under `notes/COLLECTION.md`: its mutable-state rerun qualification could cite Airflow's exact update-between-reruns warning as a bounded example. This qualifies the re-execution claim, not the separate thesis about faithful explanatory abstraction. No outbound edge is needed from Airflow to the note's larger epistemic argument.
- [Code-scheduled workflows](../../../../reference/proposals/code-scheduled-workflows.md) → source — **see-also** under `reference/COLLECTION.md`: the mechanical-step/effect distinction and replay-discipline discussion could point to Airflow's fixed-input rule as an external authoring example. It helps check which inputs a repeatable step must preserve. Do not label the proposal abstracted or derived from Airflow without actual provenance; the source does not justify the proposal's once-only effect protocol.
- [Replaceable workflow orchestrators](../../../../reference/proposals/replaceable-workflow-orchestrators.md) → source — **see-also** under `reference/COLLECTION.md`: the shared retry/interruption requirements could use Airflow as adjacent guidance for stable inputs and same-outcome task obligations independent of scheduler implementation. Its `step` intentionally consumes worker rounds, so the link must not imply every repeated command should be idempotent or that task determinism transfers to stochastic workers.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md): incremental target reconciliation and fresh serving stores are not enough to establish a specific retry-input or publication comparison. A generic data-pipeline link would broaden the report without a concrete reader benefit.
- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md): detection/corrective/fallback/escalation is broader than Airflow's task-author retry advice. Verified Tool Calls gives a more precise effect-boundary comparison.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md): the ingest adds a concrete guarantee example, not a new scheduler taxonomy dimension. Route through the more specific coordination-guarantees note instead.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The retained Airflow quotes support only the transaction analogy, complete-result obligation, same-outcome reruns, and specific-partition input rule. The watcher, XCom, UPSERT, and remote-storage discussion is ingest analysis, not yet quoted support. Future load-bearing uses of those source passages must invoke grounding rather than relying on this discovery report.
- Verified Tool Calls currently has an empty Quotes section. A future writer using its source claims must ground the needed claims separately; this connect invocation does not authorize that mutation.
- Both workflow proposals remain unadopted designs. The proposed inbound links are reading aids, not adoption decisions or inferred design lineage. Same-outcome guidance for deterministic tasks does not promise identical stochastic model outputs, exactly-once external effects, or semantic correctness.
