---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 402fd6f434ab4d4a913a580715d0113a
completed-at: '2026-11-20T18:52:54Z'
findings: []
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/eae949a14cdf013b0864a5a5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/402fd6f434ab4d4a913a580715d0113a/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 27b6cb373fbf991a3101b012ad063b9c55391bcad8a57df9d5f5c9dc4476dd9c
---

# Review

## Summary

Written as one paragraph, the note would read: "Prefer changes on balance by naming which work changed, for whom and why; you don't need a global score." That paragraph would drop several pieces that hold up the argument:

- **Settling part of a choice versus the whole of it.** The error-message case shows that settling a narrow choice does not settle the release choice. This is the boundary for when a firm answer is available.
- **Defaults versus individual applications.** Preferring 3.11 as a default is consistent with keeping a blocked application on 3.10. The default itself is open to challenge only if blockers become widespread. This is a failure condition for the main judgment.
- **Value disagreements versus uncertainty.** In the library-hours case, even perfect counts cannot settle the choice. This marks a limit on what more investigation can achieve.
- **A rule for when to investigate.** Investigate an unknown only if a plausible answer could reverse the choice.
- **A partial order instead of a total order.** A partial order describes where ranking stops but does not do the weighing.
- **Rules for incomplete comparisons.** Uptake is not a gain. A possible loss differs from an observed one. The reason for a choice tells you when to revisit it, and accumulated additions should be compared as a whole. Binding requirements take precedence over on-balance judgments. Preferring a successor does not assign credit to a component.

Each of these is a separate boundary case, decision rule or failure condition, so one paragraph would lose them. The multi-section structure is justified.
