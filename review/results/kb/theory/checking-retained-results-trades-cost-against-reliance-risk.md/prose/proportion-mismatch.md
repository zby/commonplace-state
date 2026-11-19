---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 005b200f7e094efe83ad0dd0594985d9
completed-at: '2026-11-18T16:01:58Z'
findings: []
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9c243412b15237ae1a932a78/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9c243412b15237ae1a932a78/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/005b200f7e094efe83ad0dd0594985d9/outputs/review-proportion-mismatch.md
raw-output-sha256: d9a61e52961d5017c3b9950847263e0b8f81a9a0eb5f86fa533c08613d7cfb61
---

# Review

The core claim is that how often to check a retained result trades the cost of checking against the risk of relying on stale or wrong content. The three opening paragraphs state this claim and develop both sides of it: the saving and how checking eats into it, then reliance risk through staleness and suppression. The two worked examples get the most space, and both serve the claim directly. They show a cheap, defined check on a claim that authorizes stopping, and an expensive judgment-based rerun on candidate-only output. The freshness section is short and derives from both examples. The "What a mechanical check requires" list is secondary but brief, and it ties back to the mark example. No secondary section outweighs the load-bearing material, and nothing warrants splitting out.
