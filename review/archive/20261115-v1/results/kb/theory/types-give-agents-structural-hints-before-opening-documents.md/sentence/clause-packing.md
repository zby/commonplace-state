---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 574b8a9b1a59c9337d2236c50a10cf9443a41de9a7b5629dd4af39737cdbdad9
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

The note's sentences are short and mostly carry one or two clauses each. No sentence approaches 40 words with more than two or three independent ideas, and no long interrupting clause or list separates a subject from its verb or a verb from its object.

### Findings

- INFO: The longest sentence ("The type tells the agent *what kind of thing* a document is; the description tells it *which instance* among documents of that kind is relevant to the current task.") is about 30 words. It joins two parallel clauses with a semicolon, and each dependency closes quickly, so it is not overloaded.
- INFO: "These hints enable informed routing decisions: the agent reads a type and description, then decides whether to load the full document." The colon introduces a short two-step sequence; the reader holds no long dependency open.

## Result: PASS
