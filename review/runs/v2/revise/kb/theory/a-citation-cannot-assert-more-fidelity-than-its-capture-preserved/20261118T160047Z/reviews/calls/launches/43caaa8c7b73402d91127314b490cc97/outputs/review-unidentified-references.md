---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "judges such false mismatches worse than no check"
    reason: "ADR 046 is cited as an authority without saying what it is. The note never says that it is one of this KB's own architecture decision records, and the abbreviation \"ADR\" is never expanded. The link path (../reference/adr/) shows where it lives, but the gate requires identification inline. Without it, a reader cannot tell whether the judgement comes from an external standard or from a local design decision. Identify it on first mention, for example \"Commonplace's architecture decision record ADR 046\"."
    level: warn
  - scope: passage
    quotes:
      - "equal bytes at an arbitrary path do not (ADR 073)"
      - "never existed contiguously (ADR 094)"
    reason: "ADR 073 and ADR 094 are cited as unlinked bare identifiers. Once ADR 046 is identified, a reader can infer that they are the same kind of document. Linking them, or briefly naming what each decides, would let a reader locate the evidence."
    level: info
  - scope: passage
    quotes:
      - "In one casebook corpus"
    reason: "The note cites a specific corpus as evidence but does not say what it is or whose it is. It attributes the observation only to ADR 046. A reader cannot tell what kind of collection produced the mismatch statistics. The author should name or describe the corpus; the reviewer does not supply that identification."
    level: info
outcome: warn
---

# Review

## Summary

The note names no external system, product, person or organization. Its named references are this KB's architecture decision records, which carry the evidential weight for several claims. The first one, ADR 046, appears without saying what an ADR is or that it is a local design decision rather than an outside authority. That gap is a warning. The later unlinked ADR citations and the unnamed "casebook corpus" are minor identification gaps.
