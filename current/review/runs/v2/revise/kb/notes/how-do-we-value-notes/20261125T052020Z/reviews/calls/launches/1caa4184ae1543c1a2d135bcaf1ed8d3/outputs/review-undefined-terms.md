---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "propagate value from them down through answering notes and their subroutines"
    reason: "\"Subroutines\" is applied to notes without explanation. A reader can guess that it means notes that answer sub-questions for an answering note, but nothing in the sentence says so, and the programming metaphor is not conventional for notes."
    level: warn
  - scope: passage
    quotes:
      - "subroutine reuse, demand-root coverage"
    reason: "This list names two valuation signals that the note never defines. \"Subroutine reuse\" depends on the unexplained \"subroutines\" above. \"Demand-root coverage\" is new and only loosely connected to the earlier \"root questions\". A reader cannot tell what either signal measures."
    level: warn
  - scope: passage
    quotes:
      - "Where no fixed oracle decides theory fit"
    reason: "\"Fixed oracle\" is borrowed from testing terminology and is not glossed. A short gloss, such as \"a fixed test that decides whether a note fits the theory\", would make the sentence readable without following the link."
    level: info
  - scope: passage
    quotes:
      - "link-strength-weighted inbound links"
    reason: "\"Link strength\" is not explained. A reader cannot tell what makes one link stronger than another without opening the linked quality-signal notes."
    level: info
outcome: warn
---

# Review

## Summary

Most technical terms receive an inline gloss on first use: explanatory-reach (with a gloss and a link, which this KB's active vocabulary requires), answerable, validity versus learning value, test record versus fit in a working theory, warranted reader update and counterfactual use. "Reader-need labels" is explained by its examples, and root questions are described before the note relies on them. "Goodharting" is standard enough to leave as it is.

The problems cluster in the Unsettled section. That section introduces "subroutines" for notes and later lists "subroutine reuse" and "demand-root coverage" as signals to weigh. Neither signal is defined, so a first-time reader cannot follow the open problem about combining dimensions. "Fixed oracle" and "link strength" are smaller gaps that a short gloss would close.
