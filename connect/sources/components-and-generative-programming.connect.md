---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/components-and-generative-programming.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Components and Generative Programming

**Source:** [Components and Generative Programming](../../../../sources/.snapshots/components-and-generative-programming.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg '^description:' kb/notes --glob '*.md'` and filtered for `factory|product line|domain|variab|generat|speciali|closure|learning machinery|decomposition|software production`. The most relevant candidates concern fixed decompositions, domain extensibility, and computational production methods. No existing note retains the generative-programming lineage.

**Topic indexes:**
- Read `kb/notes/tags-README.md`; the Self-improving systems and Learning theory routes cover the target argument, but no curated route currently covers software families, generative programming, or configuration knowledge.

**Body search:**
- Ran `rg -l -i 'domain engineering|application engineering|software product line|product family|generative programming|configuration knowledge|software factory|domain extensib|fixed decomposition' kb/notes kb/articles kb/reference --glob '*.md'`. Existing uses of domain extensibility are program-level claims rather than historical definitions.
- Read the source's transition from one-off systems to system families, its domain/application engineering split, the problem-space/configuration-knowledge/solution-space mapping, its generator pipeline, active-library discussion, and production-process qualification of components.

**Link following:**
- Followed the fixed-decomposition note into the bootstrap and Bitter Lesson notes. Generative programming is a close historical instance of computational product construction from hand-supplied family-specific knowledge, but it does not supply the retained learning transition proposed by those notes.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: the paper makes configuration knowledge the fixed mapping from domain-specific requests to allowed component configurations; generation can automate assembly without expanding that supplied family model.
- [The Bitter Lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **compares-with**: the paper is established prior art for symbolic computational production, but its product-line architecture, components, configuration knowledge, and generator are designed through domain engineering rather than learned from use.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **is-evidence-for**: the source identifies the family-specific structures a domain-extensible successor would have to construct—scope/features, architecture, components, configuration knowledge, and generators—while itself leaving those structures to domain engineers.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) → the future ingest -- **evidenced-by**: the paper bounds ordinary automatic generation as assembly within a previously engineered product line, sharpening the note's distinction between automation and domain extensibility.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- rejected as direct evidence: a reuse-infrastructure feedback loop is mentioned, but the paper neither specifies a retained learning transition nor allocates all required learning decisions computationally.
- [Generate KB skills at build time, don't parameterise them](../../../../notes/generate-instructions-at-build-time.md) -- rejected as keyword-level overlap: both involve generators, but the note concerns installation-time materialization and does not benefit from product-line component-assembly lineage.

## Index Membership

None

## Synthesis Opportunities

- Together with the product-line framework source, this paper separates three levels that later factory theory should preserve: engineering a family-specific production space, configuring one member within that space, and automatically generating/assembling the member. None of those alone is evidence that experience constructs a retained successor production system.

## Maintenance Observations

- The KB lacks a source-grounded distinction between computational product generation and computational development of the machinery that defines the product family.

## Flags

- The paper's phrase `feedback loop from application engineering` must not be upgraded into closed learning: it names reuse infrastructure, not computational retention of experience into successor production machinery.
