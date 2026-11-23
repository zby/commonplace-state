---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - deployment evidence arrives online and is often sparse, so candidate writes must
    be cheap to propose and install
  reason: The stated reason partly misidentifies the mechanism. Online arrival and
    the need to act before a retraining cycle explain why writes must be cheap and
    fast to install; sparsity instead bears on how much evidence each write can rest
    on (sample efficiency, the axis the footer assigns to the retained-theories note).
    Framing cheapness as a consequence of sparsity emphasizes the wrong driver without
    excluding any case, so INFO.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/05bf2559e71b933a80a9fcaf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 248c7f483c8b49dc81090398a3e73f15
completed-at: '2026-11-22T21:53:34Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/outputs/review-framing-mismatch.md
raw-output-sha256: f3ebf686ecc98d6239f651719ee472453addce287795296057336f3e8f197e1e
format: 2
---

# Review

## Summary

The note's mechanism sentences are mostly framed at the right generality. Persistence versus governance, authority belonging to a consumption path, the weights-only updater freezing choices outside its reach, and the maintenance-versus-continual-learning distinction (who sits inside the loop and does the selecting) each name the mechanism they rely on and are not scoped narrower than it.

One causal link in the second paragraph ties install cost to evidence sparsity, when the operative driver is online arrival and latency relative to retraining. This emphasizes a slightly wrong reason but excludes no case.
