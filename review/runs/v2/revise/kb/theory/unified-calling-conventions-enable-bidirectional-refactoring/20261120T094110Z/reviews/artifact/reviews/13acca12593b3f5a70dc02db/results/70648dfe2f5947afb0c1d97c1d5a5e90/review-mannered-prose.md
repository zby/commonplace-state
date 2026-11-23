---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the phase transition from neural to symbolic that unified calling makes a local
    operation
  reason: 'Literal meaning: codification is the step that moves a component from an
    LLM-interpreted implementation to code. "Phase transition" imports a physics image
    of an abrupt, system-wide change at a critical threshold, which is the opposite
    of the note''s claim that the step is local and incremental. Replace with "the
    step that moves a component from neural to symbolic, which unified calling makes
    a local operation"; this removes the unsupported threshold and global-change connotations.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/13acca12593b3f5a70dc02db/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 70648dfe2f5947afb0c1d97c1d5a5e90
completed-at: '2026-11-20T09:42:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/outputs/review-mannered-prose.md
raw-output-sha256: e36c57c94007614112c60c8b874ba408a9f60baeb54a3af22b43d2d7db2e4d68
format: 2
---

# Review

## Summary

The body is mostly literal. Figurative candidates examined:

- "big-bang rewrites" — established software-engineering term for wholesale replacement; precise shorthand, kept.
- "This friction discourages incremental refactoring" and "makes frictionless" — the note defines the friction literally (call sites, prompt structure and the agent's operation list must change), so the figure has a stated mapping.
- "Each link can be independently refactored" — the chain image is drawn in the diagram and used directly.
- "the progression is smooth" — mild and immediately cashed out by the four steps.

One phrase in the Relevant Notes annotations, "phase transition", carries connotations that contradict the note's central claim about locality, so the gate returns WARN for that local instance.
