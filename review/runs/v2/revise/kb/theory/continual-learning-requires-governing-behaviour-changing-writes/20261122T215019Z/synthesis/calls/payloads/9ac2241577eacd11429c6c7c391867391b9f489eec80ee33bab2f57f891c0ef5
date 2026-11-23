---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: d7ba0bab2a634f0aaf8e9234aa3f1a75
completed-at: '2026-11-22T21:53:15Z'
findings:
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: The opening states that continual learning requires governing behaviour-changing
    writes, but release engineering also governs such writes. The commitment that
    distinguishes this note's claim, that the system's own loop does the selecting,
    appears only in the final paragraph. It follows a form-placement aside and a release-engineering
    contrast. Moving one plain clause into the opening sentence, such as 'the system's
    own loop must select, validate, and authorize them', would make the full claim
    memorable on first read. The current text supports that clause, so this is a placement
    change, not a new claim.
  level: info
- scope: passage
  quotes:
  - Form placement is itself revisable. A stable natural-language rule may be codified,
    while a brittle symbolic rule may be relaxed back into prose
  reason: 'The last paragraph restates the governance claim, then adds several asides:
    form-placement revisability, release engineering, selection-based learning, the
    maintenance discriminator, cadence, and the subproblems governance relates. The
    form-placement aside belongs with the representational-form paragraph above, and
    moving it there would let the closing paragraph serve the core claim directly.'
  level: info
- scope: passage
  quotes:
  - belongs to a consumption path, not to stored bytes
  reason: The opening paragraph states the claim in its first two sentences, then
    introduces the learning criterion, behavioral authority, knowledge artifact, and
    system-definition artifact before the persistence conclusion. Each definition
    supports the argument, but together they make the opening read as terminology.
    Folding the artifact-role distinction into one short clause, with the links kept,
    would keep the claim in front.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/d7ba0bab2a634f0aaf8e9234aa3f1a75/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/44bf9792caeff73ef27fa0fe/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/d7ba0bab2a634f0aaf8e9234aa3f1a75/outputs/review.md
raw-output-sha256: d39ff86d862783ff7c6b67e5154db467393b63e46d8ba964f6d09147cf662eab
---

# Review

## Summary

The core claim is easy to find. The title states it, and the first two sentences state it plainly. In one sentence: in a deployed system, continual learning requires the system's own loop to select, validate, authorize, and coordinate durable behaviour-changing writes across representational forms; persistence alone does not do this. The later paragraphs serve that claim. They give the deployment constraints (cheap installation and regression validation), the forms a write can touch, and the governance problem.

The note's shape makes the claim less memorable than it could be, so the findings are INFO rather than WARN. The opening sentence leaves out the self-selection condition, which is what separates continual learning from ordinary governed software change. That condition appears only near the end of the final paragraph, among several asides. The simplest fix is to put the self-selection clause in the opening sentence and move the form-placement aside into the representational-form paragraph. Compressing the opening's run of definitions would also help. None of these changes needs a new claim. They only reorder commitments the note already makes.
