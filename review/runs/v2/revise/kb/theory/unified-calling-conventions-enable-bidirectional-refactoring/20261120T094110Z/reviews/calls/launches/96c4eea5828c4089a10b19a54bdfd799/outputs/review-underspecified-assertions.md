---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "if neural and symbolic components present the same interface, callers don't need to know which they're talking to"
    reason: "Unresolved choice: the scope of 'the same interface'. Reading A: the same name plus the same argument and return schema, and the same description shown to the LLM caller. Reading B: the same name and the same invocation mechanism (one namespace, callable as a function), while signatures and descriptions may differ between the agent and its replacement. Under A the claim that call sites and invoking prompts do not change holds by construction, but it requires every codification step to preserve the schema. Under B the claim is false whenever codification changes arguments or descriptions. The choice changes when the central claim is true and which evidence would support it. Nearby text ('The LLM sees both as callable functions', 'implementation-agnostic interfaces') does not settle it."
    level: warn
  - scope: passage
    quotes:
      - "refactoring across the boundary becomes a local operation"
    reason: "'Local' could mean that only the component's definition file changes, or that the change is confined to one link of the call chain, though tests, observability and callers' expectations about behavior may still change. The later 'call site doesn't change' points toward the first reading, so the ambiguity is probably not material."
    level: info
outcome: warn
---

# Review

The load-bearing assertion is the opening mechanism: a shared interface means callers need not know whether a component is neural or symbolic. Everything downstream depends on what counts as "the same interface": the four-step progression with unchanged call sites, the routing-rule test run, and "each link can be independently refactored".

For an LLM caller, the interface plausibly includes the tool description and argument schema that the model sees. The note never says whether those must stay fixed when an agent is replaced by a function. The two readings differ in the conditions under which the claim holds, and in whether interface-changing codifications count as counterexamples.

The routing-rule example does pin part of the interface ("receive the same set of queue labels"), which shows the author has the stricter reading in mind for outputs. The general statement still leaves inputs and descriptions open.
