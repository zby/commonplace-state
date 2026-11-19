---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A knowledge base should support fluid resolution-switching"
    reason: "As phrased, the title is close to an applause line: few informed readers would argue that a knowledge base should make movement between overview and detail rigid or costly, so the stated opposite is not a live position. The contestable point the body actually develops is narrower: resolution-switching fluidity is a separate evaluative criterion from retrieval accuracy, recall, pointer accuracy and addressability grain, so a system can retrieve the right artifact and still fail it. A title carrying that distinction (for example, that retrieval accuracy does not establish bidirectional navigability between views) would be one an informed retrieval-centric designer could dispute."
    level: warn
outcome: warn
---

# Review

## Summary

The title is a proposition, but its opposite ("a knowledge base should not support fluid resolution-switching") is not a position anyone informed would hold. "Fluid" already builds the desirability into the claim, which places it near the gate's `validation should be fast` failure example.

The body has a sharper point. It treats resolution-switching fluidity as a qualitative criterion that complements retrieval accuracy. It shows a system can retrieve the right detail yet make its wider context hard to recover, or offer an overview that never reaches the detail. It also separates the criterion from addressability grain, pointer accuracy and recall. A retrieval-focused designer could contest that independence claim, so it would make a stronger title. Alternatively, since the note mainly defines a term and inventories mechanisms, a topical title would also be valid under this gate.
