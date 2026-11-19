---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This lets subsequent reads reuse the checked result.
  reason: The preceding sentence already says the validator derives membership when
    the head is validated rather than on every read; that subsequent reads reuse the
    checked result is entailed by it. The sentence adds no new information and can
    be cut.
  level: warn
- scope: passage
  quotes:
  - Even the enforced mark can be stale until its head is next validated, and a reused
    connect report reflects the KB as of its pass.
  reason: 'This recaps two points the example sections already made: ''Enforcement
    is reactive ... so a mark can be false in between'' and the connect report''s
    broad, as-of-pass dependencies. The section''s new work is the general principle
    (absence of a known change is evidence only if every relevant change reaches the
    checker) and the takeaway ''Assurance dates from the last check''. Cut the recap
    sentence, or fold the principle and takeaway into the framing paragraph or the
    end of the connect-report section.'
  level: warn
- scope: passage
  quotes:
  - The suppression mechanism is conditional.
  reason: 'The opening paragraph already states the conditions: ''This requires that
    the consumer actually stops and that the suppressed search would find more task-relevant
    material.'' Only the bullet''s second sentence does new work: it disclaims any
    claim about how often those conditions hold. Keep that disclaimer and drop the
    restated conditionality.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/6913b67f79b55d3e9ff7a88d/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/6913b67f79b55d3e9ff7a88d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: a9d4492f9aa14120a6029b4b47868c21
completed-at: '2026-11-18T16:03:35Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/a9d4492f9aa14120a6029b4b47868c21/outputs/review.md
raw-output-sha256: f75ddfc3d2f9dcf30a608d413f02416e50414eb0b5cf8bdadf046d97d6b105d5
format: 2
---

# Review

## Summary

The note is mostly compact. Each section has a distinct job: the opening states the trade-off, the two worked examples show contrasting outcomes, the conditions list gives the mechanical-check requirements, and Scope and Open Questions set the limits. Three small units repeat material that an earlier sentence already establishes. None of them is false or confusing. Each one costs space without changing what the reader understands or can do.

The freshness section gets the most attention. Its opening principle and closing line ("Assurance dates from the last check") are worth keeping because they turn the examples into a stance the reader can carry. The middle sentence only recaps the two examples. A short section therefore spends a third of its length repeating what the reader just saw.

Two non-obvious passes, noted to prevent false positives:

- The connect-report sentence about link resolution and required sections blocks a likely misreading, namely that partial mechanical checkability makes the report mechanically checkable. It earns its place.
- The closing sentence of the conditions list ("The mark's contract supplies the first three; nothing in it establishes the fourth") applies the list to the worked example. It is not a recap.
