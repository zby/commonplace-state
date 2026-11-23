---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  - It does not tell the reviewer which earlier failure bears on the page at hand.
  reason: 'The title makes the rule ("it") the thing that must identify when a lesson
    applies. The body says the instruction does not tell the reviewer which earlier
    failure bears on the page, and that the reviewer does the recognizing. On the
    title''s literal reading, the rule does not identify applicability and so cannot
    use new lessons. The body concludes the opposite: the unchanged rule still works
    through the reviewer. Either "it" refers to the review or the reviewer rather
    than the rule, which is a shift, or the title contradicts the body.'
  level: warn
- scope: passage
  quotes:
  - The incident shows what the review must distinguish, not that the review rule
    must change.
  reason: The closing sentence says the rule need not change. A title read as a requirement
    on the rule (the file slug says rules "must identify") suggests the rule needs
    a capability or content it currently lacks. Read together, the title and the conclusion
    point in opposite directions about whether the rule itself must do more.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/07bf6c6e9d4576fd6d018fff/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 3d5f3f82607d4baab0a730a410af81c8
completed-at: '2026-11-23T11:41:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/outputs/review-internal-consistency.md
raw-output-sha256: dde646de8b2fab41d7664f26ab7c4149a9a07f7ae8df11c630babba63a77aab3
format: 2
---

# Review

## Summary

The body is consistent within itself. The instruction supplies a location, the reviewer supplies recognition of applicability, and so the rule can stay fixed. The title places the identification requirement on the rule. Read literally, that contradicts the body's point that the rule does not say which failure bears on the case and still does not need to change. The likely intended reading is "the review applying it", but the text does not say so, and the agent of identification drifts from the rule to the reviewer between the title and the body.
