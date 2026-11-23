---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 248c7f483c8b49dc81090398a3e73f15
completed-at: '2026-11-22T21:53:34Z'
findings:
- scope: passage
  quotes:
  - the force with which a consumed artifact determines what the system actually does
  reason: 'The gloss identifies behavioral authority with force alone. The linked
    definition says behavioral authority records the consumer, the channel, and the
    force; force is one of three components. The surrounding claim (authority belongs
    to a consumption path, not to stored bytes) matches the target, so the mismatch
    is a narrowing rather than a different concept. Consider ''how a consumed artifact
    shapes behaviour: through which consumer and channel, and with what force''.'
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/e4d97a2a7436eb0281866d62/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/248c7f483c8b49dc81090398a3e73f15/outputs/review-concept-attribution.md
raw-output-sha256: 7c3bb9642e26617d1ea8ff56269faafc9202ca7199e1d00561dce0612a9824f2
---

# Review

## Summary

Each identity claim was checked against its target's head or the relevant definition:

- Learning per [Learning is not only about generality]: the note's "any durable change in a system's capacity to adapt to its environment" paraphrases the target's Simon quotation faithfully.
- Knowledge artifact ("consumed as evidence or advice") and system-definition artifact ("consumed to instruct, constrain, route, validate, or train") match the target definitions' authority-path families.
- "persistent deployment-time learning" matches the target's term for an evidence-responsive selection loop completing the artifact-revision path within operating cadence.
- "the software learns by selection that people perform on it" matches the selection-based learning definition's first level ("learning by selection that others perform on it"), and "the system does the selecting itself" matches its self-improvement level.
- The proposal-selection loop's "search, reject-capable evaluation, and operative retention" matches the target's three functions.
- Codification and relaxing: "a brittle symbolic rule may be relaxed back into prose" specializes the target's relaxing (replacing an extracted component with a more general one); the target also discusses switching components between prompts and code and brittleness as a relaxing signal, so the attribution holds.
- Representational-form coevolution owning the broader cross-form trade space matches that note's own statement that this note defers to it.

Only the behavioral-authority gloss narrows its target, and only at INFO level. All targets resolved.
