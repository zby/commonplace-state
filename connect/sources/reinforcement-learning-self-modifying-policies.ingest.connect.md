---
description: "Post-ingest discovery for self-modifying policies: empirical retention, proof-gated switching, and the limits of compounding evidence."
type: kb/reports/types/connect-report.md
source: "kb/sources/reinforcement-learning-self-modifying-policies.ingest.md"
source_has_frontmatter: true
date: "2026-09-21"
depth: standard
---

# Connection Report: Reinforcement Learning with Self-Modifying Policies

**Source:** [Ingest](../../../../sources/reinforcement-learning-self-modifying-policies.ingest.md)

## Discovery Trace

Read the source, sources collection contract, report contract, and reports collection contract. Discovery used repository files only. The source has no tags, so no matching-tag sweep was required.

- Read `README.md` in all five authorized destinations: notes, reference, agent-memory-systems, agentic-systems, and sources. Also read `kb/notes/learning-theory-README.md`.
- Generated titles with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all five destinations. Initial combined display was truncated; a complete programmatic pass then counted 438 notes, 162 reference titles, 175 memory-system titles, 21 agentic-system titles, and 439 source titles and displayed matches for `self-modif`, `success-story`, `incremental self`, `compounding`, `proposal-selection`, and `fixed decomposition`.
- Description query: `rg '^description:.*(self.modif|retention|compounding|evaluation|reflective)' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. This surfaced the historical Incremental Self-Improvement review, SSA companion ingest, Exo, and proposal-selection note. The broad result was truncated; retained candidates were individually opened.
- Body query: `rg -n 'self.modif|success.story|rollback|evaluation timing|compounding' kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/reference/ --glob '*.md'`. Broad output was truncated and used only to identify candidates, not to establish their claims.
- **Notes:** individually inspected the Gödel-machine, compounding-measurement, proposal-selection, and fixed-decomposition notes. Followed the source's links to these notes; the Gödel-machine comparison explicitly distinguishes admission, reproduction, and continued retention. Read the notes collection's outbound rules before proposing inbound `evidenced-by` edges.
- **Sources:** inspected the SSA companion ingest. Kept a comparison between its ALS/IS cases and this paper's navigation SMP implementation; this gives readers a concrete way to separate the general retention algorithm from particular policy implementations.
- **Agent memory systems:** inspected the Incremental Self-Improvement review and its collection contract. Kept the historical comparison, but did not propose editing that historical review's pinned evidence boundary.
- **Agentic systems:** followed the Exo README entry and read its review. Kept a comparison on rollback scope and retained failure evidence.
- **Reference:** README, title, description, and body scans surfaced shipped-system accounts such as the tag-README improvement-loop trace. Rejected these as indirect: the proposal-selection theory note provides the useful bridge without implying that SSA validates Commonplace's shipped review machinery.
- **External:** original manuscript is already linked by the ingest. No new external candidate and no external prospecting.

## Connections Found

- [Proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: changes act before SSA evaluates their continued retention; restoration is a rejection operation distinct from producing the next modification. This supplies an implemented example of the note's temporal flexibility.
- [Shifting Inductive Bias with Success-Story Algorithm](../../../../sources/shifting-inductive-bias-success-story-algorithm.ingest.md) — **compares-with**: compare the shared retrospective reward-rate criterion across ALS/IS and navigation SMP implementations, keeping supplied instruction spaces and experimental contrasts separate.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) — **compares-with**: the historical review describes a policy-distribution learner from the earlier technical report; this source adds a concrete navigation implementation and learned evaluation timing while preserving the distinction between mutable policy and fixed evaluator.
- [Exo](../../../../agentic-systems/reviews/exo.md) — **compares-with**: SSA restores prior policy values after lived outcomes; Exo rewinds sandbox state while preserving event history. Comparing the exact state restored and evidence retained prevents treating rollback as reversal of every consequence.

The ingest already links the Gödel-machine, compounding-measurement, theory-refinement, and fixed-decomposition notes; these are not proposed as new outbound discoveries.

## Bidirectional Candidates

- [SSA companion ingest](../../../../sources/shifting-inductive-bias-success-story-algorithm.ingest.md) ↔ source — **compares-with**: a return link lets a reader move from the shared algorithm and ALS/IS experiments to the distinct navigation implementation, rather than infer that all results test the same architecture.

## Reverse-edge Candidates

- [Gödel-machine comparison](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) → source — **evidenced-by**: strengthen the existing empirical-retention comparison with the concrete distinction between when a modification becomes operative and when accumulated reward justifies retaining it. Explain that restoring policy values cannot undo elapsed time or environmental effects.
- [Compounding measurement](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source — **evidenced-by**: SSA explicitly includes later consequences in earlier modifications' retention test, yet its single-history reward trend does not isolate whether learned update choices made later learning more productive. This bounds the inference even when credit is long-horizon.
- [Proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source — **evidenced-by**: an implemented case where rejection occurs through rollback after actualization, not solely through prior admission. Prefer this case only if its navigation implementation adds value beyond the companion SSA paper.

All three reverse labels are authorized by the notes collection. Any source-dependent edit must retain sufficient quotes through grounding or use the exact `(snapshot required)` marker; the source currently retains no quotes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Learning inside a fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — useful existing source link, but no independent new edge needed; another generic bounded-architecture case adds less than the temporal retention distinction.
- [Historical Incremental Self-Improvement review](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) → source — a new inbound evidence link would expand a historical record's declared evidence boundary. Keep the outbound comparison; leave any new analysis to the current whole-system workflow.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Prioritize the Gödel-machine reverse edge. The compounding edge is useful as a narrow limit case, not as proof of causal compounding.
- This report records candidates only; no source, library note, historical review, or index was edited.
