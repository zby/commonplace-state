---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - that is why hand-maintained-and-trusted is *forbidden* rather than merely risky
  reason: The asymmetry alone (bounded versus unbounded downside) compares worst cases,
    not expected costs, so by itself it supports 'risky' as much as 'forbidden'. The
    prohibition becomes hard to vary only when combined with the later premise that
    a Level A check costs nearly nothing, so trusting an unchecked copy saves nothing.
    The note supplies both premises, but attributes the forbidding force to the asymmetry
    section. The mechanism is present but slightly mislocated.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d9cf4e57c86e8ccaf443d7c2/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d9cf4e57c86e8ccaf443d7c2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-explanatory-reach.md
raw-output-sha256: 1b5548e39cbc66bffd20a363abd21187eabf1d26312059d0e0e89b1909674122
format: 2
---

# Review

The central claim has a constrained mechanism. Two premises carry it: (1) a false trusted copy suppresses the recomputation that would expose it, while an absent copy costs only a bounded recomputation; (2) where derivation is mechanical, verification drops to a deterministic, near-free check.

**Variation test.** Vary premise 2: if checking were judgment-priced (Level B), the conclusion changes, and the note itself says so. In that regime hand-maintained dependent artifacts are "unavoidable", and managed staleness governs. Vary premise 1: if a stale copy carried a signal, or did not suppress recomputation, the prohibition loses its ground. The conclusion therefore depends on the premises; it is not adaptive pattern-recording.

**Falsifiability.** The claim would be undercut by a domain where a mechanically recomputable copy cannot be cheaply checked, or where an unchecked trusted copy's expected cost is lower than both checking and omission. Preconditions 1–4 name where enforcement fails and route those cases out explicitly.

**Ad-hoc accommodation.** Precondition 4's clause, which treats a judgment-based derivation rule as "the forbidden state, just relocated", tightens the claim rather than shielding it. Precondition 3's exclusion of execution-produced values follows from the definition of recomputability, not from a counterexample patch.

Only one thin spot remains, recorded as INFO.
