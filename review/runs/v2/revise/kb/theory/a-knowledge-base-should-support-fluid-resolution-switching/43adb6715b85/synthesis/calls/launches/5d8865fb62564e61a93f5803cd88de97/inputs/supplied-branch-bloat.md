---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: f7ef96de82e142e0b37fd6d196164c0b
completed-at: '2026-11-16T22:30:06Z'
findings: []
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/b630a632c3158f46343355d7/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/b630a632c3158f46343355d7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/f7ef96de82e142e0b37fd6d196164c0b/outputs/review.md
raw-output-sha256: 31073f7ad3cf476ee21d4231f895fa0a6e8fed93c3c92c7b07d1db1870919c24
---

# Review

## Main claim

The note's main claim is that a knowledge base should make task-relevant
movement between broad and detailed views inexpensive in both directions. It
offers this as a qualitative design criterion. The description commits the note
to three jobs: defining resolution-switching, listing the Commonplace mechanisms
that support it, and stating the criterion's limits.

## Side material checked

- **Mechanism paragraphs.** Titles and bodies, indexes and search, link context,
  and progressive disclosure each name one route by which a reader changes
  scope or detail. The aside about search having different metadata
  requirements is one clause long. It also sets up the later boundary that
  search or backlinks may supply the outward route. These paragraphs are the
  inventory the description promises, so they are not branches.
- **The evaluative criterion.** The contrast with retrieval accuracy and the
  four questions put the main claim into operation. The closing "no scoring
  rule" sentence keeps the criterion within its stated qualitative status.
- **Connection to discovery.** This section comes closest to being a branch,
  because recognition is a separate problem. However, it is three sentences long
  and works mainly as a boundary: switching can assemble candidate views but
  "does not perform the recognition or guarantee a discovery." That limit
  heads off an overclaim the reader might otherwise draw, much like the
  criterion's pass example of a compact contrast that bounds the mechanism. It
  makes no independent claim about discovery that would need separate evidence.
- **Boundaries.** The distinctions from addressability grain, pointer accuracy
  and retrieval recall, along with the remark that an outbound link is not
  always needed, are boundary conditions on the main claim.
- **Open questions.** The questions about measurement already sit in an
  open-question section. They do not pull the argument away from the main
  claim.

No branch needs removal, demotion or rehoming. The side material either lists
the mechanisms the note promises or limits the claim's scope.
