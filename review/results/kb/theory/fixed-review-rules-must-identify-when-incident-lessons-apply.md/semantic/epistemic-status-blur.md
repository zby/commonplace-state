---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 8cb1ad7dbf18f84e88042c601bd955e4265ba65f26de48e2402ad716359e9d11
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 3d5f3f82607d4baab0a730a410af81c8
completed-at: '2026-11-23T11:41:41Z'
findings:
- scope: passage
  quotes:
  - can remain the review rule even as new incidents accumulate
  reason: The opening states that the fixed instruction can stay unchanged. This is
    declarative, and its only support is the constructed example that follows. The
    modal "can" and the explicit "Suppose" let a reader tell that this is an argued
    possibility, not an observed result. The status can be recovered, but only by
    reading ahead.
  level: info
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/751241c3fb7f9b827c6f5927/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/outputs/review-epistemic-status-blur.md
raw-output-sha256: fd78d14a23270645bf16fddf14a6b1ae79bc7818da34e3f1c4dc209b940234dc
---

# Review

## Summary

The note's material claims are an argued claim that the instruction gives a location, not relevance, plus a hypothetical example and a conclusion drawn from it. The example is plainly marked "Suppose". Its consequences use modal wording ("would miss", "could still recognize"). The note presents no observation, measurement or reported incident as evidence, so no hypothetical takes on the confidence of real evidence. The opening sentence is stated before its illustrative support. This is a minor recoverability issue, not blur.
