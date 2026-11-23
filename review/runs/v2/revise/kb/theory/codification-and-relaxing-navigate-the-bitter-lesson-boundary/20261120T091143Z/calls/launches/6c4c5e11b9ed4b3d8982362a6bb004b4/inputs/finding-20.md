---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 42d3e1baabad4cc48a4f34214ae538b7
completed-at: '2026-11-20T09:15:36Z'
findings:
- scope: passage
  quotes:
  - The bet is that what you extracted is genuinely part of the spec
  - 'In the vision-feature regime, the bet is risky: the spec is a theory, and scale
    may reveal a better path'
  reason: Definition drift in "spec". In the first passage the spec is the load-bearing
    target behavior, contrasted with an accidental pattern, so being "part of the
    spec" means the bet is won. In the second, and in the regime bullets, the spec
    is the committed requirement, which in the vision regime is itself a proxy theory.
    Under the second meaning, an extraction that is exactly part of a vision-feature
    spec still loses. The bet is then stated as risky in that regime even though its
    stated condition is met. The two meanings make the bet's success condition contradict
    itself across adjacent paragraphs.
  level: warn
- scope: passage
  quotes:
  - detects when codified components are encoding vision features
  reason: The body says relaxing signals detect a component that "encodes an accident
    rather than a spec", and treats accidents (patterns mined from observed data)
    as spec mining's residual failure, distinct from the vision-feature failure that
    spec mining avoids. The footer says the same signals detect vision features. Either
    the two failure kinds are one, or the footer and body disagree; likely drift that
    needs author confirmation.
  level: info
- scope: passage
  quotes:
  - Codify for current leverage, not permanence.
  reason: The heuristic advises against codifying for permanence, while the preceding
    section concludes that arithmetic-regime codification bets "are not merely safe-for-now"
    and persist under scaling. The heuristic body reconciles this by expecting only
    the vision-feature kind to relax, but the bolded heading reads as universal. Mild
    tension.
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/7a242fe4b457e40444ca8c2e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/outputs/review-internal-consistency.md
raw-output-sha256: e710c4141c2232e2e86fbefaea8af9661e51e05c1b4dce770a4b28a5deb11f44
---

# Review

The note's main structure is internally consistent. The opening's claim that codified and learned do not partition systems agrees with the relaxing paragraph's note that a replacement can be codified by adoption. The bidirectional edge-detection trajectory agrees with "The bitter lesson describes a trajectory, not a law of nature." The arithmetic bullet's caveat about implementation and maintenance costs agrees with the trade-off framing.

The contradiction sits in the term "spec". The bet section defines winning as extracting something "genuinely part of the spec". The regime discussion in the same section, and the regime bullets earlier, use "spec" for the committed requirement, which can itself be a theory. Read with one meaning, the arithmetic/vision contrast and the bet's success condition do not line up. The note needs one sense, or two named senses (committed requirement vs load-bearing target behavior). The accident-vs-vision-feature drift in the footer and the universal-sounding heuristic heading are recorded as INFO.
