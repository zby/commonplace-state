---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/dagster-asset-versioning-and-caching.ingest.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Ingest: Dagster asset versioning and caching

**Source:** [Ingest: Dagster asset versioning and caching](../../../../sources/dagster-asset-versioning-and-caching.ingest.md)

The ingest already links: the external guide (derived-from), Build Systems à la Carte (conference ingest), the criteria-edits note, the derived-copy note, the source-lineage note, the link-graph staleness note, the LLM recompute-cost note and CocoIndex. These are not re-proposed below.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: notes, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. The label table names no tag destination, so no tag edges can be labelled. `external` is authorised (derived-from, see-also); external prospecting is skipped because no further external target is in context.

**Description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md' | rg -i 'stale|fresh|verdict|cache|recompute|version|invalidat|lineage|derived|provenance|determinis|supersed|replace'` -- flagged: execution-indeterminism, history-has-one-chance (via the nondeterminism query), keep-compiled-views-aligned, git-provenance, superseded-choices, parametric-reproduction, deterministic-validation, opposed-recompute-factors. Evaluated below.
- `rg '^description:'` on the reference freshness cluster (freshness-architecture, review-architecture, generalized-validation-invalidation proposal, collection-as-artifact-freshness proposal) -- freshness-architecture and review-architecture kept for evaluation.

**Topic indexes:**
- `kb/tags/` listing: no `derived-artifact-freshness`, `staleness-detection`, `workflow-orchestration` or `provenance` tag heads exist (the ingest's `domains` values are not tags). `kb-maintenance-README.md` and `links-README.md` matched "stale" but the sources contract authorises no label into tags.

**Body search:**
- `rg -il 'staleness|stale|fingerprint|memoiz|early cutoff|content hash|data version|freshness'` over notes, reference, agent-memory-systems, agentic-systems, sources, tags -- broad recall (100+ files); narrowed with the queries below.
- `rg -il 'dagster|bazel|nix\b|salsa|incremental computation|early cutoff|verifying trace|build system'` (excluding work/reports/snapshots) -- found `build-systems-a-la-carte-theory-and-practice.ingest.md` (extended JFP version, not yet linked), `in-toto-farm-to-table-guarantees.ingest.md`, `the-boundary-of-automation-is-the-boundary-of-verification.md`.
- `rg -l -i 'content hash|content_hash|sha256 of|fingerprint'` -- mostly retained analysis results and memory-system reviews using content hashes for ingestion dedup; only cocoindex (already linked) and the criteria-edits note (already linked) were on-topic.
- `rg -l -i 'nondetermin|non-determin' kb/notes` -- execution-indeterminism, history-has-one-chance, llm-output-deviation, any-symbolic-program. Kept execution-indeterminism and history-has-one-chance.
- `rg -l -i 'memoiz|dagster|airflow|workflow engine'` over agentic-systems and agent-memory-systems reviews -- eigenius (memoization key omits component-definition version), agno-agentos (no relevant hit), cocoindex (already linked).
- `rg -l -i 'member-mode|member mode|supersed.*member|verif.*member'` over reference proposals, ADRs and analysis types -- found `validate-workflow-executions-against-fixed-set-snapshots.md`, which is the occasion's workflow design.
- `rg -n -i 'one hop|transitiv|non-transitive|cascade'` in the link-graph and source-lineage notes -- no hits, confirming the ingest's claim that no KB note discusses non-transitive flagging.

**Link following:**
- `validate-workflow-executions-against-fixed-set-snapshots.md` "External design basis" cites `apache-airflow-best-practices.ingest.md` and `apache-iceberg-reliability.ingest.md`, ingested the same day for the same design question. Both evaluated as sibling sources.
- `build-systems-a-la-carte-theory-and-practice.ingest.md` Connections Found links the same five freshness notes as this ingest, and its §8.3/§8.4 material covers non-determinism.
- `review-architecture.md` "Freshness hash boundary" and `freshness-architecture.md` "Target and input boundary" -- Commonplace's review baseline pins exact accepted versions of note and criterion, and puts prompt scaffolding deliberately outside the hash.
- Notes `COLLECTION.md` label table checked for reverse edges: notes may author `evidenced-by` into sources. Reference `COLLECTION.md` checked: reference may author `evidenced-by` into sources.

## Connections Found

- [Build systems à la carte: Theory and practice](./../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) -- **compares-with**: on handling non-deterministic tasks in a verifying-trace rebuilder; that paper's §8.3/§8.4 replaces exact equality with membership in possible results and shows deep traces breaking under non-determinism, which bounds the ingest's departure verdict more sharply than the conference ingest it currently links. Its §7.3 rule/script versions in Cloud Shake's keys also parallel Dagster's `code_version`.
- [Apache Airflow best practices](./../../../../sources/apache-airflow-best-practices.ingest.md) -- **compares-with**: on fixing task inputs for reruns; Airflow pins a partition and asks for identical rerun outcomes, while Dagster records which upstream data version each materialization consumed. Both were ingested for the same set-workflow design question, so a reader of one needs the other.
- [Apache Iceberg reliability](./../../../../sources/apache-iceberg-reliability.ingest.md) -- **compares-with**: on version identity for retained state; Iceberg gives snapshot-level identity with atomic reference swaps, Dagster gives per-asset data versions with one-hop staleness. Together they bracket the set-snapshot versus per-member-stamp choice in the occasion.
- [Eigenius](./../../../../agentic-systems/reviews/eigenius.md) -- **compares-with**: on memoization cache-key composition; Eigenius's key omits the component-definition version, which is the same hazard as a forgotten Dagster `code_version` bump (Extractable Value item 5), seen in a deployed agentic kernel.
- [History has one chance to become checkable](./../../../../notes/history-has-one-chance-to-become-checkable.md) -- **is-evidence-for**: Dagster's per-materialization record of consumed upstream data versions is a production-time record that makes later staleness checks possible; the ingest's Limitation that retention of that record is left implicit is the note's failure condition.
- [Execution indeterminism is a property of the sampling process](./../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- **rests-on**: the departure verdict (Extractable Value item 1) depends on model-written members not reproducing from equal code and inputs, which is this note's claim.

## Bidirectional Candidates

- [Build systems à la carte: Theory and practice](./../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) <-> source -- **compares-with**: the return link gives that ingest a deployed, documented verifying-trace system with user-supplied output fingerprints, the concrete case its non-determinism discussion lacks.
- [Apache Airflow best practices](./../../../../sources/apache-airflow-best-practices.ingest.md) <-> source -- **compares-with**: the three same-occasion ingests (Airflow, Iceberg, Dagster) are each partial; the return path lets a reader of the Airflow ingest find per-input version stamping.

## Reverse-edge Candidates

- [Validate workflow executions against fixed set snapshots](./../../../../reference/proposals/validate-workflow-executions-against-fixed-set-snapshots.md) → source -- **evidenced-by** (reference → sources): this is the occasion's design. Its "External design basis" cites Airflow and Iceberg but not Dagster, and its open point that "the implementation must establish which inputs are relevant rather than assume that a matching target digest is sufficient" is exactly what Dagster's per-input consumed-version stamp and Extractable Value item 2 address.
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](./../../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) → source -- **evidenced-by** (notes → sources): an independently designed cache key that separates consumer code version from upstream output fingerprints; it already cites the conference build-systems ingest.
- [Link graph plus timestamps enables make-like staleness detection](./../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) → source -- **evidenced-by** (notes → sources): qualifies the note with version keys instead of timestamps and introduces non-transitive flagging, which the note does not discuss.
- [Review architecture](./../../../../reference/review-architecture.md) → source -- **evidenced-by** (reference → sources): weak; the "Freshness hash boundary" keeps prompt scaffolding outside the hash and treats scaffolding changes as deliberate re-review, the same trade-off Dagster makes with a hand-declared `code_version`. Reference outbound to sources is marked uncommon, so author only if the boundary is revisited.

## Off-authorisation Candidates

- [Freshness architecture](./../../../../reference/freshness-architecture.md) -- connects because Commonplace's review-pair target already implements the ingest's kernel (exact accepted versions per role-labelled input, staleness on mismatch); a reader evaluating Extractable Value item 2 should know the substrate exists. The relation is a comparison on a design axis, but sources → reference authorises only `see-also`. Suggest extending `compares-with` to `reference` destinations in `kb/sources/COLLECTION.md`, or carry the edge as the reverse `evidenced-by` above.

## Raw Text Candidates

None

## Rejected Candidates

- [In-toto farm-to-table guarantees](./../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) -- whole-chain cryptographic attestation; shares "lineage" vocabulary but not the staleness/cache-key axis.
- [The boundary of automation is the boundary of verification](./../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- build-system hit is incidental; the note is about verification cost, not invalidation.
- [Lineage](./../../../../notes/definitions/lineage.md) -- the ingest uses "lineage" only in passing; a defined-in link adds little.
- [Keep lineage and compiled views from drifting](./../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) -- concerns behaviour-shaping generated views, not verdict staleness.
- [Git-backed provenance depends on explicit contribution and dependency semantics](./../../../../notes/git-provenance-requires-contribution-and-dependency-semantics.md) -- adjacent on dependency records, but the ingest makes no claim about Git storage.
- [Superseded choices need a historical witness](./../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) -- the occasion's "replaced verdict becomes historical" is closer to the fixed-set-snapshots proposal than to this note's retention question.
- `kb/reference/proposals/generalized-validation-invalidation-and-imperative-extension.md` and `collection-as-artifact-freshness.md` -- change-driven validation targeting; Dagster's mechanism is per-asset, not validation-target selection. Only see-also would be authorised and the link would not change a reader's action.
- `kb/agentic-systems/reviews/agno-agentos.md` -- keyword hit only.

## Index Membership

None. No tag head matches the ingest's domains, and sources → tags has no authorised label.

## Synthesis Opportunities

The Dagster, Airflow, Iceberg and Build-Systems (JFP) ingests, together with the criteria-edits note and the freshness architecture, jointly imply a claim not yet written: for model-written members, staleness must be keyed on output fingerprints recorded per consumer, because input-derived versions (Dagster default, Build Systems verifying traces) assume determinism that model calls lack. The fixed-set-snapshots proposal is currently the only place drawing on these, and it does not cite Dagster or the JFP ingest.

## Maintenance Observations

- Non-transitive (one-hop) staleness flagging is a design choice with no KB note; both this ingest and the link-graph note's silence on transitivity point to it as a gap.
- The ingest's `domains` values (`derived-artifact-freshness`, `staleness-detection`, `provenance`) have no tag heads; the freshness cluster (five notes, three source ingests, two reference docs) is navigable only via links.
- Sources → reference allows only `see-also`, which blocks comparison edges from ingests to Commonplace's own implemented mechanisms (see Off-authorisation).

## Flags

- Tension: the ingest positions Dagster's kernel as something to "specify" for the occasion, while `freshness-architecture.md` describes an implemented review-pair store with the same shape. A future editor should check whether the Recommended Next Action is partly already met by the existing freshness substrate.
