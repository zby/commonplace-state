---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats"
      - "κ = 0.28 for CoT"
    reason: "The symbol κ comes from the Ebrahimi et al. paper. The note gives only its name, \"sharing factor\". It never says what is shared, what scale κ uses, or which direction means more sharing. A reader cannot tell whether κ ≈ 1 is good or bad, or why 0.28 shows that training diversity \"actively hurts\". The note uses κ in no formal argument. Replace the values with plain language, such as \"transformers reuse little or nothing across sequence lengths, and chain-of-thought supervision makes this worse\". Otherwise, define κ and its scale in one clause."
    level: warn
outcome: warn
---

# Review

The note has one piece of formal notation: the sharing factor κ in the induction-bias paragraph. The note does not define it, and it appears as bare values (κ ≈ 1, κ < 1, κ = 0.28). The next clause, "they learn length-specific solutions in isolation", suggests the intended reading. Still, the reader cannot work out from the note what the numbers measure or which direction is better. The paragraph contains no equations or derivations that need the symbol, so plain language is the better fix.

No other notation appears. The slash in "arithmetic/vision-feature boundary" is ordinary prose shorthand, not a variable.
