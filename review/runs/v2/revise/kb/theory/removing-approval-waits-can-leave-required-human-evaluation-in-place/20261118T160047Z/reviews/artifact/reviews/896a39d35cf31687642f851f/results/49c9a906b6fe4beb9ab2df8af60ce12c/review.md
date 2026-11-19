---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/896a39d35cf31687642f851f/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/896a39d35cf31687642f851f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 49c9a906b6fe4beb9ab2df8af60ce12c
completed-at: '2026-11-18T16:02:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/49c9a906b6fe4beb9ab2df8af60ce12c/outputs/review.md
raw-output-sha256: 352677e924d1f141d2be6cb7d92fe5db6e4d86cfc922f54cb303bda6d9434704
format: 2
---

# Review

## Core claim

Stated in one sentence from the note's own commitments: removing a human approval wait is a different change from removing a specified human evaluation task, so a claim of full automation must say which required tasks it keeps and which it retires.

## Prominence

The title states the claim, and the first sentence of the body restates it plainly: "Removing a human approval wait and removing a specified evaluation task are different changes." The rest of the opening paragraph adds the practical consequence: an automation claim must account for the tasks it preserves and the requirements it retires. It also sets aside the question of whether those tasks are useful. A reader can state the claim after the first paragraph.

## Subordination of later material

- The second paragraph defines the two terms the claim depends on: an actual wait is a blocking dependency, while an undone specified task is an unfulfilled requirement. It also places optional assessment outside both. This is the vocabulary the claim needs, not setup that comes before it.
- The third paragraph compares this note with the linked note on comparing operative states. It is short and comes after the claim, so it does not delay the claim.
- "The same activity can perform different roles" contrasts required approval with optional assessment. Both cases illustrate the distinction stated at the top.
- "Name the process being automated" applies the claim to monitoring and revision. It ends by restating the prescription in concrete terms: say what still requires a person, and treat retirement as a change in requirements.
- The Scope bullets set the claim's boundaries and do not compete with it.

No caveat, analogy or related-note material comes before the claim or competes with it. The structure meets the criterion's pass example: the claim comes first, and definitions, cases and scope limits follow in support.
