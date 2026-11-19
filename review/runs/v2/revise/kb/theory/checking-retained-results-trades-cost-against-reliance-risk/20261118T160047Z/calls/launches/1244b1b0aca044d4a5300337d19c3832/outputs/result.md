---
type: types/edit-result.md
outcome: changed
changes:
  - "new-pattern (link text carries a superseded target title that overstates the target's current claim): in the Relevant Notes entry for llm-recompute-cost-inverts-the-store-vs-recompute-default.md, replaced the link text 'LLM recompute cost inverts the store-vs-recompute default' with the target's current title 'LLM recompute cost shifts the store-vs-recompute balance'."
  - "new-pattern (same): in the same entry, replaced the annotation 'why recomputation is costly enough for retained results to be worth keeping' with 'why costly model-side recomputation can make a retained result worth keeping, when its total expected cost beats the alternatives'; the 'grounds' label and link target are kept."
removed-links: []
---

# Report

Strategy: `new-pattern`. The pattern is link text that keeps a target's superseded title after the target was retitled, so that the text overstates the target's current claim. No listed strategy covers it; `hedge-strength-mismatch` is closest but concerns source claims in the body, not link text.

- Passage: the Relevant Notes entry `[LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why recomputation is costly enough for retained results to be worth keeping`.
- Change: the link text now uses the target's current H1, "LLM recompute cost shifts the store-vs-recompute balance". The annotation now states the target's condition, that persistence pays only when its total expected cost beats the alternatives (the target's description and its paragraph "Expensive model-side derivation does not by itself justify persistence"). It also names model-side recomputation, the target's subject.

Kept: the link target path (the file has not been renamed), the `grounds` relation, the other two Relevant Notes entries and the whole body. No must-keep claim or relied-on term from the kb-role is affected. The finding result holds one finding (position 0), and this change fixes it; no finding is left untouched.
