---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
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
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/f9bcf815cb6f23842c1c88c4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/262edf34947f4789926811e68630a6b3/outputs/review-concept-attribution.md
raw-output-sha256: e04c8099475648fb8cf2cb99fe7702078092460acb8d97a002c651ce157a8107
---

# Review

## Summary

The body links to three notes, and the footer links to a fourth. I checked each place where the prose ties one of its concepts to a linked note:

- **Tag coverage trace** (`./evidence/tag-readme-trace-observed-causal-connection.md`): the note says the trace "records a validator finding a member the documented search missed." The target's "What changed afterward" section says that, after `covered_by` was adopted, "the new symbolic check caught a member the natural-language `rg` recipe had missed." The attribution matches.
- **Factory comparison** (`./a-better-factory-claim-compares-operative-states.md`): the note says such a comparison is "fixed before development" and "can require a gain while forbidding deterioration beyond a threshold on prior capabilities." The target declares non-regression thresholds on the predecessor's prior scope plus a declared improvement, both fixed while only the predecessor exists. The attribution matches.
- **Contrast note** (`./an-experiment-identifies-only-the-contrast-it-actually-runs.md`): the note uses it to say that preferring the successor does not identify which component deserves credit. The target names bundle-to-component attribution as one version of exceeding the observed contrast. The note's paraphrase "a comparison tests only the contrast it actually makes" keeps the target's concept.
- **Declared objective** (`./self-improvement-is-relative-to-a-declared-objective.md`, footer): the gloss "why the objective must be identifiable independently of the change it is used to judge" matches the target's "Antecedent" condition.

All targets resolved, and no attribution misstates the concept as the target treats it.
