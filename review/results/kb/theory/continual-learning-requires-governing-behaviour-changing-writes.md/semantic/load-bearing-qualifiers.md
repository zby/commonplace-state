---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 19df0882d6cddf5bd469e386aa4d02fbf9a4556f9672375b0ca96d7745f16e25
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:05Z'
findings:
- scope: passage
  quotes:
  - For deployed systems, persistence is insufficient
  reason: 'The deletion test shows that ''deployed'' does no work for this clause.
    The insufficiency of persistence is derived from the consumption-path account
    of behavioral authority, which holds for any system that retains artifacts. Deployment
    does carry weight elsewhere: it generates the two loop constraints (sparse online
    evidence, regression validation). The title is unqualified, so the narrowing affects
    only the description''s framing, not the filename-level claim.'
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/b80c7e6d771397eccccc6fbc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: c4707a47726b9254486f0fb192f8fa89ab4b94df45bc61bdf390de26dbada51d
---

# Review

## Summary

The title carries no narrowing qualifier. "Behaviour-changing" is load-bearing: it marks the contrast with content stored without authority. "Autonomous" and "during deployment" in the second paragraph govern a scoped consequence (the two added constraints) rather than the central claim, so they are correctly placed.

The only unnecessary narrowing is in the description, which attaches "for deployed systems" to the persistence-insufficiency claim. The argument for that claim does not use deployment.
