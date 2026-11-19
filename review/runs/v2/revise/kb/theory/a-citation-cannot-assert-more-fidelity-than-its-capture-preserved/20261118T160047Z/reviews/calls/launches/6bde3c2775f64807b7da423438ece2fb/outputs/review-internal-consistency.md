---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Four questions, one answered mechanically"
      - "An identity check answers part of the second question (below)."
    reason: "The heading says one question is answered mechanically, but the section immediately assigns part of the attribution question to an identity check, which the later section describes as a mechanical checksum comparison. Reconcilable if 'answered' means fully answered, but the heading compresses away the partial mechanical answer."
    level: info
  - scope: passage
    quotes:
      - "A string check answers only the wording question."
      - "an inexpensive occurrence check can justify treating mismatch as failure"
    reason: "Likely definition drift. The description distinguishes 'a wording check, an occurrence check and a source-identity check', and the 'What makes exact meaningful' section separates normalized equality from occurrence uniqueness. Yet the first section uses 'string check', 'quote check' and 'occurrence check' for the same wording test, and the opening defines the quote check as the occurrence test. A reader cannot confirm whether wording and occurrence are one check or two."
    level: info
  - scope: passage
    quotes:
      - "A mismatched or unreadable file is a failure, not an invitation to find another copy."
      - "Missing bytes therefore report as unverified, never as passed."
    reason: "Apparent tension in outcomes: an unreadable file is a failure, while missing bytes are unverified. The two may be intended as distinct cases (file present but unreadable versus capture not available on this machine), but the note does not draw the line, and the severities differ."
    level: info
  - scope: passage
    quotes:
      - "sources whose original is gone are out of scope"
    reason: "The body says a pass is relative to the evidence used, which may be a capture rather than the original, and the same Scope bullet covers sources with retrievable bytes. Excluding sources whose original is gone sits uneasily with that: a surviving capture is exactly the case the capture-relative account handles. Probably intends 'no retrievable capture either', which needs confirmation."
    level: info
outcome: pass
---

# Review

The note's key claims are consistent across sections: a quote check tests occurrence under a normalization rule; exactness depends on the rule and on unique occurrence; a pass is relative to the evidence used, bound by checksum to a capture and no further; missing evidence cannot pass; exactness and second-hand provenance are independent. The title's claim, that a citation's verified fidelity is bounded by its capture, agrees with the body's "The binding stops at the capture".

No pairwise contradiction was found. The findings are drift and compression points that need author confirmation: the heading's "one answered mechanically" against a partly mechanical identity check, shifting names for the wording/occurrence check, an undrawn line between unreadable and missing files, and a scope exclusion that the capture-relative account appears to cover.
