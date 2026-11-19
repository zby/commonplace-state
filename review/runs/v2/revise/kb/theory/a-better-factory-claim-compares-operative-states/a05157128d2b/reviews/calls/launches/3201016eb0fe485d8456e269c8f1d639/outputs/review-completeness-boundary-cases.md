---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "is the state that is installed and that later production and factory development depend on"
    reason: "A partial or staged rollout (a canary installed for a fraction of production, or a successor installed on some family members but not others) sits between candidate and operative successor. The stated criterion — installed and depended on — can classify it, but only by choosing a measurement boundary the note mentions solely for continuously revised systems. Coverage is possible but strained."
    level: info
  - scope: passage
    quotes:
      - "is the factory state current when the comparison is declared"
    reason: "The simplest instance, the first installation of a factory, has no predecessor state with prior capabilities. The framework appears to exclude it from better-factory claims, which is reasonable, but the note does not say so. Non-regression would then be vacuous rather than inapplicable."
    level: info
outcome: pass
---

# Review

The note builds three small frameworks: a three-term vocabulary for the comparison's endpoints (predecessor, candidate, operative successor); a two-component assessment relation (non-regression plus a declared improvement); and a three-case contrast (retention without improvement, improvement without learning, learning).

Boundary cases tested:

- **Continuously revised system.** This case is handled explicitly: the successor is the operative state at a named measurement boundary.
- **Installed then rolled back.** The linked operative-change definition counts a change as operative while it holds. The successor at the measurement boundary maps cleanly.
- **Deliberate retirement of capability.** Non-regression would fail this case. The Scope section handles it explicitly as an alternative declarable relation.
- **Improvement solely in cost or latency.** This maps to "at least one named production dimension".
- **Change that improves only against a different objective.** The note handles this explicitly: it need not pass the declared comparison.
- **Experience-derived change bundled with other changes.** The learning case defers to the experimental-contrast requirement, which covers this.
- **Staged or partial rollout, and first-ever factory.** Each maps only with strain; recorded as INFO.

The three-case contrast is not meant to be exhaustive. It separates three claims, and its length fits that role. No case clearly falls outside the claimed coverage.
