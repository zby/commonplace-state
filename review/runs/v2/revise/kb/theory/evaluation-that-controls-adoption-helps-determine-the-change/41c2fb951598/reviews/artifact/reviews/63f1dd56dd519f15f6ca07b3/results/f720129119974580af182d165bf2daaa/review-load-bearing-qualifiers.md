---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Removing approval waits can leave required human evaluation in place
  reason: '''Approval'' narrows the title claim without doing work in the argument.
    The mechanism depends only on there being a wait, meaning that execution blocks
    until a person acts. The body itself extends it to non-approval waits: ''A non-binding
    recommendation still creates a dependency if the agent must wait for it'', and
    a habitual wait for human input. The deletion test (''Removing human waits can
    leave required human evaluation in place'') leaves the argument unchanged. Approval
    is the motivating case, so it belongs as the example, not as a restriction in
    the central claim.'
  level: warn
- scope: passage
  quotes:
  - a maintainer a weekly sample review and rollback of harmful changes
  reason: '''Evaluation'' in the title may also be narrower than the argument. The
    wait-versus-specified-task distinction does not use any property of evaluation,
    and the note''s own example includes rollback, which is a remedial action, not
    an assessment. ''Evaluation'' is plausibly intentional topical scoping, since
    the note is about evaluation roles, so this is INFO.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: dddfe82e0c4eb506a7b324a47fa166f4e5ac505a98c1b75fb1964a3b564259ac
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/63f1dd56dd519f15f6ca07b3/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/63f1dd56dd519f15f6ca07b3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: f720129119974580af182d165bf2daaa
completed-at: '2026-11-17T13:17:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/f720129119974580af182d165bf2daaa/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: 9a983ad7b96d03c98f17c78d16ef93850f63e2fe8121b05df963781535ebb83c
format: 2
---

# Review

## Summary

The note supplies the qualifiers "approval" (on waits), "required" and "human" (on evaluation), and "evaluation".

- **"Required"** is load-bearing. Removing it loses the contrast with optional assessment, which the note develops at length.
- **"Human"** is load-bearing. The note concerns what work still requires a person.
- **"Approval"** does no work. The reasoning uses only the blocking property of a wait, and the body explicitly covers recommendation waits and habitual input waits. The narrower title may lead readers and downstream notes to cite the claim as specific to approval steps.
- **"Evaluation"** is probably intentional topical scoping, though the mechanism would carry over to any specified human task. It is recorded as INFO.
