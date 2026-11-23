---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/critique-note.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: c98ed7c8714b4845b1f384f8050eb87f
completed-at: '2026-11-20T09:16:26Z'
findings:
- scope: passage
  quotes:
  - The bet is that what you extracted is genuinely part of the spec
  - reveal when a codified component encodes an accident rather than a spec
  reason: 'The note''s diagnosis has only two outcomes: the extracted regularity is
    load-bearing, or it is an accident. Its own anchor case does not fit either outcome.
    Learned vision networks rediscover oriented edge and Gabor-like detectors in their
    early layers, so edge structure was load-bearing. Hand-coded edge pipelines still
    lost because their components were frozen and tuned separately, while learned
    systems optimize every stage together. The note needs a third failure mode: a
    real regularity whose fixed form loses to joint optimization. Without it, relaxing
    signals are presented as detectors of accidents, and that misses the main way
    the vision case lost.'
- scope: passage
  quotes:
  - They were betting that theorized components would compose into the target capability,
    with no evidence of successful composition.
  reason: The contrast with spec mining treats classical vision as theory with no
    working system. Researchers did have one to mine. Hubel and Wiesel found orientation-selective
    cells in the cat visual cortex, and Marr's primal sketch and much edge-detector
    design drew on such biological and psychophysical findings. If classical vision
    features were partly mined from a working system and still lost, 'starting from
    a working system' cannot by itself explain the better odds. The note should name
    what separates mining a deployed system's behavior from mining a biological system,
    such as substrate match, the same target distribution or behavioral rather than
    mechanistic observation. Otherwise it should narrow the historical claim.
- scope: passage
  quotes:
  - with spec mining avoiding the vision-feature failure mode
  reason: The description says spec mining avoids the failure mode. The body says
    only that it 'improves the odds' and that 'it's still a bet'. The description
    overclaims relative to the body and to the attack above.
- scope: passage
  quotes:
  - This means codification bets in the arithmetic regime are not merely safe-for-now
  reason: 'As summarized here, the Ebrahimi et al. result concerns architectural induction
    bias inside trained sequence models: step-by-step decomposition helps state tracking.
    It does not test committing a rule to a script or validator, which is the code-extraction
    case this note defines. Moving from ''this architectural bias persists under scaling''
    to ''code-extraction bets in the arithmetic regime persist'' needs a bridging
    sentence. The source note''s word ''permanent'' should also be bounded to the
    regimes the study tested.'
- scope: passage
  quotes:
  - Since you can't reliably tell which regime you're in until scale tests the distinction
  reason: The opening premise is stated without a condition. Heuristic 1 then classifies
    an executable numerical-contract test as arithmetic-regime in advance, and the
    body later says the blurry zone covers only 'most practical codification'. The
    premise should be scoped to the blurry zone, where the regime is unknown until
    scale tests it, so that it agrees with the note's own prospective classifications.
contract: report
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c98ed7c8714b4845b1f384f8050eb87f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/a696ce12eab9ca0d9501d934/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c98ed7c8714b4845b1f384f8050eb87f/outputs/review.md
raw-output-sha256: 36b79943695056f0d56d4675916dca1078324746189880f9faa5e35b033566a0
attack-outcome: partially lands
---

# Critique: Codification and relaxing navigate the bitter lesson boundary

**Note:** kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
**Central commitment:** The arithmetic/vision-feature regime of a codified decomposition often cannot be known until scale tests it. So practical systems must codify for current leverage and relax when scale makes general methods viable, and spec mining from a working system makes the codification bet safer because it shifts the risk from composition to whether a mined pattern is load-bearing rather than accidental.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The strongest objection comes from a historian of computer vision or a deep-learning practitioner, using the note's own example case. It targets the note's mechanism for why codification loses, not its conclusion that systems should codify and relax.

The note treats each code-extraction codification as a bet with two outcomes. The extracted regularity is either "genuinely part of the spec" (load-bearing) or "an accident" that holds only on observed data. In this account, relaxing signals detect the losing bet, the accident. Classical vision is the canonical loss, and the note explains it as composition without a working system: researchers "were betting that theorized components would compose into the target capability, with no evidence of successful composition."

The vision record contradicts both parts of that account.

1. **The regularities were not accidents.** Convolutional networks trained end to end repeatedly learn oriented edge detectors and Gabor-like filters in their first layers. Edge structure is therefore load-bearing; scale rediscovered it rather than refuting it. Hand-coded edge, corner and SIFT/HOG pipelines lost for another reason. Each fixed, separately tuned stage could not adapt to errors in later stages, while jointly optimized learned stages could. The losing bet was on a frozen, non-adaptive commitment to a true regularity. In the note's terms, that is neither "accident" nor "spec."
2. **There was a working system to mine.** Hubel and Wiesel's orientation-selective cortical cells, psychophysics and Marr's biologically informed primal sketch gave vision researchers a working "seeing" system from which they extracted components. They were doing a form of spec mining.

If both points hold, the note's prescription loses its diagnostic power. Spec mining from a working system does not prevent the vision-type loss. "Is this pattern load-bearing?" is the wrong question, because a load-bearing pattern can still lose to joint optimization once it has been codified. A practitioner who follows the note would mine a regularity, confirm that it is real and keep it. They would then miss the actual relaxing trigger: a general learner can now co-adapt that stage with its neighbors.

## How the note engages it

**Partially engaged.** The note has some material for an answer:

- It frames the vision loss partly as a failed *composition* bet ("will these pieces compose?"). That is close to the joint-optimization point, though it is phrased as missing evidence of composition, not as frozen stages losing to co-adaptation.
- Its third heuristic, "Watch for composition failure as a relaxing signal," points in the right direction.
- The trajectory paragraph accepts that edge detection "may re-codify as an accelerator inside a learned architecture," which allows that a codified regularity can be true.
- It hedges that the selection property is "conjectural, not established," and that spec mining is "still a bet."

The note does not engage two points. First, its accident-versus-spec dichotomy, and the relaxing signals built on it, does not fit its own anchor case. Second, the biological working system undermines the line it draws between vision researchers and spec miners. The description goes further than the body and says spec mining *avoids* the vision-feature failure mode.

## Constructive findings

- Add a third outcome to "Every code-extraction codification is a bet": the extracted regularity is real, but its fixed, separately tuned form loses to a learner that optimizes all stages together. Name this as a relaxing trigger next to accidents. Learned networks rediscovering edge detectors is the natural example. Then relaxing signals can be described as detecting both accidental encodings and frozen-stage disadvantage.
- Restate the vision-researcher contrast. Either acknowledge the biological working system and say what makes mining a deployed system's behavior different (same substrate, same target distribution, behavioral rather than mechanistic observation), or narrow the claim to "no working *engineered* system on the target task."
- Bring the description into line with the body: spec mining *improves the odds against*, not *avoids*, the vision-feature failure mode.
- Add the missing step between Ebrahimi et al., which concerns architectural induction bias in trained models, and code-extraction codification. Bound "permanent" to the tested task class.
- Scope the opening premise to the blurry zone so that heuristic 1's prospective classifications do not contradict it.

## Secondary objections

- The epiplexity paragraph says that "Low-epiplexity patterns that appear regular may be accidents visible only at current scale." Epiplexity is itself defined relative to an observer's computational bound. The note does not say how a practitioner would estimate it for a candidate codification, so the bound stays theoretical, not operational. I have not checked the paper's exact framing. This objection is therefore tentative.
- A Sutton-style objector might say that hybrids are only transitional and that codify-then-relax adds maintenance cost a general-first default would avoid. The note answers this adequately with "codify for current leverage, not permanence" and the multi-level trajectory examples (FlashAttention, tokenizers). That objection does not survive.
