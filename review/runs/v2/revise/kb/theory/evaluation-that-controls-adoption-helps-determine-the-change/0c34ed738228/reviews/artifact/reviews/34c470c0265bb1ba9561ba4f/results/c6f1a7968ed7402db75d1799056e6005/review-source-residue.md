---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A human approval required for adoption is part of the process that selected the
    revision. A later human assessment is not evidence of that same contribution to
    selection.
  reason: The opening paragraph states that the distinction does not depend on whether
    a person or a program judges, yet the motivating paragraph states the consequence
    only for human approval and human assessment without marking humans as the leading
    case. A reader may take the claim as narrower than the title. Saying 'an approval'
    and 'a later assessment', or marking the human case as the motivating example,
    would align it with the claimed generality.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/34c470c0265bb1ba9561ba4f/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/34c470c0265bb1ba9561ba4f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: c6f1a7968ed7402db75d1799056e6005
completed-at: '2026-11-17T07:20:51Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/c6f1a7968ed7402db75d1799056e6005/outputs/review-source-residue.md
raw-output-sha256: d21b1dfdde2f604606dbdcf377d2e8b24b02bc6864f72fdd5e8b671cb21e85c3
format: 2
---

# Review

## Summary

The title and opening paragraph claim generality over any evaluator, "not whether a person or a program makes it". The body's KB-specific material, an agent proposing a KB instruction and a maintainer reviewing it, is explicitly framed as hypothetical cases, so it is marked illustration rather than residue. "Deployed system" and "declared system boundary" are general.

The one mild narrowing is the motivating paragraph, which shifts to human approval and assessment without signalling that this is the case of interest rather than the scope of the claim. It does not overcommit the note, because the opening sentence states the broader scope, so it is recorded as INFO.
