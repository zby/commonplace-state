---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/skillopt-executive-strategy-self-evolving-agent-skills.md"
source_has_frontmatter: true
date: "2026-05-28"
depth: standard
---

# Connection Report: SkillOpt: Executive Strategy for Self-Evolving Agent Skills

**Source:** [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.md)

## Discovery Trace

- Read the sources collection rules and confirmed that the active outbound surface should be the ingest report, not the snapshot.
- Searched `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/sources/` for skill, procedural, text-space, external-state, trajectory, rollout, validation, held-out, rejected-edit, edit-budget, slow-update, optimizer, GEPA, TextGrad, Trace2Skill, and EvoSkill language.
- Followed high-signal hits through the continual-learning, readable-artifact, diagnostic-richness, trace-derived-learning, and skill-synthesis clusters.
- Skipped `kb/work/` per collection rules.

## Connections Found

- [Readable artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **evidence**. SkillOpt is a direct prose-artifact instance of the loop: frozen target model, mutable skill document, scored rollouts, bounded text edits, validation gate, and exported compact runtime artifact.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**. SkillOpt updates durable skill text across training rounds while leaving inference-time weights unchanged, matching deploy-time learning through readable system-definition artifacts.
- [Continual learning open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**. The learned skill is not just stored knowledge; it has instruction authority over future agent behavior.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **evidence**. SkillOpt isolates one substrate class, prose skill state, and shows an update loop that coevolves the external artifact around fixed model and harness substrates.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **evidence**. SkillOpt uses rollout traces, success/failure contrast, rejected edits, and slow/meta updates as diagnostic state for future proposals rather than relying on scalar scores alone.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- **evidence**. SkillOpt's strict held-out validation gate works because the tested domains are resettable and scored; the paper's limitations mark the weaker end of the gradient for subjective/open tasks.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **evidence**. SkillOpt is another oracle-dependent learning loop, but the learned policy is readable skill text rather than a distributed-parametric memory policy.
- [Use trace-derived extraction](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) -- **evidence**. SkillOpt converts execution trajectories into a retained behavior-shaping artifact, with held-out selection and rejected-edit buffers as signal-quality controls.

## Bidirectional Candidates

- [Trajectory-Informed Memory Generation for Enhanced Agentic Reasoning](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- **compares-with**. Both learn from execution trajectories under task-completion oracles; TIMG emits retrieved tips, while SkillOpt edits a single portable skill document with held-out validation.
- [Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md) -- **compares-with**. Both induce procedural text from traces; AWM stores workflow prompt files, while SkillOpt uses bounded edit proposals, rejected-edit memory, and explicit validation selection.
- [Skill Synthesis: Materializing Knowledge as Skills](../../../../sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md) -- **compares-with**. Skill Synthesis derives skills from domain/source corpora; SkillOpt optimizes skills from scored agent rollouts.
- [Improving AI Skills with AutoResearch Evals Skills](../../../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) -- **compares-with**. The practitioner report emphasizes manual comprehension and judge calibration; SkillOpt shows stronger automation in hard-oracle domains while preserving the same evaluator-dependence boundary.
- [Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**. Both optimize readable artifacts around a fixed model from trace/evaluation feedback; Meta-Harness changes code harnesses, while SkillOpt changes compact prose skills.
- [Adaptation of Agentic AI Survey](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) -- **compares-with**. SkillOpt is a clean T2-style case where the fixed agent adapts through external environment/support artifacts rather than weight updates.

## Reverse-edge Candidates

- [Readable artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -> source -- **evidence**. The note can cite SkillOpt as a prose-only readable-artifact loop with empirical validation across multiple task families and harnesses.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -> source -- **evidence**. The note can use SkillOpt as a durable external-artifact learning case that does not update model weights.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -> source -- **evidence**. The note can cite SkillOpt for the role of success/failure traces, rejected edits, and meta strategy in improving outer-loop proposals.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -> source -- **evidence**. The note can cite SkillOpt as a case where resettable, scored tasks make artifact hill-climbing practical.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- related terminology, but the note is about skill packaging and invocation boundaries rather than the training mechanism SkillOpt contributes.
- [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -- related by skill provenance, but SkillOpt is better treated as a contrasting provenance route: trajectory optimization instead of methodology/source distillation.
- [Choosing what to learn requires both validity and learning value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- adjacent, but SkillOpt's held-out performance gate does not clearly separate validity from learning value.
- [Externalization in LLM Agents](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md) -- useful background but too broad for a direct edge from this source.

## Index Membership

- `kb/notes/learning-theory-index.md` -- SkillOpt is useful evidence for deploy-time learning and readable-artifact continual learning.
- `kb/sources/dir-index.md` -- generated source listing should include the new snapshot and ingest report after index refresh.

## Synthesis Opportunities

- Validation-gated skill optimization is readable-artifact learning under a hard-oracle boundary: scored rollouts and held-out validation make prose skills trainable, while subjective/open domains still need human or calibrated model evaluation.
- Skill provenance now has at least three routes in the KB: methodology/source distillation, trace-to-procedure induction, and validation-gated text-space optimization.
- Rejected edits should be treated as retained learning artifacts when optimizing operational instructions; their value is negative evidence that shapes future proposal generation.

## Maintenance Observations

None

## Flags

- The snapshot was captured from arXiv HTML; formulas and some table details may be lossy compared with the PDF.
- The paper spans skill engineering, prompt optimization, agent memory, and continual learning; the strongest KB route is the readable deploy-time learning mechanism, not general skill packaging.
