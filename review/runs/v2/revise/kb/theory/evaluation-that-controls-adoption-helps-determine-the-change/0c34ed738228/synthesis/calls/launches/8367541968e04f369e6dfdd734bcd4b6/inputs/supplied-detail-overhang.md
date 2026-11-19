---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 7b78d3aa8a2548979653ad2b75884e51
completed-at: '2026-11-17T07:21:42Z'
findings:
- scope: passage
  quotes:
  - A test available to the proposing system can be optimized without improving the
    capability it is meant to assess; human approval does not remove the need to justify
    the assessment.
  reason: 'This caveat brings in a second mechanism: the proposer can game a test
    it has access to. The bullet''s boundary, that approval does not establish quality,
    is already made by the two sentences before it. The sentence could become a short
    clause or be dropped. It is only one sentence, though, and it does warn the reader
    not to treat a test-backed approval as self-justifying, so compression is optional.'
  level: info
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/0e5c4338ed34c129a11b264c/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/0e5c4338ed34c129a11b264c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/7b78d3aa8a2548979653ad2b75884e51/outputs/review.md
raw-output-sha256: 21919fb6845546b3729a93afedfac8906fff6426882e4413fede82b204803212
---

# Review

## Summary

Most of the note's detail is proportional to the job it does. The two hypothetical cases are the note's main support. Each takes three sentences and differs from the other only in when the judgment happens, which is the contrast the claim needs. The follow-up paragraph says a later assessment can still cause a future revision or a rollback. That is a needed boundary: it stops readers from taking the claim to mean that a later assessment has no causal role at all. The section "One episode can contain both roles" is short and blocks the obvious escape of relabelling the whole episode. The adoption definition takes one sentence and points to the definition note instead of restating it.

## Borderline detail

The last Scope bullet adds a test-optimization caveat after the boundary is already made. It is long only compared with its role, and its cost is small, so it is reported as INFO rather than WARN.
