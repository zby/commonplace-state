---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 9528731444671204248c1c7fed0181134ac72d8ab18a30d0a486df4eae922edd
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/56dd885d5f3c085b1bc56317/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/56dd885d5f3c085b1bc56317/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: 7cf134eb55ed4527b47f7fa442062bf1
completed-at: '2026-11-17T07:43:23Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/7cf134eb55ed4527b47f7fa442062bf1/outputs/review.md
raw-output-sha256: e1adbbf29606933e472764fdae07eb69e27add7267585be657e3cf8fbc062adf
format: 2
---

# Review

## Summary

The main claim to preserve is in the title and opening: human evaluation that adoption must wait for is part of the operating process, while assessment that only measures an adopted change is not, and automation has to address only the first. No side material competes with this claim. Each piece outside the core distinction either sets a boundary on it or blocks a likely misreading.

## Side material checked

- **Comparison with the before/after improvement note.** This sentence keeps the distinction separate from claims about causal credit or improvement. It sets a scope boundary, so it stays.
- **The two hypothetical cases.** These are the note's own contrast and carry the argument. In the required-approval case, the sentence about removing the stop points to the routine-approvals note. It is one sentence that hands the issue to a sibling note, and it keeps "always approves" from being read as evidence that the stop is dispensable. It does not develop a competing claim.
- **"A non-binding recommendation…" and "a program can apply human-authored acceptance rules…".** Each sentence shows that the test is dependency, not the label "evaluation". Both are needed boundary conditions.
- **"Name the process being automated" (monitoring and rollback).** This is the section most likely to look like a branch, because it extends the argument from adoption to continued operation. It still applies the same dependency test and closes an obvious loophole: moving the human check after adoption could otherwise be counted as removing it. It limits how the main claim can be misused, so it belongs here rather than in a separate note.
- **Scope bullets.** The bullets cover anticipated influence, the gap between a written requirement and actual execution, and the point that removing a stop does not show the resulting changes are good. Each is a short boundary condition on the main claim and opens no new line of argument.

No branch needs removal, demotion or rehoming.
