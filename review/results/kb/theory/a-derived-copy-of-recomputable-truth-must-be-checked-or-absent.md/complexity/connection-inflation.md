---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 3b670c1b79434ce5b130a3f35ab8a0ea
completed-at: '2026-11-16T22:18:30Z'
findings:
- scope: passage
  quotes:
  - adds recomputable-and-checked as a third class between arbitrary and situational
    on its fix-or-leave axis
  reason: The body's 'What enforcement buys' section already links this note and states
    the same third-class relationship almost word for word. The footer adds only the
    `extends` label, which the gate treats as enough to avoid inflation, so this is
    near-restatement rather than a failure.
  level: info
- scope: passage
  quotes:
  - mark is the shipped, validator-enforced instance of the rule; the mark contract
    lives here
  reason: Instance 1 in the body already presents the `complete` mark as the enforced,
    shipped instance and says the mark contract is in this type spec. The footer repeats
    that framing and adds only the `evidenced-by` label.
  level: info
- scope: passage
  quotes:
  - duplication cited as the fourth instance
  reason: Instance 4 in the body already cites ADR 027 as the design of the byte-identical
    two-copy layout. The footer restates that and adds only the `evidenced-by` label.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/37e9975a2da1ff66c6f376f1/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/37e9975a2da1ff66c6f376f1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/3b670c1b79434ce5b130a3f35ab8a0ea/outputs/review-connection-inflation.md
raw-output-sha256: 636e0c36a34ed7b3aef6de3ecd05e2a6885138594e34a004fd5309cb9b867f43
---

# Review

## Summary

There are thirteen Relevant Notes entries. Five are not linked from the body (boundary of automation, LLM recompute cost, history has one chance to become checkable, enforced tag-README, local materialization), so they add navigation the body does not provide.

The others are also inline links, but most of their footer entries add framing the inline use lacks. The frontloading entry adds "validity window". The keep-compiled-views entry states the generalization direction. The lineage entry identifies this note as a specialization of the managed-staleness rule. The make-like entry attaches the detection/verification collapse to its source note. The text-testing entry names the Level A/B gradient as the boundary marker. The indexes entry recasts the body's "sharpest case of" as a grounding relation.

Three entries come closest to inflation: fix-what-the-executor-can't-determine, the tag-readme type spec and ADR 027. In each, the body already states the relationship and the footer mostly repeats it. All three still add a typed relation, which the gate's second question counts as navigational value. They are recorded as info, not as failures.
