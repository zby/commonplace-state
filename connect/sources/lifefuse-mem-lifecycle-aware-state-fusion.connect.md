---
description: "Connection candidates for LifeFuse-Mem's lifecycle-supervised neural memory and acquisition-controlled overwrite evaluation"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/lifefuse-mem-lifecycle-aware-state-fusion.md
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: LifeFuse-Mem

**Source:** [LifeFuse-Mem](../../../../sources/.snapshots/lifefuse-mem-lifecycle-aware-state-fusion.md)

The snapshot is immutable. These candidate edges belong on its paired ingest. Discovery followed cp-skill-connect using repository-local search.

## Discovery Trace

- Read the captured source, including method, evaluation, ablations, and references; read the sources collection contract and connect-report type. Used the notes, reference, agent-memory-systems, agentic-systems, and sources README navigation heads loaded during this preparation run.
- Generated a fresh title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`, narrowing the large output with `rg -i 'temporal|memory|lifecycle|contrast|retention|forget|freshness'`. Source titles were separately generated with `rg -N --no-heading -m1 '^# ' kb/sources --glob '*.md'` and narrowed with `rg -i 'memory|skill|state|harness|wiki|continual|compil|life|forget|retriev'`. Large output was truncated; focused searches and reads below supplied the candidate evidence.
- Description search across all authorized destinations: `rg '^description:.*(lifecycle|overwrite|interference|temporary|temporal|forget|stable|retention)' kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'`.
- Notes: read Retire, Redact, Supersede, And Relax Memory; Three-space agent memory; Active work state; and Feedback-trained memory management. Inspected the experiment-contrast note. Kept lifecycle operations and separation as bounded design comparisons. Rejected active-work-state because task resumption and closure are not the source's temporary-fact problem. Kept the oracle-dependence note only as a comparison, since explicit lifecycle supervision differs from reinforcement learning on downstream outcomes.
- Sources: read the LongMemEval and Geometry of Forgetting ingests. Kept their different diagnostic decompositions. LongMemEval's links led to knowledge-access evaluation and selector-signal concerns, but no additional broad navigation edge was needed. The geometry ingest's links to flat-memory contamination clarified why the source's latent-state interference must not be equated with retrieval competition.
- Agent memory: followed the lifecycle note's Graphiti example and inspected `kb/agent-memory-systems/reviews/graphiti.md`, including `rg -n -i 'temporal|valid|invalid|lifecycle'`. Kept the comparison between explicit historical validity records and protected neural state.
- Reference and agentic systems: searched `temporal|lifecycle|invalid|retention` in the reference README, freshness architecture, and agentic-systems README. Freshness baselines concern applicability of evaluated artifact versions, not temporary neural writes. Harness retention entries concern a different operation. No specific edge survived.
- External: only the source arXiv URL and its already-present citations were available. No external candidate prospecting.
- No source tags were present, so no tag-completeness skip applied. Checked the notes collection's `evidenced-by` authorization when considering reverse edges; deferred them because the strongest selected note connections remain comparisons across different implementations.

## Connections Found

- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **compares-with**: LifeFuse-Mem makes temporal commitment affect writes and readout, supplying a neural-memory counterpart to the note's requirement that lifecycle metadata drive operations. It does not implement the note's broader redaction, retirement, or revision lifecycle.
- [Three-space agent memory](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — **compares-with**: the source tests separation by temporary versus durable influence rather than a cognitive taxonomy. Its supervised rank partition and phase-aware fusion provide a concrete contrast to file-space retention policies; they do not validate the note's three-space taxonomy.
- [Feedback-trained memory management is oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — **compares-with**: LifeFuse-Mem's largest ablation loss follows removal of lifecycle supervision. This exposes the supplied signal behind a learned memory policy, while differing from the note's downstream outcome-reward setting and leaving unsupervised lifecycle discovery unresolved.
- [An experiment identifies only its actual contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: acquisition-conditioned retention, overall permanent-query accuracy, and public-benchmark compatibility answer different questions. The source's controlled evaluation additionally supplies phase boundaries and query lifecycles, so it does not establish autonomous anti-overwrite performance on unlabeled histories.
- [LongMemEval](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — **compares-with**: LongMemEval separates indexing, retrieval, and reading failures; LifeFuse-Mem separates initial acquisition from post-conflict retention. Together they illustrate why a single final memory accuracy hides distinct failure locations, without equating their tasks or substrates.
- [The Geometry of Forgetting](../../../../sources/the-geometry-of-forgetting.ingest.md) — **compares-with**: both examine interference, but geometry-driven competition can hide a still-stored vector item, whereas LifeFuse-Mem addresses conflicting writes into shared neural state plus readout selection. The distinction matters for choosing retrieval constraints versus write isolation.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: Graphiti retains factual edges with validity windows and invalidates superseded facts without deleting their history. LifeFuse-Mem instead preserves selected stable coordinates and fuses checkpoint-based scores. Both distinguish earlier and later evidence, but a temporary local exception is not necessarily permanent temporal supersession.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Active work state is not retrospective memory](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): current goals, closure criteria, and unfinished work are distinct from the temporary conflicting values in this paper.
- [Freshness architecture](../../../../reference/freshness-architecture.md): a review applicability boundary is not a memory state's temporal validity policy; shared persistence vocabulary is insufficient.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

The sources README still describes a WebFetch fallback, while the loaded snapshot skill specifies Poppler PDF capture and Trafilatura HTML capture. This is a navigation-document discrepancy only; no files were changed.

## Flags

- The paper's controlled readout uses known phase boundaries, known query lifecycles, a preserved Phase-A checkpoint, and protected-state fusion. Public LoCoMo and MemoryAgentBench runs omit that readout and are compatibility checks, not direct anti-overwrite tests.
- Acquisition-controlled retention improves while final permanent-query accuracy stays near 20%; preserve both denominators. Retention and overwrite are complementary only under the stated candidate-choice protocol.
- The paper refers to a separate Appendix file for training and fusion sensitivity details. The captured main PDF ends with references; no companion was supplied or inspected in this connection pass.
- No claim about Markdown KB behavior follows directly from the neural-state experiments. File-backed lifecycle designs are comparison targets, not implementations validated by the paper.
