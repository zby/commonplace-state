---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL."
    reason: "The scheduler section brings in a second contrast, imperative scheduling versus graph DSLs (LangGraph, CrewAI), with its own four-row table. Only its closing sentence ties it back to neural-symbolic refactoring. The table gives this side argument about as much space as the mechanism section gets, so the note's weight shifts away from the calling-convention claim. Fix: shrink the section to the closing sentence's point, that cross-boundary refactoring uses ordinary extract/inline/rename, and fold it into the mechanism or 'Why this matters' section. Alternatively, mark it explicitly as a consequence of unified calling."
    level: info
  - scope: passage
    quotes:
      - "A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement."
    reason: "The title's word 'bidirectional' depends mostly on this late paragraph. Step 4 of the numbered list adds an LLM call for new cases, but it does not move a codified component back into a prompt. The code-to-prompt direction is therefore stated only in the inherited framing of the opening and in one example after the list. A reader can find the claim but may remember only the neural-to-symbolic progression. Fix: name the reverse move in the list itself, or add one sentence after the core claim in the opening saying that the same name can move either way."
    level: info
outcome: pass
---

# Review

The core claim can be stated from the note's own commitments: if neural and symbolic components share a calling convention, which llm-do implements as name-based dispatch over one namespace, a component can move across the neural-symbolic boundary in either direction without changing its call sites. The title states this claim and the description repeats it. The opening paragraph ends with it: "The answer is a unified calling convention…". Only one sentence about the underspecified instructions framing comes before it. That sentence motivates the claim and does not bury it.

Most of the later material serves the claim. "The mechanism" explains how llm-do achieves uniform calls. "Why this matters for constraining" contrasts breaking changes with stable call sites and walks through the progression. "The connection to typed callables" places the convention in a wider view in three sentences. The open questions are scoped to unified calling.

The claim stays easy to find, so the outcome is PASS. Two shape issues make it less memorable than it could be. The scheduler section and its table add a separate contrast with graph DSLs that competes for attention. The reverse direction promised by the title gets less space than the forward direction, and most of it sits after the numbered progression. Neither issue hides the claim. Both could be fixed by compressing the scheduler material into one sentence about refactoring and by naming the reverse move next to the core claim.
