---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A knowledge base should support fluid resolution-switching
  reason: 'As phrased, the title is close to an applause line: few informed readers
    would argue that a knowledge base should make movement between overview and detail
    rigid or costly, so the stated opposite is not a live position. The contestable
    point the body actually develops is narrower: resolution-switching fluidity is
    a separate evaluative criterion from retrieval accuracy, recall, pointer accuracy
    and addressability grain, so a system can retrieve the right artifact and still
    fail it. A title carrying that distinction (for example, that retrieval accuracy
    does not establish bidirectional navigability between views) would be one an informed
    retrieval-centric designer could dispute.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: dbf61a87ecba4b344c7026057666abb97137a5fb8d1b3bdc8b615c93f1f6d15e
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/ff4ac82997f27addbdcc1ea5/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/ff4ac82997f27addbdcc1ea5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: a3c5d3391deb4e209fd2c546267aafd4
completed-at: '2026-11-16T22:29:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/a3c5d3391deb4e209fd2c546267aafd4/outputs/review-claim-strength.md
raw-output-sha256: 076762592066390de4a4711e2d1c0cdc58d29b471eb62aacd4f8305803a0a560
format: 2
---

# Review

## Summary

The title is a proposition, but its opposite ("a knowledge base should not support fluid resolution-switching") is not a position anyone informed would hold. "Fluid" already builds the desirability into the claim, which places it near the gate's `validation should be fast` failure example.

The body has a sharper point. It treats resolution-switching fluidity as a qualitative criterion that complements retrieval accuracy. It shows a system can retrieve the right detail yet make its wider context hard to recover, or offer an overview that never reaches the detail. It also separates the criterion from addressability grain, pointer accuracy and recall. A retrieval-focused designer could contest that independence claim, so it would make a stronger title. Alternatively, since the note mainly defines a term and inventories mechanisms, a topical title would also be valid under this gate.
