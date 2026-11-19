---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Both cases involve reading results and forming a verdict.
  reason: The two hypothetical cases mostly restate the opening distinction concretely;
    this section could shrink to a sentence or two. The structure is still justified
    overall because other parts of the note carry boundary cases that a single paragraph
    would lose.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/97d45a7ee506a41110817742/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/97d45a7ee506a41110817742/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: f5a3ca40a144465c890c72456227bc77
completed-at: '2026-11-17T07:20:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/f5a3ca40a144465c890c72456227bc77/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 072283bcc726495cb87b76be567e1bc54e1c6567c284f6822dc303ce9ab67095
format: 2
---

# Review

## Summary

The core insight is fairly simple: a judgment helps determine a system revision only when it controls whether that revision is adopted. If the note were collapsed into one paragraph, that claim and its illustration would survive. Several load-bearing points would be lost or crammed together:

- A later assessment can still have a causal role, but in a different transition (a revision or rollback). This blocks the misreading that assessment after adoption is causally inert.
- Required approval is a fact about the process. Redescribing the episode cannot change it. This inference targets a specific reframing move and is the point the description emphasises.
- "Adoption" is anchored to operative change: a favourable assessment of a proposal that is never adopted does not count as improving the deployed system.
- Three scope conditions: other influence is not ruled out, learner-boundary membership is a separate question, and approval does not establish quality, including the risk that a test available to the proposing system gets optimized against.

These are real boundary cases and inference steps, so the multi-section structure is warranted. The only compressible part is the paired-case illustration, noted as INFO.
