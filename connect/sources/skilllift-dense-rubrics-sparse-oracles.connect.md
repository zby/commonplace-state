---
description: "SkillLift connects oracle-calibrated textual rubrics to diagnostic guidance and ranking supervision, while bounding claims by task-specific search and selected cost crossings."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/skilllift-dense-rubrics-sparse-oracles.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: SkillLift

**Source:** [SkillLift snapshot](../../../../sources/.snapshots/skilllift-dense-rubrics-sparse-oracles.md)

## Discovery Trace

Read the full retained paper in consecutive ranges, including prompts, ablation tables, token accounting and both cases. Source/report and notes contracts loaded. Reused the batch's curated heads and fresh complete title surfaces across all five permitted destinations; no source tags.

- Notes: description query `surrogate|oracle|rubric|rank|selection|holdout` found diagnostic richness, warranted autonomy, and the pairwise-comparison experimental plan. Read all three fully, including their outgoing relations. Their oracle-spectrum and learned-memory-policy neighbors were already inspected in this batch. Kept guidance versus selection, local oracle domain, and a bounded comparison of supervision targets.
- Reference: body query `SkillLift|rubric.*oracle|oracle.*rubric|Kendall|surrogate.*rank` returned no candidate.
- Agent-memory-systems: the same query returned no candidate. Existing code analyses are not evidence for this paper's empirical results.
- Agentic-systems: the same query returned no candidate.
- Sources: the query found the pairwise-judging post, On the Fragility of Self-Improving Agents and several broader benchmark discussions. Read the pairwise post fully through the experimental plan's conceptual lineage; its unsupported oracle-hardening claim is not interchangeable with SkillLift's ranking-alignment ablation. Kept the experimental plan as the narrower destination instead of an extra source edge. Other matches concern different interventions.
- Paths checked; inbound reader needs assessed under notes rules. No external prospecting; work and instructions excluded.

## Connections Found

- [Diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: criterion hits guide cheap skill revision, while executed outcomes select the champion and recalibrate the rubric. The no-rubricator ablation leaves dense feedback present but weakens results, showing the importance of calibrating that guidance in this setup; it does not identify a causal explanation of every candidate's failure.
- [Pairwise-comparison test plan](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — **compares-with**: replacing rank alignment with score regression lowers reported SkillsBench results under an identical oracle budget. This concerns fitting a surrogate to an execution oracle's local ordering; it is not a test of pairwise LLM judgment versus scalar LLM judgment, nor of tournament aggregation or position bias.
- [Warranted autonomy](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — **compares-with**: visible-package checks cheaply guide search, but final selection still consumes execution outcomes. Rank agreement over three current candidates and a cached champion does not validate the rubric on unseen skills or establish that the execution oracle captures every intended task property.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Pairwise-comparison test plan](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) → eventual tracked ingest — **compares-with**: a bounded external example of testing ranking supervision against regression by downstream optimization outcome. Explicitly distinguish the tested learning objective from the note's proposed judge-prompt intervention. Ground quotes or use `(snapshot required)` for source-dependent details.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Ranking alignment proves pairwise judging is generally better: the ablation changes surrogate alignment, not judge prompting.
- Oracle selection can never corrupt final output: cached noisy champion scores and limitations of the oracle remain relevant; the claim only separates surrogate selection from execution selection.
- The seed ablation identifies seed quality: it changes initial population size as well.
- A fixed rubric cannot support successful revision: the TicToc appendix case improves with an unchanged rubric and three successful post-stop trials.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

Task-specific search is evaluated as mean per-task best evolved-skill scores over three rollout seeds; the paper does not establish generalization of a multi-task library. Token-to-quantile comparisons exclude already-solved tasks and tasks that never cross the threshold; Table 7 ratios of 2.13–2.74 imply roughly 53–64% savings for those reported crossings. Baselines have twice the default token budget, and SkillOpt has disabled components and reduced settings. The seed ablation is confounded by population size. Main text permits deleting criteria, while the appendix rubricator forbids removal of positive criteria. The paratransit case illustrates rubric revision; the retained TicToc case expressly does not. Repeated agreement on a small current population is not out-of-sample rubric validation.
