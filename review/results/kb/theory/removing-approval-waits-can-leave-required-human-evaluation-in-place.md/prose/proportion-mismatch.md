---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: af9c036c66d64c64b1f4131a1ad4fcc1
completed-at: '2026-11-18T16:01:59Z'
findings: []
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/5b853f4dd9c810195c5f5c5c/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/5b853f4dd9c810195c5f5c5c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/af9c036c66d64c64b1f4131a1ad4fcc1/outputs/review-proportion-mismatch.md
raw-output-sha256: be32aa53b7870f7c1fd156e50b0e314f4cb625fc394d9e8f03688cce4fa82c19
---

# Review

The core claim has two parts:

- Removing an approval wait differs from automating or retiring a specified evaluation task.
- A claim of full automation must therefore say which tasks it keeps and which requirements it retires.

The opening defines the wait-versus-requirement distinction. "The same activity can perform different roles" separates both from optional assessment. "Name the process being automated" develops the load-bearing consequence: a hidden requirement, its extension to revisions, and the forms a changed check can take. That section is the longest substantive part, so the central claim receives the most development. The section on optional assessment is shorter. The scope bullets are brief. No secondary section grows at the core claim's expense, and none should be split out.
