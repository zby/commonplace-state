---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
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
  - It describes the limits of the ranking; it does not do the weighing or guarantee
    that a single stable ranking exists.
  - Compare the whole table with its earlier, shorter version
  reason: The mechanism for why pairwise on-balance judgments can guide a sequence
    of changes, and not just one choice, is thin. The note concedes that no stable
    ranking is guaranteed, and it guards against aggregate drift with one procedural
    instruction. It does not explain why successive pairwise preferences will not
    cycle or accumulate into a worse state, beyond that instruction. This part of
    the explanation is present but not yet hard to vary.
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/b4ba91be3d86e15bb4800b97/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-explanatory-reach.md
raw-output-sha256: 16b3683309beeb5aca813ace5e7ab7e33920473d42d9b9f9d0b977e1791bdb81
---

# Review

## Summary

The central claim is that on-balance judgments can guide improvement without a global measure. It comes with a mechanism that constrains it. A decision needs only a comparison between the alternatives actually on offer. That comparison is fixed by three choices: the alternative, who gains or loses, and the period. Value weights come from the operator and users, not from analysis. An unknown matters only if a plausible answer could reverse the choice. Varying premises changes the conclusion. If the alternative were an unbundled feature rather than a whole release, the message-level answer would be enough. If every unknown could reverse the choice, guidance without settling them would fail. If the purpose differs, the library example shows the same evidence favouring different hours. The claim can also fail: it fails if reasons offered for a preference cannot be checked independently, and the note names that check. The remaining thinness concerns guidance across a sequence of changes, recorded as INFO.
