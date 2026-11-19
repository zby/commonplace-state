---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 3288b9badfc1474a9ad8a5ecb8d3c76e
completed-at: '2026-11-16T18:56:43Z'
findings: []
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/add0b577fa97bd3cd24e3958/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/add0b577fa97bd3cd24e3958/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/3288b9badfc1474a9ad8a5ecb8d3c76e/outputs/review-concept-attribution.md
raw-output-sha256: 1328c229a826bf1cd624026f1ff728cd500a31b41b70b54a74d086cb6de33d4d
---

# Review

## Summary

The note borrows two concepts from linked notes: the split between a claim's test record and its fit, and the claim that system use is evidence of fit rather than an independent test. I checked both against the targets.

- The opening paragraph and the Scope section treat "theory fit" as separate from a claim's independent test record. That matches the title claim of "A claim's test record does not determine its fit in a working theory". That note defines fit as the theory handling its problem better with the claim, including changing explanation, prediction, search or modification. That agrees with this note's "help the system reason, modify, or recover".
- The self-confirmation section cites "System use provides evidence of theory fit and causal usefulness, not an independent test". The target's opening paragraphs make the same points: the live system "can reward its own misconceptions", and independent checks must stay able to overturn the claim. The blame-assignment paragraph also matches the target's read-back discussion.

Both targets resolved. No identity claim differs substantively from its target.
