---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'A citation raises four separable questions:'
  reason: 'Boundary case between enumerated items: the location question (is the quoted
    span the passage at the cited locator, or the occurrence the author meant?) does
    not map cleanly to wording, attribution, context or truth. The note does handle
    it later (''Occurrence is not location''), so the framework does not break, but
    the four-question list reads as exhaustive while a fifth question is treated separately.
    A translated quotation is a second strained case: wording against the translation
    and attribution to the original author pull apart, and the list does not say where
    the translator''s text sits.'
  level: info
- scope: passage
  quotes:
  - sources whose original is gone are out of scope
  reason: 'Extreme case at the scope boundary: an original that is gone but whose
    capture survives. The note''s own criteria cover it cleanly, since a pass is relative
    to the evidence used and a capture is listed as such evidence, and the capture''s
    bytes are retrievable, which the first clause of the same bullet covers. The exclusion
    therefore strains against the framework rather than marking a case it cannot handle;
    scope clarification (no capture either) would resolve it.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/1e0afbbf31bf20b9a9b2cd68/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/1e0afbbf31bf20b9a9b2cd68/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 6bde3c2775f64807b7da423438ece2fb
completed-at: '2026-11-18T16:04:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/6bde3c2775f64807b7da423438ece2fb/outputs/review-completeness-boundary-cases.md
raw-output-sha256: d52c04951994bf7b2602e27c67d080b7f01c6c252744455c4066fbfbad00dbf0
format: 2
---

# Review

The note carries three enumerations: the four questions a citation raises, the kinds of evidence a pass can be relative to (original, capture, intermediary extract, nothing), and the two directions in which normalization can err.

Boundary cases tested:

- Simplest instance: an exact quote of a single-occurrence span in a pinned local capture. Maps cleanly: wording passes, identity binds to the capture, context and truth stay open.
- Unattributed or anonymous source: attribution's author clause is vacuous, but the question still applies to the compared text. Maps cleanly.
- Text present only in a model's context or on another machine: the note explicitly addresses this under retained, accessible and used material.
- Location of a repeated span: handled in the body, but outside the four-question list (INFO).
- Translation: strained between wording and attribution (INFO).
- Original gone, capture retained: covered by the framework yet excluded by the Scope bullet (INFO).

No case clearly falls outside the claimed coverage. The four-question list is short and proportionate to its role, so the fix, if any, is scope clarification rather than adding categories.
