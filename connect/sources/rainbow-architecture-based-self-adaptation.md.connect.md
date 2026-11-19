---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/rainbow-architecture-based-self-adaptation.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Rainbow: Architecture-Based Self-Adaptation with Reusable Infrastructure

**Source:** [Rainbow: Architecture-Based Self-Adaptation with Reusable Infrastructure](../../../../sources/.snapshots/rainbow-architecture-based-self-adaptation.md)

## Discovery Trace

**Contracts and source reading:**

- Read the source snapshot in full, plus `kb/sources/COLLECTION.md`, `kb/sources/types/snapshot.md`, `kb/reports/COLLECTION.md`, and `kb/reports/types/connect-report.md`. The snapshot is immutable, and the source collection assigns its authored outbound surface to the matching ingest. No matching `kb/sources/rainbow-architecture-based-self-adaptation.ingest.md` exists.
- The paper's distinct connection surfaces are its external runtime architectural model, closed-loop monitoring and repair, split between reusable infrastructure and system-specific adaptation knowledge, fixed style/operator/strategy vocabulary, and two-system evaluation with stated access, centralization, and timescale limits.

**Description and title listing scans:**

- Read the curated heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over each authorised destination: `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over all five destinations. Focused the notes listing with `rg -i 'self-adapt|adaptation|self-improv|runtime|control|architect|govern|world model|system model|reus|feedback|closed-loop|behavio(u)?r-determining|system-definition'` and the sources listing with `rg -i 'self-adapt|adaptation|autonomic|requirements-aware|requirements reflection|control plane|control loop|closed-loop|cybernet|runtime model|world model|architectural|reusable|feedback-loop|regulator|self-heal'`.
- The target has no `tags` field, so no tag README or by-tag sweep applied.

**Body search:**

- Notes: ran `rg -n -i 'self-adapt|self-adaptive|adaptation'`, `rg -n -i 'external control|control loop|closed-loop|feedback loop'`, `rg -n -i 'runtime (architectural )?model|architectural model|world model|system model'`, and `rg -n -i 'system-specific|reusable infrastructure|architectural style|adaptation strateg|effectors?|gauges?|probes?'` over `kb/notes/ --glob '*.md'`. These searches found the six retained note candidates below. They also surfaced weaker definition, derivation, and localized-retention matches rejected below.
- Sources: ran `rg -n -i 'Rainbow|Garlan|architecture-based self-adapt'`, `rg -n -i 'MAPE-K|autonomic manager|self-adaptive'`, and `rg -n -i 'runtime (model|requirements)|external control|feedback loop'` over `kb/sources/ --glob '*.md'`. No prior local Rainbow reference was found. The searches led to the four retained source comparisons and the weaker source matches rejected below.
- Reference: ran `rg -n -i 'self-adapt|self-adaptive|adaptation|runtime model|external control|feedback loop|architectural model|reusable infrastructure' kb/reference/ --glob '*.md'`. Results concerned Commonplace review adaptation or generic link vocabulary, not a shipped-system claim that Rainbow would clarify, so no reference candidate was retained.
- Agent-memory systems: ran `rg -n -i 'architectural model|reusable infrastructure|system-specific adaptation|adaptation strateg|external control|feedback loop|closed-loop|self-adapt|runtime model' kb/agent-memory-systems/ --glob '*.md'`. The only plausible neighborhood was the Swamp memory review, rejected below in favor of the whole-system analysis.
- Agentic systems: ran `rg -n -i 'adapt|self-modif|self-improv|feedback|control|runtime model|architect|strategy|operator|constraint|monitor'` and `rg -n -i 'external (controller|control|manager)|feedback loop|closed-loop|sensors|actuators|architectural model|adaptation strateg|self-adapt'` over `kb/agentic-systems/ --glob '*.md'`. The whole-system Swamp analysis supplied the one retained comparison.

**Link following and candidate evaluation:**

- Read in full the six retained notes, including the runtime-self-modeling note's existing Rainbow DOI citation, and the four rejected notes listed below. Rainbow provides direct evidence for architectural mediation and control surfaces; it provides contrast, rather than direct evidence, where a note requires reject-capable proposal evaluation, revision of the learning decomposition, or persistent revision of retained artifacts.
- Read in full the retained ingests for IBM autonomic computing, the Weyns self-adaptive-systems tour, requirements reflection, and harness cybernetics. Together they place Rainbow between a contemporaneous generic autonomic loop, later field synthesis, later requirements-aware runtime reflection, and a modern agent-harness restatement without collapsing their different claims.
- Read the whole-system and memory-focused Swamp analyses. The whole-system artifact is the useful control-architecture comparison; the memory review's storage and read-back focus is not.
- Skipped external prospecting because the task supplied no external candidate beyond the target itself and the standard pass found sufficient local candidates.

## Connections Found

- [Theory-mediated system learning combines runtime self-modeling with theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -- **is-evidence-for**: Rainbow is the note's architectural-lineage example in full form. Its externally maintained architectural model mediates observations, constraint evaluation, strategy choice, and system change, while its model language, operators, and evaluation policy remain fixed inputs rather than objects of theory revision.
- [Runtime structure determines governance control surfaces](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **is-evidence-for**: Rainbow's probes, gauges, model manager, constraint evaluator, adaptation engine, effectors, and required system hooks concretely show how runtime structure determines what can be observed and corrected. Its centralized controller and longer-timescale scope also expose control-surface limits.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- **is-evidence-for**: Rainbow's runtime architectural model is operational because the constraint evaluator and adaptation engine consume it to choose and execute strategies; the same representation would be inert without that path into action selection.
- [A proposal-selection loop requires search, evaluation, and retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **compares-with**: Rainbow supplies a classic monitor-evaluate-strategy-act control loop, but selects from prescribed strategies rather than exposing reject-capable candidate search and retention of revised adaptive machinery. The contrast helps distinguish a control loop from the note's narrower proposal-selection subtype.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: Rainbow deliberately bounds adaptation with a chosen architectural style, property vocabulary, constraints, operators, strategies, and system concerns. It demonstrates the leverage of that decomposition while leaving its categories outside runtime revision.
- [Retained artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **compares-with**: Rainbow executes retained system-specific adaptation knowledge to repair a live configuration, but does not show evidence-driven revision of that knowledge persisting into later sessions. This marks the boundary between runtime repair by a fixed controller and persistent deployment-time adaptation of the controller's artifacts.
- [The Vision of Autonomic Computing](../../../../sources/the-vision-of-autonomic-computing.ingest.md) -- **compares-with**: IBM's autonomic-element model supplies the contemporaneous generic monitor-analyze-plan-execute-over-knowledge framing. Rainbow specializes that framing through an explicit architectural model, reusable gauges and effectors, system-specific styles and strategies, and measured case studies.
- [Software Engineering of Self-Adaptive Systems: An Organised Tour and Future Challenges](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) -- **compares-with**: the later tour locates runtime models, architecture-based adaptation, control, and assurance across the field's development. Rainbow is an early implemented instance against which that broader retrospective taxonomy can be read.
- [Requirements Reflection: Requirements as Runtime Entities](../../../../sources/requirements-reflection-runtime-entities.ingest.md) -- **compares-with**: requirements reflection proposes making goals and assumptions first-class runtime entities synchronized with reflective architecture. Rainbow keeps requirements implicit in architectural properties, constraints, and strategies, so the pair shows what the later proposal adds to an architecture-based controller.
- [Harness Engineering Is Cybernetics](../../../../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) -- **compares-with**: both accounts organize adaptation around observation, intervention, constraints, and system-specific judgment. Rainbow provides an older concrete architecture and empirical implementation for the control-loop pattern that the harness essay restates for agent systems.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- **compares-with**: both separate reusable runtime or control infrastructure from domain-specific typed models and operators. Rainbow closes a monitored feedback loop over a live architectural model, whereas Swamp compiles authored models and workflows into deterministic execution without an implemented drift-triggered adaptation primitive.

## Bidirectional Candidates

None. A return link cannot target the immutable snapshot as durable authored state, and no matching ingest exists yet.

## Reverse-edge Candidates

None. Several targets could eventually benefit from a return edge to a tracked Rainbow ingest, but proposing durable links to the snapshot would violate the source collection contract.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Derivation and inheritance give starting warrant; evidence earns scope](../../../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md) -- Rainbow's two reuse case studies exercise a scope question, but do not establish the note's general rule for inheriting a claim's warrant.
- [Self-improving system](../../../../notes/definitions/self-improving-system.md) -- Rainbow reconfigures its managed system, but the paper does not establish revision of the controller's own behavior-determining machinery across the definition's required persistence horizon and subsequent use.
- [Localized retention pays where change is sparse in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- Rainbow localizes reusable infrastructure and system-specific knowledge statically; it does not study retention of learned revisions in an addressable layer.
- [Scenario decomposition drives architecture](../../../../notes/scenario-decomposition-drives-architecture.md) -- the two case studies can be described as scenarios, but the paper does not make the note's claim about preserving derivation context through decomposition.
- [Requirements-Aware Systems: A Research Agenda for RE for Self-adaptive Systems](../../../../sources/requirements-aware-systems-research-agenda.ingest.md) -- this substantially repeats the selected requirements-reflection comparison and adds research-agenda breadth rather than independent evidence for the Rainbow connection.
- [Every Good Regulator of a System Must Be a Model of That System](../../../../sources/conant-ashby-every-good-regulator-1970.ingest.md) -- the theorem's qualified event mapping under optimality assumptions is not the same claim as Rainbow's explicit runtime architectural representation; a direct edge would invite equivocation over “model.”
- [The Self-Healing Agent Harness](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) -- its grader-to-ticket-to-fix-to-regate path changes product artifacts through an engineering and release workflow. The selected cybernetics source is the cleaner control-loop comparison.
- [Swamp memory-system review](../../../../agent-memory-systems/reviews/swamp.md) -- the review evaluates storage, indexing, and read-back of retained definitions. The whole-system Swamp analysis carries the relevant runtime and control-architecture contrast.

## Index Membership

None. The target is an immutable snapshot rather than an authored collection item, and no topical index scanned admits snapshot entries directly.

## Synthesis Opportunities

None. The higher-order distinction between fixed-model runtime adaptation and revisable theory-mediated learning is already stated by the retained theory-mediated and proposal-selection notes.

## Maintenance Observations

- The matching authored ingest is absent. Any accepted outbound connection must be authored through `kb/sources/rainbow-architecture-based-self-adaptation.ingest.md`, not through a durable link to this snapshot.
- The theory-mediated system-learning note currently cites Rainbow by DOI because no tracked ingest exists. Once an ingest is created, a future author should evaluate routing that source-dependent claim through the ingest under the source collection's grounding rules.

## Flags

- **Possible split candidate:** the paper supports six note connections across runtime architectural mediation, governance and action control surfaces, and boundaries of fixed-decomposition learning or retention. A future ingest should keep those independent assertions visibly separated even if they remain in one artifact.
- Candidate application is blocked until the authored ingest surface exists; this report does not authorize editing the snapshot.
