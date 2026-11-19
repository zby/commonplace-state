---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/skillrl-evolving-agents-recursive-skill-augmented-rl.md"
source_has_frontmatter: true
date: "2026-06-30"
depth: standard
---

# Connection Report: SkillRL

**Source:** [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.md)

## Discovery Trace

**Collection rules read:** `kb/sources/COLLECTION.md` authorizes source ingest reports to link to `notes`, `sources`, `agent-memory-systems`, and `agentic-systems`, while snapshots themselves remain immutable. The active authored surface for this snapshot is the adjacent ingest report.

**Curated heads:**
- Read `kb/notes/README.md` -- central thread is deploy-time learning, distillation, constraining, and discovery.
- Read `kb/reference/README.md` -- no strong shipped-system target; reference hits were rejected as mostly about Commonplace operation rather than SkillRL's source claim.
- Read `kb/agent-memory-systems/README.md` -- directed search toward trace-derived learning systems, code-grounded reviews, and the comparison survey.
- Read `kb/agentic-systems/README.md` -- no strong whole-harness target beyond memory-system coverage.
- Checked for `*academic-paper*README.md` in allowed destination roots -- none found.

**Description listing scan:**
- `rg -n "^description:.*(skill|Skill|trajectory|Trajectory|memory|Memory|learning|Learning|distill|Distill|adapt|Adapt|reinforcement|Reinforcement|trace|Trace|experience|Experience|procedural|retained)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`
  - Kept candidates: `notes/distillation-is-transformation-not-selection.md`, `notes/raw-accumulation-does-not-create-usable-memory.md`, `notes/deploy-time-learning-is-the-missing-middle.md`, `notes/continual-learning-open-problem-is-behaviour-not-knowledge.md`, `notes/memory-management-policy-is-learnable-but-oracle-dependent.md`, `notes/agent-memory-requirements/use-trace-derived-extraction.md`, `notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md`, `agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md`, `agent-memory-systems/reviews/agent-workflow-memory.md`, `agent-memory-systems/reviews/SkillWeaver.md`, `agent-memory-systems/reviews/amazon-science--SAGE.md`, and neighboring source ingests.
  - Rejected broad hits: many generic memory-system reviews because they are trace-derived but do not specifically convert trajectories into reusable skills or co-train policy use of those skills.

**Body search:**
- `rg -n "SkillRL|SkillOpt|skill library|skill bank|agent skills|trajectory|trajectories|failure lessons|raw trajectories|GRPO|reinforcement learning|memory-augmented RL|trace-derived|procedural memory|experience transfer|context bloat|token compression" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`
  - Kept `sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md` because SkillOpt is the closest prose-skill optimization contrast.
  - Kept `sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md` because SkillRL's abstracted skills challenge the "condensed experience is inert" warning only if policy training makes the condensation causally used.
  - Kept `sources/agent-workflow-memory.ingest.md` and `sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md` because both distill trajectories into future prompt guidance with task-success oracles.
  - Kept `sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` because AgeMem is the weight-policy counterpart: same oracle dependency, different retained artifact.
- `rg -n "^tags:.*(agent-memory|memory|learning|skill|context-engineering|retained-adaptation|deploy-time-learning|trace-derived)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`
  - Confirmed the candidate note cluster and many trace-derived system reviews; rejected tag-only matches without a specific SkillRL articulation.
- `rg -n "coevol|co-evol|skill bank|skill library|readable.*weight|weights.*skill|policy.*skill|substrate coevolution|prose.*parametric" kb/notes kb/sources kb/agent-memory-systems --glob '*.md'`
  - Kept `notes/treat-continual-learning-as-substrate-coevolution.md` as the best theory target for SkillRL's hybrid readable skill bank plus policy-weight loop.
  - Rejected generic "representational form" matches where the hit only listed forms without discussing co-evolution or skill learning.

**Link following:**
- From `skillopt-executive-strategy-self-evolving-agent-skills.ingest.md`, followed links to `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, `deploy-time-learning-is-the-missing-middle.md`, `diagnostic-richness-constrains-outer-loop-learning-quality.md`, and `use-trace-derived-extraction.md`.
- From `agentic-memory-learning-unified-long-term-and-short-term.ingest.md`, followed to `memory-management-policy-is-learnable-but-oracle-dependent.md`.
- From `agent-memory-systems/README.md`, followed to `trace-derived-learning-techniques-in-related-systems.md` and system reviews for Agent Workflow Memory, SkillWeaver, and Amazon Science SAGE.

## Connections Found

- [Distillation is transformation, not selection](../../../notes/distillation-is-transformation-not-selection.md) -- **evidence**: SkillRL is a trace-to-skill example where trajectories are not shortened into smaller traces but transformed into reusable skill objects with names, principles, and applicability conditions.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **evidence**: SkillRL explicitly contrasts raw trajectory memory with skill-bank ingress work: success patterns and failure lessons are shaped into structured, retrievable heuristics before reuse.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**: the recursive skill-bank update is durable cross-run behavior change through an artifact-like library, while policy training supplies a second adaptation path.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**: SkillRL targets behavior change, not passive recall; skills are prompt-visible policy objects and GRPO trains the agent to use them.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **evidence**: SkillRL is a concrete prose-plus-distributed-parametric coevolution loop: a natural-language skill bank evolves while policy weights are optimized around skill retrieval and use.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **compares-with**: both AgeMem and SkillRL use task-completion rewards and GRPO-style training; AgeMem learns memory-operation policy in weights, while SkillRL learns skill-using policy around a readable skill bank.
- [Use Trace-Derived Extraction As Meta-Learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) -- **evidence**: SkillRL mines successes and failures into future behavior-shaping skills and uses validation failures to evolve the library.
- [Trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) -- **evidence**: SkillRL does not grant raw captured trajectories immediate rule authority; it distills, retrieves, trains, and re-validates, providing a concrete maturation chain.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **evidence**: SkillRL uses success/failure trajectories, failure-mode analysis, validation categories, and skill-growth history rather than scalar rewards alone.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: the paper reports trajectory-to-skill compression and lower prompt length than raw-memory baselines while improving behavior.
- [SkillOpt ingest](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) -- **compares-with**: both optimize agent skills from rollout evidence; SkillOpt edits one readable skill with held-out validation, while SkillRL grows a hierarchical skill bank and trains model weights to use it.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers ingest](../../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with**: that paper warns that condensed experience may be behaviorally inert; SkillRL's cold-start SFT plus GRPO makes skill use part of the policy-learning loop, potentially addressing the activation gap.
- [Agent Workflow Memory ingest](../../../../sources/agent-workflow-memory.ingest.md) -- **compares-with**: both distill trajectories into reusable procedural guidance; SkillRL adds failure-derived lessons, hierarchical retrieval, and weight training around skill use.
- [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- **compares-with**: both extract reusable guidance from successful and failed trajectories; SkillRL differs by coupling the artifact library to RL policy optimization.
- [Agentic Memory ingest](../../../../sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md) -- **compares-with**: both are oracle-dependent RL memory systems; AgeMem learns when to call memory operations, while SkillRL learns from and with distilled skill artifacts.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- **evidence**: SkillRL belongs in the survey's trace-to-skill / trace-to-policy region and sharpens the mixed prose-plus-parametric form.
- [Agent Workflow Memory review](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) -- **compares-with**: AWM is the prose workflow baseline for successful-trajectory distillation; SkillRL is the skill-bank plus policy-training variant.
- [SkillWeaver](../../../../agent-memory-systems/reviews/SkillWeaver.md) -- **compares-with**: SkillWeaver crosses from trajectories to executable Playwright APIs, while SkillRL stays in natural-language skill guidance plus policy learning.
- [Amazon Science SAGE](../../../../agent-memory-systems/reviews/amazon-science--SAGE.md) -- **compares-with**: SAGE is the closest code-grounded cousin: AppWorld trajectories become executable skills, SFT data, and GRPO reward signal; SkillRL uses natural-language skills over ALFWorld/WebShop/search tasks.

## Bidirectional Candidates

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source -- **evidence**: the note should eventually cite SkillRL as a prose-plus-parametric coevolution instance if the claim is promoted.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) <-> source -- **evidence**: the survey should eventually place SkillRL beside AWM, SkillWeaver, SAGE, AgeMem, and TIMG.

## Reverse-edge Candidates

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -> source -- **evidence**: cite SkillRL if adding a concrete example of prose skill-bank and policy-weight coevolution.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -> source -- **compares-with**: add SkillRL as a contrast to AgeMem's opaque learned memory-operation policy.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -> source -- **evidence**: add SkillRL to the survey's trace-derived catalog once this source is ingested.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- rejected: title collision on "skills"; the note is about harness skill packaging, not learned agent skills as behavioral memory.
- [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -- weak: SkillRL supports skill distillation broadly, but its source is task trajectories rather than methodology-to-instruction derivation.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- weak outbound candidate: SkillRL is more a possible remedy than direct evidence for the failure. The self-evolver faithfulness paper remains the stronger evidence target.
- `kb/reference/*` shipped-system docs -- rejected: useful for operating Commonplace but not for interpreting SkillRL's scientific contribution.
- Broad trace-derived reviews such as Voyager, OS-Copilot, ExpeL, ReasoningBank, and Dynamic Cheatsheet -- rejected for this report to avoid a related-system spray; the retained system-review candidates are the ones that most directly clarify trajectory-to-skill form.

## Index Membership

- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- SkillRL should be added as a source-backed mixed prose-plus-parametric trace-derived learning instance.

## Synthesis Opportunities

SkillRL plus SkillOpt, AgeMem, AWM, SkillWeaver, SAGE, and TIMG imply a higher-order claim not yet named cleanly: **skill banks can couple readable-artifact and policy-weight learning loops**. The key distinction is whether trajectories become prompt prose, executable tools, learned memory policy, or a hybrid skill library that trains the policy to use the readable artifact.

## Maintenance Observations

None

## Flags

- Split candidate: the source has at least three independent claims (trajectory-to-skill distillation, hierarchical retrieval/context efficiency, and policy/skill-bank coevolution). The ingest report should prioritize the coevolution and distillation value rather than promoting all findings at once.
