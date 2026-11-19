---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content. Accepting some risk
    between checks can be right, provided it is an explicit choice rather than a hidden
    consequence of trusting the copy.
  reason: The body first states the core claim plainly in its third paragraph. The
    first two paragraphs set up the saving and the reliance risk, and the second paragraph
    detours through the suppression mechanism and its conditions. The title and description
    carry the claim, so a reader can find it. The note's distinctive commitment, that
    accepted risk must be an explicit choice, still arrives only after that setup.
    Opening the body with this sentence, then supplying the saving and risk paragraphs
    as its two sides, would make the claim more memorable.
  level: info
- scope: passage
  quotes:
  - These conditions make a check possible and worth relying on, not free or current.
    The mark's contract supplies the first three; nothing in it establishes the fourth.
  reason: The closing 'What a mechanical check requires' section is a free-standing
    list. It does not say how its conditions bear on the cost-versus-risk trade. Its
    link to the core claim, that these conditions decide whether a cheap check exists
    to set against reliance risk, is left for the reader to infer. One bridging clause
    would keep this section subordinate to the main claim rather than reading as a
    second topic.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/1104b18447e944c7a20c64d4/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/1104b18447e944c7a20c64d4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 4186182b36de49ad88ad41cc6f41de5e
completed-at: '2026-11-18T16:02:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/4186182b36de49ad88ad41cc6f41de5e/outputs/review.md
raw-output-sha256: 7ae146a9c76c76eddc9ca87c51b52dc226ffc7d20c3b6bfb3f0db7ea2cbcc662
format: 2
---

# Review

The note's strongest claim, stated using only its own commitments, is: how often to check a retained derived result depends on the cost of checking relative to the risk of relying on stale or wrong content, and accepting some risk between checks is right only as an explicit choice.

The title and the description make this claim prominent. The two worked examples clearly serve it: the completeness mark is a case of a cheap, defined check on a claim that authorizes stopping, and the connect report is a case of costly rerunning with an accepted, nonzero risk. The section "No known change does not establish freshness" sharpens the risk side. So the note passes. The claim is findable, and most later material supports it.

Two features make the claim less memorable than it could be. First, the body postpones its plain statement until after the saving/risk setup, which includes the conditional suppression mechanism. Second, the final mechanical-check section is not tied back to the trade-off. Each fix is small: lead the body with the "therefore" sentence, and add one clause linking the check requirements to the cost side of the trade.
