---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The asymmetric-leak claims are supported by derivation from stated regime differences and by a constructed `ticket_classifier` scenario introduced with 'Suppose'. The note reports no observed swap, in llm-do or elsewhere, that exhibits either leak. The derivation covers the class it claims, so this is not a scope overreach. A reader should still note that the claimed failure behaviors are derived, not exercised."
    level: info
outcome: pass
---

# Review

## Summary

**Claimed scope.** In any system where prompt-backed agents and code share one interface, a programmer can rebind an operation without editing callers. The leaks differ by swap direction.

**Support presented.**

- A derivation from information hiding: a shared binding hides the implementation from call sites.
- A derivation from regime differences: prompt tolerance versus code strictness, and the latency, cost and fallibility of model calls versus functions.
- One described instance, llm-do.
- A constructed example.

**Exercised domain.** The derivation's premises hold for any system with a shared prompt–code binding, which matches the claimed class. The note does not generalize from the llm-do instance; it derives the claim. The surplus is bounded explicitly. The Scope section excludes structural signature changes and call sites without latency or error headroom, and it separates call invariance from behavioral invariance. The one predictive extension, that separate surfaces push toward big-bang rewrites, is marked as "an expectation, not an observed result". Scaling to hundreds of components and observability are left in Open Questions.

The claimed scope matches the support. The INFO finding records that the leak behaviors are derived and not observed.
