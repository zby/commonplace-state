---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A non-binding recommendation still creates a dependency if the agent must wait
    for it.
  reason: The title restricts the claim to 'approval' waits, but the mechanism (execution
    control versus specification) uses no property of approval. The body itself counts
    waits for non-binding recommendations and habitual waits for human input as actual
    waits. Deleting 'approval' ('Removing human waits can leave required human evaluation
    in place') leaves the argument unchanged. The narrowing is probably intentional
    domain framing, since approval stops are the motivating case and the linked routine-approvals
    note uses the same framing, so this is INFO rather than WARN.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: dddfe82e0c4eb506a7b324a47fa166f4e5ac505a98c1b75fb1964a3b564259ac
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/5f7219f588e41ac26a54648f/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/5f7219f588e41ac26a54648f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: d155a6ea644e43e9abfa39b7f9c0a531
completed-at: '2026-11-18T16:03:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/d155a6ea644e43e9abfa39b7f9c0a531/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: b701aafffabd7f0048ac7c6384d5e4127256833a42ba7c93411a9e839f325489
format: 2
---

# Review

## Summary

Qualifiers in the title, description, and opening are *approval* (wait), *required* (evaluation), and *human*.

- **Required** is load-bearing. The note's central contrast is between required evaluation and optional assessment. Without it, the claim would sweep in optional studies, which the note explicitly says create neither a dependency nor a requirement.
- **Human** is load-bearing for the note's purpose. The argument concerns claims of automation: whether a person is still needed. A program applying human-authored rules is explicitly excluded from requiring "a new human judgment for each change."
- **Approval** is not used by the mechanism, and the body generalizes past it (see the INFO finding). Because approval stops are the evident motivating domain, the narrowing reads as intentional framing rather than an unnecessary assumption inherited by readers. It does not warrant WARN.
