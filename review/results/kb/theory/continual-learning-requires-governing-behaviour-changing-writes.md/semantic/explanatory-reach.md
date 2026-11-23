---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:05Z'
findings:
- scope: passage
  quotes:
  - A behaviour-changing write counts as continual learning when the system's own
    loop selects and retains it
  reason: Part of the central claim is closed by definition. Once continual learning
    is defined as writes the system's own loop selects, 'continual learning requires
    selecting writes' follows trivially and no observation could contradict that half.
    The non-trivial part (validation, authority assignment, coordination) still rests
    on the consumption-path and regression arguments, so the mechanism is present
    but thinner than the title suggests.
  level: info
- scope: passage
  quotes:
  - because continual adaptation compounds silent degradation
  reason: The validation requirement rests on a one-clause mechanism that names no
    route by which degradation stays silent or compounds. It is plausible, but it
    does not constrain when regression validation would be unnecessary, for example
    for writes whose authority path is tightly bounded.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/f6c108965fa1c635a5aafe40/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-explanatory-reach.md
raw-output-sha256: 8be54b22bd1db96cefc381d718f0d8a83a211aeb3aa8424020500f4fc7f53f35
---

# Review

## Summary

The central claim has a real, hard-to-vary mechanism in its first paragraph. Stored bytes carry no behavioral authority of their own; authority comes from a consumption path. So persistence cannot decide which item shapes behaviour or how strongly, and some further selecting and authorizing act is needed. Varying the premise changes the conclusion: if every stored item were automatically consumed with fixed force, storage would itself be a behaviour-changing write. The claim is falsifiable at that joint.

The weaker parts are the validation requirement and the system-selects criterion for continual learning. The validation requirement carries a one-clause mechanism. The criterion makes part of the title true by definition. Neither escape hatch is ad hoc, so the result is INFO, not WARN.
