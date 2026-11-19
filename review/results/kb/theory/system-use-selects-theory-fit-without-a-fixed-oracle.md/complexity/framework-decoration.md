---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
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
  - A claim that is repeatedly retrieved but never changes work has little evidence
    of operative fit. A claim whose withholding, replacement, or perturbation changes
    search or recovery has stronger mediation evidence. A claim whose use survives
    later demands and beats a rival formulation has stronger selection evidence still.
  reason: The three-tier gradation is load-bearing because its ordering is a decision
    rule for weighing evidence. Its labels ("operative fit", "mediation evidence",
    "selection evidence") are never used again in the note, so the named vocabulary
    does more than the argument needs. Plain ordinal wording would keep the rule.
  level: info
- scope: passage
  quotes:
  - A portfolio of causal, predictive, operational, and transfer evidence may support
    selection.
  reason: This four-category grouping does not map cleanly onto the six-item list
    earlier in the note, and nothing uses the categories. It works as a one-sentence
    summary rather than a framework, so the cost is small. Aligning it with the list
    or dropping the category names would remove a second, unused taxonomy.
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/120754c9d448cfc78cc8965d/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/120754c9d448cfc78cc8965d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/d1938ea3e06c41ceb054cd0c125162fd/outputs/review-framework-decoration.md
raw-output-sha256: 9de33d204c45f67729fc7d931e2fd0cf7225a1aa30be19f89049b192f1217396
---

# Review

## Summary

The note's structures are load-bearing. Two pieces of named vocabulary go beyond what the argument uses, but neither is large enough to warrant a warning.

## Structures checked

**The six-item consequence list in the opening.** Replacing it with one sentence, such as "fit shows up in many downstream consequences," would lose the discriminating criteria that later sections use:

- "Changes proposal, diagnosis… rather than merely being cited" feeds the counterfactual-effect argument.
- "Distinguish a bad candidate from a bad underlying theory" feeds the blame-assignment paragraph.
- "Relative to rival formulations" and "transfers" feed the self-confirmation countermeasures.
- "Preserve relevant organization" and "survive later evidence" feed the account of later work exposing outcomes.

The list supports the claim that the items together discriminate more strongly than static coherence alone. It is not decorative.

**The counterfactual evidence gradation.** Its ordering is a usable rule for ranking evidence: retrieval alone is weaker than perturbation sensitivity, which is weaker than survival against a rival. The tier labels go unused (recorded as INFO).

**The Scope bullet's four evidence categories.** This is a second, unaligned taxonomy that nothing uses (recorded as INFO).

The note contains no tables, notation or equations.
