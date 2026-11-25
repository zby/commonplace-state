---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Without explicit query-centered notes as roots, a top-level note that answers a live question can look orphaned if no other claim cites it, while a tightly linked cluster can answer each other's sub-questions in a closed loop without serving any real inquiry."
    reason: "About 45 words carrying five ideas: a fronted condition (no query-centered roots), a first failure (top-level note looks orphaned), its own condition (if no claim cites it), a contrasting second failure (closed-loop cluster), and that failure's qualifier (without serving inquiry). The two failure modes are independent and each brings its own condition, so the reader must hold the fronted condition across both. Splitting at 'while' into two sentences, each restating 'without query-centered roots' briefly or via 'Conversely,', keeps every relation."
    level: warn
  - scope: passage
    quotes:
      - "what Commonplace's reader-need labels (`grounds`, `mechanism`, `defined-in`, `evidenced-by` in [link vocabulary](../reference/link-vocabulary.md)) already express"
    reason: "The parenthetical list of four labels plus a link separates the subject 'reader-need labels' from its verb 'already express', while the reader is also holding the dash appositive's unresolved antecedent (the sub-question relation from the preceding clause). Two long dependencies are open at once. Reorder: 'what Commonplace's reader-need labels already express, such as `grounds`, `mechanism`, `defined-in` and `evidenced-by` in link vocabulary'."
    level: warn
  - scope: passage
    quotes:
      - "(how broadly an explanation transfers beyond the cases that produced it) in `kb/theory/` or fidelity and economy in `kb/reference/`"
    reason: "The 11-word gloss separates 'explanatory-reach' from its location phrase 'in `kb/theory/`', and the sentence is already about 40 words with a two-item 'such as' list. One long interruption is tolerable, but moving the gloss into its own short sentence or after the list would keep each quality bar next to its collection."
    level: info
outcome: warn
---

# Review

## Summary

Most sentences stay within two or three ideas. Two passages in the Unsettled section overload the reader. The root-question bullet packs two independent failure modes, each with its own condition, under one fronted condition; it should split at "while". The sub-question sentence inserts a label list between subject and verb while a dash appositive is still unresolved; moving the list after "already express" fixes it without losing anything. The Stakes opening sentence has a gloss that separates a quality bar from its collection, which is tolerable but could be reordered.
