---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 629582306dfe4cdea84751e99e0d5dd4
completed-at: '2026-11-18T16:02:44Z'
findings:
- scope: passage
  quotes:
  - the comparison of a system before and after an adopted change
  reason: The link text describes a general before-and-after comparison of any system,
    while the target is specifically about software factories compared under requirements
    declared before development. The reader still finds the expected predecessor-versus-adopted-successor
    comparison, so the generalization does not mislead about what the link supports,
    but the factory scope and antecedent assessment relation are not signalled.
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/8136f12e01d1262540b16b00/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/8136f12e01d1262540b16b00/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/629582306dfe4cdea84751e99e0d5dd4/outputs/review-misleading-link-text.md
raw-output-sha256: 9f507096af71717a0f6c5d242d0d43d4912af85a162b902ae494ac0860967818
---

# Review

## Summary

Both links resolve, and each target matches the expectation its link text sets.

- "routine approvals do not establish that human judgment is dispensable" paraphrases the target's title, "Routine approvals do not show that human judgment is dispensable", and the target's opening supports the sentence's use: repeated acceptance does not settle whether a check can be dropped.
- "the comparison of a system before and after an adopted change" leads to a note comparing a predecessor with an adopted, operative successor. The target's head matches the core expectation; the link text is broader than the target's factory-specific framing, noted at INFO.
