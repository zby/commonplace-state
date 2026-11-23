---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A prompt-backed callee often absorbs loosely phrased, slightly malformed, or context-dependent
    arguments by inferring intent.
  reason: '''Often'' is a frequency claim about prompt-backed callees. Neither llm-do
    use nor a cited source supports it. The leak mechanism that follows is a derivation
    from the strict-versus-tolerant contrast and reads acceptably as one, but this
    empirical-sounding premise uses the same declarative register as the derivation.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 8f05aba89d28e81694031337bcbcbd44c8acc31a62a36cfac4e644310ab78a73
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/3f1d736ad63bc277d83d8e11/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-epistemic-status-blur.md
raw-output-sha256: 59b75bed82298fc378f8d01c863a0fca338a8fbdee498f471d2f8a63cc4713d1
format: 2
---

# Review

## Summary

The material claims and their presented statuses are as follows:

- **llm-do description:** a report about an external system, presented as such.
- **Information hiding across the boundary:** a derivation from the shared interface, presented as a mechanism.
- **The asymmetric leaks:** consequences derived from stated differences between regimes. Strict code rejects input that a prompt tolerated, and a signature omits latency, cost and failure mode. They read as derivations, which matches their support. The one empirical-sounding premise, that prompt-backed callees "often" absorb loose arguments, carries no evidence (INFO).
- **Friction discouraging incremental refactoring:** explicitly marked as "an expectation, not an observed result". The status is clearly calibrated.
- **The three ticket moves:** introduced with "Suppose", so they read as a constructed illustration, not as observation.
- **Open Questions:** unresolved items are kept separate from the claims.

The note marks its one predictive claim explicitly, and no proposed mechanism inherits confidence from evidence. The statuses can be recovered from the text.
