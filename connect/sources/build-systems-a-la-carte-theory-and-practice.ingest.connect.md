---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Ingest: Build systems à la carte: Theory and practice

**Source:** [Ingest: Build systems à la carte: Theory and practice](../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md)

The ingest already authors eight connections (five notes, the conference ingest, the Eigenius review, freshness architecture). All eight paths resolve. This report adds candidates beyond those, chiefly a strong reverse edge from the live workflow proposal that the ingest's occasion describes.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section. Destinations prospected: notes, reference, agent-memory-systems, agentic-systems, sources, tags. Excluded: `kb/work/`, `kb/instructions/`. `external` authorised for `derived-from` / `see-also`; external prospecting skipped (no external target in hand beyond the paper's own URL, already in `source:`). Sources -> reference permits only `see-also`.

**Tags:** the ingest carries no `tags:`; no tag heads read. `kb/tags/` listing scanned; no head whose inclusion condition is build-system freshness specifically.

**Titles listing (all destinations):**
- `rg -N --no-heading -m1 '^# ' kb/notes kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'`, filtered on title text for `derived|recompute|fresh|stale|cache|memo|hash|replay|determin|incremental|build|invalidat|dependenc|lineage|provenance|workflow|dagster|airflow|bazel|validator|recheck|verdict|checked|rerun`. Flagged: Dagster ingest, Airflow ingest, in-toto ingest, conference ingest, execution-indeterminism note, underspecification-and-indeterminism note, stale-self-description note, keep-compiled-views-aligned, lineage note, factored-dependency-pairs proposal, generalized-validation-invalidation proposal, validate-workflow-executions-against-fixed-set-snapshots proposal, workflow-recovery-history, code-scheduled-workflows, replaceable-workflow-orchestrators, collection-as-artifact-freshness, Claude Code dynamic workflows review.
- Descriptions of all flagged items read via `rg -m1 '^description:'`.

**Body search:**
- `rg -l -i 'build system|staleness|stale|memo key|cache key|early cutoff|verifying trace|untracked|non-determinis|incremental|invalidat|fingerprint|content hash|replay'` over notes/reference/agentic-systems/agent-memory-systems/sources/tags -- ~120 files; too broad, used only to confirm cluster membership.
- `rg -n -i 'replay|from the top|acceptance (check|validator)|input hash|output hash' kb/reference kb/notes` -- decisive hits: `validate-workflow-executions-against-fixed-set-snapshots.md` (engine replays from the beginning and checks input identity, output digest and current validator result per accepted job — this is the ingest's occasion), `code-scheduled-workflows.md` ("Acceptance is memoization", replay from the top), `replaceable-workflow-orchestrators.md` (engine runs definition from the top).
- `rg -n -i 'untracked|undeclared (read|input|depend)|read set' kb` -- only operational/git-sense hits; no KB artifact names the untracked-dependency mechanism.
- `rg -n -i 'verifying trace|early cutoff|shake|frankenbuild|constructive trace|mokhov|memoi[sz]' kb` -- hits only in Dagster ingest, CocoIndex review, Eigenius review, code-scheduled-workflows; the paper's vocabulary is otherwise absent.
- `rg -l 'build-systems-a-la-carte' kb` -- inbound links today: first-principles note, criteria-edits note, Dagster ingest, in-toto ingest, conference ingest, plus `kb/work/` files (excluded). No link to the theory-and-practice version exists yet.
- `rg -n -i 'distribution|oracle|set of|acceptable'` in underspecification note -- line 32 "you can't assert equality — you test the distribution".
- `rg -n -i 'cach|recompute|reproduc|equal|test'` in execution-indeterminism note -- no hits; rejected.

**Link following:**
- Fixed-snapshot proposal -> its "External design basis" cites Airflow and Iceberg ingests only; its alternatives table includes "Trust historical acceptance without revalidation", which is the paper's verifying-trace option once validator reads are tracked.
- Dagster ingest Connections -> already frames itself as a deployed instance of the conference paper and links CocoIndex; confirms the source-to-source compares-with axis.
- Conference ingest Connections -> named `factored-dependency-pairs-for-review-freshness` and ADR 032 as verifying-trace rebuilders; `distilled-artifacts-need-source-tracking` no longer exists (renamed to the lineage note).
- Stale-self-description note -> "trigger has no edit event to hook" section, compared with §8.3 volatility and §8.8 self-tracking.

## Connections Found

- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../notes/underspecification-and-indeterminism-complicate-programming-for.md) -- **is-evidence-for**: §8.3 replaces exact-equality correctness with membership in the set of possible results for non-deterministic tasks, an independent build-systems instance of the note's "you can't assert equality — you test the distribution"; §8.4's Frankenbuild shows what goes wrong when the equality assumption is kept.
- [Source changes should surface downstream review targets](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -- **is-evidence-for**: §7.4 reports that missing dependencies and undeclared outputs caused most of GHC's cloud-migration failures, which is field evidence that an absent dependency record yields stale reuse; the Dagster ingest already links this note, but this paper supplies the failure-frequency evidence.
- [Stale self-description conceals its own staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md) -- **is-evidence-for**: the note's "trigger has no edit event to hook" claim has a build-systems counterpart in §8.3 (untracked and volatile dependencies change without an edit to a declared input) and §8.8 (systems must track their own rule scripts or pessimistically assume any script change affects every task); the paper's responses (track, mark volatile, leave untracked) bound the note's synchronization-path options.
- [Dagster asset versioning and caching](../../../../sources/dagster-asset-versioning-and-caching.ingest.md) -- **compares-with**: on handling non-deterministic outputs in a verifying-trace rebuilder; Dagster's user-supplied data versions are a deployed alternative to §8.3's set-membership weakening, and both put code version into the key (§7.3 `Ver` arguments vs `code_version`).
- [Validate workflow executions against fixed set snapshots](../../../../reference/proposals/validate-workflow-executions-against-fixed-set-snapshots.md) -- **see-also**: this is the live design for the ingest's occasion (replay-from-top engine, per-job input identity and output digest, validator rerun on replay reading current sibling files); the ingest's Recommended Next Action should point here instead of proposing a new design note.
- [Code-scheduled workflows](../../../../reference/proposals/code-scheduled-workflows.md) -- **see-also**: its "Acceptance is memoization" model is the restarting-scheduler × verifying-trace cell the ingest classifies; reader of the classification needs the system it describes.

## Bidirectional Candidates

- [Dagster asset versioning and caching](../../../../sources/dagster-asset-versioning-and-caching.ingest.md) <-> source -- **compares-with**: the Dagster ingest currently links only the 2018 conference ingest; its non-determinism and code-version points answer the limits this extended version adds (§7.3, §8.3), so the return edge helps a Dagster reader too.

## Reverse-edge Candidates

- [Validate workflow executions against fixed set snapshots](../../../../reference/proposals/validate-workflow-executions-against-fixed-set-snapshots.md) → source -- **evidenced-by** (reference COLLECTION.md): the proposal's "External design basis" cites only Airflow and Iceberg. This paper diagnoses its replay blocker: the acceptance validator reads current sibling members the job did not declare as inputs, an untracked dependency in the §8.3 sense, and its "Trust historical acceptance without revalidation" alternative becomes correct under §3.6 only if the validator's reads and version are recorded in the trace (§3.7 `track`, §7.3, §8.8). Strongest candidate in this report; the ingest's occasion question was evidently asked for this proposal.
- [Code-scheduled workflows](../../../../reference/proposals/code-scheduled-workflows.md) → source -- **evidenced-by**: "Acceptance is memoization" and the replay-discipline forces (deterministic definition, stable job identity) are the paper's restarting scheduler and verifying-trace rebuilder; §9.1 Fabricate is the nearest named prior system and §4.2 states the minimality cost of replay.
- [Factored dependency pairs for review freshness](../../../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) → source -- **evidenced-by**: hash-keyed `(document, gate)` re-checking is a verifying-trace rebuilder; §7.3/§8.8 add that gate-version (rule identity) must sit in the key. Weaker than the two above; the conference ingest may suffice if the proposal only needs the grid.
- [Underspecification and indeterminism complicate programming for prompts](../../../../notes/underspecification-and-indeterminism-complicate-programming-for.md) → source -- **evidenced-by** (notes COLLECTION.md): mirror of the outbound candidate, if the note's authors want an external non-LLM instance of equality giving way to set membership. Per the notes "Origin is not corroboration" rule, the context phrase should say this qualifies or bounds the claim, not that it corroborates it, because the paper did not test the note's claim.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md) -- memoizes components on code and input fingerprints (a constructive-trace engine in the paper's terms); `compares-with` is authorised, but the Dagster ingest already carries this comparison and `kb/agent-memory-systems/` is historical and frozen per AGENTS.md.
- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- topical (non-determinism) but the note makes no claim about caching, equality checks or recomputation; the underspecification note carries the bearing claim.
- [Apache Airflow best practices](../../../../sources/apache-airflow-best-practices.ingest.md) -- shares the rerun-same-outcome concern, but the comparison axis is already carried by the fixed-snapshot proposal that cites both; a direct source-to-source edge adds little.
- [Apache Iceberg reliability](../../../../sources/apache-iceberg-reliability.ingest.md) -- snapshot isolation is a storage mechanism, not a rebuilder; no shared axis beyond the proposal that cites it.
- [In-toto farm-to-table guarantees](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) -- already links the conference ingest on supply-chain verification; the extended version adds nothing to that axis.
- [Generalized validation invalidation](../../../../reference/proposals/generalized-validation-invalidation-and-imperative-extension.md) -- change-driven target selection is the scheduler side; the conference ingest's grid suffices; the extended version's §8 adds nothing specific.
- [Replaceable workflow orchestrators](../../../../reference/proposals/replaceable-workflow-orchestrators.md) -- mentions replay from the top, but its subject is orchestrator portability, not recheck correctness.
- [Adopt the declared layout in the analysis workflow](../../../../reference/proposals/adopt-declared-layout-in-the-analysis-workflow.md) -- its replay blocker is delegated to the fixed-snapshot proposal; link there instead.
- Collection-as-artifact freshness, workflow recovery history, Claude Code dynamic workflows review, keep-compiled-views-aligned -- keyword matches (freshness, workflow, drift) without a mechanism the paper's new material bears on.

## Index Membership

None — the ingest has no tags and no tag head has a build-system or freshness inclusion condition that this source substantively meets beyond what the linked notes already carry.

## Synthesis Opportunities

The fixed-snapshot proposal, code-scheduled-workflows, and the criteria-edits note together imply a claim the KB does not state: an acceptance validator is part of the producing task, so its read set and its version belong in the accepted job's trace key, and any validator that reads current files outside that key makes replay unstable or incorrect. The conference ingest flagged the broader latent synthesis ("the KB's freshness machinery is a build system"); this narrower claim is the one the current workflow work needs.

## Maintenance Observations

- The ingest's Recommended Next Action asks for a new design note in `kb/reference/proposals/`; [Validate workflow executions against fixed set snapshots](../../../../reference/proposals/validate-workflow-executions-against-fixed-set-snapshots.md) (dated 2026-10-07) already owns that problem. Writing a second proposal would create competing ownership.
- The conference ingest still names `distilled-artifacts-need-source-tracking`, which no longer exists (the claim now lives in `artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`). It is prose, not a link, so validation will not catch it.
- The ingest's own note that the first-principles note's "remained a blueprint" wording is overtaken by §7 is a pending revision signal for that note.

## Flags

- No split candidate: the ingest makes one occasion-driven assertion plus KB-wide evidence links.
- Tension worth keeping visible: the ingest's Extractable Value item 2 (track the validator's reads) and the fixed-snapshot proposal's preferred option (fixed execution snapshots) are two routes to the same correctness condition. The proposal's "reconstruct each execution's context" row is closest to the paper's `track`; the choice between them is not resolved here.
