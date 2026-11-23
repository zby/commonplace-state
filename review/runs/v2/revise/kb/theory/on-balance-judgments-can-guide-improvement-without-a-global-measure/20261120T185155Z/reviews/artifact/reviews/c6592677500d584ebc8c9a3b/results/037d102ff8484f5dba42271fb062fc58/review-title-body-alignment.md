---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The body establishes the title''s claim and adds two commitments the title
    does not mention: a decision rule for evidence gathering (investigate an unknown
    only if a plausible answer could reverse the choice) and Commonplace''s declared
    objective (more useful and better-warranted knowledge work for the human judgment
    spent). Both serve the title''s claim, so this is not drift. The title just understates
    the note''s operational contribution.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 97741f5173cce4174ec58c3b4fe9e45d8d04e88050a179b7613b9a8669c70e5a
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/037d102ff8484f5dba42271fb062fc58/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/c6592677500d584ebc8c9a3b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 037d102ff8484f5dba42271fb062fc58
completed-at: '2026-11-20T18:52:48Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/037d102ff8484f5dba42271fb062fc58/outputs/review-title-body-alignment.md
raw-output-sha256: ba139e46c75614783b11506e5d60659117f479f4b13e409fc80d44f5ab2e4c8e
format: 2
---

# Review

## Summary

The H1 claims that on-balance judgments can guide improvement without a global measure. The body supports that claim directly.

- The Python 3.11-over-3.10 table shows a whole-release preference defended by reasons: which work changed, who gains or loses, and why it matters. No score is assigned.
- "What analysis can settle" argues that measurement can expose a trade-off but cannot supply its weights, which is why a global measure is not available to decide the case.
- "What Commonplace chooses to count" says that a partial order represents only the defensible preferences, and that the operator supplies the weighing.
- "What to do with an incomplete comparison" applies the judgment to KB changes. It also sets limits: binding requirements are not overridden, and a preference for the successor does not assign credit to a component.

The library-hours example widens the theme from uncertainty to whose work counts. It still illustrates a judgment that a total cannot settle, so it stays within the title's scope. There is neither claim drift nor scope drift. The only gap is that the title says nothing about the note's rule for when to investigate further, which the description does carry.
