---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A knowledge base should make task-relevant switches inexpensive in both directions.
  - Fluidity is relative to the task and to the navigation operations actually available
    to the reader.
  reason: The central prescription is close to analytic. It asks that 'task-relevant'
    switches be 'inexpensive' and that readers avoid 'avoidable transition cost',
    and later makes fluidity relative to the task and the available operations. No
    mechanism says why readers must switch, and the claim weighs the benefit of cheap
    switching against nothing. That missing reason is bounded context, which prevents
    loading every view at once; it is only implied by phrases such as 'without loading
    unrelated material'. The note never weighs the cost of maintaining intermediate
    views, indexes and links. It also does not consider whether cheap switching could
    hurt a task, for example through thrashing between views. As a result, no observation
    the note allows could count against the 'should', and swapping its rationale (cost,
    comprehension, discovery) leaves the conclusion unchanged.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/14a90677b61d0922e6d404ce/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/14a90677b61d0922e6d404ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-explanatory-reach.md
raw-output-sha256: 4179c15d5b9077726e009a9af8ac78b90070ef35b0c1a89c013c7541ebb0e925
format: 2
---

# Review

## Summary

The note explains its components well. Title-as-claim lets a reader inspect assertions before loading bodies. Link phrases carry why a target matters. Pointer tiers form a cost gradient. The contrast with retrieval accuracy names two concrete failure shapes: the right detail with no recoverable context, and an overview that never reaches detail.

The central claim itself is under-explained. The note does not state why a reader must alternate between views and cannot simply load what the task needs. It does not state what fluid switching buys that would be lost otherwise, beyond avoiding cost that is by definition avoidable. The task-relativity qualifiers in the opening and the Boundaries section accurately describe scope. Combined with the missing trade-off, though, they leave the prescription with no condition under which it would fail.

A hard-to-vary version would name the constraint that creates the need to switch. It would also say what the criterion forbids, such as a design that buys cheaper switching at a maintenance or context cost greater than the transitions it saves. The note's honest "qualitative criterion" framing limits how far this matters, so the finding is WARN, not FAIL.
