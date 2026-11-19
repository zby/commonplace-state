---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/artifacts-as-memory-beyond-agent-boundary.md"
source_has_frontmatter: true
date: "2026-06-30"
depth: standard
---

# Connection Report: Artifacts as Memory Beyond the Agent Boundary

**Source:** [Artifacts as Memory Beyond the Agent Boundary](../../../sources/artifacts-as-memory-beyond-agent-boundary.md)

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- flagged notes in the agent-memory, artifact-analysis, deploy-time-learning, and evaluation clusters. Kept `designing-agent-memory-systems.md`, `agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`, `agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md`, `agent-memory-requirements/evaluate-memory-by-effects.md`, and `information-value-is-observer-relative.md`; rejected broad runtime/context notes unless they needed the source's specific environment-as-memory mechanism.
- Read `kb/notes/tags-README.md`, `kb/notes/agent-memory-README.md`, `kb/notes/artifact-analysis-README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/reference/README.md`, and `kb/agent-memory-systems/README.md`. The curated heads route the source mainly to agent-memory theory and source-to-source comparison, not shipped-system reference.

**Topic indexes:**
- `agent-memory-README.md` pointed to [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) as the main synthesis.
- `artifact-analysis-README.md` pointed to [Retained artifact](../../../../notes/definitions/retained-artifact.md), [Axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md), and [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). The paper's "artifact" term is adjacent but not identical to the KB's retained-artifact vocabulary.
- `deploy-time-learning-README.md` pointed to [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md). These are relevant by analogy, but the source is more directly about environment-side memory capacity than prose/symbolic deploy-time artifacts.

**Body search:**
- `rg -n "externalized memory|external memory|externaliz.*memory|environment.*memory|memory.*environment|agent boundary|artifactual environment|artifacts.*past" kb/notes --glob '*.md'` -- found sparse direct prior coverage. Kept [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) and [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) because they define memory by behavior-changing capacity rather than storage location.
- `rg -n "fixed agent|adapt.*environment|environment.*adapt|tool adaptation|T2|substrate coevolution|co-evolve|coevolve" kb/notes kb/sources --glob '*.md'` -- kept [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md), which already names the fixed-agent / adapted-environment pattern. The source gives a primary formal and empirical instance rather than another taxonomy.
- `rg -n "capacity.*memory|memory.*capacity|capacity.*environment|context efficiency|effect(s)?" kb/notes/agent-memory-requirements kb/notes --glob '*.md'` -- kept [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) because the paper defines externalized memory by capacity and performance deltas rather than by the mere presence of an external store.
- `rg -n "RL|reinforcement learning|environmental artifact|spatial path|externalized memory|memory management policy|AgeMem" kb/agent-memory-systems kb/sources --glob '*.md'` -- kept [AgeMem](../../../../agent-memory-systems/lightweight/agemem.md) as a comparison candidate, but lower priority: AgeMem learns a memory-management policy; this source studies an environment-side memory substrate exploited by RL agents.

**Link following:**
- From [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md), followed [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md), [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md), and [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md). These support the broader cluster, but the source most directly reinforces effect-based memory and crosscutting substrate claims.
- From [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md), followed its T2 reading dictionary. The paper is a concrete case of memory improving a fixed agent through the surrounding environment, but it also exposes a boundary: the environment artifact is not necessarily authored, durable, or governed like a KB artifact.

## Connections Found

- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) -- **evidence**: the source supplies a formal and experimental instance of the note's "fixed agent, adapted surrounding substrate" pattern, with environmental artifacts reducing memory/capacity requirements.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **evidence**: the paper shows memory effects arising from the interaction among environment state, observation channel, learning policy, and task performance rather than from a standalone memory module.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- **evidence**: the paper operationalizes externalized memory by reward and capacity comparisons across artifactual and artifactless settings, matching the note's effect-based evaluation criterion.
- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -- **evidence**: the source corroborates the design note's behavior-first boundary for memory: retained or environmental material matters when it changes downstream capacity under bounded agent conditions.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -- **evidence**: the paper's artifact definition depends on what an agent can infer from an observation about its past under a particular interface and history, giving a bounded-agent case of information value depending on observer and task.
- [Adaptation of Agentic AI ingest](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) -- **compares-with**: the survey names the T2/fixed-agent tool-adaptation category; this source develops one primary environment-as-memory instance with proofs and experiments.
- [Memory Scaling for AI Agents ingest](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) -- **compares-with**: both sources argue external memory can improve agent performance, but Databricks emphasizes retrievable/distilled enterprise memory while this paper emphasizes situated environmental artifacts and observation history.

## Bidirectional Candidates

- [AgeMem](../../../../agent-memory-systems/lightweight/agemem.md) <-> source -- **compares-with**: both are RL-adjacent memory papers evaluated by downstream task performance, but AgeMem learns a policy over explicit memory operations while this source studies task environments whose artifacts reduce internal capacity needs.

## Reverse-edge Candidates

- [The adaptation survey corroborates memory requirements but misses artifact governance](../../../../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) -> source -- **evidence**: the note should cite this source as a concrete, primary environment-side memory case for the T2/fixed-agent reading.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -> source -- **evidence**: the paper is direct evidence for evaluating memory by behavioral and capacity effects rather than artifact existence.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -> source -- **evidence**: the paper's memory effect crosses substrate, context/observation, and learning, making it a strong non-storage example.
- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -> source -- **evidence**: the paper supports the design note's behavior-changing-capacity boundary for memory and adds a formal RL vocabulary for that boundary.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -> source -- **evidence**: the artifact-reduction theorem is a formal case where the same observation has different value depending on the observer's interface, task, and history.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- rejected as a direct connection: the paper's "capacity" is RL representational/input capacity, not LLM context-window capacity. It may be useful background for the ingest summary, but a direct evidence link would blur two mechanisms.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- rejected as a primary link: the source discusses agent-environment coevolution as an implication, but the note's main claim is about coevolution among distributed-parametric, prose, and symbolic representational forms.
- [Retained artifact](../../../../notes/definitions/retained-artifact.md) -- rejected as a direct candidate unless the ingest report uses the KB term. The paper's "artifact" is an observation that informs the past; the KB's "retained artifact" is any retained state later consumed in a behavior-shaping way.
- `kb/reference/` candidates -- rejected after reading `kb/reference/README.md` and `kb/reference/COLLECTION.md`: this source does not describe the shipped Commonplace system or directly inform a built design choice.
- `kb/agentic-systems/` candidates -- rejected after scanning descriptions: this source is about a formal memory mechanism in RL environments, not a whole external harness or execution loop.

## Index Membership

- [Agent memory](../../../../tags/agent-memory-README.md) -- if promoted into a note, the source's synthesis belongs in the agent-memory cluster because it sharpens the memory boundary around behavior-changing environment artifacts.
- [Learning theory](../../../../tags/learning-theory-README.md) -- if promoted into a note, the source contributes to learning as durable capacity change and effect-based evaluation, but only through the agent-memory child area.

## Synthesis Opportunities

- The source plus existing memory-requirement notes imply a candidate note: **External memory is an agent-environment relation, not a storage location.** It would argue that memory can live in environment-side artifacts when the agent's interface and policy can exploit them to reduce internal representational burden; storage substrate is only one implementation.
- The source also suggests a boundary refinement: **not every behavior-shaping environmental artifact is a governed retained artifact.** A trail, landmark, or path can function as memory without lineage, authority, provenance, or lifecycle governance; KB memory systems add those governance properties when the artifact is meant to be maintained across future agent work.

## Maintenance Observations

None

## Flags

- Split candidate for promotion: one possible note is the general agent-environment memory boundary, while a second narrower note could distinguish situated environmental artifacts from governed KB retained artifacts.
