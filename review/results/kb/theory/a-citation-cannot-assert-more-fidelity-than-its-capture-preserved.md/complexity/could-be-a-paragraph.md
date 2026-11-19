---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 5b0e8e1a84fa45668de424df723d8dc7
completed-at: '2026-11-18T16:01:38Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/2511d3170d67ea01006057f4/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/2511d3170d67ea01006057f4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/5b0e8e1a84fa45668de424df723d8dc7/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 728e29eddeea0a63edcc56e7e4849a3581614283a08c3d850fa5fc5b02030131
---

# Review

## Summary

The note does not reduce to a single simple insight. A one-paragraph rewrite would lose several separate claims, boundary cases and failure conditions.

The title states one organizing claim: a citation cannot assert more fidelity than its capture preserved. The body develops several independent consequences that a paragraph could only list, not support:

- The four-question split, and the cost asymmetry that justifies failing on wording mismatch while not blocking on support.
- The two-sided failure of normalization rules, with the casebook evidence of which mismatches were substantive.
- The occurrence-versus-location distinction, the ban on concatenating disjoint ranges, and the limit that uniqueness does not prove intent.
- Capture binding and where it stops, the change-detection gap when surrounding context changes, and the rule that missing bytes report as unverified, not passed.
- Context lost through chunked reads, and how exact and semantic hops behave differently in a provenance chain.
- Scope limits, including unrecognized quotations that appear in no outcome.

Each item carries a failure condition or inference step the reader needs separately. The multi-section structure is justified.
