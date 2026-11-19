---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/ceec2180821ca4aab93e8b3d/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/ceec2180821ca4aab93e8b3d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 43caaa8c7b73402d91127314b490cc97
completed-at: '2026-11-18T16:01:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/43caaa8c7b73402d91127314b490cc97/outputs/review-jargon-persistence.md
raw-output-sha256: 4293772afdd22eee2709bf2f2c019a3bd5ce2abb6da2d60b8d4b1cfce8918544
format: 2
---

# Review

## Summary

The note's most repeated specialised term is "capture". It is defined inline at its first body use ("a retained copy of the source bytes taken at one time"). Every later use sits in a sentence that restates its role: "recorded capture", "binds the compared bytes to that capture", "A capture kept on another machine", "capture to extract and extract to note". A reader does not need to scroll back to follow these sentences, and "capture" is close to its ordinary English sense.

Other repeated terms, such as "normalization rule", "wording check", "occurrence" and "intermediary's extract", are either plain language or are re-grounded where they recur. No KB-internal term is defined once and then reused opaquely. Single unexplained terms such as "pin" are first-mention definition problems, not persistence problems, so this gate does not judge them.
