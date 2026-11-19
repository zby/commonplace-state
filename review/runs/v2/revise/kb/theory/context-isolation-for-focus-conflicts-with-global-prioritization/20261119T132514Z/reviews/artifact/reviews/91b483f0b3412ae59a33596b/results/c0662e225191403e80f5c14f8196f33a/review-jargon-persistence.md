---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/91b483f0b3412ae59a33596b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: c0662e225191403e80f5c14f8196f33a
completed-at: '2026-11-19T13:26:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/outputs/review-jargon-persistence.md
raw-output-sha256: fa110f8e6a297d48852ff3fbca605a6951f8debd678caa9b0426db7be03f89ad
format: 2
---

# Review

## Summary

No KB-internal term loses its grounding through repeated use.

The note's recurring coined terms are "narrow-deep" and "wide-shallow". Section two defines both in the same sentence that introduces them: a narrow-deep context serves deep problem solving, and a wide-shallow comparison set serves global prioritization. Almost every later use pairs the term with a self-explaining noun ("wide-shallow triage", "a wide-shallow pass selects from compressed summaries"). Those pairings restate the meaning, so a reader does not have to scroll back.

"Scale-bearing local facts" is defined with concrete examples in the numbered execution item. After that it appears only once more in the body, in the first open question. That is below the gate's threshold of more than two uses after definition. "Comparison set" and "context isolation" are close to plain language, and the opening sentence glosses context isolation. The note glosses "unresolved frontier" once, and the body reuses it only once, as "compressed frontier items".

No term is used often enough after its definition to become opaque, so no finding is raised.
