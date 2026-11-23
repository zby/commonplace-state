---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c479bc55423643ddb825da7ad43b3276
completed-at: '2026-11-20T18:55:18Z'
findings:
- scope: passage
  quotes:
  - not a claim that every project should use the same measure
  reason: Here 'measure' names Commonplace's declared objective (useful, better-warranted
    knowledge work per unit of human judgment). The title uses 'global measure' for
    a scoring function that ranks every version. On one reading the objective is a
    criterion that guides on-balance judgments. On the other it is itself a measure,
    which the title says is unnecessary. The surrounding paragraph ('A partial order
    can represent the preferences...', 'it does not do the weighing') settles it in
    favour of the first reading, so the blur is not material.
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/6987de65991fc374c79d6eec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-conceptual-role-conflation.md
raw-output-sha256: ca085c6f43ab01faf4cde6168330ef363c1005c8d07c17e7fa59a6d6c2f9e44c
---

# Review

## Summary

The note's main conceptual moves are kept apart: an on-balance judgment, the reasons offered for it, the partial order that represents defensible preferences, and the objective Commonplace declares. The links to the factory-comparison and contrast notes are framed as applications ("can require", "does not identify which component deserves credit"), not as inheriting a definition. The one plausible blur is the word "measure" applied to the declared objective. Nearby text resolves it, so the verdict is PASS.
