---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/improvements-can-accumulate-without-compounding.md"
source_has_frontmatter: true
date: "2026-08-07"
depth: standard
---

# Connection Report: Improvements can accumulate without compounding

**Source:** [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md)

## Discovery Trace

**Authorisation and curated heads:**

- Read `kb/notes/COLLECTION.md` first. It authorises local prospecting into `notes` (including `notes/definitions`), `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `work`. It authorises `external` only for already-known targets, so open-web prospecting was skipped.
- Read [Notes](../../../../notes/README.md), [Foundations](../../../../tags/foundations-README.md), and [Self-improving systems](../../../../tags/self-improving-systems-README.md). Neither tag head declares `complete: true`, so both by-tag description sweeps were run. The self-improving-systems head already places the source in its improvement-dynamics cluster beside cumulativity and later-episode testing.
- Read the destination heads [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), [Sources](../../../../sources/README.md), and [Instructions](../../../../instructions/README.md). `kb/types/` has no `README.md`, and no destination outside `kb/notes/` has a matching `foundations-README.md` or `self-improving-systems-README.md`.

**Complete title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each authorised local destination: `notes`, `reference`, `types`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised local destination.
- Ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `self-improving-systems` query. For the other destinations, ran `rg -l '^tags:.*\b(foundations|self-improving-systems)\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; only the Ashby source surfaced outside notes.

**Body search:**

- Across every authorised destination, ran `rg -n -i "compounding|compound|accumulat(e|es|ed|ion)|reinvest|saved (time|effort|compute)|savings|later improvement|metaproductivity|feedback.*(improvement|revision)|improvement.*feedback" kb/<destination>/ --glob '*.md'`.
- Narrowed non-note candidate files with `rg -l -i "compounding|compound|reinvest|later improvement|metaproductivity|accumulat" kb/<destination>/ --glob '*.md'`, then inspected contextual matches with `rg -n -i -C 3 'compound|accumulat|later improvement|reinvest'` (adding `autocatal` for Exo).
- **Notes and definitions:** kept [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), because it develops one possible direct contribution from retained self-directed theory into later improvement productivity. Kept [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) as a contradiction candidate because it calls the downstream spread of changes that “do not help” compounding, while the source reserves compounding for retained gains and calls worsening feedback error amplification. Rejected the objective, casebook, diagnostic-richness, ephemerality, and accepted-edit matches below. Definitions added no new term beyond the source's existing `defined-in` link to self-improving system.
- **Reference:** [Commonplace as a reflective system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) is already linked from the source and establishes cumulativity, not compounding. The ablation proposal already routes the later-episode question to the source's measurement companion. Other matches used “accumulation” in storage, review-history, or proposal senses and failed the articulation test.
- **Types:** title, description, and body scans found no type contract that corroborates or develops the causal feedback claim.
- **Agent-memory systems:** inspected the trajectory-informed-memory, incremental-self-improvement, Meta-Harness, Compound Engineering, and Eidetic review neighborhoods. They establish retention, promotion, consolidation, or later task reuse, but not that a retained benefit helped produce a later improvement; none passed the articulation test for this source.
- **Agentic systems:** kept [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) as a reverse edge because its distinction between cumulative project knowledge, same-episode acceptance, and unestablished sustained compounding directly depends on the source's feedback criterion. Rejected Exo's “autocatalytic” production relation and accumulated-corruption wording as different concepts. Rejected Agno AgentOS because its fixed outer machinery limits recursive redesign but does not itself decide whether earlier retained benefits made later hardening more productive.
- **Sources:** inspected the Huxley-Gödel Machine, Co-Harness, HyperAgents, Agent Optimizers, Harness Updating, Continual Harness, and Darwin Gödel Machine ingest neighborhoods. Kept [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) as a reverse edge: its metaproductivity-performance mismatch materially bears on the difference between immediate gain and later improvement productivity. Kept [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) as a reverse edge because its proposed harness→trajectory→weight→later-harness feedback loop depends on the source's direct-contribution criterion, while its missing matched arms leave the causal contribution provisional. HyperAgents, Agent Optimizers, Harness Updating, and Darwin Gödel Machine already reach the source directly or through its linked measurement companion, so another source-note edge would duplicate the owned evidence surface. Snapshot files were not treated as authored link surfaces; paired ingest reports were used.
- **Instructions:** title, description, and body scans found only lexical collisions such as “compound bullet” and generic accumulation wording. No procedure depends on the source's causal distinction strongly enough to justify the exceptional, meta-reader-only `rests-on` edge; the collection's frontloading posture therefore leaves this destination empty.
- **External:** skipped as required because no external target was supplied or already loaded as a candidate.

**Link following:**

- Followed the retained-theory candidate one hop through reflection, retrieval failure, reach assessment, and the general theory-mediated-learning conjecture. The neighborhood confirmed that it develops the source's explicit-theory hypothesis without claiming that retention alone proves compounding.
- Followed the false-positive candidate through proposal selection, oracle bounds, and entropy management. The neighborhood confirmed a real vocabulary-level tension, not merely a shared keyword.
- Followed Huxley-Gödel Machine through Darwin Gödel Machine, Meta-Harness, and oracle-strength notes. Its distinctive evidence is descendant productivity diverging from immediate benchmark performance; this supports an ingest-to-theory reverse edge rather than treating the source as derived from HGM.
- Followed Co-Harness through representational-form coevolution, diagnostic richness, SkillRL, and Meta-Harness. The neighborhood confirmed a plausible direct feedback architecture but no matched ablation that identifies the earlier retained benefit's contribution, so the ingest should depend on the source's criterion rather than count as confirming evidence.
- Followed Compound Engineering through its later-episode-compounding link and project-knowledge analysis. The source note is the missing premise for the analysis's sharper accumulation-versus-feedback distinction; the authorised reverse label is `rests-on` under `kb/agentic-systems/COLLECTION.md`.

## Connections Found

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- **extends**: develops one possible direct contribution in which an addressable self-directed theory makes later self-improvement more sample-efficient, while preserving that interpretation and retention are conditions rather than evidence that the contribution occurred.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- **contradicts**: calls the downstream spread of accepted changes that do not help “compounding,” whereas the source reserves compounding for earlier benefits helping produce later gains and classifies worsening feedback as error amplification.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) → source -- **rests-on**: its claim that retained project knowledge and same-episode gates do not establish sustained compounding depends on the source's causal feedback criterion, not only on the linked measurement protocol.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) → source -- **is-evidence-for**: the observed mismatch between an agent's immediate benchmark performance and its descendants' productivity materially supports separating a retained gain from the ability to help produce later gains.
- [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) → source -- **rests-on**: its harness→trajectory→weight→later-harness loop counts as compounding only if each earlier benefit causally improves a later episode; the ingest's missing matched arms leave that contribution provisional.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) -- relevant to the source's scope, but the existing `defined-in` link to self-improving system already supplies boundary, horizon, and objective; another footer edge would add little traversal value.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- profiles cumulativity and explicitly says its placements do not establish improvement; it supplies no evidence that retained benefits make later improvement more productive.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- explains what evidence improves later proposal quality, but does not establish that a retained improvement produced that evidence or contributed causally across episodes.
- [Ephemeral computation prevents accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md) -- contrasts persistence with re-derivation and says retained artifacts can make later tasks easier, but its “next problem” is task execution rather than a later improvement episode; it does not supply the source's productivity feedback.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- sharpens the same immediate-check/later-generalization asymmetry in one rule-mining case, but the source's existing link to the later-episode measurement note already owns the general inference.
- [Commonplace as a reflective system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- already linked from the source and establishes a cumulative human-inclusive pathway; its compounding contribution remains explicitly unmeasured.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) -- reward-gated retention and rollback show accumulation, but the reviewed evidence does not isolate whether earlier benefits improve the later improvement process.
- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) -- reports later task reuse of retained tips, not feedback from those task benefits into production of further improvements.
- [Eidetic](../../../../agent-memory-systems/reviews/eidetic.md) -- uses “compounding” for search-before-write consolidation into an existing memory card; this is an external system's operation name for accumulation and deduplication, not evidence of cross-episode improvement productivity.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- calls its bounded auto-improvement loop convergent hardening rather than compounding, but fixed outer machinery limits redesign scope rather than deciding the source's causal question; no later-episode productivity comparison is reported.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- its recursive/autocatalytic distinction concerns production completeness and self-speedup, while “failed changes accumulate as corruption” concerns retention of errors; neither supplies the source's gain-specific feedback path.
- [Ingest: HyperAgents](../../../../sources/hyperagents.ingest.md), [Ingest: Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md), [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md), and [Ingest: Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) -- these cases already reach the source directly or through its later-episode measurement companion, which owns their evidence details; another direct edge would duplicate a well-formed chain.
- [Note type](../../../../types/note.md) -- governs note shape and frontmatter, not the truth, mechanism, or evidence of accumulation or compounding.
- [Compound bullet](../../../../instructions/review-gates/structural/compound-bullet.md) -- lexical collision only; “compound” describes bullet structure, not feedback across improvement episodes.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) uses “compound” for retained harmful errors under an unchanged objective, while the source explicitly names that pathway error amplification rather than compounding. A later maintenance pass should reconcile the vocabulary or state that the false-positive note is indexing improvement to a different objective.

## Flags

- Unresolved terminology tension: the proposed `contradicts` edge to the false-positive note should remain visible until the two uses of “compounding” are reconciled.
