---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: cc44297aacfcf66236e6066f719f2f134021b4664b77d77f3a2ac45eaf6e3559
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 3c3ef4a3d95a47558a9f33ec9195efaa
completed-at: '2026-11-16T22:00:27Z'
findings:
- scope: passage
  quotes:
  - A better-factory claim compares operative states under an antecedent assessment
    relation
  - is stated for factories because the preserved-scope clause draws on factory development
    being in scope
  reason: The 'factory' qualifier in the title is not used by the central argument.
    The arguments for operative relata, antecedence, scope indexing and separating
    evaluator location from the learner boundary all go through for any system that
    revises its own reusable machinery. The note's Scope section says so for at least
    three parts. The only factory-dependent step is the preserved-path section, which
    the note itself presents as a consequence that 'falls out of scope indexing'.
    The qualifier therefore serves a corollary, not the central claim, and narrows
    the filename-level title.
  level: warn
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/47bcd26e7e3e671816d32637/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/47bcd26e7e3e671816d32637/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/3c3ef4a3d95a47558a9f33ec9195efaa/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: ecc91c3a46e73b00c13a4da0bc2c2de7c74a1a072fe04b4129789849109a5f51
---

# Review

## Summary

Qualifiers in the title and description:

- **Operative.** Load-bearing: it separates the successor from discarded candidates.
- **Antecedent.** Load-bearing: it makes the comparison capable of failing.
- **Scope-indexed** (description and body). Load-bearing: it makes non-regression meetable and non-vacuous.
- **Factory.** Not load-bearing.

**Deletion test for "factory".** The restated claim reads: "An improvement claim about a self-revising system compares operative states under an antecedent assessment relation." The main argument is unchanged. Only the preserved factory-development path depends on factory development being in the predecessor's scope, and the note derives that path as a consequence.

**Placement.** The Scope bullet already acknowledges most of the broader reach. That is the placement the gate recommends for the broader claim, but the narrower form remains in the title. Retaining the factory framing for the note cluster is an author decision; this review only records that the argument does not need it.
