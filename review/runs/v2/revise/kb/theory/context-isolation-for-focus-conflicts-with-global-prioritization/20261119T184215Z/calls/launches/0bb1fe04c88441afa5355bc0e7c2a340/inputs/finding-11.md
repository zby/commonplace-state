---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 1ae1638229e54e44b7812a2a1ae91aa4
completed-at: '2026-11-19T15:54:36Z'
findings:
- scope: passage
  quotes:
  - '**Claim mode: universal** under three conditions: bounded effective context,
    a competing workload whose comparison-sufficient live summary cannot sit beside
    deep task context without degrading focus, and open-ended trade-offs lacking a
    locally calibrated common scale (such as a numeric latency budget or dollar cost)
    that would let a compact injected threshold stand in for competing tasks.'
  reason: The second condition—and the consequence clause of the third—define the
    scope by negating the primary counterexample routes ("cannot sit beside deep task
    context without degrading focus"; "that would let a compact injected threshold
    stand in for competing tasks"), and the note states no refuter for its universal
    claim. Any system where a compact live portfolio summary or injected priority
    cue preserves both focus and prioritization is automatically classified outside
    the conditions rather than refuting the claim. While the note explains why abstract
    scalar bars fail without a locally calibrated scale (line 26), it gives no independent
    structural criterion for what workload or attention properties make a comparison-sufficient
    live summary degrade focus, turning the universalized headline into an outcome-insulated
    accommodation.
  level: warn
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/c4450809a25e8d0f2de105ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/outputs/review-explanatory-reach.md
raw-output-sha256: ed8d47c2df258d42b236c9bb170dd3f89a4c1dec4a3955c90ae7741b09e9bfed
---

# Review

The note does supply a genuine, hard-to-vary core mechanism: per-window attention feasibility pushes hard tasks toward context isolation, relational global prioritization depends on changing external competing work, and—where trade-offs lack a locally calibrated common scale—neither standing priority rules nor abstract scalar thresholds can substitute for concrete side-by-side comparison. Varying those premises (removing the context bound, making checks purely intrinsic, or introducing a locally calibrated metric such as a dollar cap or latency budget) predictably dissolves the conflict.

However, when the note states its claim in universal mode, it insulates that universal claim through outcome-defined preconditions and omits any stated falsifier. In particular, stipulating that a comparison-sufficient live summary "cannot sit beside deep task context without degrading focus" absorbs counterexamples (such as compact global summaries that do not noticeably hurt focus) as failures of the precondition rather than refutations, without explaining independently when summary load crosses into focus degradation.
