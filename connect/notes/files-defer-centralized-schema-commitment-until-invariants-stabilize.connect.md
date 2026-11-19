---
description: "Discovery report for possible KB connections from the repaired schema-deferral note"
type: kb/cache/types/connect-report.md
source: "kb/notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Schema timing and database authority

**Source:** [Canonical files may defer a shared schema while database authority remains a separate commitment](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md)

## Discovery Trace

**Source and authorisation:**

- Read the repaired source fully. Its claim separates centralized-schema timing from substrate choice and makes database canonicality depend on an explicit authority decision plus an operative path that installs accepted commitments the files do not determine. Invariants, relation ownership, availability, and rebuildability are evidence to assess, not sufficient authority triggers.
- Read `kb/notes/COLLECTION.md` and `kb/cache/types/connect-report.md`. The source contract authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`, while excluding `work`. Already-known external targets are allowed, but open-web prospecting is not; no external search was run.

**Curated heads and tag routing:**

- Read `kb/notes/tags-README.md` and `kb/notes/architecture-README.md`. The architecture head does not declare `complete: true`, so ran `rg -l '^tags:.*\barchitecture\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` rather than treating the curated list as complete.
- Read `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.

**Complete title and description surfaces:**

- Generated each authorised destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`, then filtered for `schema|database|file|storage|authority|commitment|derived|rebuild|edge|invariant|lineage|canonical|constrain` and destination-specific variants.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` across all seven destinations with the same concept family. The strongest neighborhoods were derivation-versus-commitment, artifact-analysis axes, derived-copy safety, storage architecture, file-backed systems with database projections, and source ingests that still describe the old database triggers.

**Body and backlink search:**

- Ran `rg -n -i 'files-defer-centralized-schema-commitment-until-invariants-stabilize|files defer (a )?(shared |centralized )?schema|schema[- ]deferral|schema commitment|Graphiti section|Graphiti boundary|where files yield|files[- ]first boundary|database authority' kb --glob '*.md' ...` to locate direct and unlinked conceptual inbounds.
- Ran `rg -l 'files-defer-centralized-schema-commitment-until-invariants-stabilize\\.md' kb --glob '*.md'` and inspected every durable inbound under `notes`, `agent-memory-systems`, and `sources`; generated reports and historical/workshop records were not treated as authored graph state.
- Ran `rg -n -i 'write-time invariant.{0,100}database|database.{0,100}write-time invariant|cannot.{0,80}rebuild|where validity is maintained|mutable state cannot be assigned|database trigger|files.{0,40}yield|unowned state|ownerless relation'` over durable collections. This isolated the remaining material imports of the defeated trigger claims.

**Link following and evaluation:**

- Followed every existing outbound link from the source one hop: constraining, progressive constraining, derivation versus commitment, governing writes, lineage, checked derived copies, edge ownership, Fintool, storage architecture, and the review-state ADRs. Most plausible theory candidates were already incorporated.
- Followed [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md), which independently separates content recovery from governed authority transfer. Kept it as a cross-substrate extension, not as a premise required by the source.
- Followed [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md). Kept it because it prevents the source's narrow timing/authority claim from being mistaken for an access-architecture decision; its current inbound wording is stale and needs repair.
- Followed code-grounded [Gnosis](../../../../agent-memory-systems/reviews/gnosis.md) and [kgai](../../../../agent-memory-systems/reviews/kgai.md). Both supply clean witnesses that a database or graph can be operationally useful while a separate record stays canonical; kgai additionally declares deterministic replay and a canonical digest.
- Followed [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md) under its collection contract. Its dataset-scoped SQLite staging is a useful reverse-direction case because it remains discardable until reviewed material is promoted.
- Evaluated Graphiti, Basic Memory, Engraph, CocoIndex, Fintool, Sig, Cognee, Mem0, and the file-wiki sources. Rejected parallel examples when they duplicated the source's existing witnesses or lacked evidence about schema timing, replay, acceptance, or authority.
- Read the types and instructions collection contracts. No type contract or executing procedure depends on this note strongly enough to warrant an additional edge.

## Connections Found

- [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **contrasts**: schema timing and state authority are only one part of an access architecture; pointers, traversal, activation, transformation, synthesis, and maintenance remain separate choices.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) — **extends**: shows the same authority-transfer distinction in a different representational substrate, where reproducing content likewise does not substitute for a governed authoritative record.
- [Gnosis](../../../../agent-memory-systems/reviews/gnosis.md) — **evidenced-by**: code inspection finds canonical repo-owned JSONL entries plus a disposable SQLite FTS5 projection, demonstrating that database use and ranking dependence do not by themselves transfer authority.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) — **evidenced-by**: its append-only decision log is canonical while a Kuzu graph is explicitly throwaway and deterministically rebuilt, giving a concrete replay-contract witness for the source's per-state-class authority analysis.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) → source — **is-evidence-for**: dataset-scoped SQLite, chunks, embeddings, and maps remain discardable exploration state until selected material is promoted into reviewed Markdown commitments.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) and its [source ingest](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — reprocessing exists but reproducible replay and acceptance semantics remain unresolved; the repaired note correctly does not need this ambiguous example.
- [Basic Memory](../../../../agent-memory-systems/reviews/basic-memory.md) and [Engraph](../../../../agent-memory-systems/reviews/engraph.md) — both use file sources plus database/search mirrors, but Gnosis and kgai provide cleaner evidence for discardability and replay.
- [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md) — its serving targets and internal update state mix derived and authoritative roles; useful for a deeper state-class audit, but not a clean illustration.
- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md), [Storage](../../../../reference/storage-architecture.md), and [010-review state should move to SQLite](../../../../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — already incorporated into the source; additional parallel links would duplicate its proof.
- Generic filesystem adoption cases such as Karpathy's wiki, the Claude/Obsidian guide, Sig, and the harness anatomy source — they show that files are usable or popular, not when a centralized schema should bind or where governing authority resides.
- `kb/types/` and `kb/instructions/` candidates — structural contracts and current file-based procedures instantiate the local system but do not independently support this theoretical claim.

## Index Membership

None. The source is already present in the curated [Architecture](../../../../tags/architecture-README.md) head.

## Synthesis Opportunities

None. The repaired source already synthesizes schema timing, derivation, authority transfer, edge-key pressure, operational dependence, and the Commonplace witness.

## Maintenance Observations

- [Axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md) calls the source a substrate claim. The repaired source explicitly says centralized-schema deferral is a timing choice and uses the four axes to separate substrate from lineage and authority.
- [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) says the source narrows the design space to substrate choice. It now narrows schema timing and authority within that design space; substrate remains workload-specific.
- [Brainstorming: how explanatory-reach informs KB design](../../../../notes/brainstorming-how-explanatory-reach-informs-kb-design.md) twice cites a Graphiti boundary section that no longer exists. Its boundary example should be the source's explicit separation of schema timing, workload pressure, and authority transfer.
- [Why directories despite their costs](../../../../notes/why-directories-despite-their-costs.md) calls the source a “substrate bet.” Its body may use canonical files as a local premise, but the linked claim is no longer that files win the substrate comparison. The note also contains older Commonplace inventory unrelated to this connection repair.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) has obsolete link text but a still-valid contrast; it needs only a title/context refresh.
- [Tracecraft ingest](../../../../sources/arrmlet-tracecraft.ingest.md) says schema deferral gives browsing and inspectability “for free” and calls optimistic locking a database trigger. The repaired note says file affordances are contingent and invariants alone do not transfer database authority.
- [Portable context-layer ingest](../../../../sources/from-harness-lock-in-to-portable-context-layer.ingest.md) calls relation-owned mutable state a sharper structural trigger. The repaired edge note requires a concrete workload comparison instead.
- [Mem0 ingest](../../../../sources/mem0-memory-layer.ingest.md) calls database-first storage the opposite bet and asserts universal losses of diffability, version control, and toolchain support. The repaired source treats substrate separately and rejects those universal implications.
- [Harness anatomy ingest](../../../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) treats “filesystem is foundational” as evidence for schema deferral. That supports a storage-use claim, not the source's timing or authority conditions.
- Several additional source ingests use generic filesystem adoption as support for schema deferral without evidence about timing or authority. These are weak connection-quality issues rather than contradictions and can be pruned in a later source-ingest review.
- Generated review/friction reports and historical workshop records still quote superseded formulations. They are evidence of earlier states, not authored current claims, and should not be rewritten as if they were current library artifacts.

## Flags

- **Inbound semantic drift:** at least eight durable callers still import parts of the superseded trigger/substrate claim. Repair should update or remove those local characterizations without changing the rebuilt source again.
