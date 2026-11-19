---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Fit is exposed through a portfolio of consequences spread across operation and
    time, including whether a claim:'
  reason: The six-item portfolio is introduced with 'including', so it does not claim
    full coverage, and boundary cases map onto it with only mild strain. A claim that
    duplicates a retained neighbour, or one stated at the wrong level of abstraction,
    has no item of its own; such redundancy surfaces only indirectly through 'reduces
    search, repair, or intervention relative to rival formulations'. These are fit
    dimensions the grounding note names. The note's explicit contrast with 'static
    coherence alone' suggests the omission is deliberate, so this is strain, not a
    gap.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/e5556df7c34cbc0bbaf3c678/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/e5556df7c34cbc0bbaf3c678/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 0b6aab3bf2ce43d9808afc045b836a39
completed-at: '2026-11-16T18:57:58Z'
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/0b6aab3bf2ce43d9808afc045b836a39/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 33134146fc4f347b3115d5cc015a2c13eb7759c8a96fbdb646fbaf221199ff40
format: 2
---

# Review

## Summary

The note has two enumerations. One is the portfolio of use consequences through which fit is exposed. The other is the list of possible causes of a failed modification. Neither claims to be complete. The portfolio is introduced with "including", and the note then says "No one item is a complete oracle". The cause list is governed by "may reflect".

Boundary cases:

- **Simplest instance.** A claim that is retrieved but changes nothing maps cleanly. The first item and the counterfactual-effect paragraph cover it.
- **Extreme instance.** A claim that is useful only under a delayed demand maps to "yields expectations that survive later evidence" and to the preservation item.
- **Between items.** A claim that raises repair cost is negative evidence under the comparative "reduces search, repair, or intervention" item.
- **Adjacent concept.** A redundant claim, or one at the wrong level of abstraction, maps only through rival comparison. This strain is recorded as an INFO finding.

Adding categories is not warranted. The list already matches its argumentative role, which is to show that fit has a distributed, testable shape.
