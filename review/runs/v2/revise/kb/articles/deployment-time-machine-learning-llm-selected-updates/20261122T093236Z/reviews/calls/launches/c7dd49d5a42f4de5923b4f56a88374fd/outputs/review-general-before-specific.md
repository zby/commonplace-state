---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Before stating the paradigm abstractly, follow a single edit through a deployed agent system"
    reason: "'One change followed through' is a worked example of the paradigm, and it comes before 'Selection-based learning versus direct gradient training', which states the general definition. Taken alone, this is the exemplify-before-general pattern. However, the opening paragraphs already state the general idea: selection by comparison and the robust comparison over a preference model. The section also announces the example-first order as deliberate. So the reader learns the rule before the case, and reordering would gain little."
    level: info
outcome: pass
---

# Review

## Summary

Adjacent section pairs checked:

1. "One change followed through" → "Selection-based learning versus direct
   gradient training": specific case before the formal definition. The
   lede states the general pattern first, so this pair is recorded as info.
2. "Selection-based learning versus direct gradient training" → "Proof,
   formula, judgment: where the bet enters": general definition, then the
   ways evaluation can work, with historical precedents. Order is correct.
3. "Proof, formula, judgment" → "Compatible with the Bitter Lesson": the
   later section answers an objection. Neither section is a specific case of
   the other.
4. "Compatible with the Bitter Lesson" → "Whether a change improved the
   system, current evidence, and limits": these address separate questions.
   No pattern/instance relation.
5. "Whether a change improved the system..." → "Where to go next":
   navigation. Not applicable.

Inside "Proof, formula, judgment", the bold-headed precedents (Gödel machine,
PRODIGY, EURISKO) come before "Robust comparison". That paragraph is the next
option in the sequence, not the general rule the precedents exemplify, so the
order is correct.
