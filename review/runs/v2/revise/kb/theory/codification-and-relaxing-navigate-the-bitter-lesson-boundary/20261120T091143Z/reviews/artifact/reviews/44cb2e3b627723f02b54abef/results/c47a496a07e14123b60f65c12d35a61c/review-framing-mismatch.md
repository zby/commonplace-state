---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This means codification bets in the arithmetic regime are not merely safe-for-now;
    the step-by-step structure that codification encodes is the kind of regularity
    that persists under scaling.
  reason: 'The cited mechanism is an architectural inductive bias inside learned sequence
    models: transformers without step-by-step structure fail to share solutions across
    lengths on calculator-class state tracking. The sentence reframes this as evidence
    about codification bets, meaning scripts and validators committed outside the
    model, and widens ''calculator-class state tracking'' to the whole arithmetic
    regime. The result supports a narrower claim: on that task class, structure that
    encodes stepwise decomposition is not dissolved by scale. State the task class
    and say it concerns architecture, or explain why it transfers to extracted code.'
  level: warn
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget.
  reason: 'The note''s own glosses define epiplexity as learnable structure within
    computational bounds, so it is relative to the observer''s budget, not independent
    of it. The section frames it as a test for the risk named earlier, a regularity
    that is an accident of the observed data. Time-bounded entropy versus epiplexity
    separates pseudo-randomness from learnable structure for a bounded learner, not
    sampling accidents from load-bearing regularities. The follow-on ''accidents visible
    only at current scale'' also runs against the bound-relative direction, since
    more compute usually reveals more structure. The framing misplaces the mechanism.
    Confidence is moderate: the paper is external and was not read.'
  level: warn
- scope: passage
  quotes:
  - If codified conventions don't compose into better systems, that's the signal to
    relax
  reason: This frames composition failure as a decisive relaxing signal. The linked
    fixed-artifact and relaxing-signal notes say composition failure can also come
    from interface mismatches, inconsistent specs or execution defects, and should
    be diagnosed first. The heuristic emphasizes one cause without excluding the others.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/44cb2e3b627723f02b54abef/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: c47a496a07e14123b60f65c12d35a61c
completed-at: '2026-11-20T09:15:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/outputs/review-framing-mismatch.md
raw-output-sha256: cc7cd9fe6bedc29ba6c53f8938c8beea325f02c61435db8c9fee1c43e3d30fce
format: 2
---

# Review

The regime and relaxing framings in the first two sections match their mechanisms: code extraction trades generality for reliability, speed and cost; arithmetic-regime decompositions do not lose required behavior; vision-feature decompositions can. The spec-mining explanation (an observed working composition narrows the bet) is correctly identified.

The two formal-results paragraphs are where the framing slips. The induction-bias paragraph turns a finding about architecture in learned models on one task class into a claim about codification bets across the arithmetic regime. The epiplexity paragraph treats a compute-relative distinction between structure and pseudo-randomness as a test for the sample-accident risk the note defines earlier. The third heuristic's framing is narrower than its mechanism but does not exclude other causes.
