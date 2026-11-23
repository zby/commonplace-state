---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/weight-resident-methodologies-compress-behavior-in-context.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/weight-resident-methodologies-compress-behavior-in-context.md
note-sha256: d9b67d4aed6d8eedc40f9fb9f66c301f58c147255b8a475fb1b26ee9c04bc81d
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
outcome: pass
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/20261120T143951Z
launch: b86f72b5b1fa4ba6ac345b0fcf8f96a6
completed-at: '2026-11-20T14:40:20Z'
findings: []
contract: verdict
target-sha256: e324a759d9af123e67f1dda5b4fec4b5b03f61563386e758b04b9ef1980602c7
target-capture: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/b86f72b5b1fa4ba6ac345b0fcf8f96a6/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T143951Z/artifact/reviews/bd400d167ef0df50fe8375a9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/b86f72b5b1fa4ba6ac345b0fcf8f96a6/outputs/review.md
raw-output-sha256: 6538efc3b33301492869de266d87a99fe1f1664a651832b32f23a4b2d0be12bf
---

# Review

The title makes a contestable claim about how much behavior a short cue can guide. A model could know a methodology well enough to describe it and still need its decision rules spelled out to apply them together. If it does, the cue saves little context compared with loading the relevant instructions. The possibility of that failure makes context efficiency a substantive claim even when the methodology is already represented in the model’s weights.
