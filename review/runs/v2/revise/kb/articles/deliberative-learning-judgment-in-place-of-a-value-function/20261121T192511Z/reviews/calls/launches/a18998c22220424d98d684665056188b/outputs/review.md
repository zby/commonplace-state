---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "as Commonplace currently is"
    reason: "Commonplace is first named here without introduction; an external reader learns what it is only from the later 'Current state of evidence' paragraph and the earlier unnamed 'Our knowledge base'. A one-clause gloss at first mention would make the article fully self-contained, but the surrounding text already lets a reader infer it is the authors' own system, so this does not break the reader-without-KB-context requirement."
    level: info
  - scope: passage
    quotes:
      - "belonged in a temporary workshop instead"
    reason: "'Workshop' and the nearby 'type contract' are KB-local terms. Both read acceptably as ordinary English in the example (a scratch area; a document-type rule), so no KB context is required to follow the scenario; noted only as a possible tightening for external readers."
    level: info
outcome: pass
---

# Review

## Summary

The article type spec is deliberately minimal. Beyond structural frontmatter fields (left to the validator), its only authoring instructions are that an article is outward-facing, self-contained prose for a technical reader with no KB context, and that `description` serves as a retrieval filter for agents rather than as the reader-facing abstract. The spec adds no `## Review` section and no title convention.

The note meets both instructions. It opens by establishing the standard ML frame (substrate plus selection signal) that its intended reader already holds, states its two-level thesis, and works through a concrete example before the abstract definition. Each KB-derived concept it relies on (deliberative learning, on-balance judgment, single- and double-loop revision, operative change, "learned") is explained inline. The links then serve as optional depth, not as required context. External precedents (Gödel machine, PRODIGY, EURISKO, the Bitter Lesson, the Sutton/Javed interview) are introduced with enough description for a reader to follow without opening them. The material-limits and evidence sections fit an outward-facing piece that does not overclaim.

The description is phrased as a retrieval summary ("Lead article: … fixed-weight LLM bet, weight-training contrast, Bitter Lesson, and empirical test") rather than a reader-facing abstract, as the spec asks.

The two info findings mark places where KB-local naming could be glossed for an external reader. Neither prevents a reader without KB context from following the argument.
