---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'The bet is that what you extracted is genuinely part of the spec'
      - 'In the vision-feature regime, the bet is risky: the spec is a theory, and scale may reveal a better path'
    reason: 'Definition drift in "spec". In the first passage the spec is the load-bearing target behavior, contrasted with an accidental pattern, so being "part of the spec" means the bet is won. In the second, and in the regime bullets, the spec is the committed requirement, which in the vision regime is itself a proxy theory. Under the second meaning, an extraction that is exactly part of a vision-feature spec still loses. The bet is then stated as risky in that regime even though its stated condition is met. The two meanings make the bet''s success condition contradict itself across adjacent paragraphs.'
    level: warn
  - scope: passage
    quotes:
      - 'detects when codified components are encoding vision features'
    reason: 'The body says relaxing signals detect a component that "encodes an accident rather than a spec", and treats accidents (patterns mined from observed data) as spec mining''s residual failure, distinct from the vision-feature failure that spec mining avoids. The footer says the same signals detect vision features. Either the two failure kinds are one, or the footer and body disagree; likely drift that needs author confirmation.'
    level: info
  - scope: passage
    quotes:
      - 'Codify for current leverage, not permanence.'
    reason: 'The heuristic advises against codifying for permanence, while the preceding section concludes that arithmetic-regime codification bets "are not merely safe-for-now" and persist under scaling. The heuristic body reconciles this by expecting only the vision-feature kind to relax, but the bolded heading reads as universal. Mild tension.'
    level: info
outcome: warn
---

# Review

The note's main structure is internally consistent. The opening's claim that codified and learned do not partition systems agrees with the relaxing paragraph's note that a replacement can be codified by adoption. The bidirectional edge-detection trajectory agrees with "The bitter lesson describes a trajectory, not a law of nature." The arithmetic bullet's caveat about implementation and maintenance costs agrees with the trade-off framing.

The contradiction sits in the term "spec". The bet section defines winning as extracting something "genuinely part of the spec". The regime discussion in the same section, and the regime bullets earlier, use "spec" for the committed requirement, which can itself be a theory. Read with one meaning, the arithmetic/vision contrast and the bet's success condition do not line up. The note needs one sense, or two named senses (committed requirement vs load-bearing target behavior). The accident-vs-vision-feature drift in the footer and the universal-sounding heuristic heading are recorded as INFO.
