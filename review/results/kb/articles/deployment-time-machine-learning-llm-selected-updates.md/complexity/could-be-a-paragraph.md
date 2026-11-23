---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 7c5f3e3ccef24cb3aa025c05050a5c3b
completed-at: '2026-11-22T09:33:39Z'
findings: []
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/6b44bc2fd19ec86041e25f16/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 57f9af1a240e1ae506ea7dadf8c3144e28882aa0b0e560754091b3fbfdeaa075
---

# Review

## Summary

A one-paragraph rewrite would lose several non-obvious claims, boundary cases and failure conditions. The multi-section structure is justified.

## What a paragraph would lose

A paragraph could state the headline: an LLM might select edits to a readable store by robust comparison rather than a single score. It would drop material that the argument depends on:

- The boundary between selection-based learning and direct updates, including the AlphaGo Zero / AlphaZero contrast and the point that engineer-selected checkpoints learn by selection without being self-improving.
- The worked routing-line example, which shows that adopting a change on trial differs from adopting it as proposed and that the double-loop step revises the review check.
- The proof, fixed-formula and heuristic-revision precedents, which locate where the bet enters, plus the stated limit of the decision-analysis analogy (open-ended work can add criteria and widen the set).
- The Bitter Lesson argument, with Sutton and Javed's rival hypothesis, the harness-evolution evidence and the bootstrap condition.
- The success criterion separate from admission (operative dependence and robust improvement), the evidence status, the five hazards and the stated failure condition for the bet.

Each item is either a separate claim, a boundary case or a failure condition, so the note is not over-complex for its content.
