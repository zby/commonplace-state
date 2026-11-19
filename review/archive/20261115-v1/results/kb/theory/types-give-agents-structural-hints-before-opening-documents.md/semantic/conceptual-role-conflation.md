---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: 2c95b9e9961ccdb10c4470e553b38d352320debd149fa71842c9a2c69c4be1bb
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: fda83731e2314289ae9e403555a60d57
completed-at: '2026-11-12T09:59:11Z'
---
### Summary

The note applies existing KB concepts (verifiability, type-system enforcement, the description as retrieval filter) to the navigation role of types. Each import is made through a link, and the note does not claim to define any of them. One compressed passage blurs the type specification and the validator that enforces it. Nearby wording and the linked note settle the roles, so the blur is not material.

### Findings

- INFO: "descriptions don't appear spontaneously; the type system is what makes them exist." "The type system" could name the type specification that creates the obligation, or the validation machinery that checks compliance. The linked enforcement note separates them ("the type creates the obligation, and `/validate` checks compliance"), and the same sentence's link text says "type-system enforcement". The attribution and the note's contribution are the same under either reading, so this falls below the materiality threshold.
- INFO: "The verifiability criterion is what makes this work: types must assert structural properties, not subject matter." This passage applies the linked criterion; it does not redefine it. The colon clause restates the imported criterion faithfully. No conflation between inherited and contributed content.

## Result: PASS
