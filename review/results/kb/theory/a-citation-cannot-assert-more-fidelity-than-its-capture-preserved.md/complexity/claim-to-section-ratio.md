---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 5b0e8e1a84fa45668de424df723d8dc7
completed-at: '2026-11-18T16:01:38Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/d58264ffbb928cd0951e8760/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/d58264ffbb928cd0951e8760/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/5b0e8e1a84fa45668de424df723d8dc7/outputs/review-claim-to-section-ratio.md
raw-output-sha256: d7d24f24912c016aa58c04c6737fb3c4312035ca14dfc852f2c66df571d856c7
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
