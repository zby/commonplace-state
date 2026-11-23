---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
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
  - Agent ──calls──▶ Tool ──calls──▶ Agent ──calls──▶ Tool ...
  reason: The ASCII call-chain diagram adds nothing to the sentence after it ("The
    calling convention is uniform across the chain"). Deleting it leaves clarity and
    precision unchanged, and it supports no prediction or derivation. It is decorative
    notation.
  level: warn
- scope: passage
  quotes:
  - Local scope — each agent gets only its arguments
  - 'Native Python: `if`, `for`, `try/except`'
  reason: 'The four-row Graph DSLs vs llm-do Scheduler table introduces more categories
    than the argument uses. The conclusion that follows it relies only on the Refactoring
    row, with some support from the Orchestration row. The State row (global context
    vs local scope) and the Control flow row are never used again. The argument survives
    as one sentence: imperative orchestration makes boundary refactoring ordinary
    code refactoring, with no graph topology to update.'
  level: warn
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/b14694c3fbda46309fe600ea/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/4bc0b3d0cf7540a382abb1ec3607e923/outputs/review-framework-decoration.md
raw-output-sha256: ceafa64ef0d54d1b4703711754c729cae0b10724af0a3af7501d204469cd8056
---

# Review

The note has three structures.

- **Numbered progression (start neural → observe → codify → extend via relaxing).** This is load-bearing. It is an ordered sequence with a concrete example at each step, and it shows the call site staying stable at both the codify step and the relax step. That stability is the note's central inference. Prose would need the same steps.
- **ASCII call-chain diagram.** This is decorative. The sentence after it states the same point, and the diagram adds no categories, boundary cases or derivations.
- **Graph DSL vs scheduler table.** This is partly decorative. The Orchestration and Refactoring rows support the following conclusion. The State and Control flow rows add distinctions that no later inference, decision or prediction uses. The table could become one or two sentences, or keep only the rows the argument needs.
