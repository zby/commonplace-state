---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/76aeb5eafe6f52b9ae499797/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/76aeb5eafe6f52b9ae499797/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: 0a76f22089bb429da455bca2d6997cae
completed-at: '2026-11-17T13:16:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/0a76f22089bb429da455bca2d6997cae/outputs/review-framing-mismatch.md
raw-output-sha256: 9f71fcdddc327fe8d86ef9d5f76055197be0efde8d2848cc5e990368e06fa677
format: 2
---

# Review

## Summary

The note's mechanism-bearing sentences name their mechanism at the right level of generality:

- "An actual wait prevents execution from proceeding until a person acts" names the mechanism, which is a blocking dependency in execution.
- "The second is an unfulfilled requirement" names the contrasting mechanism, which is a gap against the specification. The note then explicitly withholds the stronger framing that the gap is evidence of degradation.

The worked examples are framed as instances ("Consider two hypothetical cases", "Suppose adoption is automatic"). They do not limit the distinction to agent instructions or weekly reviews. "The same distinction applies to subsequent revisions" widens the scope rather than narrowing it. The Scope bullets frame the habitual wait as an actual wait rather than as a requirement, which matches the mechanism given earlier.

No sentence frames its claim in a way that excludes cases the mechanism covers or that misidentifies the mechanism.
