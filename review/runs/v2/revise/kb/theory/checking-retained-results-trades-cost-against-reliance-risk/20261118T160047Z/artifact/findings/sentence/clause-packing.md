---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: e7330664386a4e51978e1708e32e6969
completed-at: '2026-11-18T16:03:33Z'
findings:
- scope: passage
  quotes:
  - 'A stale copy can also hide its own error: when a consumer treats the copy as
    exhaustive and stops on it, the copy suppresses the search that would have exposed
    what it misses'
  reason: 'About 47 words, counting the link text, carry three ideas at once: the
    copy hides its error, the stop-and-suppress mechanism with two nested relative
    clauses (''that would have exposed what it misses''), and a trailing ''which is
    how'' clause that identifies the mechanism with the linked note and whose link
    text adds another ''when'' clause. The reader must hold the colon''s expansion
    open while reading the identity clause. Splitting at ''which is how'' (for example
    ''This is the mechanism by which [indexes lower recall ...].'') keeps every relation
    and closes the first unit before the identity claim.'
  level: warn
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/b026cb2e654c164a178c03d0/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/b026cb2e654c164a178c03d0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/e7330664386a4e51978e1708e32e6969/outputs/review-clause-packing.md
raw-output-sha256: fbace59511dbaacd33226cc0ee3d2f2d390c687a7c53eb2f77cf285708455210
---

# Review

## Summary

One sentence in the second paragraph is overloaded. It packs the hidden-error claim, the nested suppression mechanism and the identity with the indexes note into a single chain of clauses. Splitting it at "which is how" fixes this without losing any meaning.

The other sentences are under the length threshold or carry at most two ideas. The sentence "The check applies a defined rule (one-hop reach over tagged artifacts) to named inputs (the participating collections and nothing else), ..." has two parentheticals. Each resolves quickly, so they do not leave two long dependencies open at once, and the sentence is not flagged.
