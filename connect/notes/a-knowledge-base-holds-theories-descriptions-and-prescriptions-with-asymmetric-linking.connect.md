---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md"
source_has_frontmatter: true
date: "2026-04-11"
depth: standard
---

# Connection Report: Register Asymmetry

**Source:** [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md)

## Discovery Trace

**Index scan:**
- Read [notes index](../../notes/index.md) -- flagged candidates (with reasons):
  - [why-notes-have-types](../../notes/why-notes-have-types.md) -- six roles of the type system; the note's claim #3 says types may encode layers
  - [document-types-should-be-verifiable](../../notes/document-types-should-be-verifiable.md) -- base type + traits model; connects to the type-to-layer deduction claim
  - [linking-theory](../../notes/linking-theory.md) -- links as decision points; the asymmetric linking claim adds a new constraint not captured
  - [link-strength-is-encoded-in-position-and-prose](../../notes/link-strength-is-encoded-in-position-and-prose.md) -- weighted graph; asymmetry adds a direction constraint on top of strength
  - [distillation-status-determines-directory-placement](../../notes/distillation-status-determines-directory-placement.md) -- directory boundary as "distilled into a procedure" parallels prescription layer
  - [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) -- reach distinguishes facts from theories; directly supports the reach-for-theories claim
  - [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) -- methodology->skill distillation is the theory->prescription path
  - [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- library/workshop split is orthogonal to theory/description/prescription
  - [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- five writing styles; per-collection conventions would use different style mixes
  - [short-composable-notes-maximize-combinatorial-discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- "the library exists for co-loading"; this is a theory-layer design principle
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) -- genre transfer argument; connects to the philosophical-traditions mapping
  - [an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) -- unifying theory; three-layer note adds a content-type dimension to the three-property framework
  - [claim-notes-should-use-toulmin-derived-sections-for-structured-argument](../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) -- Toulmin sections are theory-layer conventions specifically
  - [areas-exist-because-useful-operations-require-reading-notes-together](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) -- areas organize by operation needs; layers organize by content kind and quality goal

**Topic indexes:**
- Read [types-index](../../notes/types-index.md) -- confirmed why-notes-have-types and document-types-should-be-verifiable as relevant; the type system index does not discuss content-kind layers
- Read [document-system-index](../../notes/document-system-index.md) -- confirmed the note should belong to this tag area; the index currently does not mention the three-layer framework
- Read [foundations-index](../../notes/foundations-index.md) -- the source note is tagged `foundations` but not listed in this index; candidate for index membership

**Semantic search:** via qmd
- query "three content layers theory description prescription linking asymmetry quality goals" --collection notes -n 15 -- top hits:
  - a-knowledge-base-holds-theories-descriptions-and-prescriptions... (93%) -- self
  - index.md (50%) -- the directory listing, not a note connection
  - charting-the-knowledge-access-problem-beyond-rag.md (38%) -- rejected: discusses access problem decomposition, not content-layer taxonomy
  - type-system-enforces-metadata-that-navigation-depends-on.md (33%) -- already flagged from index scan
  - quality-signals-for-kb-evaluation.md (33%) -- weak: quality signals catalogue but doesn't address content kinds
- query "epistemology ontology praxeology knowledge types transferable claims" --collection notes -n 10 -- top hits:
  - self (93%), title-as-claim (50%), first-principles-reasoning (38%) -- all already linked
- query "three content layers theory description prescription linking asymmetry" --collection sources -n 10 -- top hits:
  - context-engineering-ai-agents-oss-ingest.md (88%) -- discusses content categories in context files; the five categories (guidelines, rules, information, metadata, context) partially overlap with theory/description/prescription
  - the-second-brain-trap-ingest.md (50%) -- rejected: about activation, not content-layer taxonomy
- query "per-collection writing conventions quality criteria types" --collection instructions -n 5 -- top hits:
  - writing.md (93%) -- the writing guide; currently covers only notes, not per-collection conventions

**Keyword search:**
- rg "asymmetr|theory.*description.*prescription|three.*layer" -- hits only in the source note itself and unrelated asymmetry references (error-correction asymmetry in scheduler notes)
- rg "fidelity|executability|per-collection" -- hits in the source note; `fidelity` used in other notes (unit-testing, automated-synthesis, sift-kg) in different senses; `executability` only in source and skills-derive-from-methodology; no other note uses `per-collection`
- rg "epistemology|ontology|praxeology" -- hits only in the source note and minimum-viable-vocabulary (uses "ontology" in a different sense)

**Link following:**
- From [why-notes-have-types](../../notes/why-notes-have-types.md): links to document-types-should-be-verifiable, human-writing-structures-transfer-to-llms, structured-prompt-gains-do-not-establish-distribution-selection, structured-output-is-easier-for-humans-to-review. The output-quality cluster (three independent arguments) would benefit from knowing they apply specifically to the theory layer
- From [linking-theory](../../notes/linking-theory.md): links to title-as-claim, link-strength, agents-navigate-by-deciding-what-to-read-next. The linking theory does not currently address directional constraints between content kinds
- From [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md): links to constraining/distillation definitions, discovery, first-principles-reasoning. The reach-as-theory-quality-axis claim directly supports the three-layer note's argument that reach is theory-specific

## Connections Found

- [linking-theory](../../notes/linking-theory.md) -- **extends**: the linking theory models links as decision points with strength and type, but does not address directional constraints between content kinds; the three-layer note adds a new linking constraint (theories must not depend on descriptions) that the linking theory should account for, since it affects which links are valid, not just how strong they are

- [why-notes-have-types](../../notes/why-notes-have-types.md) -- **extends**: the note's practical consequence #3 claims the type system may already encode layers (note/structured-claim -> theory, spec -> description, instruction -> prescription); if true, types serve a seventh role the overview doesn't list -- content-layer identification -- and the type-to-layer deduction would affect how agents use type information for routing

- [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) -- **grounds**: the reach distinction (facts vs theories as low-reach vs high-reach accumulation) directly supports the three-layer note's claim that reach is the quality axis for the theory layer specifically, not a universal goal; the three-layer note's "theory = optimized for reach" is a corollary of this note's framework

- [distillation-status-determines-directory-placement](../../notes/distillation-status-determines-directory-placement.md) -- **extends**: proposes "distilled into a procedure" as the directory boundary for instructions; the three-layer note provides the theoretical backing -- prescriptions have executability as their quality goal, and the directory boundary is the prescription layer's physical location in the file tree

- [an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) -- **extends**: the unifying theory identifies three properties (discoverable, composable, trustworthy) and five operations; the three-layer note adds a content-kind dimension -- different layers weight these properties differently (theory layer weights composability and reach; description layer weights discoverability and fidelity; prescription layer weights trustworthiness/executability)

- [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- **extends**: the five writing styles map differently across the three layers -- prescriptions should favor prescriptive/prohibitive styles (tight constraint), descriptions should favor descriptive style (document what exists), theories should favor explanatory style (warrant-bearing); the three-layer framework provides a principled basis for per-layer style allocation

- [claim-notes-should-use-toulmin-derived-sections-for-structured-argument](../../notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) -- **extends**: the Toulmin structure is specifically a theory-layer convention -- it enforces argument quality, which is the quality goal for theories (reach + sound reasoning); descriptions and prescriptions would need different structural templates optimized for their respective quality goals (fidelity sections for descriptions, step-sequence sections for prescriptions)

## Bidirectional Candidates

- [linking-theory](../../notes/linking-theory.md) <-> source -- **extends**: the source note adds a constraint axis (directional validity based on content kind) that the linking theory's framework needs to accommodate; the linking theory provides the decision-cost model that explains *why* the asymmetry matters (invalid theory->description dependencies create a specific kind of navigation trap)

- [why-notes-have-types](../../notes/why-notes-have-types.md) <-> source -- **extends**: if types encode layers, then the type overview should acknowledge layer identification as a role; conversely, the three-layer note's open question about whether a separate `layer` field is redundant is answerable from the type system design

- [distillation-status-determines-directory-placement](../../notes/distillation-status-determines-directory-placement.md) <-> source -- **grounds**: the three-layer note provides theoretical grounding for the distillation note's hunch; the distillation note provides operational evidence (the notes/instructions directory split already instantiates the theory/prescription boundary)

## Raw Text Candidates

None

## Rejected Candidates

- [charting-the-knowledge-access-problem-beyond-rag](../../notes/charting-the-knowledge-access-problem-beyond-rag.md) -- discusses how agents find knowledge (access modes) but not what kinds of knowledge exist; the conceptual spaces don't overlap enough for a specific connection
- [quality-signals-for-kb-evaluation](../../notes/quality-signals-for-kb-evaluation.md) -- catalogues graph-topology and content-proxy signals but doesn't distinguish signals by content kind; a future version might evaluate whether quality signals should be layer-specific, but that connection doesn't exist yet
- [link-strength-is-encoded-in-position-and-prose](../../notes/link-strength-is-encoded-in-position-and-prose.md) -- link strength addresses how committed a link is, which is orthogonal to the directional constraint the three-layer note introduces; the notes share vocabulary (links, graph) but address different linking dimensions without genuine interaction
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) -- the genre transfer argument is relevant to theory-layer conventions specifically, but the connection is already captured by the more specific claim-notes-should-use-toulmin route; adding a direct link would duplicate without adding information
- [short-composable-notes-maximize-combinatorial-discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- "the library exists for co-loading" applies to all library notes; the three-layer note doesn't change what composability means, just which layer optimizes for it; too obvious to help traversal
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- the library/workshop distinction is about value trajectory (accumulates vs consumed), which is orthogonal to the theory/description/prescription distinction (quality goals within the library layer); noting both exist is not a connection
- [areas-exist-because-useful-operations-require-reading-notes-together](../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) -- areas organize by operation needs, layers organize by content kind; both justify grouping but for different reasons and at different scales; the parallel is weak
- [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) -- the methodology->skill distillation is an instance of the theory->prescription path, but the note's focus is on the distillation mechanism itself, not on the content-layer taxonomy; the connection is already captured via the distillation-status note
- [minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer.md) -- uses "ontology" in the vocabulary-set sense, not in the philosophical sub-discipline sense the source note uses; keyword overlap without conceptual connection

## Index Membership

- [foundations-index](../../notes/foundations-index.md) -- the source note is tagged `foundations` but not listed in the curated section; it introduces a structural claim about all KBs (the three-layer split) that constrains writing conventions, type design, and linking rules -- foundational enough for the curated list
- [document-system-index](../../notes/document-system-index.md) -- the source note is tagged `document-system`; its per-collection convention consequence directly affects document conventions and the type-to-layer deduction affects the type system
- [types-index](../../notes/types-index.md) -- the type-to-layer deduction (practical consequence #3) is directly relevant; the type system may encode layers, which would add a layer-identification role to the type system overview

## Synthesis Opportunities

The three-layer note's claim that "the type system may already encode layers" (consequence #3), combined with [why-notes-have-types](../../notes/why-notes-have-types.md)'s six roles and [document-types-should-be-verifiable](../../notes/document-types-should-be-verifiable.md)'s base-type + traits model, implies a synthesis: **if content layer is deducible from type, then per-layer quality goals (reach/fidelity/executability) become type-deducible quality goals** -- enabling layer-specific validation without a new field. This synthesis would connect the type system to the quality-goal framework in a way neither note does alone. Worth developing only after the three-layer note's open question ("can layer be mechanically deduced from type?") has evidence.

## Flags

- The source note is `status: seedling` with `tags: [document-system, foundations]`. The `foundations` tag is appropriate given the note's scope (applies to all KBs), but the seedling status means load-bearing `grounds` relationships from other notes should be flagged. The connections found here are additive (`extends`, `grounds` from the source to other notes, not the other direction).
- The note has five existing Relevant Notes links. None of the connections found here duplicate those links.
