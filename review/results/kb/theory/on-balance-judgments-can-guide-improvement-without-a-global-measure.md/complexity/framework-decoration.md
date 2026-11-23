---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 402fd6f434ab4d4a913a580715d0113a
completed-at: '2026-11-20T18:52:54Z'
findings:
- scope: passage
  quotes:
  - 'Three choices fix the comparison:'
  reason: 'The three-question list (alternative, who gains and who loses, over what
    period) mostly gathers distinctions the earlier examples already showed. Later
    text uses it only loosely: the closing triple ''which work changed, whose costs
    count, and what observation would change its recommendation'' is a different set,
    and the ''period'' axis returns only implicitly in the revisit advice. Each bullet
    still gives a concrete anchor, so the list is mild summary scaffolding, not empty
    decoration.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/aa4d2376e3e9bcd2e8e0ffba/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/outputs/review-framework-decoration.md
raw-output-sha256: d35a3ad81bbc9ad0789260bf4ce3a8d4dd186a43fc1c52364e3cce02c05771b5
---

# Review

## Summary

The note has three structures that could be decorative.

**The Python 3.10/3.11 table.** This structure carries weight. Each row reports a specific observation, such as paired timing runs, the `TaskGroup` cleanup order, `tomllib` being present and `getargspec` being removed. Each row also states the scope or the party affected, for example "This checks one workload on two builds, not the speed of Python applications in general." The paragraph that follows argues directly against reading the table as a tally ("not that the table has three gains and one loss"), so the argument uses the table's gain/loss shape. One sentence could not keep the four observations together with their caveats about scope and about who is affected.

**The three-choices list.** This list is partly load-bearing; see the info finding. Its categories are discriminative, and each bullet points back to a worked case. However, the argument does not consistently reuse it as a framework.

**The total-order versus partial-order contrast.** This contrast does work. It states what the evidence can rank and explicitly does not claim that a partial order weighs anything ("it does not do the weighing or guarantee that a single stable ranking exists"). The note uses no notation or equations.

Nothing introduces vocabulary or categories that the argument later leaves unused, so the outcome is pass.
