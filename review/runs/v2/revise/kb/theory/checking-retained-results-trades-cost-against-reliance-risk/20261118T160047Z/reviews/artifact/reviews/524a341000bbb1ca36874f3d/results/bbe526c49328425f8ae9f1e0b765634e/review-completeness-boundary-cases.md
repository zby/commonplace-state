---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Two retained results in this KB land differently.
  reason: 'The two worked cases occupy opposite corners: a stop-authorizing claim
    with a cheap, defined check (the mark) and a candidate-only result whose assessment
    needs judgment and whose rerun is costly (the connect report). The off-diagonal
    cases are not worked: a stop-authorizing claim whose membership depends on semantic
    judgment and so has no defined check, and a candidate-only result with a cheap
    mechanical recomputation. The general trade-off still maps both (high risk with
    high check cost; low risk with low check cost), so coverage holds, but a reader
    must derive the outcome for the stop-authorizing, no-defined-check case without
    guidance from the examples.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/524a341000bbb1ca36874f3d/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/524a341000bbb1ca36874f3d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:23Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 5b1063b27bbb4e8d4c1581dba8071e6a95ba5aefc10b146cc120d9037004fc18
format: 2
---

# Review

## Summary

The note has two frameworks to test: the general trade-off (check frequency depends on check cost relative to reliance risk) and the four-item list of what a mechanical check requires.

**The four conditions.** Boundary cases tested against the stated definition ("derives a retained result from, or compares it against, identified available inputs"):

- *Simplest instance:* the `complete: true` mark. The note states that the contract supplies conditions 1–3 and leaves 4 open. It maps cleanly.
- *Source absent:* content whose history has no later source. The footer link places this as a failure of condition 3. It maps cleanly.
- *Copy-only structural checks:* link resolution and required sections on a connect report. These compare the copy with the filesystem and the type spec, which count as identified inputs. They map, and the note explicitly says they do not reconstruct the judgment.
- *Change-detection checks* (e.g. hash comparison against a stored source digest): a comparison rule against identified inputs. They fit.
- *Scheduling:* whether a check runs at all is not a condition. The note deliberately excludes it ("possible and worth relying on, not free or current") and treats it in the freshness section.

No case falls outside the list's claimed coverage.

**The trade-off.** The general claim covers any retained derived result, and the off-diagonal cases map to it. The only strain is that the worked examples cover only the two clean corners (INFO above). The section count is proportionate to the argument, so expansion is not required. A sentence placing the semantic-membership case would suffice.
