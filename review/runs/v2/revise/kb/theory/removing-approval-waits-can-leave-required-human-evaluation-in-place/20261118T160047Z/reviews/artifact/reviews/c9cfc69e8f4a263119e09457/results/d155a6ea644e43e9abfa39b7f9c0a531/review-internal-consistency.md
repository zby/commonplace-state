---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/c9cfc69e8f4a263119e09457/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/c9cfc69e8f4a263119e09457/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: d155a6ea644e43e9abfa39b7f9c0a531
completed-at: '2026-11-18T16:03:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/d155a6ea644e43e9abfa39b7f9c0a531/outputs/review-internal-consistency.md
raw-output-sha256: 120b4b814dd0d345559538d76b2bde3031daffa9b35ebace14b52c42b372e410
format: 2
---

# Review

## Summary

Key claims by section:

- **Opening:** removing a wait and removing a specified evaluation task are different changes. Optional assessment is neither a blocking dependency nor an unfulfilled requirement. Usefulness and necessity are separate questions.
- **The same activity can perform different roles:** a required approval is a dependency even when always granted. Optional assessment has nothing depending on it. A non-binding recommendation creates a dependency if execution waits for it.
- **Name the process being automated:** a specified review can go undone while adoption continues. Revision-time assessment is a dependency of revision, not of adoption. Retiring a review changes requirements; it does not automate the review.
- **Scope:** the distinction is about required intervention, not influence. A habitual wait is an actual wait, not evidence of a requirement.

No pair contradicts. The terms stay stable. "Actual wait" or "blocking dependency" always means execution cannot proceed. "Specified task" or "requirement" always means an assignment in the process specification. "Optional assessment" is consistently defined by having neither property. The title's "required human evaluation" matches the body's "specified evaluation task", because the body treats "specified" as "required by the specification" throughout. The description's statement that optional assessment "need not be part of either change" matches the opening's "Optional assessment creates neither". The opening's "Whether a specified task is useful or necessary is a separate question" agrees with the later "Retiring an unnecessary review may be justified, but it is a change in requirements".
