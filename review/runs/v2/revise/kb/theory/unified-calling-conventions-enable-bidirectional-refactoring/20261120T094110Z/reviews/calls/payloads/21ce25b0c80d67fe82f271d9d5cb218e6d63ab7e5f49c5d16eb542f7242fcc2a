---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs."
    reason: "A concrete empirical characterization of two named external frameworks is given without a source, and the following table extends it (\"Global context through graph\", \"Redraw edges, update graph\"). The reader cannot check it, and it is not uniformly accurate as stated: CrewAI's primary abstraction is crews of agents assigned tasks rather than a node-edge graph. Cite the frameworks' documentation or a KB review of them, or narrow the claim to graph-defined orchestration such as LangGraph's."
    level: warn
  - scope: passage
    quotes:
      - "This friction discourages incremental refactoring and pushes toward big-bang rewrites."
    reason: "A causal empirical claim about team behavior with no observation or source behind it. It is plausible as reasoning from the stated costs, so it is recorded as INFO; marking it as an expectation rather than an observed effect would make its status legible."
    level: info
outcome: warn
---

# Review

## Summary

The note contains no numbers or named studies. Its main empirical anchor, llm-do, is linked to its repository, and the `ticket_classifier` and `sanitize_filename()` cases are framed as illustrations rather than reported observations.

The unsourced characterization of LangGraph and CrewAI is the one concrete external claim the reader cannot evaluate, and it bears on the scheduler comparison table. The friction claim is a lesser instance of unattributed empirical framing.
