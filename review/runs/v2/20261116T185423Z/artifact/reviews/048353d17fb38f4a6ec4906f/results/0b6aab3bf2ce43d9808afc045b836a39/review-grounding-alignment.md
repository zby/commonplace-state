---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - explains why qualities with weak operative signals can disappear under selection
    despite sounding important
  reason: The footer cites the weakly-discriminated-qualities note as a mechanism
    for qualities that 'disappear under selection'. That target is an explicitly marked
    statistical conjecture. It defines underselection as 'less enrichment through
    acceptance, not necessarily absolute decline', and says absolute degradation needs
    an additional directional mechanism. The gloss therefore presents a conjecture
    as an explanation and stretches its scope from weaker enrichment to disappearance.
    No body claim of this note depends on the link, so the gap is not load-bearing.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/048353d17fb38f4a6ec4906f/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/048353d17fb38f4a6ec4906f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 0b6aab3bf2ce43d9808afc045b836a39
completed-at: '2026-11-16T18:57:58Z'
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/0b6aab3bf2ce43d9808afc045b836a39/outputs/review-grounding-alignment.md
raw-output-sha256: 20ec7daf8472de402ea7acfb8e582ec65ad671104d110d7796c13c7f60ea60ee
format: 2
---

# Review

## Summary

I checked each linked library artifact against its title, description and opening.

- **A claim's test record does not determine its fit in a working theory.** The opening invokes it for the claim that independently tested claims can still fit poorly. The target says this directly: "A well-tested claim may fit poorly". The representation is accurate.
- **System use provides evidence of theory fit and causal usefulness, not an independent test.** The self-confirmation section invokes it by its title claim. Its account of self-confirmation matches the target's third paragraph. The target names held-out demands, transfer and controlled rival comparison, and the note's list of controls overlaps that list. The note adds withholding and perturbation as its own items without attributing them to the target. Its blame-assignment paragraph matches the target's account of read-back granularity.
- **Holding a program theory means sustaining coherent search under delayed feedback.** The footer cites it for longitudinal consequences through which program-theory fit becomes visible. This is consistent with the target's test of coherent modification under delayed evidence.
- **Use tests a decomposition locally; retained rationale is what makes transfer testable.** The footer cites it for bounding what one successful configuration establishes beyond its context. This matches the target's title claim.
- **Weakly discriminated qualities tend to be underselected.** The footer's "mechanism" gloss overstates the target, as recorded in the INFO finding. The body does not rely on it.

No material claim in the body is grounded more broadly than its linked support allows.
