---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: 'For the title''s "only if", "fixed" and "new" fail the deletion test. Any
    rule, fixed or revised, can use any lesson only if applicability can be identified.
    The qualifiers matter to the body''s other point: a rule written before the incident
    cannot have encoded its lesson, so identification moves to the reviewer. A boundary
    may depend on them, but the title''s stated claim does not use them.'
  level: info
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: '"Review" narrows the claim to publication review. The argument (an instruction
    names where to look, not which past case bears on the present one) appears to
    apply to any standing instruction that consults past cases. This looks like intentional
    domain scoping to KB review, so it is INFO.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: 8cb1ad7dbf18f84e88042c601bd955e4265ba65f26de48e2402ad716359e9d11
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/2cdfd81d1d7eb44533f0f44d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 3d5f3f82607d4baab0a730a410af81c8
completed-at: '2026-11-23T11:41:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: 5e72b0ceaadcdd3c5e166f475e6486a018383e6c90e70f8210211d3fef02fa44
format: 2
---

# Review

## Summary

The title's qualifiers are "fixed", "new" and "review". The deletion test suggests that the bare "only if" holds without "fixed" and "new". The note uses them to motivate why identification falls to the reviewer, so a hidden boundary may depend on them. The reviewer cannot rule that out, so this stays INFO. "Review" looks like deliberate domain scoping. No qualifier clearly narrows the central claim without doing work, so the gate passes.
