---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Testing or centralizing a validator lowers the cost of assurance but does not
    prove the validator correct.
  reason: The general requirement list names the role "checker", but this sentence
    switches to "validator", the KB-specific tool from the mark example. Using "checker"
    keeps the condition general. This is minor because a validator is clearly one
    kind of checker.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/5514a999d4ad9a21dc5591fd/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/5514a999d4ad9a21dc5591fd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 005b200f7e094efe83ad0dd0594985d9
completed-at: '2026-11-18T16:01:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/005b200f7e094efe83ad0dd0594985d9/outputs/review-source-residue.md
raw-output-sha256: ec8628f8e288fddd45a9ab343fc26e81c3e6deb5fa716499579d8e57450bb088
format: 2
---

# Review

The title and opening state a general claim about any retained derived result. The KB-specific material is explicitly framed as illustration: "Two retained results in this KB land differently", followed by sections named for each example. The frontloading link is explicitly extended "to persisted artifacts". The general sections use general terms ("retained result", "checker", "source"), and the one place that ties back to the mark marks itself as such ("The mark's contract supplies the first three"). The only slip is "validator" in the fourth condition, recorded as INFO.
