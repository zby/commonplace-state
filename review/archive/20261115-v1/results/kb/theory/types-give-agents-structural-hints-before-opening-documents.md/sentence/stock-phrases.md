---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
criterion-sha256: 6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c
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

No sentence matches the listed stock patterns: elevation, "worth noting", "in other words", "at its core" or "key insight". One sentence that closes a paragraph is close to a summary restatement. Under the deletion test it is nearly removable, but it does not use a listed pattern, so it is noted rather than flagged.

### Findings

- INFO: "The structural promise is what makes the routing decision informed rather than blind." This closes the verifiability paragraph by restating its point in a cleft construction ("X is what makes Y"). Removing it leaves the paragraph almost as clear, because the preceding sentences already contrast a non-actionable label with an actionable structural one. It is not a listed stock pattern, and it ties the paragraph back to routing, so it is not reported as WARN.
- INFO: "This is why description is the most important field — it's a retrieval filter, not a summary." The "X, not Y" contrast is not the elevation move ("not just X — it is Y"). It states a definitional distinction that the paragraph relies on, so it fails the deletion test: removing it loses content.

### Suggested Revision

Optionally delete "The structural promise is what makes the routing decision informed rather than blind.", or fold it into the previous sentence: "'This has Evidence and Reasoning sections' tells the agent, before opening the document, that it can extract a citable argument."

## Result: PASS
