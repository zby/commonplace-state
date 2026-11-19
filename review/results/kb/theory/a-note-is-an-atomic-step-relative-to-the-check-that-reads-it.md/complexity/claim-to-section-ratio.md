---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 706c8ecebc174f0bafa3f1e0abb2b07f
completed-at: '2026-11-16T22:36:38Z'
findings: []
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/b573c19ff6380ed7d39e8f5b/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/b573c19ff6380ed7d39e8f5b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/706c8ecebc174f0bafa3f1e0abb2b07f/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 811c9810736e462ca9158816e5c955c965b0062f4dbc8cc95d7721bc08a6ed04
---

# Review

## Summary

Each section adds a distinct claim or a necessary support unit, so sections do not outnumber claims.

## Claims and sections

Distinct non-obvious claims:

1. A note is bounded twice, by co-loading and by checking. The two bounds are independent quantities, and atomicity is relative to a named check. This is the unheaded opening.
2. The bound belongs on the artifact rather than the review, because a review-side budget fails silently when it lags. This is "Placing the bound on the artifact rather than the review".
3. For the grounding check, the cost unit is the unquoted source, because verbatim quotes move the finding step into a validator. A corollary follows: jointly supporting sources should be quoted together rather than split, and this couples the two bounds. This is "Mechanism".
4. The corpus shows the bounds coming apart, and the five-link experiment can be reread as evidence about note size rather than reviewer capacity. This is "The two bounds come apart in the corpus".
5. N is a convention chosen for auditability. It is not a reviewer-capacity threshold or an observed-miss threshold. The Descartes and Lamport precedents present checker-relative sizing as established practice. This is "What kind of number a step size is".

There are five headed sections plus the opening, against five claims. "Scope" carries boundary conditions: the dependence on validated quotes, the one-check derivation and the local evidence base. "Open Questions" names two unresolved failure cases. Both support units are separately necessary. No section restates another's framing. The corpus section supplies evidence the mechanism section does not, and the step-size section answers a question the earlier sections explicitly leave open.
