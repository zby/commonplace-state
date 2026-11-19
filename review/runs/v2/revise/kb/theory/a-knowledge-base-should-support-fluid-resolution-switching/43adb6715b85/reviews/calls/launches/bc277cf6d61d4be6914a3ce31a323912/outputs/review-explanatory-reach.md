---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A knowledge base should make task-relevant switches inexpensive in both directions."
      - "Fluidity is relative to the task and to the navigation operations actually available to the reader."
    reason: "The central prescription is close to analytic. It asks that 'task-relevant' switches be 'inexpensive' and that readers avoid 'avoidable transition cost', and later makes fluidity relative to the task and the available operations. No mechanism says why readers must switch, and the claim weighs the benefit of cheap switching against nothing. That missing reason is bounded context, which prevents loading every view at once; it is only implied by phrases such as 'without loading unrelated material'. The note never weighs the cost of maintaining intermediate views, indexes and links. It also does not consider whether cheap switching could hurt a task, for example through thrashing between views. As a result, no observation the note allows could count against the 'should', and swapping its rationale (cost, comprehension, discovery) leaves the conclusion unchanged."
    level: warn
outcome: warn
---

# Review

## Summary

The note explains its components well. Title-as-claim lets a reader inspect assertions before loading bodies. Link phrases carry why a target matters. Pointer tiers form a cost gradient. The contrast with retrieval accuracy names two concrete failure shapes: the right detail with no recoverable context, and an overview that never reaches detail.

The central claim itself is under-explained. The note does not state why a reader must alternate between views and cannot simply load what the task needs. It does not state what fluid switching buys that would be lost otherwise, beyond avoiding cost that is by definition avoidable. The task-relativity qualifiers in the opening and the Boundaries section accurately describe scope. Combined with the missing trade-off, though, they leave the prescription with no condition under which it would fail.

A hard-to-vary version would name the constraint that creates the need to switch. It would also say what the criterion forbids, such as a design that buys cheaper switching at a maintenance or context cost greater than the transitions it saves. The note's honest "qualitative criterion" framing limits how far this matters, so the finding is WARN, not FAIL.
