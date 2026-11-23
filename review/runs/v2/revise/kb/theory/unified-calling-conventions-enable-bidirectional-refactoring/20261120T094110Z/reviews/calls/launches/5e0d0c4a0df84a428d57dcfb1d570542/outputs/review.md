---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL. This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs."
      - "| State | Global context through graph | Local scope — each agent gets only its arguments |"
      - "| Control flow | DSL constructs | Native Python: `if`, `for`, `try/except` |"
    reason: "The scheduler section is a branch about a second architectural choice: imperative orchestration versus graph DSLs. The main claim concerns the calling convention: same interface, name-based dispatch and unchanged call sites. Only the closing point, that cross-boundary refactoring reuses ordinary extract/inline/rename moves, bears on that claim. The State and Control flow rows and the LangGraph/CrewAI contrast add unsourced comparative claims about other frameworks. Those claims widen the attack surface without supporting the call-site argument. Reduce the section to one sentence on refactoring moves, and move the framework comparison to an llm-do system review or the abstracted persistence-boundary note. The open question on whether the scheduler is Python-specific should move with it."
    level: warn
outcome: warn
---

# Review

**Main claim.** When neural and symbolic components share a calling convention, components can move across the boundary without changing call sites, so refactoring is local in both directions. llm-do's name-based dispatch over a hybrid VM serves as the demonstration.

**Material that supports the claim in its current place.**
- The mechanism section and the dispatch-chain diagram supply the premise.
- The four-step progression shows the codifying direction.
- The paragraph on switching `ticket_classifier` back to a prompt shows the relaxing direction, which the title's "bidirectional" commits the note to. It is long, but it supports the claim.
- The typed-callables section is compact. It ends by tying the calling convention to the claim ("makes the type-theoretic view practical"), so it supports the claim as context.
- The namespace-scale and debugging open questions are already in the right place for open questions.

**Branch that needs action.** "The scheduler layer" section compares orchestration styles (graph DSLs vs. an imperative scheduler) across four dimensions. Only one dimension, refactoring, connects to the main claim, and the section's last sentence already makes that point. The comparison of state handling and control flow, and the named contrast with LangGraph and CrewAI, are a separate claim about llm-do's design. That claim needs its own evidence, and here it draws attention away from the call-site mechanism. Keep a single sentence noting that cross-boundary refactoring uses ordinary code-refactoring moves. Rehome the comparison, together with the related Python-specificity open question.
