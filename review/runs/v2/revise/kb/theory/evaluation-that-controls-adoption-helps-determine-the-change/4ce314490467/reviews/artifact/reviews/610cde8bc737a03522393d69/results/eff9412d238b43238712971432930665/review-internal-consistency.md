---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The first is a blocking dependency; the second is an unfulfilled requirement
  reason: The paragraph defines a specified task as one that 'can remain undone while
    execution continues' and contrasts it with an actual wait. However, the 'Required
    approval' case is presumably a specified task that also blocks. The text does
    not say whether specification and blocking are independent properties, so that
    one activity can be both, or two exclusive categories. Later passages imply independence,
    but the definition reads as a dichotomy. This is likely harmless drift, but a
    person should confirm it.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/610cde8bc737a03522393d69/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/610cde8bc737a03522393d69/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: eff9412d238b43238712971432930665
completed-at: '2026-11-17T13:08:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/eff9412d238b43238712971432930665/outputs/review-internal-consistency.md
raw-output-sha256: a4abb2c585526c9cc1f79edafdc29e1485a21052b198b11f28afea94d45524a8
format: 2
---

# Review

The title, description, opening, worked cases and Scope section agree. All say that a human wait and a specified human task are separable. They also agree that a full-automation claim must distinguish tasks performed automatically from requirements retired, and that optional assessment belongs to neither change.

"Required" is used consistently to mean assigned by the process specification. The note separately says that whether a specified task is useful or necessary is a different question, and "unnecessary" in the required-approval case is used in that second sense. The note keeps the two senses apart. The habitual-wait Scope entry is consistent with the definition of an actual wait, because the definition depends on whether execution proceeds, not on a written rule. "A non-binding recommendation still creates a dependency if the agent must wait for it" also applies the same criterion.

The one point needing confirmation is whether the wait/task contrast is a pair of independent properties or two exclusive categories. This is reported as INFO.
