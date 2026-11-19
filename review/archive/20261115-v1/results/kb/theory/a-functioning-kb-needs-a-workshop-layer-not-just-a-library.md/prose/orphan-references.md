---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 2192c47eae532ed5dbeef66660ce6bbd0d0047ce4dde2f533c794ae2ecf9f4ec
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: ea883dc135d1456ea9d4016fdbc15e6a
completed-at: '2026-11-12T08:23:53Z'
---
### Summary

The conceptual distinction and proposed mechanisms are legible without empirical citations. Several concrete claims about the KB’s existing workflows lack a source or observation context that would let a reader evaluate them.

### Findings

- WARN: “Current state of the gap” asserts that tasks are the only workshop-like subsystem and lists specific integration absences, including no validation, connection awareness, or backlink tracking and search as the only integration. No linked operational reference or dated inspection supports this inventory. The linked “Why directories despite their costs” supports task lifecycle subdirectories, but does not establish this complete set of integration claims. These assertions supply the concrete premise for the proposed design work.
- WARN: “Temporal document types beyond tasks” presents “Session logs … Currently not captured at all,” invisible decision discussions, informal source queuing, and existing recurring tasks as observed local facts without identifying the workflow, records, or observation period. The illustrative future stages are clearly marked; these current-state assertions need similar scope or supporting references.

### Suggested Revision

Link the operational records or documentation supporting the current-state inventory and state when and where it was observed. Where evidence is unavailable, recast the unsupported absence claims as capabilities to investigate or proposed workflow requirements, rather than established facts about the KB.

## Result: WARN
