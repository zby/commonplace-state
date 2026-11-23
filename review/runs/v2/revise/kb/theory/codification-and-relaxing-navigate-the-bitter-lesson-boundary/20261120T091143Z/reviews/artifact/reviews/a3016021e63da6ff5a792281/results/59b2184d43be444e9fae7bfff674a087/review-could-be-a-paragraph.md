---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/59b2184d43be444e9fae7bfff674a087/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/a3016021e63da6ff5a792281/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 59b2184d43be444e9fae7bfff674a087
completed-at: '2026-11-20T09:12:46Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/59b2184d43be444e9fae7bfff674a087/outputs/review-could-be-a-paragraph.md
raw-output-sha256: a921d49d23d1c7b22c114b1168031485aae17d49487ea0ecf1f7b983b30f5dd6
format: 2
---

# Review

## Summary

Collapsing the note into one paragraph would lose several load-bearing elements:

- the regime-dependent account of what code extraction costs, with its boundary condition that arithmetic-regime decompositions lose no generality within declared scope;
- the definition of relaxing as reversing extraction rather than symbolic membership, with the adoption caveat;
- the bidirectional, multi-level trajectory examples;
- the inference that spec mining narrows the bet from "will pieces compose?" to "is this pattern load-bearing?", and the failure condition that it can still capture accidents;
- relaxing signals as the detector of a losing bet;
- two external results that bound when bets are safe;
- three distinct decision heuristics.

These are separate claims, support paths and failure conditions, not one simple insight with background around it. The multi-section structure is justified.
