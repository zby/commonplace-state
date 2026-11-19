---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The first three parts carry to any improvement claim about a system that revises
    its own reusable machinery.
  reason: This sentence uses the four-part structure to decide what transfers beyond
    factories, but the cut does not match the reason given. The factory-specific dependency
    is the preserved-path consequence, which sits inside the second part, the scope-indexed
    relation. The fourth part, evaluator location, has no stated factory dependency.
    The structure otherwise does real work; this one use draws an inference the partition
    does not support.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/1db28b62835a7f352458123f/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/1db28b62835a7f352458123f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 1b6d3b3fdecc49228919ea296c227cdb
completed-at: '2026-11-16T21:57:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/1b6d3b3fdecc49228919ea296c227cdb/outputs/review-framework-decoration.md
raw-output-sha256: 09f6ef9dd1eb96f4231d7743584cc78c1823d9acafbcf748a8c22114c84299e8
format: 2
---

# Review

I checked each structure in the note to see whether one sentence could replace it without losing an inference the argument uses.

- **Predecessor / candidate / operative successor.** The argument depends on this three-way split. The candidate term lets the note say that a construction event cannot ground the claim. It also defines the candidate-admission route and the point that a staging comparison is evidence rather than the claim itself.
- **Measurement over snapshots vs candidate admission.** The evaluator-location section uses this distinction directly: a judgment that gated installation is on the causal path, while a measurement taken after the update is not. Without the split, that section's main inference is lost.
- **Two-component relation (non-regression plus named target).** Both components are used later. Scope-indexed non-regression yields the preserved-path consequence. The named target is what antecedence fixes in advance. The Scope section also discusses an alternative relation shape and its consequence.
- **Four declarations.** The opening list previews the four argument sections, and the text later refers to it: "the fourth declaration below". The list adds no categories the argument leaves unused. Its one questionable use is the transfer bullet in Scope, recorded as an info finding.

No structure is decorative, and the note has no notation or equations.
