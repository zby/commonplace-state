---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats"
    reason: "The note cites the 'sharing factor κ' but never defines it. It does not say what κ measures, what a value of 1 means, or which direction counts as sharing. A reader cannot tell why κ ≈ 1 or κ < 1 supports 'learn length-specific solutions in isolation.' The citation names the source, but the number lacks the local context needed to evaluate it."
    level: warn
  - scope: passage
    quotes:
      - "training diversity actively hurting (κ = 0.28 for CoT)"
    reason: "Without a definition of κ or a stated baseline, the reader cannot see why 0.28 shows diversity 'actively hurting.' It is also unclear what 'CoT' supervision is compared against in that measurement. The figure appears more precise than the note's explanation of it."
    level: warn
  - scope: passage
    quotes:
      - "190K training runs showing architectural induction bias is permanent for calculator-class tasks"
    reason: "INFO. The run count is attributed to the cited paper, so it has a source. 'Calculator-class tasks' and 'permanent' are stated without saying what scale range the runs cover, and that range is what would let a reader judge 'permanent.'"
    level: info
outcome: warn
---

# Review

## Summary

Both named studies (Finzi et al. on epiplexity, and Ebrahimi et al. on induction bias) have inline links and Sources entries. So the problem is missing local context, not missing sources. The induction-bias paragraph uses three κ values as its main evidence but does not define κ. A reader cannot use them to judge the claim that follows. Either define the sharing factor and its reference value, or replace the numbers with a qualitative statement of the result.

The historical examples (edge detection, FlashAttention, tokenizers) are well known in the field and are used as illustrations, not as evidence for a specific figure, so they are not flagged.
