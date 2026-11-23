---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 0337fecd13014fbd8bc366a4aa368dc5
completed-at: '2026-11-20T09:44:15Z'
findings:
- scope: passage
  quotes:
  - This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI)
    where orchestration is defined as node-edge graphs.
  - Local scope — each agent gets only its arguments
  - 'Native Python: `if`, `for`, `try/except`'
  reason: 'The scheduler section''s job in the note''s argument is one inference step:
    because llm-do orchestration is ordinary imperative code, moving a component across
    the neural-symbolic boundary uses ordinary refactorings (extract function, inline,
    rename). The closing sentence of the section already states this. The four-row
    comparison table with graph DSLs elaborates beyond that role: the State and Control
    flow rows describe general advantages of imperative orchestration that do not
    bear on calling-convention uniformity or boundary movement, and only the Refactoring
    row supports the claim. Compress the section to two or three sentences that name
    the contrast with graph DSLs and keep the refactoring consequence, dropping the
    table or reducing it to the Refactoring row.'
  level: warn
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/0337fecd13014fbd8bc366a4aa368dc5/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/19b0ffcf6599446b82c1b8c9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/0337fecd13014fbd8bc366a4aa368dc5/outputs/review.md
raw-output-sha256: 404208482f1db423aa8a795f953ba0da34d17ddee8175ec0668a6dd8f97e2bfb
---

# Review

## Summary

Most detail in the note is proportional to its role. One passage outgrows it: the scheduler-layer comparison table.

The note claims that a unified calling convention makes the neural-symbolic boundary movable, so refactoring across it becomes a local operation. The supporting route has three parts. Name-based dispatch is the mechanism. The four-step progression shows codification and relaxing without call-site changes. The typed-callables section ties the claim to the callable view.

The scheduler section adds one inference step: imperative orchestration lets boundary moves use ordinary code refactorings. Its final sentence states that step on its own. The table before it compares graph DSLs and llm-do on four axes. Two of those axes, state scoping and control-flow constructs, make a broader case for imperative orchestration that this note does not need. That is the overhang flagged above.

## Non-obvious passes

- **Prompt-testing paragraph (`ticket_classifier` routing).** The paragraph is a six-sentence worked example, but it is the note's main concrete support for the reverse direction that "bidirectional" in the title promises. It shows that moving code back to a prompt for exploration is cheap when the name and output labels stay fixed. Cutting it to a phrase would leave relaxing as an abstract assertion, so its length is justified.
- **Name-based dispatch paragraph.** It lists three properties of name-based dispatch. Late binding is not strictly needed for the claim, but the list is one sentence long and explains why names, rather than object references, make the interface implementation-agnostic. It does not need compression.
- **Four-step progression.** Each step carries part of the codify-then-relax cycle, and the repeated statement "the call site doesn't change" is the evidence for the claim, not padding.
