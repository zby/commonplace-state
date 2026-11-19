---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Whether approval was required for that adoption is a fact about the process.
  reason: 'The mechanism is control of the adoption gate. Requiring approval makes
    the judgment part of the process that selects the revision. That mechanism is
    constrained: if approval is not required, the conclusion fails. But the note treats
    requiredness as enough for causal contribution and does not say what makes control
    causal. Consider a required approval that would have been granted for any proposal,
    such as a rubber stamp. It meets the requiredness criterion, yet the judgment
    did not discriminate among proposals. The note does not say whether such a judgment
    helps determine which system results. Because the counterfactual sensitivity of
    the judgment is left unstated, the mechanism is plausible but thin.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/a0a05fd422257978678d0f68/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/a0a05fd422257978678d0f68/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 388f012ff0b54165ac3ed49bf5e4359d
completed-at: '2026-11-17T07:22:54Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/388f012ff0b54165ac3ed49bf5e4359d/outputs/review-explanatory-reach.md
raw-output-sha256: dc67d6f2900a3c62ac66440d8fb464475fea49da2b800bb31cada60a38528869
format: 2
---

# Review

## Summary

The central claim is that evaluation which controls adoption helps determine the change. The note grounds this in a mechanism: a judgment that gates entry into use is part of the selection process. A judgment made after adoption controls only later transitions, such as a rollback or a further revision. The mechanism is not easy to vary. Removing the requirement for approval, or moving the judgment after adoption, changes the conclusion, and the note shows both variations.

The claim can fail. An account could show a case where required approval did not shape which revision entered use. The note's Scope caveats about quality, learner membership and other influence narrow what the distinction establishes. They are not escape hatches that protect it from counterexamples.

The only weakness is that requiredness stands in for causal control without a stated counterfactual condition. That is recorded as INFO.
