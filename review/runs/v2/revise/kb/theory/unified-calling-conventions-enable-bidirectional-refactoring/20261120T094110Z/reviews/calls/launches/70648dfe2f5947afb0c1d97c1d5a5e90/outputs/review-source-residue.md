---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This requires **name-based dispatch**: components are identified by string name rather than direct object reference."
    reason: "The title and opening make a general claim about unified calling conventions, but this sentence turns llm-do's implementation choice into a requirement of the general mechanism. A shared interface can also be achieved with direct references to polymorphic objects; names are needed specifically where an LLM emits the call as a string. Either scope the requirement to LLM-emitted calls or present name-based dispatch as how llm-do achieves the shared interface."
    level: warn
outcome: warn
---

# Review

## Summary

The title and opening claim generality: any system whose neural and symbolic components share a calling convention. llm-do is introduced explicitly as the demonstration ("llm-do implements this"), and most llm-do vocabulary is marked as belonging to it: `.agent` files, the hybrid VM, the "llm-do Scheduler" column and the scheduler open question.

The four-step progression uses neutral terms (agent, Python, call site) and reads as general.

The one leak is the name-based-dispatch sentence, which states llm-do's design choice as a general requirement without marking it as the illustrative case.
