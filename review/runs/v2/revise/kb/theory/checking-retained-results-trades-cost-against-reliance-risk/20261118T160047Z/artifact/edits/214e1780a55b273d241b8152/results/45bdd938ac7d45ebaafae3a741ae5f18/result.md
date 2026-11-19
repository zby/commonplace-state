---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (undefined KB-internal term at first mention; fix is an inline gloss):
  ''A tag head''s `complete: true` mark asserts'' became ''A tag head is the curated
  index page for one tag, linking to artifacts that carry the tag. Its `complete:
  true` mark asserts''.'
- 'new-pattern (undefined KB-internal term at first mention; fix is an inline gloss):
  after ''in the participating collections'' added the parenthetical ''(the collections
  the KB declares as covered by its tags)''.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
input-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/214e1780a55b273d241b8152/results/45bdd938ac7d45ebaafae3a741ae5f18/candidate.md
candidate-sha256: 6584d0b347d2249a82cba9de3107f62abd7a217d9c6120268ecc5e8e1cd7847a
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/artifact/edits/214e1780a55b273d241b8152/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z
launch: 45bdd938ac7d45ebaafae3a741ae5f18
completed-at: '2026-11-18T16:10:30Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/calls/launches/45bdd938ac7d45ebaafae3a741ae5f18/outputs/result.md
raw-output-sha256: cb8f278d0f22e7c8367039cd8140d0f54bcb5028bbdeb8096d1b39410eb42126
---

# Report

Two changes, both in the first paragraph of "The completeness mark: a stop-authorizing claim with a defined check", within the assigned scope.

- `new-pattern` (an undefined KB-internal term at first mention, fixed by an inline gloss). Passage: "A tag head's `complete: true` mark asserts". It now opens with a separate gloss sentence. The sentence says the head is "curated" and links to "artifacts that carry the tag", not to all members, because a head may be minimal (`kb/types/tag-readme.md`). The `complete: true` mark is what asserts exhaustive reach. The mark link, the mark's claim and the "one hop" wording are unchanged.
- `new-pattern` (same pattern). Passage: "carrying the tag in the participating collections". Added "(the collections the KB declares as covered by its tags)". Participation is declared in a list in `kb/tags/COLLECTION.md`, not by each collection. For that reason the gloss does not use the reviewer's suggested wording ("the collections that declare they use this tag").

Not touched:

- Finding 3 (info, "The validator performs the membership derivation"): the scope says this finding is not required.

The note's claims, all links and the relied-on terms are unchanged. That includes the completeness-mark example and the use of "tag head" in later sentences.
