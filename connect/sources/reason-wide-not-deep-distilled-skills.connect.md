---
description: "Discovery report for possible KB connections from Reason Wide, Not Deep"
type: kb/cache/types/connect-report.md
source: "kb/sources/reason-wide-not-deep-distilled-skills.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Reason Wide, Not Deep

**Source:** [Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../../sources/reason-wide-not-deep-distilled-skills.md)

## Discovery Trace

**Source and authorization:**

- Read the snapshot in full, `kb/sources/COLLECTION.md`, and the connect-report type. The snapshot is immutable; its future `.ingest.md` is the authored outbound surface. The source collection authorizes prospecting in notes, reference, agent-memory-systems, agentic-systems, and sources; it excludes work and instructions.
- Because the paper is experiment-bearing, read [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) before settling candidates. The effective update-space analysis is recorded under Flags.

**Curated heads:**

- Read `kb/notes/README.md` and `kb/notes/tags-README.md`; the deploy-time-learning, artifact-analysis, context-engineering, and agent-memory clusters were plausible. The source has no `tags:` field, so no matching tag README or by-tag `rg` pass applied.
- Read `kb/reference/README.md`; no shipped-system component directly depends on this new paper.
- Read `kb/agent-memory-systems/README.md`; its trace-learning survey and lightweight-coverage path were direct prospects.
- Read `kb/agentic-systems/README.md`; the paper describes a trace-to-skill subsystem, not a whole harness, so this destination was rejected after the title/body pass.
- Read `kb/sources/README.md`; close paper ingests were evaluated as comparisons rather than as a broad source-to-source map.

**Complete title scans:**

- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — 349 titles. Kept the crystallized-reasoning, frontloading, deploy-time constraining, trace-extraction, episode/rule, and fixed-decomposition candidates; rejected generic reasoning and prompt notes.
- The same complete scan over `kb/reference/` (132 titles) found only terminology and trajectory-evaluation proposals, not a direct shipped-system connection.
- The same complete scan over `kb/agent-memory-systems/` (172 titles) found the trace-learning survey, Trajectory-Informed Memory Generation, Agent Workflow Memory, ExpeL, SkillRL, and related systems. The survey and the two closest system shapes were followed; the rest were filtered as duplicates or weaker comparisons.
- The same complete scan over `kb/agentic-systems/` (11 titles) found no system-level target.
- The same complete scan over `kb/sources/` (473 titles) found the self-evolver faithfulness, SkillOpt, SkillRL, Agent Workflow Memory, and Trajectory-Informed Memory Generation ingests as the closest captured comparisons.

**Description and body searches:**

- `rg -n -i '^description:.*(distill|trajector|trace|experien|amortiz|prompt|reason|procedur|skill|failure|reus|frontload|codif)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` — promoted direct descriptions and exposed the existing trace-learning casebook.
- `rg -l -i 'passive skill|distilled (skill|rule)|reasoning premium|reasoning mode|trajectory.{0,60}(rule|skill|procedure)|system prompt|frontload' kb/notes --glob '*.md'` — kept the six note candidates below; rejected broad context and generic prompt hits.
- `rg -l -i 'passive skill|distilled (skill|rule)|reasoning premium|reasoning mode|trajectory.{0,60}(rule|skill|procedure)|system prompt|offline.{0,40}distill' kb/agent-memory-systems --glob '*.md'` — kept the trace-learning survey and the closest paper/code-reviewed counterparts.
- The same query over `kb/sources/ --glob '*.ingest.md'` — kept the behavioral-faithfulness tension and the passive-versus-optimized skill comparison; SkillRL remains a useful secondary comparison.
- The same query over `kb/agentic-systems/` and `kb/reference/` — no candidate passed the articulation test.

**Link following and candidate evaluation:**

- Followed the neighborhoods of [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md), [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md), [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md), [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md), and the fixed-decomposition note. These establish distinct reader needs: evidence for precomputed instruction artifacts, a trace-to-rule workflow, and a boundary on what the experiments test.
- Followed [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) through its Trajectory-Informed, Agent Workflow Memory, ExpeL, and SkillRL sections. The paper adds a distinct trajectory-run pattern: one offline coding-agent pass produces one model/domain-specific Markdown skill, with no runtime retrieval or weight update.
- Compared [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md), [SkillOpt](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md), [Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md), [Trajectory-Informed Memory Generation](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md), and [SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md). The first supplies the material tension; SkillOpt supplies the cleanest optimization contrast. The other three are useful casebook context but redundant as durable outbound edges once the trace-learning survey is linked.

## Connections Found

- [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — **is-evidence-for**: the paper operationalizes the note's mechanism by compiling recurring domain procedure into a compact system-prompt artifact and measuring the reasoning-token work it displaces.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) — **is-evidence-for**: passive skill distillation computes from already-available training trajectories before later calls, then inserts the result so each deployment episode avoids re-deriving shared procedure.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) — **is-evidence-for**: a frozen model's behavior improves through a retained natural-language system-definition artifact rather than a weight update.
- [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) — **is-evidence-for**: the coding agent performs batch analysis over successes, failures, loops, tool errors, and repeated action patterns, then promotes a rule artifact for future behavior.
- [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — **compares-with**: the method derives a rule layer from retained trajectories and even embeds corpus statistics in rules, but the paper does not establish durable item-level lineage or episode fallback after deployment.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **rests-on**: the reported gains occur inside a fixed trajectory representation, Markdown-skill hypothesis class, system-prompt injection surface, harness, action basis, and benchmark partition; the result does not select those surrounding choices.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — **is-evidence-for**: the paper adds empirical evidence for trajectory-run readable-artifact learning and a low-cost, one-pass, always-pushed skill variant not yet represented in the survey.
- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) — **compares-with**: both turn completed trajectories into natural-language procedure for a frozen acting model, but this paper compiles one domain skill with no runtime retrieval while TIMG extracts and retrieves granular tips.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: that study finds many condensed memories behaviorally inert, whereas this paper's with/without-skill results show a compact, failure-derived instruction changing outcomes; the difference motivates a specificity-and-activation hypothesis rather than resolving it.
- [SkillOpt](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) — **compares-with**: both deploy compact natural-language skills around frozen models, but passive distillation uses one corpus-analysis pass without fresh rollouts while SkillOpt iteratively edits and validation-selects a skill from scored rollouts.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) → source — **evidenced-by**: the paper is a direct measured case of replacing recurring read-time reasoning with write-time heuristic instruction.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) → source — **evidenced-by**: the reported one-time distillation cost and recurring output-token reductions instantiate the note's economic frontloading claim.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) → source — **evidenced-by**: the held-out improvements show durable prompt-side capacity change without weight updates.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) → source — **evidenced-by**: a future survey update can cite this snapshot for the passive skill-distillation case and its reported ablations.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — rejected: it concerns critique-system process validity, not the cost or reuse of acting-model reasoning.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rejected: the paper measures output-token economics and task success, not effective-window degradation; the narrower frontloading connection carries the useful claim.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — rejected: model/domain-specific skills acknowledge a boundary, but the paper does not test boundary-statability against a rival abstraction rule.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — rejected as a direct outbound edge: it is a genuine comparison, but the trace-learning survey already frontloads that system-level context and avoids a redundant case inventory.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — rejected: both use trajectories, but the proposal concerns how Commonplace should judge workflow transformation, not how a skill is distilled or deployed.
- `kb/agentic-systems/` — rejected as a destination: the paper does not describe a whole execution harness or orchestration surface, only a skill-learning subsystem around fixed harnesses.

## Index Membership

- [Lightweight agent memory systems](../../../../agent-memory-systems/lightweight/README.md) — after a doc-grounded review is written, passive skill distillation belongs in the lightweight roster as a paper-backed trajectory-to-skill system.

## Synthesis Opportunities

- The positive with/without-skill results here and the condensed-memory failures in [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) suggest a discriminating experiment: hold task, model, and prompt budget fixed while varying generic summaries versus concrete failure-derived rules with explicit actions and corpus frequencies. The present papers do not isolate whether action specificity, behavioral authority, corpus-wide recurrence, or some other bundled choice explains the different uptake.

## Maintenance Observations

None.

## Flags

- **Fixed-decomposition boundary:** the distiller can condition on recorded observations, actions/tool calls, visible outputs, rewards, pass rates, and—only in the paired ablation—reasoning traces. It can compose corpus statistics, failure contrasts, loop detection, and a 40–130-line natural-language skill. Its effective hypothesis class is model/domain-specific procedural guidance expressible in that fixed prompt artifact. The trajectory schema, chosen corpus and split sizes, distiller model/prompt, one-shot skill granularity, system-prompt insertion point, acting-model tools/actions, harness, task partition, and benchmark oracle remain fixed outside that update space.
- **Ablation limit:** the corpus-source ablation varies no-think-only versus paired think/no-think evidence. It supports the narrow claim that reasoning traces are not required in these domains; it does not validate the neighboring fixed representation, distiller, skill format, or decomposition as a whole. Distillation variance is unmeasured because each skill is produced once.
