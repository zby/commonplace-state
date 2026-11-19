---
description: "Discovery report for possible KB connections from Jack Greenfield's 2007 mature software-factory ontology"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/greenfield-mass-customizing-software-factories-2007.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Mass Customizing Solutions with Software Development Factories

**Source:** [Mass Customizing Solutions with Software Development Factories](../../../../sources/.snapshots/greenfield-mass-customizing-software-factories-2007.md)

## Discovery Trace

**Collection rules and source reading:**

- Read `kb/sources/COLLECTION.md`, `kb/reports/types/connect-report.md`, and the complete snapshot. The source collection assigns durable connections to the matching ingest and authorizes notes, reference, agent-memory systems, agentic systems, and other sources as destinations. Work and instructions are excluded. External prospecting was skipped because no already-known external comparison beyond the captured source was supplied.
- The snapshot has no `tags`, so no source-tag-matched README or by-tag description sweep applied.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/notes/learning-theory-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The theory heads exposed the deployed-system, fixed-decomposition, bootstrap, requirements-change, and closure candidates. The agentic-system head exposed Compound Engineering. The reference and agent-memory heads yielded no direct target.

**Full title and description listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and description surfaces with `rg '^description:' kb/<destination>/ --glob '*.md'` for `notes` (403 titles, 401 descriptions), `reference` (159/158), `agent-memory-systems` (175/173), `agentic-systems` (14/12), and `sources` (345/345).
- The exact mature schema ontology—concerns, artifacts, activities, assets, factory authors and users, specialization, and composition—has no existing definition or theory note. The nearest candidates concern whole deployed systems, update-space boundaries, and modern factory claims.

**Body search:**

- `rg -n -i '(viewpoint|stakeholder concern|factory develop|solution develop|factory composition|factory speciali|life cycle artifact|software factory template|software factory schema)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!kb/sources/.snapshots/**'` found no retained Greenfield ontology. Generic `viewpoint` hits and domain-specific system descriptions were rejected as vocabulary-only matches.
- `rg -n -i '(software factor|product famil|factory schema|factory template|domain[- ]specific|bootstrapp|production asset)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` surfaced [the hand-crafted bootstrap](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md), [fixed-decomposition learning](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [the deployed-system unit](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), and [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md).
- The same query over tracked source ingests surfaced [the 2003 Greenfield and Short paper](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) as the lineage anchor once drafted, plus [Fluent](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md), [Software Factories: Emerging Architectures](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md), and the SlopCodeBench reports as modern uses.
- `rg -n -i '(computational closure|operational closure|learning loop|Bitter Lesson|deployed system)' kb/notes --glob '*.md'` found the reconciliation cluster. Greenfield describes two interacting human feedback processes, not a computationally closed learning loop, so closure notes were evaluated as contrasts rather than source-backed attributions.

**Link following and candidate evaluation:**

- Followed [the deployed-system unit](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). Greenfield's 2007 definition explicitly includes a specialized development and runtime environment, processes and content, lifecycle artifacts, tools, reusable runtimes, and schema-mediated operations; it is a strong historical case for evaluating production machinery as an operative system rather than reducing the object to generated code.
- Followed [fixed-decomposition learning](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Greenfield says unanticipated product variation can force adaptation of the product-line asset base and assigns that work to factory developers, while ordinary solution developers customize and apply it. This is a precise external-specialization boundary, but the source neither implements learning nor argues that fixedness is mistaken, so the relationship is comparative.
- Followed [the hand-crafted bootstrap](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md). Unlike the 2003 paper, this article emphasizes two separate development processes, their feedback streams, and factory specialization/composition. It strengthens the object-level/factory-level distinction but supplies no computational outgrowth claim.
- Followed [changing requirements](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md). Greenfield includes changing circumstances, requirements, technologies, customer feedback, defect reports, and feature requests in lifecycle operation, but does not separate genuine change from prior ambiguity; the source should not be treated as evidence for that narrower causal distinction.
- Followed [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md) and compared the current factory ingests. The mature Greenfield account remains family-specific and gives schema, template, author/user, lifecycle, composition, and specialization semantics that current “factory” usage often omits.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: Greenfield defines the operative factory as a specialized development and runtime environment containing schema-organized tools, processes, content, partial lifecycle artifacts, and reusable runtimes. Solution production and later maintenance depend on this compound machinery, not only on a model or generated program.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: Greenfield's factory exposes a declared family-specific decomposition through viewpoints, artifacts, activities, and assets, and handles previously unanticipated product variation by having factory developers adapt the asset base. The comparison identifies the family-specialization boundary while preserving that the source is not a learning result.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **compares-with**: Greenfield assigns factory construction and change to a separate factory-development process fed by domain-practitioner knowledge and solution-developer feedback. This supplies the established human-authored specialization process that the note's domain-extensibility criterion would have to move inside a learning loop.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: Greenfield's ontology requires family-specific assets in an installable template governed by a dynamic schema, whereas Compound Engineering is analysed as a modern lifecycle workflow over product and project-knowledge artifacts. The comparison prevents a shared label from erasing different production objects and specialization boundaries.
- [Ingest: How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) -- **compares-with**: Fluent places retained project Expertise and follow-up work in a modern accepted-change loop, while Greenfield separates product work from factory-development feedback and leaves asset revision to factory developers. The pair locates the proposed successor-factory step beyond ordinary feedback-supported factory evolution.
- [Ingest: Software Factories: Emerging Architectures and Why Frontier Labs Should Care](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md) -- **compares-with**: Rosen's current usage emphasizes outer-loop control, bounded workers, durable state, and verification; Greenfield's mature ontology additionally fixes the production family's scope and locates family knowledge in a schema and template.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: the mature software-factory definition is a historical compound-system case spanning representations, tools, workflow, runtime assets, and lifecycle operations.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: after the ingest exists, the note can use Greenfield's explicit human factory-developer adaptation path as a bounded case of how unanticipated variation is handled outside ordinary product configuration, without implying the factory's decomposition is mistaken.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) → source -- **see-also**: checking the original family/schema/template account helps readers interpret why the modern analysis's use of “software factory” is an extension rather than an inherited exact definition.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- rejected as source evidence: Greenfield's two feedback processes distinguish actors and products, but both retain human decision makers and the article never defines closure.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- rejected as unsupported specificity: the article recognizes changing requirements, circumstances, and technologies but does not distinguish world change from late interpretation error.
- [System-definition artifact](../../../../notes/definitions/system-definition-artifact.md) -- rejected as a direct edge: many factory assets would satisfy Commonplace's authority-path definition when made operative, but Greenfield's asset category also includes product fragments and reference content, so the vocabularies are not coextensive.
- SlopCodeBench factory reports -- rejected from the ontology map because they evaluate long-horizon code maintenance but do not identify a product family, schema, template, or factory-development process.
- Commonplace reference and agent-memory-system matches -- rejected because they contain only generic configuration, domain, or viewpoint vocabulary and offer no useful factory-level comparison.

## Index Membership

None

## Synthesis Opportunities

- The 2003 and 2007 Greenfield sources together support a future two-process reconstruction: product-family knowledge becomes schema and template assets through factory development; solution developers then configure and apply those assets across a family member's lifecycle. Feedback can cross from product use into factory development without making the latter computationally closed. The durable synthesis belongs in the requested theory/definition notes, not this cache report.

## Maintenance Observations

None

## Flags

- “The products of factories can be composed” and “factories can be composed” are separate claims in the article. Product composition combines portions of an ultimate deliverable; factory composition combines constituent viewpoints. Do not collapse them.
- Greenfield's dynamic schema can change per family-member feature selection, while factory specialization changes the base factory's viewpoint/artifact/activity/asset structure. Configuration and specialization therefore remain distinct despite both changing a schema instance or shape.
