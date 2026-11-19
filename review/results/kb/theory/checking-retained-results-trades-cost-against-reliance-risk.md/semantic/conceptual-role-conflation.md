---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:23Z'
findings: []
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/934d731f44bdc1b6f859bfb8/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/934d731f44bdc1b6f859bfb8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-conceptual-role-conflation.md
raw-output-sha256: a1d580ee71fcf9f87dbcdf8cf7d0911420121845fdd1799ceadc98dbb4ea43e1
---

# Review

## Summary

I inspected the passages that import, extend or apply concepts.

- **Frontloading.** "This is the saving [frontloading] argues for results computed before an LLM call, extended here to persisted artifacts." The passage separates the source account (frontloading's saving, scoped to pre-call computation) from the note's own extension (persisted artifacts). It is clear what is inherited and what is contributed.
- **Index suppression.** "...which is how indexes lower recall when they suppress retrieval..." This applies a linked mechanism to the stale-copy case. The next sentence restates the mechanism's conditions as requirements on this application. The mechanism is not redefined, and its attribution stays with the linked note.
- **The mark.** The section separates the term (`complete: true`), the claim it asserts (one-hop reach over tagged artifacts in the participating collections), the contract's permission (skip the `rg` search), the validator's check, and what falls outside it (assignment fit goes to semantic review). Mark, claim, check and checker are not collapsed.
- **The connect report.** The section separates the type contract (candidates to evaluate), the judgment that assessment requires, and the mechanically checkable residue.
- **Mechanical check.** The section defines the term once and lists its conditions. It then applies them to the mark ("The mark's contract supplies the first three"), keeping definition and application distinct.

No passage permits materially different role assignments.
