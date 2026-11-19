---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 852f1c29eddd4d9b8255ca45c55cb863
completed-at: '2026-11-18T16:02:33Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5c5df6c05a51809e45af9154/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5c5df6c05a51809e45af9154/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/852f1c29eddd4d9b8255ca45c55cb863/outputs/review-general-before-specific.md
raw-output-sha256: 3a2057fd88e2f9c21b6923bc298e7a74b485ea58b2b52c5709c9d53524f78cfc
---

# Review

## Summary

The sections run from general to specific. No adjacent pair puts a specific case before the rule it exemplifies.

- "Four questions, one answered mechanically" sets out the general framework: four separable questions, of which only wording is checked mechanically.
- "What makes \"exact\" meaningful" refines the wording check with normalization, occurrence and location. It cites ADR 046 and ADR 094 as evidence for these points; they are not case studies of a rule stated later.
- "Which evidence a pass is relative to" covers source identity and evidence relativity. It builds on the identity check that the first section names and defers with "(below)". It is a parallel aspect of the framework, not a general rule that the preceding section exemplifies.
- "Scope" closes with boundaries and open questions, which is the expected position for qualifications.

None of the three adjacent pairs needs reordering.
