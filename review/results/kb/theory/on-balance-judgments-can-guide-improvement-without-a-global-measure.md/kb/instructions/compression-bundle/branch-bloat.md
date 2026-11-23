---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 39144855239449a9a8dd0641aad617f0
completed-at: '2026-11-20T18:54:27Z'
findings:
- scope: passage
  quotes:
  - Some comparisons turn less on uncertainty than on **whose work the decision serves**.
  reason: 'The public-library staffing hypothetical supports the main claim: it shows
    that more measurement cannot settle a disagreement about whose loss counts, and
    the later ''Who gains, and who bears the loss?'' bullet relies on it. But it sits
    under the heading ''A release judgment: Python 3.11 over 3.10'', where it interrupts
    the release case with a different domain. Its point partly repeats the Python
    2 script-runner loss and the value argument in ''What analysis can settle''. Keep
    it, but its best place is unclear: it could move into ''What analysis can settle''
    next to the bullet it supports, or shrink to one sentence there.'
  level: info
- scope: passage
  quotes:
  - Compare the whole table with its earlier, shorter version rather than assuming
    that a succession of reasonable additions remains reasonable in aggregate.
  reason: 'This closing sentence adds a separate claim: a series of individually reasonable
    additions can be unreasonable in aggregate. It relates to the preceding point
    about when to revisit a judgment, but it needs its own mechanism and evidence.
    The note does not use it again. It could stay as a brief boundary remark, become
    an open question, or move to a note about cumulative context growth. Its destination
    is unclear rather than clearly wrong.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/39144855239449a9a8dd0641aad617f0/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/715f7a6229c5874bf615a55b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/39144855239449a9a8dd0641aad617f0/outputs/review.md
raw-output-sha256: 35677ef8c0f6a3aeb3d7f1a87b7204b673e3e2b902d41902bc5fe9b2def4714c
---

# Review

The main claim is in the title and the Commonplace section. When gains and losses fall on different work, an on-balance judgment gives criticizable reasons for keeping or rejecting a change without a global score. Uncertainties are worth investigating only if a plausible answer could reverse the choice.

Most side material directly supports that claim:

- **Python 2/3 text handling:** shows that a change can help one group and harm another.
- **`random.py` diagnostic:** shows a narrow comparison that can be settled. The "What is the alternative?" bullet reuses it.
- **3.11 table:** the worked release judgment.
- **Timing paragraph in "What analysis can settle":** separates measurement from weighting.
- **Partial-order paragraph:** sets the limits of a ranking.
- **Tag-trace and `AGENTS.md` examples:** apply the reversal test to Commonplace.
- **Factory-comparison and contrast links:** state the boundary conditions on what an on-balance judgment can override or credit.
- **Final paragraph on criticizable reasons:** finishes the "without a global measure" argument.

None of these should be removed.

Two items are useful but could be better placed. One is the library hypothetical: it is set inside the Python release section, and its point overlaps material elsewhere. The other is the final sentence about aggregate drift: it introduces a separate mechanism that the note does not develop. Neither weakens the central argument enough to justify a WARN.
