---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/08edfb2d684f9faedc24c8d2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b4e70f5925ff4ae894d0f33589d060fa
completed-at: '2026-11-22T09:34:30Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/outputs/review-unbridged-cross-domain.md
raw-output-sha256: fa34582a8b4e19cb79ea409601b6a80f98e1045de9d0d8bbb646b0f93c43f63f
format: 2
---

# Review

## Summary

The note's argument domain is deployed LLM agents that select edits to a
readable store. Cited evidence from other domains is either bridged or used
for a purpose that needs no transfer:

- **AlphaGo Zero and AlphaZero** illustrate where the definition of
  selection-based learning draws its line. The note does not cite them as
  evidence that LLM judges work.
- **PRODIGY, EURISKO and the Gödel machine** are presented as earlier cases
  of the same process, each with its admission mechanism named and its
  difference from the bet stated. That shared mechanism is the bridge.
- **Multiple-criteria decision analysis (Greco et al.) and stochastic
  dominance** supply the comparison rule. The note marks the transfer as an
  analogy and states its limit: open-ended work can add criteria, so it can
  widen the set as well as narrow it.
- **The Sutton and Javed interview and the harness-evolution study** come
  from the same domain as the argument, so they need no bridge.

No cited result is transferred across domains without a stated mechanism or
an explicit analogy marker.
