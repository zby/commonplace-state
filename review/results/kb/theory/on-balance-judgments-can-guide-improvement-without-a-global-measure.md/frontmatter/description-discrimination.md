---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 29c4b2bc1a1b699bdc52eecaf4ed9e4cbc85c039aff97f8c4457692013a9166d
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 037d102ff8484f5dba42271fb062fc58
completed-at: '2026-11-20T18:52:48Z'
findings:
- scope: document
  quotes: []
  reason: 'The description names the question (''which uncertainties justify further
    investigation'') but not the note''s answer: investigate only when a plausible
    answer could reverse the choice. Stating that criterion would add implication
    and make the note easier to pick from a result list.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/037d102ff8484f5dba42271fb062fc58/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/6e20fc400ede001798c4737a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/037d102ff8484f5dba42271fb062fc58/outputs/review-description-discrimination.md
raw-output-sha256: 3c226d6fc81dc7d0292f0f203e3463aa7969d4fa2471344492e5720890b4c6d1
---

# Review

## Summary

The description does more than restate the title. The title says on-balance judgments can guide improvement without a global measure. The description adds scope by locating the decision: keeping a change when gains and losses fall on different tasks. It also adds a second topic the title does not mention: which uncertainties justify further investigation before acting. An agent that searches for how to decide a mixed-result change, or when to stop gathering evidence, could pick this note from a short list.

The description announces the investigation question but does not give the note's answer. That is an optional improvement, not a failure.
