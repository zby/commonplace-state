---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'That is all antecedence buys: a comparison capable of failing, not a relation
    shown to track factory quality.'
  - 'Throughout, *better* means better under the declared relation: the claim is relation-relative
    and auditable, not a verdict on the factory''s quality over its open production
    family.'
  reason: 'The caveat that the declared relation does not certify genuine factory
    quality is stated four times: in the opening paragraph, at the end of the antecedence
    paragraph, and again in Scope bullets 1 and 2. The Scope bullets carry it fully,
    with the oracle point and the wrong-dimensions point. The two in-body restatements
    add no premise or boundary condition beyond those bullets. Cut the antecedence
    paragraph''s closing sentence, or reduce the opening sentence to a short clause
    such as ''better under the declared relation'', and let Scope hold the caveat.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/compression-bundle/detail-overhang.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/compression-bundle/detail-overhang.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/221df9137fc50027d9823dc6/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/221df9137fc50027d9823dc6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 62160d7634e9437596acce73f203e7d6
completed-at: '2026-11-16T21:59:32Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/62160d7634e9437596acce73f203e7d6/outputs/review.md
raw-output-sha256: e74818eb79fa22de41be26a83c04a2e85bf70da36c1ba58637a5aec483456213
format: 2
---

# Review

## Summary

Most of the note's detail matches the work it does. One caveat outgrows its role through repetition.

## Assessment

The note sets out four declarations, and most of its supporting detail does real argumentative work:

- The interleaved-process example in **Measurement over snapshots** is needed. Without it, "a measurement boundary drawn on a continuous process" would stay abstract, and the contrast with candidate admission would lose its force.
- The list of machinery parts (prompts, code, tools, tests and so on) takes up one sentence. It also blocks the likely objection that fixed model weights rule out the comparison.
- The paragraph on preserving the factory-development path is short and keeps three things apart: preservation, editability and compounding. Each distinction stops a likely misreading.
- In **Neither claim entails the other**, the operator case and the capable-builder case are two distinct counterexamples to reading improvement as learning. The manipulation clause is the inference step that comes out of them. The paragraph is long, but each part carries a separate step.
- The oracle-problem paragraph uses three short clauses, one for each difficulty, and connects back to evaluator location. It is in proportion.

The overhang is in the caveat about what the declared relation does not establish. The note states it in the opening paragraph, again at the close of the antecedence paragraph, and twice more in Scope. The Scope bullets are the right home for it because they separate the two cases: no oracle, and dimensions that are declared correctly but still wrong. Each in-body restatement repeats the same point without adding a condition. Compressing them would shorten the note without weakening it. The reader still meets the caveat where it is fully qualified.
