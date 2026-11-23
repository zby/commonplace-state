---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: f65ad73739aa4b618c3989b05a76f11b
completed-at: '2026-11-23T11:40:51Z'
findings: []
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/f65ad73739aa4b618c3989b05a76f11b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/0ee8f2a6f8f5dc0f4f7ccc6b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/f65ad73739aa4b618c3989b05a76f11b/outputs/review.md
raw-output-sha256: 6eae7fb6f815dbaf7f20bb8c171288f7c420178f33b8f458af86cb9e7ae68f47
---

# Review

## Summary

The main claim, taken from the title and description, is that a fixed instruction to consult past incidents can carry lessons from new incidents only if the reviewer can tell which feature of an earlier failure applies to the case at hand.

The note has three short paragraphs, and none of them branches away from that claim. The first states the claim and separates "where to look" from "which failure bears on the page". The citation example sets up the case the claim needs: a lesson that applies when no surface feature, such as a shared source name, matches. The contrast with lookup by source name is a boundary condition. It shows why retrieval alone falls short. The last paragraph states the test (distinguishing apparent corroboration from independent support) and draws the conclusion that the rule itself does not need to change. That conclusion is the note's own point restated, not a side claim.

The note has no analogies, predictions, future extensions or related mechanisms that would compete with the main argument. No branch needs removal, demotion or rehoming.
