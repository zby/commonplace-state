---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

The note has four headed sections and many more distinct non-obvious claims, so no section restates the argument.

## Claims and sections

Distinct non-obvious claims include:

1. A citation raises four separable questions (wording, attribution, context, truth), and a string check answers only wording.
2. Because occurrence checks are cheap and deterministic, mismatch on an exact-wording claim can be treated as failure. Support judgments are costlier and noisier, so they cannot simply block.
3. "Exact" is relative to a normalization rule that can err in either direction.
4. Occurrence is not location. Uniqueness or a checked range removes ambiguity, concatenation must be forbidden, and uniqueness does not establish intent.
5. A pass is relative to the evidence used. Checksum binding with explicit pairing ties the compared bytes to a capture, but not to the original or its author.
6. Retained, accessible and used material differ. Missing bytes are unverified, and a silent fallback creates an undeclared dependency.
7. Reading in chunks keeps the wording but can lose the context needed to judge support.
8. Exactness and second-hand provenance are independent. Exact checks verify only their own pair, while semantic hops compound.

Sections: "Four questions, one answered mechanically" (claims 1–2), "What makes 'exact' meaningful" (claims 3–4), "Which evidence a pass is relative to" (claims 5–8), and "Scope" (boundary conditions and open questions). Each section adds new substance. Scope is a support unit that carries boundary conditions: modality limits, editorial alterations and unrecognized quotations. Sections do not outnumber claims plus necessary support units.
