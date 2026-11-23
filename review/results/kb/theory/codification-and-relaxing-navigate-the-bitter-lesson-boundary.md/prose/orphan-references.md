---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 15c0d28c726a474283672c97c466d84d
completed-at: '2026-11-20T09:13:36Z'
findings:
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
  reason: The note cites the 'sharing factor κ' but never defines it. It does not
    say what κ measures, what a value of 1 means, or which direction counts as sharing.
    A reader cannot tell why κ ≈ 1 or κ < 1 supports 'learn length-specific solutions
    in isolation.' The citation names the source, but the number lacks the local context
    needed to evaluate it.
  level: warn
- scope: passage
  quotes:
  - training diversity actively hurting (κ = 0.28 for CoT)
  reason: Without a definition of κ or a stated baseline, the reader cannot see why
    0.28 shows diversity 'actively hurting.' It is also unclear what 'CoT' supervision
    is compared against in that measurement. The figure appears more precise than
    the note's explanation of it.
  level: warn
- scope: passage
  quotes:
  - 190K training runs showing architectural induction bias is permanent for calculator-class
    tasks
  reason: INFO. The run count is attributed to the cited paper, so it has a source.
    'Calculator-class tasks' and 'permanent' are stated without saying what scale
    range the runs cover, and that range is what would let a reader judge 'permanent.'
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/51da91fa293e7c81daf474c6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-orphan-references.md
raw-output-sha256: 21fdc5d68c7680722a502a28a6c93e5fee7e7d3da0522168f3834b82662e0fde
---

# Review

## Summary

Both named studies (Finzi et al. on epiplexity, and Ebrahimi et al. on induction bias) have inline links and Sources entries. So the problem is missing local context, not missing sources. The induction-bias paragraph uses three κ values as its main evidence but does not define κ. A reader cannot use them to judge the claim that follows. Either define the sharing factor and its reference value, or replace the numbers with a qualitative statement of the result.

The historical examples (edge detection, FlashAttention, tokenizers) are well known in the field and are used as illustrations, not as evidence for a specific figure, so they are not flagged.
