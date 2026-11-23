---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/articles/types/article.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
criterion: kb/articles/types/article.md
criterion-sha256: 67e5014396781a309377cfc87db1b1b92a105f448ed73253b1d9a07db19db2e4
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 34818b4460fc41888c0de4f00317cb70
completed-at: '2026-11-22T09:34:58Z'
findings: []
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/34818b4460fc41888c0de4f00317cb70/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/42a44b8df89d406a6c1cf1a9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/34818b4460fc41888c0de4f00317cb70/outputs/review.md
raw-output-sha256: 06ace1d57b1b18f411bc03a7f059ce3a7dbbcc37860da74416278114c8570436
---

# Review

## Summary

The article type spec is deliberately minimal. Its only authoring instructions are: write outward-facing, self-contained prose for a technical reader with no KB context; use `description` as an agent retrieval filter rather than a reader-facing abstract; and leave editorial conventions to the collection contract, which this gate does not re-judge.

The note meets each instruction.

- **Self-contained for a reader without KB context.** The article defines its working terms when it first uses them: selection-based learning, preference model, robust comparison, direct update, single-loop and double-loop, workshop ("the system's temporary area for unfinished work"), Commonplace ("our agent-operated knowledge-base framework") and theory builder ("where the store holds explicit, criticized theories"). It explains its external precedents (AlphaGo Zero, Gödel machine, PRODIGY, EURISKO, the Bitter Lesson, ordinal regression) in the text, so its argument does not depend on following the links. The links into the KB add depth; the reader does not need them to follow the argument.
- **Outward-facing.** The article addresses an external technical audience. It anticipates their objections (the Bitter Lesson section), states the current evidence and its limits plainly, and invites counterexamples through a public discussion channel.
- **Description as a retrieval filter.** The description names the article's role ("Lead article") and lists the topics an agent would filter on: selection without a single score, the fixed-weight LLM bet, the weight-training contrast, the Bitter Lesson and the empirical test. It is a topic index, not an abstract.

Frontmatter and schema checks, including `source_notes` resolution, belong to the deterministic validator. Catalog properties of the title and description belong to their own gates.
