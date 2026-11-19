---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: d1938ea3e06c41ceb054cd0c125162fd
completed-at: '2026-11-16T18:55:21Z'
findings:
- scope: passage
  quotes:
  - '"Initial" means a starting environment under incomplete evaluation, not a permanent
    architecture or a promise that human holistic judgment remains necessary.'
  reason: This Scope bullet restates the point already made by the section "Why 'initial'
    matters" without adding a new boundary. The first Scope bullet likewise points
    back to the linked notes. The repetition is local and short, and it does not create
    a section that only restates framing.
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/b822ba245cc65c56190c16b7/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/b822ba245cc65c56190c16b7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/d1938ea3e06c41ceb054cd0c125162fd/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 5340d69c05626a7fd4ecaba55964fee723e6986c4929265a392784983cedf5c4
---

# Review

## Summary

The note's sections track distinct claims or necessary support units, so sections do not outnumber its substance.

## Claims and sections

Distinct non-obvious claims:

1. When no complete fixed oracle decides theory fit, live system use supplies an initial selection environment (opening).
2. Fit is tested through a distributed portfolio of consequences rather than a single acceptance criterion (opening list).
3. Counterfactual effect is the property that makes live use selective, with retrieval-only, perturbation-sensitive and rival-beating claims carrying increasing evidence (Why live use can select).
4. Live selection can confirm the system's own misconceptions, and it exposes failures without assigning blame (Initial selection is vulnerable to self-confirmation).
5. "Initial" does not reserve fit for permanent human judgment or rule out learned or formal evaluators (Why "initial" matters).

Sections: the unheaded opening, three argument sections, Scope and Open Questions. Each argument section carries one claim. The self-confirmation section is a failure-case unit that the claim needs. Scope adds boundary conditions, including the claim's relation to the research setting and to externally supplied objectives, although two bullets partly repeat earlier material (recorded as INFO). Open Questions is a conventional support unit and does not restate the argument. The section count does not exceed the claims plus the necessary support units.
