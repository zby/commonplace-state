---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Because of those three differences, naive workarounds still break down at scale."
    reason: "The sentence attributes the failure of all three workarounds to the three prose-specific properties (softer traces, implicit coupling, noisier failures), but the paragraph's own mechanisms are different. Appending exceptions fails because it adds coupling and bloat; exhaustive one-by-one ablation fails because its cost grows with store size, which would hold for ordinary code too. Only the rationale-trusting case clearly rests on one of the three properties (softer traces / faithfulness). The causal framing misdirects the reader about why the workarounds fail and excludes the scale mechanism that actually drives the ablation case."
    level: warn
outcome: warn
---

# Review

## Summary

The note frames its mechanisms correctly. Credit assignment without a chain rule is treated as debugging, and the obstacles are named as weakened debugging tools rather than a lack of gradients.

One transition sentence assigns the wrong cause. "Because of those three differences" claims that the prose-specific properties explain why the workarounds break down. The following sentences give other mechanisms: coupling and bloat from accretion, and the combinatorial cost of ablation at scale. A neutral connective would keep the paragraph accurate, for example "At scale, naive workarounds break down" or "Under those conditions, and at scale, ...". Another option is to tie each workaround to the property or the scale cost that defeats it.
