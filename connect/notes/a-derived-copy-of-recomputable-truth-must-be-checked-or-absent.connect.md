---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: A derived copy of recomputable truth must be checked or absent

**Source:** [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)

The source is already densely linked (14 outbound edges in its footer/inline: `stale-indexes`, `boundary-of-automation`, `frontloading`, `fix-what-executor`, `keep-compiled-views-aligned`, `distilled-artifacts-need-source-tracking`, `link-graph-plus-timestamps`, `text-testing-framework`, `evolving-understanding`, `llm-recompute-cost`, `tag-readme` type, ADR 025, ADR 027, `lineage` def). The high-value discovery here is therefore **return links**: four notes link *to* the source with no reciprocal edge from it, and two of those are load-bearing.

## Discovery Trace

**Description listing scan:**
- Scoped `rg` listing over `kb/notes/` by tag `context-engineering` (35 notes) and `kb-maintenance` (19 notes). Neither `context-engineering-README.md` nor `kb-maintenance-README.md` carries a `complete: true` mark, so the by-tag rg sweeps were run in full (not skippable).
- Flagged from the sweep: `history-has-one-chance-to-become-checkable` (re-derivability / checkable-at-production), `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract` (the tag-README mark instance theorized), `criteria-edits-invalidate-verdicts` (cache-key/verdict staleness), `index-curation-adds-orientation`, `semantic-review-catches-content-errors`.

**Topic indexes:**
- `kb/notes/kb-maintenance-README.md` — Detection group lists the source itself alongside `stale-indexes`, `link-graph-plus-timestamps`, `semantic-review`, `apparent-success`. All either already linked or evaluated below.
- `kb/notes/context-engineering-README.md` — Core Claims (memory-system / scheduling notes) carry no unlinked recomputable-copy candidate; no new hit.

**Inbound-link scan (`rg -l` for the source filename):**
- Notes linking *to* the source with no return edge: `history-has-one-chance-to-become-checkable` (extends), `an-enforced-tag-readme-...` (grounds), `prose-has-no-dereference-...` (exemplifies), `many-to-many-edge-state-...` (see-also ×2).
- Already bidirectional: `llm-recompute-cost-inverts-...`, `distilled-artifacts-need-source-tracking`.
- Inbound from other collections (already authored under their own rules — not connect's to touch): `reference/adr/038-type-conformance-reviews`, `reference/proposals/factored-dependency-pairs-for-review-freshness`, `types/tag-readme.md`, `types/type-spec.md`, `sources/prov-overview.ingest.md`.

**Body search:**
- `rg -n "verifiability|verdict|cache" kb/notes/` → `verifiability-gradient`, `criteria-edits-invalidate-verdicts` (evaluated below).
- Read of `verifiability-gradient.md`, `criteria-edits-invalidate-verdicts-...md`, `history-has-one-...md`, `an-enforced-tag-readme-...md`, `prose-has-no-dereference-...md`, `many-to-many-edge-state-...md`.

**Link following:**
- From `history-has-one-chance` → `verifiability-gradient` (it links there as `contrasts`); confirmed `verifiability-gradient` is one hop out and overlaps the source's already-linked verification cluster (see Rejected).
- From `criteria-edits-invalidate-verdicts` → it grounds in `history-has-one-chance` and extends `link-graph-plus-timestamps` (which the source already links), placing it as a sibling in the same staleness cluster.

## Connections Found

- [criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts](../../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — **contrasts**: both model a derived artifact as a cache keyed on a source and prescribe recompute-or-omit when the source moves, but they partition into neighbouring regimes — the source's *recomputable copy* (cheap deterministic re-derivation, so enforce-or-omit) versus the *verdict cache* (re-judgment on a criteria change, an expensive Level-B judgment). The contrast sharpens the source's own deterministic-vs-judgment axis; a reader wanting the neighbouring-shape distinction gains it. (Moderate confidence — the two notes sit one hop apart via `link-graph-plus-timestamps`, which the source already links; consider whether the transitive path already serves the reader.)

## Bidirectional Candidates

- [history-has-one-chance-to-become-checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) ↔ source — **contrasts**: the target already links in as `extends` ("the recomputable special case"). The reciprocal edge is load-bearing: the source's precondition #1 (a derivation rule) and #3 (ground truth exists at validation time) are exactly the *recomputable* half whose complement is the target's non-recomputable *history* that must be recorded at production time. A reader at the source who wants the boundary of the rule (what happens when the copy is **not** recomputable) should be pointed to the history note. Strongest missing return link.
- [an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) ↔ source — **extends**: the target already links in as `grounds`. The source lists the `complete`/`covered_by` tag-README marks as its instance #1 ("enforced and shipped") but points only at the `tag-readme` type spec for it. The target develops that instance into the MOC-plus-contract argument; a reader wanting the shipped instance's theory developed further gains from the return edge.
- [prose-has-no-dereference-reinforce-facts-at-point-of-use](../../../../notes/local-materialization-should-outperform-distant-declarations.md) ↔ source — **extends**: the target links in as `exemplifies` ("this rule in the prose regime — the banner is a derived copy of `status`, denormalize the copy, normalize the check"). The source's Open Questions explicitly flags the `status:` maturity field as a candidate unenforced trust mark — the prose note is the worked prose-regime case for that open question. A return edge would close that loop. (Modest — the inbound instance→general direction is the natural one; the return edge earns its place mainly via the `status:` open question.)
- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) ↔ source — **see-also**: the target links in twice via `see-also` ("regenerate or validate, never store" as the churn-without-mesh disposition). A reciprocal edge is optional — the relationship is genuinely asymmetric (the storage note *uses* the source's disposition), and `see-also` is the weakest label. Include only if a reader of the enforce-or-omit rule benefits from the storage-substrate consequence; otherwise leave one-directional.

## Reverse-edge Candidates

None with clear evidence. Inbound coverage is already strong: the source is cited from `kb/reference/adr/038`, `kb/reference/proposals/factored-dependency-pairs-for-review-freshness`, `kb/types/tag-readme.md`, `kb/types/type-spec.md`, and `kb/sources/prov-overview.ingest.md`, each under its own collection's rules. No unlinked reference/instruction artifact surfaced during traversal that plainly needs a rationale/evidence edge to this note.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [verifiability-gradient](../../../../notes/verifiability-gradient.md) — the source's core pivot (check price dropping to Level A) genuinely rubs against this note's resettable/efficient/rewardable decomposition and its "placement test". But the source already grounds the check-cost gradient in [text-testing-framework](../../../../notes/text-testing-framework.md) (Level A/B) and the oracle-availability boundary in [the-boundary-of-automation-is-the-boundary-of-verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). A third verification-cost link is redundant for traversal; `history-has-one-chance` already carries the `verifiability-gradient` contrast if a reader wants it.
- [index-curation-adds-orientation-that-generation-cannot-produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) — topically adjacent (generated indexes, completeness, ADR 025 omission) but its claim is about *orientation* value curation adds, not about the enforce-or-omit correctness rule; following the link does not advance the source's argument.
- [semantic-review-catches-content-errors-that-structural-validation-cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) — structural-vs-semantic validation maps onto the source's Level A/B split, but that split is already served by the linked `text-testing-framework`; keyword overlap only.

## Index Membership

- `kb/notes/kb-maintenance-README.md` — already lists the source under **Detection**. No action.
- `kb/notes/context-engineering-README.md` — the source carries the `context-engineering` tag but is not listed in this curated head. A future writer could add it under a maintenance/detection grouping, but the README is selective by design (Core Claims + Adjacent Indexes) — not a clear gap. Noted, not asserted.

## Synthesis Opportunities

None. The candidate cluster (source, `criteria-edits-invalidate-verdicts`, `history-has-one-chance`, `link-graph-plus-timestamps`) already has a shared spine — a derived artifact as a cache keyed on a source, with staleness handled by recompute/omit — but that spine is distributed across notes that cite one another rather than crying out for a new umbrella note.

## Maintenance Observations

- The source's footer uses a `complements` label ([llm-recompute-cost-inverts-...](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — "complements") that is **not** in the `kb/notes/COLLECTION.md` authorised label set (extends, grounds, enables, exemplifies, mechanism, contradicts, contrasts, defined-in, evidence, derived-from, see-also). Either the label should be normalised to an authorised one or the collection's set extended. Best-effort observation for a later validate/triage pass, not a connection candidate.

## Flags

- No split candidate: the source makes one assertion (enforce-or-omit for recomputable copies) developed across surfaces; despite 14+ links it is a single-claim synthesis-style note, not a split target.
- No unresolved tensions among candidates.
