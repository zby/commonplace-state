---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This note extends that callable structure to tools."
    reason: "The typed-callables section carries the thinnest separate claim: it restates the unified-interface idea in typed-callable vocabulary and mostly serves as a connection. Its llm-do detail (`.agent` files as signature plus prompt) adds a little concreteness, so it is not pure repetition, but it could fold into the mechanism section without loss."
    level: info
outcome: pass
---

# Review

## Summary

The note has six headed sections plus a lead. It supports them with about five distinct non-obvious claims and two justified support units, so its sections do not outnumber its substance.

Distinct non-obvious claims:

1. A shared name, signature and description gives information hiding across the prompt–code boundary, so implementations swap without caller edits (lead).
2. Unlike code-to-code hiding, the abstraction leaks asymmetrically. Prompt-to-code exposes loose LLM callers, while code-to-prompt exposes the cost, latency and error assumptions of code callers (What the interface hides and what leaks).
3. Practical consequence: enforce schemas at the boundary before codification, and write call sites that may revert to prompts for fallible, higher-latency calls (same section).
4. Without a unified interface, codification is a breaking change that probably pushes teams toward big-bang rewrites. The note marks this as an expectation (Why this matters for constraining).
5. The three moves differ: refactoring by codification, prototyping in a prompt, and relaxing. Only the first preserves behavior, yet all three stay local to the binding (same section).

Support units that need separate treatment:

- **The mechanism** grounds the abstract claim in a concrete runtime binding. It also states that the programmer chooses the implementation per run rather than per call, which is a boundary condition.
- **Scope** carries three boundary conditions: call invariance is not behavioral invariance, adapters are needed for structural changes, and call sites need headroom.

The typed-callables section is the only one close to restating framing (see the finding). Open Questions is a conventional tail, not a restating section. The ratio passes.
