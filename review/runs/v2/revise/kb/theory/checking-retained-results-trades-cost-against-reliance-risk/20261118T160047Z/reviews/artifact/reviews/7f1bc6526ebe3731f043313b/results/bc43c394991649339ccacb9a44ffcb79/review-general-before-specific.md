---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A mechanical check derives a retained result from, or compares it against, identified
    available inputs.
  reason: The general conditions for a mechanical check come after the completeness-mark
    section, which is the main instance of them ("The mark's contract supplies the
    first three"). The two sections are not adjacent, so the gate's adjacent-pair
    test does not flag them. Moving the conditions earlier would also split them from
    the two cases they are derived from, so the current order is defensible.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/structural/general-before-specific.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/review-gates/structural/general-before-specific.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/7f1bc6526ebe3731f043313b/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/7f1bc6526ebe3731f043313b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bc43c394991649339ccacb9a44ffcb79
completed-at: '2026-11-18T16:02:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bc43c394991649339ccacb9a44ffcb79/outputs/review-general-before-specific.md
raw-output-sha256: a77397232ddfdd4565c550c0dc77b4153fbeb9da2ffcfb5db04b4bb788ea1bbf
format: 2
---

# Review

The opening section states the general trade-off before any case: retaining a result saves work, checking spends some of that saving, and how often to check depends on check cost relative to reliance risk. The two case sections, on the completeness mark and the connect report, then show how that trade-off plays out differently.

Adjacent pairs:

- Intro → completeness mark: general before specific.
- Completeness mark → connect report: two parallel cases.
- Connect report → "No known change does not establish freshness": the freshness section draws a conclusion from both cases. It is not a rule that the connect-report section is an instance of, so the order is not inverted.
- Freshness → "What a mechanical check requires": neither section is a specific case of the other.

No adjacent pair puts a specific case before the general rule it exemplifies. The one INFO finding notes a non-adjacent ordering: the mechanical-check conditions generalize the completeness-mark example but appear later in the note.
