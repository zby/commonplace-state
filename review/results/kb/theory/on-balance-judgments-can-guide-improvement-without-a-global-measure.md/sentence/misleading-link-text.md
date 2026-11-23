---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 262edf34947f4789926811e68630a6b3
completed-at: '2026-11-20T18:54:22Z'
findings: []
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/408e66705384af19b4c9829e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/outputs/review-misleading-link-text.md
raw-output-sha256: 7dee2bf12ff15a9d2ea4287928190923e040cd40e52ce0500b31197280b4bec7
---

# Review

## Summary

I checked all four links against each target's title and opening, and against the cited section where the head did not settle the question:

- "[tag coverage trace](./evidence/tag-readme-trace-observed-causal-connection.md)": the target is the tag-readme causal-connection trace. Its "What changed afterward" section records the `covered_by` check catching a member that the `rg` recipe missed. The link text names the trace by the part the sentence relies on, so a reader following it finds what was promised.
- "[factory comparison fixed before development](./a-better-factory-claim-compares-operative-states.md)": the target's opening and assessment-relation section describe comparison requirements declared before development, with non-regression thresholds and a declared gain. This matches.
- "[a comparison tests only the contrast it actually makes](./an-experiment-identifies-only-the-contrast-it-actually-runs.md)": the text paraphrases the target's title claim. This matches.
- "[Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md)": the link text is the target's title. This matches.

All targets resolved, and none of the link texts gives a wrong impression of its target.
