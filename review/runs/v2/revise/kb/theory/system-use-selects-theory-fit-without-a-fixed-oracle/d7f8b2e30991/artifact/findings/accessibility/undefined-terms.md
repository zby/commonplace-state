---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 8a50c381505d456c8bee5240864437ff
completed-at: '2026-11-16T18:55:47Z'
findings:
- scope: passage
  quotes:
  - branch allocation
  reason: '"Branch allocation" appears only in this list item with no gloss; the note
    never says what branches are (search branches, candidate lines of work, code branches)
    or what allocating them means, so a reader without KB context cannot tell what
    consequence of fit this item names. Add a short gloss, e.g. which candidate lines
    of work receive effort.'
  level: warn
- scope: passage
  quotes:
  - stronger mediation evidence
  reason: '"Mediation evidence" is a technical term (evidence that the claim causally
    mediates the change in work) used without a gloss. The surrounding sentence about
    withholding, replacement or perturbation gives enough context to infer it, so
    this is minor; a brief parenthetical would make the contrast with "operative fit"
    and "selection evidence" explicit.'
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/9c8ada0ad837701669c0dda8/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/9c8ada0ad837701669c0dda8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/8a50c381505d456c8bee5240864437ff/outputs/review-undefined-terms.md
raw-output-sha256: 65fbb81539681f0775273d74f4d2aef88b3a094a1038b28a0681045833adca64
---

# Review

Most technical terms are glossed or inferable at first use. "Working theory" and "theory fit" are grounded by the opening paragraph; "fixed oracle" is paraphrased in the next paragraph as an automatic evaluator that fully decides fit; "selection environment" is explained in the same sentence that introduces it; "self-sealing", "held-out demands" and "read-back" are inferable from their sentences. No active vocabulary term from `AGENTS.md` is used in a technical sense in the body ("refinement path" uses bare refinement in its ordinary sense).

The one term a newcomer cannot recover is "branch allocation", which appears in the list of fit consequences without any context about what branches are. "Mediation evidence" is inferable but would benefit from a short gloss.
