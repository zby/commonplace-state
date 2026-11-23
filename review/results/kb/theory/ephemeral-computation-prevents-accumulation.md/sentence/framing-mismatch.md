---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/ephemeral-computation-prevents-accumulation.md
note-sha256: d3a6a9e3e3da3e9b0cfdf1f37204cd3f0a4037ff53011b0c118feabbef1ffbc3
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 22de938edbb2472ba71c405f0591518e
completed-at: '2026-11-20T15:00:18Z'
findings:
- scope: passage
  quotes:
  - '[Codification](./definitions/codification.md) assigns an operation to a symbolic
    consumer.'
  reason: Frames codification in terms of a symbolic consumer rather than the actual
    mechanism (committing a rule or operation to a held-to-reference symbolic form),
    which excludes cases the mechanism covers such as adopting a pinned model package
    as a governing reference.
  level: warn
- scope: passage
  quotes:
  - The [codification–relaxing account](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
    addresses when to move operations between interpretation and assigned execution;
    it should not be read as a binary choice between learning and forgetting.
  reason: Frames the codification–relaxing trade-off as moving between interpretation
    and assigned execution, excluding relaxing an extracted decomposition to a more
    general learned or adopted-reference method.
  level: warn
contract: verdict
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/22de938edbb2472ba71c405f0591518e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/7b869970ac2b323dabe33074/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/22de938edbb2472ba71c405f0591518e/outputs/review-framing-mismatch.md
raw-output-sha256: 5ed8f612f085fe83728c316f2154d27e33f7463ebc2a890d9f61fb46a133214f
---

# Review

## Summary

Most of the note frames its core retention, cost, safety, and scope mechanisms at the right level of generality (the deployed system and causal state survival across runs). Only the codification section narrows the underlying mechanisms in ways that exclude cases those mechanisms cover.
