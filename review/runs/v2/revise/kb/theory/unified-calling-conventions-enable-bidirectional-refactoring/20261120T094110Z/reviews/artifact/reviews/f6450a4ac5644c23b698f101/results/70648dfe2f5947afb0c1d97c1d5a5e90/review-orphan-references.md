---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI)
    where orchestration is defined as node-edge graphs.
  reason: 'A concrete empirical characterization of two named external frameworks
    is given without a source, and the following table extends it ("Global context
    through graph", "Redraw edges, update graph"). The reader cannot check it, and
    it is not uniformly accurate as stated: CrewAI''s primary abstraction is crews
    of agents assigned tasks rather than a node-edge graph. Cite the frameworks''
    documentation or a KB review of them, or narrow the claim to graph-defined orchestration
    such as LangGraph''s.'
  level: warn
- scope: passage
  quotes:
  - This friction discourages incremental refactoring and pushes toward big-bang rewrites.
  reason: A causal empirical claim about team behavior with no observation or source
    behind it. It is plausible as reasoning from the stated costs, so it is recorded
    as INFO; marking it as an expectation rather than an observed effect would make
    its status legible.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/prose/orphan-references.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/prose/orphan-references.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/f6450a4ac5644c23b698f101/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 70648dfe2f5947afb0c1d97c1d5a5e90
completed-at: '2026-11-20T09:42:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/outputs/review-orphan-references.md
raw-output-sha256: 21ce25b0c80d67fe82f271d9d5cb218e6d63ab7e5f49c5d16eb542f7242fcc2a
format: 2
---

# Review

## Summary

The note contains no numbers or named studies. Its main empirical anchor, llm-do, is linked to its repository, and the `ticket_classifier` and `sanitize_filename()` cases are framed as illustrations rather than reported observations.

The unsourced characterization of LangGraph and CrewAI is the one concrete external claim the reader cannot evaluate, and it bears on the scheduler comparison table. The friction claim is a lesser instance of unattributed empirical framing.
