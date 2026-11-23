---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/articles/types/article.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
criterion: kb/articles/types/article.md
criterion-sha256: 67e5014396781a309377cfc87db1b1b92a105f448ed73253b1d9a07db19db2e4
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a18998c22220424d98d684665056188b
completed-at: '2026-11-21T19:27:34Z'
findings:
- scope: passage
  quotes:
  - as Commonplace currently is
  reason: Commonplace is first named here without introduction; an external reader
    learns what it is only from the later 'Current state of evidence' paragraph and
    the earlier unnamed 'Our knowledge base'. A one-clause gloss at first mention
    would make the article fully self-contained, but the surrounding text already
    lets a reader infer it is the authors' own system, so this does not break the
    reader-without-KB-context requirement.
  level: info
- scope: passage
  quotes:
  - belonged in a temporary workshop instead
  reason: '''Workshop'' and the nearby ''type contract'' are KB-local terms. Both
    read acceptably as ordinary English in the example (a scratch area; a document-type
    rule), so no KB context is required to follow the scenario; noted only as a possible
    tightening for external readers.'
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a18998c22220424d98d684665056188b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/a4ea6a6f60f2dc0d4658f0ee/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a18998c22220424d98d684665056188b/outputs/review.md
raw-output-sha256: 5b1ea06bd02f152b8d02e5793743502aecb5bd665ceb935adb7e830a1405a60e
---

# Review

## Summary

The article type spec is deliberately minimal. Beyond structural frontmatter fields (left to the validator), its only authoring instructions are that an article is outward-facing, self-contained prose for a technical reader with no KB context, and that `description` serves as a retrieval filter for agents rather than as the reader-facing abstract. The spec adds no `## Review` section and no title convention.

The note meets both instructions. It opens by establishing the standard ML frame (substrate plus selection signal) that its intended reader already holds, states its two-level thesis, and works through a concrete example before the abstract definition. Each KB-derived concept it relies on (deliberative learning, on-balance judgment, single- and double-loop revision, operative change, "learned") is explained inline. The links then serve as optional depth, not as required context. External precedents (Gödel machine, PRODIGY, EURISKO, the Bitter Lesson, the Sutton/Javed interview) are introduced with enough description for a reader to follow without opening them. The material-limits and evidence sections fit an outward-facing piece that does not overclaim.

The description is phrased as a retrieval summary ("Lead article: … fixed-weight LLM bet, weight-training contrast, Bitter Lesson, and empirical test") rather than a reader-facing abstract, as the spec asks.

The two info findings mark places where KB-local naming could be glossed for an external reader. Neither prevents a reader without KB context from following the argument.
