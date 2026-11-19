---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/human-analogies-suggest-functions-not-component-boundaries.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Human analogies can motivate functions without determining component boundaries

**Source:** [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md)

## Discovery Trace

**Authorisation and breadth:**

- Read `kb/notes/COLLECTION.md` before prospecting. Its scan rule names `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/`; its authorised-label table additionally permits `evidenced-by` into `kb/types/` and `kb/agentic-systems/`. This pass conservatively prospected all seven local surfaces. `kb/work/` is excluded. The reserved `external` destination is authorised only for already-known targets, and none was supplied or already loaded, so open-web prospecting was skipped.
- The source carries `foundations` and `computational-model`. Read both matching tag heads. Neither declares `complete: true`, so no by-tag search was skipped.
- No scored semantic search was used; all discovery was repository-local and unscored.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/foundations-README.md`, and `kb/notes/computational-model-README.md`. The foundations head already curates the source in its design-method cluster and exposed the mechanism-transfer and rival-design neighborhoods. Followed the tag hub to `kb/notes/agent-memory-README.md`, which exposed a plausible new index membership because the source separates storage, activation, interpretation, authority, and action from a single memory component.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, `kb/instructions/README.md`, and `kb/types/README.md`. Reference exposed the source-adoption policy; the external-system heads exposed cognitive-memory and actor-allocation cases but no system review that isolates human resemblance as the cause of a component boundary; the instruction and type heads exposed no direct outbound target.

**Full title listings:**

- Generated the complete title surface for every prospected destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, run separately for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, `instructions`, and `types` (354, 135, 173, 12, 504, 44, and 10 title lines respectively).
- The notes surface flagged `borrowed-patterns-transfer-only-over-shared-mechanism.md`, `a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md`, `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md`, `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`, `instantiation-alone-cannot-model-agent-learning-across-sessions.md`, and `three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` for full reading.
- The source surface flagged the human-memory survey, the psychology-principles thread, the human-automation function-allocation paper, Letta's OS analogy, the computer-architecture memory analogy, the wordless-thinking essay, and the multi-agent analytics control-plane case. Other title surfaces produced no comparably direct unencoded target.

**Description listing scans:**

- Ran `rg -l "^tags:.*\\bfoundations\\b" kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the same command for `computational-model` over all seven destination roots. The scans returned the large expected note sets, a small reference/agentic set, one tagged source, and no tagged agent-memory, instruction, or type artifact.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'human|cognit|psycholog|analog|component|boundar|decompos|allocat|transfer|shared mechanism|personaliz|role placement|responsible roles|coupl'` over all seven roots. In notes this kept the general transfer rule, rival-boundary test, decomposition-warrant notes, personalization carrier, and cognitive-analogy cases. In reference it kept `source-adoption-policy.md`; in sources it kept the survey, psychology, function-allocation, and workflow-copying cases. The agentic-system, instruction, and type hits shared only allocation, decomposition, or boundary vocabulary.

**Body searches:**

- `rg -n -i 'human (analogy|analogies)|analogy|analogical|psychology|cognition|cognitive' kb/notes/ --glob '*.md'`
- `rg -n -i 'component boundar|component decomposition|allocation hypothesis|allocate|allocation|role placement|responsible roles|shared mechanism|borrowed pattern|inherited (constraint|boundar)|coupl' kb/notes/ --glob '*.md'`
- `rg -n -i 'personalization|user-specific intent|retained intent|model weights' kb/notes/ --glob '*.md'`
- `rg -n -i 'human (analogy|analogies)|analogy|analogical|psychology|cognit|shared mechanism|borrowed pattern|source adoption' kb/reference/ --glob '*.md'` and `rg -n -i 'component boundar|component decomposition|allocation|responsible roles|role allocation|fixed decomposition|design space|coupl' kb/reference/ --glob '*.md'`.
- `rg -n -i 'human (analogy|analogies|memory)|analogy|analogical|psychology|cognit|Tulving|episodic|semantic memory' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i 'component boundar|component decomposition|allocation|responsible roles|fixed decomposition|crosscutting|separable niche|memory.*component|component.*memory|coupl' kb/agent-memory-systems/ --glob '*.md'`.
- `rg -n -i 'human workflow|human (analogy|analogies)|analogy|psychology|cognit|component boundary|component decomposition|allocation|handoff|centralized.*reason|workflow stages|coupl' kb/agentic-systems/ --glob '*.md'` found actor-allocation language but no human-analogy boundary case.
- `rg -n -i 'human (analogy|analogies|workflow)|analogy|analogical|psychology|cognit|Tulving|component boundar|component decomposition|allocation hypothesis|responsible roles|role allocation|workflow stages|modeled.*human|map.*human workflow|handoff|coupl' kb/sources/ --glob '*.ingest.md'` exposed the kept survey and workflow-copying cases and the rejected taxonomy, automation, OS, and writing analogies.
- `rg -n -i 'solution.shaped|separate.*function|function.*implementation|desired outcome|implementation.*choice|component boundar|decomposition|allocation|analogy|cognit|psychology|coupl' kb/instructions/ --glob '*.md'` found `invert-solution-shaped-requests.md` and two review gates, but none depends specifically on the source's human-function-versus-component distinction.
- `rg -n -i 'function|component|boundary|allocation|analogy|cognit|psychology|coupl' kb/types/ --glob '*.md'` found only generic contract-boundary language.
- `rg -n 'human-analogies-suggest-functions-not-component-boundaries|Human analogies can motivate functions without determining component boundaries' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions kb/types --glob '*.md'` found existing inbound uses from the foundations head, four source ingests, the multi-agent analytics case, and a link-label experiment. Existing inbound edges were not re-proposed as reverse candidates.

**Link following and candidate evaluation:**

- Read the full candidate notes on mechanism-bounded transfer, boundary-preserving rivals, local decomposition tests, fixed update spaces, class/instance analogy, Tulving's taxonomy, and failure-mode transfer. Followed their authored links one hop into first-principles design-space mapping, derivation/inheritance warrant, design-rationale management, flat-memory predictions, and memory-policy evidence.
- Kept the borrowed-pattern note because it supplies the source's general premise; kept the rival-boundary note because it develops the exact “function survives while the boundary moves” test; kept the local-use note because it bounds what testing an allocation can establish; kept the Tulving note because it is a worked function-versus-boundary case. Rejected the fixed-update-space and class/instance notes because they concern later learning/update boundaries rather than warrant for the initial allocation.
- Read the multi-agent analytics ingest and snapshot. Kept the ingest because it reports that copying human analyst stages into four agent boundaries failed while a replacement preserved the functions and reassigned them among deterministic code, one judgment owner, bounded workers, and a graph; its limitations make the evidence explicitly local and unverified.
- Read the human-memory survey ingest. Kept it as a survey-scale case where human labels are mapped onto AI memory while object/form/time dimensions do the explanatory work. Read the psychology-principles, human-automation, wordless-thinking, Letta, computer-architecture, and Ars Contexta analyses; rejected them for redundancy, an already-authored inbound edge, a non-human analogy, or failure to isolate analogy's effect on a component boundary.
- Read the outbound contracts of `kb/reference/`, `kb/sources/`, `kb/instructions/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/types/` before judging return or reverse edges. The source-adoption policy and psychology-transfer note pass their own collection rules for reverse `rests-on` and `extends` candidates. No instruction, type, or external-system analysis does.
- Verified every path listed below with `test -f`; every connection candidate has frontmatter. No raw-text candidate survived.

## Connections Found

- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **grounds**: supplies the general premise behind the source's distinction: a human function may transfer, but its bundled boundary carries warrant only where the causal mechanism responsible for that bundling is shared.
- [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) -- **extends**: develops the source's “function survives while the boundary moves” check into a general one-way test that demotes a rule when a rival preserves the stated boundary invariants.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **extends**: sharpens the source's instruction to test allocation hypotheses by showing that one successful allocation warrants only local sufficiency unless the forces behind its seams were retained and varied.
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) -- **evidenced-by**: supplies a worked case where a human taxonomy suggests useful functions, but different lifecycle policies—not resemblance to Tulving's categories—must justify the engineered spaces.
- [Ingest: Why Multi-Agent Pipelines Fail for Complex Analytics](../../../../sources/multi-agent-analytics-control-plane-2087241401649996149.ingest.md) -- **evidenced-by**: reports a bounded practitioner case in which copying human analyst stages into agent boundaries failed, while preserving the functions and reallocating them across code, a judgment owner, workers, and a graph reportedly repaired coherence.
- [Ingest: From Human Memory to AI Memory](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md) -- **evidenced-by**: provides a survey-scale instance of mapping sensory, working, episodic, semantic, and procedural labels onto AI memory even though the survey's object/form/time dimensions—not the human labels—carry the architectural distinctions.

## Bidirectional Candidates

- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) <-> source -- **extends**: from the general transfer rule, the source is a concrete development of what happens when a function-level mechanism transfers but a component boundary lies beyond that mechanism's reach.
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) <-> source -- **exemplifies**: from the Tulving case, the source states the general function-versus-boundary rule that explains why lifecycle differences can justify a split while the cognitive taxonomy remains decorative.
- [Ingest: From Human Memory to AI Memory](../../../../sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md) <-> source -- **is-evidence-for**: from the ingest, the survey bears materially on the source's warning by attaching human-memory names to a taxonomy whose object/form/time axes perform the architectural work.

## Reverse-edge Candidates

- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -> source -- **extends**: after testing whether each human failure mode and mechanism transfers, the source adds the separate allocation question—where a surviving function should live in the engineered system.
- [Source-adoption policy](../../../../reference/source-adoption-policy.md) -> source -- **rests-on**: the policy's cognitive-science branch accepts useful functions only when target-side constraints justify them; the source supplies the more specific premise that this acceptance still does not inherit the human component boundary.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- rejected as a downstream consequence: it concerns corrections outside a learner's update space, while the source addresses warrant for choosing the initial allocation.
- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- rejected because it is another bounded analogy critique, but its missing retained-update relation does not bear specifically on component-boundary allocation.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- rejected as redundant with the source's existing link to the per-principle psychology-transfer note, which already imports this failure-mode test.
- [Ingest: Psychology already solved AI memory](../../../../sources/psychology-solves-ai-memory-identity-construction-2025307030651.ingest.md) -- rejected because the source already reaches its useful analysis through the linked per-principle psychology-transfer note; adding both would duplicate the same worked cases.
- [Ingest: A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- rejected because it is a useful function-allocation precedent but does not test or report a component boundary inherited from human cognition.
- [Ingest: When is it better to think without words?](../../../../sources/when-is-it-better-to-think-without-words.ingest.md) -- rejected as an outbound target because it already authors the useful inbound application of the source's rule and its human-to-agent comparison concerns representational phases, not an inherited engineered component boundary.
- [Ars Contexta](../../../../agent-memory-systems/reviews/arscontexta.md) -- rejected because the review records cognitive grounding and a three-space implementation but does not isolate whether analogy, lifecycle mechanics, or conversational derivation caused those boundaries.
- [Ingest: Multi-Agent Memory from a Computer Architecture Perspective](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) -- rejected because it tests a computer-architecture analogy, not the human analogy scoped by the source; its content-type-versus-hierarchy distinction belongs with the Tulving note instead.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected because its per-function human/computational allocation is useful actor accounting but is not derived from a human-cognition analogy.
- [Invert solution-shaped requests](../../../../instructions/invert-solution-shaped-requests.md) -- rejected because separating a problem from a proposed solution is analogous to separating a function from an allocation, but the instruction does not depend on the source's human-transfer claim.
- [Unbridged cross-domain evidence](../../../../instructions/review-gates/prose/unbridged-cross-domain.md) -- rejected because the gate checks whether evidence crosses domains through a stated bridge; the broader borrowed-pattern note is its closer theoretical premise, and the gate does not evaluate component allocation.
- [Note](../../../../types/note.md) -- rejected because the global type contract contains only general claim, scope, and collection-boundary requirements; it supplies no evidence for or application of the source's distinction.
- [Descriptive link labels may supply the self-sufficiency a reconstruction gate would check](../../../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md) -- rejected because its inbound mention uses the source only as a review fixture; it says nothing about the source's substantive claim.

## Index Membership

- [Agent memory](../../../../tags/agent-memory-README.md) -- candidate tag/index placement: the source gives memory architects a direct guard against turning the human word “memory” into one component that bundles storage, activation, interpretation, authority, and action. A future writer should add the `agent-memory` tag before considering a curated entry.

## Synthesis Opportunities

None. The combination of mechanism-bounded transfer, rival decompositions, and scope warrant is already covered by the source's existing derivation/inheritance link plus the candidates above.

## Maintenance Observations

- `kb/notes/COLLECTION.md` names five local scan destinations in prose but its authorised-label table additionally permits `kb/agentic-systems/` and `kb/types/`. This run prospected both extra label-authorised surfaces; a future contract edit could make the destination inventory and label table explicit about the same set.

## Flags

None.
