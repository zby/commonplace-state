---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 0b6aab3bf2ce43d9808afc045b836a39
completed-at: '2026-11-16T18:57:58Z'
findings:
- scope: passage
  quotes:
  - The important property is counterfactual effect.
  reason: The mechanism is present and constraining. Live use selects because consequences
    become observable, and a claim's withholding, replacement or perturbation changes
    search or recovery. It is still thin on what the central claim forbids. The claim
    says use 'can' select, gives only 'provisional' standing and is 'not a final authority',
    and the self-confirmation section relies on rivals, withholding, held-out demands
    and independent checks to make selection less self-sealing. The note does not
    state an outcome that would show live use failing to act as a selection environment.
    The Open Questions leave open whether delayed consequences discriminate 'strongly
    enough to guide selection rather than merely report viability'.
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/37d65f4255c28587a5a5bae8/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/37d65f4255c28587a5a5bae8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/0b6aab3bf2ce43d9808afc045b836a39/outputs/review-explanatory-reach.md
raw-output-sha256: 2c877e6bb8939a00f1abdaa0729f53ba015c35ca710abd8778c048bd84bb9f70
---

# Review

## Summary

The note gives a real mechanism. Fit is a property whose consequences are spread across operation and time. A live system makes those consequences observable. Counterfactual effect separates a claim that is merely cited from one that mediates work.

Varying a premise moves the conclusion. If a complete fixed oracle existed, live use would lose its role as the *initial* environment. The note says this when it allows that a learned or formal evaluator may later do better. If a claim's use had no counterfactual effect, it would earn no selection evidence.

The self-confirmation section is not ad-hoc accommodation. It names the specific routes by which use can mislead and the controls that counter them. These controls are rival formulations, withholding or perturbation, held-out demands and transfer, and each one sharpens the mechanism.

The remaining weakness is falsifiability. This is recorded as an INFO finding: the claim's possibility phrasing and its open question about discriminating power leave its failure condition implicit.
