---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'This requires **name-based dispatch**: components are identified by string name
    rather than direct object reference.'
  reason: The title and opening make a general claim about unified calling conventions,
    but this sentence turns llm-do's implementation choice into a requirement of the
    general mechanism. A shared interface can also be achieved with direct references
    to polymorphic objects; names are needed specifically where an LLM emits the call
    as a string. Either scope the requirement to LLM-emitted calls or present name-based
    dispatch as how llm-do achieves the shared interface.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/ff43fc3485ebb066050c01db/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 70648dfe2f5947afb0c1d97c1d5a5e90
completed-at: '2026-11-20T09:42:41Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/70648dfe2f5947afb0c1d97c1d5a5e90/outputs/review-source-residue.md
raw-output-sha256: 028b46ade96351deff8911e861769c290c7837cf08bb25af136631288ae22be9
format: 2
---

# Review

## Summary

The title and opening claim generality: any system whose neural and symbolic components share a calling convention. llm-do is introduced explicitly as the demonstration ("llm-do implements this"), and most llm-do vocabulary is marked as belonging to it: `.agent` files, the hybrid VM, the "llm-do Scheduler" column and the scheduler open question.

The four-step progression uses neutral terms (agent, Python, call site) and reads as general.

The one leak is the name-based-dispatch sentence, which states llm-do's design choice as a general requirement without marking it as the illustrative case.
