---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 4ba8de7fcdafcaa3e01eb59acaa6504100699f947e3c29a8e826a2c0dcccc2a6
outcome: warn
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

I checked four distinct link targets: `../types/note.md`, `./document-types-should-be-verifiable.md`, `./type-system-enforces-metadata-that-navigation-depends-on.md` and `./why-notes-have-types.md`. All resolve. Three link texts match their targets. The link text "description is the most important field" asserts a ranking that the note base type spec does not make. The Relevant Notes annotation for the same target repeats that claim.

### Findings

- WARN: "This is why [description is the most important field](../types/note.md) — it's a retrieval filter, not a summary." The link text says the target establishes description as *the most important field*. The target, the `note` type spec, lists `description` as a required field ("Discriminating retrieval filter, not a summary"). Its Description section says the field "should answer 'why this document?' for a future retrieval decision." It never ranks description above other fields, and it lists `type` as required too. A reader who does not follow the link believes the type spec makes a priority claim it does not make. A reader who does follow it finds no such claim. The Relevant Notes entry ("defines description as the most important field") repeats the mismatch.
- INFO: "[verifiability criterion](./document-types-should-be-verifiable.md)": the target's title and first section define the criterion. Matches.
- INFO: "[type-system enforcement](./type-system-enforces-metadata-that-navigation-depends-on.md)": the target's title and opening say the type system makes descriptions exist. Matches.
- INFO: "[why-notes-have-types](./why-notes-have-types.md)" (Relevant Notes): the target is the overview of type-system roles, with Navigation as the first role. Matches the "context" annotation.

### Suggested Revision

Make the link text say what the target supports, for example: "This is why the [note type defines description as a retrieval filter, not a summary](../types/note.md)." If keeping the priority claim, assert it as this note's own conclusion, outside the link: "This makes description the most important field for routing: the [note type](../types/note.md) defines it as a retrieval filter, not a summary." Update the Relevant Notes annotation to match, for example: "defines description as a discriminating retrieval filter — the role this note's routing argument depends on."

## Result: WARN
