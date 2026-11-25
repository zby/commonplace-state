---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: propagate value from them down through answering notes and their subroutines
  change: 'Replace the coined term "subroutine" with the note''s own ordinary wording
    throughout its two occurrences: "their subroutines" becomes "the notes that answer
    their sub-questions" (giving "propagate value from them down through answering
    notes and the notes that answer their sub-questions"), and "subroutine reuse"
    in the Combining-dimensions bullet becomes "sub-question reuse".'
  reason: '"Subroutine" is not registered in the KB vocabulary and no linked note
    defines it. In this note it names the same thing the first bullet already calls
    "sub-questions": a note that answers a local sub-question raised inside another
    note, measured by weighted inbound links. No occurrence needs a distinction that
    "sub-question" lacks. Swapping between the two words makes one thing look like
    two. kb-role lists neither the term nor these bullets as relied on.'
- quote: demand-root coverage
  change: Replace "demand-root coverage" with "root-question coverage" (the only occurrence).
  reason: '"Demand-root" is coined here and nowhere else in the KB. It names the **root
    questions** the first Unsettled bullet introduces. The ordinary phrase used there
    carries the same claim. Keeping a second name for the same root makes the reader
    wonder whether it is a separate signal. kb-role does not list it as relied on.'
description: Retained proposed result of kb/instructions/simplification-passes/abstractions.md
  on kb/notes/how-do-we-value-notes.md
format: 1
operation: kb/instructions/simplification-passes/abstractions.md
operation-sha256: 66c1e66712553330a826d33689fc281147d52ac6c08ae6f8510f4eb0cd9238a4
note: kb/notes/how-do-we-value-notes.md
input-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
candidate: null
candidate-sha256: null
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/artifact/edits/ed5e4f90b054cc246e9125e3/observation.json
contract-sha256: cb15395b5b139f4e2c03d3a8bc974b6cdf52f0a427c623b8341fa6cb0835883a
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z
launch: a2ec85cf163948d5a3c0306561cc00bc
completed-at: '2026-11-25T05:28:56Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/calls/launches/a2ec85cf163948d5a3c0306561cc00bc/outputs/result.md
raw-output-sha256: 20cec1e6a2ec222ee0e65d68a4a284a0d17f89ed142b8f775174c890cfc7092d
---

# Report

Scope covered only three wordings in the Unsettled section: "subroutines", "subroutine reuse" and "demand-root coverage". Proposals only; I applied no changes.

- **subroutine** (2 occurrences: "their subroutines" and "subroutine reuse"). Decision: replace it everywhere with the ordinary sub-question wording. No occurrence needs the distinction. The KB does not register it and no link defines it. This makes 2 replacements if approved.
- **demand-root** (1 occurrence: "demand-root coverage"). Decision: replace it with "root-question coverage" to match the bullet's term **root questions**. No occurrence needs the distinction. This makes 1 replacement if approved.

Noticed but outside scope: none. None of these terms appears in a link title, filename, frontmatter field or quoted span. kb-role lists no relied-on term or claim among them.
