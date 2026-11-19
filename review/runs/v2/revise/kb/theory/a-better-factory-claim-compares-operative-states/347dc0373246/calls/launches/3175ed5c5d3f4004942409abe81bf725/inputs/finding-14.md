---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: c50667b742724b11b82a141c9cc38486
completed-at: '2026-11-16T22:00:06Z'
findings:
- scope: passage
  quotes:
  - This is not an extra virtue bolted onto the comparison
  reason: This sentence uses the elevation pattern ('This is not X; it is Y'). The
    section heading already states that preserving the path 'falls out of scope indexing'.
    The preceding sentence also derives the requirement from non-regression over the
    predecessor's capability set. If the sentence is deleted, the paragraph reads
    equally well and loses no content.
  level: warn
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e75f8e198a7de9bd08b3c4ec/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e75f8e198a7de9bd08b3c4ec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/c50667b742724b11b82a141c9cc38486/outputs/review-stock-phrases.md
raw-output-sha256: 17ce45398b2d215242051c7aa523382b6be9a3d6683e34df58fc8efad9fe0604
---

# Review

I applied the deletion test to sentences that match the listed patterns or behave like them. Only the elevation sentence in the preserved-path section fails it: both the heading and the previous sentence already make its point.

Other candidates survive. 'That is all antecedence buys: …' adds the limit that antecedence does not show the relation tracks factory quality. 'Both routes yield the same kind of claim …' introduces the distinction that the evaluator-location section uses.
