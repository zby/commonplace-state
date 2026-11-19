---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/naur-equates-machine-execution-with-formulated-criteria.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connect Report: Naur's inexpressibility argument does not by itself make program theory human-only

Source: [Naur's inexpressibility argument does not by itself make program theory human-only](../../../../notes/naur-equates-machine-execution-with-formulated-criteria.md)

Source SHA-256 verified at discovery start and after report save: `3084b9e0a2fcfe551bc284d2103fcd3852d9a8d3d161e586e25414276bb7825b`.

## Discovery Trace

- Read the repo-local `cp-skill-connect` instructions, the connect-report type contract, the source artifact, and the source collection contract at `kb/notes/COLLECTION.md`.
- Read destination collection contracts for every authorized local destination family: `kb/reference/`, `kb/sources/`, `kb/instructions/`, `kb/types/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`.
- Read collection README entry points and the source tag READMEs for `foundations` and `context-engineering`.
- Because neither relevant tag README declared complete coverage for this source, ran by-tag description sweeps for `foundations` and `context-engineering`.
- Ran repository-local title and description sweeps across `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/types/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- Ran focused text searches for Naur, program theory, formulated criteria, machine-effective execution, learned recognizers, classifiers, rubrics, decision premises, semantic work, codification, transfer tests, and rationale-retention vocabulary.
- Reopened likely matches, checked candidate paths exist, and applied both source-side and destination-side collection label constraints before classifying candidates.

## Connections Found

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **mechanism**: the source's learned-recognizer argument is a concrete case of semantic work being paid elsewhere rather than removed. A trained recognizer can execute a similarity judgment without a human-readable rubric because the judgment has been relocated into learned regularities.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- **extends**: the source separates absence of human-formulated criteria from absence of machine-effective determination. This note generalizes the split into the difference between settled methodology, computational allocation, explicit representation, and codified execution.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **contrasts**: the source weakens the inference from unformulated criteria to human-only execution, while this note explains why governed retention can still require explicit artifacts even when tacit or parametric competence can execute a task.
- [Use tests and decomposition transfer locally, but rationale makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **extends**: the source reads Naur's compiler case as a bounded transfer failure rather than an in-principle proof. This note develops the same boundary: guided work with the current theory-holder may transfer situated understanding, but retained rationale is what makes later transfer testable.
- [Fix what the executor cannot determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **extends**: the source's three transfer tests ask whether a recipient receives the premises needed for independent modification judgment. This note turns that distinction into an author/executor rule for retaining goals, constraints, and unrecoverable decisions.
- [Codify versus LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- **extends**: the source distinguishes human-formulated rubrics from machine-effective recognition. This note gives the operational heuristic for when a judgment should become deterministic code and when a model-mediated heuristic can remain the right substrate.
- [The AlexNet moment](../../../../sources/02-the-alexnet-moment.ingest.md) -- **evidenced-by**: the source's learned-recognizer countermodel would benefit from a concrete ML case where hand-crafted visual criteria/features gave way to learned representation and classification.

## Bidirectional Candidates

- Source <-> [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- outbound **extends**, return **grounds**: the closure note gives the general allocation vocabulary, and the Naur note supplies the specific formulated-criteria bridge that prevents "not human-formulated" from collapsing into "not computationally executable."
- Source <-> [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- outbound **mechanism**, return **exemplifies**: the semantic-work note names the mechanism, and the Naur note is a reusable example involving program theory, learned recognition, and absent explicit rubrics.
- Source <-> [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- outbound **contrasts**, return **contrasts**: together they preserve a useful distinction between executable competence and governable, addressable retention.

## Reverse-edge Candidates

- [ADR 077: Content routing by regeneration source and consumer](../../../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md) -> source -- **rests-on**: the ADR says the routing criterion follows from Naur's theory-building problem plus the interpreter/retained-text split. Under the reference collection contract, a direct `rests-on` edge to this source note would make the narrowed Naur premise visible.
- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) -> source -- **compares-with**: the ingest applies Naur to LLM-mediated code maintenance and records that the source's "code and documentation can never capture Theory" claim is stronger than its examples prove. The target note supplies the tighter comparison point.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md), [Documentation generates the system rather than describing it](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md), [Theory-mediated self-improvement needs both interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), and [Design rationale must preserve unregenerable decision premises](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) are not new outbound candidates because the source already carries the relevant authored links or explicit inline connection.
- [Specific intent may out-yield local rationales; facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) is related to unregenerable premises, but the connection is better mediated through the already-linked design-rationale note.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) is relevant to allocating understanding, but it is an application-level strategy note. The stronger direct candidates are the closure, semantic-work, and codification-heuristic notes.
- [Unformalized improvements need a pre-formal stage in the loop](../../../notes/formal-only-gates-have-distinct-admission-and-warrant-limits.md) and [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) are broader automation-boundary claims. They overlap the source's transfer-test frame but do not add a more specific relation than the accepted candidates.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md), [Moving the interpretation/enforcement boundary requires coverage first](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md), and [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) concern instruction-following and conformance boundaries rather than Naur's formulated-criteria bridge.
- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) has a shared anti-overreach structure: evidence from a human case does not by itself fix the engineered boundary. The source-specific Naur bridge is stronger than this general analogy-transfer edge.
- [Recognition, not linking, is the hard problem in knowledge systems](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) shares recognition vocabulary, but its subject is KB connection recognition, not recognizer execution or program-theory transfer.
- [The Bitter Lesson selects production methods, not representational form](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) and [Treat continual learning as representational form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) bear on learned representations, but they would pull the source toward ML history rather than its main Naur/program-theory claim.
- No direct `kb/instructions/`, `kb/types/`, `kb/agent-memory-systems/`, or `kb/agentic-systems/` link survived the label and relevance checks.

## Index Membership

- [Foundations README](../../../../tags/foundations-README.md) -- candidate membership: the source is tagged `foundations` and belongs near rationale, design method, or human/LLM boundary material because it narrows a premise used in later KB-methodology arguments.
- [Context engineering README](../../../../tags/context-engineering-README.md) -- candidate membership: the source is tagged `context-engineering`; include it only if the README wants artifacts about interpreter-plus-retained-artifact boundaries, not just retrieval and routing mechanics.

## Synthesis Opportunities

- A narrow synthesis could combine this source, [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md), and [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md): machine-effective execution, governed retention, and human-formulated explanation are different thresholds. This may already be mostly covered by the existing closure and retention notes; write only if a remaining gap is visible after linking.

## Maintenance Observations

- Several existing link texts still use an older source-note title, including [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md), [Design rationale must preserve unregenerable decision premises](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md), and [Theory-mediated self-improvement needs both interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). The links still resolve, so this is a later cleanup signal, not a connect-report blocker.

## Flags

None.
