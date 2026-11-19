---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The stronger design is a workshop surface"
    reason: "This comparative design claim is the note's own proposal. It is stated as established ('The stronger design is'), with no proposing language. The support placed beside it is one kit that implements the design ('useful because it implements this distinction directly'). Implementation shows that the design is feasible and coherent, but not that it is stronger than the alternatives; the linked review also records that the kit's read-back faithfulness is untested. Adjacency lets the kit's existence read as warrant for the comparison, and the Commonplace implication and future-surface recommendation inherit that confidence."
    level: warn
  - scope: passage
    quotes:
      - "so higher-authority systems still need executable validators or review gates"
    reason: "This is an inference from one kit's limits and is phrased as a settled consequence ('so ... still need'). The ingest reports the opposite observation (autonomous sessions honored authority constraints from skill text alone), so this is a position the note takes rather than a derived result. Its status is recoverable from 'Its limits are equally instructive', but only with effort."
    level: info
outcome: warn
---

# Review

The note mixes definitional claims (what active work state is), derived claims (each surface answers a different question, so collapsing them loses state), observations about one external system (the Claude Workstream Kit) and design recommendations for Commonplace.

The definitional and derived claims are presented appropriately. The failure claims about chat history and retrospective memory follow from the stated questions each surface answers, and the linked notes support them. The Commonplace recommendation is explicitly marked as an implication ("the implication is", "should therefore").

The problem is the bridge between them. "The stronger design" asserts a comparative verdict that the note constructs itself. The only evidence beside it is that one kit implements the design. Because the downstream recommendations are framed as following from this claim, the kit's existence is presented as licensing a superiority claim it does not test.
