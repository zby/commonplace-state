---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: b9fcdcbe17cb846a6a298af1be72486d73dde16e986ecbf022df21ffd55f0731
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

The note has no table, taxonomy, or named framework. Its only structured element is three inline examples of types (`spec`, `structured-claim`, `index`), each paired with the operation it affords. The examples make the claim concrete, showing that a type tells an agent what it can do with a document. They add no vocabulary the argument fails to use. The type-versus-description split ("what kind" versus "which instance") is a two-way distinction, and the note's routing argument uses it directly.

### Findings

- info: The three type examples are illustrations in prose, not a decorative structure. Each maps a type to an action, which is the inference the note claims types enable.
- info: The structural-versus-subject-matter contrast in the verifiability paragraph is load-bearing. It sets the condition under which type-based routing is informed rather than blind.

## Result: PASS
