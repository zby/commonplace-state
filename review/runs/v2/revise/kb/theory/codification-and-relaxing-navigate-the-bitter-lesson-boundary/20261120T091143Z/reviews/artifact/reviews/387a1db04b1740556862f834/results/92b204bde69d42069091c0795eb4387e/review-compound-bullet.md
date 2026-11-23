---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Merely writing the convention in natural language constrains without codifying
    it.
  reason: 'Heuristic 1 is about codifying for current leverage rather than permanence,
    and its examples contrast the arithmetic regime with the vision-feature regime.
    Its final sentence makes a separate claim: prose conventions constrain without
    codifying. That claim marks the boundary of the term codification and does not
    support the leverage-versus-permanence point. It could stand as its own item or
    move to the definitional paragraph in the trade-off section, where it would not
    be buried at the end of an unrelated heuristic.'
  level: warn
- scope: passage
  quotes:
  - it conjectures what may determine the outcome without establishing it or restoring
    the foresight this note denies
  reason: This Relevant Notes item uses a semicolon to join the relation gloss with
    a second, hedging point about the target's epistemic status. The hedge qualifies
    the grounding relation, so it is borderline elaboration rather than a fully independent
    claim. It is still long enough that the caveat is easy to miss while scanning.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/92b204bde69d42069091c0795eb4387e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/387a1db04b1740556862f834/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 92b204bde69d42069091c0795eb4387e
completed-at: '2026-11-20T09:13:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/92b204bde69d42069091c0795eb4387e/outputs/review-compound-bullet.md
raw-output-sha256: 9f9a40bf4cc1e1f4023d7ca3d4e9f9e278c911cd7c1cbe70012c683567e62536
format: 2
---

# Review

## Summary

Most long list items develop a single idea. The arithmetic-regime bullet ends with a semicolon caveat about economic cost. That caveat qualifies its own claim that reliability, speed and cost can improve, so it counts as elaboration. The vision-feature bullet states one idea and its consequence. Heuristics 2 and 3 each state a rule followed by its rationale or an example. The Sources entries pair a source summary with what it grounds.

Heuristic 1 is the clear compound item. Its last sentence introduces a separate boundary claim about what counts as codification. That sentence sits after examples about a different point, so a reader scanning the heuristic would miss it. The footer item that glosses the unsupported-proxy-scope note also carries a semicolon-joined hedge. That hedge is recorded as INFO because it qualifies the relation rather than adding an unrelated point.
