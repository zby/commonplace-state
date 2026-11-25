---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "## Unsettled"
    reason: "The template names the section for unresolved points `## Open Questions`; the note uses `## Unsettled` for the same role. The type spec presents the template headings as a shape rather than a required vocabulary, so this does not break conformance, but a reader or tool looking for the template heading will not find it."
    level: info
---

# Review

## Summary

The note does what the `note` type spec's authoring instructions ask. It is a transferable piece of KB methodology about how notes are valued. The body gives an agent enough context to use it. The writing-shape instructions are met:

- **Main point near the top.** `## Stakes` states the question and why it matters. `## Current answer` then gives the five partial lenses Commonplace uses now.
- **Links to adjacent notes.** The links are inline where each lens is introduced, and the footer repeats the main ones with a relation for each. Traversal is well supported.
- **Rationale, not procedure.** The note explains design rationale and open problems. It gives no imperative steps.
- **Scope.** The note has no `## Scope` section. The spec allows leaving it out when no limit is known. For a standing query, the condition for keeping the query open is stated in the last paragraph of `## Stakes`, and its open edges are listed under `## Unsettled`. A separate Scope section would add nothing.
- **Description.** It says why someone would retrieve this note: to judge note value beyond repo and collection goals as autonomous production grows. It is one sentence, as the spec suggests.

The title is a question, but the template asks for a proposition. Whether a title is a proposition is left to the catalog title gate, so this review does not judge it. The only remaining difference is the section name for unresolved points (`## Unsettled` instead of the template's `## Open Questions`). That is recorded as an informational finding.
