---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Adoption here means entering a live behavioral path on which later operation depends,
    as distinguished by [operative change](./definitions/operative-change.md).
  reason: 'The operative-change definition requires two conditions: persistence over
    a declared horizon and a behavioral-authority path. Its misuse cases warn against
    reporting operativity without the horizon. The note''s paraphrase keeps the behavioral
    path and later dependence but drops the horizon condition. The route is still
    plausible, and the definition''s example of an approved patch that is never merged
    supports the note''s point that an unadopted proposal is not an improvement. The
    omission is not load-bearing for the note''s distinction.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/025cf07d2d665cbc2b90e1c4/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/025cf07d2d665cbc2b90e1c4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 388f012ff0b54165ac3ed49bf5e4359d
completed-at: '2026-11-17T07:22:54Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/388f012ff0b54165ac3ed49bf5e4359d/outputs/review-grounding-alignment.md
raw-output-sha256: 8d21c7fbc2a059186082d69e0628f42c48d8ec03e9cd88f985987af09895c820
format: 2
---

# Review

## Summary

The note links two library artifacts.

- **Better-factory note.** The note supplements the adoption-versus-measurement distinction in that note. The target makes this distinction. It says that a better-factory claim compares adopted operative states and that a staging comparison only supplies evidence for adoption. Its Scope also states that "Whether an evaluator also controlled adoption is a separate causal question; a description cannot change whether its judgment was required for installation." The note invokes this claim at the target's scope and develops it. The target says "comparison" where the note says "measurement", but the distinction is the same.
- **Operative-change definition.** The note uses this definition to fix what adoption means. The use is accurate in substance, apart from the omitted horizon condition recorded as INFO.

The note does not cite either target for a mechanism or scope broader than the target states.
