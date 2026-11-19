---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/be0e08c2ffcce06a628dcc79/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/be0e08c2ffcce06a628dcc79/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: f720129119974580af182d165bf2daaa
completed-at: '2026-11-17T13:17:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/f720129119974580af182d165bf2daaa/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 2a3c1fd6aae14ec921bdcbabed55510d031c00bdcd66344b5d858b832b3f5dc2
format: 2
---

# Review

## Summary

The note's main risk is that "evaluation" names both an activity and a role in the process. It handles this directly. The section "The same activity can perform different roles" separates the activity (examining results and forming a verdict) from its role (a wait or a specified requirement), and it states that "Calling an activity evaluation does not tell us whether execution waits for it or the specification requires it."

The process, the process specification and a claim about automation are kept distinct. One example says skipping review leaves "a gap against the specification, not that skipping review causes harm". That keeps the specification apart from the system's behaviour. The two linked notes are used as complementary claims, not as sources of the note's concepts, so attribution is clear. No passage permits materially different role assignments.
