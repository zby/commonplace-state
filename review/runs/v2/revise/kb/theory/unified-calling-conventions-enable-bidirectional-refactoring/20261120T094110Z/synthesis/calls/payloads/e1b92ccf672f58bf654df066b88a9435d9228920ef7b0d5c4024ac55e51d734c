---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL."]
    reason: "The scheduler section opens a second argument, imperative orchestration versus graph DSLs such as LangGraph and CrewAI. Its four-row table gives that argument about as much space as the mechanism section. Only the Refactoring row and the closing sentence bear on the calling-convention claim, and the closing sentence repeats that row. The State and Control flow rows and the named-framework contrast add unsourced comparative claims. A reader's attention moves away from stable call sites. Direction: reduce the section to one sentence saying that cross-boundary moves use ordinary extract/inline/rename refactorings. Fold that sentence into 'Why this matters for constraining' or the mechanism section, and rehome or drop the framework comparison together with the Python-specificity open question."
  - scope: passage
    quotes: ["Add an LLM call for the new cases. Again, the call site doesn't change.", "A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement."]
    reason: "The title promises 'bidirectional' refactoring, but the numbered progression mostly runs neural to symbolic. Step 4 adds an LLM call beside the code and does not move a codified component back into a prompt. The code-to-prompt move appears only in the inherited opening framing and in the late ticket_classifier paragraph, so a reader may remember a one-way progression. Direction: name the reverse move beside the core claim in the opening, or in the progression itself. Keep the ticket_classifier example as the concrete support for that move, after the author settles which reverse move 'bidirectional' denotes."
outcome: report
---

# Simplification synthesis: Unified calling conventions enable bidirectional refactoring between neural and symbolic

## Opportunities

### 1. Collapse the scheduler section to its one refactoring consequence

- Location: "The scheduler layer", from "On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL." through "No graph topology to update.", together with the open question "Is the imperative scheduler pattern specific to Python, or does it transfer to other host languages?"
- Combines: branch-bloat (scheduler branch, warn); core-claim-obscured (scheduler competes for attention, info); detail-overhang (table overhang, warn); marginal-value-redundancy (closing sentence repeats the Refactoring row, warn; State and Control flow rows, info). Four checks independently reached the same section, so this is one fold rather than several local cuts.
- Preserve or decide: Keep the inference that matters to the claim: because orchestration is ordinary code, moving a component across the boundary uses ordinary extract, inline and rename refactorings. The author must decide whether the comparison with graph DSLs, including the State and Control flow axes and the named LangGraph/CrewAI contrast, is dropped or moved to an llm-do system review or to the abstracted persistence-boundary note. The Python-specificity open question should follow that decision. One possible resolution, offered only as an illustration, is: "Because llm-do's scheduler is plain Python rather than a graph DSL, moving a component across the boundary uses the same extract, inline and rename refactorings as ordinary code."

### 2. Surface the reverse direction the title promises

- Location: opening paragraph; "Why this matters for constraining", step 4 ("Add an LLM call for the new cases. Again, the call site doesn't change.") and the following paragraph ("A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement.")
- Combines: core-claim-obscured (the reverse direction is underweighted, info). Constrained by detail-overhang's non-obvious pass and marginal-value-redundancy's observation that the ticket_classifier paragraph is load-bearing and not redundant with step 4.
- Preserve or decide: The note presents two materially different reverse moves. Step 4 adds neural handling beside retained code for new requirements. The ticket_classifier paragraph replaces code with a prompt under the same name, possibly only temporarily for exploration before the chosen rule returns to code. Before "bidirectional" is surfaced in the opening or the list, the author must decide whether it means one of these moves or both. That choice determines whether step 4 is renamed or recast and whether the exploration case is presented as the main relaxing example. This synthesis does not choose. In either case, preserve the ticket_classifier paragraph's length and its claim that a temporary prompt can serve its purpose even if the rule returns to code.
