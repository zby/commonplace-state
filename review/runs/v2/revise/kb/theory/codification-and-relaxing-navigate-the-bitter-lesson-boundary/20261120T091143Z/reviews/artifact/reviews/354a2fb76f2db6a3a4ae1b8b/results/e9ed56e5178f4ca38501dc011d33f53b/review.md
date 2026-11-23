---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
    — they learn length-specific solutions in isolation, with training diversity actively
    hurting (κ = 0.28 for CoT).
  reason: 'The paragraph''s job is one inference step: arithmetic-regime structure
    persists under scaling, so codification there is not merely safe-for-now. The
    κ values, the supervision-format sweep and the CoT figure are paper-internal measurements
    that the note never uses again; the reader needs only the finding that transformers
    fail to share solutions across lengths without the step-by-step bias. Compress
    this sentence to a short clause (e.g. ''transformers without that bias learn length-specific
    solutions that do not transfer'') and leave the numbers to the source.'
  level: warn
- scope: passage
  quotes:
  - 'This is not a partition into codified versus learned: an adopted model package
    can itself be a codified reference.'
  - Merely writing the convention in natural language constrains without codifying
    it.
  reason: 'The scope caveats on codification are stated where they do their work:
    the definition paragraph says prose retention is not codification and that model-package
    adoption is codification outside this case, and the relaxing paragraph says relaxing
    reverses extraction, not symbolic membership. These two sentences repeat those
    caveats in the opening and in heuristic 1 without adding a new boundary. Each
    recurrence keeps elaborating a caveat that has already done its job; cut them
    or fold each into a few words.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/compression-bundle/detail-overhang.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/compression-bundle/detail-overhang.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/e9ed56e5178f4ca38501dc011d33f53b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/354a2fb76f2db6a3a4ae1b8b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: e9ed56e5178f4ca38501dc011d33f53b
completed-at: '2026-11-20T09:15:15Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/e9ed56e5178f4ca38501dc011d33f53b/outputs/review.md
raw-output-sha256: 34d94032058a84ac23f5363336b606d098e70a7c1ee5309c2de38b812eee9cd4
format: 2
---

# Review

The note's core argument is proportionate: the arithmetic/vision-feature split, the relaxing complement, the "every codification is a bet" framing, the vision-researcher contrast and the spec-mining improvement each take roughly the space their inference step needs. The edge-detection / FlashAttention / tokenizer paragraph uses three brief examples to show that the trajectory runs both ways and repeats across levels; it is short and supports the "trajectory, not a law" claim, so it is not flagged. The epiplexity paragraph is about the right length for introducing an unfamiliar distinction.

Two details have outgrown their role. The induction-bias paragraph carries measurement specifics (κ values per supervision format) beyond what its single inference needs. The codification scope caveats (model-package adoption counts as codification; prose retention does not) are necessary once, at the definition, and the relaxing paragraph's reformulation does local work, but the opening and heuristic 1 restate them again. Both fixes are in-place compressions; neither requires removing the supporting point.
