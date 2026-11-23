---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/dc57433e7e052c539929a07e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:58Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-proportion-mismatch.md
raw-output-sha256: 5086cc230489605867b1f50d35a2ac69191057e041492a39cd559ffb51f3bc86
format: 2
---

# Review

## Summary

The note's core claim has two parts:

1. A unified interface lets a programmer swap prompts and code without editing
   callers. This is the title claim.
2. The swap leaks asymmetrically in the two directions. This is the description
   and the opening thesis.

Each part gets substantive development. "What the interface hides and what
leaks" develops the asymmetry with a mechanism for each direction and a
practical consequence. "Why this matters for constraining" is the longest
section. It develops the title claim through a worked example of three moves,
which also separates refactoring from prototyping and relaxing. That example
supports the load-bearing claim directly, so it is not secondary material.

"The mechanism", "Scope" and "The connection to typed callables" are short
supporting sections, sized to match their role. No secondary section outgrows
the core, and nothing needs to be split into its own note.
