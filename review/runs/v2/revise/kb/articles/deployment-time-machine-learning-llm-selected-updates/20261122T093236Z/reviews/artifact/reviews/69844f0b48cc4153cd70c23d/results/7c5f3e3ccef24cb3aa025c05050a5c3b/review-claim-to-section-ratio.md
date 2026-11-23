---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/69844f0b48cc4153cd70c23d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 7c5f3e3ccef24cb3aa025c05050a5c3b
completed-at: '2026-11-22T09:33:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 8d1dd854226360932ecaf9c10fc5853f50ff4260fd7f8fb5bf23cb7b640c0920
format: 2
---

# Review

## Summary

The article has an untitled introduction, five argument sections and one navigation section. It carries more distinct non-obvious claims than sections, and each section extends the argument rather than restating it.

## Claims and sections

Distinct non-obvious claims:

1. Selection-based learning needs a comparison, not a single score; a robust comparison over a preference model can select changes without a chosen scalar weighting.
2. The empirical bet: a fixed-weight LLM can build the preference model from a stated purpose and make the robust comparison, including double-loop revision of its criteria.
3. Selection-based learning is distinguished from direct updates (gradient steps, count-triggered writes) by proposal, evaluation and possible rejection, independent of substrate.
4. A readable store buys deployment-time updates, targeted correction and inspection, but at real costs (retrieval, upkeep, unfaithful rationales).
5. Precedents order admission routes as proof, fixed formula and criterion-revising heuristics; the bet places the LLM at the robust-comparison step, with a stated limit on the decision-analysis analogy (open-ended criteria can widen the set).
6. The approach is compatible with the Bitter Lesson because that lesson selects production methods, not representational forms, conditional on learning outgrowing the bootstrap.
7. Improvement must be judged separately from admission, by operative dependence and robust improvement, and open verdicts are decisions, not gains.

Sections and their contributions:

- Introduction: states claims 1 and 2.
- "One change followed through": a worked example that grounds claims 1, 2 and the double-loop step concretely; it is an inference-support unit the later abstractions reference ("as in the routing-line example above").
- "Selection-based learning versus direct gradient training": claims 3 and 4, with boundary cases (AlphaGo Zero vs AlphaZero, engineer-selected checkpoints).
- "Proof, formula, judgment": claim 5 and the operational form of claim 2.
- "Compatible with the Bitter Lesson": claim 6, with the rival-hypothesis evidence and the bootstrap condition.
- "Whether a change improved the system...": claim 7, evidence state and failure modes.
- "Where to go next": navigation, not argument.

The closing "That sequence establishes three things" paragraph in the example section previews later claims, but it ties the example to them rather than repeating a section. No section repeats framing instead of adding substance.
