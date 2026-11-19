---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 326e79289f244bd5adc1f6080d20368b
completed-at: '2026-11-19T13:27:12Z'
findings: []
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/326e79289f244bd5adc1f6080d20368b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/a6a8333b57cc4e8e47840c84/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/326e79289f244bd5adc1f6080d20368b/outputs/review-general-before-specific.md
raw-output-sha256: d67d5966810f726a7398fcc8844d6231f950f85fa4c01ce577cf2f82d4afb572
---

# Review

The note's sections, in order, are:

1. An untitled opening that states the general claim.
2. "Missing context causes indiscrimination; defaults set the failure direction", which gives the general mechanism and its three failure manifestations.
3. "Splitting narrow-deep execution from wide-shallow triage", which gives the general architectural response. Its Commonplace mechanisms appear after the general split, inside the same section.
4. "Residual friction at the interface", which covers tensions in that response.
5. "Scope".
6. "Open Questions".

I checked each adjacent pair. In none of them is the earlier section a specific case whose general rule only appears in the next section.

- The only section framed as a tension is "Residual friction". It follows the general split it qualifies, which is the order the gate recommends.
- The specific examples (the Nostalgebraist account, ADR 138 and the unresolved frontier) are nested inside sections that state their general pattern first.
