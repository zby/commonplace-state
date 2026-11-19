---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/role
launch: bb225826cc254a6480e15e467df2c84c
completed-at: '2026-11-16T22:26:26Z'
findings:
- scope: passage
  quotes:
  - a validator re-derives it from the source and fails on mismatch
  reason: SUPPLIED — kb/agent-memory-systems/reviews/swamp.md — citation only; it
    matches Swamp's rebuildable catalog and on-disk verification to the checked branch,
    which the note defines.
- scope: passage
  quotes:
  - When a copy can't be checked, the resolution is omission.
  reason: SUPPLIED — kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md
    — premise (rests-on) that a gate must be the type spec rather than restate it;
    the note supplies it through omission of an uncheckable natural-language copy
    in favour of reading the source live.
- scope: passage
  quotes:
  - When a copy can't be checked, the resolution is omission.
  reason: SUPPLIED — kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md
    — same premise as ADR 038, applied to COLLECTION.md; the omission resolution supplies
    it.
- scope: passage
  quotes:
  - 'Enforcement is available only when four preconditions hold:'
  reason: SUPPLIED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — needs all four preconditions (strict derivation rule, named source, ground truth
    present at validation time, centralized amortized validator) and the Level A classification;
    the note states each one and the Level A/B boundary.
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md
    — cites the note as 'the marks doctrine that ruled out an unvalidated lifecycle
    frontmatter field'. The note forbids unchecked copies of recomputable truth, but
    it treats a lifecycle or maturity field only in an open question (the `status:`
    field as a 'candidate trust mark'), and it does not say whether such a field is
    recomputable and therefore covered by the rule.
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: SUPPLIED — kb/reference/adr/068-collection-contracts-stop-enumerating-available-types.md
    — premise that decides between removing an unchecked type menu and enforcing it;
    the note supplies the two-state rule and the forbidden middle.
- scope: passage
  quotes:
  - a validator re-derives it from the source and fails on mismatch
  reason: SUPPLIED — kb/reference/proposals/a-reader-facing-banner-for-user-verification.md
    — premise that a committed banner is safe only when it is mechanically checked
    against frontmatter; the checked branch supplies it.
- scope: passage
  quotes:
  - a validator re-derives it from the source and fails on mismatch
  reason: SUPPLIED — kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md
    — needs the claim that an inline quote is admissible as a checked copy because
    a validator re-derives it and fails on mismatch; the dependent paraphrases the
    note's definition of 'checked'.
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: SUPPLIED — kb/reference/proposals/archive/source-genre-is-one-open-field-on-the-snapshot.md
    — rationale for dropping a duplicated genre field so that no unchecked derived
    copy exists; the absent branch supplies it.
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/reference/proposals/archive/tag-scope-is-declared-where-membership-claims-are-made.md
    — rests on the claim that scope is a parameter of the derived claim, so it must
    be part of what the check enforces or the claim must not be made. The note gives
    the general rule and mentions 'participating collections' in its tag-README instance,
    but it never states that a derived claim's parameters must fall within the check.
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: SUPPLIED — kb/reference/proposals/channel-compiled-instruction-artifacts.md
    — rests on the note for the constraint a compiled artifact must satisfy; the two-state
    rule (together with build-time-only omission, the ADR 025 example) supplies it.
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: SUPPLIED — kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md
    — needs the exclusion of a trusted unchecked inline copy and the deterministic-oracle
    boundary; the note supplies both, and it names instruction-text frontloading as
    instance 3 and as an open question.
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: SUPPLIED — kb/reference/proposals/decisions-bind-their-consumers-through-site-back-pointers.md
    — premise for requiring a validator-checked back-pointer and rejecting a hand-maintained
    decision index outright; the forbidden middle supplies it.
- scope: passage
  quotes:
  - When a copy can't be checked, the resolution is omission.
  reason: SUPPLIED — kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md
    — premise that each dependency document must be the gate rather than be restated
    in one; same use as ADR 038, supplied by the omission resolution.
- scope: passage
  quotes:
  - Ground truth that exists at validation time.
  reason: PARTLY SUPPLIED — kb/reference/validation-contract.md — cites 'precondition
    3' for the claim that a referential check's ground truth lives in a second artifact,
    and cites the note for why a false copy fails where an absent one warns. The asymmetry
    is supplied. Precondition 3 is about ground truth existing at validation time
    rather than being produced by execution; it is not about the ground truth lying
    in a second artifact (that location sense is closer to precondition 2), so the
    numbered reference only partly matches. The fail-versus-warn mapping is the dependent's
    own.
- scope: passage
  quotes:
  - a validator re-derives it from the source and fails on mismatch
  reason: 'SUPPLIED — kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md
    — evidence link: §3.6 is a formal definition of ''checked''; the note''s informal
    definition of ''checked'' is the term the ingest maps onto. The passage was cut
    at 1200 characters, so any further recommendation is unseen.'
- scope: passage
  quotes:
  - that is why hand-maintained-and-trusted is *forbidden* rather than merely risky
  reason: 'PARTLY SUPPLIED — kb/sources/dagster-asset-versioning-and-caching.ingest.md
    — is-evidence-for that qualifies the claim: a production system ships a trusted,
    hand-declared `code_version` as its default, with source hashing as the checked
    option. The note supplies the claim being qualified, but nothing in the note addresses
    a deployed default that sits in the forbidden state. The passage was cut at 1200
    characters.'
- scope: passage
  quotes:
  - a validator re-derives it from the source and fails on mismatch
  reason: SUPPLIED — kb/sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md
    — the handbook is a technical basis for the checked branch (locator validation,
    fingerprints, diff-driven invalidation, scoped regeneration, freezing of unverifiable
    entries); the note supplies the rule it instantiates.
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/sources/prov-overview.ingest.md — marked just-a-reference;
    it connects the note to provenance-of-provenance, meaning that lineage records
    are themselves derived artifacts that can go stale. The note treats lineage only
    as the pointer a validator follows (precondition 2), not as a derived copy that
    is itself subject to the rule.
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: SUPPLIED — kb/tags/claims-and-grounding-README.md — tag-head citation that
    summarizes the core rule; no dependent argument.
- scope: passage
  quotes:
  - Enforcement is the third class that lets both stand
  reason: 'SUPPLIED — kb/tags/context-engineering-README.md — tag-head summary: a
    recomputable value is safe to inline for context economy only when checked, otherwise
    it stays a live read; supplied by ''What enforcement buys'' and the omission consequence.'
- scope: passage
  quotes:
  - it is the forbidden state, just relocated one layer down, with a stronger trust
    signal attached
  reason: SUPPLIED — kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
    — needs precondition 1 (a mechanical derivation rule; substring match qualifies,
    paraphrase does not) and the 'stronger trust signal attached' framing it reuses
    for a false `verbatim` mark.
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: SUPPLIED — kb/theory/a-consumption-channel-delivers-force-without-the-history-that.md
    — cites the rule that a derived copy (here, verification metadata) is checked
    or absent, then contrasts it with non-recomputable attestation, which it handles
    itself.
- scope: passage
  quotes:
  - natural-language summaries and judgments do not
  reason: 'SUPPLIED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — grounds: a validated quote is a trusted copy because a validator re-derives
    it, and a paraphrase has no derivation rule; the note supplies both the definition
    of ''checked'' and precondition 1.'
- scope: passage
  quotes:
  - Dropping one costs consumers a recomputation, never correctness
  reason: 'SUPPLIED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md
    — needs the `complete` mark to be a validated copy that is non-load-bearing: it
    authorizes shortcuts, and canonical membership remains the fallback. The graceful-degradation
    consequence and instance 1 supply this.'
- scope: passage
  quotes:
  - A validator re-derives membership across the participating collections and fails
    a mark whose head does not reach every member in one hop
  reason: 'DUPLICATED — kb/theory/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md
    — the note''s instance 1 restates the validator-checked `complete` mark, which
    this dependent develops. For consumers of the mark, the dependent states it better:
    it names the shortcut the mark authorizes (skipping the by-tag sweep) and the
    scoped query as fallback, which instance 1 omits.'
- scope: passage
  quotes:
  - What flips the regime is the check price
  reason: 'SUPPLIED — kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md
    — needs two things: that a derived lineage database is itself a copy that must
    be checked or absent, and that where derivation is mechanical the check is free
    and the regime flips to enforce-or-omit. The core rule and the regime-flip section
    supply both.'
- scope: passage
  quotes:
  - re-derive and compare where the content is recoverable from the source, re-examine
    the support where it exceeds it
  reason: DUPLICATED — kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md
    — the note restates the dependent's managed-staleness regime split (a derived
    artifact is re-derived and compared; an abstracted rule is re-opened for support).
    The dependent states it better for its own use, because it owns the regime and
    ties it to the lineage view; in the note the restatement only marks a boundary.
- scope: passage
  quotes:
  - copy can cause silent, unbounded wrongness when it tells consumers to stop looking
  reason: SUPPLIED — kb/theory/commitment-not-derivation-creates-new-ground-truth.md
    — needs the absent/false asymmetry and precondition 1 by number, which it reads
    as the mechanical zone's admission test; both are present, and precondition 3's
    'never a recomputable copy in the first place' agrees with its 'degenerates past
    the commitment boundary'.
- scope: passage
  quotes:
  - copy can cause silent, unbounded wrongness when it tells consumers to stop looking
  reason: 'DUPLICATED — kb/theory/commitment-not-derivation-creates-new-ground-truth.md
    — restates the note''s asymmetry in one sentence (absence costs a recomputation;
    a false copy costs silent unbounded wrongness). The note states it better: it
    gives the mechanism (a trusted stale claim suppresses the recomputation that would
    expose it), while the dependent needs only the conclusion.'
- scope: passage
  quotes:
  - natural-language summaries and judgments do not
  reason: SUPPLIED — kb/theory/design-rationale-must-preserve-unregenerable-decision-premises.md
    — needs the split between mechanically derived copies (the strict rule) and natural-language
    explanations with no mechanical check; precondition 1 supplies it, and the dependent
    leaves the substitute mechanism open.
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: 'SUPPLIED — kb/theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md
    — grounds: the safety boundary for exact copies whose source remains authoritative;
    supplied by the core rule.'
- scope: passage
  quotes:
  - In that regime the hand-maintained dependent artifact is not forbidden; it is
    unavoidable
  reason: 'SUPPLIED — kb/theory/files-defer-centralized-schema-commitment-until-invariants-stabilize.md
    — needs two claims: a retained, trusted, recomputable copy must be checked, otherwise
    it exists only as live or build-time output; and judgment-derived prose needs
    managed staleness instead (its link anchor for that second claim points at this
    note). The core rule, the omission consequence and the managed-staleness boundary
    paragraph supply both.'
contract: report
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/role/artifact/reviews/8f417df67b7d326ac72382ec/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/role/artifact/reviews/8f417df67b7d326ac72382ec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/role/calls/launches/bb225826cc254a6480e15e467df2c84c/outputs/review.md
raw-output-sha256: efce800a63f5563fc46356b88a0249d340d9ac9db755feb0e9a26fb1ca94cd24
---

# Role in the KB: A derived copy of recomputable truth must be checked or absent

## Role
The note is a widely cited premise. Decisions and proposals argue from it to reject hand-maintained copies, either by enforcing a check or by reading the source live: ADRs 038, 041, 046 and 068, the gate-is-the-dependency-document proposals, back-pointer and banner proposals, and validation-contract. Theory notes use it as the boundary rule for mechanical derivation, against judgment-based managed staleness, commitment, paraphrase and attestation. Its most-used parts are the two-state rule with the forbidden middle, the absent/false asymmetry, the definition of "checked", the four preconditions (1 and 3 cited by number) and the regime flip at Level A checks.
Relied on: checked-or-absent / forbidden hand-maintained-and-trusted middle; definition of "checked" (validator re-derives and fails on mismatch); absent/false asymmetry; preconditions 1–4 (1 and 3 by number, 4's "stronger trust signal"); omission as the resolution (live read or build-time only); regime flip from managed staleness to enforce-or-omit at Level A; "checked copies degrade gracefully"; instance 1 (`complete` mark); recomputable-and-checked as a context-economy class. Unused: instances 2–4 (compiled memory views, hot-path contract values, `AGENTS.md.template` copies); the interrupt-placement point; "a cache must never be the only copy"; the second open question. The first open question (`status:` field) is touched only obliquely by ADR 056.

## Dependents
38 files link to the note; the supplied input shows the first 30 by path and cut 8, so those 8 are unseen. The build-systems and Dagster ingest passages were also cut at 1200 characters.
- `kb/agent-memory-systems/reviews/swamp.md` — citation of the checked branch.
- `kb/reference/adr/038-…`, `041-…`, `kb/reference/proposals/factored-dependency-pairs-…` — premise that the gate is the dependency document, not a restatement (omission branch).
- `kb/reference/adr/046-…` — all four preconditions and Level A.
- `kb/reference/adr/056-…` — "marks doctrine" against an unvalidated lifecycle field (partly supplied).
- `kb/reference/adr/068-…` — remove-or-enforce decision rule.
- `kb/reference/proposals/a-reader-facing-banner-…`, `decisions-bind-…`, `channel-compiled-…`, `checked-inline-blocks-…` — the forbidden middle and the checked branch.
- `kb/reference/proposals/archive/atomic-step-grounding-…`, `source-genre-…` — checked inline quote; absent duplicated field.
- `kb/reference/proposals/archive/tag-scope-…` — the scope of a derived claim falls inside the check (partly supplied).
- `kb/reference/validation-contract.md` — precondition 3 and the asymmetry (partly supplied).
- `kb/sources/build-systems-…`, `dagster-…`, `harness-handbook-…`, `prov-overview…` — evidence, a qualification and a connection.
- `kb/tags/claims-and-grounding-README.md`, `kb/tags/context-engineering-README.md` — tag-head summaries.
- `kb/theory/a-citation-…`, `a-consumption-channel-…`, `a-note-is-an-atomic-step-…`, `an-enforced-tag-readme-…`, `artifacts-produced-from-sources-…`, `commitment-not-derivation-…`, `design-rationale-…`, `evidence/seven-documentation-cases-…`, `files-defer-centralized-schema-…` — premise and boundary uses.

## Duplication
- The note's instance 1 restates the `complete`-mark mechanism that `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md` develops. The dependent states it better for mark consumers.
- The note's "Where the rule applies" section restates the regime split (re-derive and compare vs re-examine support) owned by `artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`. The dependent states it better.
- `commitment-not-derivation-creates-new-ground-truth.md` restates the absent/false asymmetry. The note states it better because it supplies the mechanism.
- ADR 046 and `a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` apply the preconditions closely and reuse the phrase "stronger trust signal attached". This is application rather than redundant restatement.

## Untaken recommendations
None visible. No shown passage carries an explicit "recommended next action", "revise" or "add this citation" for the note. The note cites neither the build-systems ingest (§3.6 as a formal definition of "checked") nor the Dagster ingest (which "qualifies" the claim). Both ingest passages were cut at 1200 characters, and 8 linking files are unseen, so a recommendation in the cut text cannot be ruled out.

## Reach
- **Two-state rule / forbidden middle and the definition of "checked":** nearly every dependent, especially ADRs 038, 041, 046 and 068; the banner, back-pointer, channel-compiled, checked-inline-block, factored-pair, atomic-step and source-genre proposals; validation-contract; both tag heads; `a-consumption-channel-…`; `a-note-is-an-atomic-step-…`; `seven-documentation-cases-…`; `files-defer-centralized-schema-…`; the swamp review; the build-systems and harness-handbook ingests.
- **Absent/false asymmetry:** `commitment-not-derivation-…`, `validation-contract.md` (fail vs warn), the Dagster ingest (as the claim it qualifies).
- **Preconditions and their numbering:** ADR 046 (all four); `validation-contract.md` (precondition 3 by number); `commitment-not-derivation-…` (precondition 1 by number); `a-citation-…` and `a-note-is-an-atomic-step-…` (precondition 1); `a-citation-…` (precondition 4's "stronger trust signal" wording); `design-rationale-…` (the natural-language exclusion). Renumbering or reordering the preconditions would break the numbered references in validation-contract and commitment-not-derivation.
- **Omission resolution (live read, build-time only):** ADRs 038 and 041, factored-dependency-pairs, source-genre, the context-engineering tag head, `files-defer-centralized-schema-…`.
- **Regime flip / managed-staleness boundary:** `artifacts-produced-from-sources-…`, `files-defer-centralized-schema-…`, `design-rationale-…`, `commitment-not-derivation-…`; the term "enforce-or-omit" is used by the first and the last.
- **Graceful degradation and instance 1:** `an-enforced-tag-readme-…`.
- **Recomputable-and-checked as a context-economy class:** the context-engineering tag head, checked-inline-blocks.
- **Open question on `status:`:** possibly ADR 056 (oblique).
- Changes to instances 2–4, the interrupt-placement remark, the "cache must never be the only copy" line or the second open question reach no shown dependent. The 8 cut files are unseen.
