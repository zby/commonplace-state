---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
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
  - Checked copies degrade gracefully.
  - Never write the unenforced natural-language version of a checkable claim.
  reason: 'Two of the three Consequences bullets largely restate earlier material:
    graceful degradation restates the asymmetry section''s bounded-cost side, and
    the ban on unenforced natural-language claims restates the opening rule. The third
    bullet (omission as fallback, with the ADR 025 and skill-edit evidence) adds substance,
    so the section is thin rather than redundant.'
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/1579a9f26a5254e5ba2066b9/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/1579a9f26a5254e5ba2066b9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/3b670c1b79434ce5b130a3f35ab8a0ea/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 0d575dccecf027d28f8635b5e2fb188f3beefdd70385e0ea80ebd3f4e3a34254
---

# Review

## Summary

The note has seven body sections (opening, asymmetry, regime boundary, what enforcement buys, preconditions, consequences, instances) plus Open Questions. It carries roughly as many distinct non-obvious claims or necessary support units:

1. The checked-or-absent rule itself (opening).
2. The asymmetry between bounded recomputation and silent unbounded wrongness, which justifies "forbidden" rather than "risky".
3. The regime boundary: managed staleness applies where verification is judgment (Level B), and enforce-or-omit applies where mechanical derivation makes the check Level A.
4. Recomputable-and-checked as a third class that reconciles frontloading with fix-what-the-executor-can't-determine.
5. Four preconditions for enforcement, including the argument that the validator bottoms out rather than recursing. These are boundary conditions the argument needs.
6. Consequences, including omission as a fallback rather than the optimum.
7. Instances across four surfaces, offered as evidence that the rule generalizes.

Each section adds a claim, a boundary condition or evidence. The only partial restatement is in Consequences, where two bullets mostly repeat earlier points; this does not make sections outnumber claims.
