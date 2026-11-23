---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 59b2184d43be444e9fae7bfff674a087
completed-at: '2026-11-20T09:12:46Z'
findings:
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
  - (κ = 0.28 for CoT)
  reason: The note uses the sharing factor κ without defining it or saying which direction
    is good. 'κ ≈ 1 or κ < 1' covers nearly every value and discriminates nothing
    for the reader. Deleting both κ expressions leaves the passage's meaning unchanged,
    since the prose already says the models learn length-specific solutions in isolation
    and that diversity hurts. A reader cannot use the notation to make a prediction
    or derive a consequence, so it lends quantitative appearance without doing formal
    work. Either define κ and its threshold, or drop the notation.
  level: warn
- scope: passage
  quotes:
  - separates information into time-bounded entropy (irreducible randomness) and epiplexity
    (learnable structure within computational bounds)
  reason: 'The two-way entropy/epiplexity decomposition yields only one rule: codify
    high-epiplexity regularities and distrust low-epiplexity ones. The note never
    ties this vocabulary to its own arithmetic/vision-feature regimes or to the heuristics,
    and it gives no way to estimate epiplexity for a candidate codification. A sentence
    such as ''codify learnable structure, not regularities that may be artefacts of
    current scale'' carries the same guidance. This is mild, because the framework
    is attributed to a source rather than presented as the note''s own.'
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/59b2184d43be444e9fae7bfff674a087/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/1b6260234a5d5b64588675d0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/59b2184d43be444e9fae7bfff674a087/outputs/review-framework-decoration.md
raw-output-sha256: 54cb81a39ca75efb30b877e2c341c4ebe0dcefd66f3dd3ef8cda361d00a4e40d
---

# Review

## Summary

Four structures were checked.

- **Arithmetic-regime / vision-feature dichotomy** (bullet pair): load-bearing. It drives the generality-loss boundary condition, the bet framing, the spec-mining argument and heuristic 1. Each category supports a different decision.
- **Numbered working heuristics**: these are decision rules with discriminating examples, not decoration.
- **Epiplexity decomposition**: largely reducible to one sentence and unused after its paragraph (info).
- **κ notation in the induction-bias paragraph**: decorative in its current form (warn), because it is undefined and carries no information the surrounding prose does not.
