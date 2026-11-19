---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "In that regime a structured span locator earns its keep"
    reason: "Literal meaning: in that regime a structured span locator is worth its cost or is the appropriate design. `Earns its keep` adds a deservingness connotation that the note neither uses nor supports, and it is the gate's own fail example. Replace with \"In that regime a structured span locator is the appropriate design\" (or \"is justified\"). This removes the idiom without losing precision."
    level: warn
  - scope: passage
    quotes:
      - "Change the premise and the conclusion moves, which is where the claim earns its boundaries."
    reason: "Literal meaning: the claim's boundaries are where its premise stops holding. `Earns its boundaries` adds deservingness and makes the reader translate a figure that adds no contrast or mechanism. Replace with \"The claim's scope ends where its premise fails.\" This removes that reading effort and the unused connotation."
    level: warn
  - scope: passage
    quotes:
      - "The claim bites exactly where capture is lossy"
    reason: "Literal meaning: the claim applies, or has practical consequences, only where capture is lossy. `Bites` is a mild conventional idiom, but \"The claim applies exactly where capture is lossy\" is as short and clearer. This is minor; it is recorded for completeness alongside the other scope-section idioms."
    level: info
outcome: warn
---

# Review

## Summary

Most of the note's figurative wording has a function. The *spent* / *earned* pairing in the opening ("is spent at capture and never replenished" versus authority "earned by post-capture work") sharpens a real contrast between fidelity and authority that the paragraph goes on to use: "capture sets a ceiling" and "earn authority beneath it". *Ceiling* names an upper bound precisely. The *debt* language in the scope section ("the debt is fixed at ingest … repaid deliberately") maps onto the note's mechanism: an unpreserved verbatim layer is a deficit that only re-capture removes. Those figures are kept.

The failures cluster in the Scope section. There, two uses of *earns* ("earns its boundaries", "earns its keep") add a deservingness connotation that the note does not establish. They state ideas that literal wording states at least as clearly. Both are local, so the outcome is WARN, not FAIL.
