---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 388f012ff0b54165ac3ed49bf5e4359d
completed-at: '2026-11-17T07:22:54Z'
findings:
- scope: passage
  quotes:
  - An evaluator who controls whether a proposed change enters use helps determine
    which system results.
  reason: 'The phrase ''helps determine'' is the note''s central assertion, and two
    readings fit it. Under a structural reading, the judgment is a required step in
    the adoption process, so any required approval counts as a contribution to selection.
    Under a counterfactual reading, the judgment contributes only if a different verdict
    would have changed which revision entered use, so a rubber-stamp approval would
    not count. The note''s later criterion (''Whether approval was required for that
    adoption is a fact about the process'') points toward the structural reading.
    But the word ''controls'' and the stated purpose of explaining an improvement
    point toward the counterfactual one. The choice is material. It changes the evidence
    needed: a process description versus a record that the judgment discriminated,
    such as rejections or changes made in response. It also changes the outcome of
    the note''s intended use, which is deciding whose contributions explain an improvement.
    A required approval that never discriminates is credited under one reading and
    not under the other.'
  level: warn
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/3ea13d05652d011580b91db3/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/3ea13d05652d011580b91db3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/388f012ff0b54165ac3ed49bf5e4359d/outputs/review-underspecified-assertions.md
raw-output-sha256: 488c6efc3a9505ad14dbc42279f5273108316101515230e06aff60b743717580
---

# Review

## Summary

Most assertions are precise. The note fixes the change and decision being examined. It defines adoption by reference to operative change. Its Scope states what the distinction does not establish.

The one material ambiguity is the causal sense of "helps determine". It is unclear whether controlling adoption means the judgment is a required step, or that its verdict made a difference. The two readings require different evidence, and they credit a non-discriminating required approval differently. Since attributing contributions to an improvement is the note's stated purpose, the choice is load-bearing.
