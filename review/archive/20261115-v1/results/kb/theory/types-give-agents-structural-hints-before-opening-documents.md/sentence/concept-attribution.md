---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 18b9cfe80dd7032dbf0c6460c6a62d2347c75c6d091985ca61cbe041da58299a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: f89c39834f0641958aafe179fbb54945
completed-at: '2026-11-12T09:58:02Z'
---
### Summary

The note makes three identity-style attributions to linked notes: the verifiability criterion, type-system enforcement, and the note base type's treatment of description. All three targets resolve. The verifiability and enforcement attributions match their targets. The description attribution matches in its core concept (a retrieval filter, not a summary), though the target does not rank description as the most important field. That ranking is a link-text and annotation problem, not a different concept, so it does not fail this gate.

### Findings

- INFO: "The [verifiability criterion](./document-types-should-be-verifiable.md) is what makes this work: types must assert structural properties, not subject matter." The target's title and opening section state exactly this criterion, including the same "design note" example. Its body also says types are "the hints that make those decisions informed rather than blind", which matches this note's use. Valid.
- INFO: "That's the role of [type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md) — descriptions don't appear spontaneously; the type system is what makes them exist." The target opens with nearly the same sentence and assigns itself the role of "ensuring the routing data exists at all." Valid.
- INFO: "This is why [description is the most important field](../types/note.md) — it's a retrieval filter, not a summary." The target's frontmatter table defines `description` as "Discriminating retrieval filter, not a summary," so the identified concept (description as retrieval filter) matches. The target never calls description the *most important* field. That ranking is unsupported, but the concept itself is the same. The misleading-link-text gate covers this problem.

## Result: PASS
