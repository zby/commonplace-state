---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the shipped verbatim-quote checker, run over that corpus, found eighteen of eighty-seven `verbatim`-marked spans that did not appear in their cited snapshot, with no false mismatches on manual audit"
    reason: "The figure is sourced to ADR 046, but the note omits context a reader needs to judge what it shows. ADR 046 reports a prototype run (not the shipped checker) over 87 candidates with 63 match, 18 mismatch and 6 unresolved. It also says the mismatches were dominated by editorial omission (`...`), bracketed substitution, case changes and punctuation moved inside the quotation boundary. The note offers the figure as evidence \"for the layering and for the failure of naive `verbatim` marking\". Without the mismatch composition, a reader would assume the 18 were paraphrase-layer passages marked verbatim, which is the note's central mechanism. The ADR does not say that. State the composition and the unresolved count, or narrow the evidential claim to what the mismatches show."
    level: warn
  - scope: passage
    quotes:
      - "hosted providers' output filters on mass verbatim reproduction add a third barrier"
    reason: "This is a concrete empirical claim about provider behaviour, given without a source or example. The note marks it as provider-contingent and does not rest the argument on it, so the risk is low."
    level: info
  - scope: passage
    quotes:
      - "epistack casebook work in the sibling `epistack-casebooks` repository"
    reason: "The evidence is attributed to a sibling repository that is neither linked nor described, so the reader cannot inspect it. ADR 046 is the reachable record, which keeps this at info."
    level: info
outcome: warn
---

# Review

## Summary

The note has one specific quantitative claim: eighteen of eighty-seven `verbatim`-marked spans failed the checker. It cites ADR 046 for it. Compared with ADR 046 (read through the note's link), the counts match. However, the note's framing goes beyond the record in two ways. First, it calls the run the "shipped" checker, while the ADR describes a prototype run. Second, it does not say what the mismatches were. The ADR attributes them mainly to editorial edits inside quotations, not to paraphrases presented as verbatim. That composition decides how far the figure supports the layering argument, so the missing context affects evaluation. The outcome is WARN.

Two smaller items are recorded as info. One is the unsourced remark about provider output filters, which the note itself marks as non-load-bearing. The other is the unlinked `epistack-casebooks` repository.
