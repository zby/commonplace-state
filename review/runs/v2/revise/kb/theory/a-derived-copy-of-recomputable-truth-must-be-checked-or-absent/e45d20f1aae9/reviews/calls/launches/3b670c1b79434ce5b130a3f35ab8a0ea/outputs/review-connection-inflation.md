---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "adds recomputable-and-checked as a third class between arbitrary and situational on its fix-or-leave axis"
    reason: "The body's 'What enforcement buys' section already links this note and states the same third-class relationship almost word for word. The footer adds only the `extends` label, which the gate treats as enough to avoid inflation, so this is near-restatement rather than a failure."
    level: info
  - scope: passage
    quotes:
      - "mark is the shipped, validator-enforced instance of the rule; the mark contract lives here"
    reason: "Instance 1 in the body already presents the `complete` mark as the enforced, shipped instance and says the mark contract is in this type spec. The footer repeats that framing and adds only the `evidenced-by` label."
    level: info
  - scope: passage
    quotes:
      - "duplication cited as the fourth instance"
    reason: "Instance 4 in the body already cites ADR 027 as the design of the byte-identical two-copy layout. The footer restates that and adds only the `evidenced-by` label."
    level: info
outcome: pass
---

# Review

## Summary

There are thirteen Relevant Notes entries. Five are not linked from the body (boundary of automation, LLM recompute cost, history has one chance to become checkable, enforced tag-README, local materialization), so they add navigation the body does not provide.

The others are also inline links, but most of their footer entries add framing the inline use lacks. The frontloading entry adds "validity window". The keep-compiled-views entry states the generalization direction. The lineage entry identifies this note as a specialization of the managed-staleness rule. The make-like entry attaches the detection/verification collapse to its source note. The text-testing entry names the Level A/B gradient as the boundary marker. The indexes entry recasts the body's "sharpest case of" as a grounding relation.

Three entries come closest to inflation: fix-what-the-executor-can't-determine, the tag-readme type spec and ADR 027. In each, the body already states the relationship and the footer mostly repeats it. All three still add a typed relation, which the gate's second question counts as navigational value. They are recorded as info, not as failures.
