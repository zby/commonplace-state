---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/56b9cebe359c893c5bb6296b/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/56b9cebe359c893c5bb6296b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 3b670c1b79434ce5b130a3f35ab8a0ea
completed-at: '2026-11-16T22:18:30Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/3b670c1b79434ce5b130a3f35ab8a0ea/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 1cefe353881c2a7f560dc51d846a2bf348a29abba1b44ffd6fdb532f77248577
format: 2
---

# Review

## Summary

A one-paragraph version could state the core rule: a derived copy of recomputable truth must be machine-checked or absent. It would lose several load-bearing parts:

- **The asymmetry argument.** Bounded recomputation against silent, unbounded wrongness is what makes hand-maintained-and-trusted forbidden rather than merely risky.
- **The regime boundary.** The rule applies only where mechanical derivation makes verification Level A. Where verification is judgment, managed staleness applies and the hand-maintained dependent artifact is unavoidable. This boundary case is non-obvious.
- **The third class.** Recomputable-and-checked reconciles two otherwise conflicting notes, frontloading and fix-what-the-executor-can't-determine.
- **The four preconditions.** These are failure conditions. Precondition 3 excludes execution-generated evidence. Precondition 4 argues that the validator bottoms out instead of reopening the regress, and that a judgment-based derivation rule relocates the forbidden state.
- **Instances in different states of application.** These are the evidence for generalization.

Compressing the note to one paragraph would drop boundary cases and inferences, so the multi-section structure is justified.
