---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
criterion-sha256: b93b7e638ac3b531261d9bd9e35f4e6c2f730d9dc5cf9ad8474a19140b84c8e5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: 353a92f6e16d4aa8ad74edfa07408b0b
completed-at: '2026-11-12T09:56:49Z'
---
### Summary

The note already lacks a multi-section structure: it is a title plus five short paragraphs and a footer. A one-paragraph rewrite would keep the core insight, but the gate's failure mode needs a multi-section structure that the content does not justify. That structure is absent. The paragraphs also carry a boundary condition (types must assert structural properties, not subject matter) and a dependency (routing needs enforced metadata). Both earn their place.

### Findings

- info: No section headings exist, so no section structure needs justifying. The body is about as compact as its content allows. The opening paragraph on statelessness is background, but it is one short paragraph and frames the routing problem the note answers.

## Result: PASS
