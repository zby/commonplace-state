---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - asks whether a reader can move among the views a task needs without paying avoidable
    transition cost or losing the relationship between them
  reason: The note's crispest formulation of its criterion (cheap transitions that
    keep the relationship between views) appears only after the four-mechanism inventory,
    under a newly coined second label, 'resolution-switching fluidity'. The opening
    already states the claim, so this does not hide it, but the claim would be more
    memorable if this sentence's two conditions (low transition cost, preserved relationship)
    were folded into the second opening paragraph and the section reused 'resolution-switching'
    instead of introducing a parallel term.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/98797e9eed5dcae4994ebd92/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/98797e9eed5dcae4994ebd92/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 5b2fb2d261474886a0c3926c8e8da412
completed-at: '2026-11-16T22:30:32Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/5b2fb2d261474886a0c3926c8e8da412/outputs/review.md
raw-output-sha256: aec61cbee51a11be40afacbdc6b7e0ba63932905b5363378108b6e32ebe80131
format: 2
---

# Review

## Core claim

Stated in one sentence from the note's own commitments: a knowledge base should
make task-relevant movement between broad views and detailed views inexpensive
in both directions, so broad views lead to specifics and detailed artifacts
leave a discoverable route back to wider context.

## Prominence

The title states the claim. The first paragraph defines resolution-switching
briefly and rules out the misreading of "resolution" as an intrinsic
abstraction rank. The second paragraph states the claim plainly and gives both
directions. The scoping caveat is one sentence, so it bounds the claim without
burying it. A reader can restate the claim after one read.

## Subordination of later material

Each later section serves the claim. "Commonplace mechanisms" shows how
existing features support switching in each direction. "The evaluative
criterion" turns the claim into four diagnostic questions. "Connection to
discovery" and "Boundaries" set its limits against neighbouring concepts, and
the open questions concern measurement. The links in the mechanism paragraphs
are cited support, not prerequisites.

The only shape issue is minor and recorded as an INFO finding. The best
statement of the criterion comes late and under a second name. Folding its two
conditions into the opening would make the claim more memorable. This is not a
WARN because the claim is already early and plain.
