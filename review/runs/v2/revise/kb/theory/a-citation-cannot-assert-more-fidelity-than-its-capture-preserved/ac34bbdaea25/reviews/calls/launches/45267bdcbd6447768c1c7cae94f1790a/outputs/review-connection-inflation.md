---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md)"
    reason: "The body links this note inline and fully states the relationship (this claim is the citation-fidelity instance of that general rule; ingest is the one chance). The footer entry is a bare title with no relationship label or context phrase, so it adds nothing beyond the body."
    level: warn
  - scope: passage
    quotes:
      - "- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)"
    reason: "The body links this note inline and articulates the relationship exactly (its mechanical-derivation-rule requirement is why a verbatim mark on a paraphrase cannot be trusted). The bare footer entry adds no typed relation or framing."
    level: warn
  - scope: passage
    quotes:
      - "- [A framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md)"
    reason: "The body links this note inline and states how it is used (the layering is forced because no boundary-preserving rival capture design exists). The footer entry repeats the link with no relationship semantics."
    level: warn
  - scope: passage
    quotes:
      - "- [Trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md)"
    reason: "The body links this note inline and explicitly frames it as the complement (authority earned post-capture versus fidelity fixed at capture). The bare footer entry adds no information."
    level: warn
  - scope: passage
    quotes:
      - "- [ADR 046 — Verbatim quotes are validated against their cited source](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)"
    reason: "The evidence paragraph already links ADR 046 and states its role (the shipped checker that found eighteen of eighty-seven verbatim-marked spans absent from their snapshot). The footer entry adds only the ADR's full title, no relationship or new navigational context."
    level: warn
outcome: warn
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
