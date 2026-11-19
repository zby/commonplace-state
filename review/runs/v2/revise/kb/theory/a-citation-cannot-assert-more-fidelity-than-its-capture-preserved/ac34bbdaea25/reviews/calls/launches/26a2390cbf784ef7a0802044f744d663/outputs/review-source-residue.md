---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "verification requires going back to the authoritative artifact (the sibling PDF)"
    reason: "The note claims generality over any captured long source, but this parenthetical assumes the evidence corpus's arrangement, in which every snapshot sits beside an authoritative PDF. It is stated as part of the general definition of the paraphrase layer, not as an example. Generalize it (\"the authoritative artifact, e.g. the original PDF\") or drop the parenthetical."
    level: warn
  - scope: passage
    quotes:
      - "a court restating a complaint; a news article quoting an order whose original is no longer served"
    reason: "These legal-domain cases come from the casebook corpus, but they appear in parentheses as illustrations of second-hand capture. They are framed as examples and do not overcommit the claim."
    level: info
outcome: warn
---

# Review

## Summary

The title and opening frame the claim generally: for any citation of a captured source, fidelity is bounded by the capture layer. The body mostly keeps that generality. It speaks of snapshots, layers, locators and authoritative artifacts. It ties the limits to general conditions (finite context, copyright) and names the provider-specific output filters as contingent.

One residue remains from the source setting. The paraphrase-layer bullet equates the authoritative artifact with "the sibling PDF". That is the casebook corpus's storage convention, presented as if it were part of the general mechanism. It is the only unframed narrowing, so the outcome is WARN. The legal second-hand examples are explicitly framed as illustrations and are recorded only as info.
