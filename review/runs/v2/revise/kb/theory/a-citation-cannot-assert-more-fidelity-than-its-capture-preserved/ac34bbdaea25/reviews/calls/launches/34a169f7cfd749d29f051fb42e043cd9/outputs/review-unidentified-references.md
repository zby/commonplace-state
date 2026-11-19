---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "epistack casebook work in the sibling `epistack-casebooks` repository"
    reason: "\"Epistack\" and its casebooks are named as the note's evidence base, but the note never says what epistack is or what a casebook contains. Is it a project, a method, or a corpus of legal cases? \"Sibling repository\" gives only its location. The surrounding text hints at court documents and news articles, but it does not identify the project. The author should add a brief inline identification; this review does not supply one, because neither the note nor its links state it."
    level: warn
outcome: warn
---

# Review

## Summary

Most named references are identified. ADR 046 is described inline as "the shipped verbatim-quote checker". The footer links carry short descriptions or titles that say what they are.

The exception is the evidence paragraph's "epistack casebook work in the sibling `epistack-casebooks` repository". This is the only named external project in the note, and it supplies the empirical support (eighteen of eighty-seven mismatched spans). Yet a first-time reader cannot tell what kind of project it is. A short gloss on first mention would fix this.
