---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 4bc0b3d0cf7540a382abb1ec3607e923
completed-at: '2026-11-20T09:42:15Z'
findings:
- scope: passage
  quotes:
  - the type-theoretic view that llm-do operationalises
  reason: The body already links instructions-are-typed-callables and says "llm-do
    operationalises this". The footer entry repeats that relationship nearly word
    for word, with no relationship label and no added navigational context.
  level: warn
- scope: passage
  quotes:
  - 'the operational mechanism: observe agent behavior, extract to code — enabled
    by stable call sites'
  reason: Step 2 of the body links spec-mining and explains it as observing that a
    spec consistently resolves one way and committing that to code; step 3 states
    that the call site does not change. The footer restates that framing without a
    relationship label or new context.
  level: warn
- scope: passage
  quotes:
  - the mechanism that unified calling makes frictionless
  reason: The body links constraining and argues that unified calling removes the
    breaking-change friction from each step. The footer compresses that argument without
    adding a label. This entry is borderline because a definition link in the footer
    still has some lookup value.
  level: info
- scope: passage
  quotes:
  - the phase transition from neural to symbolic that unified calling makes a local
    operation
  reason: The body links codification and the intro already says refactoring across
    the boundary "becomes a local operation". The footer adds the 'phase transition'
    gloss but no relationship label. This entry is borderline for the same reason
    as the constraining entry.
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/e3b701c1b171bd2e1ce10879/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/outputs/review-connection-inflation.md
raw-output-sha256: a4b6a83c813bec69ae57767e2f1f51fd47fad9e5eec292de37792f2decd11872
---

# Review

The footer has eight entries. Three add value the body lacks. The "Abstracted into" entry and the two "extends:" entries for programming-practices and relaxing signals point to notes the body does not link and have typed relationships. The prompting-changes entry repeats an inline link, but it adds a `grounds:` label and an explicit framing of the dependency, so it passes the gate's second question.

The four remaining entries carry no relationship label and repeat the body's inline framing for the same targets. Two do so closely: typed-callables, where the footer echoes the body's "operationalises", and spec-mining, where the footer paraphrases steps 2 and 3. Those two are inflated. Constraining and codification are near-restatements as well, but footer links to core definitions keep slight lookup value, so they are recorded as info. Adding a typed label with a distinct reader-facing reason, or dropping the entries, would resolve the findings.
