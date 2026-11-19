---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/cook-kent-tool-factory-2003.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: The Tool Factory

**Source:** [The Tool Factory](../../../../sources/.snapshots/cook-kent-tool-factory-2003.md)

The snapshot is immutable. The candidates below are for its authored companion ingest report.

## Discovery Trace

**Curated heads and title surfaces:**

- Read `kb/notes/README.md` and its linked `kb/notes/tags-README.md`, plus `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no tag-specific README or by-tag `rg` pass applied.
- Generated each authorised destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, and the same command over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. The notes surface exposed the software-factory, metacircular-interpreter, progressive-constraining, bootstrap, and closure candidates. The sources surface exposed the 2003 software-factory lineage, MDSoFa, generative programming, product-line engineering, program synthesis, and DreamCoder.
- Enumerated path-plus-description surfaces with `rg '^description:' kb/notes/ --glob '*.md'`, and the same command over each of the other four authorised destinations. No similarity scores were available; every candidate below was checked from its actual body.

**Notes body search:**

- `rg -n -i -e 'tool factor(y|ies)|software factor(y|ies)' kb/notes/ --glob '*.md'` found [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md), whose recursive-construction section is the strongest theory landing.
- `rg -n -i -e 'domain[- ]specific language|language famil(y|ies)|language design|metamodel' kb/notes/ --glob '*.md'` confirmed that the software-factory note owns the family-definition and metamodel boundary; other hits used DSLs only as examples.
- `rg -n -i -e 'bootstrap(p|ped|ping)?|self-host|metacircular|meta-circular|computational closure|methodological closure' kb/notes/ --glob '*.md'` surfaced the self-hosting, hand-crafted-bootstrap, and closure notes. The metacircular-interpreter note passed on the compiler-versus-interpreter axis; the bootstrap and closure notes were rejected as stronger claims the paper does not establish.
- `rg -n -i -e 'generated code|code generation|tool generation|generator|interpreter|rule checker|abstract syntax' kb/notes/ --glob '*.md'` surfaced [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md). Cook and Kent's interpreted-rule experimentation followed by possible static generation is a useful non-LLM comparison, but not evidence for the note's repeated-run criterion.

**Reference body search:**

- `rg -l -i -e 'tool factor(y|ies)|software factor(y|ies)' kb/reference/ --glob '*.md'` and `rg -n -i -e 'tool factor(y|ies)|language designer|design tool generator|language for designing languages' kb/reference/ --glob '*.md'` returned no content candidate.
- `rg -l -i -e 'domain[- ]specific language|language famil(y|ies)|language design|metamodel' kb/reference/ --glob '*.md'` found only a validation-extension proposal, while `rg -l -i -e 'bootstrap(p|ped|ping)?|self-host|metacircular|meta-circular|computational closure|methodological closure' kb/reference/ --glob '*.md'` found Commonplace-specific frame and trace documents. None gives a reader a useful current-system comparison to this external tool architecture.

**Agent-memory body search:**

- `rg -n -i -e 'tool factor(y|ies)|language designer|design tool generator|language for designing languages' kb/agent-memory-systems/ --glob '*.md'` returned no hits.
- The broader `rg -l -i -e 'bootstrap(p|ped|ping)?|self-host|metacircular|meta-circular|computational closure|methodological closure' kb/agent-memory-systems/ --glob '*.md'` returned initialization uses and [Closure-SDK](../../../../agent-memory-systems/reviews/Closure-SDK.md). These concern memory bootstrap or a product name, not language-definition-driven tool generation, so this destination yielded no candidate.

**Agentic-systems body search:**

- `rg -l -i -e 'tool factor(y|ies)|software factor(y|ies)' kb/agentic-systems/ --glob '*.md'` found [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md), while `rg -n -i -e 'tool factor(y|ies)|language designer|design tool generator|language for designing languages' kb/agentic-systems/ --glob '*.md'` returned no hits. Compound Engineering's project-workflow sense of software factory is already compared through the general software-factory note and is too different for a direct edge here.
- `rg -l -i -e 'bootstrap(p|ped|ping)?|self-host|metacircular|meta-circular|computational closure|methodological closure' kb/agentic-systems/ --glob '*.md'` found Exo and the AI-agent book, but their self-modifying harness and coding-agent bootstrap mechanisms do not share the paper's language-family generator.

**Sources body search:**

- `rg -l -i -e 'tool factor(y|ies)|software factor(y|ies)' kb/sources/ --glob '*.md'` surfaced the historical software-factory cluster. `rg -n -i -e 'tool factor(y|ies)|language designer|design tool generator|language for designing languages' kb/sources/ --glob '*.md'` isolated MDSoFa's explicit tool-factory function.
- `rg -l -i -e 'domain[- ]specific language|language famil(y|ies)|language design|metamodel' kb/sources/ --glob '*.md'` found the Greenfield/Short source, MDSoFa, generative programming, the later patent ontology, and DreamCoder. Greenfield/Short and MDSoFa passed as direct historical comparisons; DreamCoder passed as the learned-language counterpoint. The remaining sources were broader family/product or lifecycle accounts.
- `rg -n -i -e 'software factories can be used to produce|factory can produce|bootstrapp|recursive construction|recursive factory|self-host|metacircular' kb/sources/ --glob '*.md'` confirmed Greenfield/Short's human-directed recursive factory construction and MDSoFa's generated factory assets. Smith and Maes concern causally connected computational reflection rather than self-generation and were rejected.
- The only known external target was the snapshot's canonical PDF URL. External prospecting was not performed. A separate body `derived-from` edge was rejected as redundant because the future ingest's required `source:` metadata already supplies that direct origin.

**Link following:**

- Followed the software-factory synthesis note to Greenfield/Short, Greenfield 2007, the patent execution model, product-line engineering, generative programming, and MDSoFa. The first and last give the closest before/after context for this paper; the wider lifecycle sources remain reachable through the synthesis note.
- Followed Greenfield/Short to its hand-crafted-bootstrap and Compound Engineering comparisons. That neighborhood confirmed that Cook and Kent add mechanism-level detail to recursive factory construction without adding evidence-responsive acquisition of the family definition.
- Followed MDSoFa to program synthesis and the fixed-decomposition note. MDSoFa retained the direct comparison because it emits tool-specific modeling environments from supplied metamodels and expertise; program synthesis was rejected as a much broader construction-from-intent survey.
- Followed the metacircular-interpreter note to codification, methodology enforcement, and meta-decision settlement. These sharpen the compiler-versus-interpreter comparison, but the paper does not ground the LLM-specific claims of those neighboring notes.
- Followed DreamCoder's learned-DSL analysis through its formal-domain and oracle limits. The retained comparison is only about who revises the operative language definition, not a claim that DreamCoder generates language tooling or that Cook and Kent describe learning.

## Connections Found

- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) -- **is-evidence-for**: Cook and Kent supply a detailed family-scoped tool architecture and an explicit language-designer bootstrap, strengthening the note's recursive factory-construction account while leaving the language definition, fragments, patterns, and framework human supplied.
- [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../notes/llm-executed-methodologies-are-metacircular-interpreters.md) -- **compares-with**: the paper gives a concrete compiler-style self-hosting arrangement in which a formal language definition generates its own designer, whereas the note characterizes natural-language methodology as repeatedly interpreted and only partially codified.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- **compares-with**: Cook and Kent keep well-formedness rules interpreted while a language designer experiments, then permit static generation after the language definition is fixed; this shares the delayed-commitment axis without establishing the note's LLM or repeated-run criterion.
- [Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) -- **compares-with**: Greenfield and Short provide the broader schema-template-factory ontology and human product-line roles, while Cook and Kent provide the internal language-family tool generator and the matching recursive bootstrap mechanism.
- [MDSoFa: A Model-Driven Software Factory](../../../../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md) -- **compares-with**: both derive modeling tools or environments from supplied language-level definitions and allow factory-producing outputs, but MDSoFa reports an implemented metamodel/expertise pipeline and makes its remaining human design inputs more explicit.
- [DreamCoder: growing interpretable knowledge with wake-sleep Bayesian program learning](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- **compares-with**: both center a domain-specific language as an operative symbolic layer, but Cook and Kent generate tools from a human-authored language definition while DreamCoder revises its language from task solutions under a description-length gate.

## Bidirectional Candidates

None. Return links should be evaluated after the matching tracked ingest exists; no durable artifact should link to this local snapshot.

## Reverse-edge Candidates

None. Durable reverse links should target the matching tracked ingest after it exists, never this ignored snapshot.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- Cook and Kent use *bootstrap* for regenerating tooling from a supplied definition, not for an evidence-responsive loop that learns past its starting structure; the retained self-hosting comparison and Greenfield lineage expose this distinction without implying support for the stronger claim.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- the paper identifies human designers and generated components, but it neither defines an improvement pathway nor evaluates closure over its consequential decisions.
- [Components and Generative Programming](../../../../sources/components-and-generative-programming.ingest.md) -- its generator materializes family members from configuration knowledge rather than generating a language's tool suite; the broader software-factory synthesis already carries the useful family-engineering relation.
- [A Framework for Software Product Line Engineering](../../../../sources/framework-for-software-product-line-engineering.ingest.md) -- its domain/application lifecycle split is relevant background but adds no direct language-tool or self-bootstrap mechanism beyond the retained software-factory note.
- [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) -- the later lifecycle, specialization, and composition ontology is useful downstream context, but Greenfield/Short is the closer contemporaneous comparison for this chapter-derived tool-factory architecture.
- [Software Factory Specification and Execution Model](../../../../sources/us20090100406a1-software-factory-specification-execution-model.ingest.md) -- its viewpoint, work-product, task, and workstream type/instance model concerns product execution rather than language-designer generation.
- [Program Synthesis](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) -- it surveys search under supplied intent and program spaces; Cook and Kent start from a substantially specified language and address generation of its tools, so the direct edge would be too broad.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- both use *software factory* language, but Compound Engineering's project workflow, retained knowledge, and agent loops do not share the target's language-family generator; the ontology note is the clearer bridge.
- [Closure-SDK](../../../../agent-memory-systems/reviews/Closure-SDK.md) -- the name match is lexical only; this memory SDK does not instantiate language-definition-driven tool generation or Cook and Kent's bootstrap.
- [Reflection and Semantics in Lisp](../../../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) -- Smith's distinction between metacircular modeling and causally connected reflection is useful vocabulary, but Cook and Kent claim generated self-bootstrap rather than reflective runtime access to the tool factory's own execution.

## Index Membership

None

## Synthesis Opportunities

- Cook and Kent, MDSoFa, and DreamCoder suggest a two-stage architecture not yet stated at language-tool granularity: an evidence-responsive process could revise a family-defining language, while a deterministic generator rematerializes the dependent designer, serializer, checker, interpreter, and translators. [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) already distinguishes acquisition from construction at the broader factory level; any new note would need to add the dependency-regeneration and cross-version compatibility mechanism rather than restate that boundary.

## Maintenance Observations

None

## Flags

- Split candidate for later theory extraction: the source independently presents a generated designer architecture, an interpreted-versus-generated rule strategy, and a self-bootstrap claim. The ingest can retain one source record, but those mechanisms should not be forced into one future claim note.
