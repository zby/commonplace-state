---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/memory-backed-personalization-can-look-like-model-improvement.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Memory-backed personalization can look like model improvement

**Source:** [Memory-backed personalization can look like model improvement](../../../../notes/memory-backed-personalization-can-look-like-model-improvement.md)

## Discovery Trace

No scored search was used; all discovery was repository-local.

**Authorization and posture:**

- Read `kb/notes/COLLECTION.md`. It authorizes prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, `kb/instructions/`, and `kb/types/`, while excluding `kb/work/`. It also authorizes the reserved `external` destination for already-known targets, not open-web prospecting.
- Authorised source-to-destination labels applied here were: notes (`extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`, `evidenced-by`), reference/agent-memory/agentic-systems/sources/types (`evidenced-by` plus the destination-specific lineage labels), and instructions (`operationalized-from` or sparse `see-also`).
- The notes contract says instruction links are exceptional: the normal direction is `instruction -> note` via `rests-on`, while `note -> instruction` is warranted as `operationalized-from` only when the procedure adds ordering, defaults, or stopping conditions. That trigger is met by the three retained-intent procedures kept below.

**`kb/notes/`:**

- Curated heads read: `kb/notes/README.md`, `kb/notes/agent-memory-README.md`, `kb/notes/computational-model-README.md`, and `kb/notes/llm-reliability-README.md`. None of the three tag READMEs declares `complete: true`, so the by-tag searches were not skipped.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`.
- Description scans: `rg '^description:' kb/notes/ --glob '*.md'`; and, for each of `agent-memory`, `computational-model`, and `llm-reliability`, `rg -l "^tags:.*\\b${tag}\\b" kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|memory-backed' kb/notes/ --glob '*.md'`; `rg -n -i 'model (improvement|quality|capability)|apparent model|look(s|ed)? like.*model' kb/notes/ --glob '*.md'`; `rg -n -i 'hold .*fixed|held .*fixed|ablat|controlled attribution|component.?s? effects|interaction effect' kb/notes/ --glob '*.md'`; and `rg -n -i 'assembled (input|context)|source, subject, scope|applicable and authoritative|one of several.*authoritative' kb/notes/ --glob '*.md'`.
- Existing-link check: `rg -n 'memory-backed-personalization-can-look-like-model-improvement\\.md' kb/ --glob '*.md'`. This found already-authored inbound edges from [A bare writing prompt does not determine its intended contribution](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) and [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md); the former is already reciprocated from the source, while the latter has an independently useful return path.
- Kept [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): its treatment-grain argument directly grounds the source's model-fixed/memory-fixed evaluation design.
- Kept [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): the source is a narrow personalization instance of the general joint-system attribution claim.
- Kept [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): it develops the governance conditions hidden inside the source's allowance for personalized weights as an evidence carrier.
- Kept [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) as a return-link candidate because it generalizes the source's carrier-neutral allocation point and already links inbound to the source.
- Rejected [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md): both contain the phrase-level match that apparent model quality may be context quality, but their useful traversal is runtime/context architecture broadly rather than retained user intent and causal attribution.
- Rejected [Context engineering](../../../../notes/definitions/context-engineering.md): its model-change exclusion is correct but already supplied more specifically by the source's existing link to the three-way diagnosis note.
- Rejected [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) as a direct edge: it opens the larger explicit-versus-tacit governance comparison, while the parametric-reproduction candidate addresses the source's authority question more precisely. Its addressability limit strengthened that selection; the source now states the separability boundary directly, so no unresolved flag remains.

**`kb/reference/`:**

- Curated head read: `kb/reference/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/reference/ --glob '*.md'`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|memory-backed' kb/reference/ --glob '*.md'`; `rg -n -i 'apparent model|model quality|model improvement|model.*memory|memory.*model' kb/reference/ --glob '*.md'`; and `rg -n -i 'hold .*fixed|held .*fixed|ablat|component.*effect|interaction effect|causal attribution' kb/reference/ --glob '*.md'`.
- Evaluated [Per-artifact write briefs](../../../../reference/proposals/archive/per-artifact-write-briefs.md), which treats a brief as authoritative retained intent within a declared lifecycle. Rejected it because it is a Commonplace-specific unadopted design proposal, while the source's transferable claim does not depend on that proposed representation.
- No reference candidate passed the articulation test.

**`kb/agent-memory-systems/`:**

- Curated head read: `kb/agent-memory-systems/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|preference memor' kb/agent-memory-systems/ --glob '*.md'`; `rg -n -i 'apparent model|model quality|model improvement|stronger model|model.*memory|memory.*model' kb/agent-memory-systems/ --glob '*.md'`; and `rg -n -i 'hold .*fixed|held .*fixed|ablat|with/without|causal.*(memory|uptake)|component.*effect|interaction effect' kb/agent-memory-systems/ --glob '*.md'`.
- Kept the code-grounded [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) review. Its trace-to-user-model pipeline retains source session ids and project scope, emits assistant memory files, runs with/without-guard comparisons, and records target-model verdicts. It is a concrete case where retained personalization and interpreter behavior are separately observable, though its judge is model-based and its real-session effect is not exhaustively tested.
- Rejected [MemoryOS](../../../../agent-memory-systems/reviews/MemoryOS.md), [Continuity](../../../../agent-memory-systems/reviews/continuity.md), and [Mem0](../../../../agent-memory-systems/reviews/mem0.md) as direct edges. They are strong examples of personalization memory and its lineage/staleness risks, but none has the with/without behavioral test needed to support the source's attribution argument; Synapptic is the sharper case.

**`kb/agentic-systems/`:**

- Curated head read: `kb/agentic-systems/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|memory-backed' kb/agentic-systems/ --glob '*.md'`; `rg -n -i 'apparent model|model quality|model improvement|model.*memory|memory.*model|context quality' kb/agentic-systems/ --glob '*.md'`; and `rg -n -i 'hold .*fixed|held .*fixed|ablat|component.*effect|interaction effect|causal attribution' kb/agentic-systems/ --glob '*.md'`.
- Evaluated Agno AgentOS because it explicitly assembles behavior from model, instructions, memory, knowledge, context providers, and session history. Rejected it because the analysis supplies a component inventory, not personalization evidence or a controlled attribution mechanism.
- No agentic-system candidate passed the articulation test.

**`kb/sources/`:**

- Curated head read: `kb/sources/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/sources/ --glob '*.md'`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|preference memor' kb/sources/ --glob '*.md'`; `rg -n -i 'apparent model|model quality|model improvement|stronger model|memory scaling|model.*memory|memory.*model' kb/sources/ --glob '*.md'`; and `rg -n -i 'hold .*fixed|held .*fixed|ablat|with/without memory|causal.*(memory|uptake)|component.*effect|interaction effect' kb/sources/ --glob '*.md'`.
- Snapshot hits were followed to their authored `.ingest.md` companions, as required by the sources collection contract.
- Kept [OpenClaw-RL: Train Any Agent Simply by Talking](../../../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md): its deployment-time RL experiments are direct evidence that personalization can be retained in model weights, supporting the source's carrier-neutral boundary. Its own ingest notes that personalization quality, interference with general improvement, and comparison with artifact-based memory remain under-tested.
- Evaluated [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md): its memory perturbations across 13 backbones are strong evidence for causal uptake tests, but the experiment concerns task experience rather than user-specific conditioning and is already reached through the source's authored activation link and that note's local evidence edge. Rejected a direct edge as redundant and liable to overstate personalization evidence.
- Rejected [Components of A Coding Agent](../../../../sources/components-of-a-coding-agent-raschka.ingest.md): its exact phrase “apparent model quality is really context quality” is a qualitative coding-agent observation without user-specific memory or component ablation.
- Rejected [Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md): it reports external-memory gains but does not isolate memory size, retrieval quality, instruction engineering, or personalization from one another.
- Evaluated the externalization survey and the self-evolving-agents substrate/horizon essay; both corroborate the broad model-versus-external-artifact distinction, but neither adds a sharper path than the Synapptic/OpenClaw pair.

**`kb/instructions/`:**

- Curated head read: `kb/instructions/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/instructions/ --glob '*.md'`.
- Body searches: `rg -n -i 'personaliz|user-specific|retained intent|target commission|memory-backed' kb/instructions/ --glob '*.md'`; `rg -n -i 'apparent model|model quality|model improvement|model.*memory|memory.*model' kb/instructions/ --glob '*.md'`; and `rg -n -i 'hold .*fixed|held .*fixed|ablat|component.*effect|interaction effect|causal attribution' kb/instructions/ --glob '*.md'`.
- Kept [cp-skill-write](../../../../instructions/cp-skill-write/SKILL.md), [cp-skill-write-multistage](../../../../instructions/cp-skill-write-multistage/SKILL.md), and [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md). All three operationalize the source's retained-intent record by requiring source, subject, scope, and authority role; they add precedence and stopping behavior that the theoretical note does not fix, so `operationalized-from` is authorised.
- The full-improvement procedure's existing `Relevant Notes` footer was inspected. A reverse `rests-on` edge to this source would independently help maintainers understand why unresolved contribution is an input-specification problem rather than a stronger-model problem.

**`kb/types/`:**

- Curated head read: `kb/types/README.md`.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`.
- Description scan: `rg '^description:' kb/types/ --glob '*.md'`.
- Body search: `rg -n -i 'personaliz|user-specific|retained intent|target commission|memory-backed|apparent model|model quality|model improvement|hold .*fixed|ablat|causal attribution' kb/types/ --glob '*.md'` returned no matches.
- No type candidate passed the trigger for an evidence-bearing connection.

**External:**

- Skipped. No user-supplied or already-loaded external target required evaluation, and the collection contract does not permit open-web prospecting during connect.

**Link following:**

- Followed all three authored outbound neighbors from the source. [A bare writing prompt does not determine its intended contribution](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) and [LLM output deviation requires three-way diagnosis because remedies target different relations](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) already cover missing intent versus interpreter quality; [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) already covers storage/read-back/activation. These existing links were not duplicated as candidates.
- Followed the one-hop neighborhoods of the experiment-grain, deployed-system, parametric-authority, and Synapptic candidates. This exposed [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md), [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md), and the explicit-retention note. The first two are already carried by the experiment-grain and authored activation paths and are less specific than those candidates for this source; the explicit-retention note sharpened the governed-authority boundary but was not retained as a direct edge.
- Followed the OpenClaw-RL snapshot to its ingest report and retained the authored ingest surface rather than the immutable snapshot.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **grounds**: the source's proposed factorial evaluation depends on the treatment-grain rule that only independently varied model and memory factors can receive separate causal credit.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — **exemplifies**: memory-backed personalization is a specific case where joint deployed-system behavior is misattributed to the model component alone.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) — **extends**: develops the source's personalized-weight carrier case by distinguishing encoded user content from a governed, current, and revisable source of authority.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) — **evidenced-by**: a code-grounded system retains source- and project-scoped user observations, compiles them into assistant memory, tests guards with and without that memory, and records model-specific verdicts, concretely separating retained personalization from interpreter response.
- [OpenClaw-RL: Train Any Agent Simply by Talking](../../../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — **evidenced-by**: deployment-time RL personalization demonstrates that user-specific adaptation can reside in model weights, supporting the source's claim that a separately addressable memory interface is an architectural choice rather than the only carrier.
- [cp-skill-write](../../../../instructions/cp-skill-write/SKILL.md) — **operationalized-from**: requires every supplied retained-intent block to identify source, subject, scope, and authority role, then adds current-direction precedence and an explicit conflict stop.
- [cp-skill-write-multistage](../../../../instructions/cp-skill-write-multistage/SKILL.md) — **operationalized-from**: carries the retained-intent record into a multistage brief and adds the rule that unresolved conflicts remain unresolved rather than being silently chosen by the model.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — **operationalized-from**: turns the source's retained-intent boundary into packet fields, precedence rules, `UNDETERMINED`, a focused user question, and a stopping condition.

## Bidirectional Candidates

- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) <-> source — **exemplifies**: this note already links inbound to the source as its personalization case; a return edge would let source readers move from that concrete carrier/interpreter allocation to the general claim that a required function does not determine component boundaries.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) <-> source — **extends**: after the source points to the general whole-system claim as an instance, the general note can point back to this narrower personalization case for readers who want the model-versus-memory attribution consequence developed concretely.

## Reverse-edge Candidates

- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) -> source — **rests-on**: its retained-intent packet rules and `UNDETERMINED` stop depend on the theoretical distinction between missing user evidence and model capability; the instruction already has a `Relevant Notes` footer for such meta-reader dependencies.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) -> source — **is-evidence-for**: its code-grounded trace-to-user-model pipeline, with/without guard comparisons, and target-model verdicts bear on the source's distinction between retained personalization and interpreter response; the review's theory-facing footer is an appropriate authored surface.
- [OpenClaw-RL: Train Any Agent Simply by Talking](../../../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) -> source — **is-evidence-for**: the ingest's parametric-personalization experiment bears directly on the source's claim that weights can carry user-specific adaptation, while its limitations bound the strength of the personalization and interaction claim.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — phrase-level overlap about apparent model quality, but its reader need is context scarcity and runtime architecture rather than user-specific intent attribution.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — its component split is broader than the source's model/memory causal boundary and adds no personalization-specific premise.
- [Context engineering](../../../../notes/definitions/context-engineering.md) — correctly excludes model changes, but the source's existing three-way-diagnosis link supplies the distinction at the more useful failure-analysis grain.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — useful background on the governance cost of weights, but [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) addresses authority without expanding into the full retention-form comparison.
- [MemoryOS](../../../../agent-memory-systems/reviews/MemoryOS.md) — direct personalization-memory implementation, but no with/without memory test or lineage-preserving long-term record strong enough for the source's causal-attribution claim.
- [Continuity](../../../../agent-memory-systems/reviews/continuity.md) — exposes stale-memory and silent-personalization risks, but does not test whether its pushed memory causes the resulting behavior.
- [Mem0](../../../../agent-memory-systems/reviews/mem0.md) — rich scoped personalization machinery, but its reviewed implementation lacks behavioral ablation and source-span provenance.
- [Components of A Coding Agent](../../../../sources/components-of-a-coding-agent-raschka.ingest.md) — exact “apparent model quality” wording, but qualitative and coding-agent-wide rather than evidence about retained user intent.
- [Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) — external-memory gains are reported at bundle level without isolating memory, retrieval, instruction engineering, or personalization effects.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — strong causal evidence for whether supplied experience affects behavior, but not a personalization experiment; the useful activation result is already reachable through the source's authored link to the activation note.
- [Per-artifact write briefs](../../../../reference/proposals/archive/per-artifact-write-briefs.md) — shares the retained-intent authority problem but is an unadopted Commonplace-specific representation rather than evidence or a premise for the source's general claim.

## Index Membership

- [Agent memory](../../../../tags/agent-memory-README.md) — candidate for “Boundaries And Failure Modes” or a small evaluation subsection: the source connects activation, authority, carrier choice, and failure attribution in one personalization case.
- [Computational model](../../../../tags/computational-model-README.md) — candidate under “Error Correction & Reliability”: it specializes the assembled-input/interpreter split to memory-backed personalization and gives a component-swap evaluation protocol.
- [LLM reliability](../../../../tags/llm-reliability-README.md) — candidate under “The Taxonomy” or “Architectural Responses”: it shows how an upstream memory change and an interpreter improvement can produce the same visible gain but require different diagnosis.

## Synthesis Opportunities

None. The strongest apparent synthesis — separately addressable memory enables component attribution while parametric or co-adapted personalization entangles carrier and interpreter — is already explicit in the source's evaluation boundary and does not need a new note.

## Maintenance Observations

None

## Flags

None
