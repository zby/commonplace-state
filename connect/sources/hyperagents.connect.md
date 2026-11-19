---
description: "Discovery report for possible KB connections from the HyperAgents paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/hyperagents.md"
source_has_frontmatter: true
date: "2026-08-04"
depth: standard
---

# Connection Report: HyperAgents

**Source:** [HyperAgents](../../../sources/hyperagents.md)

## Discovery Trace

**Setup and source read:**
- Read the source collection contract, snapshot and ingest-report type contracts, connect-report contract, and the full paper snapshot. The source collection authorizes ingest reports to link to notes, reference, sources, agent-memory systems, and agentic systems; snapshots themselves remain immutable.
- Applied the fixed-decomposition lens required for experiment-bearing sources: identified the available histories, editable operations, effective hypothesis class, fixed task/evaluation/search machinery, and what each ablation actually varies.

**Curated heads and listings:**
- Read the notes tag hub plus the self-improving-systems, agent-memory, and computational-model curated heads; read the reference, sources, agent-memory-systems, and agentic-systems collection heads.
- Scanned Markdown titles and descriptions across all authorized destination collections. This surfaced the existing code-grounded [HyperAgents review](../../../../agent-memory-systems/reviews/hyperagents.md), the DGM source lineage, and the reflective-leverage, fixed-decomposition, compounding, machinery, proposal-selection, and diagnostic-richness clusters.

**Focused body search and link following:**
- Searched for HyperAgents, Darwin Gödel Machine, self-modification, meta-agent, outer-loop, parent-selection, archive, transfer, compounding, persistent memory, and performance tracking. Read the strongest candidate artifacts in full and followed their relevant authored links one hop.
- Checked the generated systems matrix and table: HyperAgents already has code-grounded survey membership, so this source adds paper-level empirical evidence rather than a new system entry.

## Connections Found

- [HyperAgents code-grounded review](../../../../agent-memory-systems/reviews/hyperagents.md) -- **compares-with**: the review establishes the shipped trace-to-code mechanism; the paper supplies the corresponding multi-domain outcomes, ablations, transfer protocol, and claimed emergent memory artifacts. The paper also qualifies the review's broad editability claim by making clear that main-run parent selection, evaluation, task distributions, and sandbox budgets remain fixed.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: DGM-H broadens the editable Python program to include task and meta agents, but the main experiments hold the outer search/evaluation decomposition fixed. Gains inside that boundary do not validate the frozen parent selector, benchmark objectives, judges, or task distributions.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **rests-on**: DGM-H is a direct worked case of archive search, benchmark evaluation, and executable patch-lineage retention; its latest-only ablation tests the archive/exploration component within this architecture.
- [Reflective leverage is tested in the next episode](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **is-evidence-for**: Improvement@50 freezes transferred meta agents in an unseen domain and measures the quality of later improvements rather than only the score that selected the original change. It is an unusually direct, though still narrow and retrospectively selected, instance of displaced next-episode measurement.
- [Compounding self-improvement needs leverage to multiply and autonomy to scale](../../../../notes/improvements-can-accumulate-without-compounding.md) -- **compares-with**: the transfer result supports reusable leveraged machinery, but the 200-iteration transfer-versus-fresh difference is not statistically significant and no acceleration or rising improvement productivity is measured. The paper supports accumulation and possible leverage more strongly than compounding.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- **compares-with**: HyperAgents moves the task/meta boundary inward and preliminarily makes parent selection editable, yet the learned selector does not beat the handcrafted one and evaluation stays outside. This is a useful case where revisability exposes machinery without establishing that the revised machinery earned persistence.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: evolved hyperagents introduce performance histories and synthesized persistent memory that can enrich later proposal context. The source offers qualitative examples, not an independent ablation of either artifact, so it corroborates the mechanism without isolating it.
- [Ingest: Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) -- **compares-with**: DGM-H retains DGM's archive/evaluation loop while moving the instruction-generation mechanism into the mutable hyperagent. The comparison should preserve that both systems still rely on fixed outer machinery in the main experiments.

## Bidirectional Candidates

- [HyperAgents code-grounded review](../../../../agent-memory-systems/reviews/hyperagents.md) <-> source -- **see-also**: the review should point to this paper ingest for the reported outcome evidence, while the ingest should use the review as the implementation-grounded companion.

## Reverse-edge Candidates

- [Reflective leverage is tested in the next episode](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -> source -- **evidenced-by**: Improvement@50 is a concrete cross-domain frozen-improver test, close to the note's displaced-measure protocol; the note should also record the retrospective transfer-agent selection and single target domain.
- [Compounding self-improvement needs leverage to multiply and autonomy to scale](../../../../notes/improvements-can-accumulate-without-compounding.md) -> source -- **evidenced-by**: the paper is a useful boundary case separating transfer of improvement machinery from demonstrated compounding, because its compounding comparison is directionally positive but not statistically significant.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -> source -- **evidenced-by**: DGM-H explicitly acknowledges fixed task distributions and outer selection/evaluation, and its modifiable-selector appendix does not outperform the handcrafted selector.
- [HyperAgents code-grounded review](../../../../agent-memory-systems/reviews/hyperagents.md) -> source -- **see-also**: add the paper as the empirical companion for multi-domain outcomes, transfer, and ablation claims.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- broad code editability is relevant, but the fixed-decomposition and machinery notes express the paper-specific boundary more precisely.
- [Knowledge-centric self-improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) -- both transfer retained improvement artifacts, but one curates external knowledge and the other evolves executable agent code; no direct comparison is needed in this ingest.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- both expose broad self-modification behind a protected substrate, but Exo is a running harness without HyperAgents' benchmark evolution protocol. The DGM lineage and existing HyperAgents review are closer companions.
- [Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- related outer-loop harness optimization, but its controlled trace-richness ablation is better used through the diagnostic-richness note than as another direct source-to-source edge.

## Index Membership

- [Agent Memory Systems table](../../../../agent-memory-systems/systems-table.md) already lists the code-grounded HyperAgents review; no new index membership is required for this paper snapshot.

## Synthesis Opportunities

- HyperAgents' Improvement@50 protocol plus [Reflective leverage is tested in the next episode](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) could yield a worked-case section distinguishing transfer of an improver from transfer of an improved task artifact. The same section should explain why a positive transfer result is evidence of leverage but not yet evidence of accelerating compounding.

## Maintenance Observations

- The code-grounded review currently says no with/without-lineage or per-memory faithfulness test was found. The paper does not supply a per-patch or per-memory intervention, but its frozen-meta-agent transfer experiment is stronger outcome-level evidence than the review presently records; the distinction should remain explicit if the review is updated.
- The paper's qualitative persistent-memory and performance-tracking examples were not independently ablated, so they should not replace the review's code-grounded artifact inventory or be treated as the established cause of transfer.

## Flags

- The snapshot is a full ar5iv-to-text capture and contains LaTeXML math markup artifacts. Claims and numerical results are readable, but exact equation quotation should be checked against the original rendered HTML or PDF.
