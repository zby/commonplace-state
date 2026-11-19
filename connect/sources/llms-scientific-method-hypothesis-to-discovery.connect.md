---
description: "Connections from Zhang et al.'s scientific-method perspective to discovery, evaluation, and hypothesis assessment"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/llms-scientific-method-hypothesis-to-discovery.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: LLMs in the scientific method

**Source:** [Publisher paper](https://www.nature.com/articles/s44387-025-00019-5.pdf). The snapshot is immutable; proposed edges belong to its ingest.

## Discovery Trace

- Read the snapshot and the sources collection's linking contract. Read the learning-theory and foundations curated heads; neither declares complete coverage. Read the sources and agentic-systems READMEs and the reference and agent-memory-system index material.
- Generated the complete title listing with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`; filtered candidate titles using `scientific|discovery|synthesis|hypothes|oracle|causal|falsif|popper`.
- Queried note descriptions with `rg '^description:' kb/notes --glob '*.md'` filtered by `scientific|hypothes|discovery|oracle`. Read automated-synthesis, known-target-discovery, discovery-lifecycle, and the hypothesis-generation-and-updating ingest. Followed the synthesis note's link to the automation/verification boundary.
- Notes: generation versus trustworthy evaluation is a strong comparison. Discovery-lifecycle is a useful process comparison but not the same ontology. Known-target benchmarks bound claims of discovery automation.
- Sources: the hypothesis-generation-and-updating paper supplies a controlled comparison to the perspective's broad agenda. Other Popper and scientific-method source matches are broader topical neighbours and were not kept.
- Reference: README routes shipped-system facts; this perspective supplies no specific change to the shipped architecture. No candidate kept.
- Agentic systems: index entries include research and verification systems, but the perspective neither analyzes those exact systems nor supplies a distinct source-grounded comparison. No candidate kept.
- Agent-memory systems: storage and activation vocabulary is relevant background, but the paper's scientific-method contribution does not warrant a generic memory edge. No candidate kept.
- External: evaluated only the already supplied publisher source. No external connection prospecting.
- Read notes collection labels before proposing inbound `evidenced-by` edges. No work or instructions targets prospected because the source contract excludes them.

## Connections Found

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) — **compares-with**: the perspective separates creative hypothesis generation from reliable testing and warns that formal validation can inherit translation errors; it offers an argued agenda, not a controlled test of the note's bottleneck claim.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **compares-with**: the paper distinguishes bounded scientific tools from a future capacity to pose questions and conduct open-ended discovery, which the note's benchmark boundary helps assess.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **compares-with**: its observation, hypothesis, experiment, and automation activities can be compared with the KB's explicitly constructed six-phase evaluation scheme without treating the two as identical.
- [Hypothesis generation and updating in large language models](../../../../sources/hypothesis-generation-and-updating-in-large-language-models.ingest.md) — **compares-with**: the controlled number-game probes bound what plausible hypothesis outputs reveal, whereas Zhang et al. propose roles for such outputs in scientific inquiry.

## Bidirectional Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) could cite the accepted ingest with **evidenced-by** as an independently argued scientific-workflow instance of the distinction, explicitly not as experimental confirmation.

## Reverse-edge Candidates

None beyond the bidirectional candidate.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): the narrower synthesis candidate already carries the relevant distinction; the perspective does not establish the universal-looking title.

## Index Membership

None; the source collection README describes the collection rather than enumerating papers.

## Synthesis Opportunities

The perspective, discovery lifecycle, and known-target benchmark note suggest comparing problem generation, candidate generation, and prospective assessment separately. This is a candidate comparison, not evidence that a complete autonomous discovery process exists.

## Maintenance Observations

None.

## Flags

- The paper is a perspective with cited examples, not a new dataset or controlled evaluation. Preserve that boundary in any downstream use.
