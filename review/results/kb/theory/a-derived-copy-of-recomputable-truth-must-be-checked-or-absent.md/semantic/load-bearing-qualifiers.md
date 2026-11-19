---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: 6a9c8733d3906b1ae0ad19bb313466b162dbf7388a77276b26d65c5e003a0d8a
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
findings: []
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/9c078b55e17b2b66e7a5194b/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/9c078b55e17b2b66e7a5194b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: dd26b1bf2a6d23a3aea8a379f48086c3dda1d8a3f641eb46b3ef0caa38047765
---

# Review

The title and description carry four restricting terms: "derived copy", "recomputable", "machine-checked", and "hand-maintained-and-trusted". Each was tested by deletion.

- **"recomputable"**: Load-bearing. Without it, the claim would cover every dependent artifact. The regime section then contradicts it: where verification is judgment, hand-maintained dependents are "unavoidable". The rule flips exactly where derivation becomes mechanical and the check drops to Level A.
- **"machine-checked"** (versus checked in general): Load-bearing. The asymmetry only forbids the unchecked state because a deterministic check is near-free. A judgment check would return the case to managed staleness.
- **"derived copy"**: Load-bearing for precondition 3 and for the contrast with abstracted rules ("generalizes beyond them"). A value that execution produces, or a rule that exceeds its sources, is excluded because it is not a copy.
- **"trusted"** (in "hand-maintained-and-trusted"): Load-bearing. The asymmetry mechanism runs through trust suppressing recomputation.

No qualifier narrows the central claim to fit one downstream use. The tag-readme application sits in the instances section, not in the claim.
