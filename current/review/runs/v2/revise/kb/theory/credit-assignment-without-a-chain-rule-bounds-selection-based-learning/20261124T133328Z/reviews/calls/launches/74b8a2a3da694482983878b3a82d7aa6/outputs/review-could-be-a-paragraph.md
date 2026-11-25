---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

A one-paragraph rewrite would keep the headline: credit assignment without a chain rule is a debugging problem. It would lose material the test counts as load-bearing:

- the inference that interdependence grows with store size, framed as the backward inverse of the validation radius;
- the three specific reasons prose-and-code stores are harder to debug than software, each tied to a distinct debugging tool (stack traces, declared dependencies, clean reproduction);
- the failure conditions of three naive workarounds;
- the separate debuggability levers, which split cheap suspect narrowing from targeted causal checks;
- the boundary cases in `## Scope`: flat independent lookup tables avoid the problem, and the note excludes model-internal attribution.

The note is already compact, and its structure is light: one body, a scope list and open questions. It carries more than one simple insight, so the multi-part structure is justified.
