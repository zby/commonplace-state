---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/fbb82f81e60fbd3db85aa079/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:57Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-mannered-prose.md
raw-output-sha256: f43b4ae36f240dd83066df8fcfe19dcb61ea85ad2082720bcf3aca194548fc99
format: 2
---

# Review

## Summary

The note's figurative phrases are conventional technical shorthand, and each
says something specific:

- "Leaks asymmetrically" draws on the recognised leaky-abstraction pattern. The
  note then spells out the mapping: what the interface cannot hide in each swap
  direction.
- "Big-bang rewrites" is a standard software-engineering term for wholesale
  replacement, and it contrasts with incremental refactoring.
- "Call-site headroom" is conventional engineering usage. The bullet defines it
  at once as latency budget, cost budget and error handling.
- "Brittle proxy theory" and "hidden coupling" are literal enough in this
  context, and the note uses both connotations.

No phrase passes the gate's test. In each case the literal version would be no
clearer, and the figure adds no connotation the note leaves unsupported.
