---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/ac1dd9845bb25b752a86baec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c479bc55423643ddb825da7ad43b3276
completed-at: '2026-11-20T18:55:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-grounding-alignment.md
raw-output-sha256: 2326c3fee00a857e45553bd0c0c254391fe15991f397039e4a10ee69b3c6805d
format: 2
---

# Review

## Summary

The note uses four links, all to library artifacts. I checked each for representation.

- **Tag coverage trace** (`evidence/tag-readme-trace-observed-causal-connection.md`). The note says the trace records a validator finding a member that the documented search missed. The trace reports that adopting `covered_by` caught a block-YAML member the `rg` recipe had missed. The note calls this "a local gain", which is no wider than the trace claims.
- **Factory comparison** (`a-better-factory-claim-compares-operative-states.md`). The target declares, before development, a required gain plus non-regression thresholds on prior capabilities. That matches "require a gain while forbidding deterioration beyond a threshold on prior capabilities". The target's Scope section also says passing does not settle the broader on-balance judgment, which is consistent with the note's use.
- **Contrast note** (`an-experiment-identifies-only-the-contrast-it-actually-runs.md`). The target rules out bundle-to-component attribution. The note invokes exactly that limit for crediting a component.
- **Declared objective** (footer, `self-improvement-is-relative-to-a-declared-objective.md`). The note cites it for the requirement that the objective be identifiable independently of the change, and the target states that antecedence condition.

None of these citations is stretched beyond the target's claim or scope.
