---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 0d803fab7d78498584be07f131ac550c
completed-at: '2026-11-18T16:03:05Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/121775ecf4e3476603a0b6d8/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/121775ecf4e3476603a0b6d8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/0d803fab7d78498584be07f131ac550c/outputs/review-misleading-link-text.md
raw-output-sha256: f253dfbb114691bddd248714a98653467f8ec6eec9bd54aa3898a371401ae458
---

# Review

The body has two markdown links; both resolve and their text matches the target.

- "trade-off between checking cost and reliance risk" → `./checking-retained-results-trades-cost-against-reliance-risk.md`. The target's title is "Checking retained results trades cost against reliance risk", and its opening paragraphs develop exactly that trade-off. The reader's expectation is met.
- "ADR 046" → `../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`. The surrounding sentence leads the reader to expect a decision about quote checking that judges false mismatches worse than no check. The target is the verbatim-quote validation ADR, and its Consequences section states that an under-normalized checker's false mismatches are worse than no check.
