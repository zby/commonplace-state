---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
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
  - the arithmetic/vision-feature boundary determines what capability the commitment
    risks excluding
  reason: The opening states the note's general distinction as exact specs versus
    proxy theories. Here the note switches to 'arithmetic' and 'vision-feature,' which
    are labels from the bitter-lesson source domain (calculators, and hand-designed
    computer-vision features). It uses them without saying they are its names for
    the opening distinction, and introduces them with a definite article as if the
    reader already knows them. The later bullets define the regimes, but the mapping
    to 'exact spec / proxy theory' stays implicit. Heuristic 1 then classifies an
    executable test as 'in the arithmetic regime,' so the source-domain label now
    names a general category. Either map the labels to the opening terms once ('arithmetic-regime
    (exact-spec)…') or use the general terms.
  level: warn
- scope: passage
  quotes:
  - The vision researchers made this bet at maximum disadvantage.
  reason: '''The vision researchers'' presumes the source narrative (the bitter-lesson
    history of hand-engineered vision features). The note never introduces it as a
    case. The paragraph should be marked as an illustrative historical case, for example:
    ''Classical computer-vision research illustrates the worst case…'''
  level: warn
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/e3a3758d1cbef848fdd1bd3e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-source-residue.md
raw-output-sha256: 9e467ea4772fd9b7e60355ab6d8053a437992940d9a64cb02f7128399a995d40
---

# Review

## Summary

The title and opening claim generality: any practical system that combines scripts and checks with learned components, with agent-operated KB methods as the evident target. Most examples are framed as examples. The edge-detection, FlashAttention and tokenizer passage is explicitly a trajectory illustration, and the heuristics use KB-relevant cases (executable tests, workflow decompositions, endpoints).

Residue remains in two places. The regime vocabulary comes from the bitter-lesson source domain and is used as the note's general terminology without being mapped to the exact-spec/proxy-theory distinction stated in the opening. And "the vision researchers" appear as if the reader already shares the source's narrative.
