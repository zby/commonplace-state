---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 70648dfe2f5947afb0c1d97c1d5a5e90
completed-at: '2026-11-20T09:42:41Z'
findings: []
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/25d05af9e95a11ff58832160/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/outputs/review-unbridged-cross-domain.md
raw-output-sha256: b67b0485be8b37ea657e9fffc93473b8f67596da7cd17ce49fe927115eacbf59
---

# Review

## Summary

The note cites no studies or empirical results from another field. Its evidence is the llm-do system, which lies in the same domain as the argument: LLM agent architectures that mix neural and symbolic components. Ordinary software-refactoring practice (extract function, inline, rename) is applied to components that are themselves code-level callables. The note states the bridge: under a shared calling convention, a neural component occupies the same call position as a function. The typed-callables connection is an internal KB link within the same domain and is labelled a "view" that llm-do makes practical, not imported evidence.

No cross-domain transfer lacks a stated mechanism.
