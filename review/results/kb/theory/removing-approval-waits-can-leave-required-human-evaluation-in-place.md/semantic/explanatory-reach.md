---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: d155a6ea644e43e9abfa39b7f9c0a531
completed-at: '2026-11-18T16:03:42Z'
findings: []
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/e54f86ac301fe68352fd173e/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/e54f86ac301fe68352fd173e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/d155a6ea644e43e9abfa39b7f9c0a531/outputs/review-explanatory-reach.md
raw-output-sha256: 70bbf1f6c5eaa42323b49e3cfa26dfab16f19c7fc01efa6a36225af785a99ff8
---

# Review

## Summary

The central claim is that removing an approval wait can leave required human evaluation in place. The mechanism is that the two live in different places. A wait is a blocking dependency in execution control. A required evaluation is an assignment in the process specification. Removing one therefore does not remove the other. The weekly-review example shows this directly: adoption proceeds when the maintainer does nothing, while the specified review goes undone.

Varying a premise changes the conclusion. If the specification were defined as exactly what execution enforces, removing the wait would retire the requirement, and the claim would fail. The note's argument depends on those two layers being separable, so the explanation is load-bearing. The same mechanism also predicts the revision-process case: a required assessment becomes a dependency of revision but not of the earlier adoption. That is an extension, not an ad-hoc addition.

The claim is falsifiable in the relevant sense. A process in which removing every human wait necessarily discharged every human requirement would contradict it. The Scope qualifications sharpen the distinction rather than shielding it: they exclude non-intervening influence and classify a habitual wait as an actual wait. None of them protects the claim from a counterexample without explanation.
