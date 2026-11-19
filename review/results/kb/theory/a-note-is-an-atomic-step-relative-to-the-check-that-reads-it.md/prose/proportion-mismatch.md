---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
findings:
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old.
  reason: The Descartes and Lamport precedents take about as much space as the placement
    argument and are supporting context rather than load-bearing. They are explicitly
    framed as analogy, so this is not a mismatch with the core. It is worth watching
    if the section grows.
  level: info
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/df7752627f6b9a9d2f5cc978/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/df7752627f6b9a9d2f5cc978/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-proportion-mismatch.md
raw-output-sha256: 50a614716c1366a88c5a4c9de2cdd2d5898342407ec0c4ed6006aba76f400b9a
---

# Review

The core claim has two parts. Note size has two independent bounds, co-loading and checking. The checking bound is relative to a named check, and for the grounding check its unit is the unquoted source.

The two-bounds claim and the check-relativity get a compact but complete statement in the opening. They are then worked out in the most developed section, "Mechanism: for the grounding check, the unit is the unquoted source". That section explains the cost unit, why quoting removes a source from it, the two limits and the joint-support consequence. The corpus section and the reinterpretation of the paired experiment give the next-largest share and directly support the claim that the bounds diverge. The placement section is short and proportionate to its role.

The only secondary material of comparable length is the historical precedent passage in "What kind of number a step size is". It is marked as analogy and does not crowd out the mechanism, so the proportions hold. The INFO finding records it as the part to watch.
