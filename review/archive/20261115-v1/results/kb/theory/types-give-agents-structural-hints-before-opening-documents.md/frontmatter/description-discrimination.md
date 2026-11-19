---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: f6f67c52d8a3bad2e0cef6aa8f57baf38e9aa0928c3983e7edb727f26d4103d2
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: d13a0023e3b4b8ca1db5ea97d18890913e47cf3be538e907313397e6f5176fba
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910
launch: d765cf91f0514877b39691b815a5c020
completed-at: '2026-11-12T09:56:53Z'
---
### Summary

The description goes beyond the title. It names a mechanism: the type says which operations a document affords, and the description filters among instances of that type. It also gives an implication: routing decisions can be made without loading full documents. An agent scanning a short result list could tell this note apart from neighbours about type verifiability or metadata enforcement.

### Findings

- low: The description adds the type/description division of labour, which the title does not contain. That division is the note's distinctive mechanism, so the description adds retrieval value and does not paraphrase the title.

## Result: PASS
