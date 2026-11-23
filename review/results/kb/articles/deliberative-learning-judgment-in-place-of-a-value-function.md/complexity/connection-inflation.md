---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 6b80ae350a6d485eb5857f28ee0c68a4
completed-at: '2026-11-21T19:26:18Z'
findings:
- scope: passage
  quotes:
  - paired with [reversibility can favor a change by limiting future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md).
  reason: This is the thinnest entry. The body already links the reversibility note
    inline as the way to act under an open verdict, and 'paired with' adds little
    beyond that. It does add a pointer that the two notes are read together, so it
    is not fully inflated.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/6b80ae350a6d485eb5857f28ee0c68a4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/e16193ddae3907e1da7d4536/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/6b80ae350a6d485eb5857f28ee0c68a4/outputs/review-connection-inflation.md
raw-output-sha256: 1b4fbbcb0438e2a28ea8e40668705bd7039a6c9432662d8633403c07371c1a75
---

# Review

## Summary

The article has no "Relevant Notes" footer. Its "Where to go next" section is the navigational footer, so I tested each entry there.

- **Deliberative learning.** The body links this definition inline as the source of the two conditions. The footer adds what the reader will find only in the target: what a claim must name, the distinction between correction and displacement, and boundary cases such as triggers and direct updates. This is navigational context the body does not supply, so the entry is not inflated.
- **On-balance judgments.** The body uses this link to support the on-balance definition. The footer adds what the target covers beyond that use, including how to decide under open verdicts and Commonplace's declared objective. Not inflated.
- **Reversibility.** This entry is attached to the on-balance entry and adds only the pairing. See the info finding.
- **Companion drafts.** These three articles are not linked in the body. The entry also gives status context: they were written before the term was adopted and are being re-anchored from the theory-builder special case. Not inflated.

No entry fails both tests in the gate.
