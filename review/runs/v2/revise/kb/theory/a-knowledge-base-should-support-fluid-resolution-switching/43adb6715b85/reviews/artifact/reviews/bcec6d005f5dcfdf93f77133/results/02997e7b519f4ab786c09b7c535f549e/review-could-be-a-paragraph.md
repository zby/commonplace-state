---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/bcec6d005f5dcfdf93f77133/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/bcec6d005f5dcfdf93f77133/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 02997e7b519f4ab786c09b7c535f549e
completed-at: '2026-11-16T22:29:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/02997e7b519f4ab786c09b7c535f549e/outputs/review-could-be-a-paragraph.md
raw-output-sha256: b9a143a1a203604f0f03da4a928fddda95dfaf00aac5104b5ee74b73644f1563
format: 2
---

# Review

I rewrote the note mentally as one paragraph:

> A KB should make switches between broad and detailed views cheap in both directions. Commonplace's title, index, link-context and progressive-disclosure mechanisms support this. The criterion complements retrieval accuracy, is not addressability grain, and does not perform recognition.

That paragraph loses content the note's argument needs:

- **The four diagnostic questions.** They split downward movement into selection ("choose a narrower target ... without opening every candidate body") and loading ("without loading unrelated material"). They also separate upward recovery from relationship preservation. These are the criterion's operational content.
- **Two failure cases that separate the criterion from retrieval accuracy.** A system can retrieve the right detail but make its context hard to recover. It can also offer an overview that never reaches the needed detail.
- **The outward-route boundary case.** Backlinks, an index or search can supply the outward route, so an outbound link is not required everywhere. Some tasks also never need to return to a broad view.
- **The distinction from grain.** Grain prices the smallest retrievable matched unit. Resolution-switching concerns transitions among views.
- **The open measurement questions.** These qualify the criterion's status as not yet a metric.

The note holds several boundary cases and a decomposition of the criterion, not one simple insight. Its multi-section structure is justified.
