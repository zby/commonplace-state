---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the arithmetic/vision-feature boundary determines what capability the commitment risks excluding"
    reason: "The opening states the note's general distinction as exact specs versus proxy theories. Here the note switches to 'arithmetic' and 'vision-feature,' which are labels from the bitter-lesson source domain (calculators, and hand-designed computer-vision features). It uses them without saying they are its names for the opening distinction, and introduces them with a definite article as if the reader already knows them. The later bullets define the regimes, but the mapping to 'exact spec / proxy theory' stays implicit. Heuristic 1 then classifies an executable test as 'in the arithmetic regime,' so the source-domain label now names a general category. Either map the labels to the opening terms once ('arithmetic-regime (exact-spec)…') or use the general terms."
    level: warn
  - scope: passage
    quotes:
      - "The vision researchers made this bet at maximum disadvantage."
    reason: "'The vision researchers' presumes the source narrative (the bitter-lesson history of hand-engineered vision features). The note never introduces it as a case. The paragraph should be marked as an illustrative historical case, for example: 'Classical computer-vision research illustrates the worst case…'"
    level: warn
outcome: warn
---

# Review

## Summary

The title and opening claim generality: any practical system that combines scripts and checks with learned components, with agent-operated KB methods as the evident target. Most examples are framed as examples. The edge-detection, FlashAttention and tokenizer passage is explicitly a trajectory illustration, and the heuristics use KB-relevant cases (executable tests, workflow decompositions, endpoints).

Residue remains in two places. The regime vocabulary comes from the bitter-lesson source domain and is used as the note's general terminology without being mapped to the exact-spec/proxy-theory distinction stated in the opening. And "the vision researchers" appear as if the reader already shares the source's narrative.
