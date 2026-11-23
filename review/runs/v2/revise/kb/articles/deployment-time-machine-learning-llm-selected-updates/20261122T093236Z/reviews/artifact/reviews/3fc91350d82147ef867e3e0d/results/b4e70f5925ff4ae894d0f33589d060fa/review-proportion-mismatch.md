---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - derive the preference model from the declared purpose of the work
  reason: The article's distinctive claim is that a fixed-weight model can build the
    preference model from a stated purpose. This part of the bet is asserted twice
    but never illustrated. The routing-line example shows the judge choosing a trial
    over permanent adoption. It never shows which value functions the purpose admits,
    or how the judge decided that the trial wins under all of them. By contrast, secondary
    material gets detailed development. The Gödel machine paragraph sets out its axioms,
    its optimality guarantee, its blind spots and its ability to rewrite its own utility
    function. The Bitter Lesson section spends a full paragraph on the harness-evolution
    study's diagnosis. The load-bearing step is thinner than these supporting precedents
    and objections.
  level: warn
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/prose/proportion-mismatch.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/prose/proportion-mismatch.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: fb51077aa8dac05a5ef18899f53d5817709c13e8af39af438673c49ccbf6054b
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/3fc91350d82147ef867e3e0d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b4e70f5925ff4ae894d0f33589d060fa
completed-at: '2026-11-22T09:34:30Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/outputs/review-proportion-mismatch.md
raw-output-sha256: a6b11abda71a7e4e8f454ee050fbdfaf7d6c85eb59bd77845699296295439c48
format: 2
---

# Review

## Summary

The note has two core claims. The first is that selection needs only a
robust comparison, not one score. The second, and the article's distinctive
contribution, is the bet that a fixed-weight language model can derive the
preference model from a stated purpose and make that comparison. The first
claim is well developed: the decision-analysis account, the limit of the
analogy, and the treatment of open comparisons and reversibility.

The second claim is developed mostly as a statement of what the bet requires
and what it is not: reasons instead of explicit value functions, consistency,
and the double-loop requirement. Its first and novel step, building the
preference model from a purpose, gets no worked case. The worked example
mentions a weighing but skips the step where the admissible value functions
are identified. Meanwhile, the historical precedents (especially the Gödel
machine) and the Bitter Lesson rebuttal receive more detail than this step.

A fix need not cut the secondary material. Extending the routing-line example
would do it: name two or three value functions the purpose admits, and show
that they disagree on permanent adoption but agree on the trial. That would
give the load-bearing step concrete support. If the Bitter Lesson discussion
keeps growing, it could become its own article.
