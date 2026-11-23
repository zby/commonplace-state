---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget
  reason: 'Unresolved scope (whose computational bounds) and comparison basis (safer
    than what, against which risk). Reading A: epiplexity is measured relative to
    the codifier''s or current model''s bounds, so "safer" means less likely to be
    an accident of today''s observer. Reading B: it is measured relative to a future
    scaled learner''s bounds, so "safer" means less likely to be relaxed when scale
    arrives. Epiplexity is observer-relative, so the readings select different measurements,
    predict different outcomes under scaling, and imply different evidence before
    codifying. The sentence also does not say whether "safer" means the regularity
    is spec rather than accident, or that the codified component will not be relaxed.
    This sentence carries the paragraph''s claim that the framework "helps bound when
    codification bets are safe".'
  level: warn
- scope: passage
  quotes:
  - If codified conventions don't compose into better systems, that's the signal to
    relax
  reason: 'Comparison basis unresolved: better than the system without the conventions,
    or better than a general (relaxed) replacement, or failing to reach the target
    capability at all. Each reading triggers relaxing under different conditions and
    requires different evidence. Recorded as INFO because the linked notes supply
    a composition-failure sense that a reader can import.'
  level: info
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
  reason: κ is not defined, so a reader cannot tell from the number which direction
    indicates sharing. The following clause ("learn length-specific solutions in isolation")
    states the intended reading, which limits materiality; INFO.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/75c327f5f3c31e8f79ae08b5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 42d3e1baabad4cc48a4f34214ae538b7
completed-at: '2026-11-20T09:15:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/outputs/review-underspecified-assertions.md
raw-output-sha256: 8fa2130c775b314dae582a9f52803aab0c1062f1d674244aaffd28e260b7d0a7
format: 2
---

# Review

Most load-bearing assertions are specified enough. The codification scope is narrowed explicitly to the code-extraction case. The regime bullets name the condition under which each holds. Relaxing is defined with its trade (higher cost and lower reliability for regained generality) and its limit (it reverses the extraction, not symbolic membership). The bet is defined as extracted regularity vs accidental pattern on observed data.

The material gap is the epiplexity claim. Epiplexity is defined relative to an observer's computational bounds, and the note does not say which observer's bounds it means, nor what "safer" compares or protects against. Different choices change what one would measure before codifying and what one predicts at scale. This sentence is the paragraph's main contribution to "when codification bets are safe", so the gap affects the note's argument. The comparison basis in heuristic 3 and the undefined κ are recorded as INFO.
