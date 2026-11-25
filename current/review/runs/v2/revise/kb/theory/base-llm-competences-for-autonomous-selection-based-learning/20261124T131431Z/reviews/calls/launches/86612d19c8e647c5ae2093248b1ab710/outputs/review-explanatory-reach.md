---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Any sub-task shown to be reliably offloadable to harness code moves out of the LLM column"
    reason: "The mechanism explains why some semantic residue stays on the model. Code enforces defined rules without interpretation. Meaning-dependent judgments cannot be pre-paid when their inputs do not yet exist, and open-ended work keeps producing new inputs. The note gives no mechanism for the particular three-way cut, however. It could be regrouped into two or four competences without changing the argument, and the Scope revision clause lets the list change freely. The mechanism is present but thin for the specific enumeration in the title."
    level: info
outcome: pass
---

# Review

## Summary

The central claim is that harness code can offload much of the loop, leaving semantic competences on the base LLM. Its mechanism is hard to vary. If the premise that new failure modes keep arriving is removed, the residue could be codified upstream, and the conclusion fails. If the error-correction asymmetry is removed, offloading loses its rationale. The claim is falsifiable: showing that one of the three competences can be offloaded reliably would refute part of it, and the Scope section says so. That revision clause is a stated test condition, not an ad-hoc escape hatch.

The weaker part is the decomposition into exactly three competences. The note motivates them as recurring kinds of semantic work in the loop: interpretation, diagnosis and synthesis, and judgment. It does not derive why the boundaries fall there. Its claim that the competences fail independently would constrain the cut if it were supported. Recorded as INFO.
