---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - its extra words give the person facing the error a repair that works
  reason: 'This frames the newer diagnostic''s advantage as its extra words. The mechanism
    the paragraph describes is what those words say: they name the local file that
    hides the standard-library module and suggest renaming it. A longer message without
    that identification would not give the repair. The framing points the reader toward
    length rather than content. It does not exclude any case, so this is INFO.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/7d27f8061213d5ce3a01f381/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 262edf34947f4789926811e68630a6b3
completed-at: '2026-11-20T18:54:22Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/outputs/review-framing-mismatch.md
raw-output-sha256: 54bf78c5c4ed05c5fa2e7b7cbd21bff07ffab71db48a32d7a0cff52481b100af
format: 2
---

# Review

## Summary

Most sentences that give reasons or mechanisms are framed at the right level. Examples:

- "Use of a new instruction shows uptake, not a gain."
- "A more precise timing result will not make a broken dependency run."
- The library-hours case states that its scope is hypothetical and says what transfers from it.
- "Analysis can expose that trade-off; it cannot supply the weights merely by assigning each feature a score" correctly places the limit in value-weighting, not in measurement.

The one weak framing is minor: the CPython 3.13 diagnostic is credited to its "extra words" when its benefit comes from naming the shadowing file. It changes emphasis but does not narrow the claim.
