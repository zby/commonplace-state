---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/us20090100406a1-software-factory-specification-execution-model.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Software factory specification and execution model

**Source:** [Software factory specification and execution model](../../../../sources/.snapshots/us20090100406a1-software-factory-specification-execution-model.md)

## Discovery Trace

**Description listing scan:**

- Generated the complete `# ` title surface for `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The only direct historical sequence in the current source collection is the 2003 Greenfield–Short paper and Greenfield's 2007 essay. No current note or reference artifact is dedicated to the software-factory ontology.
- Ran `rg -ni '^description:.*(software factor|product line|domain-specific|domain specific|work product|viewpoint|metamodel|Greenfield)' kb/sources --glob '*.md'`. Kept the 2003 and 2007 Greenfield ingests as versioned vocabulary comparisons. Rejected modern “software factory” sources because their use of the phrase does not resolve this historical metamodel.
- Ran `rg -ni '^description:.*(ontology|metamodel|decomposition|type|artifact|schema|domain|work product)' kb/notes --glob '*.md'` and the same query over `kb/reference/`. The fixed-decomposition note was evaluated but rejected as an outbound source claim: this application discloses a decomposition but supplies no adoption, comparison, or performance evidence for a transfer about learning.
- Ran `rg -ni '^description:.*(ontology|workflow|artifact type|work product|task template)' kb/agent-memory-systems --glob '*.md'` and `rg -ni '^description:.*(software factory|artifact-mediated|workflow|ontology|task)' kb/agentic-systems --glob '*.md'`. Operational Ontology Framework was a keyword-only match. Compound Engineering uses “software factory” for a modern artifact-mediated harness, not for Greenfield's product-family metamodel.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. None provides a narrower curated historical-software-factory head. The sources landing confirms that the authored connection surface belongs in the paired ingest, not this snapshot.

**Body search:**

- `rg -ni 'factory schema|software factory|software factories' <destination> --glob '*.md'` found the two historical Greenfield ingests and modern metaphorical uses. The historical pair was kept; the modern uses were rejected for this source's bounded ontology-disambiguation role.
- `rg -ni 'work product|workstream|task template|viewpoint' <destination> --glob '*.md'` found generic task-template and work-product uses but no artifact that encodes this source's type/instance distinctions.
- `rg -ni 'product[- ]line|domain[- ]specific' <destination> --glob '*.md'` confirmed the 2003 and 2007 product-family context but did not produce a stronger non-source target.
- `rg -ni 'metamodel|ontology' <destination> --glob '*.md'` found generic ontology discussions; none needs this patent application as evidence.

**Link following:**

- Followed the 2003 and 2007 ingests to `the-deployed-system-not-the-model-is-the-unit-of-learning.md`, `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`, `a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md`, and `compound-engineering-plugin.md`. Those artifacts already receive the broader transfer from the earlier historical sources. This application adds terminology precision, not new evidence of learning, adoption, or measured performance.

## Connections Found

- [Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) — **compares-with**: the 2003 paper's `software schema` is a graph of product-family viewpoints with associated DSLs, constraints, and transformations, packaged with processes and tools as a `software template`; the application instead calls a factory schema an instance of a metamodel and separately models viewpoint, work-product type, task template, workstream template, and asset, with a factory developer specifying the schema.
- [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) — **compares-with**: the 2007 essay says a viewpoint defines concerns, artifacts, activities, and assets; the application separates those concepts into viewpoint/view/concern, work-product type/work product, task template/task/workstream, and asset, then defines the runtime product as a collection of work products and applies the factory across specification, development, deployment, and maintenance. These are vocabulary changes and finer type/instance distinctions, not synonyms to harmonize silently.

## Bidirectional Candidates

- [Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) ↔ source — **compares-with**: a return comparison would mark the later shift from software-schema/software-template packaging to an explicit factory-schema metamodel with runtime instances.
- [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) ↔ source — **compares-with**: a return comparison would preserve the source-native `artifacts`/`activities` vocabulary beside the application's `work product`/`task` vocabulary.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — rejected because the application specifies a fixed metamodel but does not test an optimizer, a rival decomposition, adoption, or outcomes; treating the disclosure as evidence for the note would exceed its evidential genre.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — rejected because the shared “software factory” phrase hides different system boundaries; the historical 2003 and 2007 sources already provide the useful counterpoint for that modern analysis.
- [Operational Ontology Framework](../../../../agent-memory-systems/reviews/operational-ontology-framework.md) — rejected as a keyword-only ontology match with no shared source-side type system or lineage.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- A separately named Trafilatura snapshot of the Google Patents HTML page predates this run and omits dependent-claim text while declaring `full-source`. It was preserved but excluded from this discovery and must not be substituted for the complete PDF snapshot.

## Flags

- The source is a Microsoft patent application and design disclosure. Its claimed productivity, predictability, quality, reuse, traceability, and maintenance benefits are proposed effects, not evidence of adoption or performance.
