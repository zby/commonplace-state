---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "propagate value from them down through answering notes and their subroutines"
    reason: "The literal meaning is that value would pass from a root query note to the notes that answer it, and then to the notes that answer their local sub-questions. 'Subroutines' is a programming image that the note never maps. It brings in call-and-return invocation and executable dependency, and it leaves the reader to work out that it means the notes answering sub-questions from the previous sentences. A literal replacement such as 'through answering notes and the notes that answer their sub-questions' is at least as clear and removes the unmapped connotation."
    level: warn
  - scope: passage
    quotes:
      - "subroutine reuse"
    reason: "The same unmapped image appears in the list of signals. The literal meaning is reuse of a note as the answer to a sub-question inside another note, which the first Unsettled bullet already states plainly. 'Sub-question reuse' or 'reuse as a sub-question answer' says this directly and keeps the term consistent with the earlier description."
    level: warn
outcome: warn
---

# Review

## Summary

The note is mostly literal. "Well-formed clutter", "closed loop", "Goodharting" and the "Stakes" heading are conventional or precise. They contribute contrast or name a recognized pattern, so they do not meet the test.

The one figurative choice that meets the test is "subroutine", used twice. The note defines the relation it means in literal terms: one note answers a local sub-question raised inside another. It then switches to a programming image without stating the mapping. The literal wording is no less clear, and it would keep one term for one concept across the Unsettled section. The pattern is local, so the outcome is WARN.
