---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/agent-harness-large-language-model-agents-survey.md"
source_has_frontmatter: true
date: "2026-05-28"
depth: standard
---

# Connection Report: Agent Harness for Large Language Model Agents

**Source:** [Agent Harness for Large Language Model Agents: A Survey](../../../sources/agent-harness-large-language-model-agents-survey.md)

## Discovery Trace

**Index scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md). Snapshots are immutable; connection candidates should inform the authored `.ingest.md` surface. Authorised labels for ingest/source review include `evidence`, `derived-from`, `rationale`, `defined-in`, `compares-with`, and sparse `see-also`.
- Read [notes directory index](../../../notes/dir-index.md). Promising candidates: runtime decomposition, always-loaded context mechanisms, memory-as-crosscutting concern, methodology enforcement, orchestration guarantees, verification boundary, and session-history/context-loading notes.
- Read [reference directory index](../../../reference/dir-index.md). No direct reference target was stronger than note/source targets; shipped commonplace reference docs are not the main destination.
- Read [agent-memory systems README](../../../../agent-memory-systems/README.md). Promising compares-with candidates: reviewed harness/runtime systems and source-only harness papers.

**Body search:**
- `rg -n "harness|agent harness|execution loop|tool registry|lifecycle hooks|evaluation interface|HARNESSCARD|trajectory evaluation|sandbox|protocol standardization|MCP|A2A|context manager|context engineering|tool governance|memory management architecture|runtime governance" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -- found the existing harness cluster plus related notes on context, memory, evaluation, and orchestration.
- `rg -n "scheduler|context engine|execution substrate|tool loop|framework-owned tool loop|agent runtime|runtime|orchestration|coordination|observability|lifecycle|evaluation|verification" kb/notes --glob "*.md"` -- confirmed the three-part runtime decomposition and adjacent evaluation/coordination notes as strongest note candidates.
- `rg -n "Claude Code|OpenHands|LangChain|LangGraph|AutoGen|CrewAI|MCP|A2A|SWE-bench|AgencyBench|SkillsBench|OpenClaw|AIOS|MemGPT|Voyager|Reflexion|tool registry|sandboxing|protocol" kb/sources kb/agent-memory-systems --glob "*.md"` -- found source-to-source comparison targets and already-ingested harness-adjacent papers.

**Link following:**
- Followed [agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) to always-loaded context, methodology enforcement, unified calling conventions, and prior harness sources.
- Followed [always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) to control-plane, capability-description, memory, and configuration-injection surfaces.
- Followed [agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) to memory operational axes and memory requirements.
- Followed source siblings: [The Anatomy of an Agent Harness](../../../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md), [What is an Agent Harness](../../../../sources/what-is-an-agent-harness-2046980769747533830.ingest.md), [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md), [Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md), and [Intelligent AI Delegation](../../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md).

## Connections Found

- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **evidence**. The survey independently formalizes a model-surrounding runtime layer, and its `E/T/C/S/L/V` tuple maps mostly onto scheduler, context engine, and execution substrate while exposing pressure to treat lifecycle hooks and evaluation interfaces explicitly.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **evidence**. The survey's context manager, system-prompt assembly concerns, skills, tool registries, and protocol surfaces corroborate the note's claim that harnesses actively decide what context is ambient versus on-demand.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **evidence**. The survey places memory under both context management and state storage, matching the note's split between storage, retrieval/activation, and learning rather than treating memory as a plug-in subsystem.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) -- **evidence**. The survey's memory discussion names capture, retention, retrieval, write governance, poisoning, persistence, and evaluation as harness policies around memory artifacts.
- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- **evidence**. Lifecycle hooks, permission layers, sandboxing, tool governance, validation, and observability are harness-side enforcement mechanisms along the same instruction-to-hook-to-script constraining gradient.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **evidence**. The survey's multi-agent section treats cross-agent prompt injection, shared-state consistency, identity, delegation, and failure containment as guarantee problems rather than merely channel problems.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**. The survey argues that reliable agent deployment depends on trajectory evaluation, observability, reproducible benchmarks, and harness configuration disclosure, all of which are verification infrastructure rather than model capability.
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- **evidence**. Separating `C` context manager, `S` state store, and `V` evaluation interface reinforces the distinction between persisting traces/state and loading selected material into the next bounded call.

## Bidirectional Candidates

- [The Anatomy of an Agent Harness](../../../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) -- **compares-with**. Both taxonomize harness components; the earlier source derives components from model limitations, while this survey formalizes a six-tuple and adds literature coverage, system matrix, and challenge analysis.
- [What is an Agent Harness](../../../../sources/what-is-an-agent-harness-2046980769747533830.ingest.md) -- **compares-with**. Both elevate lifecycle hooks and permission/safety as harness primitives; the survey supplies an academic taxonomy and broader corpus, while Dhinakaran supplies a practitioner anti-framework distinction.
- [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- **compares-with**. NLAH studies one natural-language externalization strategy experimentally; this survey covers harnesses as a general runtime governance layer and names the broader component space.
- [Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) -- **compares-with**. The reliability paper develops metrics for consistency, robustness, predictability, and safety; this survey argues that harness configuration and evaluation interfaces are where those properties become observable and governable.
- [Intelligent AI Delegation](../../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md) -- **compares-with**. The delegation paper focuses on task transfer, accountability, and protocol gaps; this harness survey treats A2A/MCP/protocols and multi-agent coordination as one challenge area inside runtime governance.
- [Agent Behavioral Contracts](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- **compares-with**. ABC formalizes runtime behavioral constraints; this survey identifies lifecycle hooks, tool governance, and evaluation interfaces as harness locations where such contracts can execute.
- [Lessons from Building AI Agents for Financial Services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) -- **compares-with**. Fintool is a production case of sandboxing, filesystem-first context, skills, and domain-specific evaluations; the survey supplies a generalized harness taxonomy for those choices.

## Reverse-edge Candidates

- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -> source -- **evidence**. The note can cite this survey as a stronger academic corroboration and as a challenge to decide whether lifecycle/evaluation deserve explicit treatment beyond the three-part decomposition.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -> source -- **evidence**. The note can cite the survey's context-manager and skill/protocol discussion as external confirmation of the ambient/on-demand context split.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -> source -- **evidence**. The note can cite the survey's memory-as-harness-infrastructure framing.
- [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) -> source -- **evidence**. The note can cite lifecycle hooks, sandboxing, and tool governance as independent harness-layer instances of deterministic enforcement.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- related through Agent Skills and progressive disclosure, but the survey's contribution is harness-level governance rather than skill packaging mechanics.
- [MCP bundles stateless tools with stateful runtime](../../../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- the survey discusses MCP as protocol infrastructure, but does not engage the state-tax critique enough for a direct evidence edge.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- adjacent and potentially useful as background, but the stronger orchestration edge is the guarantees note because the survey emphasizes coordination failures and safety.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- relevant through evaluation and benchmark infrastructure, but the verification-boundary note is a better target for this source.

## Index Membership

- [Architecture index](../../../notes/architecture-index.md) -- the source belongs in the harness/runtime architecture cluster.
- [Context engineering index](../../../notes/context-engineering-index.md) -- relevant because the paper treats context management as one harness component and frames harness engineering as distinct from context engineering.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) -- potential source-only coverage if the project wants survey papers about harness/runtime systems visible beside related system reviews.
- `kb/sources/dir-index.md` -- generated source listing should include the snapshot and ingest report after index refresh.

## Synthesis Opportunities

- The current three-part runtime decomposition may need an explicit account of governance and evaluation. The survey's `L` and `V` components could be treated as cross-cutting policy/evaluation layers over scheduler, context engine, and substrate, or as separate runtime components. A follow-up note should decide which interpretation is cleaner.
- Harness disclosure may become the evaluation analogue of model cards. The survey's HARNESSCARD recommendation connects reliability evaluation, reproducibility, and context engineering: results without harness configuration are underspecified.
- "Harness engineering" may be the practical integration layer for existing KB theories: bounded-context scheduling, context engineering, memory policy, methodology enforcement, verification, and coordination guarantees all become runtime responsibilities inside the harness.

## Maintenance Observations

- The KB now has several harness-taxonomy ingests plus at least one runtime-decomposition note. A later synthesis pass should consider whether the harness cluster needs a curated index or one stable taxonomy note to prevent repeated source-by-source mapping.

## Flags

- The source is broad and survey-shaped. It should not be decomposed into many weak edges; the strongest value is its formal six-component tuple and the lifecycle/evaluation pressure it adds to the existing runtime decomposition.
- The source page reports version 3 and a field that says "Peer-reviewed article". Treat this cautiously until publication venue and peer-review status are verified from an external bibliographic source.
