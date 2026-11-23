---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "That is the same property [one case-level conjecture offers as the diagnosis of a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md)"
    reason: "The note's property is whether an extracted regularity is genuinely part of the spec rather than an accidental pattern on observed data, which is a fact about the regularity. The target's property is earned versus asserted reach: whether a claim's scope was tested against cases that could refute it rather than inferred from fit. A genuinely load-bearing regularity committed without a refuting test still has asserted reach in the target's sense, so the two properties are not the same. The next clause ('asserts a scope that nothing assessed') does use the target's concept, but the identity is stated for the truth property. Identify the assessed-scope property, or say the accident case is one way to have unearned reach."
    level: warn
  - scope: passage
    quotes:
      - "reveal when a codified component encodes an accident rather than a spec"
    reason: "The target says its signals 'shift confidence', 'aren't binary tests', and detect badly-fitting theories 'not the theory/spec distinction itself', since a component can pass the early signals and still encode a proxy theory. 'Reveal' attributes a decisiveness the target disclaims. The accident/spec framing is close to the target's badly-fitting-theory concept, so the core attribution holds."
    level: info
outcome: warn
---

# Review

Identity claims checked against their targets:

- Fixed-artifact distinction (exact specs versus proxy theories) → `exact-implementation-does-not-validate-a-requirement.md`. The target distinguishes locally exact requirements from requirements that are conjectured proxies for an objective; the note's parentheticals match. Holds.
- Codification as moving a rule into symbolic form by rewriting or adopting a reference → `definitions/codification.md`. Matches the definition, including adoption of a model package. Holds.
- Code extraction trading generality for reliability, speed and cost → `constraining-and-extraction-both-trade-generality-for-reliability.md`. Matches. Holds.
- "The same property" as the bitter-lesson note's diagnosis → `bitter-lesson-selects-against-unearned-reach-not-against-structure.md`. Substantive mismatch between truth of a regularity and tested status of its scope (warn).
- Spec mining as extraction from a working system → `spec-mining-as-codification.md`. Matches the target's pattern. Holds.
- Relaxing signals as detecting accidents → `operational-signals-that-a-component-is-a-relaxing-candidate.md`. Concept matches; strength overstated (info).

The epiplexity and induction-bias attributions point to external papers that were not available within the reading scope, so they were not checked.
