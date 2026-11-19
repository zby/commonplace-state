---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This distinguishes human work within the process from optional assessment of its
    results, rather than deciding who deserves causal credit for an improvement.
  reason: This positioning paragraph sits between the definitions and the first example.
    It disclaims a question the note never raised (causal credit) and points to a
    sibling note. That is mild apparatus before the examples that carry the claim.
    Moving it to the end, or cutting it to a one-line pointer, would let the definitions
    lead straight into the cases. It does not hide the claim, which the title and
    first sentence already state.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/1cc5fb71720bfad95b0aae1f/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/1cc5fb71720bfad95b0aae1f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: d60ba13d970b49cabc3f10bf68d4c52a
completed-at: '2026-11-17T13:07:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/d60ba13d970b49cabc3f10bf68d4c52a/outputs/review.md
raw-output-sha256: a9b419fdcadeb7dca05baf5571c37b1e2826acb26ed92e1450a71c12d4cbc99f
format: 2
---

# Review

## Summary

Core claim in one sentence, from the note's own commitments: removing a human approval wait differs from removing a specified human evaluation task, so a claim of full automation must say which specified tasks it preserves and which requirements it retires.

The note makes this claim prominent. The title states it as a claim. The first sentence of the body gives the distinction plainly, and the rest of the opening paragraph gives its consequence for automation claims. The second paragraph then defines the two terms the claim depends on: blocking dependency and unfulfilled requirement. The two hypothetical cases and the weekly-review example each apply that distinction. The closing sentence of "Name the process being automated" restates the claim's practical rule: retiring a review changes requirements; it does not automate that review. The Scope bullets are short boundary conditions and stay subordinate.

The only obscuring material is the third paragraph's positioning against causal credit and the before/after comparison note. It is brief and does not hide the claim, so it counts only as an INFO finding.
