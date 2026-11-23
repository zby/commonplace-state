---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 70648dfe2f5947afb0c1d97c1d5a5e90
completed-at: '2026-11-20T09:42:40Z'
findings:
- scope: document
  quotes: []
  reason: The Scheduler layer section (paragraph, four-row table and closing paragraph)
    is about as long as The mechanism section, yet it supports the title claim only
    indirectly through its final sentence. The mechanism section explains name-based
    dispatch but not what else must match for a swap to leave callers unchanged (argument
    and return shapes, error behavior). The imbalance is mild; the scheduler comparison
    could become its own note if it grows.
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/5d1ed990621f57d7dc14197d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/outputs/review-proportion-mismatch.md
raw-output-sha256: 66d4c014133922d67b9d6ddcee974f2c4573e61a58c6405207c0912572f481c1
---

# Review

## Summary

Core claim: when neural and symbolic components share a calling convention, a component can be moved across the boundary in either direction without changing call sites.

Support by section:

- **Opening** states the claim and its motivation.
- **The mechanism** gives the llm-do instance and name-based dispatch — the load-bearing explanation.
- **Why this matters for constraining** carries the forward progression (four steps) and the reverse direction (step 4 plus the prompt-trial paragraph), which together cover "bidirectional".
- **The scheduler layer** contrasts imperative and graph orchestration; only its last sentence ties back to the claim.
- **The connection to typed callables** links the interface view to the type-theoretic note.

The secondary scheduler material does not outweigh the load-bearing sections. Taken together, the mechanism and progression sections receive the most development, so the proportions pass, with an INFO note on the comparatively thin account of what makes the convention "unified".
