---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Evidence for the layering and for the failure of naive"
    reason: "Spread: the footer presents the ADR 046 checker result (eighteen of eighty-seven verbatim-marked spans absent from their snapshot) as evidence for the layering and for the failure mechanism the note describes, namely a paraphrase-layer passage marked verbatim. The linked ADR attributes those mismatches mainly to editorial omission, bracketed substitution, case changes and moved punctuation, which are edits to quotations rather than paraphrases mislabelled as verbatim. The result supports the claim that hand-asserted verbatim marks are often false. It does not support the stratification or the paraphrase-marking mechanism, yet the wording extends it to both. The other cited evidence, the 'epistack casebook work' in a sibling repository, is unlinked and unreported, so readers cannot recover what it shows."
    level: warn
  - scope: passage
    quotes:
      - "and no rival capture design drops the layering while preserving the commitments the framework has already made"
    reason: "This universal negative is the note's own unreported result. No rival search or list of candidates appears, but the sentence reads as an established finding and carries the 'not a design choice' conclusion. The linked framework-rule note treats a failed rival search as at most a candidate, never a certification, so the presentation is stronger than its status."
    level: warn
  - scope: passage
    quotes:
      - "It cannot work, and the reason is exact rather than merely practical."
    reason: "'Exact' asserts deductive status. The following argument is a derivation from the linked derived-copy rule, and its status can be recovered there. This is recoverable but emphatic; INFO only."
    level: info
outcome: warn
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
