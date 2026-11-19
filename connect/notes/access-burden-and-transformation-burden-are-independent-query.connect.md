---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Access burden and transformation burden are distinct query dimensions

**Source:** [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md)

## Discovery Trace

**Authorisation and curated heads:**

- Read the source note, `kb/notes/COLLECTION.md`, and the connect-report type contract before discovery. The notes contract authorises local prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `external` is authorised only for already-known targets. It excludes `kb/work/`.
- Read `kb/notes/README.md`, `kb/notes/foundations-README.md`, and `kb/notes/computational-model-README.md`. Neither matching tag README declares `complete: true`, so ran both required by-tag scans: `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the same query with `computational-model`.
- Read the destination heads `kb/reference/README.md`, `kb/types/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No matching tag README exists at those collection roots.
- Generated every authorised local destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and its path-plus-description surface with `rg '^description:' kb/<destination>/ --glob '*.md'`.

**Notes:**

- Focused search 1: `rg -l -i '(access|retriev|locat|find).{0,120}(transform|reason|aggregat|synthesi)|(transform|reason|aggregat|synthesi).{0,120}(access|retriev|locat|find)' kb/notes/ --glob '*.md'`.
- Focused search 2: `rg -l -i '(symbolic|mechanical|formal).{0,120}(semantic|judg|interpret|LLM)|(semantic|judg|interpret|LLM).{0,120}(symbolic|mechanical|formal)' kb/notes/ --glob '*.md'`.
- Focused search 3: `rg -l -i 'specified (operation|transformation)|specif.{0,60}(mechanical execution|symbolic execution)|acceptance conditions' kb/notes/ --glob '*.md'`.
- Kept [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md): it develops the consequence of classifying a transformation as semantic by locating where the required meaning-dependent judgment can be paid and what inputs relocation requires.
- Kept [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md): the source's query router is a concrete application of its broader lenses over specification completeness, oracle strength, interpretation space, and pattern stability.
- Kept [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md): it directly grounds the revised source's caveat that symbolic execution can conform exactly to a specified operation without showing that the specification answers the original query.
- Evaluated [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md), [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md), and [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). The first and fourth are already integrated into the kept codification synthesis, the select/call note establishes an orchestration normal form rather than a routing criterion, and the production/evaluation note addresses inferential-path review rather than result validation against a query.
- Followed all three kept candidates one hop. The semantic-work neighborhood led to `codification`, `rule-based-context-selection`, and `frontloading`; these explain placement and prepayment but would duplicate the kept target. The codification neighborhood led to `agentic-systems-interpret-underspecified-instructions`, `oracle-strength-spectrum`, and the exact-implementation note; the first two are bundled most usefully by the codification synthesis, while exact-implementation independently supports the source's explicit specification caveat. The exact-implementation neighborhood led to proximate targets, oracle strength, and spec mining; these broaden the objective hierarchy or hardening workflow rather than sharpening the query-dimension claim.
- Confirmed that [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md), [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), and [Soft degradation often binds before the hard cap when required evidence fits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) are already linked from the source; they are not new candidate edges.

**Reference:**

- Focused search: `rg -n -i '(access|retriev|locat).{0,100}(transform|reason|aggregat|synthesi)|(symbolic|deterministic|formal).{0,100}(semantic|judg|interpret|LLM)|(semantic|judg|interpret|LLM).{0,100}(symbolic|deterministic|formal)|specif.{0,40}(execution|operation|transform)' kb/reference/ --glob '*.md'`.
- Evaluated `navigation.md`, `storage-architecture.md`, ADR 023's deterministic/semantic grounding split, and ADR 038's structural/semantic type-conformance split. They describe Commonplace access or checking machinery, not the independent access and answer-transformation burdens of a query, so no direct Commonplace analogue warranted an `evidenced-by` or sparse `see-also` edge.

**Types:**

- Ran `rg -n -i '(access|retriev|locat).{0,100}(transform|reason|aggregat|synthesi)|(symbolic|deterministic|formal).{0,100}(semantic|judg|interpret|LLM)|(semantic|judg|interpret|LLM).{0,100}(symbolic|deterministic|formal)' kb/types/ --glob '*.md'`.
- The global contracts separate deterministic bookkeeping from semantic judgment in validation and review, but none addresses query access and transformation as distinct dimensions. No candidate passed the articulation test.

**Agent-memory systems:**

- Focused search: `rg -n -i '(access|retriev|locat|query).{0,120}(transform|reason|aggregat|synthesi)|(transform|reason|aggregat|synthesi).{0,120}(access|retriev|locat|query)|(symbolic|deterministic|formal).{0,120}(semantic|judg|interpret|LLM)|(semantic|judg|interpret|LLM).{0,120}(symbolic|deterministic|formal)|structured quer' kb/agent-memory-systems/ --glob '*.md'`.
- Kept [Sparks](../../../../agent-memory-systems/reviews/sparks.md): its inspected runtime assigns manifest, query, lint, and context-assembly plumbing to deterministic Go while leaving classification, page writing, synthesis, and contradiction handling to an external agent. This is a code-grounded instance of separately routing access mechanics and semantic transformation.
- Evaluated [Synthadoc](../../../../agent-memory-systems/reviews/synthadoc.md), [DocMason](../../../../agent-memory-systems/reviews/docmason.md), and [xMemory](../../../../agent-memory-systems/reviews/xMemory.md). Synthadoc and DocMason combine retrieval, synthesis, and validation but do not test whether their burdens vary separately, making them less precise instances than Sparks; xMemory's “decoupling before aggregation” means extracting records before thematic organization, not distinguishing query access from answer transformation.
- Followed Sparks' links to artifact-analysis definitions, activation, and the workshop-layer note. They explain its retained surfaces and pull behavior but do not add a more direct query-routing connection.

**Agentic systems:**

- Focused search: `rg -n -i '(retriev|access).{0,100}(transform|reason|aggregat|synthesi)|(symbolic|deterministic).{0,100}(semantic|LLM)|(semantic|LLM).{0,100}(symbolic|deterministic)' kb/agentic-systems/ --glob '*.md'`.
- Evaluated [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md), [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md), [Swamp](../../../../agentic-systems/reviews/swamp.md), and [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md). Semantic Engine stops at access and exploration; GBrain's retrieve→synthesize path and Swamp's intent→runtime split are system descriptions without a separability test; dynamic workflows supplies symbolic orchestration already covered by the source's authored scheduler links. No candidate passed strongly enough to retain.

**Sources:**

- Focused search: `rg -n -i 'reading context and integrating context|deterministic symbolic|symbolic (operators|control|runtime|combinators)|exact aggregation|transformation burden|retrieval.{0,80}(reasoning|aggregation|synthesis)|reasoning.{0,80}retrieval|knowledge.{0,80}reasoning|access.{0,80}integration|full.table|target.column|column readability' kb/sources/ --glob '*.ingest.md'`.
- Kept [Why Large Language Models Fail at Tabular Prediction](../../../../sources/why-large-language-models-fail-at-tabular-prediction.ingest.md): its controlled full-table setup keeps target-column readability near ceiling while multi-column classification degrades, directly separating available-input access from integration capacity within the tested regime.
- Kept [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md): its λ-RLM runtime assigns filtering, reduction, aggregation, depth, and cost accounting to deterministic combinators while reserving bounded semantic leaf judgments for models, with formal and benchmark qualifications recorded in the ingest.
- Kept [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md): its reported emergent strategies combine iterative query refinement, file slicing, programmatic aggregation, and re-inspection, supplying a bounded empirical case for access and transformation alternating in one execution loop.
- Evaluated [AI Components for a Deterministic System](../../../../sources/eric-evans-ai-components-deterministic-system.ingest.md), [Intern-S2-Mobius](../../../../sources/intern-s2-mobius-decoupled-knowledge-and-reasoning.ingest.md), and [Three Dimensions That Matter To An Agent Memory Store](../../../../sources/three-dimensions-agent-memory-store-2054246434506199529.ingest.md). Evans' modeling/classification split does not imply that classification is formally executable; Mobius separates model-internal storage and reasoning roles rather than external query access and transformation burdens; Three Dimensions already authors the useful inbound access-versus-map-reduce link and adds no new edge.
- Followed the three kept ingests one hop. The tabular neighborhood isolates context volume, dependency depth, and coordinate integration; λ-RLM leads to the already-authored scheduler and bounded-context notes; the coding-agent neighborhood leads to context efficiency, semantic-overflow scheduling, and process/output structure. These neighborhoods confirm three non-duplicative uses: separability evidence, a typed routing architecture, and an iterative access/transformation execution case.

**Instructions and reverse-edge pass:**

- Read `kb/instructions/COLLECTION.md` because the notes contract says the usual instruction relationship is inverse. Focused search: `rg -n -i 'symbolic|semantic|deterministic|retriev|access burden|transformation burden|aggregation|classification|acceptance condition|fully specified' kb/instructions/ --glob '*.md'`.
- Conversion, validation, review, and full-pass procedures separate deterministic operations from semantic judgment, but their procedures do not depend specifically on the access/transformation distinction. No justified `instruction → source` `rests-on` candidate was found, and no procedure adds ordering, defaults, or stopping conditions that would justify a source-side `operationalized-from` edge.

**External:**

- External is authorised but is not a prospecting surface. The user supplied no external target and none was already present in loaded task context, so external prospecting was skipped.

## Connections Found

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **extends**: develops the source's semantic-transformation side into a placement rule, explaining when meaning-dependent judgment can be prepaid upstream or moved off a bottlenecked context and which inputs that relocation requires.
- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- **exemplifies**: the source's specification-sensitive query router is a query-specific instance of the broader decision across specification completeness, oracle strength, interpretation space, and pattern stability.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **grounds**: directly supports the source's caveat that exact symbolic execution establishes conformance to a specified operation, not that the operation or specification answers the original query.
- [Sparks](../../../../agent-memory-systems/reviews/sparks.md) -- **evidenced-by**: the code-grounded system routes manifest, query, lint, and context-assembly access plumbing through deterministic code while leaving classification, synthesis, and contradiction handling to an external agent.
- [Why Large Language Models Fail at Tabular Prediction](../../../../sources/why-large-language-models-fail-at-tabular-prediction.ingest.md) -- **evidenced-by**: a controlled full-table prompt keeps target-column access near ceiling while multi-coordinate integration degrades, showing within the tested regime that available inputs do not imply successful transformation.
- [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) -- **evidenced-by**: λ-RLM is a measured architecture that assigns deterministic filtering, reduction, and aggregation to typed combinators and semantic leaf judgments to bounded model calls.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) -- **evidenced-by**: the benchmarked agents reportedly alternate search and slicing with scripted aggregation and iterative refinement, instantiating the source's loop in which access and transformation expose work for one another.

## Bidirectional Candidates

- [Why Large Language Models Fail at Tabular Prediction](../../../../sources/why-large-language-models-fail-at-tabular-prediction.ingest.md) <-> source -- **is-evidence-for** from the ingest: its read-versus-integrate intervention is a bounded empirical case for the source's access/transformation distinction; the return path would give the ingest's result an explicit theoretical landing.
- [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) <-> source -- **is-evidence-for** from the ingest: its typed-combinator/neural-leaf boundary is a direct worked architecture for the source's routing corollary, while the ingest records the fixed-library and benchmark limits.
- [Coding Agents are Effective Long-Context Processors](../../../../sources/coding-agents-are-effective-long-context-processors.ingest.md) <-> source -- **is-evidence-for** from the ingest: its iterative query-refinement and programmatic-aggregation strategies are a bounded observed instance of access and transformation alternating without collapsing into one burden.

## Reverse-edge Candidates

- [Sparks](../../../../agent-memory-systems/reviews/sparks.md) → source -- **is-evidence-for**: the review already states that deterministic query/plumbing and agent-authored semantic work occupy different responsibilities; this rare evidence-direction link would give that observation an explicit theoretical target.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) -- already carries the inbound extraction link and is already linked from the source; no candidate edge remains to author.
- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- supplies one underlying lens, but the kept codify-versus-LLM synthesis is the more useful landing for the source's multi-factor routing rule.
- [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) -- proves an orchestration normal form, not how to distinguish access from answer transformation or decide when an operation is specified.
- [Synthadoc](../../../../agent-memory-systems/reviews/synthadoc.md) -- combines retrieval, synthesis, gap detection, and validation, but does not test their separability; Sparks is the cleaner code-grounded routing case.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- covers discovery and access but intentionally stops before answer transformation, so the connection would be one-axis topical overlap.
- [xMemory](../../../../agent-memory-systems/reviews/xMemory.md) -- its extraction-before-theme-aggregation sequence uses “decoupling” differently from the source's distinct query burdens.
- [AI Components for a Deterministic System](../../../../sources/eric-evans-ai-components-deterministic-system.ingest.md) -- a frozen taxonomy narrows classification but does not make each classification a fully specified operation; treating it as the source's formal/semantic split would overstate the case.
- [Intern-S2-Mobius](../../../../sources/intern-s2-mobius-decoupled-knowledge-and-reasoning.ingest.md) -- separates storage and reasoning roles inside distributed-parametric state, not the difficulty of finding query inputs from the difficulty of deriving the requested output.
- [Three Dimensions That Matter To An Agent Memory Store](../../../../sources/three-dimensions-agent-memory-store-2054246434506199529.ingest.md) -- already authors the useful inbound link for the retrieval-versus-map-reduce distinction, so no new edge is needed.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- the source already carries the tag but is absent from the selective curated head; it would add the specification-sensitive query-routing consequence of symbolic scheduling to the Scheduling & Orchestration cluster.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
