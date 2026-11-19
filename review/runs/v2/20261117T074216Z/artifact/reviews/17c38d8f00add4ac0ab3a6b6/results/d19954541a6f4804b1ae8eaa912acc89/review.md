---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - If a maintainer must inspect each adopted instruction and reverse harmful changes,
    the broader process still requires human work.
  - Optional observation is different from monitoring on which the process relies.
  reason: 'The note leaves the mechanism of post-adoption dependency open. Elsewhere
    it tests dependency by waiting: a person is needed ''for the process to proceed'',
    and the non-blocking case qualifies because the process ''neither waited for that
    assessment nor relies on it to continue.'' Post-adoption monitoring does not make
    adoption wait. That leaves two reasonable readings of ''monitoring on which the
    process relies'' and ''must inspect''. (a) A rule or schedule requires the inspection
    to happen, such as a mandatory review step or a gate on the next cycle. (b) The
    system''s quality or safety depends on a human catching and reversing harmful
    changes, even though nothing blocks without that human. The choice is material.
    Under (b), the week-later assessment in the Non-blocking assessment case becomes
    relied-on monitoring whenever a harmful finding would lead to a rollback. That
    collapses the note''s central contrast. It also changes which human activities
    the description says automation ''must address''. Under (a), that assessment stays
    optional observation. The text does not say which test separates optional observation
    from relied-on monitoring.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 9528731444671204248c1c7fed0181134ac72d8ab18a30d0a486df4eae922edd
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/17c38d8f00add4ac0ab3a6b6/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/17c38d8f00add4ac0ab3a6b6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: d19954541a6f4804b1ae8eaa912acc89
completed-at: '2026-11-17T07:42:57Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/d19954541a6f4804b1ae8eaa912acc89/outputs/review.md
raw-output-sha256: 367356e8a3ec55042869e3098ab8149c125c0b49a32070610826c87729eb2647
format: 2
---

# Review

## Summary

Most of the note's load-bearing assertions are resolved locally. The opening distinction defines its consequence: required evaluation "requires a person for the process to proceed", while measuring assessment "can observe a process that runs without one". The two hypothetical cases fix the scope (one KB instruction), the timing (before adoption versus a week later) and the dependency test (whether the agent must wait). The closing clauses of "The same activity can perform different roles" address edge cases: a non-binding recommendation that the agent must wait for, and human-authored rules applied by a program. The Scope bullets set explicit boundaries: required intervention, not influence; a written requirement versus actual execution; stop removal versus quality.

## The unresolved choice

The section "Name the process being automated" extends dependency from adoption to "continued operation". This is where the note leaves an argument-relevant mechanism open. Up to that point, the test is waiting: does the process stop until a human acts? Post-adoption monitoring with rollback never makes adoption wait, so this passage needs a different test. It does not state one. "Must inspect" and "monitoring on which the process relies" could mean a procedural requirement, or a dependence of outcome quality on human correction. The second reading would also cover the earlier non-blocking assessment whenever its findings could trigger a rollback. The note therefore cannot yet say reliably which human activities count as stops that automation must address. That is the practical consequence its description promises.

The gate reports this choice and does not choose for the author. The author might state the test for relied-on monitoring. Alternatively, the author might limit the extension to monitoring that a rule makes mandatory, or explain how the Non-blocking assessment case avoids it.
