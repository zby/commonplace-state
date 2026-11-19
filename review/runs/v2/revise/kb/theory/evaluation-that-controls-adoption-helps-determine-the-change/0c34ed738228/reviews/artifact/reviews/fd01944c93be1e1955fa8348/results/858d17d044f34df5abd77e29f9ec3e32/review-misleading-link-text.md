---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/fd01944c93be1e1955fa8348/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/fd01944c93be1e1955fa8348/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 858d17d044f34df5abd77e29f9ec3e32
completed-at: '2026-11-17T07:21:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/858d17d044f34df5abd77e29f9ec3e32/outputs/review-misleading-link-text.md
raw-output-sha256: 0f46e74812383a09d67c07a49c42974a0e893736792ce036b90fc7c6cdcd287e
format: 2
---

# Review

The body has two links, and both resolve.

- "[the better-factory comparison]" points to `a-better-factory-claim-compares-operative-states.md`, titled "A better-factory claim compares operative states under an antecedent assessment relation". The link text names that claim accurately. The target contains the adoption-versus-assessment distinction the surrounding sentence promises: it separates candidates from the installed successor and says, "Whether an evaluator also controlled adoption is a separate causal question".
- "[operative change]" points to `definitions/operative-change.md`, which defines that term. The surrounding sentence leads the reader to expect a criterion separating live, depended-on changes from inert ones, and the definition supplies one (a behavioral-authority path; "an approved patch never merged" is excluded).
