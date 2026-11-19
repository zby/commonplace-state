---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 0499d84d3687b03ad5185f1122735c6934aa8fdc27e6c85fd1a2aa1d7a76cb7c
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

The note has no internal section headings below the title, so there are no adjacent section pairs to compare. Its paragraph order already moves from general to specific. First comes the problem: stateless agents with finite context. Next comes the general mechanism, that types give structural hints before a document is opened. That paragraph then gives examples (`spec`, `structured-claim`, `index`). After it come the role of descriptions, the verifiability criterion and the enforcement dependency. No specific case comes before the rule it exemplifies.

### Findings

- INFO: No specific-before-general ordering found. The note has only one body section, and its paragraphs present the general claim before the examples.

## Result: PASS
