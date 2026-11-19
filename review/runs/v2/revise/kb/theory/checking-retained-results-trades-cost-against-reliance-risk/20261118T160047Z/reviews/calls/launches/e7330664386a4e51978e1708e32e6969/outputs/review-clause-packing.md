---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A stale copy can also hide its own error: when a consumer treats the copy as exhaustive and stops on it, the copy suppresses the search that would have exposed what it misses"
    reason: "About 47 words, counting the link text, carry three ideas at once: the copy hides its error, the stop-and-suppress mechanism with two nested relative clauses ('that would have exposed what it misses'), and a trailing 'which is how' clause that identifies the mechanism with the linked note and whose link text adds another 'when' clause. The reader must hold the colon's expansion open while reading the identity clause. Splitting at 'which is how' (for example 'This is the mechanism by which [indexes lower recall ...].') keeps every relation and closes the first unit before the identity claim."
    level: warn
outcome: warn
---

# Review

## Summary

One sentence in the second paragraph is overloaded. It packs the hidden-error claim, the nested suppression mechanism and the identity with the indexes note into a single chain of clauses. Splitting it at "which is how" fixes this without losing any meaning.

The other sentences are under the length threshold or carry at most two ideas. The sentence "The check applies a defined rule (one-hop reach over tagged artifacts) to named inputs (the participating collections and nothing else), ..." has two parentheticals. Each resolves quickly, so they do not leave two long dependencies open at once, and the sentence is not flagged.
