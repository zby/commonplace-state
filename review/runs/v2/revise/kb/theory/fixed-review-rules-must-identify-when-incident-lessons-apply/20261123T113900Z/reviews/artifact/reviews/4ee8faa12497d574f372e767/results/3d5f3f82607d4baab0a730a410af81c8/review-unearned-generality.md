---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 8cb1ad7dbf18f84e88042c601bd955e4265ba65f26de48e2402ad716359e9d11
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/4ee8faa12497d574f372e767/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 3d5f3f82607d4baab0a730a410af81c8
completed-at: '2026-11-23T11:41:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/3d5f3f82607d4baab0a730a410af81c8/outputs/review-unearned-generality.md
raw-output-sha256: af1b08974fc12fe7bece196875a50d95752c7f3a9d0b477ae6f020d05f117fa6
format: 2
---

# Review

## Summary

The title's vocabulary is close to the argument's level: "review rule", "lessons", "incidents" and "identify when they apply". These terms match the example of a wiki reviewer, a consult-past-incidents instruction and a citation-independence lesson, with no more abstract stand-ins. Downgrading to the concrete case, "a check-past-incidents instruction for citation review", narrows the claim's coverage, but the title is not phrased in inflated terms such as "retained artifact" or "standing procedure". The description's "standing instruction" is a near-synonym of "fixed rule". Abstraction is not spread through the body. The note has one instance class, but its wording does not claim more than that class supports, so this gate has no finding.
