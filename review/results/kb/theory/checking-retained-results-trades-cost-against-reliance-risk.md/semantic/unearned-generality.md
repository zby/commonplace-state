---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 026ae5c9ff703a8247bfafda34b3a935d78abce327947bf045a54aa7d3e15bcf
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:24Z'
findings: []
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/27818959d99099634a32e84f/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/27818959d99099634a32e84f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-unearned-generality.md
raw-output-sha256: 41bd66bf2fd39ea8f1ff87e802d4e1dbd3f975f8ffb3405ede13b20cb57d8576
---

# Review

## Summary

**Abstract terms in the central claim:** "retained results", "checking", "reliance risk".

- **"Retained results"** stands in for the concrete cases the note works: a frontmatter completeness mark and a connect report. These are two different instance classes. One is a boolean claim derived deterministically from tagged membership. The other is a judgment-laden discovery artifact. The note works both under the general term and reaches different verdicts for them, so downgrading to either concrete term would demote the other to an unexplained special case.
- **The mechanism** does not depend on the artifact's form. Amortization over uses, separate update paths between source and copy, and suppression by a copy treated as exhaustive are properties of retaining a derived result. The note states this explicitly, and the linked index note argues that suppression applies to any artifact treated as exhaustive.
- **Forbids test.** The general claim rules out treating any retained derived result, including ones outside the two cases, as fresh merely because no change is known. It also rules out relying on an unchecked copy as an implicit rather than explicit risk choice. These are prohibitions, not just added coverage.
- **Distribution.** Abstraction is concentrated in the claim and the conditions list. The examples are concrete: `complete: true`, `rg`, participating collections, link resolution.

The abstraction is earned.
