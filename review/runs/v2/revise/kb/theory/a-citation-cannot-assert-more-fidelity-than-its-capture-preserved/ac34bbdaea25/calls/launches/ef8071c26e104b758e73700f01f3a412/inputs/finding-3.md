---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 45267bdcbd6447768c1c7cae94f1790a
completed-at: '2026-11-16T22:09:16Z'
findings:
- scope: passage
  quotes:
  - '- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md)'
  reason: The body links this note inline and fully states the relationship (this
    claim is the citation-fidelity instance of that general rule; ingest is the one
    chance). The footer entry is a bare title with no relationship label or context
    phrase, so it adds nothing beyond the body.
  level: warn
- scope: passage
  quotes:
  - '- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)'
  reason: The body links this note inline and articulates the relationship exactly
    (its mechanical-derivation-rule requirement is why a verbatim mark on a paraphrase
    cannot be trusted). The bare footer entry adds no typed relation or framing.
  level: warn
- scope: passage
  quotes:
  - '- [A framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md)'
  reason: The body links this note inline and states how it is used (the layering
    is forced because no boundary-preserving rival capture design exists). The footer
    entry repeats the link with no relationship semantics.
  level: warn
- scope: passage
  quotes:
  - '- [Trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md)'
  reason: The body links this note inline and explicitly frames it as the complement
    (authority earned post-capture versus fidelity fixed at capture). The bare footer
    entry adds no information.
  level: warn
- scope: passage
  quotes:
  - '- [ADR 046 — Verbatim quotes are validated against their cited source](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)'
  reason: The evidence paragraph already links ADR 046 and states its role (the shipped
    checker that found eighteen of eighty-seven verbatim-marked spans absent from
    their snapshot). The footer entry adds only the ADR's full title, no relationship
    or new navigational context.
  level: warn
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f92cc007f37acdcdd7914948/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f92cc007f37acdcdd7914948/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/45267bdcbd6447768c1c7cae94f1790a/outputs/review-connection-inflation.md
raw-output-sha256: 6644ad3687241367fc8c284b32dd58fbb7a4ec4fa5a6ef6c1f98325cd59759c7
---

# Review

## Summary

Five of the seven Relevant Notes entries are inflated: each repeats a link the body already uses inline with its relationship fully articulated, and each footer entry is a bare title with no relationship label or context phrase.

## Assessment

The gate does not flag a footer entry just because the body also links the same note. The problem here is that these five entries also fail its second question: they carry no relation such as extends or grounds, and no framing absent from the body. The body already explains each one precisely: the general rule this claim instantiates, the derivation-rule requirement it applies, the forced-constraint test it passes, the complementary authority claim, and the ADR that supplies the evidence. As written, the footer only duplicates those links.

Two entries are not inflated:

- `Structure inference needs capture at the decision surface` is absent from the body, and its context phrase ("decision rationale rather than quote fidelity") tells a reader how it differs from this note.
- `Collection prototypes` is absent from the body, and its phrase points to a concrete demonstration of the grounding-layer marker.

A fix is either to give each of the five entries a typed relationship and a phrase saying what the reader gains by following it from the footer, or to drop them and leave the inline links to do the navigation.
