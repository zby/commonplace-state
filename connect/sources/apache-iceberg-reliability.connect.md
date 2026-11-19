---
description: "Discovery-only connections for Apache Iceberg reliability: atomic publication, snapshot reads, and assumption-checked retries as bounded comparisons for KB storage and agent coordination."
type: types/connect-report.md
source: "kb/sources/.snapshots/apache-iceberg-reliability.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Apache Iceberg reliability

**Source:** [Apache Iceberg reliability](../../../../sources/.snapshots/apache-iceberg-reliability.md)

**Authored surface:** The snapshot is immutable. All outbound suggestions below are for the future `kb/sources/apache-iceberg-reliability.ingest.md`, which does not yet exist. Reverse suggestions likewise target that future tracked ingest, never the snapshot. This report is discovery before drafting, not source analysis or authored edges.

**Operation:** `cp-skill-connect`, executed directly without workers; model `gpt-6.1-sol`. Inputs are the complete snapshot, source collection contract, connect-report type, and current repo-local discovery surfaces.

## Discovery Trace

### Setup and breadth

- Confirmed `kb/sources/COLLECTION.md` exists; read it and the complete connect-report type before discovery. Read the complete snapshot. It has frontmatter, so the report is not provisional on that account.
- Source mechanism: complete file membership is retained in snapshots; writes prepare a new metadata tree and atomically replace the current metadata reference. A losing writer rebuilds against current state, checks operation assumptions, and reuses unaffected work. Compaction must fail if either replaced input file has disappeared.
- Prospected every named local destination: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. Storage, shared-state correctness, and retry admission give plausible triggers across these destinations. Excluded `work` and `instructions`; no search there. Did not expand into the separately owned agentic-system-analyses collection.
- Source-to-notes labels considered: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, `see-also`. Source-to-reference only permits `see-also`; source-to-system reviews permits `compares-with` or `see-also` (and `is-evidence-for` for legacy memory systems). Source-to-sources permits `compares-with` or `see-also`. Tags are named as a search surface but have no source-to-tags label in the table; no genuine tag-head edge was forced.
- External authorization covers known targets only. Evaluated the original source URL already in the snapshot for `derived-from`. Skipped open-web prospecting. No semantic search, MCP, or external browsing was used.

### Curated heads and title surface

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/tags/README.md`, and `kb/sources/README.md` fully.
- Generated each destination's complete title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered the truncated combined output in read ranges. Titles surfaced edge ownership, canonical files, freshness, coordination guarantees, Tracecraft, Origin, beads_rust, and tool-effect verification.
- Read the architecture and review-system tag heads selected through the tags landing. Architecture's storage group routes to the edge-ownership and canonical-files notes. Review-system routes to freshness and review finalization, but its subject is semantic review, not table consistency.
- The snapshot has no `tags:`. No source-tag searches applied. The loaded review-system head has `complete: true`; no by-tag `rg` was run for it. Its relevant routes were already available through the head and reference landing.

### Description and body queries, per destination

For each of the six destinations, ran:

1. `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'concurr|atomic|transaction|snapshot|consisten|retry|retries|storage|coordination|provenance|invalidation|derived|freshness'`
2. `rg -l -i 'optimistic concurrency|atomic (swap|commit|replace)|compare.and.swap|retry validation|serializable|iceberg' kb/<destination>/ --glob '*.md'`
3. `rg -l -i 'stale (state|write|input)|concurrent (write|edit)|conflict.*retr|retr.*conflict|consistent snapshot' kb/<destination>/ --glob '*.md'`

These were deterministic lexical searches; no similarity scores were available.

- **Notes:** Descriptions and query 2 selected the edge-ownership note; descriptions also selected canonical files and coordination guarantees. Read all three fully and kept their mechanism-specific comparisons. Query 3 selected the Popperian-practices note; full reading showed a criticism/interpretation argument rather than a storage retry mechanism, so rejected it. A title containing “atomic step” refers to checkable inference grain, not transactional atomicity, and was not promoted from its description.
- **Reference:** Descriptions selected freshness architecture, review architecture, and ADR 035. Read all fully. Kept freshness as the nearest current Commonplace companion for revision-guarded acceptance. ADR 035 and review architecture provide useful atomic-finalization context but do not need separate outbound links in addition to freshness. Query 2 also surfaced ADR 052, already identified as the freshness architecture's store decision; did not treat its keyword hit as another independent connection.
- **Agent-memory systems:** Descriptions selected Tracecraft's bucket claims; query 2 also selected Origin's page CAS. Read both fully. Kept Tracecraft's concrete conditional-create/backend distinction; Origin has a plausible but narrower version-guard comparison, retained as rejected in favor of the clearer Tracecraft and freshness routes. The landing and collection contract establish that this corpus is frozen; its reviews remain historical comparisons, not candidates for reciprocal edits.
- **Agentic systems:** Descriptions selected beads_rust's transactional claim and workflow gates. Read it fully and kept a comparison of predicate checking inside the accepted mutation boundary. Body queries surfaced Eigenius and numerous archived runtime results, but those were not accepted merely for mentioning atomic operations or stale state. The authored beads_rust account is the clearer reader route for this mechanism; archive hits were not counted as current comparative evidence.
- **Tags:** Descriptions selected architecture, Commonplace architecture, and review-system. Both body queries returned no matches. Read architecture and review-system fully, followed their storage/freshness routes, and retained no direct head connection or membership. Read `kb/tags/COLLECTION.md`: sources do not participate in tag membership, and neither the snapshot nor its future ingest belongs in a tag member listing.
- **Sources:** Descriptions selected Tracecraft, Verified Tool Calls, ToolGate, and the multi-agent memory position paper. Read all fully. Kept the first three for named axes: object-store commit guarantees, effect-aware versus assumption-aware retry, and trusted-state admission versus metadata admission. Kept the position paper as a more cautious comparison of storage consistency with semantic conflict handling. Query 2 selected Tracecraft and an unrelated Prime Agent ingest; the latter's harness topic did not justify a storage connection.

### Link following and reverse pass

- From the edge-ownership note followed canonical-files and freshness links one hop; both were read fully. This cluster separates logical keys, authority decisions, and workload guarantees. Iceberg is relevant to the guarantee comparison, not proof that a workload must choose a database.
- From freshness followed review architecture; from the reference landing also read ADR 035. These explain the all-or-nothing acceptance boundary while freshness preserves the separate baseline-revision guard.
- From the Tracecraft ingest followed the code-grounded Tracecraft review and the multi-agent memory ingest. The later review supplies stronger, backend-specific claim evidence than the earlier ingest. The position paper leaves consistency mechanisms unspecified and adds a semantic-conflict boundary absent from Iceberg's file-membership example.
- From beads_rust followed its interpretation/enforcement note one hop and read it fully. Rejected transferring that reflective-change claim to Iceberg: atomicity repairs alone do not establish a change of responsibility between interpreted and enforced rules.
- Read `kb/notes/COLLECTION.md` for reverse edges, plus the two system collection contracts. Notes can use `evidenced-by` to qualify or bound a claim through a tracked ingest; illustrative official documentation is not a refutation experiment. Frozen legacy reviews should not be scheduled for return-link edits.
- Verified all 17 evaluated paths retained in the report's candidate/rejection neighborhoods exist. Confirmed the matching Iceberg ingest is absent. No library artifacts, indexes, snapshot bytes, or logs were changed.

## Connections Found

Ordered for ingest drafting; these are candidate links, not a requirement to include every item.

- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — **compares-with**: Iceberg connects to this note because its file-backed snapshots achieve coordinated changes through a distinct atomic metadata-reference operation. Compare concrete commit machinery and stale-work rejection, rather than treating files or database rows as guarantees by themselves. Iceberg supplies no cost crossover or edge-key benchmark.
- [Canonical files may defer a shared schema while database authority remains a separate commitment](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — **compares-with**: Iceberg connects to this note because data files alone do not determine table membership; the accepted metadata reference selects which snapshot governs reads. This helps a KB designer separate payload persistence from authority over the accepted state. It does not show schema deferral or a transfer of Commonplace authority.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **is-evidence-for**: Iceberg connects to this claim because it specifies visibility and conflict-admission mechanisms beyond “shared object storage”: readers use a stable snapshot, and conflicting writers must recheck assumptions before publication. This is a bounded engineering illustration of the channel/guarantee distinction, not empirical corroboration of agent reliability or semantic consistency.
- [Freshness architecture](../../../../reference/freshness-architecture.md) — **see-also**: Iceberg connects to this companion because both admit prepared work through a guarded acceptance boundary. Commonplace guards baseline revision/generation and keeps evidence tied to captured inputs; Iceberg checks current table assumptions when retrying. The comparison prevents conflating baseline concurrency protection with live-file currency or automatic rebasing.
- [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md) — **compares-with**: Iceberg connects to this historical review because both use bucket-backed files with an operation-specific atomic primitive. Tracecraft's S3 conditional-create claim differs from its HuggingFace check-then-write fallback; Iceberg's table-state guarantees depend on atomic metadata-reference replacement. Compare guarantees and their backend preconditions, not the shared bucket label.
- [beads_rust](../../../../agentic-systems/reviews/beads-rust.md) — **compares-with**: Iceberg connects to this account because an assumption and its mutation must share a protected commit boundary. beads_rust's CLI checks the unassigned predicate inside the transaction; its generic MCP route lacks that claim operation. This gives the agent reader a concrete route-parity test for implementing assumption-checked mutations. Local SQL claims do not establish distributed table guarantees.
- [Ingest: tracecraft](../../../../sources/arrmlet-tracecraft.ingest.md) — **compares-with**: Iceberg connects to this ingest because it is a counterpoint to treating raw object puts and naming conventions as sufficient coordination. Its complete membership snapshots and atomic metadata commits identify the extra layer that a proposed file-backed KB coordination design would need. Use the later code-grounded review above to qualify this ingest's unverified claim-race discussion.
- [Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) — **compares-with**: Iceberg connects to this paper analysis because both condition retry on state rather than interpreting failure as permission to repeat. Iceberg's example is a known competing commit with revalidated file-membership assumptions; the paper handles ambiguous external effects using verification and idempotency. These are different failure classes and cannot share a retry rule without that distinction.
- [ToolGate: Contract-Grounded and Verified Tool Execution for LLMs](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) — **compares-with**: Iceberg connects to ToolGate because both separate preparing or executing work from installing accepted state. Compare predicates at admission: current file membership before compaction commit versus typed/result checks before trusted-state absorption. Neither comparison establishes rollback of arbitrary external tool effects.
- [Multi-Agent Memory from a Computer Architecture Perspective](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) — **compares-with**: Iceberg connects to this position paper because it provides a concrete snapshot/commit protocol where the paper largely names a consistency need. The paper's heterogeneous semantic conflicts delimit transfer: serializing table membership does not decide which conflicting agent assertion is true.
- [Apache Iceberg reliability](https://iceberg.apache.org/docs/latest/reliability/) — **derived-from**: The future ingest analysis is worked out from this already captured official source. Use the existing observation identity; the moving `latest` URL is not a version pin.

## Bidirectional Candidates

None. Useful note-to-ingest return paths are listed in the reverse section. No reciprocal edit is proposed to the frozen legacy review corpus.

## Reverse-edge Candidates

Both are conditional on creation of the tracked Iceberg ingest. The links below locate the existing author-side artifacts, not a durable snapshot citation.

- [Edge ownership selects the key; choosing files or a database requires a workload comparison](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) → future Iceberg ingest — **evidenced-by** under `kb/notes/COLLECTION.md`: qualifies the substrate comparison with an official documented file-backed construction whose atomic publication requires additional metadata machinery. State exactly what existence claim the example supports; do not present it as a benchmark or a universal file-store result.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) → future Iceberg ingest — **evidenced-by** under `kb/notes/COLLECTION.md`: bounds the shared-memory inconsistency discussion with a specific structural remedy for file-membership state. It is an illustration, not a test of semantic reconciliation or liability governance. Author as a body-supported source use, not an evidence-only footer.

## Off-authorisation Candidates

None. No tag-head edge passed the concrete-reader-benefit test strongly enough to justify extending the source label table. No `exemplifies`, `contrasts`, or `mechanism` label was substituted into the source's authorized set.

## Raw Text Candidates

None. The relevant evaluated connection targets have frontmatter. Curated README files were navigation inputs, not raw-text connection targets.

## Rejected Candidates

- [Origin](../../../../agent-memory-systems/reviews/origin.md) — page version/CAS and stale-source handling could support a narrow comparison, but the report already offers clearer assumption-at-commit routes through freshness, beads_rust, and Tracecraft. No evidence here shows that Origin has Iceberg-style snapshot publication or equivalent retry validation.
- [Review system architecture](../../../../reference/review-architecture.md) and [ADR 035](../../../../reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — genuine atomic-finalization context, but redundant outbound companions once freshness is selected. They remain one-hop routes from it; do not imply identical failure recovery or file/DB transaction semantics.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — checking compaction assumptions is not criticism of a knowledge claim or capture of a rejected interpretation. A stale-state search hit does not establish shared mechanism.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) — Iceberg documents formal correctness machinery, not reflective governance of a transfer between natural-language rules and symbolic enforcement. The note itself distinguishes same-form atomicity repairs from boundary movement.
- [Architecture](../../../../tags/architecture-README.md) and [Review-system](../../../../tags/review-system-README.md) — helpful discovery routes, not useful direct source edges. Sources are outside participating tag collections; storage snapshot consistency alone also fails review-system's semantic-review inclusion condition.

## Index Membership

None. Iceberg is not an external agent runtime or agent-memory system, so do not add it to system rosters. Sources do not participate in the tag membership scheme. A future theory note could earn architecture placement through its KB-specific mechanism, but no such note exists in this task.

## Synthesis Opportunities

None. The discovered notes already separate storage substrate, accepted authority, and coordination guarantees. Iceberg adds a bounded implementation comparison, not a demonstrated new higher-order KB claim.

## Maintenance Observations

- The Tracecraft account has an evidence-boundary tension across retained artifacts. The earlier [ingest](../../../../sources/arrmlet-tracecraft.ingest.md) alternates between asserting optimistic claim isolation and warning that claiming appears non-atomic. The later [code-grounded review](../../../../agent-memory-systems/reviews/tracecraft.md) distinguishes S3 `IfNoneMatch` from a HuggingFace check-then-write fallback. The [coordination-guarantees note](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) still describes non-atomic claiming without that backend qualifier. A later explicitly authorized reconciliation should preserve dates and backend scope rather than flatten these observations into one timeless claim. This connect run makes no repair and proposes no new mutation to frozen reviews.

## Flags

- Drafting priority is the atomic publication boundary and assumption-checked retry. Performance and distributed-planning assertions are background unless a future ingest supplies a concrete KB reader need.
- This is official documentation, not independently inspected implementation or reproduced outcome evidence. Do not report measured agent reliability or universal storage guarantees from it.
- Snapshot reads, atomic publication, and semantic correctness are separate. Stable table membership does not establish truth of agent-authored knowledge.
- The snapshot says retries rebuild against current state only when assumptions still hold; do not reduce this to blind retry, universal idempotency, or reuse of every intermediate result.
- The original URL uses `latest`; retain the existing capture and exact checksum when the ingest is drafted rather than silently refreshing the observation.
- The absent ingest is an expected prerequisite of this pre-drafting discovery, not a broken-link repair target. No durable edge may point into `.snapshots/`.
