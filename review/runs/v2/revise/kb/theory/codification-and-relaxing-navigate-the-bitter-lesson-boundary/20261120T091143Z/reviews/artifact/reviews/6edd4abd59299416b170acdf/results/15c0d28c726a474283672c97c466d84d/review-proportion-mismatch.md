---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Most practical codification happens in the blurry zone between them, where you
    can't tell which regime you're in.
  reason: INFO. The note's premise is that the regime cannot be identified until scale
    tests it. That premise gets one sentence here and one clause in the opening. The
    two formal-results paragraphs give more space to the clear-cut arithmetic case
    (induction bias) and to a general safety criterion (epiplexity) than to the ambiguous
    zone where the heuristics actually apply. The imbalance is modest, because spec
    mining, relaxing signals and the heuristics all address the ambiguous case.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/6edd4abd59299416b170acdf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 15c0d28c726a474283672c97c466d84d
completed-at: '2026-11-20T09:13:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-proportion-mismatch.md
raw-output-sha256: 8ddb41204bfa095c59c2938866b7936fce632534da258facc3c41af5b6a0ad46
format: 2
---

# Review

## Summary

Core claim, from the title and description: the regime cannot be known in advance, so practical systems should codify and then relax, and spec mining lowers the risk of a vision-feature-style failure. The supporting parts are proportioned reasonably. Relaxing gets a definition paragraph, a bidirectional-trajectory paragraph, a signals paragraph and three heuristics. Spec mining gets two paragraphs that develop the narrower-bet argument. The first section's scoping of code-extraction codification is long. It still serves the claim, because it fixes what relaxing reverses.

The one soft spot is the INFO finding: the evidence paragraphs strengthen the safe end of the spectrum more than the ambiguous middle the note is about. No secondary section outweighs the core argument enough to justify splitting it out.
