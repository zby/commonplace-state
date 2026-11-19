---
description: "Discovery report for possible KB connections from Greenfield et al.'s executable software-factory metamodel"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/greenfield-software-factory-specification-execution-model.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Software factory specification and execution model

**Source:** [Software factory specification and execution model](../../../../sources/.snapshots/greenfield-software-factory-specification-execution-model.md)

## Discovery Trace

**Collection rules and source reading:**

- Read `kb/sources/COLLECTION.md`, `kb/reports/types/connect-report.md`, and the complete retained patent page. The source collection permits links to notes, reference, agent-memory systems, agentic systems, other sources, and already-known external targets; it excludes work and instructions.
- The page contains the complete abstract, description, claims, and publication record used here. Its long citations and legal-history tail were read as capture context, not treated as ontology evidence.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/notes/learning-theory-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The strongest candidates were the deployed-system, fixed-decomposition, work-product/self-improvement boundary, and Compound Engineering analyses. No reference or agent-memory-system artifact needs a direct edge.

**Full title and description listings:**

- Generated fresh complete title and description surfaces for notes (403/401), reference (159/158), agent-memory systems (175/173), agentic systems (14/12), and sources (348/348).

**Body search:**

- `rg -n -i '(factory schema|task template|work product|software factor|factory develop|product develop|solution develop|product famil|domain[- ]specific|operative factory|learning loop|computational closure)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!kb/sources/.snapshots/**'` found no existing durable note with the patent's schema/viewpoint/work-product/task/workstream metamodel. It surfaced the Greenfield 2003 and 2007 ingests, the deployed-system and fixed-decomposition notes, the self-improvement boundary-case note, and Compound Engineering.

**Link following and candidate evaluation:**

- Followed [the deployed-system unit](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). The patent makes the production unit an IDE extension plus a schema, editors, task and workstream templates, and assets; this is a concrete compound-system case, not evidence that the patented system learns.
- Followed [fixed-decomposition learning](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Factory developers define the domain-specific viewpoints, work-product types, tasks, processes, and assets in advance, while product developers instantiate and enact them. This identifies an externally supplied update-space boundary but does not establish that the boundary is mistaken.
- Followed [the self-improvement boundary cases](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md). The patent's distinction between the product as a collection of work products and the factory machinery that produces it gives a source-specific instance of the note's general product-versus-organization test.
- Followed [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md) and the two Greenfield ingests. The patent adds exact task/work-product instance semantics to the mature Greenfield account; it does not add a computational learning or successor-selection process.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the patented factory is an operative IDE extension comprising schema-organized editors, task and workstream templates, reusable assets, and cross-viewpoint operations used throughout specification, development, deployment, and maintenance.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: a human factory developer supplies the family-specific viewpoints, work-product types, task templates, workstreams, and assets within which a development team produces products; the source exposes that fixed specialization boundary without testing alternatives.
- [The self-improving system definition classifies its boundary cases without ad hoc exceptions](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- **is-evidence-for**: the patent expressly represents a product as a collection of work products and separately represents the factory schema, templates, editors, and assets that govern their production, giving the product-versus-production-organization distinction a software-factory instance.
- [Ingest: Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) -- **compares-with**: the 2007 essay speaks broadly of activities acting on artifacts, while the patent distinguishes work-product types from instances, task templates from enacted tasks, and workstream templates from customized processes.
- [Ingest: Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) -- **compares-with**: the earlier paper packages a software schema and production assets in a software template; the patent instead calls the schema plus editors, task templates, and assets collectively the factory, so later synthesis must version rather than silently merge the vocabulary.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: the patented factory fixes a target product type and a typed lifecycle production model, while the modern plugin is analysed as a broader artifact-mediated workflow whose installed prompt corpus normally remains outside its project-level loops.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The self-improving system definition classifies its boundary cases without ad hoc exceptions](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md) → source -- **evidenced-by**: the source provides a precise historical case where product work products and behavior-determining factory machinery are different objects.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: the factory system makes multiple schema-organized representations, tools, workflows, and reusable assets jointly operative in later production.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- rejected as source evidence: the patent assigns factory definition to a factory developer and product production to a development team, but it does not define computational closure or a learning transition.
- [Program theory sustains search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- rejected as a direct edge: both cover lifecycle work, but the patent specifies production metadata rather than the note's explanatory mechanism for search under delayed feedback.
- Patent-page cited and citing documents -- rejected from local prospecting: their titles are page metadata, not already-ingested primary sources read for this task.

## Index Membership

None

## Synthesis Opportunities

- The 2003 paper, 2007 essay, and this patent support a versioned reconstruction: the early software template packages family-specific schema and assets; the mature schema relates concerns, artifacts or work-product types, activities or tasks, and assets; the operative factory is the configured environment in which a team enacts those tasks to create and maintain family members. Vocabulary changed, but all three accounts keep human factory authorship separate from product development.

## Maintenance Observations

None

## Flags

- Do not treat `activity` and `task`, `artifact` and `work product`, or the 2003 `software template` and the patent's collective `software factory` as exact synonyms without identifying the source version.
- The source says experience can motivate refinement of a factory, but it assigns specification to a factory developer and supplies no evidence-responsive computational update or adoption mechanism. Feedback-supported evolution is not learning closure.
