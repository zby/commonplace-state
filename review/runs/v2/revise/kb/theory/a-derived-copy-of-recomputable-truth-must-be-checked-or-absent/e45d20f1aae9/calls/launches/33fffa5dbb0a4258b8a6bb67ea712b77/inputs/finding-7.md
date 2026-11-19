---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 72a0ce93e4214465b4d1d2779c80a3c5
completed-at: '2026-11-16T22:18:58Z'
findings:
- scope: passage
  quotes:
  - the rule rides entirely on that
  reason: 'Literal meaning: the rule depends entirely on this asymmetry. "Rides on"
    adds no precision or mapping that the note later uses, and the reader has to translate
    the idiom. Replacement: "and the rule depends entirely on that asymmetry" removes
    the translation step without losing anything.'
  level: warn
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/47d562dae83a2c68be3c9311/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/47d562dae83a2c68be3c9311/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-mannered-prose.md
raw-output-sha256: 0d90209c8796df544ef9c11dd0e2c6f5673f0869c8afb9134b0390bbcb5bd3ed
---

# Review

Most figurative wording in the note does useful work. "Collapse into one free step" (detection and verification) and "the interrupt-placement problem dissolves" are conventional, and the following clauses state their literal mechanism. "The forbidden state, just relocated one layer down, with a stronger trust signal attached" sharpens the regress argument in precondition 4. "A machine watches the situation on the author's behalf" is immediately made literal as "converting staleness into a validation failure at check time". "Degrade gracefully" is standard engineering vocabulary, and the same bullet defines it. "One missed edit away from the catastrophic state" has a strong connotation of scale. The preceding paragraph's "silent, unbounded wrongness" supports that connotation, so it is not flagged.

One local idiom, "the rule rides entirely on that", contributes nothing that the literal "depends entirely on" lacks, so the gate returns WARN for a single instance. The pattern is not pervasive.
