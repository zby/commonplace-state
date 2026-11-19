---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/89ff6ce227b5e51dd192b495/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/89ff6ce227b5e51dd192b495/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 0d803fab7d78498584be07f131ac550c
completed-at: '2026-11-18T16:03:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/0d803fab7d78498584be07f131ac550c/outputs/review-concept-attribution.md
raw-output-sha256: 0a9146d7b9747bd387f0bced103cd25637bbddbc8b57d602c34cfc2c44944905
format: 2
---

# Review

The note makes two attributions to linked targets; both resolve and both match.

- "This is a choice within the trade-off between checking cost and reliance risk" identifies the fail-on-mismatch choice as an instance of the linked note's title claim. The target (`checking-retained-results-trades-cost-against-reliance-risk.md`) states that how often to check depends on check cost relative to the risk of relying on stale or wrong content, and its completeness-mark section says an inexpensive, defined check makes enforcement attractive. The note's further qualification — reuse of the check's result accepts the risk of changes since it ran — matches the target's "assurance dates from the last check".
- "ADR 046 judges such false mismatches worse than no check" matches ADR 046's Consequences: an under-normalized checker "would produce false mismatches on correct quotes, which is worse than no check". The casebook-corpus attribution (mismatches dominated by editorial omission, bracketed substitution and case changes) matches ADR 046's prototype-run paragraph.

ADR 073 and ADR 094 are cited by number without links; they are citations of decisions rather than concept identifications, and the reading scope does not extend to unlinked files, so they were not checked under this gate.
