---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: bdb15b9082614770b69f37ba9041d8ae
completed-at: '2026-11-16T22:39:19Z'
findings:
- scope: passage
  quotes:
  - an absence of that kind is a validator's result rather than a reviewer's finding
  reason: 'This frames the mechanism as the validator. The verbatim validator only
    checks quotations that are present: it resolves each `verbatim`-marked quote against
    its linked source. It cannot detect that a claim lacks a retained passage. The
    next sentence shows the real mechanism, which is counterfactual: had the author
    quoted the details, the validator would then have checked the quote. Detection
    therefore moves from the reviewer to authoring discipline, which the bound requires,
    plus the validator''s check of whatever was quoted. As written, the sentence excludes
    the case that the absence goes unquoted and the validator says nothing.'
  level: warn
- scope: passage
  quotes:
  - the bound is held by a validator that fails the note, not by a reviewer that stops
    reading
  reason: This presents the artifact-side bound as held by an existing validator,
    while the Scope section says the note does not decide N or 'a validator rule that
    would enforce it'. The mechanism is accurate for the proposed placement, but the
    present tense frames it as something already in force. Making the conditional
    explicit ('would be held') would match the scope.
  level: info
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old.
  reason: Descartes is introduced as a precedent for sizing to the checker, but the
    quoted precept sizes parts to 'its adequate solution', and the note itself concludes
    'The parts are sized to the solution'. Only the evidence of simple links points
    implicitly to a checker. The next paragraph partly corrects this ('Lamport makes
    the checker explicit'). The lead sentence emphasizes checker-relativity more than
    the Descartes evidence carries.
  level: info
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/df7931ab20bd78883ecf4de2/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/df7931ab20bd78883ecf4de2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/bdb15b9082614770b69f37ba9041d8ae/outputs/review-framing-mismatch.md
raw-output-sha256: 3dd552487f9ac15c1f136316f7490b64ebbfe9c5863ab73fc54059a89c8ed0dc
---

# Review

Most of the note's mechanistic sentences identify their mechanism at the right level. Examples are the cost of the grounding check as the number of unquoted artifacts to search, a review-side budget failing silently, and the evidence from occurrence versus representativeness. The note also scopes itself to the grounding check and says the unit would need to be re-derived for any other check. That avoids the main generality risk for this gate.

The warning concerns the reinterpretation of the paired experiment. It assigns detection of a missing retained passage to the validator, but the validator only checks quotations that are present. Under an artifact-side bound, the absence is prevented when the author has to quote. It is not detected by a validator. The two info findings concern emphasis: present-tense wording for a validator that the Scope section says is undecided, and checker-relative framing for a Descartes quotation that sizes parts to the solution.
