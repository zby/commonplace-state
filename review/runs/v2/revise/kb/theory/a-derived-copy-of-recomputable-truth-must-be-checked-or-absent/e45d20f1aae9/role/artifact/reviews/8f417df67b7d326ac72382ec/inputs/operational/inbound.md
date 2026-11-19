# Inbound contexts of `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`

38 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

Only the first 30 files by path are shown; 8 more were cut.

## `kb/agent-memory-systems/reviews/swamp.md`

- Title: Swamp
- Description: Swamp review: agent-authored automation compiled into validated YAML workflows, with versioned operational data and progressively disclosed skills

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - Matches Swamp's rebuildable catalog and on-disk verification behavior.

## `kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md`

- Title: 038-Type-conformance reviews use the type spec as the gate
- Description: Type-conformance review pairs put the note's type spec on the gate side of the existing (note, gate) freshness key, so a type edit stales exactly its cohort with no new storage semantics

> - [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why the gate must be the type spec rather than restate it

## `kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md`

- Title: 041-Collection-conformance reviews use COLLECTION.md as the gate
- Description: Collection-conformance pairs put the note's COLLECTION.md on the gate side of the existing (note, gate) freshness key, matching the enforcement type contracts got in ADR 038

> - [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why the gate must be the COLLECTION.md rather than a catalog gate restating it

## `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`

- Title: 046-Verbatim quotes are validated against their cited source
- Description: `commonplace-validate` resolves every `verbatim`-marked quotation against the source it links; a false verbatim claim fails, and `unresolved` warns only where the convention is demonstrably in use

> That is exactly the state [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) forbids. All four of its preconditions hold here: the derivation rule is a strict substring test, the quote names its source via the adjacent markdown link, the source snapshot is a checked-in file present at validation time, and the extraction heuristic is a single centralized artifact amortized across every citation it protects. The check is therefore Level A — deterministic, near-zero cost — not a judgment-based review gate.

## `kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md`

- Title: 056-Adopted and retired proposals archive out of the frontier
- Description: Adopted and retired proposals move to a link-sink archive after extraction; provenance becomes a title tag, so ADRs from 2026-07-25 must carry a Considered alternatives section

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: the marks doctrine that ruled out an unvalidated lifecycle frontmatter field

## `kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md`

- Title: 068-Collection contracts stop enumerating available types
- Description: Accepted decision that COLLECTION.md states type eligibility instead of listing types, with kb/work allowed to use any valid type contract

> Nothing in the runtime parsed these tables and nothing enforced their contents. The menu was therefore an unchecked constraint that agents obeyed — the configuration [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rules out, producing the failure [indexes lower recall when they suppress retrieval that would find more](../../theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) names.

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: the rule that decides between removing the copy and enforcing it

## `kb/reference/proposals/a-reader-facing-banner-for-user-verification.md`

- Title: A reader-facing banner for user verification
- Description: Proposal: surface committed user verification at the point of reading through a standardized Markdown banner without turning absence into a review or truth verdict

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: a committed banner is safe only when mechanically checked against frontmatter

## `kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md`

- Title: Atomic-step grounding bounds unquoted sources per note
- Description: Proposal: move the grounding reading limit from the review to the note — a note may cite at most N sources a reviewer must open and search, with validated inline quotes and note links exempt

> **ADR 078 is not contradicted.**
> [ADR 078](../../adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md)
> rejected evidence living in the target artifact and kept the ingest `## Quotes`
> pool as the evidence owner. An inline quotation is not a second evidence store:
> it is a checked copy of a quote the ingest already retains, admissible exactly
> because a validator re-derives it and fails on mismatch — the general rule that
> [a derived copy of recomputable truth must be checked or absent](../../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
> The ingest remains the owner, and the required `## Quotes` tightening above is
> what keeps that true.

## `kb/reference/proposals/archive/source-genre-is-one-open-field-on-the-snapshot.md`

- Title: Source genre is one open-vocabulary field on the snapshot
- Description: Proposal (adopted): record source genre once as an open-vocabulary field on the snapshot, drop the ingest-report enum and genre-carrying tags, and unify two divergent vocabularies

> 2. **The ingest-report drops its `source_type` field.** The report's Classification section keeps its prose justification, and the Limitations Standards lens is selected by reading the paired snapshot's field — the ingest process opens the snapshot anyway. No duplicated field means no unchecked derived copy, per [a derived copy of recomputable truth must be checked or absent](../../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

> - [A derived copy of recomputable truth must be checked or absent](../../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the single-ground-truth rule behind dropping the report's copy of genre

## `kb/reference/proposals/archive/tag-scope-is-declared-where-membership-claims-are-made.md`

- Title: Tag scope is declared where membership claims are made
- Description: Proposal (adopted): one tag namespace per KB; membership claims range over participating collections; trace-learning stays navigable; canonical filename-derived heads live in kb/tags/

> - [A derived copy of recomputable truth must be checked or absent](../../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: scope is a parameter of the derived claim, so it must be part of what the check enforces or the claim must not be made

## `kb/reference/proposals/channel-compiled-instruction-artifacts.md`

- Title: Channel-compiled instruction artifacts
- Description: Proposal: resolve execution channel at install time so an agent reads one literal procedure, extending build-time generation from paths to shell and command form

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: the constraint a compiled artifact must satisfy

## `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md`

- Title: Checked inline blocks for shared instruction text
- Description: Proposal: reuse natural-language authoring mechanics in specialized writer prompts through literal inlining backed by deterministic source-to-copy checks

> The existing rule that [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rules out a trusted, hand-maintained middle state. The question is which checked or absent form fits instruction text.

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: rules out a trusted but unchecked inline copy and supplies the deterministic-oracle boundary

## `kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md`

- Title: Decisions bind their consumers through site back-pointers
- Description: Proposal: make a recorded decision reach the operations it constrains by having each ADR declare the artifacts it binds and each bound artifact carry a checked back-pointer, rather than a hand-maintained decision index

> - [A derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why the candidate's back-pointer must be validator-checked and why the hand-maintained index option is rejected outright

## `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md`

- Title: Factored dependency pairs for review freshness
- Description: Proposal: keep review dependencies factored as two-input pairs where that shape fits; type and collection pairs are shipped while a review target with more than two inputs remains

> - [a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why each dependency document must be the gate rather than be restated in one

## `kb/reference/validation-contract.md`

- Title: The validation contract
- Description: The base, type-rule, and schema sources of deterministic findings, their dereferencing limits, and the run-scoped execution model

> So the dividing line is not frontmatter/body. It is **inside the supplied schema instance** (declarable) versus **outside that instance** (must be loaded and checked). Directory schemas can compare the member data their loader supplies; they cannot perform filesystem reads themselves. A referential check's ground truth lives in a second artifact, which is precondition 3 of [a derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — the rule that makes these checks obligatory rather than optional.

> - [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rests-on: why a referential check is obligatory rather than optional, and why a false copy fails where an absent one warns

## `kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md`

- Title: Ingest: Build systems à la carte: Theory and practice
- Description: Extended JFP version of Build Systems à la Carte: classifies replay-from-top workflow engines, and shows why untracked reads, missing self-tracking and non-determinism break exact recheck

> For the KB, the paper is the formal anchor for the derived-artifact freshness cluster, and it adds the limits the conference ingest lacked. It is evidence for [Criteria edits invalidate verdicts; process edits invalidate artifacts](../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md). §8.8 says systems whose tasks are full programs must pessimistically assume that any script change may change any task. §7.3 puts script and rule versions into Cloud Shake's cache keys to avoid stale products. It is evidence for [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md): §3.6 is a formal definition of "checked". It is also evidence for [LLM recompute cost shifts the store-vs-recompute balance](../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md): §8.3 replaces exact equality with membership in the set of possible results for non-deterministic tasks, and §8.4 shows that deep traces then return results inconsistent with their own dependencies. It supplies failure modes for [Link graph plus timestamps enables make-like staleness detection](../theory/link-gr [cut at 1200 characters]

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
> criteria versus process. It qualifies
> [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md):
> the hand-declared `code_version` is a tru [cut at 1200 characters]

> - [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — is-evidence-for: qualifies the claim; a production system ships the trusted, hand-declared version string as its default, with source hashing as the checked option

## `kb/sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md`

- Title: Ingest: Harness Handbook
- Description: Source-validated behavior maps improve harness edit-site localization, while executed modification and self-evolution remain unevaluated.

> The paper is a concrete technical basis for the KB's claim that [a derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md): its generated handbook remains subordinate to source through locator validation, fingerprints and hashes, diff-driven invalidation, scoped regeneration, and freezing of unverifiable entries. Its L1-L3 navigation supplies evaluated evidence for [progressive-disclosure pointer design](../theory/pointer-design-tradeoffs-in-progressive-disclosure.md), and its synchronized caches instantiate the requirement to [keep lineage and compiled views from drifting](../theory/agent-memory-requirements/keep-compiled-views-aligned.md).

## `kb/sources/prov-overview.ingest.md`

- Title: Ingest: PROV-Overview — An Overview of the PROV Family of Documents
- Description: W3C PROV family roadmap — the canonical standard for 'full provenance' that the KB's lineage concept deliberately trims down from

> 5. **Provenance-of-provenance as a modeled concern.** PROV explicitly treats provenance of provenance records (bundles, PROV-LINKS); a recurring blind spot when the KB's own lineage records are themselves derived artifacts that can go stale — connects to [a derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). [just-a-reference]

## `kb/tags/claims-and-grounding-README.md`

- Title: claims-and-grounding
- Description: Curated head for the claims-and-grounding tag — claim titles, claim modality, ground truth and supersession, source grounding and quotes, and grounding evidence from review runs

> - [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — a copy of recomputable information is machine-checked against its source or does not exist

## `kb/tags/context-engineering-README.md`

- Title: Context engineering
- Description: Curated head for the context-engineering tag — getting the right knowledge into a bounded LLM context at the right time: routing, loading, scoping, context budgets, scheduling, and what to retain for later loading

> - [A derived copy of recomputable truth must be checked or absent](../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - names when a recomputable value is safe to inline for context economy: only when a validator can re-derive and check it, otherwise it must stay a live read

## `kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md`

- Title: A citation cannot assert more fidelity than its capture preserved
- Description: Capture is layered (verbatim / paraphrase / second-hand) by forced constraints; a citation's fidelity is bounded by which layer holds the passage, and no notation can raise it — only re-capture

> The temptation is to fix provenance downstream — a richer citation format, a structured span locator, a stricter gate. It cannot work, and the reason is exact rather than merely practical. [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) requires a *mechanical derivation rule* before a copy may be trusted. A verbatim-layer quote has one: substring match. A paraphrase-layer passage has no such rule — there is no mechanical comparison between a paraphrase and its source, only judgment. So marking a paraphrase-layer passage `verbatim` does not make it verbatim; it produces precisely the hand-maintained-and-trusted copy that rule forbids, with a stronger trust signal attached than the unmarked version would carry. Notation can *express* the fidelity bound. It cannot move it.

> - [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)

## `kb/theory/a-consumption-channel-delivers-force-without-the-history-that.md`

- Title: A consumption channel delivers force without the history that earned it
- Description: A consumption path can promote content into a higher-force role without checking whether an authorization covers that content, version, and use

> Authorization metadata inherits the same problem. A verified flag or approved status is itself content in a trusted position, so a stale or unbacked mark can suppress the check that would have caught it. A [derived copy of recomputable truth must therefore be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), while a non-recomputable attestation must be invalidated whenever its scope may no longer hold. This KB applies the latter rule to `user-verified`: a substantive edit strips the human attestation, and only another explicit act restores it.

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
> This is the general rule that [a derived copy of recomputable truth must be
> checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
> applied to citation: the quote is a copy of something held elsewhere, and it is
> admissible because a validator re-derives it and fails on mismatch. A paraphrase
> has no such derivation rule, and [a citation cannot assert more fidelity than
> its capture preserved](./a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)
> — a passage never captured word for word cannot be quoted into this route
> without returning to the source.

> - [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: why a validated quote may be trusted as a copy while a paraphrase may not

## `kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md`

- Title: An enforced tag-README combines a MOC pattern with checked membership
- Description: A Commonplace tag-README can inherit Milo's contextual mapping pattern while validation checks only its declared membership relations, not editorial quality.

> A valid `complete` mark permits a consumer to skip the by-tag membership sweep
> and to trust the README's routing through its linked child heads. Without the
> mark, the scoped membership query remains the fallback. The mark is therefore [non-load-bearing validated
> copies](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
> that authorize particular shortcuts rather than replace canonical membership.
> A false trusted copy can hide missing members when it [suppresses the retrieval
> that would expose
> them](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md);
> checking the exact relation on which stopping depends turns such drift into a
> visible failure. This is a conditional control-flow mechanism, not evidence
> that every agent needs these marks or that consumers always stop at an index.

## `kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`

- Title: Source changes should surface downstream review targets, while reverse lineage can remain searchable
- Description: Source-dependent artifacts need lineage signals when an upstream change may render those artifacts stale, regardless of where the lineage record is stored

> The designs compose: source-side pointers as the human-visible interrupt, derived into a database for global queries — at which point the database is itself a derived copy that must be [checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

> Under the interruption-first model, the consumer-facing artifact carries the content needed for use while a lineage view gives maintainers downstream targets when the workflow recognizes an upstream change. What the subsequent review *is* depends on the lineage regime: a derived artifact (content worked out from the source) is stale until re-derived and compared; an abstracted rule (content exceeding its instances) is re-opened for support rather than invalidated. Where the derivation is mechanical, [the check is free and the regime flips to enforce-or-omit](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

## `kb/theory/commitment-not-derivation-creates-new-ground-truth.md`

- Title: Commitment, not derivation, creates new ground truth
- Description: Derivation — claims recoverable from the source, nothing added — leaves the source as ground truth; what adds unentailed resolutions becomes ground truth at commit, repaired by supersession

> **Enforce-or-omit is a mechanical-zone rule.** [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rides on the deletion column: absence costs a recomputation, a false copy costs silent unbounded wrongness, so hand-maintained-and-trusted is forbidden. Its precondition 1 — mechanical re-derivability — is the mechanical zone's admission test stated as an availability condition. Pushed past the commitment boundary the rule degenerates rather than weakens: with no derivation to check against, "checked or absent" reduces to "absent", which deletes the only copy of something no source recovers. The rule is not weaker there; it does not apply there.

> - [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: locates its rule as the mechanical zone's enforcement rule and shows it degenerating rather than weakening past the commitment boundary

## `kb/theory/design-rationale-must-preserve-unregenerable-decision-premises.md`

- Title: Design rationale must preserve decision premises its interpreter cannot regenerate
- Description: Retention test for source-checkout design rationale: keep current decision premises not faithfully recoverable from implementation, git, and general knowledge; treat recoverable, role-free explanation as a cache

> Mechanically derived copies have a stricter maintenance rule: [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). Natural-language explanations whose fidelity requires judgment have no mechanical check; what stands in for one — a lineage edge, a review baseline, a named owner — is a design choice this note does not fix. Neither case licenses a hand-maintained copy to acquire unexamined authority merely because it is convenient to read.

## `kb/theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md`

- Title: Seven documentation cases left routing and synthesis
- Description: A seven-artifact Commonplace sweep found that direct source access removed exact-fact prose while discovery maps and cross-component boundaries survived; it does not establish a universal documentation ratio

> - [A derived copy of recomputable truth must be checked or absent](../a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: supplies the safety boundary for exact copies whose source remains authoritative

## `kb/theory/files-defer-centralized-schema-commitment-until-invariants-stabilize.md`

- Title: Canonical files may defer a shared schema while database authority remains a separate commitment
- Description: Canonical files can defer a centralized schema while meanings remain unsettled; a database becomes canonical only when an explicit authority decision and operative write path commit resolutions the files no longer determine.

> A serving or index view remains derived only to the extent that its declared inputs and rule determine its output. Its [lineage](./definitions/lineage.md) must also state the applicable refresh, checking, review, or invalidation obligation. A mechanically recomputable copy that is retained and trusted must be checked against its current source; otherwise it should exist only as live or build-time output and be absent when not generated. [Judgment-derived prose instead needs managed staleness](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), and a retained commitment cannot be checked back into a source that never contained it. An unchecked convenience view can otherwise drift into an accidental second authority. Accountability, rather than co-location or cheap replay, is what lets authored files remain canonical while another substrate provides derived capabilities.
