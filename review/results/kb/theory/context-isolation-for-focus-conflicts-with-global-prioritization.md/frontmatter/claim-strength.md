---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 91c3eddefea25fa164a0c1a0ff91aff9d159083adf76f7ac39755768454faab6
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 5e36d291e02142ad8df5bc8e2f3a242b
completed-at: '2026-11-19T13:26:03Z'
findings: []
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/5e36d291e02142ad8df5bc8e2f3a242b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/0b1638f28bbfee7bf253de7c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/5e36d291e02142ad8df5bc8e2f3a242b/outputs/review-claim-strength.md
raw-output-sha256: f0875511651ea1db3859e325ea7e7dc03afcf0b9be66655b6a6a0938470686ae
---

# Review

## Summary

The title "Context isolation for focus conflicts with global prioritization" asserts a contestable trade-off. An informed reader could reasonably argue the opposite. One position is that isolation is compatible with global prioritization because priorities, tolerances and budgets can be injected into the isolated worker's handoff. Another is that a capable model can load enough portfolio state beside its task context. The note itself names both as refutation conditions in its claim-mode paragraph. Common practice treats isolation mainly as a benefit for focus and verification, so a structural cost to cross-task prioritization is a non-obvious point. The claim is not a truism.
