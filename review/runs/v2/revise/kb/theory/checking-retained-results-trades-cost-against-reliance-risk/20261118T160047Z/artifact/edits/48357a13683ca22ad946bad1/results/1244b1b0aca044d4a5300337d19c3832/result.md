---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (link text carries a superseded target title that overstates the target''s
  current claim): in the Relevant Notes entry for llm-recompute-cost-inverts-the-store-vs-recompute-default.md,
  replaced the link text ''LLM recompute cost inverts the store-vs-recompute default''
  with the target''s current title ''LLM recompute cost shifts the store-vs-recompute
  balance''.'
- 'new-pattern (same): in the same entry, replaced the annotation ''why recomputation
  is costly enough for retained results to be worth keeping'' with ''why costly model-side
  recomputation can make a retained result worth keeping, when its total expected
  cost beats the alternatives''; the ''grounds'' label and link target are kept.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
input-sha256: 43135bf4b39741c3f4e40a03bb005f4504526df8522e562476fd4099476412b1
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/48357a13683ca22ad946bad1/results/1244b1b0aca044d4a5300337d19c3832/candidate.md
candidate-sha256: 1e6f346febb4bb7f7d16dcb927a9aa2d73f27cd378f26f306db9ec6900e5374f
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/48357a13683ca22ad946bad1/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z
launch: 1244b1b0aca044d4a5300337d19c3832
completed-at: '2026-11-18T16:13:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/calls/launches/1244b1b0aca044d4a5300337d19c3832/outputs/result.md
raw-output-sha256: ecce6b7df1aa989711cd21109c5cdac5411e1a0d1d41bc9e273135bf46795fb6
---

# Report

Strategy: `new-pattern`. The pattern is link text that keeps a target's superseded title after the target was retitled, so that the text overstates the target's current claim. No listed strategy covers it; `hedge-strength-mismatch` is closest but concerns source claims in the body, not link text.

- Passage: the Relevant Notes entry `[LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why recomputation is costly enough for retained results to be worth keeping`.
- Change: the link text now uses the target's current H1, "LLM recompute cost shifts the store-vs-recompute balance". The annotation now states the target's condition, that persistence pays only when its total expected cost beats the alternatives (the target's description and its paragraph "Expensive model-side derivation does not by itself justify persistence"). It also names model-side recomputation, the target's subject.

Kept: the link target path (the file has not been renamed), the `grounds` relation, the other two Relevant Notes entries and the whole body. No must-keep claim or relied-on term from the kb-role is affected. The finding result holds one finding (position 0), and this change fixes it; no finding is left untouched.
