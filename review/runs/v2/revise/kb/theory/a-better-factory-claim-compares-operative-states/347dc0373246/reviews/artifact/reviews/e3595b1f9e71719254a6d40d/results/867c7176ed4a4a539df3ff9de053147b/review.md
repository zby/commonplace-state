---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Without the index, the requirement is either unmeetable or vacuous depending on
    how generously the reader reads "no worse".
  reason: 'UNSUPPORTED — the dichotomy is asserted, not shown. Non-regression against
    the predecessor over a scope wider than its prior scope is not obviously unmeetable:
    on tasks the predecessor could not do, its baseline is low, so ''no worse'' there
    is near-trivial rather than impossible. Nor is it shown to be vacuous. The joint
    does not establish why the unindexed requirement fails, so the necessity of scope
    indexing rests on this sentence alone.'
- scope: passage
  quotes:
  - non-regression over that set requires the successor to keep such a path
  reason: THIN — the relation is defined as thresholds on dimensions declared in advance.
    Keeping a factory-development path follows from non-regression only if the declared
    thresholds include that path as a measured dimension. The note does not establish
    that a scope-indexed relation must include it. Its claim that preservation simply
    'falls out' of scope indexing also assumes that the comparison can check, at comparison
    time, whether the path remains applicable after the transition. The linked requirement
    may need further development episodes to test.
- scope: passage
  quotes:
  - So evaluator location is not recoverable from who was in the room; it has to be
    declared alongside the boundary.
  reason: 'THIN — the preceding sentences show that attendance does not fix evaluator
    location. They do not show that location must be declared rather than recovered
    from the record: whether a judgment gated installation looks like a causal fact
    a record could show. The Scope section then calls the route a description choice
    that ''determines where the evaluator sits'', which makes the location descriptive
    rather than causal. The joint leaves unresolved which reading supports ''has to
    be declared''. It also does not show that gating, which places the evaluator on
    the causal update path, keeps evaluator location separate from the learner boundary,
    which the Open Questions leave open.'
- scope: passage
  quotes:
  - This is also why the oracle problem for better-factory claims is sharp rather
    than incidental.
  reason: THIN — 'This' refers to the evaluator-location point, but of the three supporting
    clauses, only the last (human acceptance judgments re-entering the human-inclusive
    boundary) depends on evaluator location. Expense and gameability of acceptance
    tests hold regardless of where the evaluator sits. The 'why' therefore links the
    oracle problem's sharpness only partly to the preceding argument.
- scope: passage
  quotes:
  - Without antecedence the claim is close to unfalsifiable, because a successor that
    differs at all differs favourably on some dimension available to be named after
    the fact.
  reason: 'THIN — the reason supports the risk of post-hoc selection of the target
    dimension. It does not support near-unfalsifiability of the whole relation: a
    retrospectively chosen relation could still require non-regression over the prior
    scope, which a successor can fail. The note''s own Scope concedes that an independent
    retrospective criterion can ground a legitimate claim, so the hazard depends on
    who chooses the relation afterward, not on timing alone.'
outcome: report
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e3595b1f9e71719254a6d40d/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e3595b1f9e71719254a6d40d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 867c7176ed4a4a539df3ff9de053147b
completed-at: '2026-11-16T22:01:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/867c7176ed4a4a539df3ff9de053147b/outputs/review.md
raw-output-sha256: b8789529ceeec40710a7ad405d52486278fb8da5e96b29c636f61afc8a772cb9
format: 2
---

# Friction check: better-factory claims compare operative states

**Central claim (one sentence):** A claim that a factory got better becomes determinate only when it compares the predecessor with the installed, depended-on successor under a scope-indexed relation (non-regression plus a named target) fixed before the development it judges, with evaluator location declared separately from the learner boundary.

## Filter
**Filter:** SURVIVES

The commitments to operative-state relata, an antecedent relation, scope-indexed non-regression and two successor routes can coexist. The claim makes the relation constrain auditability, not quality, and the Scope section limits its reach. The closest strain is between separately declared evaluator location and the admission route, where gating places the evaluator on the causal path. The note leaves that strain open as a question; it does not split the central claim into incompatible parts.

## Thinnest joints

The ranking follows how much of the structure rests on each joint and how little support it gets. The scope-indexing dichotomy ranks first. It is the only stated justification for indexing, and the preserved-path section builds on indexing, yet the sentence asserts both horns without argument. The preserved-path derivation ranks next because it presents a further requirement as a logical consequence. It holds only if the factory-development path is one of the declared dimensions. The evaluator-location joint depends on a causal reading of "gated", which the Scope section's descriptive reading of routes undermines. The oracle-problem and unfalsifiability joints point in the right direction but overreach their reasons. Joints left unsurfaced held up: candidates are excluded by definition, deployed-system scope follows from the linked note, and the experiment-contrast argument for attribution follows from its linked note.

## For the human
Look first at "unmeetable or vacuous": say concretely what non-regression over an unindexed scope would demand and why it fails. The scope-indexing and preserved-path sections depend on that answer.
