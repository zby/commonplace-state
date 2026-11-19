# Inbound contexts of `kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md`

41 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

Only the first 30 files by path are shown; 11 more were cut.

## `kb/agent-memory-systems/reviews/swamp.md`

- Title: Swamp
- Description: Swamp review: agent-authored automation compiled into validated YAML workflows, with versioned operational data and progressively disclosed skills

> - [A derived copy of recomputable truth must be checked or absent](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) - Matches Swamp's rebuildable catalog and on-disk verification behavior.

## `kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md`

- Title: 038-Type-conformance reviews use the type spec as the gate
- Description: Type-conformance review pairs put the note's type spec on the gate side of the existing (note, gate) freshness key, so a type edit stales exactly its cohort with no new storage semantics

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the choice to use the type spec directly, avoiding restatement drift while reusing the two-input freshness machinery

## `kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md`

- Title: 041-Collection-conformance reviews use COLLECTION.md as the gate
- Description: Collection-conformance pairs put the note's COLLECTION.md on the gate side of the existing (note, gate) freshness key, matching the enforcement type contracts got in ADR 038

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the choice to use COLLECTION.md directly, avoiding restatement drift while reusing the existing freshness machinery

## `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`

- Title: 046-Verbatim quotes are validated against their cited source
- Description: `commonplace-validate` resolves every `verbatim`-marked quotation against the source it links; a false verbatim claim fails, and `unresolved` warns only where the convention is demonstrably in use

> [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) frames the choice to check these claims rather than continue trusting them. For the retained-file case considered here, three mechanical-check conditions hold: the comparison rule is a substring test under the checker’s normalization; the adjacent Markdown link locates the source; and the checked-in source is available at validation time. Location alone does not establish availability. The fourth condition, a sufficiently trustworthy checker, needs separate support. Centralizing the extraction heuristic spreads assurance work across citations but does not prove it correct. The prototype audit below supplies bounded evidence for a deterministic check rather than a judgment-based review gate; no check-cost measurement is recorded here.

## `kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md`

- Title: 056-Adopted and retired proposals archive out of the frontier
- Description: Adopted and retired proposals move to a link-sink archive after extraction; provenance becomes a title tag, so ADRs from 2026-07-25 must carry a Considered alternatives section

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — see-also: frames the drift risk of unvalidated lifecycle state; directory separation was selected here to avoid both that risk and repeated filtering

## `kb/reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md`

- Title: 066-Claims declare modality in text, and passes repair mode mismatch
- Description: Claim modes and their refuters remain active in text and premise review; ADR 080 replaced in-pass mode conversion with author hand-back, and ADR 091 tightened the universal refuter

> - No frontmatter modality field ships. If corpus sweeps later need to enumerate declared ideal-type or statistical claims mechanically, addressability can be added then. This decision requires checking a duplicated field against the claim text or omitting it; that is a local maintenance condition, not a universal prohibition on retained results. [Checking cost and reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) remain relevant when designing that check.

## `kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md`

- Title: 068-Collection contracts stop enumerating available types
- Description: Accepted decision that COLLECTION.md states type eligibility instead of listing types, with kb/work allowed to use any valid type contract

> Nothing in the runtime parsed these tables and nothing enforced their contents. The menu was therefore an unchecked constraint that agents obeyed. [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) frames this trade-off; the observed refusal of legitimate writes is the local reason to stop accepting that risk. It instantiates the failure [indexes lower recall when they suppress retrieval that would find more](../../theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) names.

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the trade-off; observed write refusals and the simpler path invariant support removing this unchecked menu

## `kb/reference/proposals/a-reader-facing-banner-for-user-verification.md`

- Title: A reader-facing banner for user verification
- Description: Proposal: surface committed user verification at the point of reading through a standardized Markdown banner without turning absence into a review or truth verdict

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the proposed consistency check as a choice to spend checking effort against false attestation risk

## `kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md`

- Title: Atomic-step grounding bounds unquoted sources per note
- Description: Proposal: move the grounding reading limit from the review to the note — a note may cite at most N sources a reviewer must open and search, with validated inline quotes and note links exempt

> **ADR 078 is not contradicted.**
> [ADR 078](../../adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md)
> rejected evidence living in the target artifact and kept the ingest `## Quotes`
> pool as the evidence owner. An inline quotation is not a second evidence store:
> it is a checked copy of a quote the ingest already retains, admissible exactly
> because a validator re-derives it and fails on mismatch — the general rule that
> [a derived copy of recomputable truth must be checked or absent](../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md).
> The ingest remains the owner, and the required `## Quotes` tightening above is
> what keeps that true.

## `kb/reference/proposals/archive/source-genre-is-one-open-field-on-the-snapshot.md`

- Title: Source genre is one open-vocabulary field on the snapshot
- Description: Proposal (adopted): record source genre once as an open-vocabulary field on the snapshot, drop the ingest-report enum and genre-carrying tags, and unify two divergent vocabularies

> 2. **The ingest-report drops its `source_type` field.** The report's Classification section keeps its prose justification, and the Limitations Standards lens is selected by reading the paired snapshot's field — the ingest process opens the snapshot anyway. No duplicated field means no unchecked derived copy, per [a derived copy of recomputable truth must be checked or absent](../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md).

> - [A derived copy of recomputable truth must be checked or absent](../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rationale: the single-ground-truth rule behind dropping the report's copy of genre

## `kb/reference/proposals/archive/tag-scope-is-declared-where-membership-claims-are-made.md`

- Title: Tag scope is declared where membership claims are made
- Description: Proposal (adopted): one tag namespace per KB; membership claims range over participating collections; trace-learning stays navigable; canonical filename-derived heads live in kb/tags/

> - [A derived copy of recomputable truth must be checked or absent](../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: scope is a parameter of the derived claim, so it must be part of what the check enforces or the claim must not be made

## `kb/reference/proposals/channel-compiled-instruction-artifacts.md`

- Title: Channel-compiled instruction artifacts
- Description: Proposal: resolve execution channel at install time so an agent reads one literal procedure, extending build-time generation from paths to shell and command form

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: the trade-off the compiled-copy adoption criterion asks the design to resolve

## `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md`

- Title: Checked inline blocks for shared instruction text
- Description: Proposal: reuse natural-language authoring mechanics in specialized writer prompts through literal inlining backed by deterministic source-to-copy checks

> [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) frames the choice between accepting drift, checking copies, and reading the source. This proposal seeks agreement for rules intended to remain identical across writers, so its candidate designs favor checks or live reads over unchecked copies. Whether that extra machinery is worth its cost remains subject to the adoption criteria below.

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the cost of checking shared text against the risk of divergent writer instructions and states the mechanical-check conditions

## `kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md`

- Title: Decisions bind their consumers through site back-pointers
- Description: Proposal: make a recorded decision reach the operations it constrains by having each ADR declare the artifacts it binds and each bound artifact carry a checked back-pointer, rather than a hand-maintained decision index

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the candidate's checked back-pointers as a local cost-risk choice, not the only permissible retained routing surface

## `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md`

- Title: Factored dependency pairs for review freshness
- Description: Proposal: keep review dependencies factored as two-input pairs where that shape fits; type and collection pairs are shipped while a review target with more than two inputs remains

> - [Checking retained results trades cost against reliance risk](../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the choice to use dependency documents directly where pairs fit, avoiding restatement drift without widening the freshness input set

## `kb/reference/validation-contract.md`

- Title: The validation contract
- Description: The base, type-rule, and schema sources of deterministic findings, their dereferencing limits, and the run-scoped execution model

> So the dividing line is not frontmatter/body. It is **inside the supplied schema instance** (declarable) versus **outside that instance** (must be loaded and checked). Directory schemas can compare the member data their loader supplies; they cannot perform filesystem reads themselves. A referential check needs locatable inputs outside the supplied instance and those inputs must be available at check time: distinct conditions 2 and 3 of [checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md). Those conditions make checking possible; they do not make it obligatory. The base contract below selects which checks Commonplace runs and their severities.

> - [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — rests-on: frames the checking-cost and reliance-risk trade-off; the base contract selects checks and severities locally

## `kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md`

- Title: Ingest: Build systems à la carte: Theory and practice
- Description: Extended JFP version of Build Systems à la Carte: classifies replay-from-top workflow engines, and shows why untracked reads, missing self-tracking and non-determinism break exact recheck

> For the KB, the paper is the formal anchor for the derived-artifact freshness cluster, and it adds the limits the conference ingest lacked. It is evidence for [Criteria edits invalidate verdicts; process edits invalidate artifacts](../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md). §8.8 says systems whose tasks are full programs must pessimistically assume that any script change may change any task. §7.3 puts script and rule versions into Cloud Shake's cache keys to avoid stale products. It compares with [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) on what a mechanical check establishes: §3.6 is a formal definition of "checked". The comparison concerns the note's mechanical-check conditions, not the choice of checking frequency. It is also evidence for [LLM recompute cost shifts the store-vs-recompute balance](../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md): §8.3 replaces exact equality with membership in the set of possible results for non-deterministic tasks, and §8.4 shows that deep traces then return results inconsistent with their [cut at 1200 characters]

## `kb/sources/build-systems-a-la-carte.ingest.md`

- Title: Ingest: Build Systems à la Carte
- Description: How the scheduler×rebuilder build-systems framework grounds the KB's derived-artifact freshness machinery (staleness, verifying traces, recompute-vs-store)

> - **[Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md)** — compares with the paper on checking retained results: a verifying trace stores a hash of a derived value and re-checks it against the source, while a content-addressable cache lets you drop and refetch. These are specific checking and recovery mechanisms, not corroboration of a universal requirement to check or discard every derived copy. The note's cost-risk trade-off is our interpretation, not a result established by the paper.

## `kb/sources/dagster-asset-versioning-and-caching.ingest.md`

- Title: Ingest: Dagster asset versioning and caching
- Description: Dagster keys each asset materialization on code and input data versions, flags one-hop Unsynced staleness, and lets output fingerprints stop cascades; a version-pinned verdict model.

> Within the KB, the source is a deployed instance of the build-system framework
> in [Build Systems à la Carte](./build-systems-a-la-carte.ingest.md). In that
> paper's terms Dagster is a verifying-traces rebuilder, and output
> fingerprinting gives it early cutoff. The source partly relaxes two limits
> that ingest records: its user data versions address nondeterministic outputs,
> and it states the computational cost that justifies caching. It bears on
> [Criteria edits invalidate verdicts; process edits invalidate artifacts](../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md):
> if a verification is modelled as a downstream asset, a change to the
> verifier's own code version marks the verdict Unsynced, while a change to the
> producer's code version marks the producer Unsynced and reaches the verdict
> only when the producer's output fingerprint changes. That is the note's key
> boundary realized as a cache design, though Dagster does not frame it as
> criteria versus process. It bears on
> [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md):
> the hand-declared `code_version` is a trusted, u [cut at 1200 characters]

> - [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — is-evidence-for: bears on the choice of checking mechanism; a production system ships the trusted, hand-declared version string as its default, with source hashing as the checked option, but does not measure the cost-risk trade-off

## `kb/sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md`

- Title: Ingest: Harness Handbook
- Description: Source-validated behavior maps improve harness edit-site localization, while executed modification and self-evolution remain unevaluated.

> The paper supplies a checking design to compare with [checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md): its generated handbook remains subordinate to source through locator validation, fingerprints and hashes, diff-driven invalidation, scoped regeneration, and freezing of unverifiable entries. These mechanisms illustrate one design for managing reliance risk; whether its checks are worth their cost requires a separate assessment. Its L1-L3 navigation supplies evaluated evidence for [progressive-disclosure pointer design](../theory/pointer-design-tradeoffs-in-progressive-disclosure.md), and its synchronized caches instantiate the requirement to [keep lineage and compiled views from drifting](../theory/agent-memory-requirements/keep-compiled-views-aligned.md).

## `kb/sources/prov-overview.ingest.md`

- Title: Ingest: PROV-Overview — An Overview of the PROV Family of Documents
- Description: W3C PROV family roadmap — the canonical standard for 'full provenance' that the KB's lineage concept deliberately trims down from

> 5. **Provenance-of-provenance as a modeled concern.** PROV explicitly treats provenance of provenance records (bundles, PROV-LINKS); a recurring blind spot when the KB's own lineage records are themselves derived artifacts that can go stale — connects to [checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) as another retained result whose staleness can mislead consumers. [just-a-reference]

## `kb/tags/claims-and-grounding-README.md`

- Title: claims-and-grounding
- Description: Curated head for the claims-and-grounding tag — claim titles, claim modality, ground truth and supersession, source grounding and quotes, and grounding evidence from review runs

> - [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — retained results amortize production work; checking spends part of that saving to manage the risk of relying on stale or wrong claims

## `kb/tags/context-engineering-README.md`

- Title: Context engineering
- Description: Curated head for the context-engineering tag — getting the right knowledge into a bounded LLM context at the right time: routing, loading, scoping, context budgets, scheduling, and what to retain for later loading

> - [Checking retained results trades cost against reliance risk](../theory/checking-retained-results-trades-cost-against-reliance-risk.md) - retaining results amortizes discovery and derivation across uses; checking frequency trades that saving against the risk of relying on stale or wrong content

## `kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md`

- Title: A citation cannot assert more fidelity than its capture preserved
- Description: Quote checking in general: what a wording check, an occurrence check and a source-identity check each establish, which evidence a pass is relative to, and what stays unverified — attribution upstream, contextual support, truth

> For an exact-wording claim, an inexpensive occurrence check can justify treating mismatch as failure rather than warning. This is a choice within the [trade-off between checking cost and reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md), not a universal rule for retained results. Later readers can reuse the check's result, accepting the risk of changes since it ran.

## `kb/theory/a-consumption-channel-delivers-force-without-the-history-that.md`

- Title: A consumption channel delivers force without the history that earned it
- Description: A consumption path can promote content into a higher-force role without checking whether an authorization covers that content, version, and use

> Authorization metadata inherits the same problem. A verified flag or approved status is itself content in a trusted position, so a stale or unbacked mark can suppress the check that would have caught it. For derived authorization metadata, [checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md); the channel's force can justify strict enforcement, but the trade-off does not universally require checking on every use. A non-recomputable attestation instead needs a policy for changes that may defeat its scope. This KB chooses a strict policy for `user-verified`: a substantive edit strips the human attestation, and only another explicit act restores it.

## `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md`

- Title: A note is an atomic step relative to the check that reads it
- Description: Two independent bounds on a note: one claim sized to the reader's bounded context, and one checkable inference sized to the checker's single pass — for the grounding check the unit is the unquoted source

> The reason is that Commonplace has moved that finding step into code. A
> quotation marked `verbatim` is resolved by substring match against the file it
> links, and a mismatch fails the note before any reviewer opens anything ([ADR
> 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md));
> the source-side material is itself held as retained quotes validated against the
> captured source ([ADR
> 073](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)).
> This is a local enforcement choice within the trade-off that [checking retained
> results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md):
> the quote is a copy of something held elsewhere, and the citation contract
> requires a validator to check its occurrence and fail on mismatch. A paraphrase
> instead needs judgment about support rather than this wording check. For exact quotations, [a citation cannot assert more fidelity than
> its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)
> — a passage never captured word for word cannot be quoted into this route
> without returning to the source.

> - [Checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md) — grounds: the cost–risk comparison within which Commonplace chooses mechanical quote checking, distinct from judgment about support

## `kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md`

- Title: An enforced tag-README combines a MOC pattern with checked membership
- Description: A Commonplace tag-README can inherit Milo's contextual mapping pattern while validation checks only its declared membership relations, not editorial quality.

> A valid `complete` mark permits a consumer to skip the by-tag membership sweep
> and to trust the README's routing through its linked child heads. Without the
> mark, the scoped membership query remains the fallback. The mark is a retained
> claim that authorizes a particular shortcut rather than replacing canonical
> membership. [Checking retained results trades cost against reliance
> risk](./checking-retained-results-trades-cost-against-reliance-risk.md): the
> validator checks this claim when the head is validated, and later reads reuse
> that result rather than repeating the membership derivation.
> A false trusted copy can hide missing members when it [suppresses the retrieval
> that would expose
> them](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md);
> checking the exact relation on which stopping depends turns such drift into a
> visible failure at the next validation. The mark may be false between checks. This is a conditional control-flow mechanism, not evidence
> that every agent needs these marks or that consumers always stop at an index.

## `kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`

- Title: Source changes should surface downstream review targets, while reverse lineage can remain searchable
- Description: Source-dependent artifacts need lineage signals when an upstream change may render those artifacts stale, regardless of where the lineage record is stored

> The designs compose: source-side pointers as the human-visible interrupt, derived into a database for global queries — at which point the database is itself a retained derived result whose [checking frequency trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md). A stale lineage view can miss review targets, so the chosen refresh policy matters to the interruption-first criterion.

## `kb/theory/commitment-not-derivation-creates-new-ground-truth.md`

- Title: Commitment, not derivation, creates new ground truth
- Description: Derivation — claims recoverable from the source, nothing added — leaves the source as ground truth; what adds unentailed resolutions becomes ground truth at commit, repaired by supersession

> **Mechanical checkability supplies an option, not a universal enforcement rule.** [Checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md): retaining a result amortizes production across uses, while checking spends part of that saving to reduce reliance risk. Its condition 1 requires a judgment-free derivation or comparison rule, but does not fix a checking interval. Judgment-checked derivations may also merit reuse. Past the commitment boundary, comparison with the original inputs cannot recover what the commitment added; requiring that recovery as a condition of retention would delete irrecoverable content.

> - [Checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md) — contrasts: checking a retained derivation manages reliance risk, but cannot reconstruct an addition its source never determined

## `kb/theory/design-rationale-must-preserve-unregenerable-decision-premises.md`

- Title: Design rationale must preserve decision premises its interpreter cannot regenerate
- Description: Retention test for source-checkout design rationale: keep current decision premises not faithfully recoverable from implementation, git, and general knowledge; treat recoverable, role-free explanation as a cache

> For mechanically derived copies, [checking retained results trades cost against reliance risk](./checking-retained-results-trades-cost-against-reliance-risk.md); mechanical checkability does not fix the refresh interval. Natural-language explanations whose fidelity requires judgment cannot have that fidelity reconstructed mechanically. Their review arrangements — supported by a lineage edge, a review baseline, or a named owner — and the risk accepted between reviews are design choices this note does not fix. Such explanations can still be worth retaining and relying on. Neither case licenses a hand-maintained copy to acquire unexamined authority merely because it is convenient to read.
