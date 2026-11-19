---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: b782e79a95b2475dbf75ec62dfa4555d
completed-at: '2026-11-18T00:18:26Z'
findings:
- scope: passage
  quotes:
  - Retaining a change does not establish improvement, and establishing improvement
    does not show that production experience caused it.
  reason: The opening of the third section partly restates the introduction's point
    that retention has no quality requirement, but the section then extends it with
    the improvement-without-learning case and the requirement for causal-contribution
    evidence, so it is not a restating section.
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/a831a8498c0319b8226b855a/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/a831a8498c0319b8226b855a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/b782e79a95b2475dbf75ec62dfa4555d/outputs/review-claim-to-section-ratio.md
raw-output-sha256: b9c116c2904b46700e9070193f968289e68da605508cb7c5c0fa65b2d9fdceee
---

# Review

## Summary

The note has three argument sections plus Scope and Open Questions. It carries at least five distinct non-obvious claims:

1. The relata are the predecessor and the installed, depended-on successor; a generated-and-discarded candidate is not a term, so the claim cannot be read off a construction event.
2. The assessment relation must be declared before development, which blocks post-hoc selection of requirements without showing that they track quality.
3. Non-regression needs an explicitly declared scope; this framework uses the predecessor's prior capabilities, and the compared states span all operative machinery, not only model weights.
4. If factory development is in the checked scope, non-regression requires a still-applicable revision path, not merely editable files.
5. Retention, improvement and learning are separable claims; learning requires evidence that the experience-derived change contributed causally, which only a with/without contrast tests.

Each argument section maps to one or more of these claims. The relata section carries claim 1. The assessment-relation section carries claims 2–4. The improvement/retention/learning section carries claim 5. Scope carries boundary conditions: no oracle, antecedence is not constitutive, other relation shapes are possible, and transfer to other systems is conditional. Open Questions records unresolved specification problems. Sections do not outnumber claims plus necessary support units.
