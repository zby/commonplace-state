---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "[constraining](./definitions/constraining.md) — the mechanism that unified calling makes frictionless"
      - "[codification](./definitions/codification.md) — the phase transition from neural to symbolic that unified calling makes a local operation"
      - "[spec-mining-as-codification](./spec-mining-as-codification.md) — the operational mechanism: observe agent behavior, extract to code — enabled by stable call sites"
      - "[instructions-are-typed-callables](./instructions-are-typed-callables.md) — the type-theoretic view that llm-do operationalises"
    reason: "The collection's footer convention is `- [title](path) — label: context phrase` using the label table. These four footer entries carry only a context phrase and no label. The two definition targets fit `defined-in`; spec-mining reads as `mechanism`; typed-callables reads as `grounds` or `extends`."
    level: warn
  - scope: passage
    quotes:
      - "Abstracted into: [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md)"
    reason: "`Abstracted into:` is not a label in the collection's table, and it does not use the footer form. It is the inverse of the target's own `abstracted-from` edge. The contract allows a reciprocal link only when the reverse direction independently helps readers. It also says never to add one merely to mirror an existing edge. If a reader of this note does need the generalization, use a table label such as `extends` with a context phrase that says why."
    level: warn
  - scope: passage
    quotes:
      - "On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL."
    reason: "The scheduler section mostly describes llm-do's current construction and compares it with LangGraph and CrewAI in a table of unscoped characterizations, such as \"Global context through graph\". The contract routes descriptions of a specific system's construction to `kb/agentic-systems/`. It also requires the body to stay composable: a note citing this claim about calling conventions as a premise would inherit an unrelated second cluster about imperative versus declarative orchestration. Only the section's last sentence connects back to the thesis. Either shrink the section to that connection or split the scheduler comparison off."
    level: warn
  - scope: passage
    quotes:
      - "llm-do demonstrates this with name-based dispatch over a hybrid VM"
    reason: "llm-do is the case the claim was built from, so under the rule that origin is not corroboration it can serve as an existence witness or an illustration, not as a demonstration that the general claim holds. Wording such as \"llm-do exhibits one such convention\" would keep its role within scope. A collection gate need not block on this."
    level: info
outcome: warn
---

# Review

The placement is correct. After llm-do is scoped as the witness and the illustration, a substantive claim about the design space remains: if neural and symbolic components share one calling convention, an implementation can move across the boundary without changes at the call sites. The note explains the mechanism (name-based dispatch with late binding), and it ends with real open questions instead of defensive hedging. Both fit the collection's quality goal of explanatory reach.

Three of the collection's conventions are not met:

- **Footer labels.** Four of the footer entries have no label. One entry uses an off-table inverse label that mirrors an edge the target note already authors.
- **Body composability.** The scheduler section imports a second cluster about how llm-do and graph DSLs orchestrate work. That cluster describes particular systems more than it supports the thesis.
- **Origin used as evidence (minor).** The description calls the case the claim came from a demonstration of it.

None of these make the note misplaced, so the outcome is warn rather than fail.
