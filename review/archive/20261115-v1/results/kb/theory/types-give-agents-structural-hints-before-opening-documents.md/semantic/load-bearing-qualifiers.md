---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 6c7d294d28b56d86ad38e9bc0ab4c3df40681be79745c798c3cc500862c27cbe
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: a3de7bb9680f1856845c00f781dd427bf942dccfa5a709fc2ed58599892d512b
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

The qualifiers in the title and description are "structural", "before opening documents", "agents", and "without loading full documents". Each does work in the argument. "Before opening" is the core of the routing claim. "Structural" is load-bearing through the verifiability paragraph: subject-matter labels are explicitly shown to fail ("This is a design note" tells an agent nothing it can act on). "Agents" ties to the premises the argument uses (stateless sessions, finite and expensive context).

### Findings

- INFO: "Agents" could arguably be widened to any reader with limited attention, since human readers also route by metadata. The note's premises, however, are agent-specific (no memory across sessions, context cost), and the KB is plainly scoped to agent-operated KBs. This is intentional domain scoping, not a narrowing qualifier without work to do.
- INFO: Deletion test on "structural": "Types give agents hints before opening documents" would admit subject-matter types. The note argues explicitly that such types do not support informed routing. The qualifier is therefore load-bearing and should stay.

## Result: PASS
