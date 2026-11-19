---
description: "Discovery report for possible KB connections from Greenfield and Short's OOPSLA 2003 software-factories paper"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/greenfield-short-software-factories-oopsla-2003.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools

**Source:** [Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools](../../../../sources/.snapshots/greenfield-short-software-factories-oopsla-2003.md)

## Discovery Trace

**Collection rules and source reading:**

- Read `kb/sources/COLLECTION.md`, `kb/reports/types/connect-report.md`, and the complete 1,814-line snapshot. The authored surface belongs on the matching ingest; the snapshot remains immutable. The source collection authorizes prospecting in notes, reference, agent-memory systems, agentic systems, and other sources, while excluding work and instructions. External prospecting was skipped because no already-known external target beyond the captured source was supplied.
- The snapshot has no `tags`, so no source-tag-matched README or by-tag description sweep applied.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/notes/deploy-time-learning-README.md`, `kb/notes/learning-theory-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The note heads exposed the deployed-system, bootstrap, fixed-decomposition, and closure distinctions. The agentic-systems head exposed Compound Engineering as a current system already called a software factory. The reference and agent-memory heads produced no source-specific target.

**Full title and description listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and description surfaces with `rg '^description:' kb/<destination>/ --glob '*.md'` for `notes` (403 titles, 401 descriptions), `reference` (159/158), `agent-memory-systems` (175/173), `agentic-systems` (14/12), and `sources` (345/345).
- Notes flagged [the deployed system](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [the hand-crafted bootstrap](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md), [fixed-decomposition learning](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and [machinery persistence](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md). Agentic systems flagged [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md). Sources flagged the Fluent, current factory-architecture, and SlopCodeBench reports retained below or rejected below.

**Body search:**

- `rg -n -i '(software factor|product famil|factory schema|factory template|domain[- ]specific|bootstrapp|production asset)' kb/notes --glob '*.md'` found that the exact Greenfield vocabulary is not yet reconstructed in notes. It surfaced the bootstrap and machinery notes through their broader learning claims.
- The same query over `kb/reference`, `kb/agent-memory-systems`, and `kb/agentic-systems` found no Commonplace reference or memory-system target and one direct modern comparison, Compound Engineering.
- `rg -n -i '(software factor|product famil|factory schema|factory template|domain[- ]specific|bootstrapp|production asset)' kb/sources --glob '*.ingest.md'` found [Fluent](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md), [Software Factories: Emerging Architectures](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md), and [Why Software Factories Fail](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md). The first two provide useful contrasts in the object and scope of current factory claims; the benchmark report is about maintenance evaluation rather than factory ontology.
- `rg -n -i '(computational closure|operational closure|learning loop|Bitter Lesson|deployed system)' kb/notes --glob '*.md'` located the current theory cluster. Greenfield and Short do not claim a closed learning loop, so closure notes were not retained as evidential targets merely because the occasion asks about closure.

**Link following and candidate evaluation:**

- Followed [the hand-crafted bootstrap](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) to machinery persistence, proposal-selection, fixed-decomposition learning, and repeatable operative revision. Greenfield and Short explicitly call factory-producing-factory construction “bootstrapping,” but human product-line developers still build the next schema and template. This makes the source a high-value prior-art contrast, not evidence that successor production is learned or computationally closed.
- Followed [the deployed system](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) through its scope and evidence. Greenfield and Short define the operative factory as an IDE configured by a family-specific template containing schema-governed process and implementation assets. That is a direct historical instance of behavior depending on a system larger than an executable model or generated program.
- Followed [Compound Engineering](../../../../agentic-systems/reviews/compound-engineering-plugin.md) through its boundary analysis. The current system uses “software factory” for an artifact-mediated product-and-project-knowledge workflow without a declared Greenfield product family, schema, or template. Comparison prevents modern umbrella usage from being silently attributed to the earlier ontology.
- Compared [Fluent](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) and [Software Factories: Emerging Architectures](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md). Fluent adds retained expertise that can alter later shaping and review; Rosen emphasizes outer-loop control, durable state, verification, and human checkpoints. Neither ingest establishes Greenfield's family-scoped schema/template ontology, so both are retained as named modern contrasts rather than continuations by definition.

## Connections Found

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **compares-with**: Greenfield and Short already describe a software factory producing templates for later factories and call the construction “bootstrapping,” but the transition remains work performed by product-line developers using supplied factory-building assets. This separates established recursive factory production from the note's stronger requirement that evidence-responsive learning take over successor production.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the paper's operative factory is an extensible IDE configured with a family-specific schema, processes, DSL tools, frameworks, and other production assets; the produced family member is not the only behavior-determining object.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: the modern plugin analysis uses “software factory” for a lifecycle workflow over product code and project knowledge, while Greenfield and Short reserve the factory for family-specialized production machinery configured by a schema-governed template. The comparison makes the vocabulary shift inspectable.
- [Ingest: How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) -- **compares-with**: Fluent's retained Expertise can influence later shaping and execution, giving a modern product-plus-machinery learning claim absent from Greenfield and Short's human-driven factory bootstrapping.
- [Ingest: Software Factories: Emerging Architectures and Why Frontier Labs Should Care](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md) -- **compares-with**: Rosen defines current factories by outer-loop control, bounded workers, durable state, and verification, whereas Greenfield and Short define them through family-specific production knowledge, schemas, templates, and configured tools. The pair distinguishes lineage from later umbrella usage.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) → source -- **evidenced-by**: after the ingest exists, the note can cite Greenfield and Short as prior art for factory-producing-factory bootstrapping while stating that their transition is not a retained learning transition.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: the configured-IDE definition supplies a historical case where production behavior resides across tools, process assets, implementation assets, and representations rather than one model.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) → source -- **see-also**: a reader benefits from checking the older family-scoped ontology before interpreting the analysis's deliberate modern use of “software factory.”

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- rejected as direct evidence: the paper allocates factory construction to product-line developers and product construction to product developers, but it neither defines learning closure nor tests removal of human decisions.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- rejected as direct evidence: the paper makes family scope and production assets explicit, but it does not study learning inside a fixed update space or evaluate inherited mistakes.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- rejected as redundant with the narrower bootstrap comparison and as unsupported on warrant: Greenfield and Short demonstrate recursion in construction, not reflective selection over whether machinery deserves to persist.
- [Ingest: Why Software Factories Fail: Benchmarking the new frontier](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) -- rejected from the ontology map: it evaluates codebase evolution under incrementally revealed requirements but does not specify the factory's family scope or production machinery.
- Commonplace reference and agent-memory-system candidates -- rejected because their matches concern project-local domain configuration or generic bootstrapping, not software-factory ontology.

## Index Membership

None

## Synthesis Opportunities

- The Greenfield paper plus the bootstrap and closure cluster support a future distinction among **recursive construction**, **retained successor production**, and **computational closure**: a factory can construct another factory without learning, and a learning transition can remain human-open. This should be resolved in the supporting theory notes rather than promoted from this cache report.

## Maintenance Observations

None

## Flags

- Greenfield and Short's 2003 `software schema` is a graph of viewpoints and mappings over family-member specifications; later sources may use `factory schema` for a richer task/work-product/asset metamodel. Do not silently merge the two versions until the later primary source is ingested.
