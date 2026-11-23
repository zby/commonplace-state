---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: b8f1f7f1daec40c8abca19e626134cf2
completed-at: '2026-11-22T21:52:38Z'
findings:
- scope: passage
  quotes:
  - Form placement is itself revisable. A stable natural-language rule may be codified,
    while a brittle symbolic rule may be relaxed back into prose
  reason: Minor branch. Moving a lesson between forms later extends the form-placement
    point from the previous paragraph. It does not help define governance as choosing,
    validating, authorizing and coordinating writes. Placed here, it separates the
    definition of governance from the selection argument that follows. The linked
    codification-and-relaxing note already covers it. Move it into the form paragraph
    or leave it to the footer link; either works, and neither is required.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/b8f1f7f1daec40c8abca19e626134cf2/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/4de91ba774efddfaf34009f5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/b8f1f7f1daec40c8abca19e626134cf2/outputs/review.md
raw-output-sha256: d576f90725aaa6b8616897979c0d6d435492b632245223a052a00e65fee0d118
---

# Review

## Summary

The main claim is that continual learning in a deployed system requires governing behaviour-changing writes. Governing means selecting, validating, authorizing and coordinating those writes; persistence alone is not enough. Most of the side material makes this claim stronger or sets its limits:

- **Knowledge artifacts, system-definition artifacts and behavioral authority** supply the premise that storing something does not decide whether it changes behaviour.
- **The deployment constraints**, cheap installation and validation against regression, explain why the select and validate steps are needed.
- **The concession about parametric plasticity and stability** answers an obvious objection, so it stays.
- **The three-form passage** supports coordination across forms and leaves the wider trade space to the coevolution note, so the branch has already been moved out.
- **The contrast between maintenance and continual learning** sets the boundary for "the system does the selecting itself," which the governance definition depends on. It is somewhat long, but it is a needed boundary condition, not a branch.
- **The closing sentence** says storage, activation and parametric adaptation remain subproblems. It limits the claim instead of opening a new one.

The one marginal branch is the remark that form placement can be revised later, noted in the finding. It is short and has a home elsewhere, so it does not weaken the main claim enough to warrant a WARN.
