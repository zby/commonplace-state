---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: dddfe82e0c4eb506a7b324a47fa166f4e5ac505a98c1b75fb1964a3b564259ac
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/736f9022900ff6c9a88d2dd0/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/736f9022900ff6c9a88d2dd0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: d155a6ea644e43e9abfa39b7f9c0a531
completed-at: '2026-11-18T16:03:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/d155a6ea644e43e9abfa39b7f9c0a531/outputs/review-unearned-generality.md
raw-output-sha256: f850f7195d944b8aae2cc71fb74a997d5cb830259dfaea45143d72dcfdbb5418
format: 2
---

# Review

## Summary

The central claim uses concrete vocabulary: "approval waits", "required human evaluation". The examples concern an agent adopting a written procedure. The claim is stated for processes in general rather than for agent instruction adoption.

- **Downgrade test:** replacing "process" with "agent instruction-adoption process" leaves the argument unchanged.
- **Explanatory-reach check:** the generality is earned by the mechanism. The distinction rests only on whether execution control blocks on a person and whether the process specification assigns a task to one. Neither property depends on agents or written procedures. The note states this structural basis directly ("An actual wait prevents execution from proceeding until a person acts. A specified task can remain undone while execution continues.").
- **Forbids test:** the general wording rules out calling any process "fully automated" while its specification still assigns human tasks. That forbids more than an agent-only claim would, so the extra coverage carries extra content.

The abstraction is concentrated in a few deliberate terms ("process specification", "blocking dependency", "unfulfilled requirement"), each of which does work. It is not spread defensively across the prose.
