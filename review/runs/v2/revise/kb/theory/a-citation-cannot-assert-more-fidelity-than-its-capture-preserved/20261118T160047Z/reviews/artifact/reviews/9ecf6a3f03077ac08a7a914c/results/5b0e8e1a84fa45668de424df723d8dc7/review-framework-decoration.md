---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Truth: is the quoted claim true?'
  reason: 'The truth category is never developed after the list. It still has a job:
    it marks a question no check in the note answers, and the description names it
    as unverified. So it is a boundary marker rather than an unused category.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/9ecf6a3f03077ac08a7a914c/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/9ecf6a3f03077ac08a7a914c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 5b0e8e1a84fa45668de424df723d8dc7
completed-at: '2026-11-18T16:01:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/5b0e8e1a84fa45668de424df723d8dc7/outputs/review-framework-decoration.md
raw-output-sha256: b7fc9be86fa3c36d58f6e2a42faf6993092624d6fe0cbab2aaf6810384c81b0a
format: 2
---

# Review

## Summary

The note has one formal-looking structure, the numbered list of four citation questions. It is load-bearing, not decorative. The note uses no tables, notation or equations.

## The four-question decomposition

If the list is replaced by one sentence, such as "a quote check verifies only wording", the note loses the routing it relies on. The very next paragraph assigns each question to a different mechanism:

- A string check answers wording.
- An identity check answers part of attribution.
- Context needs a reader of both texts.

The later sections follow this split. "Which evidence a pass is relative to" develops the partial attribution answer: checksum binding to a capture, which stops short of the original or its author. The chunked-read paragraph relies on the wording/context split, since excerpts can keep the wording while losing the context needed to judge support. The cost asymmetry between deterministic wording checks and noisy support judgments also depends on keeping these questions apart.

Truth is the only category not developed later. It still serves as an explicit boundary of what stays unverified (INFO finding). The decomposition introduces no vocabulary or cross-references beyond what the argument uses.
