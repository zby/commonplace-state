---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - judges such false mismatches worse than no check
  reason: ADR 046 is cited as an authority without saying what it is. The note never
    says that it is one of this KB's own architecture decision records, and the abbreviation
    "ADR" is never expanded. The link path (../reference/adr/) shows where it lives,
    but the gate requires identification inline. Without it, a reader cannot tell
    whether the judgement comes from an external standard or from a local design decision.
    Identify it on first mention, for example "Commonplace's architecture decision
    record ADR 046".
  level: warn
- scope: passage
  quotes:
  - equal bytes at an arbitrary path do not (ADR 073)
  - never existed contiguously (ADR 094)
  reason: ADR 073 and ADR 094 are cited as unlinked bare identifiers. Once ADR 046
    is identified, a reader can infer that they are the same kind of document. Linking
    them, or briefly naming what each decides, would let a reader locate the evidence.
  level: info
- scope: passage
  quotes:
  - In one casebook corpus
  reason: The note cites a specific corpus as evidence but does not say what it is
    or whose it is. It attributes the observation only to ADR 046. A reader cannot
    tell what kind of collection produced the mismatch statistics. The author should
    name or describe the corpus; the reviewer does not supply that identification.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/unidentified-references.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/unidentified-references.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 422847c587793f494bfa140e10c46772cc1decaf72d3a611ec83daa39da288c3
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/a4650d123a341cba78ff47e0/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/a4650d123a341cba78ff47e0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 43caaa8c7b73402d91127314b490cc97
completed-at: '2026-11-18T16:01:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/43caaa8c7b73402d91127314b490cc97/outputs/review-unidentified-references.md
raw-output-sha256: 46708aa0d761a64313ecab6c8d6ba42a6747949603c328b06654272d6bc0ce21
format: 2
---

# Review

## Summary

The note names no external system, product, person or organization. Its named references are this KB's architecture decision records, which carry the evidential weight for several claims. The first one, ADR 046, appears without saying what an ADR is or that it is a local design decision rather than an outside authority. That gap is a warning. The later unlinked ADR citations and the unnamed "casebook corpus" are minor identification gaps.
