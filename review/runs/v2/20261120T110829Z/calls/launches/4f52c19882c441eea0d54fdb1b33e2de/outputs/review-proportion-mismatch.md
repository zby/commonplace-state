---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

The note's core claim has two parts:

1. A unified interface lets a programmer swap prompts and code without editing
   callers. This is the title claim.
2. The swap leaks asymmetrically in the two directions. This is the description
   and the opening thesis.

Each part gets substantive development. "What the interface hides and what
leaks" develops the asymmetry with a mechanism for each direction and a
practical consequence. "Why this matters for constraining" is the longest
section. It develops the title claim through a worked example of three moves,
which also separates refactoring from prototyping and relaxing. That example
supports the load-bearing claim directly, so it is not secondary material.

"The mechanism", "Scope" and "The connection to typed callables" are short
supporting sections, sized to match their role. No secondary section outgrows
the core, and nothing needs to be split into its own note.
