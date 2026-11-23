---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 33bc96d018eb47759199e2647dea7376
completed-at: '2026-11-20T11:09:32Z'
findings:
- scope: passage
  quotes:
  - Caller (agent or code) ──▶ ticket_classifier ──▶ binding
  reason: The ASCII flow diagram restates the preceding sentence, in which the programmer
    binds a name such as `ticket_classifier` to either a prompt-backed agent or a
    Python function. Deleting the diagram loses no category, decision rule or inference,
    and it supports no prediction. The same route already survives as one sentence.
  level: warn
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/52cbe69fb477c7769e4f50d4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/outputs/review-framework-decoration.md
raw-output-sha256: 17a250e58a7fdaedebac54362e8d81aa7a14d87c596d2169703fd6f3d57efd91
---

# Review

## Summary

The note has four structures. Only one is decorative.

- **ASCII binding diagram (The mechanism).** Decorative; see the finding. It shows one name resolving to one of two implementations, which the prose above it already says in one sentence. It adds no information about the run-level binding choice or the declared-argument scoping. Those appear only in prose.
- **Two-direction leak list.** Load-bearing. Each direction names a distinct caller type and a distinct failure mechanism, and the next paragraph derives two separate prescriptions from them. Merging the two into one sentence would lose the asymmetry, which is the note's central claim.
- **Three-move taxonomy (refactoring, prototyping, relaxing).** Load-bearing. The note uses the distinction for an inference: only the first move preserves behavior, yet all three stay local to the binding. The categories also map onto linked definitions (codification, relaxing) rather than adding vocabulary the argument never uses.
- **Scope bullets.** Each bullet states a boundary condition that limits the main claim. None adds categories that go unused.

Delete the diagram, or replace it with something prose cannot carry, such as where run-level binding resolution happens.
