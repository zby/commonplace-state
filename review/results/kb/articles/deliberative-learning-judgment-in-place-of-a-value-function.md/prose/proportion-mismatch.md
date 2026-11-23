---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: e6c44a5d053c40b889fc04e430cca4c7
completed-at: '2026-11-21T19:26:59Z'
findings:
- scope: passage
  quotes:
  - We bet that a fixed-weight language model can fill the judge slot autonomously,
    running double-loop deliberative learning with targeted correction for work where
    no fixed criterion is adequate.
  reason: 'The article''s distinctive claim, stated in its title and its second-level
    thesis, is that a fixed-weight language model can do on-balance judgment in place
    of a value function. The article states this bet in one paragraph, and the reasons
    to expect it to hold are never developed. The paragraph lists only what the bet
    requires: weighing edits, diagnosing which retained edit caused a failure, and
    revising criteria. It gives no reason or mechanism showing why current models
    might meet those requirements. The Bitter Lesson section, by contrast, spans five
    paragraphs, including a detailed reinterpretation of an external study. The precedent
    tour also gets three full paragraphs. Secondary material that defends the article
    against an objection or supplies historical context is therefore more developed
    than the case for the central bet. Either develop why a language-model judge is
    plausible, for example with the kinds of trade-off and trace diagnosis it already
    handles, or shorten the Bitter Lesson section, perhaps by moving the Harness Evolution
    reinterpretation into its own note.'
  level: warn
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/7de6ee23f4fb8ddd7cf96e01/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/outputs/review-proportion-mismatch.md
raw-output-sha256: 8c1c9ed353b329de7ab4fee4e86790f4d5121cde8498c3a66cd990cb7fe76729
---

# Review

## Summary

The article makes a two-level claim:

1. Deliberative learning is a paradigm in which on-balance judgment does the
   work of a value function.
2. The bet is that a fixed-weight language model in the judge slot makes this
   an automated machine-learning paradigm.

The first level gets reasonable support from the worked example, the
two-condition definition, the comparison table and the precedent sequence. The
on-balance judgment paragraph is short for the title concept, but it links to a
dedicated note.

The second level is the article's novelty claim ("What is new is not the loop,
but a machine judge ..."). It gets the least development of any major element:
one paragraph stating the bet's requirements and a later admission that no
end-to-end evidence exists. The Bitter Lesson section, which responds to an
objection, is longer and more detailed, especially the reinterpretation of the
Harness Evolution study. Being candid that the bet lacks evidence is not the
problem. The problem is that the article never says why the bet is reasonable,
while it argues secondary material at length.
