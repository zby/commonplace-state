---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 4bc0b3d0cf7540a382abb1ec3607e923
completed-at: '2026-11-20T09:42:15Z'
findings: []
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/0e27af64d8c9ccb2e9254f60/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/outputs/review-could-be-a-paragraph.md
raw-output-sha256: d3b0144654021389d11f22a40768bbf5050c46d2cce6a2bcb757d194fa24a781
---

# Review

A one-paragraph rewrite would keep the headline claim: a shared calling convention lets components move between neural and symbolic without call-site changes. It would lose several load-bearing parts:

- **The inference step.** Name-based dispatch supplies dynamic resolution, late binding and implementation-agnostic names. This explains *why* the convention works, not just that it does.
- **The worked progression.** Start neural, observe, codify, then extend by relaxing. This includes a concrete example and the counterfactual: without the convention, each step is a breaking change that pushes toward big-bang rewrites.
- **The reverse case.** Moving back to a prompt as a cheap experiment while the code still meets its current requirement. This is a non-obvious use of the bidirectionality.
- **The scheduler contrast.** Imperative orchestration, unlike graph DSLs, keeps boundary refactorings within ordinary code refactorings. This is a second claim with its own comparison basis.
- **Open questions.** Scale, cross-boundary debugging and host language set the claim's boundary conditions.

The note holds more than one simple insight, so its multi-section structure is justified.
