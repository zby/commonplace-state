---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 56a09e77c61afb21f708bbe35f31d71b5fe838ceccbf94368f7c7786e6b9b1c6
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/08cd20205142130571e647c4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c479bc55423643ddb825da7ad43b3276
completed-at: '2026-11-20T18:55:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-unearned-generality.md
raw-output-sha256: fc5777ba2333505c892e2ed748a02d8d15fbcaeb5cf66dadcc881e33393315aa
format: 2
---

# Review

## Summary

The central claim uses three abstract terms: "on-balance judgments", "improvement" and "global measure". The concrete wording that would replace them is roughly "choosing which version to keep without scoring every version". The note works several distinct instance classes under the general terms: Python error messages, whole Python releases, public library hours, a Commonplace validator change and an AGENTS.md routing line. So the downgrade test does not demote these to special cases of one narrower class. The general claim also forbids something the narrower one would allow: it rules out demanding a complete score before choosing, in each of these settings. Abstraction sits in the title and the analytic sections where the argument needs it. The prose elsewhere stays concrete.
