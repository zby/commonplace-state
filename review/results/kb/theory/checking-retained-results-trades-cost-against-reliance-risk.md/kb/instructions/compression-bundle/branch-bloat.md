---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 5aa390a7f38c41ef9c0812198210894c
completed-at: '2026-11-18T16:02:31Z'
findings:
- scope: passage
  quotes:
  - 'A mechanical check derives a retained result from, or compares it against, identified
    available inputs. Relying on one requires:'
  - '**A sufficiently trustworthy checker.** Testing or centralizing a validator lowers
    the cost of assurance but does not prove the validator correct.'
  reason: The 'What a mechanical check requires' section shifts from the note's trade-off
    claim to a general claim about when mechanical checks are possible and reliable.
    Conditions 1-3 restate what the completeness-mark section already shows ('a defined
    rule ... to named inputs'). They help explain why the mark's check is cheap and
    the connect report's is not, but the note never makes that link explicit here.
    Condition 4 (checker trustworthiness) opens a separate question, and the note
    itself leaves it open. The section is relevant enough to stay, but it reads as
    the start of its own note on preconditions for mechanical checking. Either tie
    it explicitly to check cost in the trade-off, or rehome the general enumeration,
    with the trustworthiness question, in a separate note or workshop lead. The right
    destination is unclear, so this is INFO.
  level: info
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/d1a68ed01a33433336cbaa6f/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/d1a68ed01a33433336cbaa6f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/5aa390a7f38c41ef9c0812198210894c/outputs/review.md
raw-output-sha256: cfc8e34d81a6caa684532b30dc2cb4f291c8c34bf3099f4179dbd75e6b4ca905
---

# Review

The note's main claim is in its title and its third paragraph: how often to check a retained result depends on check cost relative to the risk of relying on stale or wrong content. Accepting risk between checks is fine when the choice is explicit. The note works this claim through two contrasting cases.

Most of the side material supports that claim where it sits:

- The opening caveat that verification can be cheaper than derivation sets a boundary on the cost side.
- The suppression mechanism, linked to the indexes note and stated with its conditions, supplies the mechanism behind reliance risk.
- The completeness-mark and connect-report sections are the two cases the claim is worked through. Each has asides: semantic review sits outside the check, and the dependency set is hard to track. Both bound the cost or risk of their own case.
- "No known change does not establish freshness" sharpens the risk side: assurance dates from the last check. It is short and needed.
- The Scope and Open Questions sections are compact limits, not competing claims.

The only branch worth noting is the "What a mechanical check requires" section. It generalizes the mark's check into four conditions. The fourth condition, checker trustworthiness, adds a concern that the main argument does not need and that the note leaves as an open question. The section partly supports the cost contrast between the two cases, so removing it is not clearly right. Its best home, here with an explicit tie to check cost or in a separate note, is uncertain, so the finding is INFO rather than WARN.
