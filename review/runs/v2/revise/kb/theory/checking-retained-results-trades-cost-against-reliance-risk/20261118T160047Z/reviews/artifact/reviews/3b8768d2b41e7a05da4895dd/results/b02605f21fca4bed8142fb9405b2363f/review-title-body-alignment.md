---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'A mechanical check derives a retained result from, or compares it against, identified
    available inputs. Relying on one requires:'
  reason: 'The body also lists the conditions a mechanical check needs before it can
    be relied on: a rule applied without judgment, a locatable copy and source, a
    source available at check time, and a sufficiently trustworthy checker. It separately
    establishes that the absence of a known change does not establish freshness. Both
    sections bear on how cheap and how reliable a check is, so they stay within the
    title''s trade-off. They do extend its scope slightly, from the trade-off itself
    to the preconditions for mechanical checking. This needs no title change.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: dbf8868e9c69bbc93853a7597247757556602796f9ea19a20828e61f3d5e222f
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/3b8768d2b41e7a05da4895dd/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/3b8768d2b41e7a05da4895dd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: b02605f21fca4bed8142fb9405b2363f
completed-at: '2026-11-18T16:01:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/b02605f21fca4bed8142fb9405b2363f/outputs/review-title-body-alignment.md
raw-output-sha256: e7db8abe939d54c001af3760a02842c8ed3ed9280c0e775eb83f55cf888cb96c
format: 2
---

# Review

## Summary

The body supports the H1 claim. It sets out the saving a retained result provides and says checking spends part of it. It then names the reliance risk: staleness through separate update paths, and suppression of the search that would find omissions. It concludes that how often to check depends on check cost relative to reliance risk. Two worked cases apply the trade-off. The completeness mark has a cheap, defined check on a claim that authorizes stopping, so it favours enforcement. The connect report has expensive rediscovery with broad dependencies, so reuse can be reasonable.

The later sections, on freshness and on what a mechanical check requires, elaborate the cost and reliability side of the same trade-off. There is no claim drift. The scope extension is minor and is recorded as an info finding.
