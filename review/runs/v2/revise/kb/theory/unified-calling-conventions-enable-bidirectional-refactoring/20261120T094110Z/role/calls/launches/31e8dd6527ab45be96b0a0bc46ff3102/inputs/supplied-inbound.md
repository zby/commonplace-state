# Inbound contexts of `kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md`

16 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

## `kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md`

- Title: Ingest: Towards Linguistic Symbiosis of an Object-Oriented and a Logic Programming Language
- Description: Implementation evidence that linguistic symbiosis across logic and object-oriented paradigms requires explicit syntactic and semantic mappings.

> The strongest landing point is [Unified calling conventions enable bidirectional refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md): this source shows that a common call surface needs semantic mappings, not only shared names. [Representational form](../theory/definitions/representational-form.md) prevents equating programming-paradigm mismatch with Commonplace's natural-language/symbolic distinction. The paper is secondary to the 2001 and 2006 sources for defining reflection itself.

## `kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md`

- Title: Ingest: Inter-language Reflection: A Conceptual Model and Its Implementation
- Description: Mature model defining inter-language reflection as traditional reflection plus linguistic symbiosis through data and protocol mappings.

> The paper supplies the mature technical model for [Cross-representational reflection](../theory/reflective-coverage-is-graded-across-representational-forms.md) and adds a useful qualification to [Unified calling conventions enable bidirectional refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md): sharing a callable surface requires both data mappings and protocol mappings when regimes disagree about values and behavior. [Representational form](../theory/definitions/representational-form.md) constrains the proposed generalization beyond programming languages.

## `kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md`

- Title: Ingest: How to build your own agent harness??? (Mike Piccolo / iii)
- Description: iii ships a production agent harness as independently-versioned workers on one bus behind a uniform trigger primitive, making harness layers hot-swappable

> The companion [connect report](../reports/cache/connect/sources/how-to-build-your-own-agent-harness-2060069083878408689.connect.md) places this source firmly in the KB's harness cluster. As an immutable snapshot it authors nothing; the report's load-bearing output is reverse-edge candidates plus the outbound edges a future note-author could draw. The strongest fits are evidence relationships: [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) (iii is a fifth convergent practitioner taxonomy whose workers map cleanly onto scheduler / context-engine / execution-substrate — and the only one shipping the decomposition as separately-versioned runtime components), [agent-orchestration-occupies-a-multi-dimensional-design-space](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) (iii fixes a distinctive point: external symbolic scheduler, cross-session versioned workers, fail-closed policy guarantee), [unified-calling-conventions-enable-bidirectional-refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) (production evidence that name-b [cut at 1200 characters]

> 3. **Self-contained internal rewrite as evidence the composition holds.** The turn-orchestrator FSM collapsed 11→7 states and deleted a per-call resume mechanism while every neighbour stayed unchanged because contracts are bus-level function ids. Concrete production evidence for [unified-calling-conventions-enable-bidirectional-refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md), which currently grounds the claim only on llm-do. [just-a-reference]

> Write a new note in `kb/notes/` capturing **component replaceability / independent versioning behind a uniform calling convention as a first-class harness property** (the connect report's flagged theory gap, Extractable Value #1). It should cite this source as primary evidence, link to [unified-calling-conventions-enable-bidirectional-refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) (mechanism) and [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) (the decomposition it operationalizes), and carry the "slider not a fork" reframing into [agent-orchestration-occupies-a-multi-dimensional-design-space](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md). The connect report flags this as a split candidate, so expect the author to spread the remaining edges (enforcement/recovery, always-loaded-context) across their target notes rather than route everything to one.

## `kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md`

- Title: Ingest: The Anatomy of an Agent Harness
- Description: Practitioner taxonomy deriving harness components (filesystem, bash, sandboxes, memory, context management, long-horizon execution) from model limitations — provides the component anatomy that bridges Lopopolo's practice and the cybernetics framing

> - [unified-calling-conventions-enable-bidirectional-refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) — **exemplifies**: model/harness co-training creates overfitting (apply_patch, Terminal Bench divergence) — evidence for why stable interfaces matter

> **What is most surprising?** The claim that models post-trained with specific harnesses *degrade* when the harness changes. The apply_patch example and the Terminal Bench 2.0 divergence (same model, dramatically different scores across harnesses) suggest that post-training creates a kind of learned coupling between model weights and harness structure that goes beyond simple prompt sensitivity. This is surprising because a "truly intelligent model should have little trouble switching between patch methods" — the author says this themselves, then notes it doesn't hold in practice. The implication is that co-training doesn't just optimize the model for a harness — it *overfits* the model to the harness, creating a new class of brittleness that the [unified-calling-conventions](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) note predicts but that we now have practitioner evidence for. This finding strengthens Extractable Value item 3 and should be treated as more than a reference — it names a failure mode (co-training overfitting) that may become more important as model-harness co-evolution intensifies.

## `kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md`

- Title: Ingest: UPML: A Framework for Knowledge System Reuse
- Description: UPML separates reusable reasoning components from explicit bridges and refiners, while leaving much adapter construction to knowledge engineers.

> UPML is a technical basis for distinguishing reusable method content from the adaptation logic that connects or specializes it. Its bridges and refiners make concrete the meta-decisions discussed in [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../theory/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): a bridge adapts an interface between components, while a refiner changes a component by specialization. It also compares with [Unified calling conventions enable bidirectional refactoring between neural and symbolic](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md), because both treat an explicit interface vocabulary as the boundary that permits components to be recomposed.

## `kb/tags/computational-model-README.md`

- Title: Computational model
- Description: Tag README — PL concepts (scoping, homoiconicity, partial evaluation, typing) applied to LLM instructions, plus the scheduling architecture that follows from context scarcity

> - [Unified calling conventions](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) — calling conventions that let components move between neural and symbolic implementations

## `kb/tags/constraining-README.md`

- Title: constraining
- Description: Curated head for the constraining tag — narrowing the interpretation space of artifacts, from conventions to deterministic code; codification, relaxing, and the decision heuristics

> - [unified calling conventions enable bidirectional refactoring](../theory/unified-calling-conventions-enable-bidirectional-refactoring.md) — how to commit reversibly: neural and symbolic components behind the same callable interface

## `kb/theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md`

- Title: Ad hoc prompts extend the system without schema changes
- Description: Any system with an LLM agent layer can absorb new requirements through natural language prompts without changing the deterministic base

> - [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: unified calling conventions make it possible to start with a prompt and later extract to a skill without changing call sites

## `kb/theory/code-complements-weight-prompt-with-symbolic-operations.md`

- Title: Code complements the weight–prompt pair with independently executed symbolic operations
- Description: Distinguishes model interpretation from runtime-assigned execution, including model-generated code and the same code artifact used as prompt context or as an executable operation

> - [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — extends: makes movement between the two execution paths local while preserving an interface

## `kb/theory/llm-context-interprets-instructions-and-content-through-one-medium.md`

- Title: LLM contexts interpret instructions and content through the same token medium
- Description: LLMs interpret instructions and content through one token medium, enabling natural-language artifacts to alter behavior without translation while requiring architecture to enforce role, scope, and authority boundaries

> - [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — applies: one interface can resolve names to neural or symbolic implementations

## `kb/theory/llm-context-is-composed-without-scoping.md`

- Title: LLM context is composed without scoping
- Description: Flat context concatenation lacks local scope and produces name collision, contamination, and spooky action at a distance; selected invocation inputs limit direct access without establishing scope within the supplied context

> - [unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — existing approximation: llm-do's per-agent system prompts and arguments are frame-local context

## `kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md`

- Title: Operational signals that a component is a relaxing candidate
- Description: Operational signals for when a component likely encodes a brittle proxy theory rather than an exact specification and should be relaxed instead of codified harder

> - [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: unified calling makes acting on relaxing signals cheap — refactoring from codified to learned is a local operation

## `kb/theory/reflective-coverage-is-graded-across-representational-forms.md`

- Title: Reflective coverage is graded across representational forms
- Description: Reflective coverage is stated per represented form and operation profile; control of an external dependency does not make that dependency part of the system's reflective coverage

> - [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — mechanism: supplies one interface-level mapping while leaving aspect coverage, authority, and lineage as separate obligations

## `kb/theory/research/adaptation-agentic-ai-analysis.md`

- Title: Adaptation signals choose pressure; artifact analysis chooses the retained surface
- Description: Maps agentic-adaptation signals onto artifact-analysis axes so KB learning records which retained surface changes, what authority it gains, and how to review it

> - [Unified calling conventions enable bidirectional refactoring](../unified-calling-conventions-enable-bidirectional-refactoring.md) - enables: moving learned behavior between neural/natural-language/symbolic surfaces is cheaper when call boundaries stay stable

## `kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md`

- Title: RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence
- Description: RLM variants, Tendril, and llm-do show that control-language restriction and artifact persistence are separate questions, including where cited RLM sources leave post-return lifecycle unspecified

> - [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — grounds: supplies the llm-do call-boundary side of the comparison

## `kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md`

- Title: Statecharts and programs differ in what they show, not in what they can compute
- Description: Why the expressiveness argument between state machines and programs is empty, which control structure each representation shows natively versus encodes as data, and how that decides whether a workflow reads better as a chart or as code

> - [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — exemplifies: the graph-DSL versus imperative-scheduler comparison is one instance of this choice
