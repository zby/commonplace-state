---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/e6c303af994a4bb3d233481a/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/e6c303af994a4bb3d233481a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 629582306dfe4cdea84751e99e0d5dd4
completed-at: '2026-11-18T16:02:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/629582306dfe4cdea84751e99e0d5dd4/outputs/review-framing-mismatch.md
raw-output-sha256: eab14de82b9df5e8515892632b6e6dce16689281550d1147d78869e5c3e4e520
format: 2
---

# Review

## Summary

The mechanism sentences frame their claims at the generality of the mechanism. The core distinction is stated in general terms: an actual wait "prevents execution from proceeding until a person acts", while a specified task "can remain undone while execution continues". The examples (written procedures for an agent, weekly sample review, rollback) are explicitly hypothetical illustrations and do not restrict the claim to agent instructions or to monitoring. The opening's "monitoring or later revision decisions" is introduced with "may" as an instance, not as the boundary of the distinction.

The note also guards against the narrower or wider misframing a reader might bring: it separates "Calling an activity evaluation" from whether execution waits for it, separates "a non-binding recommendation" that still blocks from human-authored rules that do not, and scopes the habitual-wait case as "an actual wait to remove, not evidence that the evaluation is needed". No sentence names a domain or cause that excludes cases the mechanism covers.
