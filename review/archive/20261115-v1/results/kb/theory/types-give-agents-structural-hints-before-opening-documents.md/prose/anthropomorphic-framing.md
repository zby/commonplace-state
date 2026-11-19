---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
criterion-sha256: 548129976b078198dfeda7986dda4ad0c99587d8a92abf119701fcd34c8ea608
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: b1cbd1adcc964c3a9cd5db25254b4b2d
completed-at: '2026-11-12T09:57:46Z'
---
### Summary

The note describes agent behaviour with verbs such as "tells", "decides", "guess", "act on" and "no memory of what they've read". In context these are conventional shorthand for an agent system's operations (loading files, selecting what to load), not claims about cognitive internals. The note does not argue about model cognition and makes no claim that depends on a mental-state reading.

### Findings

- INFO: "they start fresh every session with no memory of what they've read before" uses "memory" in the ordinary engineering sense of retained state across sessions; it is immediately glossed by "stateless", so it does not imply unsupported internals.
- INFO: "A `spec` tells an agent it can implement from this" and "tells the agent it can extract a citable argument" are conventional metonymy for metadata signalling which operations a document supports. No change needed.
- INFO: "guess what's relevant" and "decides whether to load the full document" describe selection behaviour, not belief or understanding. Acceptable shorthand.

## Result: PASS
