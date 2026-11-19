---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 0519683dd2a2ad488108c956b1c1a59791f57be492893178645772a263c8257f
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:03Z'
findings: []
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/8219c846964482c4ac427162/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/8219c846964482c4ac427162/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-unearned-generality.md
raw-output-sha256: 55a73b33a1321976dca0657289860c9856188439dcf4fc2ff17274b2e2d21003
---

# Review

## Summary

The central claim's abstract terms are "view", "resolution" and "knowledge base".

- **"View."** The concrete term it could stand in for is "note" or "index". A downgrade to "notes and indexes" loses cases the note actually argues from: titles and descriptions as views of a single note, search results as a broad entry route, contextual link phrases, and generated summaries. The abstraction is therefore exercised by several instance classes, not adopted defensively.
- **"Resolution."** This is defined narrowly as the scope and detail a view exposes. The definition explicitly forbids reading it as an intrinsic abstraction rank of an artifact. The abstract term therefore rules something out instead of merely widening coverage.
- **"Knowledge base."** This is the KB's ordinary domain term and not an altitude raise over a narrower argued case.

Abstraction is concentrated in the definition and the criterion, where the argument needs it. The mechanisms section speaks in concrete Commonplace terms. There is no distributed, non-load-bearing abstraction.
