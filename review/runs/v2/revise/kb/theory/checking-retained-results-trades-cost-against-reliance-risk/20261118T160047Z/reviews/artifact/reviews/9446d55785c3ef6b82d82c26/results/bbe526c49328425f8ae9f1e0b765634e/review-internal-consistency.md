---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9446d55785c3ef6b82d82c26/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/9446d55785c3ef6b82d82c26/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:24Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-internal-consistency.md
raw-output-sha256: 8fc85ab5e445ef8279a171ac341add5d96b2c2dcdd6e3a18fcffd9b39412ecc8
format: 2
---

# Review

## Summary

**Key claims by section:**

- *Opening:* retention amortizes work; checking spends part of the saving. Full recomputation on every use largely defeats it unless verification is cheaper. Staleness comes from separate update paths, and suppression can hide errors. Check frequency depends on cost relative to risk.
- *Mark:* stop-authorizing; derived at validation time and reused by later reads; enforcement is reactive, so the mark can be false between validations; assignment fit is out of scope.
- *Connect report:* candidate-only; assessment needs judgment; rerunning is costly and has broad dependencies; reuse can be reasonable; the risk is nonzero.
- *Freshness:* absence of a known change implies freshness only with full change delivery; assurance dates from the last check.
- *Mechanical check:* four conditions; they make a check possible, not free or current; the mark supplies conditions 1–3.
- *Scope / Open Questions:* the trade-off is qualitative; suppression is conditional; the contract is not behaviour evidence; checker adequacy and silent-omission prevalence stay open.

**Pairwise contradiction.** None. "Enforcement is reactive... a mark can be false in between" agrees with "Even the enforced mark can be stale until its head is next validated". The claim that the mark is worth enforcing agrees with the statement that the contract does not establish checker trustworthiness, because the note calls enforcement "attractive", not proven.

**Definition drift.** "Retained result", "check" and "stop-authorizing" keep stable meanings. "Mechanical check" is defined once and applied consistently. The connect report's checkable properties are described as not reconstructing judgment, which agrees with condition 1.

**Summary/body match.** The description matches the body: trade-off, check cost versus reliance risk, and the two worked cases.
