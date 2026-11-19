---
description: "Discovery report for possible KB connections from the Co-Harness paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/co-harness-co-evolving-harness-and-model-weights.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents

**Source:** [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../sources/co-harness-co-evolving-harness-and-model-weights.md)

## Discovery Trace

**Curated heads and complete title surfaces:**

- Read `kb/notes/learning-theory-README.md`, `kb/notes/deploy-time-learning-README.md`, and `kb/notes/context-engineering-README.md`; these routed the source to representational-form coevolution, diagnostic richness, and the localized-artifact learning loop.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The reference collection had no plausible shipped-system target, while the two external-system heads identified Meta-Harness and Agentic Harness Engineering as comparison context.
- Ran fresh full-title listings with `rg -N --no-heading -m1 '^# '` over each authorised local destination: 317 note titles, 124 reference titles, 171 agent-memory titles, 8 agentic-system titles, and 397 source titles. Candidate titles were filtered by `harness|model|weight|learning|trajectory|scaffold|training|feedback|failure|distill|context|tool`.

**Description listing scan:**

- `rg '^description:' kb/notes --glob '*.md' | rg -i 'representational|continual learning|outer-loop|scaffolding|harness|trajectory|failure|validation radius'` retained [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md).
- Equivalent description scans over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` retained the Meta-Harness and SkillRL analyses as comparison cases. Reference hits concerned Commonplace's own review harness or model partitions and were rejected as a scope mismatch.

**Body search:**

- `rg -n -i 'joint optim|co.?evol|weights.*harness|harness.*weights|distributed-parametric.*symbolic|parametric.*natural-language|fine-tun.*trajector|distill.*weights|cross-class credit' kb/notes --glob '*.md'` found that Co-Harness directly instantiates the joint-loop possibility posed by the coevolution note and challenges the readable-artifact note's statement that distributed-parametric plus symbolic has no clean instantiation.
- `rg -n -i 'co.?evol|harness.*weight|weight.*harness|fine-tun.*trajector'` over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` found no stronger local target than the theory notes; Agentic Harness Engineering and Meta-Harness keep weights fixed and therefore serve only as comparison cases.
- `rg -n -i 'co.?evol|harness.*weight|weight.*harness|fine-tun.*trajector' kb/sources --glob '*.ingest.md'` retained SkillRL, Meta-Harness, Language-model harnesses are compositional generalizers, and The Anatomy of an Agent Harness. SkillRL is the nearest natural-language-plus-parametric loop; Meta-Harness is the nearest fixed-weight harness optimizer; the compositional-generalizer paper trains weights under a fixed harness; the practitioner essay supplies an overfitting warning rather than a demonstrated learning loop.

**Link following:**

- Followed the coevolution note to the readable-artifact loop, continual-learning behavior split, deploy-time learning, and representational-form definition. The source fills the joint-optimizer gap while also exposing the existing note's pace-mismatch and cross-class-credit-assignment concerns.
- Followed diagnostic richness to Meta-Harness and Agentic Harness Engineering. Co-Harness uses structured failure attribution and local diffs, but does not ablate trace richness, so it supports the mechanism as an instance rather than supplying controlled evidence for the general claim.
- Followed the SkillRL ingest and the fixed-harness compositional-generalizer ingest. These separate the source's novelty: SkillRL coevolves natural-language skills with weights; the fixed-harness paper distills harness-enabled behavior only into weights; Co-Harness keeps localized harness artifacts and distributed-parametric weights as continuing alternating learning targets.

## Connections Found

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: Co-Harness is a concrete automated loop spanning distributed-parametric weights and a mixed natural-language/symbolic harness, precisely the cross-form coevolution the note frames as the open problem.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: accepted localized harness patches are versioned, regression-checked, and rolled back within a bounded patch locus while the following weight update retains a wider behavioral validation radius; the source also qualifies the note's claim that distributed-parametric plus symbolic lacks a clean instantiation.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: HarnessCritic turns full failure trajectories into explicit root cause, locus, severity, evidence, and diff suggestions before proposal aggregation, exemplifying structured diagnostic evidence as the proposer substrate.
- [Ingest: SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- **compares-with**: both alternate artifact updates with weight learning from trajectories, but SkillRL evolves natural-language skills while Co-Harness can patch prompts, tool schemas, skills, middleware, and memory across both localized forms.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: both use trace-grounded agents to revise harness artifacts under benchmark validation, but Meta-Harness freezes weights while Co-Harness deliberately feeds improved-harness trajectories into the next model update.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source -- **evidenced-by**: the paper supplies the concrete automated mixed-form loop currently missing from the note's inventory.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- **evidenced-by**: the paper both tests the note's validation-radius distinction and falsifies its point-in-time statement that distributed-parametric plus symbolic has no clean instantiation.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source -- **evidenced-by**: the paper provides a second structured trace-to-root-cause-to-local-diff instance, though not a diagnostic-richness ablation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- too foundational to gain useful traversal beyond the more precise representational-form coevolution note.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- the harder-benchmark gains are compatible with its frontier claim, but three math benchmarks and two model sizes do not test model generations or deployment reassignment.
- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) -- keyword overlap around structured gains is misleading; Co-Harness changes rollout quality through harness repair rather than isolating an inference-time training-distribution-selection mechanism.
- [Agent runtimes decompose into scheduler, context engine, and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- the paper's five-tuple can be mapped onto the decomposition, but that architectural restatement adds less than the learning-loop links.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- the comparison is already captured more directly by the source's discussion and the Meta-Harness comparison; a second broad system-review edge would duplicate it.

## Index Membership

None

## Synthesis Opportunities

- Co-Harness, SkillRL, and the fixed-harness compositional-generalizer result together support a sharper mixed-form distinction: a harness can merely shape a weight-training distribution, or it can remain a separately retained and revised learning target. Only the latter is genuine representational-form coevolution, and it introduces cross-form credit assignment, compatibility, rollback, and validation-radius questions that a one-way distillation account hides.

## Maintenance Observations

- The coevolution note says automated distributed-parametric-plus-natural-language coupling is missing, and the readable-artifact note says distributed-parametric plus symbolic has no clean instantiation. SkillRL already qualifies the first statement, and Co-Harness now qualifies both; these are point-in-time factual claims worth revising when the workshop promotes its central synthesis.

## Flags

- The evidence is a July 2026 arXiv v1 preprint with no independent reproduction located in this repo. Treat the reported gains and autonomous-run claims as provisional.
