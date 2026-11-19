---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/sources/context-as-an-environment.ingest.md
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: Ingest: Context as an Environment

**Source:** [Ingest: Context as an Environment](../../../../sources/context-as-an-environment.ingest.md)

## Discovery Trace

**Target and collection contracts:**

- Read the complete tracked ingest and `kb/sources/COLLECTION.md`. The ingest already links Scroll to ACM, Virtual Context, and Fractal, so this report does not repeat those authored edges as candidates.
- Read `kb/notes/COLLECTION.md`, `kb/agent-memory-systems/COLLECTION.md`, and `kb/agentic-systems/COLLECTION.md` before evaluating possible return links. All proposed outbound system comparisons use the source collection's authorised `compares-with` label.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Read the context-engineering, agent-memory, and tool-loop topic heads. They routed the search toward context selection, bounded working views, programmable orchestration, and the distinction between storage and activation.
- The reference head supplied no direct Commonplace implementation analogue. The agent-memory head exposed the code-grounded comparison corpus; the agentic head exposed Fractal and Claude Code dynamic workflows as orchestration-side boundaries.

**Complete title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg -N '^description:' kb/<destination>/ --glob '*.md'` across `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- The listings flagged Prime Agent, the RLM family, lambda-RLM, ACM, AgeMem, Virtual Context, Letta, OpenViking, Playground, Recuris, AI-Context-OS, Slate, and several generic retrieval products. Reference matches remained Commonplace-specific and failed the articulation test.

**Body search:**

- `rg -l -i 'context (window|assembly|virtuali[sz]ation|management)|compaction|paging|progressive disclosure|L0/L1/L2|working memory|core memory|archival memory|persistent (python|repl)|append-only (event|log)|event log|session (memory|history)|prompt (injection|assembly)' kb/agent-memory-systems --glob '*.md'` -- retained systems with distinct selection, transformation, or projection mechanisms; generic stores and retrieval APIs were evaluated but rejected below.
- `rg -n -i 'RLM|recursive language|Tendril|llm-do|context.*environment|programmatic context|event log|working view|projection' kb/notes kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- retained the programmable-context family and projection-boundary comparisons.
- `rg -n -i 'operation alphabet|action alphabet|operation set|operator set|action basis|expressive (power|interface)|what .* can express|expressivity' kb/notes kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- found no existing context-operation-interface note, but found that `action alphabet` already names world-effect capabilities in the tool-loop and coordination notes.
- `rg -n -i 'prime agent|persistent recursive|persistent repl|context environment|session environment' kb/notes kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- retained Prime Agent as the closest missed comparison.
- Inspected the selected rows in `kb/agent-memory-systems/systems.csv` for AI-Context-OS, Claude Context Guard, Cognee, Hermes, Hindsight, Letta, Link, Mem0, MemoryOS, Napkin, OpenViking, Playground, Spacebot, Supermemory, and Virtual Context. The matrix's read-back and targeting fields distinguish push/pull direction but do not encode the transformation interface available after access.

**Link following:**

- Followed Fractal into the RLM mechanism and persistence-boundary notes, then into Prime Agent and lambda-RLM. This separated arbitrary model-written programs, restricted typed combinators, and persistent recursive-session machinery.
- Followed ACM into AgeMem and the memory-policy note. Both learn invocation inside a hand-designed operation set, making them the clean fixed-interface contrast to Scroll rather than merely two more memory systems.
- Followed Virtual Context into Letta, OpenViking, AI-Context-OS, and Playground. Letta contributes mixed push/pull control, OpenViking contributes hierarchical filesystem operations, and Playground contributes a temporal-cover selector. AI-Context-OS mostly corroborates OpenViking's hierarchy and was not retained as another core edge.
- Followed Recuris through active work state and rule-ready activation. It contributes verified event/state signals and an editable invocation policy rather than another representation or retrieval backend.
- Followed The Log Is the Agent, Coding Agents Are Effective Long-Context Processors, and Slate as boundary cases: retention without a projection policy, generic filesystem computation, and orchestration through compressed episode returns.

## Connections Found

- [Prime Agent: A Self-Improving RLM Harness](../../../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) -- **compares-with**: both give the model a persistent Python substrate for constructing bounded views, while Prime Agent adds daemon-owned recursive sessions, message topology, restart recovery, and separately versioned memory and harness state. The comparison separates operation expressivity from persistence and coordination horizon.
- [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) -- **compares-with**: lambda-RLM replaces Scroll's general Python with deterministic typed `SPLIT`, `MAP`, `FILTER`, `REDUCE`, `CONCAT`, `CROSS`, and `PEEK` operators, providing the sharpest local contrast between expressive freedom and a restricted, inspectable composition language.
- [AgeMem](../../../../agent-memory-systems/lightweight/agemem.md) -- **compares-with**: AgeMem learns when to invoke six fixed short- and long-term-memory operations, whereas Scroll reasons by writing programs over exact retained state. Together with ACM, it isolates learned policy from the hand-chosen interface in which that policy learns.
- [Letta](../../../../agent-memory-systems/reviews/letta.md) -- **compares-with**: Letta combines always-pushed editable core blocks, explicit recall and archival tools, compaction, and background memory editing. It contrasts Scroll's single explicit-print boundary with a mixed system-push/model-pull interface.
- [OpenViking](../../../../agent-memory-systems/reviews/openviking.md) -- **compares-with**: OpenViking exposes a `viking://` filesystem, fixed search/read/write operations, and L0/L1/L2 representations selected through hooks and retrieval. It tests whether hierarchy and progressive disclosure can substitute for part of Scroll's arbitrary transformation surface.
- [Playground](../../../../agent-memory-systems/reviews/playground.md) -- **compares-with**: Playground selects a budgeted temporal cover over summary chunks and supplements it with explicit range retrieval. Its context policy chooses a frontier in a temporal hierarchy rather than letting the model compute an unrestricted projection over a log.
- [Recursive Experiential Working Memory Evolution](../../../../sources/recursive-experiential-working-memory-evolution.ingest.md) -- **compares-with**: Recuris uses verified pending/done/blocked state and typed runtime events to trigger skills, and can revise its invocation policy under evaluation gates. It adds signal-grounded activation and policy adaptation to a comparison otherwise dominated by retained substrates and fixed selectors.
- [The Log Is the Agent](../../../../sources/the-log-is-the-agent-2065129901427130678.ingest.md) -- **compares-with**: both make append-only history durable ground truth, but the essay leaves view rendering largely unspecified while Scroll supplies an executable projection mechanism. It is the useful negative control showing that retention alone does not define a context policy.
- [Recursive Language Models - what finally gave me the 'aha' moment](../../../../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) -- **compares-with**: both externalize context into a persistent REPL and admit model-written search and transformation with explicit output projection; the RLM walkthrough supplies the simpler run-scoped mechanism from which Scroll's event-sourced session design can be distinguished.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) -- **compares-with**: generic filesystem search, slicing, and scripting form a less specialized programmable baseline. The comparison asks what Scroll's event schema, resident namespace, and eviction landmarks add beyond ordinary coding-agent operations over externalized text.
- [Slate: Moving Beyond ReAct and RLM](../../../../sources/slate-moving-beyond-react-and-rlm.ingest.md) -- **compares-with**: Slate manages context by dispatching bounded threads and admitting only compressed episode returns to the orchestrator. It supplies an orchestration-side boundary where projection occurs across agent calls rather than through a memory-query interface.

## Bidirectional Candidates

- [Prime Agent: A Self-Improving RLM Harness](../../../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md) <-> source -- **compares-with**: a return edge would let readers of the broader persistent-RLM harness find Scroll's narrower, benchmarked event-log and working-view design.
- [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) <-> source -- **compares-with**: a return edge would make the restricted-combinator versus arbitrary-program contrast traversable from either side.
- [The Log Is the Agent](../../../../sources/the-log-is-the-agent-2065129901427130678.ingest.md) <-> source -- **compares-with**: a return edge would point readers from the log-first thesis to a concrete implementation of the projection layer that thesis leaves open.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [AI-Context-OS](../../../../agent-memory-systems/reviews/AI-Context-OS.md) -- its L0/L1/L2 files, adapters, and hybrid retrieval corroborate the hierarchical progressive-disclosure family, but OpenViking exposes the same axis with a clearer agent-facing operation surface; retaining both would overweight one design family.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) -- bounded prompt memory, progressive skills, session recall, and background trace learning make it a broad mixed-memory example, but Letta and Recuris supply sharper contrasts for control placement and adaptive activation.
- [Mem0](../../../../agent-memory-systems/reviews/mem0.md), [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md), [MemoryOS](../../../../agent-memory-systems/reviews/MemoryOS.md), [Supermemory](../../../../agent-memory-systems/reviews/supermemory.md), and [Cognee](../../../../agent-memory-systems/reviews/cognee.md) -- these vary extraction, storage, ranking, and retrieval, but their contribution to this question reduces to fixed recall plus injection. They are relevant to a product survey, not needed to establish a new context-operation family.
- [Claude Context Guard](../../../../agent-memory-systems/reviews/claude-context-guard.md), [Link](../../../../agent-memory-systems/reviews/link.md), and [napkin](../../../../agent-memory-systems/reviews/napkin.md) -- their pagination, bounded packets, and progressive overviews are useful implementations of pull-based disclosure, but Virtual Context and OpenViking already represent that family more discriminatingly.
- [Agent memory systems comparison table](../../../../agent-memory-systems/systems-table.md) -- this is the right population index but not a system-level comparison target. Its storage, push/pull, targeting, trace-learning, and enforcement columns do not yet record the operation language or projection boundary at issue.
- [Compiling coordination preserves primitive, not aggregate, authority](../../../../notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md) -- it uses `primitive action alphabet` for world-effect authority. That is a terminology constraint on the proposed synthesis, not evidence for the context-management claim.

## Index Membership

- [Agent memory systems](../../../../agent-memory-systems/README.md) -- the ingest itself should remain in `kb/sources/`. If this comparison becomes durable, Scroll merits a doc-grounded lightweight review, or preferably a code-grounded review of the named public implementation, before joining the agent-memory comparison corpus. The generated 148-system table intentionally excludes doc-only reviews.

## Synthesis Opportunities

- Prefer the claim **The context-operation interface bounds the policies it can realize** over the current tentative “context-operation alphabet” wording. `Action alphabet` already has a distinct KB meaning tied to world-effect capabilities, while the proposed note concerns transformations of retained state into active context.
- Use archetypes rather than enumerating every memory system. A compact core is: Scroll and Prime Agent/RLM for open-ended programs; lambda-RLM for restricted composition; ACM and AgeMem for learned selection over fixed operations; Virtual Context for proxy-owned projection; Letta for mixed push/pull state; OpenViking for hierarchical filesystem disclosure; Playground for temporal-cover selection; and Recuris for state-grounded, editable activation. The Log Is the Agent, coding agents, and Slate are boundary controls.
- Compare each system on seven axes: retained substrate and fidelity; addressable unit; available locate/expand/transform/summarize/delete/expose operations; controller and policy learner; projection boundary; persistence horizon; and whether the operation set or invocation policy can itself change.
- The existing 148-system matrix already covers storage, read-back direction, push targeting, trace learning, and enforcement. Operation interface and projection boundary are missing axes. The synthesis note can establish those axes with representative systems before any separate matrix-extension work attempts corpus-wide coding.

## Maintenance Observations

- This report previously targeted the ignored snapshot. It now targets the tracked ingest, which is the source collection's durable authored surface.
- The current ingest's recommended note names only Scroll, ACM, and Virtual Context. That trio establishes open program versus fixed actions versus proxy selection, but omits restricted program composition, learned fixed-operation policy, mixed push/pull control, hierarchical and temporal selectors, and adaptive event-grounded activation.

## Flags

- Evidence tiers differ: Letta, OpenViking, Playground, Virtual Context, and Fractal have code-grounded reviews; AgeMem and the paper ingests are doc- or paper-grounded. A future comparison must preserve that distinction rather than treating every cell as equally verified.
- The broader source makes several independent claims about evidence retention, activation failures, programmable composition, and fixed harness choices. A synthesis note should bind itself to the operation-interface claim and leave benchmark superiority and general memory quality outside its scope.
