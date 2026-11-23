---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Deployment time, taking effect on the next task that reads the store"
    reason: "The comparison table makes update timing a structural axis, with deployment time for deliberative learning and training runs for weights. The article's own two-condition definition has no timing condition, and two boundary cases fall outside the row. First, online weight updates made during deployment are weight training at deployment time. Second, a team editing its handbook or code by judgment before a release is deliberative learning outside deployment. The intro itself counts the handbook team as a precedent. The row describes the Commonplace deployment, not the paradigm contrast it claims to draw."
    level: warn
  - scope: passage
    quotes:
      - "the bet fails—and weights-only continual learning wins those domains"
    reason: "The failure clause names two outcomes: the bet holds, or weights-only continual learning wins. Other outcomes fit the article's own material. Both approaches could fail in a domain. A human judge could still make deliberative learning viable there. The approaches could also combine: the cited Harness Evolution study reports adapters that stack with an evolved harness. The bet's failure does not imply the weights-only alternative."
    level: warn
  - scope: passage
    quotes:
      - "Inspecting traces to edit, narrow, or revert specific entries while keeping the rest"
    reason: "The table presents targeted, trace-based correction as the deliberative side of the contrast. The simplest deliberative learner is a one-shot admission gate that never revises earlier edits. It meets both conditions but has no such correction, and the linked definition treats correction as a separate property. The article's 'Where to go next' points to this distinction, so the boundary is recoverable. The table cell still strains it."
    level: info
  - scope: passage
    quotes:
      - "four hazards can defeat it"
    reason: "Search omission is an adjacent failure outside the list: the loop never proposes the edit worth having, and no judge can recover that. Retrieval misses are another; the earlier cost paragraph names them, but the hazard list does not. The list is not presented as exhaustive, so coverage is strained rather than broken."
    level: info
  - scope: passage
    quotes:
      - "Looking at three precedents shows that the bottleneck was always"
    reason: "The precedent ladder of proof, fixed formula and on-balance judgment classifies systems by what fills the value-function role. The EURISKO rung sits on a different axis, criterion revision. Human on-balance judges, such as the software teams named in the intro, are the obvious precedent for the top rung, yet the ladder omits them. The mapping is possible but strained."
    level: info
outcome: warn
---

# Review

The article sets up three frameworks:

- the two membership conditions with the weight-training comparison table;
- the precedent ladder of proof, formula, changing heuristics and judgment;
- the evaluation apparatus: the learned verdict, the two-part check, the four
  hazards and the failure condition.

The two conditions handle their boundary cases well. Direct updates, readable
tabular tables, triggers and automatic logging are placed explicitly, and the
fixed-criterion limiting case is named.

The comparison table is the weak point. Its timing row does not follow from
the definition. Online weight training and pre-release deliberative editing
both fall outside the row. The correction row describes a property that some
members lack.

The closing failure condition treats a failed bet as a win for weights-only
learning. It leaves out mixed, hybrid and human-judge outcomes, and the
article's own cited evidence points to some of these.

The remaining findings are INFO: the hazard list and the precedent ladder are
illustrative rather than claimed to be complete. None calls for adding
categories. Narrowing the timing row and the failure clause would close the
gaps.
