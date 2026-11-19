---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/methodology-enforcement-is-constraining.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Methodology enforcement is constraining

**Source:** [Methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md)

## Discovery Trace

**Description and title listing scans:**

- Ran `rg -N --no-heading -m1 '^# ' <destination>/ --glob '*.md'` and `rg -N --no-heading '^description:\\s*' <destination>/ --glob '*.md'` across every destination authorised by `kb/notes/COLLECTION.md`: `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. These scans surfaced instruction consumption, validation placement, event hooks, hard gates, mixed representational forms, and harness enforcement as the useful candidate clusters. No search scores were available because discovery used `rg`.

**Topic indexes:**

- Read the curated heads for all authorised destinations: `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.
- Read `kb/notes/constraining-README.md` and `kb/notes/learning-theory-README.md`. The source is already listed in the constraining index; the learning-theory index routes it through `covered_by: [constraining, ...]`. Neither index permitted skipping the scoped tag scans, so discovery also ran `rg -l '^tags:.*\\bconstraining\\b' kb/notes/ --glob '*.md'` and the equivalent `learning-theory` query, followed by description extraction.

**Body search:**

- Notes: ran `rg -n -i 'activation (rule|reliability)|unreliable activation|explicit invocation|required (gate|validator)|event hook'`, `rg -n -i 'instruction.{0,50}(skill|hook|script|validator)|skill.{0,50}(hook|script|validator)|hook.{0,50}(script|validator|warning|block)'`, and `rg -n -i 'partial order|single ladder|fixed ladder|independent (axis|axes)|two[- ]axis|orthogonal axis'` over `kb/notes/`. Kept the activation-regress, objective-fidelity, and diagnostic-informativeness candidates below. Rejected similarly worded notes whose axes concern orchestration, autonomy, or memory retrieval rather than enforcement.
- Reference: ran `rg -n -i 'trigger|activation|invocation|event[- ]fired|warning hook|required validator|blocking hook'`, `rg -n -i 'instruction.{0,60}(validator|gate|script|skill)|validator.{0,60}(instruction|gate)|enforcement.{0,60}(meaning|response|routing|activation)'`, and `rg -n -i 'partial order|independent (axis|axes)|separate (axis|axes)|separat(es|ing) (meaning|enforcement|maintenance)'` over `kb/reference/`. Kept ADR 026 as a concrete case where a formal response rule remains reactively activated; rejected ADR 005 because it addresses placement criteria rather than the independence of activation and response semantics.
- External-system reviews: searched `kb/agent-memory-systems/` for instruction/skill/hook combinations, activation with gates or triggers, hard versus soft gates, and mixed natural-language/symbolic forms. Searched `kb/agentic-systems/` for `instruction|skill|hook|trigger|gate|validator|enforc|natural-language|symbolic`. Kept Ars Contexta and Eigenius because each documents a configured combination that breaks a total artifact-type ladder.
- Sources: searched `kb/sources/` for instruction/skill/hook combinations, hard and soft constraints, runtime enforcement, deterministic triggers, and mandatory versus optional validators. Kept the harness-engineering ingest for its retained source evidence about moving standards into structural tests and linters. The Agent Behavioral Contracts and Natural-Language Agent Harnesses ingests were rejected because their current analyses depend on the old ladder and retain no source quotes for the narrower two-axis claim.
- Instructions: ran the title and description scans plus `rg -n -i 'activation rule|explicit invocation|required (gate|validator)|event hook|warning hook|blocking hook|response semantics|enforcement strength' kb/instructions/ --glob '*.md'`. No procedure adds ordering, defaults, or stopping conditions that this methodology note leaves open, so no `operationalized-from` candidate was kept.
- External web prospecting was skipped. The source introduced no unresolved named external dependency, and the connect scope was satisfied by authorised local destinations.

**Link following:**

- Followed [Promotion selects for unreliable activation, and the regress ends only at an external firing event](../../../../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) into its activation-memory neighbourhood. It supplies the mechanism by which explicit triggering terminates routing regress rather than merely repeating the source's table.
- Followed [Exact implementation does not validate a requirement](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) into its codification and specification-mining neighbours. It directly supports the source's warning that deterministic enforcement can encode the wrong proxy.
- Followed [Error messages that teach are a constraining technique](../../../../notes/error-messages-that-teach-are-a-constraining-technique.md) into its recovery and frontloading neighbours. It adds diagnostic informativeness as an independent response property and already carries a return link to the source.
- Read [Instruction](../../../../types/instruction.md), [ADR 026](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), the [Ars Contexta review](../../../../agent-memory-systems/reviews/arscontexta.md), and the [Eigenius analysis](../../../../agentic-systems/reviews/eigenius.md) in full or through their load-bearing sections. Each contains an actual configured consumption path, not merely shared vocabulary.
- Read the retained quotes and analysis in [Harness engineering: leveraging Codex in an agent-first world](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md). Its evidence supports response-semantic hardening, but does not by itself establish independence from activation; the candidate below is limited accordingly.

## Connections Found

- [Promotion selects for unreliable activation, and the regress ends only at an external firing event](../../../../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) — **mechanism**: explains why reliable activation requires an external firing event and why merely adding another interpreted routing layer does not end the regress.
- [Exact implementation does not validate a requirement](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **grounds**: supplies the premise behind the source's proxy caveat by separating fidelity to an encoded rule from the validity of the requirement that rule represents.
- [Error messages that teach are a constraining technique](../../../../notes/error-messages-that-teach-are-a-constraining-technique.md) — **extends**: adds diagnostic informativeness as a response property that can vary without changing either the trigger or the blocking semantics.
- [Instruction](../../../../types/instruction.md) — **evidenced-by**: the instruction type contract provides a concrete Commonplace case of the activation distinction by requiring a consumer, channel, and firing condition and treating an unconsumed instruction as inert.
- [ADR 026: Tag README type with completeness and coverage marks](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — **evidenced-by**: its marks have formal validation semantics but are checked reactively only when a marked README is validated, instantiating strong response semantics with invocation-dependent coverage.
- [Ars Contexta](../../../../agent-memory-systems/reviews/arscontexta.md) — **evidenced-by**: one deployed system combines auto-loaded context, natural-language skills, event hooks, warning validators, and scripts, showing that package names alone do not determine one enforcement order.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — **evidenced-by**: its manually loaded natural-language protocol coexists with a hard justification gate on one named load boundary, making response force and activation coverage independently inspectable.
- [Harness engineering: leveraging Codex in an agent-first world](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — **evidenced-by**: its retained practitioner evidence documents standards moving from instruction and manual cleanup into structural tests and linters, corroborating the response-hardening path and its bounded coverage.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Verifiability gradient](../../../../notes/verifiability-gradient.md) — concerns the cost and strength of checking an outcome, not whether an enforcement rule fires; the source's existing automation-boundary link already carries the useful part of this neighbourhood.
- [Capability placement should follow autonomy readiness](../../../../notes/capability-placement-should-follow-autonomy-readiness.md) — ranks placement by autonomy readiness and could reintroduce the artifact-type ladder the source now rejects.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — uses activation for memory retrieval and behavioural uptake rather than activation of an enforcement rule.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — shares the anti-ladder shape but applies it to orchestration architecture; the analogy adds no enforcement-specific mechanism.
- [ADR 005: Quality check placement](../../../../reference/adr/005-quality-check-placement.md) — gives historical placement criteria but does not establish the separation between activation and response semantics.
- [Agent Behavioral Contracts: formal specification and runtime enforcement for AI agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) — its stored analysis maps hard and soft constraints onto the superseded linear gradient, and its quotes section retains no source passages that independently ground the revised model.
- [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) — supports structured natural-language control but retains no quotes about invocation coverage or the independence of triggering and response semantics.

## Index Membership

None — the source already appears in [Constraining](../../../../tags/constraining-README.md), and [Learning theory](../../../../tags/learning-theory-README.md) deliberately routes it through that covered child index.

## Synthesis Opportunities

- The source, [Error messages that teach are a constraining technique](../../../../notes/error-messages-that-teach-are-a-constraining-technique.md), [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md), and [Exact implementation does not validate a requirement](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) jointly imply that enforcement should be described as a profile rather than a strength: activation coverage, immediate response semantics, diagnostic informativeness, recovery, and fidelity to the real objective can vary separately.

## Maintenance Observations

- The revised source rejects an inherent instruction → skill → hook → script order, but several inbound descriptions still present that sequence as a reliability gradient. Representative stale uses occur in [Ad hoc prompts extend the system without schema changes](../../../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md), [Skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md), [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md), [Constraining](../../../../notes/definitions/constraining.md), [the subtree-scoped write-time contracts proposal](../../../../reference/proposals/where-subtree-scoped-write-time-contracts-live.md), and the two rejected source ingests above. A separate maintenance sweep should distinguish a common maturation path from a total ordering.

## Flags

None.
