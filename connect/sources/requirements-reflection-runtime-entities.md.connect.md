---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/requirements-reflection-runtime-entities.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Requirements Reflection: Requirements as Runtime Entities

**Source:** [Requirements Reflection: Requirements as Runtime Entities](../../../../sources/.snapshots/requirements-reflection-runtime-entities.md)

The target is an immutable snapshot. Every outbound candidate below is for the future name-matched ingest report, not for the snapshot itself.

## Discovery Trace

**Curated heads and scope:**

- Read `kb/sources/COLLECTION.md` and its `Outbound links` section first. It authorises prospecting in `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; excludes `work` and `instructions`; and authorises the already-known external DOI without making the open web a prospecting surface.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags`, so no matching tag-README or by-tag `rg` pass applied. Candidate traversal later reached the selective `self-improving-systems`, `computational-model`, and `foundations` tag heads; none declares `complete: true`.
- Generated each authorised destination's full title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Ran the path-plus-description scan as `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'reflect|runtime|requirement|self-adapt|architecture|address|goal|uncertain|first-class|introspect|self-improv|govern|objective|trade.?off|representation|synchron'` for all five destinations.
- The DOI in the snapshot frontmatter was already-known provenance. Open-web prospecting for the authorised `external` destination was skipped.

**Notes search and evaluations:**

- `rg -n -i 'requirements reflection|runtime (requirements|goals)|requirements as runtime|first-class runtime|goal.{0,40}architecture|architecture.{0,40}goal' kb/notes/ --glob '*.md'` found the exact existing use in [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md). Kept it because the source supplies that synthesis's requirements-reflection structural lineage, and the note already cites the DOI.
- `rg -l -i 'self-representation|causally connected' kb/notes/ --glob '*.md'` plus the title/description surface flagged the reflective-system cluster. Kept [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md), [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md), and [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md): the paper respectively supplies a requirements-specific addressability argument, an aspect-and-operation-specific two-stratum proposal, and a historical statement that runtime representation and synchronization determine possible inspection and intervention.
- `rg -l -i 'uncertaint|multi-objective|utility function' kb/notes/ --glob '*.md'` surfaced many generic decision-under-uncertainty matches. None articulated the paper's specific interactive multi-criteria requirements mechanism better than the retained reflection cluster, so no uncertainty-only note was kept.
- Evaluated and rejected [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md): the paper supplies runtime interpretation and causal synchronization but not empirical theory refinement, independent read-back, or recurrent theory learning. The existing synthesis note already states that boundary.

**Reference search:**

- `rg -l -i 'requirements reflection|runtime (requirements|goals)|goal model|self-representation|causally connected|self-adaptive|introspect|intercession' kb/reference/ --glob '*.md'` returned only Commonplace-specific reflective traces and source-assessment proposals. `rg -l -i 'uncertaint|multi-objective|utility function|goal conflict|goal priorit' kb/reference/ --glob '*.md'` returned review-calibration material rather than a requirements-runtime analogue. These fail the source-to-reference trigger: the paper is theory and an external design proposal, not evidence about a Commonplace selection or shipped state.

**Agent-memory and agentic-system search:**

- `rg -l -i 'requirements reflection|runtime (requirements|goals)|goal model|self-representation|causally connected|self-adaptive|introspect|intercession' kb/agent-memory-systems/ --glob '*.md'` found Cludebot's `self_model` memory type and Exo's memory review. Both were rejected: neither review exposes a requirements model causally synchronized with runtime architecture, and the latter's relevant whole-system mechanism belongs in `agentic-systems`.
- The same query over `kb/agentic-systems/`, followed by `rg -n` over the returned files, kept [Exo](../../../../agentic-systems/reviews/exo.md). It supplies a running contrast on one named axis: Exo has a broad executable self-rewrite surface but no explicit runtime requirements semantics, while this paper proposes a semantically rich goal/requirements surface and synchronization architecture without a realized system.
- `rg -l -i 'uncertaint|multi-objective|utility function|goal conflict|goal priorit' kb/agent-memory-systems/ --glob '*.md'` and the same query over `kb/agentic-systems/` produced only generic uncertainty metadata, ranking, and book-level discussion. No candidate passed the articulation test.

**Sources search and evaluations:**

- `rg -n -i 'requirements reflection|runtime (requirements|goals)|requirements as runtime|first-class runtime|goal.{0,40}architecture|architecture.{0,40}goal' kb/sources/ --glob '*.md'` found the later self-adaptive-systems sources. Kept [Software Engineering of Self-Adaptive Systems](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) because its six-wave account locates runtime models, goals, uncertainty, and control as distinct engineering layers, and kept [Defining Self-adaptive Systems](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) because its later systematic review finds goals and uncertainty still underrepresented in formal definitions.
- `rg -n -i 'self-representation|causally connected|metaobject protocol|self-adaptive system|models@run.time' kb/sources/ --glob '*.md'` kept [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) and [Metaobject Protocols](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md). The first supplies the general declarative-reflection topology that requirements reflection specializes; the second supplies a documented protocol design against which the paper's proposed goal meta-object operations can be compared.
- [The Vision of Autonomic Computing](../../../../sources/the-vision-of-autonomic-computing.ingest.md) was evaluated but rejected: generic MAPE-K adjacency adds less discrimination than Weyns's explicit runtime-model/goal/uncertainty chronology.

**Link following:**

- Followed the existing requirements-reflection DOI from the theory-mediated-system-learning note into its reflective-system and theory-mediated-self-improvement neighbourhood. This confirmed the source as the structural lineage only and prevented overclaiming it as evidence for empirical theory refinement.
- Followed the addressability note to reflective coverage and the reflective-system definition. This separated the paper's strongest contribution (requirements-specific addressability plus requirements/architecture synchronization) from the already-grounded general reflection definition.
- Followed Maes to representational form and reflective coverage, and followed Weyns, the systematic review, and the MAPE-K origin source through their existing self-improving-system links. This preserved Maes as the primary vocabulary anchor while locating the new source as a requirements-specific extension and historical self-adaptation contribution.
- Followed Exo to the theory-mediated-self-improvement note. The neighbourhood confirmed the productive comparison: realized broad self-editability versus semantically explicit but proposed requirements reflection.

## Connections Found

- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -- **abstracted-from**: the note explicitly uses requirements reflection as the structural lineage for making purposes and goals causally available to runtime self-adaptation, while adding the separate empirical theory-refinement mechanism.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- **is-evidence-for**: the paper's central design argument is that reifying requirements lets a system inspect, explain, reason about, and selectively modify them rather than acting only through derived low-level monitors; this is a requirements-specific conceptual precedent for reflective addressability, not evidence that the proposed system was built.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- **is-evidence-for**: the proposed requirements and architecture strata name different represented aspects, expose different operation profiles, and require an explicit synchronization mapping, providing a concrete antecedent for assessing coverage per aspect, operation, and transfer mechanism.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **is-evidence-for**: the paper argues that the richness of the runtime requirements meta-model determines which goal questions and interventions are possible, while synchronization determines whether reassessment can reach running architecture; this supports the note's structural-affordance mechanism as a conceptual precedent rather than an implementation result.
- [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) -- **compares-with**: Maes supplies the general causally connected and declarative-reflection topology; requirements reflection specializes the represented domain to goals and requirements and adds an explicit synchronization problem between requirements and architectural strata.
- [Metaobject Protocols: Why We Want Them and What Else They Can Do](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) -- **compares-with**: both expose selected meta-level operations through a protocol, but Kiczales et al. localize language-semantic intervention while the requirements paper proposes goal/requirement operations and must additionally keep them semantically synchronized with a separate running architecture.
- [Software Engineering of Self-Adaptive Systems](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) -- **compares-with**: the 2010 paper proposes one integration of runtime models, goal-driven adaptation, and uncertainty; Weyns later separates those into distinct waves and places them within a managed-system/managing-system conceptual model.
- [Defining Self-adaptive Systems: A Systematic Literature Review](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) -- **compares-with**: the requirements-reflection agenda makes goals and uncertainty first-class runtime concerns, while the later review finds both dimensions still largely absent from formal self-adaptive-system definitions; together they distinguish an early design agenda from later evidence about the field's unresolved semantic gap.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo realizes a broad, causally operative self-rewrite surface over prompts, tools, and executor code but does not represent requirements and goal trade-offs as first-class runtime entities; the paper supplies that semantic layer and synchronization design but no realized adaptive system.

## Bidirectional Candidates

- [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) <-> future requirements-reflection ingest -- **compares-with**: a return link would give readers the clearest requirements-specific declarative-reflection extension and its cross-stratum consistency problem.
- [Metaobject Protocols: Why We Want Them and What Else They Can Do](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) <-> future requirements-reflection ingest -- **compares-with**: a return link would pair general marked meta-level protocol design with a proposal to expose and manipulate goal/requirement entities through analogous operations.
- [Software Engineering of Self-Adaptive Systems](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) <-> future requirements-reflection ingest -- **compares-with**: a return link would connect Weyns's later field map to a primary proposal spanning its runtime-model, goal-driven, and uncertainty layers.
- [Defining Self-adaptive Systems: A Systematic Literature Review](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) <-> future requirements-reflection ingest -- **compares-with**: a return link would connect the review's documented goal/uncertainty gap to an earlier paper that made those dimensions its explicit research agenda.

## Reverse-edge Candidates

- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -> future name-matched ingest -- **abstracted-from**: replace the current bare DOI landing with the tracked ingest once it exists so the note's structural-lineage claim has a local analysed and groundable source surface.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -> future name-matched ingest -- **evidenced-by**: cite the paper narrowly as a historical requirements-specific statement of the inspect/explain/revise affordance, not as evidence that those benefits were empirically achieved.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -> future name-matched ingest -- **evidenced-by**: cite the two-stratum proposal for its aspect-specific operations and explicit mapping obligation, while keeping the note's cross-form taxonomy as the local inference.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -> future name-matched ingest -- **evidenced-by**: cite the paper as a conceptual precedent for the claim that representation and synchronization structure bound available inspection and correction operations.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflective system](../../../../notes/definitions/reflective-system.md) -- the paper applies computational reflection to requirements but does not improve on Maes as the primary definition and vocabulary source; linking it as another definition anchor would blur application with definition.
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- the source supplies the reflective representation and intervention half only; it does not supply independent empirical read-back, explicit theory revision, or recurrence, and the existing synthesis note already routes this bounded antecedent.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- the paper's complaint that compiled monitors lose links to high-level goals resembles the note's layered path, but it does not establish the note's distinct requirement-to-objective proxy claim.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- the paper treats unforeseen environment and emergent effects as reasons for runtime reassessment but does not distinguish genuine world change from late disambiguation, so it neither supports nor cleanly contrasts the note's mechanism.
- [The Vision of Autonomic Computing](../../../../sources/the-vision-of-autonomic-computing.ingest.md) -- shares self-management and goal-directed adaptation vocabulary, but Weyns supplies the more discriminating comparison by separating runtime models, goals, uncertainty, and control into explicit layers.
- [Cludebot](../../../../agent-memory-systems/reviews/cludebot.md) -- its `self_model` memory type is a lexical match only; the review does not establish a causally synchronized runtime requirements/architecture model.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- its product strategy and self-representation distinction is adjacent, but it has no requirements meta-model or two-way requirements/architecture synchronization mechanism.

## Index Membership

None. The source collection head does not enumerate individual ingests, and note tag READMEs index notes rather than source snapshots or ingests.

## Synthesis Opportunities

None. The higher-order bridge from runtime requirements reflection to fallible theory refinement is already captured by [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md); the remaining candidates supply grounding and comparisons rather than a distinct uncaptured synthesis.

## Maintenance Observations

- The name-matched authored surface `kb/sources/requirements-reflection-runtime-entities.ingest.md` does not exist. The snapshot therefore cannot yet carry any durable connection, and the existing theory-mediated-system-learning note can only cite the external DOI rather than a tracked ingest.

## Flags

- Apply accepted outbound and reverse-edge candidates only after the matching ingest exists. Never author a durable link to `kb/sources/.snapshots/requirements-reflection-runtime-entities.md`.
