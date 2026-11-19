---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: f24a9e255fc219f95881a1840844ab934c05d25ce0e5882af047e9fd5401a95f
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: b77f299bcf63471da4849e1261722ecb
completed-at: '2026-11-16T22:18:10Z'
findings: []
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/dc28a3da284f5e9bd92dfc70/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/dc28a3da284f5e9bd92dfc70/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/b77f299bcf63471da4849e1261722ecb/outputs/review-claim-strength.md
raw-output-sha256: e2c74ed8614e95dabcd84380e3d41aec72aac6cb17affbab1768d30ecc7852ef
---

# Review

## Summary

The title "A derived copy of recomputable truth must be checked or absent" is contestable. An informed practitioner could reasonably argue the opposite: that hand-maintained derived copies are acceptable when edit discipline, code review or tolerable staleness keeps them close enough to the source. Denormalized fields, cached summaries and copied lists are maintained by hand in many working systems. The title excludes that middle state, so it takes a position that someone could dispute. It is not a truism, and it is sharper than a generic "derived data should be kept in sync".
