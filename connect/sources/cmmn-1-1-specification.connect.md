---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/cmmn-1-1-specification.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Case Management Model and Notation (CMMN) Version 1.1

**Source:** [Case Management Model and Notation (CMMN) Version 1.1](../../../../sources/.snapshots/cmmn-1-1-specification.md)

The source is an immutable local snapshot, and no tracked ingest exists yet: `kb/sources/cmmn-1-1-specification.ingest.md` is absent. Every outbound candidate below is a recommendation for that future ingest's `Connections Found` footer. Never author a durable link to the snapshot itself (sources COLLECTION.md).

Source claims used for judging candidates (snapshot sections read: 1 Scope, 4.1 General Concept, 4.2 Target Users, 4.3 Interoperability, 5.4.9 PlanningTable, 8.5 Sentry, 8.6 rules):
- Case management is for work that "cannot be orchestrated by a predefined sequence of Tasks". BPMN suits "predefined, fully specified, repeatable" processes.
- "Planning at run-time is a fundamental characteristic". Design time defines predefined segments plus *discretionary* items (PlanningTables, applicability rules). At run time, workers add discretionary items to the case instance plan.
- Business analysts start with models that are wholly at human discretion. They incorporate "repeatable patterns and best practices" iteratively as rules and predictable task patterns (4.2).
- The execution semantics are guard-stage-milestone (Hull 2010). Sentries are made of OnParts (event) plus an IfPart (condition over the CaseFile). Plan items have lifecycles. ManualActivationRule chooses between Enabled (a human must start the item) and Active. RequiredRule and autoComplete govern when a stage may complete.
- The CaseFile is the shared case data that rules and human decisions read.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md`, outbound section. Prospectable destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/` and `kb/instructions/`. The `external` destination is authorised only for `derived-from` and `see-also`. Labels by destination:
  - theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
  - theory/definitions: `defined-in`
  - sources: `compares-with`, `see-also`
  - agentic-systems: `compares-with`, `see-also`
  - reference: `see-also` only
- `kb/types/connect-report.md`, `kb/theory/README.md`.
- Inbound-side contracts for reverse edges: `kb/theory/COLLECTION.md`, whose labels to sources are `evidenced-by`, `abstracted-from`, `derived-from` and `see-also`, with the "origin is not corroboration" rule. Also `kb/agentic-systems/COLLECTION.md`, whose labels to sources are `derived-from`, `evidenced-by` and `see-also`.

**Description / title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 433 titles. Filtered with `rg -i 'workflow|orchestrat|plan|codif|constrain|human|discretion|automat|state machine|scheduler|operational|executab|runtime|run-time|event|trigger|lifecycle|process|stage|milestone|rigid|flexib|loop|spec|dsl|control'`. Flagged: progressive-constraining, codifying-predictable-choices, scheduler-llm-separation, stateful-tools-hidden-schedulers, bounded-context-orchestration-model, active-work-state, runtime-structure-governance, specification-strategy, orchestration design space, codification/constraining definitions, spec-mining, warranted-transfer, increasing-autonomy-relocates-effort, augmentation-automation-boundary, specification-level-separation.
- `rg -N --no-heading '^description:' --glob '*.ingest.md' kb/sources` filtered by `workflow|orchestrat|human-in|discretion|automation|plan(ning)? at|knowledge work|process model|dynamic|case|statechart|state machine|operationali`. Flagged: model-types-levels-human-interaction-automation (PSW), ironies-of-automation, the-code-is-the-graph, claude-code-dynamic-workflows-docs, operationalism-sep, build-systems-a-la-carte.
- Description reads for about 25 theory candidates were used to accept or reject them (see below).

**Topic indexes / tag heads:**
- Listed `kb/tags/`. Read the descriptions of `computational-model`, `method-guided-action`, `constraining` and `warranted-autonomy`. The `warranted-autonomy` "human–computation allocation" section led to `methodological-and-computational-closure-track-different-changes.md`.
- The snapshot carries no `tags:`, so no by-tag `rg` was run.

**Body search:**
- `rg -il 'cmmn|case management|BPMN|guard-stage-milestone|van der aalst|adaptive case' kb` (excluding snapshots). Hits: only `kb/work/operationalization-executability-automation/exploration.md` (excluded destination) and a critique cache file. No existing KB artifact treats CMMN.
- `rg -l -i 'discretion' kb/theory kb/agentic-systems kb/agent-memory-systems`: codifying-predictable-choices, specification-level-separation, fix-what-the-executor-cant-determine, intent-framed-delegation, plus agentic-systems retained-archive results (rejected as archive noise).
- `rg -l -i 'run-?time planning|planning at run|event-condition|entry criteri|business process|workflow engine|petri|statechart|state machine'` over the same scope: statecharts-and-programs, a-functioning-kb-needs-a-workshop-layer, instantiation-alone, a-guard-against-a-conjectured-requirement, and agentic-systems reviews swamp and agno-agentos.
- `rg -n -i 'state machine|statechart'` in the workshop-layer and instantiation notes. The workshop-layer note's open question "Would validated state machines help agents, or just add ceremony?" is a direct hook.
- `rg -l -i 'state machine|lifecycle state|valid transitions' kb/reference` found only proposals and routing docs. No reference target fits `see-also` usefully.
- `rg -l -i 'human-in-the-loop|approval gate|manual approval' kb/agentic-systems/reviews`: swamp and agno-agentos.

**Link following:**
- specification-level-separation leads to scheduler-llm-separation and llm-mediated-schedulers. This confirmed a cluster about engine-enforced bookkeeping versus judgment, with CMMN as a pre-LLM human-worker instance.
- fix-what-the-executor-cant-determine leads to intent-framed-delegation, which owns the information relation. The candidate stayed on fix-what-the-executor because it carries the per-choice rule that PlanningTables instantiate.
- active-work-state leads to the workshop-layer note. Both were kept on different axes: closure versus formalism.
- progressive-constraining (body read): the extract-stable-patterns mechanism matches CMMN 4.2's analyst iteration.

## Connections Found

All of these are for the future `kb/sources/cmmn-1-1-specification.ingest.md`.

- [CMMN 1.1 specification](https://www.omg.org/spec/CMMN/1.1/) -- **derived-from**: the ingest analysis would be worked out from the normative OMG document (formal/2016-12-01). The external URL is the source already in hand.
- [Progressive constraining commits only after patterns stabilize](../../../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) -- **is-evidence-for**: CMMN 4.2 prescribes this cycle as an industry standard. A case model begins "entirely at the discretion of human participants". Analysts incorporate patterns "as repeatable patterns and best practices emerge" into rules and predictable task patterns. This is a pre-LLM, human-executor instance of commit-after-stabilization. It is origin-independent support with a different executor class, which bounds the claim's scope beyond LLM code generation.
- [A functioning KB needs a workshop layer, not just a library](../../../../theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- **is-evidence-for**: the note asks how much formalism work-in-motion documents need, and whether validated state machines would help. CMMN is a mature formalism for exactly that kind of work. It gives plan-item lifecycles, sentries over shared case data, RequiredRule/autoComplete completion conditions, and run-time-added discretionary items. The workshop layer can treat it as a reference design or a cautionary case when it answers that open question.
- [Statecharts and programs differ in what they show, not compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- **compares-with** (axis: drawing control whose plan is produced at run time). The note says run-time-produced plans read better as programs. CMMN draws them anyway: a static catalogue of possible items plus PlanningTables marking where run-time planning may add them. The instance plan itself is never drawn. The comparison tests where the note's chart/program boundary falls.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with** (axis: design-time fixing versus run-time discretion). CMMN splits design-time predefined segments from discretionary items, bounded by PlanningTables and applicability rules evaluated over CaseFile state. This is a standardized notation for leaving bounded choices to an executor with live case evidence.
- [Specification-level separation recovers scoping before it recovers error correction](../../../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) -- **compares-with** (axis: making discretion boundaries explicit). OpenProse marks judgment holes with `**...**` but leaves enforcement to the LLM. CMMN marks discretionary items in notation and has a conformant engine enforce lifecycle transitions and sentry evaluation. It is a concrete "architectural separation" counterpart for human executors.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) -- **compares-with** (axis: which bookkeeping is engine-enforced and which is left to judgment). CMMN puts plan-item state transitions, sentry satisfaction and stage completion in the engine, and leaves task selection and ordering to human case workers. The split matches the note's "workflow state and defined transitions" in code, with humans in place of the LLM.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- **compares-with** (axis: what the retained model settles versus whether a human decides during operation). ManualActivationRule, discretionary items and UserEventListeners let a CMMN model settle routing and leave the content of a decision to a human. That is methodological routing without computational closure, as the note distinguishes.
- [Preferential codification concentrates less predictable work at the agent boundary](../../../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) -- **compares-with** (axis: residue left at the discretion boundary). CMMN's analysts codify "repeatable patterns", and discretionary items remain for knowledge workers. The spec describes this human-analog residue but measures nothing about it, so the link is a comparison, not evidence.
- [Active work state is not retrospective memory or chat history](../../../../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **compares-with** (axis: closure criteria and current state for unfinished work). The CaseFile plus plan-item lifecycle states, RequiredRule and autoComplete give a formal account of "what is live now and when can this work leave the active set".
- [Codification](../../../../theory/definitions/codification.md) -- **defined-in**: include only if the ingest analysis describes analysts' rule-formalization (4.2) or engine-enforced sentries as codification. The reader may not know the KB's technical sense.
- [Ingest: Parasuraman, Sheridan, Wickens levels of automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with** (axis: per-function human/automation allocation). PSW allocates by stage and level. CMMN allocates per plan item through ManualActivationRule (Enabled versus Active) and discretionary planning, and keeps run-time selection and ordering with humans.
- [Ingest: The code is the graph (Colvin)](../../../../sources/the-code-is-the-graph-2110055467007303729.ingest.md) -- **compares-with** (axis: graph representations of orchestration and resumable state). Colvin argues executable node/edge graphs lose against host-language control flow. CMMN avoids sequence edges entirely: transitions are event and condition sentries over a persistent shared CaseFile. This is a different graph design that his trilemma does not directly address.

## Bidirectional Candidates

- [A functioning KB needs a workshop layer, not just a library](../../../../theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) <-> source -- **evidenced-by** (theory side, once the ingest exists): it would qualify the open question about state-machine formalism with a standardized design for lifecycle-bearing work.
- [Progressive constraining commits only after patterns stabilize](../../../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) <-> source -- **evidenced-by** (theory side): it would bound the claim to more than LLM code generation. The CMMN practice was recorded independently of how the note was built, so it is not `abstracted-from`. The context phrase should say it qualifies or bounds the claim, not that it corroborates it, because no refutation attempt is reported.

## Reverse-edge Candidates

All of these depend on the ingest being written first. Theory notes must link the ingest, never the snapshot.

- [Statecharts and programs differ in what they show, not compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) → future ingest -- **evidenced-by** (qualifies): CMMN is a counter-case in which a drawn notation deliberately covers run-time planning. It does so by drawing the planning *scope* rather than the plan.
- [Specification-level separation recovers scoping before it recovers error correction](../../../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) → future ingest -- **evidenced-by** (qualifies): an established notation in the "architectural separation" regime that still names discretion explicitly.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Swamp](../../../../agentic-systems/reviews/swamp.md) and [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- rejected: both are predefined DAG or workflow engines with approval gates, which is closer to BPMN than to CMMN. Any shared axis (manual gates) is better carried by the PSW comparison.
- [Ingest: Ironies of automation](../../../../sources/ironies-of-automation.ingest.md) -- rejected: CMMN never discusses operator monitoring or deskilling. Keyword-only overlap on "automation".
- [Ingest: Claude Code dynamic workflows docs](../../../../sources/claude-code-dynamic-workflows-docs.ingest.md) -- rejected: its axis is persistence of script-authored orchestrators. CMMN's case models are persistent by design, so the comparison adds nothing beyond the Colvin link.
- [Ingest: Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md) -- rejected: a shared workshop context (operationalization) is not a shared axis with the specification's content.
- [The augmentation-automation boundary is discrimination, not accuracy](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- rejected: CMMN "guides and assists" knowledge workers but says nothing about per-instance discrimination.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- rejected as redundant: the design-time/run-time split is better carried by fix-what-the-executor and progressive-constraining.
- [Warranted transfer leaves people the hardest-to-warrant decisions](../../../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) -- rejected: CMMN gives no warrant account for which items stay discretionary. The codifying-predictable-choices comparison already covers the residue axis.
- [Spec mining is codification's operational mechanism](../../../../theory/spec-mining-as-codification.md) -- rejected: CMMN's pattern incorporation is analyst modeling, not extraction of deterministic verifiers from observed behavior.
- `kb/reference/` -- no candidate. Only `see-also` is authorised, and no reference document covers workflow formalisms or lifecycle engines.

## Index Membership

- Optional source tags for the future ingest (read each head's inclusion condition before assigning): [method-guided-action](../../../../tags/method-guided-action-README.md) for design-time method versus run-time discretion; [warranted-autonomy](../../../../tags/warranted-autonomy-README.md) for per-item human/computation allocation; [constraining](../../../../tags/constraining-README.md) for analyst iteration from discretion to rules. Source tags do not affect membership listings.

## Synthesis Opportunities

Progressive constraining, preferential codification and fix-what-the-executor-cant-determine, read together with CMMN 4.2 and 5.4.9, suggest a candidate higher-order claim. Mature human-work standards already institutionalize a two-phase discretion boundary: a declared discretionary catalogue plus iterative codification of observed patterns. That makes the boundary a design object to version, not a fixed property of the task. This needs testing before promotion; do not create it from this report.

## Maintenance Observations

- `kb/work/operationalization-executability-automation/exploration.md` lists CMMN 1.1 as a candidate with "No matching ingest in targeted searches". Once an ingest exists, the workshop row is stale. Updating it is workshop work, not a library edge.
- No tracked ingest pairs with this snapshot, so `commonplace-validate kb/sources` will likely warn that no ingest matches its URL or checksum until the ingest is written.
- The snapshot's capture note says the embedded PDF title metadata ("Business Motivation Model") is wrong. This needs no action but is worth carrying into the ingest provenance.

## Flags

- No authored surface exists yet. All outbound candidates wait on `cp-skill-ingest kb/sources/.snapshots/cmmn-1-1-specification.md`.
- Keep the workshop's caution in the ingest: a CMMN model does not execute or automate the work itself. Conformance covers notation, modeling and execution semantics of plan-item state, not doing the tasks.
