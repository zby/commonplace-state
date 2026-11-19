---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A stale copy can also hide its own error
  reason: 'The suppression mechanism needs only a copy that is incomplete and treated
    as exhaustive. Staleness is not required: a copy that was wrong when it was produced
    suppresses the fallback search in the same way. The sentence names only the stale
    case. It does not say that only stale copies can do this, and the note''s framing
    elsewhere (''stale or wrong content'') covers the other case, so the sentence
    emphasizes one case without excluding the other.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/d85e6a1b64043d78bcbd2a08/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/d85e6a1b64043d78bcbd2a08/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: e7330664386a4e51978e1708e32e6969
completed-at: '2026-11-18T16:03:33Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/e7330664386a4e51978e1708e32e6969/outputs/review-framing-mismatch.md
raw-output-sha256: 43f9e7fb64c09f81d7c36c45438eb1a2510aa7b3515d051468700b4d890bda70
format: 2
---

# Review

## Summary

The note's mechanism statements are framed at the right level of generality. These were checked and hold:

- Staleness comes from separate update paths for the source and the copy.
- The trade-off is check cost against reliance risk.
- A check that recomputes on every use defeats the saving, unless verification is cheaper than derivation.
- A defined check on a stop-authorizing claim makes enforcement attractive.
- Rerunning discovery is hard because its dependency set is broad.
- The absence of a known change is evidence of freshness only if every relevant change reaches the checker.

The only framing note is minor. One sentence ties the hidden-error mechanism to staleness, although the mechanism covers any incomplete copy. The surrounding text already says "stale or wrong," so this is recorded as INFO only.
