---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: '"Which tasks it preserves" can be read as the human tasks the claim leaves
    in place, which sits awkwardly with "full automation". The intended reading, tasks
    kept but now performed automatically, becomes clear only in the later sentence
    about distinguishing "tasks performed automatically from tasks no longer required".
    "Which tasks it automates" or "which tasks it keeps and performs automatically"
    would settle it where it first appears.'
  level: info
- scope: passage
  quotes:
  - Calling an activity evaluation does not tell us
  reason: 'On a first pass "an activity evaluation" can parse as a compound noun phrase
    (as in "calling an evaluation") before the reader reaches the intended structure:
    calling [an activity] [evaluation]. The trailing "it" resolves this, so the misreading
    is brief. "Labeling an activity as evaluation" would remove the garden path.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/87f83a1de3c6409f07bb3574/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/87f83a1de3c6409f07bb3574/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: 5b3677a41e544c2793109e03dd301aec
completed-at: '2026-11-17T13:07:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/5b3677a41e544c2793109e03dd301aec/outputs/review-parsing-ambiguity.md
raw-output-sha256: 8f35edae17578699030298c3aa97f174c4ae8285aa841f3fb3fb2ce9c218dbc0
format: 2
---

# Review

Most sentences parse cleanly. Pronoun antecedents are local and unambiguous: "one" in the first paragraph refers to a person, "It complements" refers to the distinction just stated, and "the first"/"the second" refer to the wait and the specified task. Negation scope is controlled: "not by itself evidence that…" and "not automation of that review" negate the intended constituent.

Two spots allow a plausible but short-lived misreading. Both are recorded as info because the next clause or a later sentence resolves them, so neither leads a reader to a wrong conclusion.
