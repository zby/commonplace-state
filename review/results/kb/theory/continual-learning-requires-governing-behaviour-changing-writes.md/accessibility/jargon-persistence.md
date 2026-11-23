---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 5cfa66d6f22840dea82b6bc7e07bc81a
completed-at: '2026-11-22T21:51:24Z'
findings:
- scope: passage
  quotes:
  - Form placement is itself revisable.
  reason: '"Form" is the KB term representational form, grounded in the third paragraph
    and reused several times afterwards. Each later use sits within a paragraph of
    the grounding and next to concrete examples (natural-language rule, symbolic rule,
    prose), so the reader keeps the meaning; no change needed.'
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/5cfa66d6f22840dea82b6bc7e07bc81a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/c7ba5e8dbf348f5da382f323/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/5cfa66d6f22840dea82b6bc7e07bc81a/outputs/review-jargon-persistence.md
raw-output-sha256: f0b9a3a7b2f805492b932493ee0d589526bdb325e941c56885080caf1809bf8d
---

# Review

The KB-specific terms are mostly used once or twice after their grounding. "Behavioral authority" is glossed and returns only as "authority path". "System-definition artifact" is glossed in the first paragraph and reused once in the second. "Behaviour-changing write" recurs, but the first paragraph defines it in plain terms as a durable change to future behaviour, and later uses keep that context ("selects and retains it because deployment evidence bears on an improvement objective").

"Representational form" is the most persistent term. The three forms are named with examples, and later uses of "form" stay close to that grounding and sit beside concrete instances. The reader does not need to scroll back. The note is short, so no term drifts far from its definition.
