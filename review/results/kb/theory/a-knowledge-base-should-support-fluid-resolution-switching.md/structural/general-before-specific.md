---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 781f95f45d1445dc997e161dfef0215d
completed-at: '2026-11-16T22:30:03Z'
findings:
- scope: passage
  quotes:
  - Commonplace mechanisms
  reason: 'The system-specific mechanisms section, named by a proper noun, comes before
    ''The evaluative criterion'', which states the general criterion those mechanisms
    serve. The mechanisms exemplify the criterion rather than qualifying it. However,
    the opening section already states the general rule: views at different scopes,
    and cheap switches in both directions. So the reader meets the rule before the
    instances, and the later section only formalizes it. The order is defensible.
    Moving the criterion section first would also be acceptable.'
  level: info
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/db4fe4db64d635c17d1fdefb/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/db4fe4db64d635c17d1fdefb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/781f95f45d1445dc997e161dfef0215d/outputs/review-general-before-specific.md
raw-output-sha256: f079e28bff6f18f2a785f0e55c9e4e6a4fe39b7a2b71e1c802c9d2cfed776fe0
---

# Review

## Summary

There are five adjacent section pairs after the introduction. Only one pair
places a more specific section before a more general one: "Commonplace
mechanisms" before "The evaluative criterion". That pair gets an INFO
finding, not a WARN. The introduction already states the general pattern,
so the reader does not see the instances before the rule.

The other pairs pose no ordering problem:

- "Connection to discovery" follows the criterion and extends it.
- "Boundaries" qualifies the concept after it has been stated.
- "Open questions" comes last, as expected.
