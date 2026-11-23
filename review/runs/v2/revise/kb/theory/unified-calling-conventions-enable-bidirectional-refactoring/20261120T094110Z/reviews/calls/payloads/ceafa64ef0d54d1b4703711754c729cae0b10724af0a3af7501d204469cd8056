---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Agent ──calls──▶ Tool ──calls──▶ Agent ──calls──▶ Tool ..."
    reason: "The ASCII call-chain diagram adds nothing to the sentence after it (\"The calling convention is uniform across the chain\"). Deleting it leaves clarity and precision unchanged, and it supports no prediction or derivation. It is decorative notation."
    level: warn
  - scope: passage
    quotes:
      - "Local scope — each agent gets only its arguments"
      - "Native Python: `if`, `for`, `try/except`"
    reason: "The four-row Graph DSLs vs llm-do Scheduler table introduces more categories than the argument uses. The conclusion that follows it relies only on the Refactoring row, with some support from the Orchestration row. The State row (global context vs local scope) and the Control flow row are never used again. The argument survives as one sentence: imperative orchestration makes boundary refactoring ordinary code refactoring, with no graph topology to update."
    level: warn
outcome: warn
---

# Review

The note has three structures.

- **Numbered progression (start neural → observe → codify → extend via relaxing).** This is load-bearing. It is an ordered sequence with a concrete example at each step, and it shows the call site staying stable at both the codify step and the relax step. That stability is the note's central inference. Prose would need the same steps.
- **ASCII call-chain diagram.** This is decorative. The sentence after it states the same point, and the diagram adds no categories, boundary cases or derivations.
- **Graph DSL vs scheduler table.** This is partly decorative. The Orchestration and Refactoring rows support the following conclusion. The State and Control flow rows add distinctions that no later inference, decision or prediction uses. The table could become one or two sentences, or keep only the rows the argument needs.
