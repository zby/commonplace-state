---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A tag head's"
    reason: "\"Tag head\" is KB-specific and is never glossed. The sentence explains what the `complete: true` mark asserts, but not what a tag head is: an index page for one tag that links to the tag's members. A reader without KB context can only guess this from \"reached from the head in one hop\". Later sentences (\"when the head is validated\", \"until its head is next validated\") depend on this unexplained term. Add a short inline gloss."
    level: warn
  - scope: passage
    quotes:
      - "carrying the tag in the participating collections"
    reason: "\"Participating collections\" uses the KB's technical sense of collection, a registered term, and adds a participation relation. Neither is explained. The reader cannot tell which artifacts fall in scope of the completeness claim, which matters because the later check is described as reading \"the participating collections and nothing else\". A clause such as \"the collections that declare they use this tag\" would make the sentence self-contained."
    level: warn
  - scope: passage
    quotes:
      - "The validator performs the membership derivation"
    reason: "\"The validator\" appears with a definite article as though the reader already knows which tool is meant. Context lets the reader infer that it is some automated checker of tag heads, so this is minor. Naming it, for example as \"the KB's validation command\", would remove the guess."
    level: info
outcome: warn
---

# Review

## Summary

Most technical terms are handled well. The mark is a registered vocabulary term; it is linked, and its sentence glosses it by stating what it asserts. The connect report is linked and glossed as a record of "one discovery pass for a target artifact" that "proposes candidate links". Frontloading is linked, and its sentence paraphrases the idea as results computed before an LLM call. The completeness section, however, rests on two KB-internal terms with no gloss: "tag head" and "participating collections". A reader without Commonplace context cannot fully parse the scope of the claim the mark makes. Short inline glosses on first mention would fix both.
