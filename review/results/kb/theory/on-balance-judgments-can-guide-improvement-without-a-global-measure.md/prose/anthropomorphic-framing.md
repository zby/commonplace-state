---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 32816be3282745488aa71d2e6743f69c
completed-at: '2026-11-20T18:53:20Z'
findings: []
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/134972688eef686827ba5bc5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/outputs/review-anthropomorphic-framing.md
raw-output-sha256: 779d3a09d65167ef8ebeaab731a3230dbe8f42aa389f7e67f811bc44c30b55b1
---

# Review

## Summary

The note mentions agents in a few places and uses ordinary operational verbs for them. One line "directs agents to instructions for a task they previously mishandled". Another places a task "near the limit of what the agent can use effectively". The note also says "an agent can offer reasons". None of these claims anything about model internals or beliefs.

The closing paragraph says that the reasons' availability "does not establish that any particular agent judges well". That is the note's explicit point about how to assess judgment quality, and it is hedged. It does not assert any cognitive capacity. I found no use of "knows", "understands", "believes" or similar terms that would need a technical substitute.
