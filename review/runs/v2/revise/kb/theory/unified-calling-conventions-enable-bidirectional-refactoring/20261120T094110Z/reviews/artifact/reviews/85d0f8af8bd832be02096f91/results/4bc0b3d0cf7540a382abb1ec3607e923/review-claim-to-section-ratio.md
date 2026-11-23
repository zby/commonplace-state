---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Both are callables with defined interfaces. The unified calling convention is
    what makes the type-theoretic view practical rather than just analogical.
  reason: 'The typed-callables section is the thinnest section: beyond the concrete
    detail that `.agent` files pair frontmatter with a prompt, it mostly restates
    the mechanism section''s point that both component kinds present one interface.
    It still carries a distinct (if small) claim, so it does not push the section
    count past the claim count.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/85d0f8af8bd832be02096f91/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 4bc0b3d0cf7540a382abb1ec3607e923
completed-at: '2026-11-20T09:42:15Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/outputs/review-claim-to-section-ratio.md
raw-output-sha256: a6ed7feeb920871c7bc271c3caafc0c9e99e0ddd113191c20bf3744826e5bcd1
format: 2
---

# Review

The note's distinct non-obvious claims are:

1. A unified calling convention, implemented by name-based dispatch, makes the neural/symbolic boundary movable without changing call sites (intro and "The mechanism").
2. Without it, each codification step is a breaking change that pushes toward big-bang rewrites; with it, constraining and relaxing become incremental, and the reverse move to a prompt can serve as a cheap experiment ("Why this matters for constraining").
3. An imperative scheduler, unlike a graph DSL, lets boundary refactorings use ordinary code refactorings ("The scheduler layer").
4. The unified convention turns the typed-callables view from analogy into practice ("The connection to typed callables").

The body has five substantive sections (intro plus four headed sections) and an Open Questions section, which is a separate support unit carrying boundary conditions (scale, debugging, host language). Claim 1 spans the intro and the mechanism section, but the intro states the problem and the mechanism section supplies the inference step (name-based dispatch and late binding), so neither merely restates the other. Sections do not outnumber claims plus necessary support units. The typed-callables section is thin, as the info finding notes, but it is not a restatement of framing.
