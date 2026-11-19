---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: f720129119974580af182d165bf2daaa
completed-at: '2026-11-17T13:17:01Z'
findings:
- scope: passage
  quotes:
  - Removing a human approval wait and removing a specified evaluation task are different
    changes.
  reason: 'The mechanism is largely definitional: a wait is defined by execution flow
    and a specified task by the specification, so their separability follows from
    the definitions. That makes the claim hard to vary, but it is falsifiable only
    by showing that waits and requirements are coextensive in practice. The note does
    not name such a counter-case, for example a process whose only specification of
    the check is the gate itself.'
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/b1ab09474ad2d8e3760246da/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/b1ab09474ad2d8e3760246da/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/f720129119974580af182d165bf2daaa/outputs/review-explanatory-reach.md
raw-output-sha256: eb1b5b10060a2322c9165d93a175e44c171b1b4846db96d6d343f90457323e32
---

# Review

## Summary

The central claim is that removing approval waits can leave required human evaluation in place. The note explains why. A wait is a property of execution: it blocks progress until a person acts. A specified task is a property of the process specification: it can remain undone while execution continues. Removing one does not therefore remove the other.

Varying a premise changes the conclusion. If the requirement existed only as the wait, removing the wait would remove the requirement. The Scope bullet on habitual waits partly addresses this: an unwritten wait is "not evidence that the evaluation is needed to meet a stated requirement". The secondary consequence, that a full-automation claim must name preserved and retired tasks, follows from the distinction and is not ad hoc.

The qualifications, such as the absence of a harm claim and the separation of usefulness from requirement, narrow what the note asserts. They do not shield it from counterexamples. The mechanism is present but mostly analytic, which is recorded as INFO.
