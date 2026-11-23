---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring — extract function, inline, rename. No graph topology to update."
    reason: "The table's Refactoring row already says this: 'Redraw edges, update graph' versus 'Change code — extract functions, inline agents'. The closing sentence adds only the explicit link to the neural/symbolic boundary. Its last clause, 'No graph topology to update', repeats the Graph DSL cell outright. Recommend cutting the trailing clause and folding the neural/symbolic link into the sentence that introduces the table, or into the Refactoring row."
    level: warn
  - scope: passage
    quotes:
      - "Both are callables with defined interfaces."
    reason: "The previous sentence already entails this: `.agent` files are a type signature plus an implementation, and tools are typed Python functions. Deleting it costs nothing, because the next sentence makes the point that matters, unified calling makes the typed-callable view practical. Cut it."
    level: warn
  - scope: passage
    quotes:
      - "Local scope — each agent gets only its arguments"
      - "Native Python: `if`, `for`, `try/except`"
    reason: "The State and Control flow rows contrast llm-do with graph DSLs on axes that do not bear on the note's claim about movable neural/symbolic boundaries. They may be useful context about the scheduler. It is unclear whether they do reader work here or belong in a note about llm-do's orchestration style."
    level: info
  - scope: passage
    quotes:
      - "Each link can be independently refactored without disturbing the rest."
    reason: "This mostly restates the intro's 'refactoring across the boundary becomes a local operation' and the preceding paragraph's 'the prompt that invokes it doesn't change'. Its remaining job is to caption the diagram's multi-hop chain. Possibly fold it into the diagram's lead-in sentence."
    level: info
outcome: warn
---

# Review

Most of the note earns its space. The opening paragraph gives the gap and the answer once. The name-based dispatch paragraph states the requirement that makes the mechanism work. The four-step progression makes the codify/relax cycle concrete. The `ticket_classifier` paragraph adds a distinct use: switching back to a prompt for exploration while working code still exists. That case is not covered by step 4's relaxing for new requirements, so it is not redundant. The friction sentence in "Why this matters for constraining" ("pushes toward big-bang rewrites") turns the mechanism into a consequence and should stay.

The problems are local and come from recap. In the scheduler section, the paragraph after the table repeats the table's Refactoring row. The typed-callables section contains one sentence that its previous sentence already entails. Two lower-confidence items are flagged as INFO: the comparison-table rows that do not touch the note's claim, and the sentence after the diagram, which partly recaps earlier text.
