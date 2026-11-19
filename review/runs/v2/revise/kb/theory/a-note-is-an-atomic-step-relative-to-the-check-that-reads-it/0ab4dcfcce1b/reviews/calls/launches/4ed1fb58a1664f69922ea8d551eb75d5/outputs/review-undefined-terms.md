---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "an ingest's analytical prose"
    reason: "\"Ingest\" is used as a noun for a KB artifact (a tracked source analysis that holds retained quotes and the analyst's own prose), but the note never says what an ingest is. A reader without Commonplace context cannot tell why an ingest's prose differs from its retained quotes, and that difference is the point of the sentence."
    level: warn
  - scope: passage
    quotes:
      - "Commonplace marks those uses `(snapshot required)`"
    reason: "The marker is explained by its consequence (the source counts fully against the step), but \"snapshot\" itself is not glossed. The reader is not told that it means the reviewer must open the full captured copy of the source. The later phrase \"the snapshot route\" relies on that unstated meaning."
    level: warn
  - scope: passage
    quotes:
      - "the rule for one check, Commonplace's"
    reason: "\"Grounding check\" first appears here without a gloss. The preceding sentence hints at it (judging whether quoted passages support a claim), and the next section defines it properly, so the gap is short."
    level: info
outcome: warn
---

# Review

## Summary

Most technical terms are glossed where they first appear. "Atomic step" is defined in bold. "Co-loading" is explained by the following clause about how many notes fit in a context together. "Oracle domain" is paraphrased as the range of candidates a checker can assess with the required confidence. The linked theory notes are each introduced by a sentence that states their claim. The note uses no active vocabulary terms from `AGENTS.md` in a technical sense.

Two Commonplace-internal terms are used without a gloss: "ingest" as an artifact kind, and "snapshot" in the `(snapshot required)` marker and "the snapshot route". Both appear in sentences whose argument depends on knowing what they are. "Grounding check" is briefly used before its definition, which is minor.
