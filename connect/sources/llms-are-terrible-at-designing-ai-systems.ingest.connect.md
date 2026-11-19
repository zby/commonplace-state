---
description: "Post-acceptance discovery for Goedecke's AI-design ingest: allocation, prompted criticism, and bounded inbound source uses."
type: types/connect-report.md
source: "kb/sources/llms-are-terrible-at-designing-ai-systems.ingest.md"
source_has_frontmatter: true
date: "2026-11-08"
depth: standard
---

# Connection Report: LLMs are terrible at designing AI systems

**Source:** [Ingest: LLMs are terrible at designing AI systems](../../../../sources/llms-are-terrible-at-designing-ai-systems.ingest.md)

Operation: post-acceptance `cp-skill-connect`, following `kb/instructions/cp-skill-connect/SKILL.md` and the global connect-report type. Judgment model: `gpt-6.1-sol`. Inputs are the current ingest and repository state on the report date. All edges below are candidates, not authored links. No agents or external search services were used.

## Discovery Trace

### Authorization and scope

Read the complete source, `sources/COLLECTION.md`, `reports/COLLECTION.md`, and `types/connect-report.md` before discovery. The source permits prospecting theory, reference, agent-memory-systems, agentic-systems, tags, and other sources. Work and instructions are excluded as destinations. External targets are permitted only from already-loaded context. Theory permits `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` for definitions, and sparse `see-also`; reference permits only `see-also`; source and agentic-system comparisons permit `compares-with` or `see-also`; legacy memory reviews additionally permit `is-evidence-for`. Tags are named as a search destination but have no authorized source-to-tag label.

The source has no tags. No source-tag lookup was applicable. Its strongest existing outbound links are the allocation heuristics and activation note; discovery does not propose adding duplicate links to them. Its learning discussion already links the fixed-decomposition note and theory-builder definition. The distinct contributions are a reported semantic-allocation failure and a prompted-versus-spontaneous design objection. The training explanations remain conjectures.

### Curated heads and complete title surfaces

Read `README.md` in every authorized local destination: theory, reference, agent-memory-systems, agentic-systems, tags, and sources. The historical memory landing explicitly freezes its survey; the current agentic-systems landing distinguishes authored accounts from archived analyses. Neither is treated as a current source of prevalence claims.

Generated the complete title surface once for each of those six destinations with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered truncated output before judging the listing. Theory titles surfaced exact implementation, relaxing signals, promotion, elicitation, and fixed decomposition. The other listings surfaced Graphiti, Eigenius, the earlier Goedecke requirements essay, and The Bug That Shipped. Brief matches were treated as their corresponding document, not separate link targets.

Followed the tag landing to `failure-modes-README.md` and `constraining-README.md`, reading both completely. The former routes to activation, promotion, and elicitation; the latter routes to allocation and relaxing signals. The failure-modes head has `complete: true`; no by-tag `rg` was run for that tag. Completeness does not cover sources. No tag membership or assignment is proposed.

### Description listing scan

For each of the same six destinations, ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'semantic|contradict|symbolic|design|activation|formaliz|codif|RLVR|critici|reasoning'`. Recovered the truncated description output.

- **Theory:** retained exact implementation as the most precise additional allocation landing. Elicitation supplies an operational companion to the source's proposed experiment. Promotion and relaxing signals were evaluated but not retained as additional edges: the former adds no demonstrated delivery intervention, and the latter's operational tests were not run in this source.
- **Reference:** ADR 124 separates formal classification from task adequacy. Read it, but rejected an edge because the theory landing supplies the relevant distinction without sending a source reader into Commonplace decision history. Memory coverage and gap-plan descriptions concern shipped implementation rather than this anecdote.
- **Agent-memory-systems:** Graphiti's description names LLM extraction and fact invalidation. Read the complete review and retained a bounded implementation comparison. Other semantic-memory descriptions did not identify a closer contrast than its explicit contradiction-resolution path.
- **Agentic-systems:** Eigenius's description suggested a proof-versus-translation comparison. Read the complete review and rejected it as a less direct detour than Graphiti and exact implementation. Archived Ecdysis and JEPA-Anything hits do not directly test the reported semantic-memory design failure.
- **Tags:** constraining and failure-modes routed discovery to claims rather than becoming outbound targets. No source-to-tag label is authorized.
- **Sources:** retained The Bug That Shipped on prompted diagnosis versus spontaneous detection, and the earlier Goedecke essay on rival accounts of agent-added machinery. Followed the Graphiti ingest to its stronger code-grounded companion rather than recommending both.

### Body search

Ran both queries in each authorized local destination, with `--glob '*.md'`:

1. `rg -l -i 'contradiction detection|semantic adequacy|logical atoms|RLVR|regex.*classif|classif.*regex' kb/<destination>/`
2. `rg -l -i 'design judgment|prompted criticism|unprompted|brittle proxy' kb/<destination>/`

Destination results and evaluations:

- **Theory:** the first query found automation/oracle discussions, not a closer allocation claim. The second found activation, promotion, relaxing signals, and several improvement-evidence notes. Full reads favored activation as an inbound source-use candidate; promotion remained a redundant additional landing. The source supplies no evidence of later retained learning or compounding.
- **Reference:** the first query returned no hits; the second found archived workflow/review-budget proposals. Neither offers a source-specific reader benefit. The separately title-selected ADR 124 was read and rejected as described above.
- **Agent-memory-systems:** the first query returned Cortex, LACP, MentisDB, MiroShark, AriGraph, ATLAS, Eidetic, and Quicky Wiki; the second returned no hits. These names were triage results, not inspected implementation evidence. The description-selected Graphiti review gives a more explicit, fully inspected comparison on the precise contradiction-judgment boundary.
- **Agentic-systems:** the first query returned archived Ecdysis, SoL-Pi, and GBrain material plus the memory table. The second returned AI Agents in Depth and an archived RSIAgent analysis. None establishes the claimed training cause or agent design error. The complete title/description-selected Eigenius read was the closer formal-methods candidate, but still failed the incremental reader-benefit test.
- **Tags:** the first query returned no hits; the second returned reflection and failure-modes. The failure-modes head was read and followed to its claim notes. No formal tag edge was retained.
- **Sources:** the first query found Graphiti and the earlier Goedecke requirements essay among broader hypothesis-validation/coordination hits. The second found The Bug That Shipped, review/simplification essays, and Harness-IF. Full reads of the two retained comparators established distinct comparison axes; general instruction-following and simplification hits were not enough to warrant more links.

### Link following and reverse pass

- The allocation heuristics link to exact implementation, oracle strength, and mixed implementations. Read exact implementation completely: it isolates the unvalidated natural-language-to-atoms step without assuming a solver defect. This is the strongest new theory edge.
- The activation note links to elicitation and The Bug That Shipped. Read both completely. The latter supplies a more structured, though still practitioner-reported, open-versus-probed comparison than Goedecke's anecdote. Elicitation gives the source's proposed experiment a reusable measurement framing.
- The failure-modes head links to promotion; the constraining head links to relaxing signals. Full reads showed overlap, but not enough distinct source evidence to justify additional edges.
- The source's fixed-decomposition link was followed and read completely. Its effective-update-space caveat rules out inferring an action-closure omission merely from absent model API access; no new evidence edge is recommended there.
- The Graphiti ingest points to the code-grounded historical review as the stronger account. Read both completely and retained only the review for the concrete comparison.
- Read `theory/COLLECTION.md` completely before judging inbound labels. The two reverse candidates below use its authorized `evidenced-by` label for a qualifying practitioner case, not corroboration. Neither note currently links this ingest. No origin relation is inferred.
- Read `tags/COLLECTION.md`: sources do not participate in generated tag membership. No index addition is recommended.
- **External:** the ingest's existing `source` URL is the already-known original and supports `derived-from` if a future writer needs a labelled source edge. Its identity is already recorded; no redundant edge is proposed. Open-web prospecting was skipped.

All candidate local paths were checked with `Path.is_file()` before inclusion. Search results were evaluated qualitatively; no numerical scores were produced.

## Connections Found

These are incremental candidates beyond the ingest's existing links.

- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) — **is-evidence-for**: this ingest connects to the claim because its solver anecdote illustrates how implementing logical rules can leave the upstream mapping from natural-language memories to those rules unjustified. Use as a reported illustration of the distinction, not evidence that the solver was locally correct or that a particular representation necessarily failed.
- [Elicitation requires maintained question-generation systems](../../../../theory/elicitation-requires-maintained-question-generation-systems.md) — **see-also**: this ingest connects to the methodology because its proposed spontaneous-versus-prompted design experiment needs separate measures for elicited objections, design changes, and task outcomes. The target provides an open-versus-probed measurement framing; the anecdote does not validate the target's proposed interventions.
- [Ingest: The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md) — **compares-with**: both describe objections produced after a targeted probe but missed in less directed work. The comparator reports a multi-scenario trial protocol, whereas Goedecke supplies selected design anecdotes. Following the link helps separate the shared failure shape from their very different evidential scope.
- [Ingest: What requirements don't you have?](../../../../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — **compares-with**: both Goedecke essays describe agents adding machinery that may not serve the actual task. The earlier essay concerns invented requirements and unstated tolerances; this one concerns unsuitable semantic formalization. Both invoke training explanations without testing them, so the comparison exposes specification and elicitation rivals rather than establishing an RLVR cause.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: this ingest connects to the pinned implementation review on where contradiction judgment is assigned. Graphiti asks an LLM to identify duplicate and contradicted facts, then uses code to maintain temporal validity. This supplies a concrete mixed design to compare against the reported logical-atoms pipeline, while exposing that detection and authorized invalidation are separate decisions. The historical code inspection is not evidence of superior contradiction accuracy or lower cost.

## Bidirectional Candidates

None. The strongest useful inbound edges concern notes already linked by the ingest; they are listed separately below. No reciprocal link is justified merely by retaining an outbound comparison.

## Reverse-edge Candidates

- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) → source — **evidenced-by**: a future writer could add a bounded practitioner illustration in the specification or mixed-implementation discussion. The reported natural-language-to-atoms design makes the distinction between implementation success and semantic objective fit concrete. The context phrase must say that the anecdote qualifies or illustrates the allocation issue; no comparative cost/accuracy test or corroboration is supplied. This is the highest-priority inbound candidate and agrees with the ingest's recommended source-only disposition.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → source — **evidenced-by**: a future writer could use the reported late design objection as another expert-witness case: produce-on-request criticism did not appear to govern the earlier work. This is secondary to the existing stronger evidence and useful chiefly as a design-stage example, not a needed additional citation. State beside the link that earlier context exposure, cause, and later design improvement were not observed; do not classify it as a demonstrated context-to-action failure.

## Off-authorisation Candidates

None. Tag heads were useful routing surfaces, but no source-to-tag edge independently passed the reader-benefit test; their missing source-side label does not justify a contract extension here.

## Raw Text Candidates

None.

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — already linked as a possible diagnostic. The essay does not inspect training access or rule out composed alternatives, so it cannot establish the note's effective-update-space boundary in this case.
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) — the anecdote motivates asking about triggers, but does not test retention or a delivery package. Activation and elicitation give the closer routes without importing an unobserved memory intervention.
- [Operational signals that a component is a relaxing candidate](../../../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) — plausible future testing context, but the essay supplies no metamorphic, integration, or distribution-shift measurements. The allocation and exact-implementation links better match what was actually reported.
- [ADR 124: retire unique operational semantics as the form criterion](../../../../reference/adr/124-retire-unique-operational-semantics-as-the-form-criterion.md) — relevant distinction, but local vocabulary history is not needed to evaluate this source. Prefer the transferable exact-implementation claim.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — its conditional proof/translation correspondence is adjacent to formalization fidelity, but it addresses a different implemented substrate. It neither corroborates nor refutes the memory anecdote; Graphiti is the more direct bounded comparison.

## Index Membership

None. The sources landing explains the collection rather than curating individual ingests. Sources are outside participating tag membership, and this essay does not warrant an exceptional editorial entry in the theory-oriented heads.

## Synthesis Opportunities

None. The allocation and activation mechanisms already have notes. The two Goedecke essays and The Bug That Shipped suggest comparison questions, not a new established mechanism or a warranted training explanation.

## Maintenance Observations

The relaxing-signals note still uses the older artifact-level “exact-spec artifacts versus proxy theories” framing, while its linked exact-implementation note now explicitly assigns exactness and proxyhood to different links in a named requirement path. A later maintenance pass could align the former's opening and footer with that path-relative distinction. No repair was made here.

## Flags

- The ingest has no retained quotes. Before a future theory writer relies on source-side details, use the grounding workflow to retain the minimum exact support, or explicitly require the snapshot when full observation is necessary. This report does neither and grants no authority to mutate the ingest.
- The activation note already cites numerous sources. Any later source addition must independently satisfy its collection's five-unquoted-source bound; connection discovery is not an instruction to append another ungrounded citation.
- Preserve the ingest's source-only disposition. Neither selected anecdotes nor prompted criticism establish a general code-versus-model preference, an RLVR cause, successful redesign, or durable learning.
