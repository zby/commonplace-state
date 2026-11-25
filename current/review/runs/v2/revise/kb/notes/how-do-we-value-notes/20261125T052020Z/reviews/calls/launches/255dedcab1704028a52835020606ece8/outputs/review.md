---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This query stays open as long as candidate selection relies on ad-hoc judgment rather than a tested valuation practice"
    reason: "The note's one stated applicability condition (when the query stays open and when it would narrow or retire) sits inside `## Stakes` rather than under a `## Scope` heading. The type spec asks for known limits under their own heading so a rescoping edit can narrow them without rewriting the body. Because this is a lifecycle condition on a standing query rather than a limit on an asserted claim, and the five lenses carry their own inline conditions, the omission is minor."
    level: info
  - scope: document
    quotes: []
    reason: "The template's `## Open Questions` role is filled by a section headed `## Unsettled`. The content matches the template's intent (unresolved points worth tracking), so this is a heading-label divergence, not a missing function."
    level: info
outcome: pass
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
