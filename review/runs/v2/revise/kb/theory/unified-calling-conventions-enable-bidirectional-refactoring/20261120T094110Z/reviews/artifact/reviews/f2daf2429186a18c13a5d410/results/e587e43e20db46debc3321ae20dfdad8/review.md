---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that
    owns control flow rather than a graph DSL.
  reason: 'The scheduler section brings in a second contrast, imperative scheduling
    versus graph DSLs (LangGraph, CrewAI), with its own four-row table. Only its closing
    sentence ties it back to neural-symbolic refactoring. The table gives this side
    argument about as much space as the mechanism section gets, so the note''s weight
    shifts away from the calling-convention claim. Fix: shrink the section to the
    closing sentence''s point, that cross-boundary refactoring uses ordinary extract/inline/rename,
    and fold it into the mechanism or ''Why this matters'' section. Alternatively,
    mark it explicitly as a consequence of unified calling.'
  level: info
- scope: passage
  quotes:
  - A team can also switch back to a prompt to test a proposed change while the code
    still meets its current requirement.
  reason: 'The title''s word ''bidirectional'' depends mostly on this late paragraph.
    Step 4 of the numbered list adds an LLM call for new cases, but it does not move
    a codified component back into a prompt. The code-to-prompt direction is therefore
    stated only in the inherited framing of the opening and in one example after the
    list. A reader can find the claim but may remember only the neural-to-symbolic
    progression. Fix: name the reverse move in the list itself, or add one sentence
    after the core claim in the opening saying that the same name can move either
    way.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/e587e43e20db46debc3321ae20dfdad8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/f2daf2429186a18c13a5d410/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: e587e43e20db46debc3321ae20dfdad8
completed-at: '2026-11-20T09:44:18Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/e587e43e20db46debc3321ae20dfdad8/outputs/review.md
raw-output-sha256: 2dc4394a60ff8510700c39ec9d0fda79d922627310685e1546ba5982c9b44c31
format: 2
---

# Review

The core claim can be stated from the note's own commitments: if neural and symbolic components share a calling convention, which llm-do implements as name-based dispatch over one namespace, a component can move across the neural-symbolic boundary in either direction without changing its call sites. The title states this claim and the description repeats it. The opening paragraph ends with it: "The answer is a unified calling convention…". Only one sentence about the underspecified instructions framing comes before it. That sentence motivates the claim and does not bury it.

Most of the later material serves the claim. "The mechanism" explains how llm-do achieves uniform calls. "Why this matters for constraining" contrasts breaking changes with stable call sites and walks through the progression. "The connection to typed callables" places the convention in a wider view in three sentences. The open questions are scoped to unified calling.

The claim stays easy to find, so the outcome is PASS. Two shape issues make it less memorable than it could be. The scheduler section and its table add a separate contrast with graph DSLs that competes for attention. The reverse direction promised by the title gets less space than the forward direction, and most of it sits after the numbered progression. Neither issue hides the claim. Both could be fixed by compressing the scheduler material into one sentence about refactoring and by naming the reverse move next to the core claim.
