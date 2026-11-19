---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The normative ''should'' rests mainly on one sentence about complementing
    retrieval accuracy. ''Commonplace mechanisms'' gives four paragraphs to how switches
    are realized. The proportions fit the description''s stated aim of defining and
    inventorying, so this is a weak signal: if the note means to argue why fluidity
    matters, that rationale is its thinnest part.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/a649aeb1980ca22fafe5f5e1/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/a649aeb1980ca22fafe5f5e1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 0b808d1de3e64c04abdb9554dbd77b33
completed-at: '2026-11-16T22:29:35Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/0b808d1de3e64c04abdb9554dbd77b33/outputs/review-proportion-mismatch.md
raw-output-sha256: e9a0dd280181168182da8f3576b1512b0c425780cbcac51f9bab1a60697902d5
format: 2
---

# Review

The core claim is that a knowledge base should make task-relevant switches
between broad and detailed views inexpensive in both directions. The note
develops this as a qualitative evaluative criterion. The description frames
the note as a definition plus an inventory of mechanisms and limits.

Support is distributed as follows:

- The opening defines resolution and states the bidirectional criterion.
- "Commonplace mechanisms" has four paragraphs. Each one shows a concrete way
  of exposing different scope or detail. These paragraphs support the claim
  that the criterion can be met.
- "The evaluative criterion" names the property, contrasts it with retrieval
  accuracy and turns it into four diagnostic questions. This is the
  load-bearing section, and its length is comparable to the mechanisms
  section.
- "Connection to discovery", "Boundaries" and "Open questions" are short and
  scoping.

No secondary section crowds out the criterion. The only imbalance is between
how and why. The note spends more space on how switching is supported than on
why a knowledge base needs it. The info finding records this. It does not need
a split or restructuring.
