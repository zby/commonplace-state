---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/the-best-model-routing-is-task-specific-2077537847951945742.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: The Best Model Routing is Task Specific

**Source:** [The Best Model Routing is Task Specific](../../../sources/the-best-model-routing-is-task-specific-2077537847951945742.md)

## Discovery Trace

**Description listing scan:**
- `rg "^description:.*(routing|router|task|workflow|vertical|harness|cost|latency|context|oracle|eval|model|distribution|document|parse|tool|scheduler|selection|provider|gateway)" kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob "*.md"` -- no scores; flagged the scheduler/context-engine cluster, vertical-agent source, Raschka coding-agent source, Fintool source, dynamic-workflows source, and several model-routing keyword hits in system reviews.

**Topic indexes:**
- [context-engineering-README](../../../../tags/context-engineering-README.md) -- used to orient the source against context efficiency, bounded-context orchestration, and vertical-agent context allocation.
- [tool-loop-README](../../../../tags/tool-loop-README.md) -- checked because the source treats model selection as part of a harness/router rather than as a standalone model property; it did not yield a stronger target than the scheduler/context-engine notes.

**Body search:**
- `rg -n "model routing|router|routing|task-specific|task specific|difficulty model|quality bar|cost.*latency|latency.*cost|frontier model|cheap model|generic gateway|vertical agent|vertical AI|workflow|task distribution|private ground truth|eval.*private|document parsing|OCR|VLM|ParseBench|LlamaParse" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- no scores; found the closest local prior art around context efficiency, bounded scheduling, vertical agents, dynamic workflows, harness taxonomies, oracle strength, and several weak keyword-only model-routing mentions.
- `rg -n "LlamaParse|ParseBench|model routing|task-specific routing|generic gateway|OpenRouter Fusion|Devin Fusion|Harvey|Decagon|difficulty model|private ground truth" kb --glob "*.md"` -- no scores; only this new snapshot matched most exact terms. Existing "model routing" hits were broader harness/system-review mentions, not the same task-specific routing argument.

**Link following:**
- Followed [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md), and [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). These confirmed that the source's routing layer is best treated as scheduler/context-engine evidence plus verifier/oracle evidence, not merely as provider configuration.
- Followed sibling sources [Building a Good Vertical Agent](../../../../sources/building-a-good-vertical-agent-2065190286519906657.ingest.md), [Components of A Coding Agent](../../../../sources/components-of-a-coding-agent-raschka.ingest.md), [Lessons from Building AI Agents for Financial Services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md), and [A harness for every task](../../../../sources/a-harness-for-every-task-dynamic-workflows.ingest.md). The vertical-agent source is the strongest sibling: it frames context as expected-cost allocation over a task distribution, while this source applies the same shape to model choice and verifier-backed quality bars.

## Connections Found

- [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: the source supplies cost-plane practitioner evidence that agent systems should spend bounded model/context calls only where the task-specific quality bar justifies them.
- [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -- **evidence**: the source's router is a concrete `select` policy over bounded calls, choosing page/task-specific prompts, models, and engines from explicit workflow state.
- [agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **evidence**: task-specific model routing sits at the scheduler/context-engine boundary: the system decides what call happens next and what model/context frame that call receives.
- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the source explicitly says routing alpha depends on a workflow-specific difficulty model and eval, and LlamaParse uses an agentic judge to validate routed outputs.
- [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: task-specific routing works only when "good enough" can be measured cheaply enough to route to non-frontier models; the source is a practitioner example of oracle hardening as economic leverage.
- [Building a Good Vertical Agent](../../../../sources/building-a-good-vertical-agent-2065190286519906657.ingest.md) -- **compares-with**: both sources argue vertical-agent advantage comes from knowing a workflow distribution deeply enough to allocate scarce resources; one allocates context tiers, the other allocates models and document engines.
- [Components of A Coding Agent](../../../../sources/components-of-a-coding-agent-raschka.ingest.md) -- **compares-with**: both sources reattribute apparent model quality to harness design. Raschka emphasizes context quality; this source emphasizes routing and task-specific evaluation.
- [A harness for every task: dynamic workflows in Claude Code](../../../../sources/a-harness-for-every-task-dynamic-workflows.ingest.md) -- **compares-with**: both describe per-task harnesses that choose sub-agents/models and verification patterns instead of using one fixed model loop for all work.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -> source -- **evidence**: cite the source as cost-plane support that resource scarcity includes routing frontier calls away from tasks where cheaper models clear a known bar.
- [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -> source -- **evidence**: cite LlamaParse-style page routing as a real-world `select` policy whose cost estimate depends on page complexity, model capability, and verification.
- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -> source -- **evidence**: cite "difficulty model plus eval as private ground truth" as a practitioner formulation of verifier-dependent automation.
- [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -> source -- **evidence**: cite the document-routing case as an example where soft/hardening oracles make cheaper generator choices usable.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [model-partition-registry](../../../../reference/proposals/model-partition-registry.md) -- rejected: despite the shared phrase "model partition", that proposal is about Commonplace review execution partitions, not application-level routing among model/provider choices.
- [Context providers: the missing layer between agents and tools](../../../../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) -- rejected as a main connection: it shares source-scoped delegation and bounded calls, but its core claim is about tool/source boundaries rather than task-specific model quality bars.
- [How We Built Our Knowledge Base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md) -- rejected: enterprise memory and knowledge-base architecture are adjacent to context engineering, but the source does not help interpret model routing.
- [Lessons from Building AI Agents for Financial Services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) -- rejected as a main connection: it has strong oracle/eval and vertical-product overlap, but the distinctive Fintool contribution is filesystem-first skills and domain evals rather than routing among models.
- [ReframeWeb](../../../../agent-memory-systems/reviews/ReframeWeb.md) -- rejected: it contains a code-grounded note that per-task model routing is data rather than config, but the system review is about memory retrieval and has too little overlap with the source's routing-economics argument.

## Index Membership

None

## Synthesis Opportunities

The source plus [Building a Good Vertical Agent](../../../../sources/building-a-good-vertical-agent-2065190286519906657.ingest.md), [context efficiency](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), and [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) imply a note-level claim: task-specific routing earns value only when a workflow has a learned input taxonomy and verifier strong enough to define "cheap enough and good enough" per subtask. Generic gateways can optimize providers and ensembles, but they cannot own that workflow-specific oracle.

## Maintenance Observations

None

## Flags

- No split needed: the source has many examples, but they support one central claim about task-specific routing under a workflow-specific evaluation surface.
