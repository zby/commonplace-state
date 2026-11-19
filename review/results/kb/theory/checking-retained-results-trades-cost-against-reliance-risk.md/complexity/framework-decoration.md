---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 266f6db8202e453b8a399fe78a9fed3b
completed-at: '2026-11-18T16:01:44Z'
findings:
- scope: passage
  quotes:
  - The mark's contract supplies the first three; nothing in it establishes the fourth.
  reason: 'The four-condition list is the note''s only framework-like structure. The
    argument uses it: the note applies it to the mark by number, and the footer applies
    condition 3 to the history contrast. However, the list is never applied explicitly
    to the connect report, where conditions 1 and 2 are the ones that fail (judgment
    is needed, and the dependency set is broad). Applying it there would make the
    second example use the structure too. This does not make the list decorative.'
  level: info
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/cff1081d95788536b9277835/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/cff1081d95788536b9277835/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/266f6db8202e453b8a399fe78a9fed3b/outputs/review-framework-decoration.md
raw-output-sha256: 0fd3923886a1955ab49d3f3add1e41741120c933ce937ab36acc64b8f1e26310
---

# Review

## Structures assessed

The note has no tables, notation or equations. Its only framework-like structure is the numbered list of four conditions for relying on a mechanical check.

**Deletion test:** a single sentence could name the four conditions. However, the note refers to them by position ("the first three", "the fourth", and condition 3 in the footer). It also uses them to reach a non-obvious conclusion: the mark's contract supplies the rule, the locatable inputs and the source availability, but not checker trustworthiness. That conclusion is what motivates the first open question. The list enables a decision about what is still unassured, so it is load-bearing.

**Unused categories:** every condition is used. Conditions 1–3 are used together for the mark, condition 4 separately for the mark, and condition 3 again for the history contrast. Conditions 1 and 2 also match the connect report's limits, although the note does not say so explicitly (see the info finding).

The section headings name example cases rather than taxonomy categories, so they do not need assessment as framework.
