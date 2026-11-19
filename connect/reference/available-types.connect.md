---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/reference/available-types.md"
source_has_frontmatter: true
date: "2026-04-12"
depth: standard
---

# Connection Report: Available Types

**Source:** [Available Types](../../../reference/available-types.md)

## Discovery Trace

**Index scan:**
- Read [reference index](../../../reference/index.md) -- flagged candidates:
  - [type-loading](../../../reference/type-loading.md) -- already linked from source; complementary mechanism doc
  - [architecture](../../../../reference/architecture.md) -- describes the installed `kb/types/` and `kb/*/types/` layout that available-types catalogs
  - [instruction-generation](../../../../reference/instruction-generation.md) -- init scaffolding creates the type directories listed in available-types
  - [scenario-architecture](../../../../reference/scenario-architecture.md) -- decomposition references "load the relevant type definition from `kb/types/` or `kb/*/types/`"
  - [storage-architecture](../../../../reference/storage-architecture.md) -- already links to available-types; documents the storage layer for type definitions
  - [collection definition](../../../../reference/definitions/collection.md) -- already links to available-types; collections own or inherit type contracts
  - [control-plane-goals](../../../../reference/control-plane-goals.md) -- distinguishes framework-provided type system from per-installation goals
- Read [notes index](../../../notes/index.md) -- flagged candidates:
  - [why-notes-have-types](../../../../notes/why-notes-have-types.md) -- already links to available-types; the "why" to this note's "what"
  - [document-types-should-be-verifiable](../../../../notes/document-types-should-be-verifiable.md) -- already links to available-types; theory note
  - [directory-scoped-types-are-cheaper-than-global-types](../../../../notes/directory-scoped-types-are-cheaper-than-global-types.md) -- already links to available-types; economic argument for the global/local split
  - [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](../../../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) -- already links to available-types; the type ladder this note catalogs
  - [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- already links to available-types; observes workshop types missing from current inventory
  - [claim-notes-should-use-toulmin-derived-sections-for-structured-argument](../../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) -- already links to available-types; `structured-claim` extends the catalog
  - [instructions-are-typed-callables](../../../../notes/instructions-are-typed-callables.md) -- already links to available-types; skill signatures reference these types
  - [methodology-enforcement-is-constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- mentions document type maturation following the gradual-typing pattern
  - [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- already links to available-types; observes types are oriented toward reference knowledge
  - [related-systems/thalo-type-comparison](../../../../agent-memory-systems/thalo-type-comparison.md) -- already links to available-types; external type system comparison
  - [type-system-index](../../../notes/type-system-index.md) -- already links to available-types as "document-classification"
  - [document-system-index](../../../notes/document-system-index.md) -- already links to available-types
  - [title-as-claim-enables-traversal-as-reasoning](../../../../notes/title-as-claim-enables-traversal-as-reasoning.md) -- already links to available-types as a multi-claim spec example
  - [generate-instructions-at-build-time](../../../../notes/generate-instructions-at-build-time.md) -- about generating skills at build time; relevant because types also use template generation

**Topic indexes:**
- [type-system-index](../../../notes/type-system-index.md) -- available-types is already listed as "document-classification"; the curated sections group exactly the theory notes that explain the catalog's design choices. No new candidates beyond what the index scan found.
- [document-system-index](../../../notes/document-system-index.md) -- already links to available-types. Curated sections point to the same type-system theory cluster.

**Semantic search:** via qmd
- query "type system document types validation schema structural contracts" (notes) -- top hits:
  - [document-types-should-be-verifiable](../../../../notes/document-types-should-be-verifiable.md) (93%) -- already linked; the theory note underpinning the catalog
  - [types-give-agents-structural-hints-before-opening-documents](../../../../notes/types-give-agents-structural-hints-before-opening-documents.md) (44%) -- not linked from available-types but linked indirectly via why-notes-have-types
  - [methodology-enforcement-is-constraining](../../../../notes/methodology-enforcement-is-constraining.md) (33%) -- mentions document type maturation paralleling gradual-typing; connection to available-types is indirect
- query "directory-scoped types local type definitions template instructions schema" (notes) -- top hits:
  - [directory-scoped-types-are-cheaper-than-global-types](../../../../notes/directory-scoped-types-are-cheaper-than-global-types.md) (93%) -- already linked
  - [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) (50%) -- surveys always-loaded context; types live in this space but connection is generic
- query "type maturity ladder text note structured-claim base type traits" (notes) -- top hits:
  - [title-as-claim-enables-traversal-as-reasoning](../../../../notes/title-as-claim-enables-traversal-as-reasoning.md) (93%) -- already linked
  - [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](../../../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) (56%) -- already linked

**Keyword search:**
- rg "available-types" kb/ --glob "*.md" -- 35+ references across the KB. Nearly all existing inbound links use the `[document-classification](../reference/available-types.md)` link text. This is a heavily linked hub node.

**Link following:**
- From [type-loading](../../../reference/type-loading.md): links to ADR-012, ADR-015, ADR-016, collection definition, architecture. All already linked from available-types or from type-loading itself; no new candidates.
- From [architecture](../../../../reference/architecture.md): describes the installed layout including `kb/types/` and `kb/*/types/`. Currently links to type-loading and available-types only indirectly via the layout diagram.
- From [instruction-generation](../../../../reference/instruction-generation.md): describes `commonplace-init` creating the type directories and scaffold. The init step is the mechanism that places the type files available-types catalogs, but this is operational detail, not a meaningful conceptual connection.
- From [control-plane-goals](../../../../reference/control-plane-goals.md): table row "Type system | Framework | kb/*/types/" describes the type system as framework-provided infrastructure. Already acknowledges available-types's territory implicitly.

## Connections Found

The target note already has well-chosen links to its complementary notes (type-loading, note base type, text root type, ADR-013, ADR-012, ADR-015). Scanning the full KB reveals that most type-system-related notes already link *to* available-types rather than the other way around. The existing links section is appropriate for a catalog/reference note -- it points to the mechanism (type-loading) and the decisions (ADRs) rather than to the theory notes that justify the catalog.

New connections worth adding:

- [architecture](../../../../reference/architecture.md) -- **cross-reference**: available-types catalogs the type definitions that architecture shows in the installed layout; architecture describes where type files physically live, available-types describes what those files contain. An agent following the architecture layout diagram benefits from knowing the type inventory.
- [collection definition](../../../../reference/definitions/collection.md) -- **cross-reference**: collections are defined partly by owning or inheriting a type contract; available-types lists which types each collection owns. The collection definition already links to available-types, but the return link from available-types would help an agent reading the catalog understand what "directory-scoped" means operationally.
- [scenario-architecture](../../../../reference/scenario-architecture.md) -- **cross-reference**: the write-a-note decomposition table explicitly lists "Global or collection-local type definitions | kb/types/, kb/*/types/" as a step. Available-types is the catalog of what lives there.

## Bidirectional Candidates

- [architecture](../../../../reference/architecture.md) <-> available-types -- **cross-reference**: architecture already shows the type tree layout; available-types would benefit from linking to architecture for the installed-project context, and architecture would benefit from linking to available-types for the type inventory. Currently neither links to the other directly.
- [scenario-architecture](../../../../reference/scenario-architecture.md) <-> available-types -- **cross-reference**: scenario-architecture references type definitions as a step in the write-note decomposition; available-types is the specific inventory. Neither currently links to the other.

## Raw Text Candidates

None

## Rejected Candidates

- [always-loaded-context-mechanisms-in-agent-harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- surveys always-loaded context, and types are part of the context loading story, but the connection is too generic. The note surveys harness mechanisms broadly; available-types catalogs one specific system's types. An agent gains nothing by following this link.
- [generate-instructions-at-build-time](../../../../notes/generate-instructions-at-build-time.md) -- both involve build-time generation (type templates, skill templates), but the shared concept is "template generation" which is too generic to articulate a specific connection.
- [instruction-generation](../../../../reference/instruction-generation.md) -- `commonplace-init` creates the directories that host type files, but the connection is "init creates everything" rather than something specific about types. An agent reading the type catalog doesn't need to know about the init scaffolding process.
- [control-plane-goals](../../../../reference/control-plane-goals.md) -- mentions the type system as framework-provided infrastructure, but the mention is incidental (one row in a table). No deep connection.
- [methodology-enforcement-is-constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- mentions document type maturation paralleling gradual-typing, but the connection to the catalog is indirect; it connects to the theory of types, not to the inventory.
- [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- observes types are oriented toward reference knowledge, but this is a theory-level observation; the catalog just lists what ships.

## Index Membership

- [type-system-index](../../../notes/type-system-index.md) -- already listed as "document-classification" in the Overview section.
- [document-system-index](../../../notes/document-system-index.md) -- already linked in the Foundations section via "For the live commonplace repo's current type inventory..."

## Synthesis Opportunities

None. The available-types note is a descriptive catalog of what ships. The theory notes that explain *why* the catalog looks this way (why-notes-have-types, directory-scoped-types-are-cheaper, document-types-should-be-verifiable) already exist and are well-connected. No gap between existing notes implies an uncaptured higher-order claim.

## Flags

- **Hub node saturation.** Available-types is already one of the most heavily linked notes in the KB (35+ inbound references). Most type-system theory notes already point to it. The three new connections found (architecture, collection definition, scenario-architecture) are all within the reference collection and are cross-references rather than deep conceptual connections. This is expected for a catalog/inventory note -- it serves as a reference target more than as a source of outbound connections.
- **Stale link text.** Many notes link to available-types using the text `[document-classification]`. The note's title is "Available Types" and it has never been called "document-classification" in its own title or frontmatter. The link text appears to be a legacy reference to a prior title or role. This is cosmetic but could confuse an agent following the link.
