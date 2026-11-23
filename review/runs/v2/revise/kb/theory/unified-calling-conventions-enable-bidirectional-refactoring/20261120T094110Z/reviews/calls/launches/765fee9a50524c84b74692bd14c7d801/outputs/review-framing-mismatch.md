---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This requires **name-based dispatch**"
    reason: "What makes call sites stable is indirection behind a shared interface. Name-based dispatch is how llm-do achieves that indirection, and it is natural when the caller is an LLM that emits a string. Code callers could also get implementation-agnostic interfaces through a protocol or interface reference. The sentence puts weight on one implementation, but the following sentence explains why names suit this runtime, so the framing does not mislead about the mechanism."
    level: info
  - scope: passage
    quotes:
      - "**Extend via relaxing** — new requirements emerge (handle Unicode, detect dates). Add an LLM call for the new cases."
    reason: "The step is called relaxing, but what it describes is adding neural handling for requirements the code never covered. It does not move existing rigid code back to the LLM, which is how the note's opening describes relaxing. The point stands: the call site stays stable either way. The label just frames extension as a reversal."
    level: info
outcome: pass
---

# Review

## Summary

The note's explanations of mechanism mostly sit at the right level of generality. The core claim is framed as a shared interface that keeps call sites stable, so refactoring across the neural/symbolic boundary stays local. That framing matches the mechanism described. The scheduler section correctly says that refactoring becomes ordinary code refactoring because orchestration is written in Python rather than as graph edges. Two framings put weight on a narrower case than the mechanism covers: name-based dispatch as a requirement, and "relaxing" as the label for extension. Neither excludes cases the reader needs, so both are informational.
