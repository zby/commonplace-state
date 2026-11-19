---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 6a33452f49e5477b8099d126092706ac
completed-at: '2026-11-16T22:21:23Z'
findings:
- scope: passage
  quotes:
  - Omission is the fallback, not the optimum.
  reason: The 'X, not Y' closer restates the preceding sentence, which already says
    both omission routes 'pay a build-time or hot-path cost that enforcement would
    have avoided'. Deleting it leaves the bullet reading equally well.
  level: warn
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/36293ebea524900c8ddc8fab/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/36293ebea524900c8ddc8fab/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-stock-phrases.md
raw-output-sha256: 03cd6b3759eab57103a3f101158858c59219a63b69f9e328de8e23c27f5b6e2b
---

# Review

Applied the deletion test to sentences matching stock patterns and to short summary sentences. Most survive: "A bounded, recoverable downside on one side; a silent, unbounded one on the other" adds the forbidden-rather-than-risky conclusion; "This looks like it reopens the regress, but it doesn't" introduces a substantive rebuttal; "This is the trivially checkable case" classifies the instance. One closing aphorism repeats its bullet's previous sentence and is filler.
