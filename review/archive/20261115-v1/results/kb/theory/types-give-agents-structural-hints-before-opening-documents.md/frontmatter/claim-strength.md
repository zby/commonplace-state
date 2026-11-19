---
note: kb/theory/types-give-agents-structural-hints-before-opening-documents.md
note-sha256: 46b27fc41383c7b1d25db27679c47c878ba64767dd1abe39f4921ec8b9c6ec5e
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 605b7f5dbed3c7d1831c1e556958911bb61f2c9ebbbe69e22adac138ef60c61f
outcome: warn
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

The title "Types give agents structural hints before opening documents" is a proposition, but most of it sits close to a truism. Any metadata field is visible before the document is opened, and few informed readers would deny that a type label carries some information. The contestable content is the word "structural": a type should signal structure and affordances, not subject matter, and type plus description is enough to route without loading. The body develops that point, but the title only hints at it, so a reader could take the title as "metadata is informative".

### Findings

- medium: The obvious opposite, "types give agents no information before opening documents", is not a position anyone informed would hold. That leaves "structural" as the only contestable element. Someone could argue that types in practice are topical labels, or that descriptions or search do the routing and types add little. The title does not state that position clearly enough to invite this disagreement.
- low: The note's stronger and more contestable claims stay in the body. One is that types must assert structural properties rather than subject matter to be useful for routing. The other is that type plus description lets an agent narrow from hundreds of files without opening any. The title states neither.

### Suggested Revision

Sharpen the title to the contestable point the body establishes, for example:

- `Types route agents only when they promise structure, not subject matter`
- `Type and description together let agents route without opening documents`

## Result: WARN
