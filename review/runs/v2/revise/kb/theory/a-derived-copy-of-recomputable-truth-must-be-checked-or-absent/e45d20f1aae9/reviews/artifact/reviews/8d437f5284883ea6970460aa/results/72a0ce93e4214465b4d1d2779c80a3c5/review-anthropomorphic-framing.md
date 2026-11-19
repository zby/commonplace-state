---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - a plan's executor learns things no validator could pre-check
  reason: '"Learns" applied to an executor (possibly a model) could read as a cognition
    claim, but the sentence only means the run produces information unavailable before
    execution; this is conventional shorthand and the note defends no internal-state
    claim. A literal alternative would be "a plan''s execution produces information
    no validator could pre-check".'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/8d437f5284883ea6970460aa/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/8d437f5284883ea6970460aa/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 72a0ce93e4214465b4d1d2779c80a3c5
completed-at: '2026-11-16T22:18:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-anthropomorphic-framing.md
raw-output-sha256: ba8c17d4406ed235a763f06e23dc50d8141c9d2ecb722b52f22de972f6caf5fb
format: 2
---

# Review

The note's subjects are mostly artifacts, validators and consumers, and its agentive verbs are conventional metonymy for software or for principles: "Frontloading ... wants a recomputable value inlined", "a machine watches the situation on the author's behalf", "a machine can follow it". These are standard technical shorthand, and none makes a literal claim about system cognition.

The only verb that names a mental process is "learns", applied to a plan's executor in precondition 3. Read in context, it means that execution generates evidence that does not exist at validation time. It makes no claim about model internals. It is recorded as INFO, and the gate passes.
