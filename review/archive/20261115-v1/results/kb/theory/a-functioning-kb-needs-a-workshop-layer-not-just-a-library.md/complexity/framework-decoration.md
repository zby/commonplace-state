---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: b9fcdcbe17cb846a6a298af1be72486d73dde16e986ecbf022df21ffd55f0731
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: c53c5614e777471f969e16cf42464f5d
completed-at: '2026-11-12T08:23:16Z'
---
### Summary

The library/workshop distinction supports the note’s design question: temporary work needs lifecycle handling and links to durable knowledge. The two bridge directions also do distinct work. However, the inventory of prospective workshop types introduces more categories than the argument uses.

### Findings

- WARN: “Temporal document types beyond tasks” gives six categories and illustrative stages without showing which differences require different design choices. Decision threads, experiments, queues, and session logs recur as bridge examples, but periodic reviews and collaborative threads add no subsequent inference or decision rule. The later preference for local subsystem conventions depends on differing lifecycles and relationships, not on this particular six-part inventory. A short paragraph could preserve that reasoning with fewer categories.
- INFO: The comparison table has a useful core: explicit transitions and completion or disposal distinguish operational requirements from durable artifact contracts. The Scope paragraph supplies hybrid boundary cases. Extraction and composition distinguish opposite information flows, support different mechanisms, and inform the minimum-bridge and skill-signature questions; these structures are load-bearing.

### Suggested Revision

Replace the six-item inventory with a short paragraph using a few examples to explain why workflows need different transitions, dependencies, or recurrence rules. Retain a separate category only when its distinctive requirement supports a later design choice. The remaining prospective workflows can be mentioned together without individual stage sequences.

## Result: WARN
