---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f24b57e737d155f868fa595e2368f8ef50701cd23fcd6527138d10efd84c77f7
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: 8be791a40f11c0a55ffa35a184314b493aafed720195e5b9c5afb8947476309b
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

The title and opening claim generality over agents working with typed document collections. Domain-specific vocabulary in the body — the type names `spec`, `structured-claim`, `index`, the "Evidence and Reasoning sections" example, and "every note in a design KB is about design" — is presented as illustration, introduced with "A `spec` tells..." or quoted as contrasting examples. None of it leaks in unmarked to narrow the claim.

### Findings

- INFO: "This has Evidence and Reasoning sections" ties the structural-property example to one particular type's section layout. It is quoted as an example of a structural assertion, so it reads as illustration rather than a commitment of the general claim to that type.

## Result: PASS
