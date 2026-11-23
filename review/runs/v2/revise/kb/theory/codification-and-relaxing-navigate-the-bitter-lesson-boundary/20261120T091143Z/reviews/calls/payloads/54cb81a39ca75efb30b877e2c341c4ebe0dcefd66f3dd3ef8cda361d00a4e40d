---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats"
      - "(κ = 0.28 for CoT)"
    reason: "The note uses the sharing factor κ without defining it or saying which direction is good. 'κ ≈ 1 or κ < 1' covers nearly every value and discriminates nothing for the reader. Deleting both κ expressions leaves the passage's meaning unchanged, since the prose already says the models learn length-specific solutions in isolation and that diversity hurts. A reader cannot use the notation to make a prediction or derive a consequence, so it lends quantitative appearance without doing formal work. Either define κ and its threshold, or drop the notation."
    level: warn
  - scope: passage
    quotes:
      - "separates information into time-bounded entropy (irreducible randomness) and epiplexity (learnable structure within computational bounds)"
    reason: "The two-way entropy/epiplexity decomposition yields only one rule: codify high-epiplexity regularities and distrust low-epiplexity ones. The note never ties this vocabulary to its own arithmetic/vision-feature regimes or to the heuristics, and it gives no way to estimate epiplexity for a candidate codification. A sentence such as 'codify learnable structure, not regularities that may be artefacts of current scale' carries the same guidance. This is mild, because the framework is attributed to a source rather than presented as the note's own."
    level: info
outcome: warn
---

# Review

## Summary

Four structures were checked.

- **Arithmetic-regime / vision-feature dichotomy** (bullet pair): load-bearing. It drives the generality-loss boundary condition, the bet framing, the spec-mining argument and heuristic 1. Each category supports a different decision.
- **Numbered working heuristics**: these are decision rules with discriminating examples, not decoration.
- **Epiplexity decomposition**: largely reducible to one sentence and unused after its paragraph (info).
- **κ notation in the induction-bias paragraph**: decorative in its current form (warn), because it is undefined and carries no information the surrounding prose does not.
