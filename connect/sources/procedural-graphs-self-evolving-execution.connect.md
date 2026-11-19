---
description: "Discovery context for ingesting Procedural Graphs: localized action guidance, retained graph revision, and validation boundaries"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/procedural-graphs-self-evolving-execution.md"
source_has_frontmatter: true
date: "2026-09-21"
depth: standard
---

# Connection Report: Procedural Graphs

**Source:** [Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](../../../../sources/.snapshots/procedural-graphs-self-evolving-execution.md)

Discovery executed under `kb/instructions/cp-skill-connect/SKILL.md`. This is an advisory discovery report for an ingest drafter. All outbound suggestions belong on the eventual matching ingest, never on the immutable snapshot. Reverse suggestions likewise target that future tracked ingest, not the local snapshot.

## Discovery Trace

**Scope and source:** Read the complete snapshot, sources and reports collection contracts, connect-report type, and notes outbound rules. Sources authorize notes, reference, agent-memory-systems, agentic-systems, other sources, and known external destinations. Instructions and workshops are excluded. The snapshot has frontmatter but no tags; no tag-derived sweep was required.

**Title and description scans:** Generated fresh `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` listings for all five authorized local destinations. Counts at discovery: notes 438 titles/435 descriptions; reference 162/161; agent-memory-systems 175/173; agentic-systems 21/18; sources 439/439. A Python wrapper filtered title candidates with `procedur|workflow|graph|trace|rejection|failure|evolv|refin|gating|gates|activation|context selection|action model|learning|autogenesis|validation`, and descriptions with `procedural|rejection|state.condition|transition|held.out|Autogenesis|autogenesis`. These were lexical screens, not semantic scores.

**Curated heads:** Read each destination's README, plus the context-engineering and self-improving-systems tag READMEs. The latter two are selective heads without `complete: true`. They routed to the action-selection and proposal-selection clusters. No index completeness claim replaced the whole-collection title/description scans.

**Per-destination evaluation:**

- **Notes:** The listing and body search `rg -n -i 'subgraph|procedural|rejection|state.condition|held.out' kb/notes/ --glob '*.md' --max-count 1` surfaced activation, retained instructions, diagnostic richness, and learning-boundary candidates. Read the retained-instruction, action-model, rule-ready-signal, fixed-decomposition, failure-explanation, trace-authority, deployment-time-adaptation, diagnostic-richness, accepted-edit, and proposal-selection notes. Kept concrete mechanism matches below. Rejected treating the paper's offline training study as direct deployment-time adaptation evidence.
- **Reference:** README and full listings led to the automated-note-refinement proposal. Body queries included `procedural|rejection memory|held.out|local.*subgraph|transition` and a focused `graph|workflow|rejection|rollback` query. Read the proposal; retained no outbound edge because its set-valued note-writing oracle is too different for the shared incumbent pattern alone to earn an adjacent link. The general proposal-selection note is the better route.
- **Agent-memory-systems:** README and listings led to Agent Workflow Memory. Read its review, especially write-side, read-back, and authority sections. The focused `graph|workflow|rejection|rollback` query confirmed workflow-file injection. Kept the comparison because per-domain file push versus per-step local guidance changes the retrieval decision and consumption cost. A graph label by itself did not justify linking Graphiti or AriGraph.
- **Agentic-systems:** README and listings identified Autogenesis. Read its review. The same focused query exposed versioned mutation, rejection journals, and rollback. Kept the comparison on update scope and acceptance checks; its smoke gate differs materially from PG's held-out task-score gate.
- **Sources:** README and listings identified GEPA, AWM, Autogenesis, and several harness-evolution ingests. Read GEPA's ingest; kept it as the closest retained comparison of trace-driven mutation and candidate selection. Prefer the AWM and Autogenesis code-grounded reviews above to duplicating links to their ingests. Broad body queries were truncated, so candidate judgments rely on focused reads and the scoped listing screens rather than a claim to inspect every body hit.
- **External:** No open-web prospecting. The original arXiv URL already supplied by the snapshot is eligible as provenance.

**Link following:** Followed the retained-instruction note to proposal-selection; followed the fixed-decomposition note to diagnostic richness; followed the GEPA ingest to the accepted-edit note; followed the AWM review's activation and trace-learning pointers at the description/claim level. The first two yielded stronger candidate paths. The accepted-edit note concerns human instance acceptance, so its argument is a useful analogy rather than direct evidence from PG's validation gate.

## Connections Found

- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) — **is-evidence-for**: graph edits preserve tested procedural choices for later tasks even with frozen model weights; Section 3.3 and Algorithm 1 identify the retained graph and its acceptance criterion.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **is-evidence-for**: exact matching of the last procedure supplies the rule-ready signal for two-hop retrieval; failed matching causes full-graph fallback, while the guidance model performs the subsequent situational interpretation.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: the explicit path is graph neighborhood → generated guidance → solver prompt → chosen action. The usage ablation compares consumption treatments of the same graph, making the access path an empirical design variable.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: the refiner proposes rejectable edits, structural and held-out checks control acceptance, and the retained checkpoint guides later tasks. Rejected candidates do not become the next parent.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: PG exposes graph topology and attributes to revision, including repairs to a poor expert graph, while leaving the tool interface, localization/guidance procedure, refiner, evaluator, and data partition outside the reported update loop. This identifies its effective revision boundary without claiming that the fixed layer is mistaken.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) — **compares-with**: rejection records enter later refiner calls, creating a consumption path for negative evidence. The paper does not separately ablate rejection memory or establish that a particular retained explanation changed a later proposal, so this is a test-design comparison rather than a causal validation claim.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — **compares-with**: both distill trajectories into reusable procedural guidance, but the reviewed AWM loads selected workflow files at coarse domain scope, while PG localizes the recent action and generates guidance from connected transitions at each step. PG's baseline adaptation should not be treated as identical to the reviewed original implementation.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) — **compares-with**: both retain inspectable edits and rejected-history signals; PG's graph-specific held-out performance gate contrasts with the reviewed branch's broader extension lifecycle and crash-oriented smoke gate.
- [GEPA](../../../../sources/gepa-reflective-prompt-evolution.ingest.md) — **compares-with**: both turn execution evidence into retained non-weight changes; GEPA revises module prompts and samples a Pareto frontier, whereas PG revises graph topology/attributes and accepts a non-decreasing validation score against one incumbent.
- [Original paper](https://arxiv.org/abs/2609.09153) — **derived-from**: external provenance for the eventual ingest's account of the represented procedure graph and experiments.

## Bidirectional Candidates

None. Useful inbound evidence uses are specified below rather than mechanically mirroring every comparison.

## Reverse-edge Candidates

Under the notes collection's `evidenced-by` authorization, the following notes could cite the future tracked ingest after their authors assess and ground the relevant claims:

- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) → future ingest — **evidenced-by**: an evaluated graph is a concrete retained procedure selected among model-generated candidates.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) → future ingest — **evidenced-by**: exact last-action matching and full-graph fallback provide an explicit selector example.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) → future ingest — **evidenced-by**: the same-graph usage ablation distinguishes representation from its runtime consumption mechanism.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — PG is relevant to artifact-based adaptation generally, but the reported evolution uses training batches and freezes the graph during episodes and test evaluation. It does not directly establish adaptation during deployment, and soft guidance needs its own authority classification.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — the note's primary oracle is human acceptance of one edit. PG evaluates a whole graph on held-out tasks; the scope warning transfers, but calling this direct evidence would erase the different oracle and assessed unit.
- [Automated note refinement as a search over a fixed source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) — incumbent retention is shared, but set-valued note quality and task-score graph optimization differ enough that the general proposal-selection claim is a more useful link.

## Index Membership

None. The snapshot is not a durable index target; source identity and connections should first reside in its tracked ingest.

## Synthesis Opportunities

The action-model and rule-ready-signal notes together suggest a bounded comparison question: when does deterministic localization plus model-generated situational guidance outperform whole-artifact injection? PG Table 3 supplies a within-system consumption contrast, while AWM supplies a different granularity of activation. A future synthesis would need matched comparisons before attributing gains to graph structure itself.

## Maintenance Observations

The reference proposal's prose says `cp-skill-connect` wires artifacts into the library. The current skill explicitly writes only a discovery report. This is a procedure-description mismatch in the proposal, separate from the present connection candidates.

## Flags

- **Multiple extraction topics:** more than five connections span context selection, procedural representation, and improvement governance. Keep the source ingest whole, but consider separate future theory notes if extracting claims; no split or new note is authorized by this report.
- **Soft authority:** edges are described as admissible transitions, but the solver receives advisory natural-language guidance. Neither the graph nor its structural validator establishes hard execution conformance.
- **Structural checks are narrower than prompt requirements:** Appendix B.6 checks endpoints and terminal reachability; reaching a zero-out-degree terminal is not specifically reaching `End`. Tool-catalog membership is requested in the refiner prompt, not independently enforced by the generic validator.
- **Serializer boundary:** Appendix B.5 says the local serializer omits stored relation labels in its example. Do not infer that all graph semantics are presented to the guidance model merely because they are stored.
- **Cost boundary:** localized generative guidance uses fewer tokens than full-graph generative guidance in Table 3, but more than the no-graph baseline. Fewer solver steps do not establish lower total token cost.
- **Selection boundary:** the EnterpriseArena evolution study returns 85% test survival; 95% is an intermediate observed peak, not the selected final result. With 20 episodes per split, round decisions are a search trace rather than per-round significance tests.
- **Causal limits:** the usage ablation has no localized raw-injection arm and does not isolate every interaction. Construction modes bundle incremental feedback and validation; rejection memory is not separately ablated. Better task scores do not by themselves verify diagnostic explanations or cross-domain transfer.
