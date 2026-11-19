---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "causes a retained change to its reusable machinery that later work depends on"
    reason: "Modifier attachment: the relative clause \"that later work depends on\" most naturally attaches to the nearest noun, \"its reusable machinery\", giving the reading \"a change to the machinery that later work depends on\". The intended condition (per the linked factory-learning note) is that later production depends on the retained change. The unintended reading drops the dependence-on-the-change guard that distinguishes retention from inert storage. Reordering fixes it, e.g. \"causes a retained change to its reusable machinery, and later work depends on that change\"."
    level: warn
  - scope: passage
    quotes:
      - "a description cannot change whether its judgment was required for installation"
    reason: "Reference: \"a description\" has no antecedent, so readers can take it as a description of the evaluator's role, the note's own framework description, or a system description; \"its\" must then be resolved back past it to the evaluator. The intended reading (labelling an evaluator as the judge does not alter whether it actually gated installation) is recoverable but not immediate."
    level: info
outcome: warn
---

# Review

## Summary

Most sentences have a single plausible parse; negations such as "not merely stored" and "not merely editable files" scope clearly. The opening definition of experience-responsive retention has a relative clause that attaches more naturally to the machinery than to the change, which plausibly misstates the dependence condition. A Scope bullet uses "a description" without an antecedent, a smaller reference problem.
