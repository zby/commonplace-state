---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:23Z'
findings:
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: 'Stated alone, the central sentence is close to a generic cost-benefit truism:
    almost any decision to check anything depends on cost relative to risk. The hard-to-vary
    content sits in the factors the body supplies: amortization over uses, separate
    update paths, stop authorization through suppression, judgment-dependence of the
    check and breadth of the dependency set. These factors appear through the two
    worked cases rather than as the named variables that decide where a retained result
    lands. The mechanism is present and constraining, but the headline claim borrows
    its reach from the cases.'
  level: info
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9a63d8fe2df9cc34203b8159/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9a63d8fe2df9cc34203b8159/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-explanatory-reach.md
raw-output-sha256: ea3a40e29575a6f7e09fd05570f526f18a7f743e72386c16a40d996b452f976f
---

# Review

## Summary

**Mechanism.** The note explains both sides of the trade-off. The saving comes from amortizing one derivation over many uses, and checking spends part of it. The risk comes from separate update paths, which cause staleness. Risk is amplified when a consumer treats the copy as exhaustive and stops, so the copy suppresses the search that would expose its omissions.

**Variation test.** Varying a premise changes the conclusion in the way the mechanism predicts:

- If verification is cheaper than derivation, per-use checking can still save work. The note states this.
- If the claim does not authorize stopping (connect report), suppression risk is lower, and reuse can be reasonable.
- If the check needs judgment or depends on a broad, hard-to-track set, it is costly and incomplete, and reuse becomes attractive.
- If every relevant change reached the checker, the absence of a known change would establish freshness. The freshness section makes this conditional explicit.

The two cases land differently because they differ on these premises, not by stipulation.

**Falsifiability.** A case would count against the claim if a cheap, defined check on a stop-authorizing claim were not worth enforcing, or if absence of a known change established freshness without full change delivery. Both are concrete.

**Ad-hoc accommodation.** "Accepting some risk between checks can be right, provided it is an explicit choice" is a normative condition tied to the suppression mechanism, not an escape hatch.

The headline sentence is thinner than the body (INFO above), but the explanation in the artifact constrains it.
