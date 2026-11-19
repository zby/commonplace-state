---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - After opening the detail, can the reader recover a relevant broader view
  reason: The four questions treat the broad and detailed views as separate things
    the reader opens and leaves. A boundary case is a single long artifact whose headings
    or opening summary give the broad view and whose sections give the detail. Coverage
    is still possible, since a view is defined by scope and detail rather than by
    artifact, but the questions' wording ('opening the detail', 'recover') strains
    for within-artifact switching.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/9a9e12f946b2ef6c8bea559c/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/9a9e12f946b2ef6c8bea559c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-completeness-boundary-cases.md
raw-output-sha256: ef5fbf04fe14178a117993761107cb8c047331e4d17fa5c776a6a90300d204a5
format: 2
---

# Review

## Summary

The note has two enumerations: four Commonplace mechanisms and four questions the criterion prompts. Neither claims to be exhaustive. The mechanisms sit under a heading that limits them to Commonplace, and the questions are said to "identify possible friction" without supplying a scoring rule.

Boundary cases tested against the stated definition, where resolution is the scope and detail a view exposes:

- **Simplest instance:** a task answered from one view alone. The note covers it with "not ... a claim that every task needs the same sequence of views" and "Nor does every task need to return to a broad view."
- **Lateral movement between sibling notes at the same scope:** this falls outside resolution-switching by definition, and the note does not claim it.
- **Scope and detail moving apart:** an index has wider scope and less per-item detail than a note. The note's separate mechanisms for detail (title/description/body) and for scope (index/note) handle this cleanly.
- **Outward route without an authored link:** the Boundaries section covers this explicitly through backlinks, indexes and search.
- **Within-artifact switching:** a heading or summary and the sections it introduces. This maps onto the definition, but the questions' wording is strained for it (INFO above).

No case clearly falls outside the claimed coverage. The enumerations are short and match their role, so adding to them is not warranted.
