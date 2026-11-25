---
type: types/answers.md
description: The operator's answers to kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/artifact/edits/ed5e4f90b054cc246e9125e3/results/a2ec85cf163948d5a3c0306561cc00bc/result.md
question: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/artifact/edits/ed5e4f90b054cc246e9125e3/results/a2ec85cf163948d5a3c0306561cc00bc/result.md
question-sha256: 48dbe14d6803c18b7bb437b3682c2c582adcfc4414cc352ea32c134eb1a989fa
items:
- id: '1'
  proposal:
    quote: propagate value from them down through answering notes and their subroutines
    change: 'Replace the coined term "subroutine" with the note''s own ordinary wording throughout its two occurrences: "their subroutines" becomes "the notes that answer their sub-questions" (giving "propagate value from them down through answering notes and the notes that answer their sub-questions"), and "subroutine reuse" in the Combining-dimensions bullet becomes "sub-question reuse".'
    reason: '"Subroutine" is not registered in the KB vocabulary and no linked note defines it. In this note it names the same thing the first bullet already calls "sub-questions": a note that answers a local sub-question raised inside another note, measured by weighted inbound links. No occurrence needs a distinction that "sub-question" lacks. Swapping between the two words makes one thing look like two. kb-role lists neither the term nor these bullets as relied on.'
  state: rejected
  reason: 'The operator preferred the more direct alternative: reuse of answers to sub-questions.'
  decided-by: operator
  decided-at: '2026-11-25T07:45:00Z'
- id: '2'
  proposal:
    quote: demand-root coverage
    change: Replace "demand-root coverage" with "root-question coverage" (the only occurrence).
    reason: '"Demand-root" is coined here and nowhere else in the KB. It names the **root questions** the first Unsettled bullet introduces. The ordinary phrase used there carries the same claim. Keeping a second name for the same root makes the reader wonder whether it is a separate signal. kb-role does not list it as relied on.'
  state: approved
  decided-by: operator
  decided-at: '2026-11-25T07:47:51Z'
---

# Answers

Set each item's `state` on the operator's word: `approved`, `rejected` with a `reason`, or `deferred` with a `reason` and a `revisit` condition. A decided item also carries `decided-by: operator` and `decided-at`. Change no `id` or `proposal`.
