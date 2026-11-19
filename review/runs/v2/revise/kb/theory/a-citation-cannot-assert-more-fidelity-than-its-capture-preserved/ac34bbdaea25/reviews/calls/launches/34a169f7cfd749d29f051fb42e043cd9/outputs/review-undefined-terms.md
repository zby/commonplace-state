---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "no rival capture design drops the layering while preserving the commitments the framework has already made"
      - "provider-contingent rather than inherited"
    reason: "The section's argument that layering is forced depends on the linked note's technical sense of an \"inherited constraint\" and a \"boundary-preserving rival\". Neither term is glossed inline; the link title stands in for the definition. The later contrast \"provider-contingent rather than inherited\" also needs that sense. A reader who has not opened the linked note cannot tell what test makes a constraint inherited. Add a short gloss, for example: a constraint is inherited when no alternative design avoids it while keeping the framework's existing commitments."
    level: warn
  - scope: passage
    quotes:
      - "Fidelity is fixed at ingest"
    reason: "\"Ingest\" is a KB-specific step name. The preceding sentence's \"capture step\" lets a reader infer that ingest is when the source is captured, so this is minor. Saying \"at ingest (the capture step)\" once would remove the inference."
    level: info
outcome: warn
---

# Review

## Summary

The note defines its central terms well. *Fidelity* and *authority* get explicit inline definitions. The three capture layers are defined in a list. "Mechanical derivation rule" is made concrete at once with substring match as the example. "Source-span locator" is clear from the surrounding sentences.

The main gap is in "Capture is layered because it is forced to be". The section claims layering is not a design choice and supports that by citing the linked note's notions of an *inherited* constraint and a *boundary-preserving rival*. The sentence uses those terms in their technical sense but does not gloss them. "Provider-contingent rather than inherited" later relies on the same distinction. So the reader has to follow the link to see why the section's conclusion holds.

"Ingest" is a smaller case: the reader can infer it from the adjacent "capture step".
