---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Evidence for the layering and for the failure of naive
  reason: 'Spread: the footer presents the ADR 046 checker result (eighteen of eighty-seven
    verbatim-marked spans absent from their snapshot) as evidence for the layering
    and for the failure mechanism the note describes, namely a paraphrase-layer passage
    marked verbatim. The linked ADR attributes those mismatches mainly to editorial
    omission, bracketed substitution, case changes and moved punctuation, which are
    edits to quotations rather than paraphrases mislabelled as verbatim. The result
    supports the claim that hand-asserted verbatim marks are often false. It does
    not support the stratification or the paraphrase-marking mechanism, yet the wording
    extends it to both. The other cited evidence, the ''epistack casebook work'' in
    a sibling repository, is unlinked and unreported, so readers cannot recover what
    it shows.'
  level: warn
- scope: passage
  quotes:
  - and no rival capture design drops the layering while preserving the commitments
    the framework has already made
  reason: This universal negative is the note's own unreported result. No rival search
    or list of candidates appears, but the sentence reads as an established finding
    and carries the 'not a design choice' conclusion. The linked framework-rule note
    treats a failed rival search as at most a candidate, never a certification, so
    the presentation is stronger than its status.
  level: warn
- scope: passage
  quotes:
  - It cannot work, and the reason is exact rather than merely practical.
  reason: '''Exact'' asserts deductive status. The following argument is a derivation
    from the linked derived-copy rule, and its status can be recovered there. This
    is recoverable but emphatic; INFO only.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: f2419977ea2ca2adc64b5e1cec80307125cef1c3ddcd35727b8c85310517f854
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/8276d02492f7dae58386b754/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/8276d02492f7dae58386b754/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-epistemic-status-blur.md
raw-output-sha256: 0a8d239050e1e9545e2fde3f1853b41285858af32ac3b46a8b7700b207392367
format: 2
---

# Review

Claim inventory:

- **Fidelity is non-increasing and only re-capture raises it.** This is a derivation from the layer definitions and the lack of a mechanical rule for paraphrase. It is presented as derived, which is appropriate.
- **Layering is forced.** This is presented as derived from the context-window and copyright premises, plus an asserted absence of rivals. The rival absence is an unreported search result, stated as fact.
- **The three-layer taxonomy.** This is the note's own qualitative construction, introduced with "it stratifies". A qualitative decomposition needs only light proposing language, so this is not flagged alone.
- **The locator corollary.** It is marked "It follows", so it is a derivation.
- **The evidence footer.** It reports an observation, then attaches it to claims it does not test.

The main problem is spread from the footer. The checker found false verbatim marks. On the linked ADR's account, they were mostly editorial alterations of genuine quotations. That observation supports "hand-asserted verbatim is unreliable" but is presented as evidence for "the layering" as well. The unlinked casebook evidence cannot be assessed from the page.

The Open Questions section correctly marks the two open issues as unresolved.
