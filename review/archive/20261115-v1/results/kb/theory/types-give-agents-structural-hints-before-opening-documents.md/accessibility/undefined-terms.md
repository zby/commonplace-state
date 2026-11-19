---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: 3224c054f701239072486cdd66ab3929406feab114650468b44740091b4c875f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: 3567175ed76343db93c2acb60ff19332
completed-at: '2026-11-12T09:56:34Z'
---
### Summary

The note's technical terms are mostly defined or paraphrased where they first appear. "Routing decisions" is explained in the sentence that introduces it; the "verifiability criterion" is stated inline ("types must assert structural properties, not subject matter"); "type-system enforcement" is paraphrased ("descriptions don't appear spontaneously; the type system is what makes them exist"); and each example type is glossed. No active vocabulary term from `AGENTS.md` appears in the body prose (context engineering appears only as a tag). The one mild gap is that the note assumes the reader knows that "type" and "description" are metadata fields attached to each document; this is largely inferable from paragraph two ("the agent reads a type and description, then decides whether to load the full document") and paragraph three ("description is the most important field"), so it does not block understanding.

### Findings

- low: "type" and "description" are used from the first paragraphs as KB metadata fields without saying they are frontmatter fields every document carries. A reader new to the KB can infer this from context, but a short gloss on first mention would remove the guesswork.

### Suggested Revision

In paragraph two, a phrase such as "Types — a declared kind recorded in each document's metadata, alongside a one-line description — solve this by giving agents structural hints *before* opening a document." would make the fields explicit.

## Result: PASS
