---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL."]
    reason: "The scheduler section and its four-row table set up a second contrast, imperative orchestration versus graph DSLs. Their space is close to the mechanism section's, so the reader's attention moves away from the calling-convention claim. Only the Refactoring row and the closing sentence bear on that claim, and the closing sentence repeats the row. The State and Control flow rows and the LangGraph/CrewAI contrast make unsourced claims about other frameworks. Direction: reduce the section to one or two sentences saying that cross-boundary moves reuse ordinary extract/inline/rename refactorings. Fold those sentences into 'Why this matters for constraining' or the mechanism section. Rehome the framework comparison and the Python-specificity open question to an llm-do-specific or orchestration-focused artifact."
  - scope: passage
    quotes: ["A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement."]
    reason: "The title promises 'bidirectional', but the numbered progression moves only from neural to symbolic. Step 4 adds an LLM call for new cases; it does not move codified code back to a prompt. The reverse move appears only in the inherited opening framing and in one late example paragraph, so a reader may remember a one-way progression. Direction: name the reverse move next to the core claim in the opening, or make it an explicit step or labelled counterpart of the progression. Keep the ticket_classifier example as its concrete support."
outcome: report
---

# Simplification synthesis: Unified calling conventions enable bidirectional refactoring

## Opportunities

### 1. Collapse the scheduler branch into its one supporting inference

- Location: "## The scheduler layer", the whole section, including the table and the closing sentence "The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring"; also the open question "Is the imperative scheduler pattern specific to Python…".
- Combines: branch-bloat (scheduler section); core-claim-obscured finding 1 (competing contrast); detail-overhang (State and Control flow rows); marginal-value-redundancy findings 1 and 3 (the closing sentence repeats the Refactoring row; off-claim rows).
- Preserve or decide: The author must decide whether the imperative scheduler is part of the claim, meaning that unified calling enables local refactoring only together with imperative orchestration. The other option is that the scheduler is an independent llm-do design choice that happens to help. If it is part of the claim, the condition belongs beside the core claim, not in a separate section. If it is independent, one sentence is enough. Keep the point that refactoring moves are ordinary code refactorings. A destination for the rehomed comparison must exist before the content leaves this note; it is not settled here.

### 2. Surface the reverse direction the title promises

- Location: "## Why this matters for constraining", from the numbered list through the `ticket_classifier` paragraph; the opening sentence "The answer is a unified calling convention…".
- Combines: core-claim-obscured finding 2; the detail-overhang and marginal-value-redundancy passes, which both judged the `ticket_classifier` paragraph to be needed support for the reverse direction.
- Preserve or decide: The note uses two meanings of the move toward the LLM. One is relaxing as an extension, where step 4 adds an LLM call for new requirements. The other is reverting code to a prompt for exploration while the code still works. The author must decide which of these "bidirectional" names, or whether it names both. That choice settles where the reverse move is stated. Preserve the example's condition that the name and the set of output labels stay fixed, because that condition carries the argument. One possible resolution is an opening sentence such as: "The same name can move either way: codify a stable pattern, or put a prompt back in to explore a change." This is a candidate wording, not a settled one.
