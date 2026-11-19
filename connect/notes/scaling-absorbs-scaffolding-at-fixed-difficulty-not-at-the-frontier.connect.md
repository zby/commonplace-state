---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: Scaling and frontier scaffolding

**Source:** [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md)

## Discovery Trace

### `kb/notes/`

**Curated heads and tag routing:**

- Read [Notes](../../../../notes/README.md), [Learning theory](../../../../tags/learning-theory-README.md), and [deploy-time-learning](../../../../tags/deploy-time-learning-README.md). Neither matching tag README declares `complete: true`, so tag-scoped discovery was not skipped.
- Ran `rg -l '^tags:.*\\blearning-theory\\b' kb/notes/ --glob '*.md'` and `rg -l '^tags:.*\\bdeploy-time-learning\\b' kb/notes/ --glob '*.md'`; the latter surface placed the source beside the readable-artifact, representational-form, and bitter-lesson arguments.

**Complete recall surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and `rg '^description:' kb/notes/ --glob '*.md'`.
- The title/description scan flagged [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md), [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [Localized retention pays where change is sparse in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), and [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md).

**Body search:**

- `rg -n -i 'scaffold|harness|fixed difficulty|frontier|external structure|externaliz|absorb|relaxing|bitter lesson' kb/notes/ --glob '*.md'` found the source's existing bitter-lesson and relaxing links plus the persistence/warrant and representational-form cluster.
- `rg -n -i 'scal(e|ing)|capabilit|reliabilit|task horizon|autonomy|governance|verification' kb/notes/ --glob '*.md'` singled out the bounded-validation-radius and change-topology mechanisms as concrete versions of the source's "cheaper, more governable, or more inspectable" condition.
- `rg -l -i 'reliability function|governance value|task horizon|moving frontier|new structure|durable external' kb/notes/ --glob '*.md'` reduced the candidate set to the source and [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md); the latter is already linked by the source.

**Link following and evaluations:**

- Followed the persistence note's links to the bitter-lesson, governance, and oracle arguments. It supplies the general rule that no machinery survives by position; the source supplies a distinct time-indexed, frontier-versus-fixed-task condition, so both directions pass the articulation test.
- Followed the readable-artifact loop's links to representational-form coevolution, codification/relaxing, and the authoritative-record boundary. Its bounded validation radius explains one concrete reason an external reliability function can remain advantageous.
- Followed localized retention's links to readable artifacts and the bitter lesson. It explains when externally addressable units lower adaptation and validation cost, but does not itself make the source's frontier claim.
- Rejected [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), [Increasing computational autonomy relocates human effort to an elastic frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md), and [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) as new candidates: each is already an authored source link.

### `kb/sources/`

**Curated head and recall surfaces:**

- Read [Sources](../../../../sources/README.md), then ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, `rg '^description:' kb/sources/ --glob '*.md'`, and the two source-tag queries above. No source-tag README matched the source's tags.
- `rg -n -i 'scaffold|harness|fixed difficulty|frontier|externaliz|absorb|bitter lesson' kb/sources/ --glob '*.md'` and `rg -n -i 'scal(e|ing)|capabilit|reliabilit|task horizon|autonomy|governance|verification' kb/sources/ --glob '*.md'` surfaced Co-Harness and the three cases the source already cites.

**Link following and evaluations:**

- Read [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../sources/co-harness-co-evolving-harness-and-model-weights.md). Its alternating loop explicitly says a stronger model can expose higher-order harness bottlenecks; that is direct, though only provisional, evidence for the source's recurrence condition.
- Rejected the already-linked Claude Fable, financial-services, and effective-harnesses ingests as new candidates because they are already the source's stated three observations. Rejected [Ingest: Externalization in LLM Agents](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md): it maps the artifact space but supplies no matched cross-generation or moving-frontier evidence.

### `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/instructions/`, and `kb/types/`

**Curated heads and recall surfaces:**

- Read the root READMEs for reference, agent-memory-systems, agentic-systems, sources, and instructions. `kb/types/` has no root README; its collection was still checked through its complete title and description surfaces.
- For every destination, ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'`; ran the source-tag queries across the non-notes destinations as well.
- Ran `rg -n -i 'scaffold|harness|fixed difficulty|frontier|externaliz|absorb|bitter lesson'` over each destination, then `rg -n -i 'scal(e|ing)|capabilit|reliabilit|task horizon|autonomy|governance|verification' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ kb/types/ --glob '*.md'`.

**Evaluations:**

- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) is a useful fixed-model harness-evolution case, but it does not compare changing model generations or establish the source's longitudinal condition; reject it as direct evidence for this claim.
- The reference, agentic-systems, instructions, and type hits described package mechanics, workflow operations, or structural contracts rather than a general explanation or evidence for frontier recurrence. No candidate passed the articulation test.
- `external` is authorised only for already-known targets. No external target was supplied or already loaded beyond the snapshots above, so open-web prospecting was skipped.

## Connections Found

- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — **extends**: it gives the source's claim its general selection principle — external machinery persists only while its function earns a warrant — while this source distinguishes the fixed-task absorption case from the moving deployment frontier where a new warrant can recur.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — **mechanism**: bounded validation radius, explicit dependencies, and inspectable rollback explain a concrete way that an external reliability or governance function can remain cheaper and more governable than an absorbed parametric alternative.
- [Localized retention pays where change is sparse in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — **grounds**: its change-topology condition supplies one testable economic boundary for the source's conditional externalization claim — durable external structure pays when new frontier changes remain localized in addressable, dependency-explicit units.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — **extends**: its generic account of coupled weight, natural-language, and symbolic improvement loops needs this source's claim to explain why stronger weights need not eliminate the readable side at the tasks newly attempted at deployment.
- [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../sources/co-harness-co-evolving-harness-and-model-weights.md) — **evidenced-by**: its alternating model/harness loop reports that an updated model exposes higher-order harness bottlenecks, a concrete recurrence mechanism; retain the source note's caveat that this is not a matched, cross-generation deployment trend.

## Bidirectional Candidates

- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) <-> source — **extends**: a reader of the general persistence-by-warrant argument gains this note's fixed-task/frontier discriminator and proposed longitudinal test, not merely a duplicate bitter-lesson application.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source — **extends**: a reader of the generic coevolution frame gains the deployment-selection condition under which a readable external layer persists while parametric capability grows.

## Reverse-edge Candidates

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source — **extends**: its claim that readable artifacts remain useful regardless of opaque-loop maturity needs the source's sharper condition that this remains true only when frontier difficulty and an external reliability advantage continue to grow or hold.
- [Localized retention pays where change is sparse in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) → source — **extends**: its representation-neutral locality criterion would gain a deployment-scale boundary showing why a currently effective external decomposition can be absorbed on old tasks yet be re-created for a newly opened task frontier.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — already linked by the source for the fixed-difficulty relaxation half; another edge would not add a traversal need.
- [Increasing computational autonomy relocates human effort to an elastic frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) — already linked for the moving-frontier premise.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — already linked for the per-task relaxation cycle.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) — fixed-model harness search demonstrates external scaffold evolution but not the model-generation or frontier comparison this source claims requires.
- [Ingest: Externalization in LLM Agents](../../../../sources/externalization-in-llm-agents-unified-review.ingest.md) — a relevant vocabulary survey, but it does not provide the source's discriminating longitudinal evidence.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — the source adds the frontier-persistence boundary to this tag's account of durable readable artifacts and their relation to model updates.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

None.
