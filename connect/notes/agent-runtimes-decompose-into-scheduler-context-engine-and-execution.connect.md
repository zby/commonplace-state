---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Separating agent-runtime responsibilities

**Source:** [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md)

## Discovery Trace

**Description listing scan:**

- Read the `notes` collection head and the `computational-model` and `architecture` tag heads. Neither tag head declares `complete: true`, so the by-tag description scan `rg -l '^tags:.*\b(computational-model|architecture)\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` was run.
- Generated fresh H1 surfaces for all authorised local destinations (`notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`) and filtered them with `rg -i 'responsibil|failure|runtime|harness|scheduler|context|external state|module boundar'`.
- `reference` supplied Commonplace-specific implementation detail but no general diagnostic target. Agent-memory and agentic-system reviews supplied many instances; the theoretical notes and source ingests below were retained because they state the responsibility boundary or a discriminating countercase directly. No instruction operationalises this classification, so the rare instruction edge was skipped.

**Topic indexes:**

- [Computational model](../../../../tags/computational-model-README.md) places the source next to bounded-context scheduling but still omits it from the curated scheduling cluster.
- [Architecture](../../../../tags/architecture-README.md) remains mainly a head for Commonplace's shipped architecture, so the general diagnostic note is a weaker curated fit there.
- The agent-memory and agentic-systems heads were read; their examples confirm implementation overlap but are not better first links than the retained theory and evidence targets.

**Body search:**

- `rg -n -i 'diagnostic.*responsibil|responsibility.*failure|control progression|context assembly|external state|action services|repair surfaces|module boundaries' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` surfaced the nested output-diagnosis note, a host-language scheduler that deliberately bundles two responsibilities, and a six-component harness survey that pressures the note's first-cut scope.
- `rg -n -i 'execution substrate|context engine|scheduler|component boundar|component taxonom|runtime structur|crosscutting|cross-cutting|harness perimeter' ...` retained the earlier candidates on boundary warrant, memory, orchestration dimensions, governance, and external evidence.
- `rg -n 'agent-runtimes-decompose-into|scheduler context engine|execution substrate' ...` found extensive existing inbound reliance. Those authored edges were recorded as maintenance scope rather than proposed again.

**Link following:**

- Followed the source's bounded-context link into [The practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md), which is a concrete implementation where host code owns both next-step choice and prompt framing; it directly tests the distinction between analytical and module boundaries.
- Followed the three-way diagnostic phrasing into [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md); rejected it because its fixed-input relations are a nested but separate diagnostic surface, not a development of runtime responsibility.
- Followed the memory/search rows into the crosscutting-memory note and the scheduler row into the multi-dimensional-orchestration note. Followed source ingests that either instantiate the responsibility cut or pressure it with lifecycle/evaluation concerns.

## Connections Found

- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) -- **contrasts**: provides the general rival-allocation test that explains why the source presents responsibilities rather than mandatory modules.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **extends**: works through the source's storage-versus-activation example and adds learning as a concern crossing the first-cut runtime responsibilities.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **extends**: decomposes scheduling into placement, persistence, coordination, guarantees, and return artifacts, showing why the source's three questions are a first cut rather than a complete architecture.
- [The practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) -- **extends**: gives a concrete runtime where host-language code owns both progression and prompt framing, demonstrating analytical separation without separate modules and naming the lifetime point at which operative state must externalize.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **extends**: develops how exposed scheduling, context, and state/action responsibilities change the points where validation and correction can attach.
- [Ingest: Agent Harness for Large Language Model Agents](../../../../sources/agent-harness-large-language-model-agents-survey.ingest.md) -- **evidenced-by**: its execution/tool/context/state/lifecycle/evaluation tuple corroborates the broad responsibility split while qualifying it with governance and evaluation axes that the source explicitly leaves open.
- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- **evidenced-by**: exposes stage structure, runtime charter, and file-backed state that can be tested against the three diagnostic questions; its benchmark results test the harness, not the taxonomy.
- [Ingest: Scaling Managed Agents: Decoupling the brain from the hands](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) -- **evidenced-by**: production separation of stateless harness, durable session log, and executable sandbox supplies concrete recovery, isolation, and latency consequences while keeping selection and storage distinct.

## Bidirectional Candidates

None. Several retained targets already link to the source; the useful missing direction is outbound from this note.

## Reverse-edge Candidates

None. Existing inbound coverage already includes the context-engineering definition, bounded-context orchestration, memory, governance, deployed-system learning, and multiple source ingests.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [LLM output deviation requires three-way diagnosis because remedies target different relations](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) -- offers a useful nested diagnostic after the input is assembled, but it does not refine the upstream runtime-responsibility split.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- already consumes the source for a different learning-boundary argument; an outbound edge would widen the note rather than sharpen diagnosis.
- [MCP bundles stateless tools with a stateful runtime](../../../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- concerns stateful packaging of tool invocation, not the distinction among choosing, framing, and executing one operation.
- Individual agent-memory and agentic-system reviews -- examples were plentiful but less discriminating than the theoretical extensions and source ingests retained above.
- The source's current Vtrivedy10 and Raschka references -- already authored inline and therefore not connection candidates.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- candidate for the curated `Scheduling & Orchestration` cluster because the note supplies the first diagnostic cut connecting scheduling, per-call context, and external exact state.

## Synthesis Opportunities

None. The finer relationship between runtime-responsibility diagnosis and fixed-input output diagnosis is not yet supported strongly enough to warrant a synthesis note.

## Maintenance Observations

- The reframed title no longer asserts three peer components or practitioner convergence, but many inbound citers still use the old wording. A required follow-up should update visible link text and reconsider any sentence that treats the former component ontology as a settled premise; path-only relocation will not do that semantic repair.

## Flags

- The source deliberately leaves evaluation, governance, and observability as possible additional axes. The harness survey is a useful pressure test, not a reason to expand the note into an exhaustive taxonomy.
