---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 9a3dadef070b47feafc46aa3d3260d94
completed-at: '2026-11-16T18:56:07Z'
findings: []
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/9af65665941650557f7726a7/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/9af65665941650557f7726a7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/9a3dadef070b47feafc46aa3d3260d94/outputs/review-general-before-specific.md
raw-output-sha256: ec149620adb56916fe8924f2abe2cb2e994d86c5963828c35e342239d6661db3
---

# Review

The section order runs from general to specific. The untitled opening states the claim and the evidence portfolio. "Why live use can select" gives the general mechanism, counterfactual effect. "Initial selection is vulnerable to self-confirmation" qualifies that mechanism. "Why \"initial\" matters" bounds what the claim does not assert. Scope and Open Questions close the note.

No adjacent pair puts a specific case before the general rule it exemplifies. The self-confirmation section is a tension, but it follows the rule it qualifies. The section after it does not state a general rule that the tension depends on. The note uses no case-study framing or proper-noun sections that come before their generalization.
