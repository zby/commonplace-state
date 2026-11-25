---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/types/note.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 255dedcab1704028a52835020606ece8
completed-at: '2026-11-25T05:23:05Z'
findings:
- scope: passage
  quotes:
  - This query stays open as long as candidate selection relies on ad-hoc judgment
    rather than a tested valuation practice
  reason: The note's one stated applicability condition (when the query stays open
    and when it would narrow or retire) sits inside `## Stakes` rather than under
    a `## Scope` heading. The type spec asks for known limits under their own heading
    so a rescoping edit can narrow them without rewriting the body. Because this is
    a lifecycle condition on a standing query rather than a limit on an asserted claim,
    and the five lenses carry their own inline conditions, the omission is minor.
  level: info
- scope: document
  quotes: []
  reason: The template's `## Open Questions` role is filled by a section headed `##
    Unsettled`. The content matches the template's intent (unresolved points worth
    tracking), so this is a heading-label divergence, not a missing function.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/255dedcab1704028a52835020606ece8/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/275021220aa9affffb00d090/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/255dedcab1704028a52835020606ece8/outputs/review.md
raw-output-sha256: b69a0fe322d3232ded9f24fecd923b29ac80cedc8d0ca75096d0f9d8f687c78f
---

# Review

## Summary

The note does what the `note` type's authoring instructions ask. It is a transferable piece of KB methodology (how to judge whether a note is worth keeping) rather than task-local material. It gives an agent enough body context to use it. `## Stakes` states why the question matters and when it would retire. `## Current answer` puts the substantive position near the top: five partial valuation lenses, each tied to a linked theory or reference note. `## Unsettled` tracks the open problems.

## Writing shape

- **Main claim near the top.** The opening is a stakes section rather than the claim itself. For a standing query, however, the current answer follows immediately and is the note's main content, so the instruction is met.
- **Links to adjacent notes.** Inline links carry the relationship in each lens bullet. The footer repeats the main neighbours with relation labels. Traversal is well supported.
- **Rationale versus procedure.** The note explains valuation rationale and open design problems. It contains no imperative procedure that belongs in instructions.
- **Scope.** No `## Scope` heading exists. The only stated limit is the query's lifecycle condition, which is embedded in `## Stakes`. This is recorded as info rather than warn: the spec permits omitting the section when no claim limit is known, and that condition does not limit a claim.
- **Description.** The description is a single sentence and separates this query from the collection-goal documents it extends. Its discriminating power is left to the description gate.

The note carries no `user-verified` field, which is consistent with the verification rules. Title form, description discrimination and frontmatter structure belong to other gates and the validator, so this review does not judge them.
