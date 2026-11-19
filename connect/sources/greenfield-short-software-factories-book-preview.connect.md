---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/greenfield-short-software-factories-book-preview.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Software Factories book preview

**Source:** [Software Factories: Assembling Applications with Patterns, Models, Frameworks, and Tools](../../../../sources/.snapshots/greenfield-short-software-factories-book-preview.md)

## Discovery Trace

**Scope and authored surface:**

- Read the complete snapshot and `kb/sources/COLLECTION.md`. The capture is explicitly `partial-source`: Google Books metadata, publisher description, and partial contents, not the book text. Its durable authored surface must be the matching ingest; no durable artifact should link to or modify the snapshot.
- The source collection authorises prospecting in `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`; `work` and `instructions` are excluded. No external candidate was already supplied, so open-web prospecting was skipped.

**Curated heads and full title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The snapshot has no `tags:` field, so no tag README was applicable.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over all five authorised destinations. The complete surfaces contained 413 note titles, 159 reference titles, 357 source titles, 175 agent-memory titles, and 14 agentic-system titles.

**Description listing scan:**

- Notes: `rg '^description:' kb/notes/ --glob '*.md'` flagged the registered [Software factory](../../../../notes/definitions/software-factory.md) definition and [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md). Factory-learning, successor-factory, and domain-extensibility notes were evaluated but rejected because the preview does not describe evidence-responsive factory revision, operative succession, or acquisition of new family specialization.
- Sources: `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'software factor|tool factor|product line|generative programming|domain-specific|domain specific|model-driven|model driven|factory construction|factory development|production machinery|pattern|framework'` flagged the Greenfield/Short 2003 paper, Cook/Kent Tool Factory proposal, Greenfield 2007 essay, product-line and generative-programming sources, MDSoFa, and current agent-factory sources. The first three and one current-usage comparison were kept; the ingredients and MDSoFa were too indirect for this partial preview.
- Reference: `rg '^description:' kb/reference/ --glob '*.md' | rg -i 'software factor|tool factor|product line|generative programming|domain-specific|domain specific|model-driven|model driven|factory construction|factory development|production machinery|pattern|framework'` returned only generic framework/pattern documentation. `source-adoption-policy.md` was evaluated and rejected as process guidance rather than a connection to this source.
- Agent memory: the equivalent complete description stream filtered by the same terms returned only generic framework reviews. No candidate passed the articulation test.
- Agentic systems: the equivalent description scan plus body search surfaced Compound Engineering only through its body-level use of *software factory*. It was rejected as a direct edge because the stronger Greenfield 2003 source already supplies the historical comparison one hop away.

**Body search:**

- `rg -n -i 'software factor(y|ies)|factory development|factory learning|domain-specific language|domain specific language|model-driven|generative programming|software product line|pattern automation|application assembly|framework-based components' kb/notes/ --glob '*.md'` isolated the software-factory definition and synthesis cluster.
- `rg -n -i 'visual languages|XML as source|source artifacts|reusable assets|rapid assembly|application assembly|framework based components|life cycle metadata|high fidelity model transformation|code generation' kb/notes/ --glob '*.md'` confirmed that only the definition and historical synthesis match the preview's integrated-asset mechanism; generic code-generation hits were rejected.
- `rg -n -i 'software factor(y|ies)|tool factor(y|ies)|domain-specific language|domain specific language|model-driven development|generative programming|software product line|pattern automation|rapid assembly|framework based components|reusable assets' kb/sources/ --glob '*.md'` found the historical source cluster and several modern name matches.
- `rg -n -i 'Software Factories: Assembling Applications|chapter 5|Greenfield and Short|Steve Cook|Stuart Kent' kb/sources/ --glob '*.md'` confirmed the title/author match to the 2003 paper and Cook/Kent's explicit chapter-5 provenance.
- `rg -n -i 'software factor(y|ies)|domain-specific language|model-driven development|generative programming|software product line' kb/reference/ --glob '*.md'` and the same query over `kb/agent-memory-systems/` returned no matches.
- `rg -n -i 'domain-specific language|model-driven development|generative programming|software product line|software factor(y|ies)' kb/agentic-systems/ --glob '*.md'` found only the Compound Engineering use and its README entry.

**Link following:**

- Followed the historical synthesis to the Greenfield/Short 2003 paper, Greenfield 2007 essay, patent execution model, product-line framework, generative-programming paper, Cook/Kent Tool Factory proposal, and MDSoFa. The preview directly names the book program and contributors, but its partial publisher copy cannot carry the detailed ontology or implementation claims recovered from those full sources.
- Followed Cook/Kent to the Greenfield/Short paper and MDSoFa. The Cook/Kent source was kept because it explicitly says its proposal was adapted from chapter 5 of this book and the preview names Cook and Kent as contributors of two DSL chapters.
- Followed the Greenfield/Short paper to Compound Engineering. The indirect route already gives the useful historical-versus-modern comparison, so a direct preview-to-Compound edge was rejected as redundant.

## Connections Found

- [Software factory](../../../../notes/definitions/software-factory.md) -- **defined-in**: supplies the KB's Greenfield-style, family-specific term boundary for a preview whose publisher copy uses *software factory* broadly and promotionally.
- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) -- **is-evidence-for**: the preview's publisher description bears on the synthesis's broad integration claim by naming domain-specific reusable patterns, languages, frameworks, tools, model transformations, code generation, and application assembly; its partial-source scope does not support the synthesis's detailed ontology or claimed outcomes.
- [Greenfield and Short's 2003 software-factory paper](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) -- **compares-with**: the same authors and near-identical title make the full paper the strongest comparison for separating the 2004 book preview's public framing from the paper's precise family/template/schema and recursive-construction account.
- [Cook and Kent's Tool Factory proposal](../../../../sources/cook-kent-tool-factory-2003.ingest.md) -- **compares-with**: the preview names Cook and Kent as contributors of two DSL chapters, while their ingest identifies the proposal as adapted from chapter 5 and exposes the language-family tool-generation mechanism behind the book's high-level description.
- [Greenfield's 2007 mass-customization account](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) -- **compares-with**: the later essay provides the mature lifecycle, schema, specialization, composition, and two-process vocabulary that the 2004 promotional preview only gestures toward.
- [Software Factories: Emerging Architectures and Why Frontier Labs Should Care](../../../../sources/software-factories-emerging-architectures-a-2094075909242294713.ingest.md) -- **compares-with**: the historical preview centers domain-specific languages, reusable assets, models, frameworks, and product assembly, whereas the current essay uses *software factory* for an outer-loop agent control plane with durable state, verification, and human checkpoints.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. The target is an immutable local snapshot and may not receive durable inbound links; any future return edge must target the matching tracked ingest after it exists.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Factory development](../../../../notes/definitions/factory-development.md) -- rejected because the preview discusses building reusable assets but does not distinguish product-level work from later changes to family-level production machinery.
- [Domain-extensible software factory](../../../../notes/definitions/domain-extensible-software-factory.md) -- rejected because automation within a supplied specific problem domain does not establish computational acquisition of specialization for novel domains.
- [A Framework for Software Product Line Engineering](../../../../sources/framework-for-software-product-line-engineering.ingest.md) -- rejected because the preview merely lists software product lines among enabling technologies; the Greenfield/Short full paper already carries the direct integration account.
- [Components and Generative Programming](../../../../sources/components-and-generative-programming.ingest.md) -- rejected because the preview merely lists generative programming and code generation; it supplies no detail with which to compare the source's configuration-knowledge mechanism.
- [MDSoFa](../../../../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md) -- rejected because same-era model-driven factory construction is adjacent, but the preview contains no implementation detail or recursive factory-construction claim to support a specific comparison.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected as a direct edge because its broader modern usage is already reachable through the stronger Greenfield/Short paper, which explicitly compares the two factory boundaries.

## Index Membership

None

## Synthesis Opportunities

- The historical preview, the Greenfield/Short ontology, and current agent-factory accounts suggest a semantic-shift claim: *software factory* now spans family-specific production machinery and outer-loop orchestration systems. A future synthesis should require authors to declare which boundary they mean instead of treating the shared name as equivalence.

## Maintenance Observations

- The registered [Software factory](../../../../notes/definitions/software-factory.md) definition requires family-specific reusable production knowledge, while [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) uses *software factory* for a project workflow without linking the registered term or explicitly marking a broader usage. Review whether that use should be scoped as a modern comparison term.

## Flags

- **Partial-source ceiling:** this snapshot contains metadata, publisher description, and partial contents only. Treat its statements about lower cost, higher speed, reliability, industrial adoption, and replacement of current development methods as promotional claims reported by the preview, not as demonstrated outcomes or claims verified from the book.
- **Immutable target:** apply accepted outbound candidates only to the matching tracked ingest; do not edit or link durably to this snapshot.
