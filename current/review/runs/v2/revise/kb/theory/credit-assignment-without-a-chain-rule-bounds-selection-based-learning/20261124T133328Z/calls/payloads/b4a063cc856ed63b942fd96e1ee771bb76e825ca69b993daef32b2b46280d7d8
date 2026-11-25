---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
note-sha256: 2edb199c9fc66d721a3310a5dfbe13fd0efad9c76eb1f87e49567bbf16389743
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews
launch: 5d97a230e9b349aabc4e8d79c0215bde
completed-at: '2026-11-24T13:36:04Z'
findings:
- scope: passage
  quotes:
  - Because of those three differences, naive workarounds still break down at scale.
  reason: The sentence attributes the failure of all three workarounds to the three
    prose-specific properties (softer traces, implicit coupling, noisier failures),
    but the paragraph's own mechanisms are different. Appending exceptions fails because
    it adds coupling and bloat; exhaustive one-by-one ablation fails because its cost
    grows with store size, which would hold for ordinary code too. Only the rationale-trusting
    case clearly rests on one of the three properties (softer traces / faithfulness).
    The causal framing misdirects the reader about why the workarounds fail and excludes
    the scale mechanism that actually drives the ablation case.
  level: warn
contract: verdict
target-sha256: 445d4f9910c0a70b503081a3e06658de2e895f949e9930c9f7643aac8fa69e2f
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/5d97a230e9b349aabc4e8d79c0215bde/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/artifact/reviews/c06d870afb2c35ab0adf6bcb/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/reviews/calls/launches/5d97a230e9b349aabc4e8d79c0215bde/outputs/review-framing-mismatch.md
raw-output-sha256: 598f029d55f874294681b91b070300453877d6b6c98997f1a10197de8ed6dc08
---

# Review

## Summary

The note frames its mechanisms correctly. Credit assignment without a chain rule is treated as debugging, and the obstacles are named as weakened debugging tools rather than a lack of gradients.

One transition sentence assigns the wrong cause. "Because of those three differences" claims that the prose-specific properties explain why the workarounds break down. The following sentences give other mechanisms: coupling and bloat from accretion, and the combinatorial cost of ablation at scale. A neutral connective would keep the paragraph accurate, for example "At scale, naive workarounds break down" or "Under those conditions, and at scale, ...". Another option is to tie each workaround to the property or the scale cost that defeats it.
