---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A tag head's
  reason: '"Tag head" is KB-specific and is never glossed. The sentence explains what
    the `complete: true` mark asserts, but not what a tag head is: an index page for
    one tag that links to the tag''s members. A reader without KB context can only
    guess this from "reached from the head in one hop". Later sentences ("when the
    head is validated", "until its head is next validated") depend on this unexplained
    term. Add a short inline gloss.'
  level: warn
- scope: passage
  quotes:
  - carrying the tag in the participating collections
  reason: '"Participating collections" uses the KB''s technical sense of collection,
    a registered term, and adds a participation relation. Neither is explained. The
    reader cannot tell which artifacts fall in scope of the completeness claim, which
    matters because the later check is described as reading "the participating collections
    and nothing else". A clause such as "the collections that declare they use this
    tag" would make the sentence self-contained.'
  level: warn
- scope: passage
  quotes:
  - The validator performs the membership derivation
  reason: '"The validator" appears with a definite article as though the reader already
    knows which tool is meant. Context lets the reader infer that it is some automated
    checker of tag heads, so this is minor. Naming it, for example as "the KB''s validation
    command", would remove the guess.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/82caf8b9164af22bbdc2cf45/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/82caf8b9164af22bbdc2cf45/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 54b268f3616f41b19bb6e34d68a910e5
completed-at: '2026-11-18T16:01:48Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/54b268f3616f41b19bb6e34d68a910e5/outputs/review-undefined-terms.md
raw-output-sha256: 9b93c92740cd8c2d470661737826df9db292e61d361438bace0c9b1cc6b18deb
format: 2
---

# Review

## Summary

Most technical terms are handled well. The mark is a registered vocabulary term; it is linked, and its sentence glosses it by stating what it asserts. The connect report is linked and glossed as a record of "one discovery pass for a target artifact" that "proposes candidate links". Frontloading is linked, and its sentence paraphrases the idea as results computed before an LLM call. The completeness section, however, rests on two KB-internal terms with no gloss: "tag head" and "participating collections". A reader without Commonplace context cannot fully parse the scope of the claim the mark makes. Short inline glosses on first mention would fix both.
