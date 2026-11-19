---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/5e01973e614bee73be015054/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/5e01973e614bee73be015054/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: 5b3677a41e544c2793109e03dd301aec
completed-at: '2026-11-17T13:07:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/5b3677a41e544c2793109e03dd301aec/outputs/review-framing-mismatch.md
raw-output-sha256: f3c221b76c4695a17ab0d459fbdf1a0ee8cd4008bd21887083cb038b5017e11d
format: 2
---

# Review

The note's mechanism is the difference between a blocking dependency (execution waits for a person) and a specified but unperformed task (the specification assigns work that can go undone while execution continues). The mechanism-bearing sentences frame it at that level. "An actual wait prevents execution from proceeding until a person acts" and "A specified task can remain undone while execution continues" name the two conditions directly rather than through a narrower proxy such as approval buttons or evaluation activities.

The note also guards against the obvious misframings. "Calling an activity evaluation does not tell us whether execution waits for it or the specification requires it" locates the distinction in role, not activity type. The Scope bullets cover the cases a narrower framing would exclude: an unwritten habitual wait still counts as a blocking dependency, and anticipated assessment can shape proposals without creating a stop. Examples such as the weekly sample review are offered as instances and are not presented as the boundary of the claim. No sentence excludes cases the mechanism covers.
