---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Unifying conjecture makes a general and its instances intelligible together

**Source:** [Unifying conjecture makes a general and its instances intelligible together](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md)

## Discovery Trace

### Notes

**Curated heads and listings:**

- Read `kb/notes/README.md`, [Learning theory](../../../../tags/learning-theory-README.md), and [discovery](../../../../tags/discovery-README.md). The discovery head declares `complete: true`, so the by-tag `rg` sweep for `discovery` was skipped. Learning theory declares `covered_by`, not `complete`, so `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` was run.
- Generated the full notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and the full description surface with `rg '^description:' kb/notes/ --glob '*.md'`.

**Body searches:**

- `rg -n -i 'unifying conjectur|singular hypothes|shared (feature|structure)|generative model|known (cases|particulars)|instance(s)? of (a |the )?(general|structure)|lemma|reusable intermediate|recognition cost|naming amortiz|false positive|similarity search' kb/notes/ --glob '*.md'` found the discovery, explanatory-reach, abstraction-boundary, and KB-composability clusters.
- `rg -n -i 'conjectur(e|al|ing)?' kb/notes/ --glob '*.md'` separated the source's unifying form from broader conjecture and testing uses.
- `rg -n 'conjecture-is-seeing-the-particular-as-an-instance-of-the-general|Unifying conjecture makes a general and its instances intelligible together' kb/ --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/**'` enumerated the current inbound neighborhood and exposed one stale description of a removed section.

**Link following and evaluation:**

- Followed the source's existing links to [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md), [information value is observer-relative](../../../../notes/information-value-is-observer-relative.md), and the connect skill. These already supply lifecycle placement, observer-relative recognition cost, and one operationalization, so they were not proposed again as new outbound edges.
- Followed inbound edges from [First-principles reasoning](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), [Short composable notes](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md), [Generality bought to avoid counterexamples](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md), [Known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), [Minimum viable vocabulary](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md), [Raw accumulation](../../../../notes/raw-accumulation-does-not-create-usable-memory.md), and [Theory-mediated learning](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). A reciprocal source-side candidate was kept only where it gives a reader a distinct next step rather than merely mirroring the inbound edge.
- [First-principles reasoning](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) passed because it turns the source's increasing explanatory commitment into a criticizable reach test. [Automated synthesis](../../../../notes/automated-synthesis-is-missing-good-oracles.md) passed because it separates proposing a plausible unification from validating it. [Short composable notes](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) passed because co-presence of independent particulars is a concrete prerequisite for the comparison the source describes.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) passed because recognizing a shared feature or structure does not by itself license warrant or practice to transfer. [Generality bought to avoid counterexamples](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) passed as the nearest contrast between productive and defensive abstraction.
- [Known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) passed because it makes reconstruction of a general from supplied particulars measurable while bounding what that establishes. [Minimum viable vocabulary](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) passed because it develops the source's naming-amortizes-recognition consequence into an observer-relative optimization.
- Rejected [fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) as a separate source-side edge: it already points to the source, and the kept co-presence candidate states the more direct prerequisite. Rejected [abstract an experience into a lesson](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) because it narrows the abstraction problem to trace-derived memory and is already reachable through the kept productive-versus-defensive abstraction target.

### Types

- Read `kb/types/README.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'` and `rg '^description:' kb/types/ --glob '*.md'`, and ran `rg -n -i 'conjectur|hypothes|instance|generali[sz]|abstraction|recognition|shared structure|generative model' kb/types/ --glob '*.md'`.
- The source's declared [Note type](../../../../types/note.md) governs artifact shape, not the unifying-conjecture mechanism. No type target passed the articulation test.

### Reference

- Read `kb/reference/README.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` and `rg '^description:' kb/reference/ --glob '*.md'`, and ran `rg -n -i 'unifying conjectur|singular hypothes|shared (feature|structure)|generative model|instance(s)? of|particular|lemma|abstraction|recognition|similarity search' kb/reference/ --glob '*.md'`.
- Followed [ADR 053](../../../../reference/adr/053-retire-distillation-without-a-successor-term.md), which already links to the source to document a vocabulary migration. That historical routing does not develop or corroborate the source's theoretical claim, so no reference target was kept.

### Agent-memory systems

- Read `kb/agent-memory-systems/README.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`, and ran `rg -n -i 'unifying conjectur|singular hypothes|shared (feature|structure)|generative model|instance(s)? of|particular|lemma|abstraction|recognition|similarity search|semantic neighbor' kb/agent-memory-systems/ --glob '*.md'`.
- Inspected [A-mem](../../../../agent-memory-systems/reviews/a-mem.md). It implements embedding retrieval, generated metadata, links, and neighbor evolution, but does not evaluate whether those operations recover shared features, structures, or generative models. It was rejected rather than treated as evidence for a depth hierarchy the review does not test.

### Agentic systems

- Read `kb/agentic-systems/README.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`, and ran `rg -n -i 'unifying conjectur|singular hypothes|shared (feature|structure)|generative model|instance(s)? of|particular|lemma|abstraction|recognition|similarity search|hypothesis' kb/agentic-systems/ --glob '*.md'`.
- Inspected [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md). Its embedding search is a useful feature-level candidate surface, but the analysis deliberately stops before semantic promotion and does not compare recognition depths. It illustrates a boundary without testing the source's central mechanism, so it was not kept.

### Sources

- Read `kb/sources/README.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'`, and ran `rg -n -i 'unifying conjectur|singular hypothes|shared (feature|structure)|generative model|instance(s)? of (a |the )?(general|structure)|particulars?|lemma extraction|reusable intermediate|recognition cost|naming amortiz|false positives?|similarity search' kb/sources/ --glob '*.md'` plus the ingest-only query `rg -n -i 'conjectur|hypothesis|general structure|shared structure|generative model|instances? of|particulars?|abstraction depth|recognition cost|similarity search|lemma|reusable' kb/sources/ --glob '*.ingest.md'`.
- Followed the authored ingest companions for Self-Revising Discovery Systems, Shannon's Creative Thinking, Emergent Analogical Reasoning, Notes Without Reasons, DiscoverPhysics, FALSIFYBENCH, and GIANTS. The four kept sources each bear on a distinct part of the source: evidence-preserving schema revision, a practitioner generalization operator, controlled relational-structure alignment, and feature adjacency versus articulated semantic connection.
- Rejected DiscoverPhysics because its most relevant hard case is positing an unobserved particular, which the source now expressly uses as the boundary outside unifying conjecture. Rejected FALSIFYBENCH because it measures hypothesis-testing policy in the broader discovery lifecycle rather than the instance-to-general operation. Rejected GIANTS as direct evidence because it reconstructs a known target; the kept [known-target benchmark note](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) carries the necessary qualification more safely.

### Instructions

- Read `kb/instructions/README.md` and `kb/instructions/COLLECTION.md`, generated the full title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` and `rg '^description:' kb/instructions/ --glob '*.md'`, and ran `rg -n -i 'repeated (cases|instances)|conjectur|hypothes|shared (feature|structure)|generative model|instance(s)? of|particular|lemma|abstraction|recognition|similarity search|false positive' kb/instructions/ --glob '*.md'`.
- The source already records the connect skill as an operationalization. [Write an Instruction](../../../../instructions/write-instruction.md) passed independently because it turns repeated instances into a bounded reusable procedure through explicit ordering, parameters, boundary tests, and verification. Because instruction links into notes are normally inverse `rests-on` edges for meta-readers, both instruction-side candidates are recorded below.

### External

- The source collection authorizes the reserved `external` destination, but it is not a prospecting surface. No external target was supplied, no web search was run, and all source evaluation used repo-local snapshots and ingest reports.

## Connections Found

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **extends**: it turns the source's feature/structure/generative ordering into a criticizable test for when a unification has explanatory-reach rather than local adaptive fit.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- **extends**: it separates generating a plausible unifying candidate from validating novelty and truth, locating the expensive part of the source's semantic and generative recognition steps.
- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- **enables**: co-presence of independent particulars under bounded context is the operational prerequisite for comparing them and noticing the shared structure the source describes.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **extends**: recognizing a shared feature or structure creates a candidate relation, while this target supplies the further mechanism-identity test required before warrant or practice may transfer across it.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- **contrasts**: the source's productive abstraction makes a general and its instances more discriminating together, while this target identifies defensive abstraction that widens coverage without adding content.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- **extends**: it turns reconstruction of a general from supplied particulars into a measurable task while marking why success does not establish prospective problem selection or discovery closure.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) -- **extends**: it develops the source's naming-amortizes-recognition consequence into a selection problem over which names reduce extraction cost for a specific observer.
- [Ingest: Self-Revising Discovery Systems for Science](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) -- **evidenced-by**: its typed schema revision and evidence transport provide a worked formal case in which a new general category reorganizes prior particulars, subject to explicit gates; the ingest cautions that the category-theoretic apparatus is not independently validated.
- [Ingest: Creative Thinking](../../../../sources/creative-thinking-by-claude-shannon.ingest.md) -- **evidenced-by**: Shannon's generalization and analogy operators independently articulate movement from a specific problem through a structurally similar solved problem to a broader class, while remaining practitioner testimony rather than experimental evidence.
- [Ingest: Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md) -- **evidenced-by**: a controlled synthetic task finds analogical transfer depends on relational-role alignment rather than entity similarity, bearing directly on the source's shared-feature versus shared-structure distinction within the ingest's synthetic-task boundary.
- [Ingest: Agentic Note-Taking 23: Notes Without Reasons](../../../../sources/agentic-note-taking-23-notes-without-reasons-202689418851669643.ingest.md) -- **evidenced-by**: the adjacency-versus-articulated-connection case gives the source's KB consequence a concrete practitioner witness—embedding similarity surfaces feature neighbors, while useful links require a stated relation—subject to the ingest's single-system and self-report caveats.
- [Write an Instruction](../../../../instructions/write-instruction.md) -- **operationalized-from**: the procedure adds an execution order, minimum repeated instances, parameter extraction, boundary testing, and verification to the source's move from recurring particulars to a reusable general procedure.

## Bidirectional Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) <-> source -- **grounds**: the source's feature/structure/generative hierarchy supplies the concrete depth axis that the target currently poses only as an open “synthesis complexity spectrum,” while the target supplies the source-side verification boundary.

## Reverse-edge Candidates

- [Write an Instruction](../../../../instructions/write-instruction.md) -> source -- **rests-on**: for a meta-reader maintaining the procedure, its opening move—compare repeated cases, posit their stable core, and retain a boundary—is a procedure-level instance of unifying conjecture.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) -> source -- **rests-on**: the articulation test and the separation of search from semantic judgment depend on the theory that candidate adjacency is not yet recognition of a shared structure.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) -- useful inbound application already authored from the target; a reciprocal source-side edge would duplicate the more direct co-presence prerequisite carried by Short composable notes.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- applies the abstraction boundary specifically to trace-derived memory; the productive-versus-defensive abstraction candidate gives the source reader the more general discriminator and already routes to this narrower case.
- [A-mem](../../../../agent-memory-systems/reviews/a-mem.md) -- implements vector retrieval and LLM-driven neighbor evolution but does not test whether the generated relations recover shared features, structures, or generative models.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- clearly keeps embedding search on the candidate side of promotion, but does not attempt or evaluate the source's unifying recognition operation.
- [ADR 053: Retire distillation without a successor term](../../../../reference/adr/053-retire-distillation-without-a-successor-term.md) -- already points to the source for a historical vocabulary migration; reverse traversal would expose implementation history rather than support or develop the theoretical claim.
- [Ingest: DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- its latent-entity failure is a singular hypothesis case, which the final source now marks as outside unifying conjecture; it therefore cannot support the source's depth hierarchy without collapsing the boundary.
- [Note type](../../../../types/note.md) -- declares document shape but says nothing about the epistemic operation the source analyzes.

## Index Membership

None. The source is already curated in both [Learning theory](../../../../tags/learning-theory-README.md) and the complete [discovery](../../../../tags/discovery-README.md) head; no additional index passed the articulation test strongly enough to justify a new tag or membership candidate.

## Synthesis Opportunities

- The source, [Generality bought to avoid counterexamples](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md), and [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) jointly imply three separate judgments that are easy to collapse: recognizing cases under one general, checking that the general excludes false positives, and deciding which consequences may transfer across the relation. A future synthesis could name this recognition/content/transfer sequence without treating a shared pattern as its own warrant.
- The source's three forms, [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md), and [Known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) imply a depth-indexed evaluation program: feature clustering, structural correspondence, and generative explanation need different candidate generators and increasingly demanding oracles. The KB currently holds the pieces but not the measurement ladder.

## Maintenance Observations

- [Title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) says this source contains a “maturation path” listing seven extracted claims and repeats that assertion in its footer. The current source has no such section after the final rewrite, so that inbound context is stale and should be revised when maintenance is next authorized.
- Several existing note-side footer edges into the source use labels outside the current notes collection authorization: `instance` in [information value is observer-relative](../../../../notes/information-value-is-observer-relative.md), `connects` in [known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), `meta` in [soft-bound traditions](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md), and `parallels` in [first-principles reasoning](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md). A future maintenance pass should remap or remove those formal footer labels under each source note's current collection rules.

## Flags

None
