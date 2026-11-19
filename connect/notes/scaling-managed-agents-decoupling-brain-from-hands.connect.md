---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/scaling-managed-agents-decoupling-brain-from-hands.md"
source_has_frontmatter: true
date: "2026-04-11"
depth: standard
---

# Connection Report: Scaling Managed Agents: Decoupling the brain from the hands

**Source:** [Scaling Managed Agents: Decoupling the brain from the hands](../../sources/scaling-managed-agents-decoupling-brain-from-hands.md)

## Discovery Trace

**Index scan:**
- Read [notes index](../../notes/index.md). Flagged:
  - [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- direct conceptual match: the source's "session / harness / sandbox" virtualizes the same harness perimeter the note decomposes as scheduler / context engine / execution substrate.
  - [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) -- source's harness recovery and event-log replay instantiate symbolic state outside the model, but the connection is mostly through the runtime decomposition note.
  - [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) -- source explicitly separates durable session log from what the harness passes into Claude's context window.
  - [the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) -- source offers a production counter-design to raw transcript inheritance, but less directly than the session-history note.
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [context-engineering](../../notes/definitions/context-engineering.md) -- source treats context as durable external state plus harness-selected loading, matching the KB's broader context-engineering definition.
  - [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) -- source's brain/hand decoupling and token isolation are concrete scoping boundaries, though the note is more about prompt/context scoping than infrastructure credentials.
  - [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) -- source gives concrete production evidence that topology and isolation matter for scaling, without addressing verification.
  - [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) and [tool-loop](../../notes/tool-loop-index.md) -- source's many-hands architecture treats each hand as a separate tool surface.
  - [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- source occupies a distinctive point in the design space: stateless harnesses, durable session log, many hands, interface-stable boundary artifacts.

**Topic indexes:**
- Read [tool-loop](../../notes/tool-loop-index.md) -- kept [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) as a weaker connection because the source generalizes fresh tool loops into hosted hands, but the note's primary concern is task decomposition under varying capability surfaces.
- Read [computational-model](../../notes/computational-model-index.md) -- kept the runtime decomposition, bounded-context orchestration, session-history, context-engineering, and scoping candidates as the relevant cluster.

**Semantic search:** via qmd
- query "Managed Agents decouples harness brain hands session sandbox durable event log stable interfaces agent runtime" -- top hits:
  - [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) (93%) -- kept; strongest connection.
  - [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) (35%) -- kept; the source's durable session log plus selected `getEvents()` loading is a concrete implementation of the note's storage/loading separation.
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) (50%) -- rejected; source mentions sandboxes and files, but does not discuss inspectability as the anti-blackbox mechanism.
- query "agent harness session log outside context window getEvents context object long horizon" -- top hits:
  - [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) (55%) -- kept.
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) (45%) -- kept as broader support.
  - [context-engineering](../../notes/definitions/context-engineering.md) (37%) -- kept as definition-level connection.
  - [always-loaded-context-mechanisms-in-agent-harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) (45%) -- rejected; the source is about hosted runtime interfaces, not user-controlled always-loaded surfaces.
- query "execution substrate sandbox tool interface scheduler context engine runtime decomposition" -- qmd failed with an `InsufficientMemoryError`; used keyword search and index scan fallback for this concept cluster.
- query "credential sandbox security boundary agent tools vault MCP tokens isolation" -- top hits:
  - [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) (88%) -- kept, but only as a concrete isolation/topology example; source does not address verification.
  - [mcp-bundles-stateless-tools-with-stateful-runtime](../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) (39%) -- rejected; source's MCP proxy/vault example is about credential isolation, not the stateful-runtime tax.
  - [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) (34%) -- kept as a design-space placement candidate.
- query "Managed Agents Anthropic harnesses stable interfaces brain hands session sandbox context engineering" against sources -- top hits:
  - [this source](../../sources/scaling-managed-agents-decoupling-brain-from-hands.md) (93%).
  - [Ingest: The Anatomy of an Agent Harness](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) (43%) -- confirms the runtime-taxonomy neighborhood but not a direct source-to-source link for the report.

**Keyword search:**
- `rg "brain|hands|session log|context object|getEvents|time-to-first-token|TTFT|harness.*container|sandbox.*credential|tokens.*sandbox|stale as models|context anxiety|Managed Agents|agent runtimes|scheduler.*context engine.*execution substrate|execution substrate|tool surfaces" kb/notes kb/sources kb/instructions --glob "*.md"` -- found the source itself, [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [files-not-database](../../notes/files-not-database.md), [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md), and source ingests for related harness taxonomies. Kept runtime decomposition, session-history, and subtasks/tool-surface candidates; rejected memory/file-system candidates as indirect.

**Link following:**
- From [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), followed links to [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) and [context-engineering](../../notes/definitions/context-engineering.md). This confirmed the source is best used as an extension/evidence point for the runtime decomposition, not as a separate foundation for every downstream note.
- From [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md), followed links to [the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) and [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md). Kept the session-history note because it states the exact storage/loading separation the source implements.
- From [tool-loop](../../notes/tool-loop-index.md), followed to [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md). Kept as a secondary connection: Managed Agents' many-hands abstraction generalizes tool-surface variation into a stable interface, but the note's primary forcing case is subtask delegation.

## Connections Found

- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- **extends**: Managed Agents independently decomposes a production agent runtime into separable interfaces -- harness/brain, session log, and sandbox/hands -- strengthening the note's claim that the "harness" perimeter becomes more architecturally useful once split into distinct components.
- [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) -- **exemplifies**: the source's session log stores the full durable event stream, while `getEvents()` lets the harness choose positional slices and transformations before passing anything into Claude's context window.
- [context-engineering](../../notes/definitions/context-engineering.md) -- **extends**: the source adds a production interface design where recoverable context storage is guaranteed by the session, while arbitrary context organization and prompt-cache-aware transformations remain in the harness.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **exemplifies**: the source treats context efficiency as an architectural concern, reporting lower time-to-first-token after separating stateless harness startup from sandbox provisioning and delaying hands until needed.
- [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) -- **extends**: Managed Agents provides a concrete topology/isolation example: decoupled brains, hands, and sessions let harnesses and sandboxes fail or be replaced independently, and credential isolation is achieved by keeping tokens outside the sandbox. The source does not address the verification part of the chain.
- [subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) -- **extends**: the source's "many hands" architecture treats each execution environment as a named `execute(name, input) -> string` tool, showing a hosted version of fresh capability surfaces beyond the note's subtask-delegation case.
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **exemplifies**: Managed Agents is a concrete point in the orchestration design space: stateless harnesses, durable session persistence, many remote hands, and stable brain/hand/session interfaces that can outlast implementation changes.

## Bidirectional Candidates

- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) <-> source -- **extends**: a future update could add Managed Agents as new practitioner evidence alongside Vtrivedy10, Raschka, Lopopolo, and the cybernetics thread.
- [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) <-> source -- **exemplifies**: the source gives unusually direct implementation language for "store more than you load."

## Raw Text Candidates

None

## Rejected Candidates

- [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) -- rejected as a direct link because the source is a runtime interface report rather than a formal scheduler/select-call argument; the connection is already mediated by the runtime decomposition and session-history notes.
- [the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../../notes/the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md) -- rejected as redundant with the more specific session-history connection.
- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) -- rejected as too broad: source's isolation is mostly service/runtime/credential isolation, while the note's core claim is about flat prompt context and sub-agent lexical frames.
- [mcp-bundles-stateless-tools-with-stateful-runtime](../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) -- rejected: both mention MCP and state, but the source uses MCP as a credential proxy pattern; the note argues against forcing stateless tools through stateful servers.
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- rejected: source discusses sandboxes and repos but not inspectability as the mechanism that defeats blackbox risk.
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- rejected: the durable session object is a form of storage/context substrate, but the source is about runtime interface design, not memory as storage/retrieval/learning.

## Index Membership

- [computational-model](../../notes/computational-model-index.md) -- source belongs in the scheduling/orchestration cluster as production evidence for separating harness, context/session, and execution substrate.
- [tool-loop](../../notes/tool-loop-index.md) -- possible but weaker; source extends the tool-loop discussion only where "hands" become independent execution surfaces under a stable call interface.
- [related-systems](../../notes/related-systems/related-systems-index.md) -- no index addition recommended; this is a source ingest, not a reviewed external repository/system entry.

## Synthesis Opportunities

- The source plus [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md), and [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) suggest a synthesis note about **stable agent runtime interfaces**: as model behavior changes, the durable interface should preserve session, computation, and capability boundaries while letting harness internals churn.
- The source's "context anxiety disappeared in Opus 4.5" example may support a later synthesis about **harness assumptions becoming stale as model capability changes**, connecting to the bitter lesson boundary, but that thread was not explored deeply in this standard pass.

## Flags

- Several target notes are `status: seedling` and one is `status: speculative`; the proposed relationships are additive (`extends`, `exemplifies`) rather than load-bearing foundations.
- The qmd query for "execution substrate sandbox tool interface scheduler context engine runtime decomposition" failed with an `InsufficientMemoryError`; keyword search and index scan covered the same candidate cluster.
