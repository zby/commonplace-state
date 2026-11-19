---
description: "Discovery report for possible KB connections from the Graphiti source snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/graphiti-temporal-knowledge-graph.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Graphiti: Temporal Knowledge Graph for AI Agents

**Source:** [Graphiti: Temporal Knowledge Graph for AI Agents](../../../sources/graphiti-temporal-knowledge-graph.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/tags-README.md` and the selective `kb/notes/agent-memory-README.md`; the latter routed to artifact-analysis, lifecycle, authority, activation, and the external-system survey.
- Read `kb/reference/README.md`; `storage-architecture.md` was the only direct Commonplace analogue worth opening.
- Read `kb/agent-memory-systems/README.md`; it routed to the code-grounded matrix and the dedicated Graphiti review.
- Read `kb/agentic-systems/README.md`; no whole-harness candidate matched a graph-memory subsystem snapshot.
- Read `kb/sources/README.md`; source-to-source comparisons were then checked by scoped search rather than treated as a casebook index.
- The source has no `tags:` field, so no complete tag README could replace a by-tag search.

**Full title and description scans:**

- Generated the complete title surface for each authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; filtered candidates with `schema|database|file|graph|temporal|invalidation|authority|lineage|derived|rebuild|memory|retrieval|episode`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` for the same five destinations and filtered with the same concept family. This surfaced the schema-deferral and edge-ownership notes, storage architecture, the dedicated Graphiti review, the cross-system comparison, and several source ingests that compare graph and non-graph memory.

**Body search:**

- `rg -n -i 'graphiti|bitemporal|bi-temporal|temporal invalidation|valid_at|invalid_at' ...` surfaced the dedicated review, the lifecycle note, the cross-system comparison, two stale Graphiti-boundary statements, and existing source comparisons.
- `rg -n -i 'raw episodes|ground truth stream|derived fact|rebuild|reprocess|recomput|canonical|authority|truth-maintenance|temporal validity|validity.*maintain|invalidat' ...` was broad; only candidates whose bodies established lineage, authority, or replay semantics were retained.
- `rg -n -i 'episode.*(derived|source|ground truth|rebuild|replay)|(?:derived|source|ground truth|rebuild|replay).{0,80}episode|graph.{0,80}(derived|rebuild|replay|canonical)|(?:derived|rebuild|replay|canonical).{0,80}graph' ...` surfaced Graphiti's mixed raw/derived graph, kgai's explicit deterministic-replay contrast, and weaker topical matches.
- `rg -n 'graphiti-temporal-knowledge-graph(\\.ingest)?\\.md' kb --glob '*.md' ...` found existing inbound links from the anti-graph source ingest, Mem0, and Cognee; it also confirmed that the repaired schema-deferral note does not link Graphiti.

**Pinned implementation check:**

- Read the pinned Graphiti checkout at `34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6`. Its README calls episodes the raw ground-truth stream and facts derived. `graphiti_core/graphiti.py:add_episode_bulk()` accepts `RawEpisode` inputs, saves episodes, extracts and resolves nodes and edges, and persists resolved and invalidated edges. Examples clear a store and ingest source episodes. This establishes a reprocessing path, not a clean-store replay guarantee or equivalent output.

**Link following and candidate evaluation:**

- Followed the dedicated [Graphiti review](../../../../agent-memory-systems/reviews/graphiti.md) through its artifact-analysis, write-side, read-back, curiosity, and related-system sections. Kept it as the primary companion because it is code-grounded and explicitly separates imported episodes from LLM-derived facts, timestamps, summaries, and contradiction judgments.
- Followed the repaired [schema-deferral note](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) into the edge-ownership note and Commonplace storage decision. Kept the schema note because Graphiti now tests its distinction between substrate, derivation, and governing commitment; rejected the edge-ownership note because Graphiti's topology does not itself settle ownership or substrate.
- Followed [kgai](../../../../agent-memory-systems/reviews/kgai.md) because it supplies the missing controlled contrast: an append-only file log, an explicitly throwaway graph, deterministic replay, and a canonical digest. Kept it to show what evidence Graphiti would need before its graph could be called reproducibly derived.
- Followed the lifecycle note and comparative review. Kept temporal lifecycle as a bounded use case, but rejected substrate-majority and activation claims as orthogonal to the rebuild correction.
- Evaluated existing Mem0, Cognee, CrewAI, and three-space comparisons. Kept only the anti-graph essay as a useful source-to-source tension; the rest duplicate the dedicated review or do not bear on authority/replay.
- External prospecting was skipped. The already-known Graphiti repository is recorded in the snapshot and the pinned code review; no additional external target is needed.

## Connections Found

- [Canonical files may defer a shared schema while database authority remains a separate commitment](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — **compares-with**: Graphiti stores raw episodes and generated graph facts in one database, so it tests the note's rule that substrate alone does not decide which state is canonical or derived.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: Graphiti implements temporal invalidation and point-in-time fact fields as a concrete lifecycle mechanism, without establishing that every retained graph field is irrebuildable authority.
- [Storage](../../../../reference/storage-architecture.md) — **see-also**: Commonplace's authored-file/derived-index/canonical-operational-store split gives a local comparison for classifying Graphiti per state class rather than per database.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **see-also**: the later code-grounded review supersedes the snapshot as the strongest local account of Graphiti's mixed raw and generated state, write path, lineage, and authority.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) — **compares-with**: both use a graph to serve temporal knowledge, but kgai declares a deterministic replay contract and canonical file log whereas Graphiti exposes reprocessing without an equivalent replay guarantee.
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — **see-also**: the comparison places Graphiti on axes that discriminate activation and lifecycle independently of graph storage.
- [Three Dimensions That Matter To An Agent Memory Store](../../../../sources/three-dimensions-agent-memory-store-2054246434506199529.ingest.md) — **compares-with**: Graphiti's temporal graph capabilities bound that essay's blanket anti-graph conclusion, while neither source establishes that graph substrate alone determines authority.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

None. Existing source ingests already link the snapshot or ingest where useful. The code-grounded Graphiti review should continue to rely on pinned repository code rather than this manual summary as evidence.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — Graphiti has mutable relation state, but the snapshot supplies no workload comparison and graph topology alone cannot support a substrate conclusion.
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — matching entity and episode node names to cognitive categories is a superficial analogy and does not test the taxonomy's mechanism.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — multiple LLM calls at ingestion are topical evidence of cost shifting, but the snapshot gives no comparative context budget or outcome measurement.
- [Claw learning loops must improve action capacity, not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — Graphiti is a retrieval subsystem, not evidence about whether a complete learning loop improves action capacity.
- Mem0, Cognee, and CrewAI source comparisons — useful at survey time but redundant with the current code-grounded reviews and unrelated to the authority/replay correction.
- `kb/agentic-systems/` — MCP and API surfaces do not make Graphiti a whole agentic harness; no candidate passed the collection trigger.

## Index Membership

None. Graphiti already has a dedicated code-grounded review and a row in the agent-memory systems table.

## Synthesis Opportunities

None. The lifecycle note already states the temporal-memory distinction, while the schema-deferral note now carries the more general authority/derivation boundary.

## Maintenance Observations

- The existing ingest says the schema-deferral note names Graphiti as authoritative and says its graph cannot be rebuilt. The current note omits Graphiti, and the pinned implementation exposes reprocessing from retained `RawEpisode` inputs. Both statements require correction.
- The existing ingest's “no further action” disposition depends on that defeated claim and must be reopened.
- [Brainstorming: how explanatory-reach informs KB design](../../../../notes/brainstorming-how-explanatory-reach-informs-kb-design.md) still refers twice to a Graphiti boundary section that the repaired schema-deferral note no longer contains. This is an inbound-maintenance issue, not an edge to author from the source.
- Reprocessing and reproducible rebuild remain distinct. The inspected code does not establish a supported clean-store rebuild command, byte-identical state, decision-identical LLM extraction, or equivalent search results under pinned model, embedder, ontology, prompt, and ordering inputs.

## Flags

- **Lineage tension:** Graphiti's documentation calls episodes ground truth and facts derived, but raw episodes, generated facts, invalidation judgments, and indexes coexist in the graph database. Classification must be per state class.
- **Open replay question:** a clean-store experiment is needed before claiming either irrebuildability or reproducible derivation for the generated graph state.
