---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A bounded, recoverable downside on one side; a silent, unbounded one on the other
  reason: '''Unbounded'' carries the step from ''risky'' to ''forbidden'' but leaves
    its dimension unresolved. Reading A is duration: with no signal, the wrongness
    persists until something else exposes it. Reading B is magnitude: the harm a false
    copy can cause has no ceiling. Under A the claim holds for every unchecked trusted
    copy, but the expected harm can still be small, so the inference to ''forbidden''
    needs the later free-check premise. Under B the claim is false for many low-stakes
    copies but would license prohibition on worst-case grounds alone. The truth conditions
    and the inference that follows both change.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/e16c4936f395085b24c5cbc3/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/e16c4936f395085b24c5cbc3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-underspecified-assertions.md
raw-output-sha256: c04cde6f0f4f0109ca19955c70857752b804ae0d66eb508adc204dadce8626d6
format: 2
---

# Review

Most load-bearing assertions are exact. "Checked" is defined operationally: a validator re-derives the copy and fails on mismatch. "Absent" is defined as deleted or replaced by a live read. The regime boundary is fixed by Level A versus Level B check cost. Each precondition names its criterion. Enforcement "would dominate" is resolved immediately into "recovering the context economy without the drift".

The one unresolved choice is the asymmetry's key word. The section's stated purpose is to explain why the hand-maintained state is "*forbidden* rather than merely risky". It rests that on the downside being "unbounded". Nearby context ("with no signal that anything is wrong") points toward duration, but "catastrophic" in the next sentence points toward magnitude. The two readings call for different support and justify prohibition by different routes.
