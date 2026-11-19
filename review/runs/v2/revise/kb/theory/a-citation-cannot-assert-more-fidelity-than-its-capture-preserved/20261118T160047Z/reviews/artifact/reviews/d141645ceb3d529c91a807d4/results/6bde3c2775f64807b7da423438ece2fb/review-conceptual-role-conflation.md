---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - no mechanism here checks that the capture faithfully represents the original or
    that the named author wrote it
  - Missing bytes therefore report as unverified, never as passed.
  - covers recognized quote candidates the checker could not pair with a source
  reason: 'Conflates the current artifact''s general explication of quote checking
    with one object of application, Commonplace''s own validator (cited through ADR
    073 and ADR 094 and its ''unresolved'' outcome). Reading 1: ''here'' means ''in
    this account of quote checking'', so the absence of a capture-fidelity or authorship
    check, the unverified-not-passed rule and the unresolved outcome are general properties
    any quote checker of this kind has or should have. Reading 2: ''here'' means ''in
    Commonplace''s implementation'', so these are reported facts about one system
    that a different checker might not share. The description promises ''quote checking
    in general'', which favours reading 1, while the ADR citations and outcome labels
    favour reading 2. The choice changes the scope of the claims (universal limit
    versus one system''s current behaviour) and what the note contributes (a normative
    design rule versus a description). The author must decide whether these sentences
    state a general requirement, describe Commonplace as an instance, or both, and
    mark which.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/d141645ceb3d529c91a807d4/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/d141645ceb3d529c91a807d4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 45b14aeb750013ef233e111278be943d3c5461fd10b42559133047fc6b27a2e4
format: 2
---

# Review

Most passages keep their roles clear. "Exact" is explicitly defined as "equal after this normalization rule"; the four questions are the note's own decomposition; ADR 046 is clearly attributed as the source of the judgment that false mismatches are worse than no check; and the trade-off note is invoked as a framework within which a severity choice is made, not as the source of that choice.

The material blur is between the general account and the system it is drawn from. The note's description frames it as quote checking in general, but several load-bearing sentences in "Which evidence a pass is relative to" and the Scope section use the deictic "here", Commonplace's outcome vocabulary ("unresolved"), and ADR citations as if a system's behaviour and a general rule were one claim. A reader cannot tell whether a non-Commonplace checker that does verify capture fidelity, or that does fall back to a cached copy, contradicts the note or merely differs from Commonplace. That attribution and scope decision belongs to the author.
