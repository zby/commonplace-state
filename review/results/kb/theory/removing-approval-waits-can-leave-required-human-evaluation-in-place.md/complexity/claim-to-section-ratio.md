---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: e4430f090da04e1997080ccf89c99475
completed-at: '2026-11-18T16:01:41Z'
findings: []
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/90afd08577dc16305c4e8345/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/90afd08577dc16305c4e8345/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/e4430f090da04e1997080ccf89c99475/outputs/review-claim-to-section-ratio.md
raw-output-sha256: c3c874472475260030eae75c0c0972ec883b320c3db7834030b706ed42a0cb58
---

# Review

## Summary

The note has more distinct non-obvious claims than sections, and each section extends the argument rather than restating it.

## Claims and sections

Distinct non-obvious claims:

1. Removing a human approval wait differs from removing a specified evaluation task. A claim of full automation must therefore say which tasks it keeps and which requirements it retires.
2. An actual wait is a blocking dependency. A specified but undone task is an unfulfilled requirement, which does not by itself show harm. Optional assessment creates neither.
3. The same activity (examining results and forming a verdict) can be a required wait or an optional study. The label "evaluation" does not decide which. A non-binding recommendation can still block, and human-authored rules applied by a program need no new human judgment per change.
4. Dependency is relative to a process. A required assessment before each revision is a dependency of the revision process, not of the earlier adoption. Using an optional study's findings does not make future studies required.
5. Retiring a review changes the requirements; it does not automate the review.

Sections: the unheaded opening, "The same activity can perform different roles", "Name the process being automated" and "Scope". That makes four units for at least five claims. The opening states claims 1–2. The roles section carries claim 3 through its two contrasting cases. The process section carries claims 4–5 and the weekly-review gap example. Scope supplies two boundary conditions, anticipated influence and habitual unwritten waits, that the earlier sections do not cover. The second and third paragraphs of the opening overlap a little with the first, but they add the blocking-versus-unfulfilled mechanism and the relation to the operative-states note, so they are not restatement.
