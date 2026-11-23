---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - If such blockers were widespread and costly, that would challenge the default
    itself.
  reason: 'Possible tension with the note''s own investigation rule: ''investigate
    an unknown only if a plausible answer could reverse the choice''. The note says
    widespread blockers would reverse the 3.11 default, and it says its checks are
    not a survey of how often each reason applies. It affirms the default anyway,
    without saying that widespread blockers are implausible or that it investigated
    them. The note probably assumes they are implausible, but it does not say so,
    so this needs the author to confirm.'
  level: info
- scope: passage
  quotes:
  - not a claim that every project should use the same measure
  reason: Possible definition drift. The title uses 'global measure' for a score that
    ranks every version, and the note says such a score is unnecessary. Here 'measure'
    refers to Commonplace's declared objective, and the section heading says 'choose
    to count'. The surrounding text treats the objective as a criterion for on-balance
    judgment, not a score, so this is drift in wording rather than a contradiction.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/ad235d2a54bf81aa7b6d7bc3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: c479bc55423643ddb825da7ad43b3276
completed-at: '2026-11-20T18:55:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/c479bc55423643ddb825da7ad43b3276/outputs/review-internal-consistency.md
raw-output-sha256: dda07ffbd7027cd3d662c8f811ee77aaf55717008136c492b35c4c01df54514c
format: 2
---

# Review

## Summary

The sections do not contradict each other. The opening Python discussion, the 3.11 table, the "What analysis can settle" section and the Commonplace application all hold the same position. A choice between alternatives needs reasons about who gains or loses and why it matters, not a global score. Value weights come from judgment, and unknowns are investigated when they could reverse the choice. Two places need a human check. The 3.11 default is affirmed while a reversing unknown (how widespread blockers are) is left uninvestigated without saying why. The word "measure" also shifts meaning between the title and the Commonplace section.
