---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The type spec asks notes to state the claim's limits under a `## Scope` heading (assumptions, applicability conditions, known failure cases) and to omit it only when no limit is known. The note has no Scope section, yet its own text shows known limits. The claim that call sites 'don't change' holds only when the neural and symbolic implementations accept the same arguments and return the same output set; the prompt-switching example has to stipulate this ('receive the same set of queue labels'). The claim also depends on name-based dispatch in a shared namespace. Its evidence is one system, llm-do. Neural and symbolic callees can also differ in determinism, latency, cost and failure modes, which callers may depend on even when the signature is unchanged. These conditions are stated inline or not at all, so a rescoping edit would have to rewrite the claim."
    level: warn
outcome: warn
---

# Review

The note mostly meets the `note` type's authoring instructions. The title is a compressed handle for the claim. The opening paragraph states the main claim, that a unified calling convention makes the neural–symbolic boundary movable, and the mechanism comes next. The note links inline and in its footer to adjacent notes on constraining, codification, spec-mining and typed callables, and each link says how that note relates. Its content is design rationale. The numbered progression illustrates the mechanism and is not an imperative procedure, so it belongs in a note and not in instructions. The Open Questions section matches the template.

One instruction goes unmet. The note has no `## Scope` section, even though known limits exist, and the note itself shows some of them. Moving a component between neural and symbolic leaves call sites unchanged only when the two implementations share an input/output contract. The claim also relies on name-based dispatch, and its only evidence is llm-do. The Open Questions already raise scale and debugging. A Scope section is where the note should state the conditions under which the claim holds. That would let a later rescoping edit narrow the claim without rewriting the mechanism section.
