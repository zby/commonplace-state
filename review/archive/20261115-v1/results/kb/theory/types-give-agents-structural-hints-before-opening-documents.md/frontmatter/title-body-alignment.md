---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 0bab2cac5b5683effcc0144e77be581f27f37ec7e4397145d15abb6f009128fd
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: b2930f2198c00862677777da136d1e12e0ca38fede54784dff8f6b211ee73963
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

The body supports the title. Paragraph 2 states the claim directly ("Types solve this by giving agents structural hints *before* opening a document") with examples (`spec`, `structured-claim`, `index`). Paragraph 4 explains why the hints must be structural: the verifiability criterion requires types to assert structural properties rather than subject matter. The body also broadens to the pairing of type and description, and to the enforcement that makes the metadata reliable. These sections serve the title's claim and do not replace it.

### Findings

- low: There is mild scope widening. The body's culminating point is that type *and* description together let an agent narrow from hundreds of files without opening any, and the description field leads with "Types and descriptions". The H1 names only types. The description material is framed as a consequence ("This is why…"), so the drift is not large enough to misdirect a reader. If the joint claim becomes the note's centre, the title should name descriptions too.

## Result: PASS
