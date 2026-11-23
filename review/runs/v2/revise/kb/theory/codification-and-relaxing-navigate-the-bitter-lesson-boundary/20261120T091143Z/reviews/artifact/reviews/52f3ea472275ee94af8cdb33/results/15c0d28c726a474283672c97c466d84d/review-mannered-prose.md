---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - seen from the author's side rather than the survivor's
  reason: 'Intended literal meaning: the same property, viewed when a codification
    is committed rather than in hindsight after scaling has shown which method held
    up. ''The survivor''s'' side makes the reader work out who the survivor is (a
    method? an observer of the surviving method?). It also imports a selection-and-survival
    connotation, and the next sentence says that selection is only conjectural. Literal
    replacement: ''seen at commitment time rather than in retrospect after scaling.''
    This removes the translation step and the implied selection mechanism.'
  level: warn
- scope: passage
  quotes:
  - The vision researchers made this bet at maximum disadvantage.
  reason: INFO only. 'At maximum disadvantage' is mild idiom. The next sentences state
    its literal content (no working system to extract from, no evidence that the pieces
    compose), so the reader is not left to translate it. 'Without any working system
    to extract from' would be as clear, but this is a preference rather than a defect.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/52f3ea472275ee94af8cdb33/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 15c0d28c726a474283672c97c466d84d
completed-at: '2026-11-20T09:13:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-mannered-prose.md
raw-output-sha256: 5fb8bbfd5783458a55786940d46c15adce3b02922c7db4a850f53a8de9e703da
format: 2
---

# Review

## Summary

The note's main figure is "bet." It is an explanatory mapping that the note uses: codification commits to an extracted regularity under uncertainty. Later passages develop that mapping with "safe" versus "risky" bets, a "narrower bet with better odds" for spec mining, and "a losing bet" detected by relaxing signals. It structures the argument, so it passes. "Blurry zone," "trajectory" and "stack" are conventional and precise enough.

One phrase meets the test. "The survivor's" side is less clear than a literal time-of-judgment contrast. It also introduces a selection connotation that the note itself marks as unestablished. The finding is local and does not obstruct reading the note as a whole.
