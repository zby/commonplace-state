---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - causes a retained change to its reusable machinery that later work depends on
  reason: 'Modifier attachment: the relative clause "that later work depends on" most
    naturally attaches to the nearest noun, "its reusable machinery", giving the reading
    "a change to the machinery that later work depends on". The intended condition
    (per the linked factory-learning note) is that later production depends on the
    retained change. The unintended reading drops the dependence-on-the-change guard
    that distinguishes retention from inert storage. Reordering fixes it, e.g. "causes
    a retained change to its reusable machinery, and later work depends on that change".'
  level: warn
- scope: passage
  quotes:
  - a description cannot change whether its judgment was required for installation
  reason: 'Reference: "a description" has no antecedent, so readers can take it as
    a description of the evaluator''s role, the note''s own framework description,
    or a system description; "its" must then be resolved back past it to the evaluator.
    The intended reading (labelling an evaluator as the judge does not alter whether
    it actually gated installation) is recoverable but not immediate.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/4cc1c0a0cc093babc0471474/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/4cc1c0a0cc093babc0471474/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 48f9b14a22014423bec136841b0a492e
completed-at: '2026-11-18T00:20:14Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/48f9b14a22014423bec136841b0a492e/outputs/review-parsing-ambiguity.md
raw-output-sha256: 9d62a9008ef4ec19652d5350754ae0736bf41756f22bd42c420688b6ad4983bf
format: 2
---

# Review

## Summary

Most sentences have a single plausible parse; negations such as "not merely stored" and "not merely editable files" scope clearly. The opening definition of experience-responsive retention has a relative clause that attaches more naturally to the machinery than to the change, which plausibly misstates the dependence condition. A Scope bullet uses "a description" without an antecedent, a smaller reference problem.
