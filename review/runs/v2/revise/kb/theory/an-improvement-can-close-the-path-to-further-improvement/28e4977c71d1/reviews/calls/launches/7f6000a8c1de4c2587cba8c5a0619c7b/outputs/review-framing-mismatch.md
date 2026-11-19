---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "disables a mechanism needed to select or install later revisions"
    reason: "The mechanism the note describes is the whole revision path: evidence leads to a proposed change, an adoption decision, installation and later use. Framing the loss as a mechanism needed to 'select or install' excludes cases the mechanism covers. Examples are a change that disables proposing revisions, or one that leaves installed changes unconsumed. The note itself counts the second case as loss when it says that kept files do not preserve the capability 'if the successor no longer permits or consumes their changes'. Wording such as 'a mechanism needed to carry later revisions through to use' would match the mechanism."
    level: warn
outcome: warn
---

# Review

## Summary

Most mechanism statements are framed at the right level. Non-regression protects whatever is in its checked scope. The example's comparison checked task performance while the change removed a different capability. Preservation attaches to the function, not to a component.

The opening paragraph is the exception. It names only selection and installation as the disabled functions. Later, the note defines the relevant question as the full chain from evidence to later use. Its replacement criterion is whether a revision can be carried "through to use". A reader of the opening alone would miss losses at the proposal or later-use stages. The later text corrects this, so the narrowing is local, but it does exclude covered cases.
