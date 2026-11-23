---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
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
  - Some comparisons turn less on uncertainty than on **whose work the decision serves**.
  reason: 'The library-hours paragraph carries a distinct claim (some disagreements
    are about whose loss counts, so more data cannot resolve them) but sits under
    the heading ''A release judgment: Python 3.11 over 3.10''. This is a placement
    issue, not a surplus section; the claim adds substance.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/5eaa68e42d5dcdc2274ccf3c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 70f671fa173c71e836e21cb4db3f068f53b9b4abf94af519821048a4ef361f5f
---

# Review

## Summary

The note has an untitled opening plus four headed sections and carries more distinct non-obvious claims than sections, so no section merely restates framing.

Distinct non-obvious claims, roughly in order:

1. A defensible preference between versions names the work that changed, who it changed for and why it matters; it needs no global score (opening, with the Python 2/3 text-handling case).
2. A narrow choice, such as between two error messages, can be settled firmly, but that does not settle the wider choice between releases (opening, `random.py` case).
3. A whole-release default can be preferred while particular applications rationally stay behind, because the losses fall on callers who can be identified and tested. Widespread blockers would challenge the default itself (3.11 section).
4. Some disagreements are about whose work the decision serves, so more measurement cannot resolve them (library-hours paragraph).
5. Analysis can expose a trade-off but cannot supply its weights. The comparison is fixed by the alternative, whose gains and losses count, and the period. Investigate an unknown only if a plausible answer could reverse the choice ("What analysis can settle").
6. Commonplace's declared objective, and the claim that a partial order shows where ranking stops without doing the weighing ("What Commonplace chooses to count").
7. A procedure for incomplete comparisons. Uptake is not a gain. A possible loss differs from an observed one. The reason for a choice tells you when to revisit it, and the whole should be compared with its predecessor. Binding requirements override on-balance judgments. Preferring the successor does not assign credit. Reasons make a judgment open to criticism without showing that the judge is competent ("What to do with an incomplete comparison").

Each headed section adds at least one of these claims, or a decision rule or boundary condition, that appears nowhere else. The only structural oddity is the info finding: the library-hours paragraph sits under a heading about Python releases.
