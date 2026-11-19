---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: Localized retention pays where change is sparse in a matching decomposition

**Source:** [Localized retention pays where change is sparse in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md)

## Discovery Trace

**Curated heads and tag scans:**

- Read the available destination heads for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`, plus the source's `learning-theory` and `deploy-time-learning` tag READMEs. `kb/types/` has no `README.md`, so its complete title and description surfaces were used instead. `learning-theory-README.md` declares `covered_by`, not `complete`; `deploy-time-learning-README.md` has no completeness mark, so neither head justified skipping the by-tag scans.
- Ran `rg -l '^tags:.*\blearning-theory\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the equivalent `deploy-time-learning` query. These surfaced the representational-form, coevolution, decomposition-warrant, addressability, and readable-artifact neighborhoods. Kept the form definition and coevolution frame; rejected the decomposition-warrant and explicit-only claims after full reads because the source's existing Parnas, use-test, bitter-lesson, and reflection links already cover those reader needs more directly.

**Full title and description surfaces:**

- Generated fresh complete `# ` title listings with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all seven local destinations: notes (320 titles), types (9), reference (124), agent-memory-systems (171), agentic-systems (8), sources (403), and instructions (36).
- Ran `rg '^description:' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md' | rg -i 'decompos|locali|sparse|change|revision|dependenc|granular|modul|coupl|cohes|representational|parametric|schedule|drift|addressab|validation|artifact.*unit|unit.*artifact'`. Kept `task-fitted-structure-costs-cross-task-reuse.md` as a narrower temporal application; no type, reference, agentic-system, or instruction description passed the articulation test.

**Body search:**

- Ran `rg -n -i 'change topology|change footprint|sparse change|matching decomposition|revision (cost|radius)|localized (edit|revision|retention)|dependency closure|change schedules|changes together|information hiding|Parnas|dense.*change|model edit|mixture.of.experts'` over every authorised local destination. This found the already-authored Parnas edge, existing backlinks from the new bitter-lesson and reflection notes, the unit-boundary tension with short composable notes, and ROME's narrow model-editing result.
- Ran `rg -n -i 'bounded (text )?edit|selective (edit|revision)|edit locality|locality|localized|independent(ly)? (edit|update)|update existing|granular|granularity|modular|cohesion|change together|revision cost|blast radius' kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. `o-o.md`, `dense-mem.md`, and several reviews describe packaging or retrieval granularity, but none establishes change-sparse revision cost; they were rejected rather than used as evidence.
- Ran `rg -n -i 'one (idea|claim)|atomic|split|bundle|cohes|change|revision|scope|artifact' kb/instructions --glob '*.md'` and read `kb/instructions/COLLECTION.md` for the first-class inverse-edge pass. No procedure's rule materially depends on this note strongly enough to warrant an exceptional `rests-on` edge.

**Link following:**

- Followed the source's Parnas, reflection/addressability, readable-artifact, decomposition-use-test, bitter-lesson, and retrieval links, then inspected the candidate neighborhoods around representational-form coevolution, short composable notes, task-fitted structure, decomposition provenance, explicit retention, second-order revision, and the ROME ingest.
- Backlink search `rg -n -l 'localized-retention-pays-where-change-is-sparse-in-a-matching' kb --glob '*.md'` found two library backlinks: `reflection-buys-addressability.md` and `the-bitter-lesson-selects-production-methods-not-representational.md`. Both already author useful inbound edges, so neither is repeated as a candidate.
- External prospecting was skipped: `external` authorisation permits already-known evidence, but no external target was supplied and connect uses repository-local discovery only.

## Connections Found

- [Representational form](../../../../notes/definitions/representational-form.md) — **defined-in**: defines the localized-versus-distributed axis the source relies on when it claims that forms win where their unit structure matches the change class.
- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) — **contrasts**: short atomic units optimize co-loading and discovery, while this source says maintenance units should follow change covariance; readers designing note boundaries need the tension rather than either rule alone.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — **extends**: develops the source's heterogeneous-change conclusion into the broader frame of asynchronous improvement loops across natural-language, symbolic, and distributed-parametric forms.
- [Task-fitted structure costs cross-task reuse](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — **extends**: works out the source's change-matching mechanism for KB structure whose original question set drifts, including the accumulating cost of units hardened around yesterday's task.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) — **extends**: applies the source's heterogeneous-change result to the bitter lesson, showing why scalable search over localized forms is a live quadrant rather than a defense of permanent hand-crafting.
- [Ingest: Locating and Editing Factual Associations in GPT](../../../../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — **evidenced-by**: supplies a narrow distributed-parametric case where a factual edit is localized and specific, while its missing scope-addressability and untested sequential scale sharply bound the source's model-editing example.

## Bidirectional Candidates

- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) <-> source — **contrasts**: its readers independently need to know that the smallest co-loadable unit may not be the unit whose contents change together.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source — **mechanism**: the source supplies the change-topology mechanism for why a heterogeneous deployment can retain more than one form instead of converging on one universal update medium.
- [Task-fitted structure costs cross-task reuse](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) <-> source — **mechanism**: the source explains its temporal drift cost as mismatch between retained boundaries and the decomposition in which later changes are sparse.

## Reverse-edge Candidates

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source — **mechanism**: this source separates an explicit dependency graph from a genuinely small closure, supplying the missing conditions behind that note's bounded-validation-radius claim.
- [Ingest: Locating and Editing Factual Associations in GPT](../../../../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) → source — **is-evidence-for**: the ingest already identifies selective parametric revision as reusable evidence and should name this source as the theory claim its localization/specificity result bears on.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Provenance warrants a decomposition's scope claim; only discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — genuine epistemic overlap, but the source already links the Parnas case, the local-use/transfer distinction, and the bitter-lesson scope criterion; another decomposition-warrant edge would not add a distinct traversal need.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — addressability is upstream context already reached more precisely through `reflection-buys-addressability.md`; this candidate does not explain the sparse-change payoff.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) — selectively revises represented commitments, but does not establish when such revision is cheaper than substrate-level correction; keyword overlap alone is insufficient.
- [o-o](../../../../agent-memory-systems/reviews/o-o.md) — its all-in-one polyglot packaging is an intuitive counter-shape, but the review reports portability/modularity tradeoffs rather than observed revision cost under different change schedules.
- [Parnas (1972), "On the Criteria To Be Used in Decomposing Systems into Modules"](../../../sources/parnas-1972-criteria-decomposing-systems-modules.md) — the source already authors the strongest `abstracted-from` edge to this snapshot.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — the source supplies one condition under which externalized structure pays, but the scaling note's reader reaches that condition through its existing production-method link; a direct reverse edge would duplicate the stronger path.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — distinguishes why a change arrived, whereas this source concerns the footprint after it arrives; the distinction does not materially develop or test the topology claim.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — the source adds the missing change-topology criterion for choosing among deploy-time update forms and belongs in the framework or learning-fundamentals grouping.

## Synthesis Opportunities

- The source together with [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) and [Task-fitted structure costs cross-task reuse](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) implies a higher-order claim: artifact granularity is a multi-objective decomposition problem. Co-loading favors small independent claims, maintenance favors grouping content that changes together, and reuse favors keeping task-derived structure replaceable; no single "atomicity" rule optimizes all three.

## Maintenance Observations

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) currently moves directly from explicit dependencies to a bounded causal neighborhood. This source distinguishes computable impact from small impact: an explicit graph can expose a system-wide closure. The earlier note should be tightened or linked to this qualification so the two claims do not remain in apparent conflict.

## Flags

- Unresolved design tension: co-loading atomicity and change-cohesion can prescribe different boundaries. The source states the maintenance rule strongly, while the short-composable note states the consumption rule strongly; a future synthesis should name how to arbitrate when they diverge.
- Unresolved claim tension: the readable-artifact note treats explicit dependencies as sufficient for bounded validation, while this source requires both explicit dependencies and bounded downstream impact.
