---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: e6c44a5d053c40b889fc04e430cca4c7
completed-at: '2026-11-21T19:26:59Z'
findings:
- scope: passage
  quotes:
  - its scorer saw a failure mode in a quarter of runs that never reached the proposer
  reason: The figure is sourced through the linked ingest, but the article does not
    say which failure mode this was or why it was the binding one. Without that context,
    the reader cannot judge whether this number supports the reinterpretation that
    the stall came from what the proposer was shown and not from a limit of artifact-level
    learning. A short clause naming the failure mode would make the figure legible.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/43534977b0fa631e66ca9be6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/outputs/review-orphan-references.md
raw-output-sha256: c0221c2356636400f387a86b1aa42d077f37df5ed5514aa42a9bccc8f410a234
---

# Review

## Summary

Each named study, system or empirical claim has a source and enough local
context to be evaluated:

- Schmidhuber's Gödel machine and Minton's PRODIGY (1988) link to supporting
  notes or ingests and describe the mechanism each one used.
- The EURISKO episode is marked as "reported" and links to its ingest.
- Sutton's Bitter Lesson essay and the 2026 Sutton–Javed interview link to
  external sources.
- The 2026 "Harness Evolution Hits a Ceiling" study links to its ingest.

The routing-line example and its "three similar over-broad rules" are clearly
hypothetical ("Suppose ..."), not empirical claims. The one
compressed figure, "a quarter of runs", is sourced but loses some legibility
because the article does not name the failure mode it counts. That gap is minor,
so it is recorded as INFO.
