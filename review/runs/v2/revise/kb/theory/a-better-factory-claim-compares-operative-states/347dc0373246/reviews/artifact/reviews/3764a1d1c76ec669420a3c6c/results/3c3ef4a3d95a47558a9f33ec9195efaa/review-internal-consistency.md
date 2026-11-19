---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A real episode can be described either way, and the description determines where
    the evaluator sits.
  - The same human activity — reading results and forming a verdict — falls on opposite
    sides depending on whether it gated the successor.
  reason: 'The body grounds evaluator location in a causal fact: whether the judgment
    actually gated installation, given that an admission decision determines what
    the factory retains. The Scope section says the route is a description choice
    and that the description determines where the evaluator sits. If a human verdict
    in fact controlled installation, the body places it on the causal update path
    whatever the description says. The Scope bullet lets a measurement description
    move it off that path. The two passages disagree about whether evaluator location
    tracks causal fact or declared reading.'
  level: warn
- scope: passage
  quotes:
  - The first three parts carry to any improvement claim about a system that revises
    its own reusable machinery.
  reason: The reason given for the factory restriction is the preserved-scope clause.
    That clause is a consequence of the second part, the scope-indexed relation. Yet
    the bullet carries the first three parts over in general and leaves out the fourth,
    evaluator location, which the body never ties to anything factory-specific. The
    stated reason does not match which part is held back.
  level: info
- scope: passage
  quotes:
  - Neither claim entails the other
  reason: 'The heading implies one pair of claims that do not entail each other. The
    section covers two different pairs: passing does not establish learning, and retention
    does not establish passing. The pairing is recoverable from the text but drifts
    from the heading.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/3764a1d1c76ec669420a3c6c/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/3764a1d1c76ec669420a3c6c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 3c3ef4a3d95a47558a9f33ec9195efaa
completed-at: '2026-11-16T22:00:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/3c3ef4a3d95a47558a9f33ec9195efaa/outputs/review-internal-consistency.md
raw-output-sha256: b7fec67bb442cb19a7c5b612fd13a4dffdfae0f826bb3e8cc7b4f017ccb7b635
format: 2
---

# Review

## Summary

Most of the note is consistent.

- The definition of "better" as relation-relative in the opening matches the Scope section's statement that genuine betterness over an open family is unresolved.
- The successor definitions hold across both routes.
- Preservation, assessed at the comparison, and compounding, tested in later episodes, are kept apart throughout.

**Contradiction.** The body and the Scope section disagree about what fixes evaluator location: the body treats it as whether a judgment actually gated installation, the Scope section as how the episode is described. This is the warning finding.

**Smaller drift.** The scope bullet's reason does not match the part it holds back, and the "Neither claim entails the other" heading pairs claims differently from its section. Both are recorded as INFO findings.
