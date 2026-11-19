---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - without paying avoidable transition cost
  reason: '''Avoidable'' has no stated baseline. One reading: avoidable given the
    KB''s existing surfaces and operations. Another: avoidable by any design change,
    including new indexes, summaries or links that cost authoring and maintenance.
    The first makes the criterion an audit of the current design. The second makes
    it a design target that would need to be weighed against upkeep. The Open questions
    section defers the cost currency but not this baseline. Because the note presents
    the criterion as a qualitative prompt for possible friction, not a scored test,
    it is not clear that the difference changes any inference the note draws, so this
    is INFO.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/24c64988949b6574b27b04ea/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/24c64988949b6574b27b04ea/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-underspecified-assertions.md
raw-output-sha256: 8b9c328c872cbe52e80fbfa46606cda7568d9f984891192e25e230e0a1843a1e
format: 2
---

# Review

## Summary

The note's load-bearing assertions are mostly resolved in context. "Resolution" is defined as the scope and detail a view exposes. "Views" is grounded by examples: titles, descriptions, bodies, indexes, search results, link phrases and generated summaries. "Losing the relationship" is spelled out by the fourth question, whether the transition keeps why the two views belong together. "Inexpensive" leaves its cost currency open, but the note says so explicitly and lists the candidate measures under Open questions. A reader therefore knows the assertion is deliberately qualitative and not silently ambiguous.

The Boundaries section separates the criterion from addressability grain, pointer accuracy and retrieval recall in terms that fix the comparison. The remaining possible ambiguity is the baseline behind "avoidable" (INFO). No assertion leaves a material choice unresolved at WARN level.
