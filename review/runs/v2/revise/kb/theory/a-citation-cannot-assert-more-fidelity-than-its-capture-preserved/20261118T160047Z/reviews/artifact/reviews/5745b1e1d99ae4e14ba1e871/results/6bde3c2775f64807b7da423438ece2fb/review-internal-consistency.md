---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Four questions, one answered mechanically
  - An identity check answers part of the second question (below).
  reason: The heading says one question is answered mechanically, but the section
    immediately assigns part of the attribution question to an identity check, which
    the later section describes as a mechanical checksum comparison. Reconcilable
    if 'answered' means fully answered, but the heading compresses away the partial
    mechanical answer.
  level: info
- scope: passage
  quotes:
  - A string check answers only the wording question.
  - an inexpensive occurrence check can justify treating mismatch as failure
  reason: Likely definition drift. The description distinguishes 'a wording check,
    an occurrence check and a source-identity check', and the 'What makes exact meaningful'
    section separates normalized equality from occurrence uniqueness. Yet the first
    section uses 'string check', 'quote check' and 'occurrence check' for the same
    wording test, and the opening defines the quote check as the occurrence test.
    A reader cannot confirm whether wording and occurrence are one check or two.
  level: info
- scope: passage
  quotes:
  - A mismatched or unreadable file is a failure, not an invitation to find another
    copy.
  - Missing bytes therefore report as unverified, never as passed.
  reason: 'Apparent tension in outcomes: an unreadable file is a failure, while missing
    bytes are unverified. The two may be intended as distinct cases (file present
    but unreadable versus capture not available on this machine), but the note does
    not draw the line, and the severities differ.'
  level: info
- scope: passage
  quotes:
  - sources whose original is gone are out of scope
  reason: 'The body says a pass is relative to the evidence used, which may be a capture
    rather than the original, and the same Scope bullet covers sources with retrievable
    bytes. Excluding sources whose original is gone sits uneasily with that: a surviving
    capture is exactly the case the capture-relative account handles. Probably intends
    ''no retrievable capture either'', which needs confirmation.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5745b1e1d99ae4e14ba1e871/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5745b1e1d99ae4e14ba1e871/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-internal-consistency.md
raw-output-sha256: 9773e599572612abd28a36610aa05c4e0bc1f9e6e59e0b5d2df851fd057ea0e9
format: 2
---

# Review

The note's key claims are consistent across sections: a quote check tests occurrence under a normalization rule; exactness depends on the rule and on unique occurrence; a pass is relative to the evidence used, bound by checksum to a capture and no further; missing evidence cannot pass; exactness and second-hand provenance are independent. The title's claim, that a citation's verified fidelity is bounded by its capture, agrees with the body's "The binding stops at the capture".

No pairwise contradiction was found. The findings are drift and compression points that need author confirmation: the heading's "one answered mechanically" against a partly mechanical identity check, shifting names for the wording/occurrence check, an undrawn line between unreadable and missing files, and a scope exclusion that the capture-relative account appears to cover.
