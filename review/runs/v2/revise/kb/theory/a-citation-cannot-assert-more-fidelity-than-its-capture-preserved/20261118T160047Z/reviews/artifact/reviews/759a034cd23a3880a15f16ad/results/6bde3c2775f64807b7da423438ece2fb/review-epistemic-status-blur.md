---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Judging support is costlier and noisier
  reason: A comparative, empirical-sounding claim stated declaratively without evidence.
    Its status is recoverable as a consequence derived from the adjacent premise (wording
    agreement is deterministic; support requires a reader of both texts), and the
    same sentence marks the related reliability question as unmeasured, so the calibration
    holds; the derivation is left for the reader to reconstruct.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: c4a5001c550b584b637412bf2b1c91bb2d0028bbea7478f1ec662d8d36a9e63b
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/759a034cd23a3880a15f16ad/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/759a034cd23a3880a15f16ad/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-epistemic-status-blur.md
raw-output-sha256: df976df92535928f6b89fdf6905a7c42d5f38fac497c9e8c18127f3d72a74ada
format: 2
---

# Review

The note's material claims carry recoverable statuses.

- Observations are attributed and scoped: the casebook mismatch profile is "in one casebook corpus" and tied to ADR 046; the judgment that false mismatches are worse than no check is presented as ADR 046's judgment ("judges"), not as a measured result.
- The severity choice is framed as a choice within the cost/reliance trade-off, "not a universal rule".
- The four-question decomposition is the note's own qualitative construction, presented as separable questions a citation raises; it needs no heavier proposing language.
- Derived consequences (uniqueness does not establish intent; a pass is relative to the evidence used; missing bytes cannot pass) follow from stated premises and read as derivations.
- Unmeasured quantities are marked as such: support-judging reliability and the rate of unrecognized quotations. Transfer beyond agent-operated KBs is explicitly said to rest on reasoning, not external evidence.

No support is spread from one claim to another, and no well-supported finding is hedged without reason. The one INFO concerns a comparative left for the reader to derive.
