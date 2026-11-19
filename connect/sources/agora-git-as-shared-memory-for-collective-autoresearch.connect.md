---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/agora-git-as-shared-memory-for-collective-autoresearch.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Agora: Git as Shared Memory for Collective AutoResearch

**Source:** [Agora: Git as Shared Memory for Collective AutoResearch](../../../../sources/.snapshots/agora-git-as-shared-memory-for-collective-autoresearch.md)

## Discovery Trace

**Collection rules and authored surface:**
- Read `kb/sources/COLLECTION.md`. It authorises prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; excludes `kb/work/` and `kb/instructions/`; and permits `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and sparse `see-also` according to destination.
- The target is an immutable snapshot. Candidate outbound edges therefore belong on the future matching `kb/sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md`, not on this snapshot.
- External prospecting was skipped: no user-supplied external candidate beyond the source itself was in scope, and the skill forbids open-web prospecting.

**Curated heads and title surfaces:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all five authorised local destinations. The most promising title clusters concerned orchestration guarantees, trace authority, canonical/derived storage, shared-state coordination, agent scaling, and open-ended research evaluation.
- The snapshot carries no `tags:` field, so no matching tag-README or by-tag description pass applied.

**Description listing scan:**
- Ran `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' | rg -i 'memory|shared|collective|research|lineage|provenance|verification|diversity|coordination|decentrali|external|artifact|frontier|negative|append|graph'`.
- Ran the narrower follow-up `rg '^description:' ... | rg -i 'coordination|shared state|shared memory|collective|research agent|discovery|lineage|provenance|verification|reproduc|diversity|explor|negative result|external.*outcome|persistent.*adapt|retained artifact|append-only|git'`.
- Kept the coordination-guarantee, trace-authority, storage-architecture, DeLM, Tracecraft, scaling-science, and CRUX candidates below. Huxley-Gödel Machine was evaluated but rejected because its lineage-selection mechanism concerns self-modifying agent descendants rather than a community's shared research record.

**Body search:**
- Ran `rg -n -i "shared (memory|state)|git.*memory|append-only|contribution (graph|dag)|immutable lineage|public frontier|negative results|independent (verification|reproduction)|diversity-aware|monoculture|duplicate(d)? search|collective intelligence|decentralized.*research|coordination substrate"` across all five authorised destinations.
- Ran `rg -n -i "(downstream evidence|reproduction|reproducib|verification.*claim|claims.*artifacts|evidence.*lineage|lineage.*evidence|Git history|shared workspace|institution|attention allocation|exploration.*exploitation)"` across the same destinations.
- Agora's claim graph and verification weights gave a direct articulation to trace authority; its Git-canonical/SQLite-derived split gave a direct Commonplace architecture comparison; and its diversity intervention plus missing control made CRUX and the scaling paper useful evaluative contrasts.

**Link following:**
- Followed the coordination cluster from [agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) to [agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md), [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md), and [DeLM](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md). Kept the first, Tracecraft, and DeLM because each exposes a distinct comparison axis; rejected the broader design-space note as redundant for this source.
- Followed the evidence-quality cluster to [trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). Kept it because Agora explicitly separates asserted contributions from later independent reproduction and downstream use, while warning that its score is not truth.
- Followed source-evaluation neighbors to [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) and [Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md). Kept both because they supply controlled or expert-evaluated contrasts for claims the Agora case alone cannot settle.

## Connections Found

- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **is-evidence-for**: Agora is a concrete shared-state coordination regime whose guarantees are append-only lineage, canonical identity, independent-verification records, self-citation exclusion, and reconstructable indexes; the run also shows that visibility and scoring did not by themselves prevent monoculture or duplicate work.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- **is-evidence-for**: Agora preserves contributions first as claims, then records independent reproduction and downstream use as stronger signals while explicitly denying that the resulting evidence score is a truth signal.
- [Externally tested theory builder](../../../../notes/definitions/externally-tested-theory-builder.md) -- **rests-on**: Agora delegates project objectives, evaluator rules, artifact contracts, and acceptance boundaries to each project, while its community supplies candidate theories and the external evaluator supplies the outcome level; the paper's missing matched arm shows why this interface permits outcome measurement without by itself identifying Agora's causal effect.
- [Storage](../../../../reference/storage-architecture.md) -- **see-also**: Agora and Commonplace both separate canonical retained artifacts from rebuildable SQLite views, but Agora gives Git commits and parent edges domain semantics while Commonplace explicitly keeps commits and merges outside framework-wide correctness semantics.
- [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md) -- **compares-with**: both systems provide asynchronous shared state for independently scheduled agents, but Agora makes immutable contribution lineage, verification, frontier analysis, and attention allocation the primary research-memory semantics, whereas Tracecraft's strongest mechanisms are operational claims, messages, waits, and artifact exchange.
- [Ingest: Decentralized Multi-Agent Systems with Shared Context](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) -- **compares-with**: DeLM studies verification-gated compact shared context inside bounded tasks, while Agora studies durable cross-session research contributions with parent lineage, negative results, reproduction records, and diversity-aware frontier selection; together they separate admission/visibility guarantees from long-horizon institutional memory.
- [Ingest: Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- **compares-with**: the scaling study provides controlled evidence that coordination benefit depends on decomposition, verification, and overhead, while Agora supplies a sustained community trace whose missing isolated and flat-log controls leave the shared-DAG benefit unresolved.
- [Ingest: Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) -- **compares-with**: CRUX reports strong autonomous research engineering but weak open-ended judgment under expert review; Agora reports rapid collective optimization under a hard evaluator, making the pair useful for separating research-institution effects from task oracle strength and research judgment.

## Bidirectional Candidates

None. Reciprocal utility is strongest for the notes and comparisons above, but the durable authored Agora ingest does not yet exist, so no verified return-link target can be proposed.

## Reverse-edge Candidates

None. Several notes could eventually cite the tracked Agora ingest as `evidenced-by`, but collection doctrine forbids durable links to the immutable snapshot and the matching ingest path does not yet exist.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- rejected as redundant: the narrower coordination-guarantee note gives a clearer reader payoff for Agora's shared-state mechanism.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- rejected as too general: Agora clearly adds metadata, lineage, views, and trust signals, but the coordination and trace-authority notes state the more discriminating connection.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) -- rejected because Agora is a useful explicit-record example but does not test or substantially qualify the parametric-substitution claim.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- rejected because clade metaproductivity selects descendants in an agent self-modification tree, whereas Agora scores a multi-author contribution DAG for research attention; the shared lineage vocabulary would invite a stronger equivalence than the mechanisms support.
- [Academic Research Skills](../../../../agentic-systems/reviews/academic-research-skills.md) -- rejected because its staged, host-mediated research pipeline is structurally unlike Agora's planner-free community substrate; generic research-workflow overlap would not help traversal.

## Index Membership

None. This snapshot is an immutable local input and should not be indexed as a library artifact; any future index placement belongs to the tracked ingest or a system analysis.

## Synthesis Opportunities

- Agora, DeLM, and Tracecraft together suggest a higher-order claim: a shared substrate becomes a coordination architecture only when its record types carry workload-specific guarantees. Agora supplies immutable lineage and reproduction semantics, DeLM supplies admission and visibility semantics, and Tracecraft supplies task-claim and delivery semantics. The current coordination-guarantee note contains the general frame but does not yet compare these three concrete regimes.
- Agora and the controlled scaling study together suggest a bounded evaluation principle: sustained multi-agent traces reveal coordination dynamics, but matched arms are required to attribute discovery efficiency to the coordination substrate rather than agent count, task structure, evaluator strength, or intervention.

## Maintenance Observations

None.

## Flags

- The future ingest should preserve the paper's causal limit next to any positive mechanism claim: the 12-day run had no matched isolated or flat-log arm, and the escape from monoculture followed a mid-run human deployment of new diversity views.
- The source makes several independent contributions (shared-memory architecture, evidence scoring, diversity-aware attention, and a weight-transfer result). An ingest can analyze all four, but any later transferable note should split institutional-memory claims from the task-specific model-initialization method.
