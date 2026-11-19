---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Model-resolved indirection adds interpretation work to LLM execution

**Source:** [Model-resolved indirection adds interpretation work to LLM execution](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md)

## Discovery Trace

**Authority and contracts:**

- Read `.agents/skills/cp-skill-connect/SKILL.md` and `kb/cache/types/connect-report.md` completely and used their single-use, standard-depth, repo-local discovery and report-section requirements.
- Read `kb/notes/COLLECTION.md`, the source artifact, and `kb/types/note.md` completely. Read the destination contracts and curated heads for `notes` (including `notes/definitions`), `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions` completely.
- The source collection authorizes notes, definitions, types, reference, agent-memory-systems, agentic-systems, sources, and instructions as local destinations. The notes contract authorizes `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, and `evidenced-by` within notes; `defined-in` for definitions; `evidenced-by` for types, reference, agent-memory-systems, agentic-systems, and sources; and `operationalized-from` or `see-also` for instructions. The source's current authored labels are within that vocabulary. `kb/work/` is excluded.
- External targets are reserved for known targets. None was supplied, so external prospecting was skipped. No web or external semantic search was used.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/computational-model-README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md` as the curated routing surfaces.

**Title and description listing scan:**

- Ran the fresh title surface query `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorized local destination. The surfaces contained 355 `notes`, 10 `types`, 135 `reference`, 173 `agent-memory-systems`, 12 `agentic-systems`, 515 `sources`, and 44 `instructions` title lines.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` for the same destinations. The corresponding surfaces contained 352, 13, 133, 171, 10, 450, and 97 description lines.
- `notes/definitions` was separately scanned with the same title and description queries: 23 titles and 23 descriptions. Relevant definitions were `representational-form`, `context-engineering`, `constraining`, and `codification`; the source already links `constraining`, so it was not proposed again.
- The `computational-model` tag scan used `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md'` followed by the description projection. `computational-model-README.md` does not declare `complete: true`, so the by-tag scan was required and was performed. The relevant neighborhood was then checked by body, not accepted from tag membership alone.

**Body search and articulation checks:**

- `notes`: ran repository-local `rg` searches for model-resolved indirection, dereferencing, placeholders, binding, resolvers, literals; for frontloading, partial evaluation, build-time compilation, materialization, point-of-use views, and distant declarations; and for context cost, interpretation overhead, token cost, loading frequency, and runtime parameters. Candidates were retained only when the target supplied a distinct mechanism, boundary, contrast, falsifiable comparison, or concrete evidence.
- `types`: ran `rg -n -i 'context|prompt|instruction|token|indirection|frontload|compile|config|variable|template|partial|runtime|build|literal' kb/types/ --glob '*.md'`. No source→type connection passed the label/articulation check; `types/instruction.md` passed as a reverse edge because its executor-boundary rule needs this theory.
- `reference`: ran `rg -n -i 'indirection|frontload|build.?time|compile|template|variable|config|literal|context.{0,30}(cost|budget|token)|instruction.{0,30}(load|specific)' kb/reference/ --glob '*.md'`. The shipped instruction-generation note is already linked inline by the source. Existing proposal→source `rests-on` edges were recorded as existing edges, not duplicated.
- `agent-memory-systems`: ran scoped `rg` searches for indirection, frontloading, compilation, materialization, pre-computation, templates, literals, runtime variables, context budgets, and skill/prompt preparation. Funes passed because its review describes a concrete raw-source→compiled-context pipeline; progressive-disclosure and retrieval-budget matches did not isolate model-side instruction resolution.
- `agentic-systems`: ran the corresponding `rg` body search. The remaining matches described host-runtime registry selection, session summaries, or orchestration, not an LLM resolving an instruction binding; no source→agentic-system edge passed.
- `sources`: ran three local `rg -l`/`rg -n` passes for context variables and costs, build-time compilation/materialization and distilled skills, and prompt/instruction/context overhead. Authored `.ingest.md` reports were preferred over immutable snapshots. RLM, Reason Wide/Not Deep, and Machine Studying passed with bounded claims; distractor, survey, context-file, and qualitative skill matches were rejected when they did not isolate the source's mechanism.
- `instructions`: ran scoped `rg` searches for the same resolver, frontloading, compilation, materialization, literal, runtime-parameter, and context-cost terms. `write-instruction.md` passed only as a reverse edge because it prescribes frontloaded self-contained instructions; no procedure adds the source's ordering, defaults, or stopping conditions, so no `operationalized-from` edge was proposed.
- Label checks used each destination contract before retaining a candidate. In particular, `evidenced-by` is used for concrete cases/reports, `mechanism` or `grounds` only where the target supplies the claimed causal explanation, and `extends`/`contrasts` only where the target changes the comparison or decision boundary.

**Link following:**

- Followed every current source link: [Instruction generation](../../../../reference/instruction-generation.md), [Constraining](../../../../notes/definitions/constraining.md), [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md), [Frontloading is partial evaluation, not divide-and-conquer](../../../../notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md), [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), and [Instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md). These are already-authored source edges and were not repeated as new connections.
- Followed one hop from that neighborhood through context efficiency, pointer design, local materialization, recomputation, shared-token interpretation, underspecification, traditional executor conformance, and build-time instruction generation. The promising candidates below were read and checked against their actual claims and contracts.
- Followed cross-collection paths to `types/instruction.md`, `reference/instruction-generation.md`, `reference/adr/018-types-are-path-references-to-instruction-docs.md`, `reference/proposals/deterministic-write-context-assembly.md`, `agent-memory-systems/reviews/funes.md`, the three retained ingest reports, and `instructions/write-instruction.md`.
- Reverse searches for `indirection-is-costly-in-llm-instructions.md`, `model-resolved indirection`, and the current source heading found existing inbound links from `checked-inline-blocks-for-shared-instruction-text.md` and `channel-compiled-instruction-artifacts.md`, plus the source's current neighborhood. Existing edges were not proposed again.

**Destination outcome:**

- `notes`: connections found below; `notes/definitions`: None as a new edge because the source already links `constraining` and the other definitions did not pass the term-definition test.
- `types`: None as a source→type edge; one reverse-edge candidate.
- `reference`: None as a new source→reference edge because the source already links `instruction-generation`; four reverse/design checks were retained below.
- `agent-memory-systems`: one concrete connection.
- `agentic-systems`: None.
- `sources`: three concrete connections; no raw-text candidate.
- `instructions`: None as a source→instruction edge; one reverse-edge candidate.

## Connections Found

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **extends**: The source adds model-side binding and interpretation work to this note's distinction between per-window feasibility and aggregate token economics, clarifying why a short alias and a long literal cannot be compared by token count alone.
- [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — **extends**: The note compares fixed, query-time, and crafted pointers by specificity, cost, and reliability; the source adds the binding-time question of whether the model or a deterministic resolver must turn the pointer into an actionable value.
- [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — **extends**: The source supplies the model-side mechanism behind this note's declaration-only versus generated point-of-use comparison, while preserving the note's single-authority, verification, and maintenance costs.
- [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **extends**: The source generalizes that cost reversal from recomputing derived values to resolving references and branches, making storage, regeneration, drift, and per-use interpretation part of the same decision.
- [LLM contexts interpret instructions and content through the same token medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) — **mechanism**: The shared token medium and absent formal program/data boundary explain why a model-facing placeholder remains semantic work, while executor-side expansion can deliver the resolved value without asking the model to substitute it.
- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: Its spec-to-program projection and non-unique natural-language semantics supply the reason a prompt reference has a model-visible failure surface rather than an automatic dereference procedure.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md) — **contrasts**: The source's conventional-code comparison needs this adjacent distinction: a programming runtime can adjudicate a lookup procedure, whereas an LLM must both infer the intended binding and produce a consistent use.
- [Generate KB skills at build time, don't parameterise them](../../../../notes/generate-instructions-at-build-time.md) — **extends**: That note gives the concrete build-time policy for installation-specific values and standalone generated skills; the source adds the resolver-choice, authority, literal-size, and regeneration conditions that determine when the policy pays.
- [Funes](../../../../agent-memory-systems/reviews/funes.md) — **evidenced-by**: Funes is a concrete external case of paying raw-source interpretation upstream into compiled wiki artifacts and directing later questions to those artifacts; it supports upstream preparation without proving that every useful data reference should be literalized.
- [Ingest: Recursive Language Models - what finally gave me the 'aha' moment](../../../../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) — **evidenced-by**: Its `context`-variable example bounds the claim: executor-side data indirection can be valuable when it keeps a huge value out of the prompt, unlike an instruction placeholder whose value the model must act on.
- [Ingest: Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) — **evidenced-by**: Its offline analysis produces a skill that displaces repeated runtime reasoning at lower output-token cost, a concrete instance of paying recurring semantic work upstream while retaining the report's decomposition and generalization limits.
- [Ingest: Machine Studying](../../../../sources/machine-studying.ingest.md) — **evidenced-by**: Its cheatsheet/preparation case reports a low-inference-budget benefit and an explicit preparation-versus-inference tradeoff; it supports the source's budget-shift mechanism but does not isolate literal substitution from search and prompt injection.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Instruction](../../../../types/instruction.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **rests-on**: The type contract tells authors to fix arbitrary values such as paths and templates while leaving live-system choices to the executor; this source supplies the LLM-specific interpretation-cost rationale for that split.
- [Instruction generation](../../../../reference/instruction-generation.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **rests-on**: The shipped generation flow chooses setup-time substitution over runtime variables for generated artifacts, so maintainers revisiting that boundary should be able to read the theory behind the choice.
- [018-Types are path references to instruction docs](../../../../reference/adr/018-types-are-path-references-to-instruction-docs.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **rests-on**: The ADR prefers direct file pointers over making an agent execute a separate resolution protocol; the source explains the model-side cost that makes that design boundary meaningful.
- [Deterministic write-context assembly](../../../../reference/proposals/deterministic-write-context-assembly.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **rests-on**: The proposal explicitly weighs literal rendering against a manifest of source paths and names runtime indirection as a cost; this source would give the unadopted choice its theoretical premise.
- [Write an Instruction](../../../../instructions/write-instruction.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **rests-on**: The procedure's frontloaded, first-reading requirement would benefit from the narrower explanation of why unresolved values and extra instruction hops recur as LLM work on every use.
- [Ingest: Recursive Language Models - what finally gave me the 'aha' moment](../../../../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **is-evidence-for**: The ingest report explicitly extracts context-variable indirection as a transferable mechanism; linking the theory would make its useful data-reference counterexample and instruction-placeholder boundary visible to readers.
- [Ingest: Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **is-evidence-for**: The report's offline-to-skill construction and lower output-token use bear on the source's claim that recurring interpretive work can be paid once, while its variance limits remain visible.
- [Ingest: Machine Studying](../../../../sources/machine-studying.ingest.md) → [source](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — **is-evidence-for**: Its preparation/inference budget comparison is useful evidence for the source's relocation claim, with the reverse edge also exposing that the observed package includes search and note injection rather than only binding resolution.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Links encode conditional possibilities, not obligations](../../../../notes/links-encode-conditional-possibilities-not-obligations.md) — its claim is about optional navigation versus content required by every reader, not specifically about model-side substitution of an instruction binding; the reader need is already handled more directly by pointer design and local materialization.
- [LLM-executed methodologies are metacircular interpreters](../../../../notes/llm-executed-methodologies-are-metacircular-interpreters.md) — it addresses repeated reinterpretation of methodologies and codification, but does not isolate the resolver choice or literal-versus-alias tradeoff in this source.
- [A goal-holding interpreter fails softly; workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) — it describes accumulated workaround cost after blocked operations, not the source's earlier binding-time decision or its unresolved-reference failure surface.
- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — context contamination and scope boundaries are adjacent, but the note does not establish the source's distinction between model-resolved instruction values and executor-resolved data values.
- [Context engineering](../../../../notes/definitions/context-engineering.md) — it is a broader definition, and the source does not use the term as vocabulary needing a `defined-in` edge; the existing frontloading and loading links provide the relevant route.
- [Generated index](../../../../types/generated-index.md) — build-time directory listing and instruction-value generation have different consumers and semantics; the title match does not pass the articulation test.
- [002-Inline global types in writing guide](../../../../reference/adr/002-inline-global-types-in-writing-guide.md) — its historical inlining decision is a useful analogy for reducing file hops, but it does not isolate model-side variable resolution and is not retained as a new reference edge.
- [025-Complete generated indexes are build-time only](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — the ADR concerns index generation and publication, not the cost of making an LLM resolve instruction variables or dead branches.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — its registry indirection is host-language runtime selection of agent types, not an LLM reading and substituting a variable in instructions.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — its always-visible session summary is a live runtime input and therefore a boundary case, not evidence for resolving stable setup values before model consumption.
- [AI-Context-OS](../../../../agent-memory-systems/reviews/AI-Context-OS.md) — its L0/L1/L2 context budgeting is progressive disclosure, but the review does not isolate instruction-placeholder interpretation or setup-time literalization.
- [OpenViking](../../../../agent-memory-systems/reviews/openviking.md) — URI retrieval, sidecars, and pre-action recall are runtime memory activation mechanisms; they do not establish a model-side instruction resolver cost.
- [Ingest: How Is LLM Reasoning Distracted by Irrelevant Context?](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — its controlled distractor experiments support a broad context-interference claim, but do not isolate reference resolution or compare model-facing aliases with executor-side expansion.
- [Ingest: Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) — it surveys authored context-file categories and evolution without behavior measurement or a parameterized-versus-generated comparison.
- [Ingest: Skill synthesis — materializing knowledge as skills](../../../../sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md) — it shows useful generated skills but lacks a baseline separating materialization from supplying the same source material in a long prompt.
- [Ingest: Components of A Coding Agent](../../../../sources/components-of-a-coding-agent-raschka.ingest.md) — its qualitative context-quality thesis and frontloaded repository context are relevant to the existing frontloading cluster, but it does not isolate instruction indirection.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) — its literal paths and frontloaded discovery contract are generic procedure mechanics, and it is the procedure being executed rather than an operationalization of this source's build-time policy.
- [Write a KB note](../../../../instructions/cp-skill-write/SKILL.md) — its self-contained writing workflow is not a procedure-specific implementation of the source's resolver choice; frontloading in the skill is a general execution requirement.

## Index Membership

None

## Synthesis Opportunities

- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md), [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md), [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md), [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md), and [Generate KB skills at build time, don't parameterise them](../../../../notes/generate-instructions-at-build-time.md) together suggest a two-axis materialization rule: make a value literal or local when an authoritative value is known before the consuming call and intended readers need it; retain a runtime choice or optional pointer when the live situation determines it or only some readers need it. No current note states the binding-time/authority test and the reader-need test as one decision procedure.

## Maintenance Observations

- `kb/notes/computational-model-README.md` already contains this source's path, but its display title and description still use the pre-copyedit wording “Indirection is costly in LLM instructions” and the old runtime/context summary. The path is valid; the curated entry is stale and was not edited.
- Existing inbound `rests-on` edges from `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` and `kb/reference/proposals/channel-compiled-instruction-artifacts.md` were found. They already point at the source and were not duplicated as candidate work.
- The source's current inline and `Relevant Notes` links resolve, and their labels are authorized. All candidate, reverse-edge, and synthesis paths in this report were checked with `test -f`; no source, library artifact, index, or log was edited.

## Flags

- **Possible split candidate:** The source makes independent claims about the cost model, binding-time/resolver choice, the runtime-parameter boundary, and the portable KB skill-generation example. A future writer could separate the general cost model, the materialization decision rule, and the portability/derived-copy obligation.
- **Scope tension to preserve:** RLM-style `context` references can reduce prompt volume when the referenced value is data that should remain outside the model's input, while instruction placeholders add interpretation work when the model must act on their values. The source's runtime-parameter boundary is sound only while data references and instruction references remain distinguished.
