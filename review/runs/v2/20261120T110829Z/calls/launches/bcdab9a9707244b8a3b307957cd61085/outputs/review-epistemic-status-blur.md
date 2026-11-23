---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A prompt-backed callee often absorbs loosely phrased, slightly malformed, or context-dependent arguments by inferring intent."
    reason: "'Often' is a frequency claim about prompt-backed callees. Neither llm-do use nor a cited source supports it. The leak mechanism that follows is a derivation from the strict-versus-tolerant contrast and reads acceptably as one, but this empirical-sounding premise uses the same declarative register as the derivation."
    level: info
outcome: pass
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
