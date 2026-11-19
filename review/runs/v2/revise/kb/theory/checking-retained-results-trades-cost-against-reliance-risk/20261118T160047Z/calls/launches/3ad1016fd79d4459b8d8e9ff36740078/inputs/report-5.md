---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/role
launch: dbf0b5ed2c77443da87dbb2106e52ab1
completed-at: '2026-11-18T16:07:47Z'
findings:
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/agent-memory-systems/reviews/swamp.md — links under
    the old title 'A derived copy of recomputable truth must be checked or absent'
    to match Swamp's rebuildable catalog and on-disk verification. The note supplies
    checking of retained derived results as a cost-risk choice, but not the checked-or-absent
    rule the link text names; the dependent uses the note in a stricter sense than
    the note now holds.
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'SUPPLIED — kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md
    — rests-on: needs the framing that a restated copy drifts, to justify using the
    type spec directly. The note supplies the drift mechanism; it does not name reading
    the source directly as an option, but the ADR needs only the drift risk.'
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'SUPPLIED — kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md
    — rests-on: same need as ADR 038, the drift risk of restating COLLECTION.md, avoided
    by using it directly.'
- scope: passage
  quotes:
  - Testing or centralizing a validator lowers the cost of assurance but does not
    prove the validator correct.
  reason: SUPPLIED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — needs the four mechanical-check conditions, applied one by one to verbatim quotes,
    and the claim that centralizing a checker does not prove it correct. The note
    supplies the numbered list and the condition-4 caveat.
- scope: passage
  quotes:
  - Testing or centralizing a validator lowers the cost of assurance but does not
    prove the validator correct.
  reason: DUPLICATED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — the ADR restates condition 4 ('Centralizing the extraction heuristic spreads
    assurance work across citations but does not prove it correct'). The ADR's version
    is the better one for its use because it names the concrete heuristic; the note's
    version is the general statement the ADR instantiates.
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'SUPPLIED — kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md
    — see-also: needs the drift risk of unvalidated lifecycle state.'
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: SUPPLIED — kb/reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md
    — needs the check-or-omit choice for a duplicated modality field framed as a local
    cost-risk condition, explicitly 'not a universal prohibition on retained results'.
    The note's trade-off framing matches that reading.
- scope: passage
  quotes:
  - Accepting some risk between checks can be right, provided it is an explicit choice
    rather than a hidden consequence of trusting the copy.
  reason: SUPPLIED — kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md
    — needs the trade-off framing for an unchecked constraint that agents obeyed,
    with observed write refusals as the local reason to stop accepting the risk. The
    suppression mechanism it also invokes is cited directly from the indexes note.
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: 'SUPPLIED — kb/reference/proposals/a-reader-facing-banner-for-user-verification.md
    — rests-on: needs the framing of a consistency check as checking effort spent
    against false-attestation risk.'
- scope: document
  quotes: []
  reason: NOT SUPPLIED — kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md
    — (archived proposal) cites 'the general rule that a derived copy of recomputable
    truth must be checked or absent' to make inline quotations admissible. The note
    states no such general rule; it makes checking frequency a cost-risk choice, and
    other dependents cite it as explicitly not universal.
- scope: document
  quotes: []
  reason: NOT SUPPLIED — kb/reference/proposals/archive/source-genre-is-one-open-field-on-the-snapshot.md
    — (archived, adopted proposal) cites 'the single-ground-truth rule' that a derived
    copy must be checked or absent, as rationale for dropping the report's genre field.
    The note no longer states this rule; it would supply only the weaker reason that
    an unchecked copy carries drift risk.
- scope: passage
  quotes:
  - named inputs (the participating collections and nothing else)
  reason: 'PARTLY SUPPLIED — kb/reference/proposals/archive/tag-scope-is-declared-where-membership-claims-are-made.md
    — (archived, adopted proposal) rests-on: needs ''scope is a parameter of the derived
    claim, so it must be part of what the check enforces or the claim must not be
    made''. The note shows scope as part of the mark''s checked inputs, but not the
    must-check-or-must-not-claim rule.'
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: 'SUPPLIED — kb/reference/proposals/channel-compiled-instruction-artifacts.md
    — rests-on: needs the trade-off that the compiled-copy adoption criterion asks
    the design to resolve.'
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md
    — says the note 'frames the choice between accepting drift, checking copies, and
    reading the source' and 'states the mechanical-check conditions'. The note supplies
    accepted risk, checking and the four conditions; it does not name reading the
    source instead of keeping a copy as one of the options.
- scope: passage
  quotes:
  - Accepting some risk between checks can be right, provided it is an explicit choice
    rather than a hidden consequence of trusting the copy.
  reason: 'SUPPLIED — kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md
    — rests-on: needs checked back-pointers framed as a local cost-risk choice, not
    the only permissible retained routing surface.'
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'SUPPLIED — kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md
    — rests-on: same need as ADRs 038 and 041, avoiding restatement drift by using
    dependency documents directly.'
- scope: passage
  quotes:
  - These conditions make a check possible and worth relying on, not free or current.
  reason: 'SUPPLIED — kb/reference/validation-contract.md — rests-on: cites ''distinct
    conditions 2 and 3'' (locatable inputs; available at check time) by number, and
    the claim that the conditions make checking possible, not obligatory. The note''s
    numbering and its possible-not-free statement match.'
- scope: passage
  quotes:
  - These conditions make a check possible and worth relying on, not free or current.
  reason: 'DUPLICATED — kb/reference/validation-contract.md — restates the note''s
    point as ''Those conditions make checking possible; they do not make it obligatory''.
    Each phrasing fits its own place: the contract''s ''not obligatory'' is what it
    needs before selecting checks locally; the note''s ''not free or current'' covers
    cost and freshness.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md
    — compares with the note on what a mechanical check establishes (§3.6 definition
    of 'checked'), explicitly not on checking frequency; the note's mechanical-check
    conditions supply the comparison point. The passage is cut at 1200 characters,
    so any further need or recommendation in it is unseen.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/sources/build-systems-a-la-carte.ingest.md — compares verifying
    traces and content-addressable caches with the note's checking of retained results,
    and disclaims corroboration of a universal check-or-discard requirement. The note's
    trade-off framing matches that disclaimer.
- scope: document
  quotes: []
  reason: 'PARTLY SUPPLIED — kb/sources/dagster-asset-versioning-and-caching.ingest.md
    — is-evidence-for: bears on the choice of checking mechanism (a trusted, hand-declared
    code version versus source hashing). The note supplies the cost-risk trade-off
    and checker trustworthiness (condition 4) but does not treat the choice between
    a declared version and a computed check as mechanisms. The prose passage is cut
    at 1200 characters.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md
    — needs a frame against which to compare a checking design (locator validation,
    fingerprints, scoped regeneration); the note's trade-off supplies it, and the
    ingest likewise leaves cost-worthiness unassessed.
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'SUPPLIED — kb/sources/prov-overview.ingest.md — citation only (''just-a-reference''):
    lineage records as another retained result whose staleness can mislead consumers.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/claims-and-grounding-README.md — citation only, as a
    tag-head entry; its gloss (amortized production, checking spends part of the saving)
    matches the note's opening.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/context-engineering-README.md — citation only, as a tag-head
    entry; its gloss restates the note's description.
- scope: passage
  quotes:
  - Assurance dates from the last check.
  reason: SUPPLIED — kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
    — needs the trade-off as a non-universal frame within which an inexpensive occurrence
    check can justify failure, and that later readers reuse a check's result, accepting
    changes since it ran.
- scope: passage
  quotes:
  - the copy suppresses the search that would have exposed what it misses
  reason: 'SUPPLIED — kb/theory/a-consumption-channel-delivers-force-without-the-history-that.md
    — needs: derived authorization metadata falls under the trade-off, which does
    not universally require checking on every use, and a stale mark can suppress the
    check that would catch it. The note supplies both the trade-off and the suppression
    mechanism.'
- scope: passage
  quotes:
  - Some properties remain mechanically checkable, such as link resolution and required
    sections, but checking them does not reconstruct that judgment.
  reason: 'SUPPLIED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — grounds: needs the cost-risk comparison within which mechanical quote checking
    is a local choice, distinct from judgment about support. The note supplies the
    trade-off and the mechanical-versus-judgment distinction.'
- scope: passage
  quotes:
  - 'Enforcement is reactive: the validator flags a gap when the head is next validated,
    so a mark can be false in between.'
  reason: SUPPLIED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md
    — needs the completeness mark read as a retained claim checked at validation,
    reused by later reads, and possibly false between checks.
- scope: passage
  quotes:
  - The validator performs the membership derivation when the head is validated, rather
    than on every read.
  reason: DUPLICATED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md
    — both notes state that the mark authorizes skipping the membership sweep, is
    checked at validation, is reused by later reads and can be false between checks,
    and both link the suppression mechanism. The tag-README note states the mark's
    mechanics better for its dependents, because it is the mark's home; the note adds
    the stop-authorization framing and the contrast with the connect report.
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: SUPPLIED — kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md
    — needs a lineage database treated as a retained derived result whose checking
    frequency trades cost against reliance risk.
- scope: passage
  quotes:
  - A derivation or comparison rule
  reason: SUPPLIED — kb/theory/commitment-not-derivation-creates-new-ground-truth.md
    — needs amortized production with checking spending part of the saving, and condition
    1 (judgment-free rule) cited by number as not fixing a checking interval; contrasts
    checking with additions a source never determined.
- scope: passage
  quotes:
  - so one production is amortized over many uses
  reason: DUPLICATED — kb/theory/commitment-not-derivation-creates-new-ground-truth.md
    — restates the note's opening in one sentence ('retaining a result amortizes production
    across uses, while checking spends part of that saving'). The dependent's one-line
    version is adequate for its use; the note's opening adds the frontloading link
    and the cheaper-verification exception.
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: SUPPLIED — kb/theory/design-rationale-must-preserve-unregenerable-decision-premises.md
    — needs mechanically derived copies placed under the trade-off, with mechanical
    checkability not fixing the refresh interval.
contract: report
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/role/artifact/reviews/9f520931a98b3cfc23f2cfd0/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/role/artifact/reviews/9f520931a98b3cfc23f2cfd0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/role/calls/launches/dbf0b5ed2c77443da87dbb2106e52ab1/outputs/review.md
raw-output-sha256: 61137f5b0e13b1530d37d5f68a6366bfa0cdaf162ebc3311b15eabcba2ce9001
---

# Role in the KB: Checking retained results trades cost against reliance risk

## Role
The note is the KB's general frame for keeping derived copies: a retained result saves recurring work, and how often it is checked is a cost-against-reliance-risk choice, not a universal rule. ADRs, proposals and the validation contract rest on it to justify local choices (use the source directly, check a copy, or accept drift), and theory notes cite it to place a specific check inside the trade-off. Its numbered mechanical-check conditions are cited individually. A cluster of older dependents still links to it under a former title stating a stricter rule ("must be checked or absent"), which the note no longer supplies.
Relied on: the cost-risk trade-off and its non-universality; drift from separate update paths; the four mechanical-check conditions with their numbering (1, 2, 3 and 4 are each cited); "possible, not free or obligatory"; the condition-4 caveat about centralized checkers; the completeness-mark example; the suppression mechanism; assurance dating from the last check; the mechanical-versus-judgment distinction. Unused: the connect-report example as such, the frontloading connection, the Scope bullets and the Open Questions. No visible dependent cites the "No known change does not establish freshness" section by name, although two dependents rely on its point.

## Dependents
41 files link to the note; only the first 30 by path are shown, and 11 are cut and unseen. Two ingest passages (build-systems theory-and-practice, Dagster) are cut at 1200 characters.

- `kb/agent-memory-systems/reviews/swamp.md` — the check-or-absent rule (old title), for Swamp's rebuildable catalog.
- `kb/reference/adr/038-…`, `041-…`, `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md` — restatement drift, avoided by using the dependency document directly.
- `kb/reference/adr/046-…` — the four conditions applied to verbatim quotes, and the condition-4 caveat.
- `kb/reference/adr/056-…` — drift risk of unvalidated lifecycle state.
- `kb/reference/adr/066-…` — check-or-omit for a duplicated field as a local cost-risk condition.
- `kb/reference/adr/068-…` — trade-off framing for dropping an unchecked menu.
- `kb/reference/proposals/a-reader-facing-banner-for-user-verification.md` — consistency check against false attestation.
- `kb/reference/proposals/archive/atomic-step-grounding-…`, `…/source-genre-…` — the check-or-absent general rule (old title).
- `kb/reference/proposals/archive/tag-scope-…` — scope as part of what the check enforces, or no claim.
- `kb/reference/proposals/channel-compiled-instruction-artifacts.md` — the trade-off its adoption criterion resolves.
- `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` — a three-way choice (accept drift, check, read the source) and the conditions.
- `kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md` — checked back-pointers as a local choice.
- `kb/reference/validation-contract.md` — conditions 2 and 3 by number; conditions make checking possible, not obligatory.
- `kb/sources/build-systems-a-la-carte*.ingest.md` (two), `harness-handbook…`, `dagster…`, `prov-overview…` — comparison points for checking mechanisms and stale derived records.
- `kb/tags/claims-and-grounding-README.md`, `kb/tags/context-engineering-README.md` — citation only.
- `kb/theory/a-citation-cannot-assert-…`, `a-consumption-channel-…`, `a-note-is-an-atomic-step-…`, `an-enforced-tag-readme-…`, `artifacts-produced-from-sources-…`, `commitment-not-derivation-…`, `design-rationale-must-preserve-…` — the trade-off as a non-universal frame for a specific check, plus suppression, the mark's mechanics, condition 1 or the mechanical-versus-judgment distinction.

## Duplication
- ADR 046 restates condition 4 for its extraction heuristic; the ADR's version is better for its local use because it names the heuristic.
- The validation contract restates "possible, not obligatory"; each phrasing fits its place.
- The enforced tag-README note and this note both carry the completeness mark's mechanics (skip permission, validation-time check, reuse, false between checks, suppression link). The tag-README note is the mark's home and states the mechanics better for dependents; this note adds the stop-authorization framing and the connect-report contrast.
- The commitment note restates the note's opening sentence in brief; adequate for its use.

## Untaken recommendations
None in the visible passages. The two ingest passages cut at 1200 characters and the 11 cut files may contain recommendations that are unseen here.

## Reach
- **The trade-off claim and its non-universality** reach most dependents: ADRs 038, 041, 056, 066, 068; the banner, channel-compiled, checked-inline-blocks, decisions-bind and factored-dependency proposals; the validation contract; the citation-fidelity, consumption-channel, atomic-step, lineage, commitment and design-rationale notes; and the build-systems ingest that disclaims a universal check requirement.
- **The numbered conditions** reach ADR 046 (all four, in order), the validation contract (conditions 2 and 3 by number), the commitment note (condition 1 by number) and the checked-inline-blocks proposal. Renumbering or merging conditions would break those references.
- **The condition-4 wording** reaches ADR 046.
- **"Possible, not free or current"** reaches the validation contract.
- **The completeness-mark section** reaches the enforced tag-README note.
- **The suppression mechanism** reaches the consumption-channel note and the enforced tag-README note.
- **The mechanical-versus-judgment distinction** reaches the atomic-step, commitment and design-rationale notes.
- **The title** reaches every linker. Four dependents (swamp, and the atomic-step, source-genre and tag-scope archived proposals) already link under a former title stating a stricter check-or-absent rule; their reliance does not match the current claim.
- The connect-report example, the frontloading link, Scope and Open Questions reach no visible dependent; the 11 cut files are unseen.
