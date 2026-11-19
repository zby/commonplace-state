---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
criterion-sha256: f1fcb48aee55f7e09f0dfb44fb3617a247191cb80ead12ef374c8317d28d2b8f
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

The note is short (five body paragraphs) and its recurring vocabulary — "structural hints", "routing decision", "type", "description" — stays grounded where it is reused. "Routing" is introduced in paragraph two with its meaning spelled out ("the agent reads a type and description, then decides whether to load the full document"), and later uses ("routing decision informed rather than blind") sit close enough and carry enough local context to read without scrolling back. "Verifiability criterion" and "type-system enforcement" each appear once in the body and are glossed in their own sentence, so they never persist as ungrounded jargon.

### Findings

- info: "structural hints" / "structural promise" recur three times, but each use is anchored by a concrete example in the same or adjacent sentence (e.g. "This has Evidence and Reasoning sections"), so the grounding is not lost.
- info: "routing" appears in paragraphs two, four and the Relevant Notes; the term is close to its plain-language meaning (deciding which document to open) and stays recoverable at each use.

## Result: PASS
