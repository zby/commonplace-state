---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: 6a9c8733d3906b1ae0ad19bb313466b162dbf7388a77276b26d65c5e003a0d8a
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
findings:
- scope: passage
  quotes:
  - a validator is centralized, versioned, reviewed on every change, and amortized
    across every copy it protects
  reason: This empirical-sounding generalization about validators carries precondition
    4's argument that the regress bottoms out. It is stated as established fact, with
    no evidence or citation. Whether validators are in fact reviewed on every change
    is a property of a particular development process, not of validators as such.
    Its status as an assumption or design expectation is not recoverable from the
    wording.
  level: warn
- scope: passage
  quotes:
  - An unenforced copy is always one missed edit away from the catastrophic state
  reason: The preceding paragraph establishes the harm modally ('A *false* copy can
    cause silent, unbounded wrongness'); this sentence restates it as 'always' and
    'catastrophic' without new support. The derived consequence takes on more confidence
    than its premise carries.
  level: info
- scope: passage
  quotes:
  - would dominate, recovering the context economy without the drift
  reason: The claim that enforcement would dominate omission for hot-path contract
    values is a projection about an unbuilt mechanism; the Open Questions section
    asks for the 'cheapest general mechanism' for such regions. The conjectural status
    is recoverable, but only by connecting two distant passages.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/795ef4f655e02dc25604cbbd/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/795ef4f655e02dc25604cbbd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-epistemic-status-blur.md
raw-output-sha256: 8dc7e9fcc7c8171d927d2a5e844ebbb90458963cc204a2b48275af4f048f97cd
---

# Review

The note is mainly a normative derivation. From an asymmetry premise and a check-cost premise it concludes that a recomputable copy must be checked or absent. Most of it presents that status honestly. The harm is stated modally ("can cause"). The check-cost boundary is tied to a cited pyramid. The four preconditions are a qualitative decomposition the note owns. Instance states are labelled (enforced, resolved by omission, not yet applied).

The WARN concerns precondition 4. The argument that the validator regress terminates rests on a factual description of how validators are maintained, given in the same declarative register as the derivation. A reader cannot tell whether "reviewed on every change" is observed practice, a requirement the note imposes, or an assumption. Yet precondition 4's conclusion inherits the confidence of that description.
