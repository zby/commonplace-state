---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md"
source_has_frontmatter: true
date: "2026-04-22"
depth: standard
---

# Connection Report: Agents Explore but Agents Ignore

**Source:** [Agents Explore but Agents Ignore](../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md)

## Discovery Trace

**Collection rules:**
- Read [sources collection rules](../../../../sources/COLLECTION.md). Snapshots are immutable and should not receive authored links. Ingest reports and source reviews carry active outbound links. Source-to-note labels authorised there are `evidence`, `derived-from`, `rationale`, `defined-in`, and sparse `see-also`; source-to-source/system labels include `compares-with`.

**Index scan:**
- Read [notes index](../../../notes/dir-index.md). Flagged [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md), [prompt-ablation-converts-human-insight-to-deployable-framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md), [reliability-dimensions-map-to-oracle-hardening-stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [agent-is-a-tool-loop](../../../../notes/agent-is-a-tool-loop.md), [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md), [apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops](../../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md), and [soft-bound-traditions-as-sources-for-context-engineering-strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md).
- Read source-adjacent ingest reports found by body search: [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md), [Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md), [Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), and [EsoLang-Bench](../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming-languages.ingest.md). Kept the first two as strong source comparisons; kept Meta-Harness/EsoLang as synthesis context only.

**Topic indexes:**
- Source frontmatter has `tags: [academic-paper]`. No curated `academic-paper` topic index was found in notes; topic-index discovery proceeded through [evaluation index](../../../notes/evaluation-index.md), [tool-loop index](../../../notes/tool-loop-index.md), and [computational model index](../../../notes/computational-model-index.md) via candidates surfaced from the directory index and body search.

**Body search:**
- `rg -n "curiosity|explor|observation|observations|environment|agent.*environment|open-loop|fixed pattern|adapt|scaffold|tool availability|pass@|process" kb/notes kb/reference kb/agent-memory-systems --glob "*.md"` surfaced the strongest clusters around activation, process constraints, tool-loop capability surfaces, and evaluation.
- `rg -n "benchmark|evaluation|metric|task success|outcome|process|trajectory|agent.*reliability|agent.*benchmark" kb/notes kb/reference kb/agent-memory-systems --glob "*.md"` surfaced the reliability/oracle cluster and source comparisons.
- `rg -n "environmental curiosity|solution injection|discovery@|interaction@|agents ignore|open-loop sequence|observations as potential reasons|revise their strategy|unexpected.*relevant|act on information|tool availability" kb/notes kb/sources kb/agent-memory-systems --glob "*.md"` found no existing note using the paper's exact vocabulary; all matches were the new snapshot.
- `rg -n "pass@k|pass@|task success|benchmark.*oracle|clear oracle|process-oriented|outcome-driven|task completion|agent reliability|discrimination" kb/notes kb/sources kb/agent-memory-systems --glob "*.md"` connected the paper to agent reliability and oracle-strength notes because solution injection separates task success from process adaptation.
- `rg -n "scaffold|tool.*surface|tool suite|function-calling|bash-only|str_replace|hidden scheduler|framework-owned tool loop|tool loops" kb/notes kb/reference kb/agent-memory-systems --glob "*.md"` connected the tool-availability result to capability-surface notes, but rejected several framework-loop notes as too broad.

**Link following:**
- Followed [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) to [elicitation-requires-maintained-question-generation-systems](../../../../notes/elicitation-requires-maintained-question-generation-systems.md), [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), and [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md). Kept it as a sibling mechanism, not the main target: that note is about activating stored model/KB knowledge, while this source is about integrating information already present in live context.
- Followed [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) to [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) and [agentic-systems-interpret-underspecified-instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md). Kept process-structure because the paper tests exploration/reflection instructions as process constraints.
- Followed [tool-loop index](../../../notes/tool-loop-index.md), [agent-is-a-tool-loop](../../../../notes/agent-is-a-tool-loop.md), and [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md). Kept `agent-is-a-tool-loop`; rejected dynamic-tool-removal/loop-exposure as adjacent but not the paper's core claim.

## Connections Found

- [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **evidence**: the paper provides a sharp case of silent ignored context: an injected solution can be present in the live observation stream while the output remains coherent and task-directed. It extends the note's "ignored context" phenomenon, though the mechanism here is not primarily long-context volume.
- [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: exploration/reflection prompts improve interaction and pass rates because they constrain the agent's process, not the final answer shape.
- [prompt-ablation-converts-human-insight-to-deployable-framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- **evidence**: the paper's prompt variations are a benchmark-scale version of testing which framings trigger a desired cognitive move, here noticing and investigating unexpected environmental evidence.
- [reliability-dimensions-map-to-oracle-hardening-stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) -- **evidence**: solution injection adds a process-oriented reliability metric (`interaction@k`) showing that mean task success cannot distinguish adaptive observation-grounded behavior from rigid plan execution.
- [agent-is-a-tool-loop](../../../../notes/agent-is-a-tool-loop.md) -- **evidence**: the paper's scaffold/tool-suite ablations support the convention that prompt plus capability surface materially defines an agent; adding `str_replace_editor` changes behavior even when task success improves.
- [soft-bound-traditions-as-sources-for-context-engineering-strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- **evidence**: the environmental-curiosity failure is a concrete case of blocked transfer from human learning/scaffolding traditions: agents do not reliably signal or act on surprise without externally supplied process cues.
- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **see-also**: sibling mechanism. That note covers stored knowledge failing to surface; this source covers live-context information failing to connect to the active task and plan.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) -- **compares-with**: both papers study how tool exposure changes agent behavior; Coding Agents finds filesystem-native search/slicing can improve long-context work, while this paper shows extra editing tools can suppress environmental investigation despite improving pass rate.
- [Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) -- **compares-with**: both argue that aggregate task success is too coarse for deployed agents, but Rabanser et al. decomposes reliability into consistency/robustness/predictability/safety, while this paper isolates observation-to-action adaptation.

## Bidirectional Candidates

- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **see-also**: the note should point to this source only if it explicitly distinguishes stored-knowledge activation from live-context integration.
- [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) → source -- **evidence**: the paper gives empirical support that process prompts can change task outcomes independently from output format.
- [agent-is-a-tool-loop](../../../../notes/agent-is-a-tool-loop.md) → source -- **evidence**: the tool-suite ablation supports treating capability surface as constitutive of the agent, not incidental configuration.

## Reverse-edge Candidates

- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → [Agents Explore but Agents Ignore](../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md) -- **see-also**: useful as a sibling distinction, not direct evidence for the note's stored-knowledge activation claim.
- [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) → [Agents Explore but Agents Ignore](../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md) -- **evidence**: benchmark evidence that process instructions such as "explore before acting" and "investigate discovered files" can improve both process metric and pass rate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) -- rejected as too specific to dynamic tool surfaces and sub-agent dispatch. The paper varies tool suites across runs, but does not study mid-task tool-surface changes.
- [apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops](../../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) -- adjacent through "success is insufficient," but its mechanism is hidden fallback after tool failure. This paper's mechanism is ignored observations, not degraded execution paths.
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- related through aggregate success vs per-instance properties, but environmental curiosity is prior activation/adaptation, not self-assessment discrimination.
- [Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- relevant contrast on diagnostic richness, but better treated as synthesis context: rich traces help only when the proposer inspects the unexpected details instead of summarizing them away.
- [EsoLang-Bench](../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming-languages.ingest.md) -- adjacent benchmark-fitness source, but the present paper is about observed-signal integration, not OOD semantic competence.

## Index Membership

- [evaluation-index](../../../notes/evaluation-index.md) -- the source contributes a process-oriented agent evaluation metric that separates discovery from interaction.
- [tool-loop-index](../../../notes/tool-loop-index.md) -- the tool-suite result is useful evidence that capability surface changes behavior, not just convenience.
- [computational-model-index](../../../notes/computational-model-index.md) -- the paper operationalizes agents as scaffolds plus tools over environment observations.

## Synthesis Opportunities

- This paper plus [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), [process-structure-and-output-structure-are-independent-levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md), and [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) implies a new sibling claim: "Context presence does not imply contextual integration." The stored-knowledge activation gap and the live-context integration gap are adjacent but distinct.
- This paper plus [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) suggests a tool-design tension: richer tool suites can improve task success while narrowing environmental search behavior. The high-reach claim would be that tool additions are behavioral priors, not neutral affordances.

## Flags

- The source is a strong candidate for a new narrow note rather than updating [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), because the live-context integration failure is distinct from model-internal or KB-stored knowledge activation.
