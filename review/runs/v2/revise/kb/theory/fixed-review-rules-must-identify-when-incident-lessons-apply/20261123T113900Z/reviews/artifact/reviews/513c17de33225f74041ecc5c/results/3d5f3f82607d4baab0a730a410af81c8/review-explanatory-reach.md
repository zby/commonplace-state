---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: 'As worded, the central claim is close to analytic: a lesson cannot be applied
    without telling when it applies. No observation could contradict it, so it forbids
    almost nothing. The substantive part is in the body, not the title: the instruction
    supplies only where to look, and recognizing applicability depends on a structural
    feature (shared origin plus reliance on independence), not on surface identifiers.'
  level: warn
- scope: passage
  quotes:
  - A reviewer following the original instruction could still recognize it.
  reason: This sentence carries the note's conclusion that the rule need not change,
    but it gives no mechanism for recognition. It does not say what the reviewer must
    already hold, such as the concept of independence, or when recognition would fail.
    The note therefore states no condition under which a fixed rule would stop being
    enough. Varying what the reviewer knows leaves the sentence equally plausible.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/513c17de33225f74041ecc5c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 3d5f3f82607d4baab0a730a410af81c8
completed-at: '2026-11-23T11:41:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/outputs/review-explanatory-reach.md
raw-output-sha256: 5b9197ded45a24ee78275d31d4e0fd6b290980b8a10c908f16caf080faf7fc8d
format: 2
---

# Review

## Summary

The note has a partial mechanism. The instruction names a location, not relevance, and a lesson transfers through a structural feature that a lookup by name would miss. The second point is constrained and testable. However, the title's "only if" is nearly true by definition, so it adds little content. The body's main move, that a reviewer following the unchanged rule "could still recognize" the lesson, does not say what makes recognition possible or what would make it fail. Without that, nothing in the argument says when an incident would show that the rule must change. The closing sentence's contrast is therefore not hard to vary.
