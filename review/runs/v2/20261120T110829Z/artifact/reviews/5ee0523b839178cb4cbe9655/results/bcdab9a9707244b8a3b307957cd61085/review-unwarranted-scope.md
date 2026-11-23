---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The asymmetric-leak claims are supported by derivation from stated regime
    differences and by a constructed `ticket_classifier` scenario introduced with
    'Suppose'. The note reports no observed swap, in llm-do or elsewhere, that exhibits
    either leak. The derivation covers the class it claims, so this is not a scope
    overreach. A reader should still note that the claimed failure behaviors are derived,
    not exercised.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
note-sha256: 8f05aba89d28e81694031337bcbcbd44c8acc31a62a36cfac4e644310ab78a73
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/5ee0523b839178cb4cbe9655/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:22Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-unwarranted-scope.md
raw-output-sha256: 61a3d95aef8f274cd61bb9020287e2f0fa619624cb903986f0ea1cc67aea4aea
format: 2
---

# Review

## Summary

**Claimed scope.** In any system where prompt-backed agents and code share one interface, a programmer can rebind an operation without editing callers. The leaks differ by swap direction.

**Support presented.**

- A derivation from information hiding: a shared binding hides the implementation from call sites.
- A derivation from regime differences: prompt tolerance versus code strictness, and the latency, cost and fallibility of model calls versus functions.
- One described instance, llm-do.
- A constructed example.

**Exercised domain.** The derivation's premises hold for any system with a shared prompt–code binding, which matches the claimed class. The note does not generalize from the llm-do instance; it derives the claim. The surplus is bounded explicitly. The Scope section excludes structural signature changes and call sites without latency or error headroom, and it separates call invariance from behavioral invariance. The one predictive extension, that separate surfaces push toward big-bang rewrites, is marked as "an expectation, not an observed result". Scaling to hundreds of components and observability are left in Open Questions.

The claimed scope matches the support. The INFO finding records that the leak behaviors are derived and not observed.
