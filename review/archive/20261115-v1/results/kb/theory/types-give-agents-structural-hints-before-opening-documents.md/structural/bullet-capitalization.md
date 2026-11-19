---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/structural/bullet-capitalization.md
criterion-sha256: 2e734f0ddd534de59baaf5a39723d7e7a92d8037d10c9987db951756c0932a05
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: c9cc6c66977a40b68e1916e71c7e767e
completed-at: '2026-11-12T09:58:05Z'
---
### Summary

The note's only bullet list is the "Relevant Notes" footer. Each of its four items begins with a link. Three link labels are lowercase file slugs, which count as identifiers. The fourth label, "note base type", is lowercase prose. It matches the lowercase link-label convention of the list, so it is a stylistic edge case, not a capitalization failure.

### Findings

- INFO: The bullet `[note base type](../types/note.md) — defines description ...` starts with a lowercase prose link label. The sibling bullets start with lowercase slug identifiers, so the lowercase start is consistent with the list. Capitalizing it as "Note base type" would be optional.

## Result: PASS
