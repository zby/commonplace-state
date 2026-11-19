---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A detailed artifact should leave a discoverable route back to wider organizing
    context.
  reason: The note defines resolution as a property of a view, 'not an intrinsic abstraction
    rank assigned to an artifact'. This sentence, by contrast, calls an artifact 'detailed'.
    Context suggests it means 'an artifact read at its detailed view', so this is
    likely compression, not contradiction. It is still a small drift from view-relative
    to artifact-level vocabulary, which a reader could take as reintroducing the rank
    the definition rules out.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/e71a092e99b6d3ba5208a793/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/e71a092e99b6d3ba5208a793/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-internal-consistency.md
raw-output-sha256: 0621b8f0375c74ede89dc6d2c6e732c4d0846065f292bd3b3f7401840a1b3412
format: 2
---

# Review

## Summary

The sections agree on their key claims.

- The opening asks for switches "in both directions" and a "discoverable route back". Boundaries then says an artifact need not carry an outbound link and that not every task returns to a broad view. These are consistent: the opening already says "discoverable route", not "link", and limits the requirement to "task-relevant" switches.
- "Bidirectional navigability" in Boundaries matches the opening's "both directions".
- The description, the opening definition and the criterion section all treat resolution as scope and detail exposed by a view. The only drift is the artifact-level phrasing noted above (INFO).
- The Discovery section's limit, that switching assembles views but does not perform recognition, matches the criterion's modest framing as a prompt for friction, not a guarantee.

There are no contradictions.
