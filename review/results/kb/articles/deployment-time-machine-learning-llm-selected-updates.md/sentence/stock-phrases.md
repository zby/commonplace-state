---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 113c49a86250430da7cf4d1d3b227564
completed-at: '2026-11-22T09:37:43Z'
findings:
- scope: passage
  quotes:
  - The loop itself is not new.
  reason: Fails the deletion test. The preceding paragraph already says 'The process
    itself is not new' and gives the precedents, and the next sentence begins 'The
    bet is that…', which sets up the contrast without help. The sentence is a not-X/but-Y
    setup that repeats established content. Deleting it loses nothing.
  level: warn
- scope: passage
  quotes:
  - Those payoffs carry real costs that belong on the ledger of any comparison with
    weight training.
  reason: A transitional framing sentence. The next sentence lists the costs directly.
    It nearly fails the deletion test, but it does mark the turn from payoffs to costs
    and names the comparison the costs belong to, so it is kept as information.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/74dd499e58cbb952bb36effe/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/outputs/review-stock-phrases.md
raw-output-sha256: 2e3d9383a29a13528c0117a78df45171bc8804c4f38ec24eefc34f735d04f40a
---

# Review

## Summary

The article avoids the listed stock patterns: there is no 'it's worth noting',
'at its core', 'key insight' or 'in other words' restatement. Several
'X, not Y' sentences carry content the paragraph needs, such as the rival
hypothesis to the Bitter Lesson and what the judge must do versus how its
weights work, so they pass. One sentence in the opening bet paragraph repeats
the previous paragraph's novelty disclaimer and fails the deletion test.
