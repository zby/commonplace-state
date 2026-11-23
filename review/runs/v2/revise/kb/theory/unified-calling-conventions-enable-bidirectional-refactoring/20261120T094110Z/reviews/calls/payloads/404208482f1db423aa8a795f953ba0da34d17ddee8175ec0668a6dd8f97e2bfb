---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs."
      - "Local scope — each agent gets only its arguments"
      - "Native Python: `if`, `for`, `try/except`"
    reason: "The scheduler section's job in the note's argument is one inference step: because llm-do orchestration is ordinary imperative code, moving a component across the neural-symbolic boundary uses ordinary refactorings (extract function, inline, rename). The closing sentence of the section already states this. The four-row comparison table with graph DSLs elaborates beyond that role: the State and Control flow rows describe general advantages of imperative orchestration that do not bear on calling-convention uniformity or boundary movement, and only the Refactoring row supports the claim. Compress the section to two or three sentences that name the contrast with graph DSLs and keep the refactoring consequence, dropping the table or reducing it to the Refactoring row."
    level: warn
outcome: warn
---

# Review

## Summary

Most detail in the note is proportional to its role. One passage outgrows it: the scheduler-layer comparison table.

The note claims that a unified calling convention makes the neural-symbolic boundary movable, so refactoring across it becomes a local operation. The supporting route has three parts. Name-based dispatch is the mechanism. The four-step progression shows codification and relaxing without call-site changes. The typed-callables section ties the claim to the callable view.

The scheduler section adds one inference step: imperative orchestration lets boundary moves use ordinary code refactorings. Its final sentence states that step on its own. The table before it compares graph DSLs and llm-do on four axes. Two of those axes, state scoping and control-flow constructs, make a broader case for imperative orchestration that this note does not need. That is the overhang flagged above.

## Non-obvious passes

- **Prompt-testing paragraph (`ticket_classifier` routing).** The paragraph is a six-sentence worked example, but it is the note's main concrete support for the reverse direction that "bidirectional" in the title promises. It shows that moving code back to a prompt for exploration is cheap when the name and output labels stay fixed. Cutting it to a phrase would leave relaxing as an abstract assertion, so its length is justified.
- **Name-based dispatch paragraph.** It lists three properties of name-based dispatch. Late binding is not strictly needed for the claim, but the list is one sentence long and explains why names, rather than object references, make the interface implementation-agnostic. It does not need compression.
- **Four-step progression.** Each step carries part of the codify-then-relax cycle, and the repeated statement "the call site doesn't change" is the evidence for the claim, not padding.
