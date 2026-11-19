# Premise decomposition: Human analogies can motivate functions without determining component boundaries

**Note:** kb/notes/human-analogies-suggest-functions-not-component-boundaries.md
**Register:** claim
**Central commitment (one sentence):** A human-cognition analogy can suggest a function or failure mode for an agent, but resemblance alone does not warrant inheriting the human component boundary; the target's dependencies and allocation tradeoffs must supply that warrant.

## Premises and counterexamples

1. **At least some functions or failure modes can be specified independently of the human implementation that exhibits them.** — HOLDS — Embodied and jointly adapted capacities were the strongest apparent counterexamples, but the premise is existential: preserving user-specific intent across requests can be specified without requiring the human mechanism that realizes it.
2. **The fact that several functions appear unified in one human does not by itself show that they form one indivisible causal component.** — HOLDS — A human can experience remembering and interpreting as one act, yet that person-level unity does not establish that storage, activation, interpretation, and action share one architectural boundary even within the human source.
3. **At least one function suggested by a human analogy can be realized by more than one engineered allocation.** — HOLDS — Personalization is a concrete witness: retained intent can enter live context from an artifact, be activated by a context engine, or be learned into model weights, with different components carrying the responsible roles.
4. **Different allocations can produce behavior similar enough that behavior alone does not identify which allocation produced it.** — HOLDS — Internal instrumentation or controlled interventions can distinguish allocations, but those add evidence beyond behavior; an output-only observer need not be able to tell whether personalization came from context or weights.
5. **Allocations that preserve the same function can differ materially in provenance, correction cost, portability, attribution, latency, interface cost, or coordination burden.** — HOLDS — Artifact-backed and weight-backed personalization already witness several such differences; the hunt found no requirement that functionally adequate allocations have identical engineering consequences.
6. **A component boundary inherited from a human source constrains the target only when the target shares the causal dependencies that make the human bundling useful.** — DEFEATED — Consider an agent whose operator-facing “memory” must be one inspectable and correctable component because its audit protocol is deliberately organized around that familiar human category: the human-derived boundary constrains the exposed architecture even though the agent's storage, activation, and learning mechanisms do not share the causal dependencies that make human memory bundled. — LOCAL — instance
7. **Restating a surviving function as required behavior and dependencies permits candidate allocations to be compared without presupposing the human boundary.** — HOLDS — A function whose identity includes a particular coupling looked like a counterexample, but then that coupling is a dependency the restatement must preserve, not a boundary licensed by resemblance alone.
8. **Neither coupling nor separation is generally superior independently of the target's constraints.** — HOLDS — Coupling can preserve shared representations and reduce interface cost, while separation can improve provenance and replaceability; each has concrete failure cases, and the hunt found no architecture-independent ordering between them.

## For the human

Look first at premise 6: its shared-causal-dependency exclusivity omits target-side interface or audit constraints that can independently warrant a human-derived exposed boundary.
