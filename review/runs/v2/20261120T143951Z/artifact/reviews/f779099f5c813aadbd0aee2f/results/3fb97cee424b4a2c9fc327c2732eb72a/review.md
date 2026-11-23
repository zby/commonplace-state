---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Discarding all experience-dependent state prevents cross-run accumulation
  reason: The note defines the discarded state broadly enough to include every way
    an earlier run can affect a later one. Once all those paths are gone, the title's
    conclusion follows by definition. A title such as 'Ephemeral programs can support
    learning across runs' would assert the contestable point.
  level: fail
outcome: fail
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: a1a696788b97bc2edb4c029809dfd2a391a9f3b5e875dfd3b013b9f625e04bf7
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/3fb97cee424b4a2c9fc327c2732eb72a/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T143951Z/artifact/reviews/f779099f5c813aadbd0aee2f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/20261120T143951Z
launch: 3fb97cee424b4a2c9fc327c2732eb72a
completed-at: '2026-11-20T14:40:51Z'
raw-output: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/3fb97cee424b4a2c9fc327c2732eb72a/outputs/review.md
raw-output-sha256: a8ef31d330fbd8da28f5980912aa80522df665046d98bd891aa028412e85718f
format: 2
---

# Review

A one-off script can expose a dependency error and be deleted after the system adds a regression test. The later run can use the test to catch the error. This example identifies the architectural choice the title could foreground: which record of the episode to carry forward.
