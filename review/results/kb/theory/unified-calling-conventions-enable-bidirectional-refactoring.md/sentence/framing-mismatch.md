---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 765fee9a50524c84b74692bd14c7d801
completed-at: '2026-11-20T09:44:02Z'
findings:
- scope: passage
  quotes:
  - This requires **name-based dispatch**
  reason: What makes call sites stable is indirection behind a shared interface. Name-based
    dispatch is how llm-do achieves that indirection, and it is natural when the caller
    is an LLM that emits a string. Code callers could also get implementation-agnostic
    interfaces through a protocol or interface reference. The sentence puts weight
    on one implementation, but the following sentence explains why names suit this
    runtime, so the framing does not mislead about the mechanism.
  level: info
- scope: passage
  quotes:
  - '**Extend via relaxing** — new requirements emerge (handle Unicode, detect dates).
    Add an LLM call for the new cases.'
  reason: 'The step is called relaxing, but what it describes is adding neural handling
    for requirements the code never covered. It does not move existing rigid code
    back to the LLM, which is how the note''s opening describes relaxing. The point
    stands: the call site stays stable either way. The label just frames extension
    as a reversal.'
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/79235c87a5a5cda9ed5bd4ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/outputs/review-framing-mismatch.md
raw-output-sha256: 02b2f671bfe0938af529a39fffa4cca3130ab1873e5e5dff67b05c82e0ec433c
---

# Review

## Summary

The note's explanations of mechanism mostly sit at the right level of generality. The core claim is framed as a shared interface that keeps call sites stable, so refactoring across the neural/symbolic boundary stays local. That framing matches the mechanism described. The scheduler section correctly says that refactoring becomes ordinary code refactoring because orchestration is written in Python rather than as graph edges. Two framings put weight on a narrower case than the mechanism covers: name-based dispatch as a requirement, and "relaxing" as the label for extension. Neither excludes cases the reader needs, so both are informational.
