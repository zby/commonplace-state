---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 6c3ee52530d64420814f235b9966e3ed
completed-at: '2026-11-18T16:02:15Z'
findings: []
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/9adf8e9ed09396af22a6a5af/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/9adf8e9ed09396af22a6a5af/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/6c3ee52530d64420814f235b9966e3ed/outputs/review-general-before-specific.md
raw-output-sha256: 84ec89c81ac6e0e735ed19f208f7743d7594c217fc291d2f79fc9e7e3a45c310
---

# Review

The note's sections, in order, are an untitled introduction, "The same activity can perform different roles", "Name the process being automated" and "Scope".

The introduction states the general distinction: removing an approval wait differs from removing a specified evaluation task, and optional assessment is neither. It also defines blocking dependency and unfulfilled requirement. The general rule therefore comes first.

"The same activity can perform different roles" gives two hypothetical cases that illustrate the distinction already stated. "Name the process being automated" follows it. That section opens with another example, but it develops a further consequence: a claim of automation must name which tasks remain and what changed. It does not state the general rule that the preceding cases exemplify, so this adjacent pair is not specific-before-general. "Scope" adds boundary conditions after the main argument, which is the expected order.

No adjacent pair puts a specific case before the general statement it exemplifies.
