---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Parametric continual learning keeps its own plasticity-stability and catastrophic-forgetting
    problems
  reason: Possible definition drift. The third paragraph calls parametric weight updating
    'continual learning' without qualification. The fourth paragraph then makes continual
    learning conditional on the system's own loop selecting a write, linked to selection-based
    learning, which contrasts with direct updates. Under the later criterion, ordinary
    online gradient updating might not count. The 'for retained candidates' qualifier
    may reconcile the two by exempting direct updates, but the text does not say so.
    Human confirmation is needed on whether 'continual learning' has one extension
    throughout.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/35341b0b128ac69b35bd153a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-internal-consistency.md
raw-output-sha256: ab090989aa4dd28a6a77774088171eb33fc2b95ddee7ff2c55992d1f77ec0f9e
format: 2
---

# Review

## Summary

The description, opening and final paragraph list the same governance functions under slightly different wording: select or choose, validate, authorize or assign an authority path, and coordinate. These lists agree. The broad learning criterion in the opening is consistent with the later statement that hand-authored maintenance is also learning. The three-form passage and its "need not touch all three" qualification are consistent with the description's "coordinate behaviour-changing updates across the representational forms".

One likely drift remains: the extension of "continual learning" changes between the parametric paragraph and the system-selects criterion. Because a qualifier may reconcile them, this is reported as INFO, not a contradiction.
