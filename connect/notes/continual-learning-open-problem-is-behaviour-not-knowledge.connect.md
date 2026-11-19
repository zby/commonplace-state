---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Continual learning requires governing behaviour-changing writes, not just storing content

**Source:** [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md)

## Discovery Trace

**Destination: notes**

- **Curated heads:** Read [Notes](../../../../notes/README.md), [Learning theory](../../../../tags/learning-theory-README.md), and [deploy-time-learning](../../../../tags/deploy-time-learning-README.md). Neither tag README declares `complete: true`, so I did not skip the by-tag sweep.
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — surfaced the source’s immediate neighborhood and flagged [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md), [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md), and [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) as the strongest unlinked candidates.
- **Description listing scan:** `rg '^description:' kb/notes/ --glob '*.md'` — kept the four candidates above because each adds a missing reader move: tractable first loop, candidate-selection gates, governance control surfaces, or cross-form operation profile. The same scan also surfaced already-linked neighbors such as `retained-artifacts-enable-persistent-deployment-time-adaptation`, `the-deployed-system-not-the-model-is-the-unit-of-learning`, and `knowledge-storage-does-not-imply-contextual-activation`; I rejected them as already-served traversal paths rather than new candidates.
- **Body search:** `rg -n "continual learning|deploy-time|behavio[u]?r-changing|representational form|govern|validat|learning-value|behavioral authority|readable-artifact|reflective coverage" kb/notes/ --glob '*.md'` — confirmed that:
  - [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) narrows the source’s three-form governance problem to the near-term natural-language/symbolic loop.
  - [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) splits the source’s “choose and validate” clause into two distinct acceptance checks.
  - [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) explains which structural surfaces make the source’s validation, correction, and drift-control operations possible.
  - [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) supplies the cross-form coverage vocabulary behind the source’s parametric / natural-language / symbolic distinction.
- **Link following:** Followed the already-loaded neighborhoods in the four candidate notes. That pass reinforced that the source already covers the coevolution / retained-artifact / deployed-system cluster directly, so I kept only the candidates that add a distinct next question rather than another restatement of the same cluster.

**Destination: reference**

- **Curated head:** Read [Reference](../../../../reference/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` — flagged [Agent memory coverage](../../../../reference/agent-memory-coverage.md) and [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) as the strongest current-state surfaces for the source’s governance frame.
- **Description listing scan:** `rg '^description:' kb/reference/ --glob '*.md'` — kept [Agent memory coverage](../../../../reference/agent-memory-coverage.md) because it maps validation, authority, activation, lifecycle, and promotion gaps onto the shipped Commonplace system. [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) stayed adjacent but weaker because it is a future-work plan rather than the current-state map.
- **Body search:** `rg -n "continual learning|deploy-time|behavio[u]?r-changing|representational form|govern|validat|learning-value|behavioral authority|readable-artifact|reflective coverage" kb/reference/ --glob '*.md'` — confirmed that [Agent memory coverage](../../../../reference/agent-memory-coverage.md) is the best descriptive witness for the source’s claim inside Commonplace because it names exactly the current authority / activation / lifecycle surfaces and their missing pieces.
- **Link following:** Followed the loaded links from [Agent memory coverage](../../../../reference/agent-memory-coverage.md) to its implementation references and stopped there; nothing in that neighborhood offered a better first reference edge than the coverage map itself.

**Destination: agent-memory-systems**

- **Curated head:** Read [Agent Memory Systems](../../../../agent-memory-systems/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`
- **Body search:** `rg -n "continual learning|deploy-time|behavio[u]?r-changing|representational form|govern|validat|learning-value|behavioral authority|readable-artifact|reflective coverage|trace-learning" kb/agent-memory-systems/ --glob '*.md'`
- Evaluation: the promising surfaces were survey-scale notes such as [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md), but the source already links that note directly. I did not find a stronger unlinked agent-memory-systems target that beat the existing survey edge on articulation value.

**Destination: instructions**

- **Curated head:** Read [Instructions](../../../../instructions/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/instructions/ --glob '*.md'`
- **Body search:** `rg -n "continual learning|deploy-time|behavio[u]?r-changing|representational form|govern|validat|learning-value|behavioral authority|readable-artifact|reflective coverage|review|freshness" kb/instructions/ --glob '*.md'`
- Evaluation: no instruction survived the articulation test. The notes collection contract says notes → instructions is usually inverse, and this scan did not reveal an `operationalized-from` or high-value `see-also` exception for this source.

**Destination: sources**

- **Curated head:** Read [Sources](../../../../sources/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/sources/ --glob '*.md'`
- **Body search:** `rg -n "continual learning|deploy-time|behavio[u]?r-changing|representational form|govern|validat|learning-value|behavioral authority|readable-artifact|reflective coverage|trace-learning" kb/sources/ --glob '*.md'`
- Evaluation: the strongest hits were source ingests and snapshots already routed through notes the source either already links or that did not improve traversal beyond the kept note/reference candidates. I did not keep a new source-collection target.

**External destination**

- Authorized by the notes collection contract, but no already-supplied external artifact was in loaded context, so external prospecting was skipped.

## Connections Found

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **extends**: the source states the full three-form governance problem; this note gives the practical first slice a reader would follow when asking which part of that problem is tractable now.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **mechanism**: the source says continual learning must choose and validate behaviour-changing writes; this note decomposes that acceptance step into the distinct validity and value gates the source leaves implicit.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **mechanism**: the source says governance must validate, correct, and coordinate writes; this note explains which scheduler, context-engine, and substrate surfaces make those governance operations possible or impossible.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- **grounds**: the source’s cross-form writable-surface claim depends on a reader being able to distinguish observation, selection, configuration, and modification across natural-language, symbolic, and parametric forms.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- **evidenced-by**: Commonplace’s current memory-system map independently breaks durable behaviour change into contracts, validation, activation, authority, lifecycle, and promotion gaps, corroborating the source’s claim that storage alone is not the governing problem.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- rejected because the source already links it directly and already delegates the retained-artifact branch there.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- rejected because it is already a direct source link and already covers the model-only boundary the source depends on.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected because it is already a direct source link and already carries the storage-versus-activation distinction.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected as a new candidate because it is already the source’s current survey-scale external evidence edge.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected because it is a future-work plan for one shipped system, while [Agent memory coverage](../../../../reference/agent-memory-coverage.md) is the better current-state descriptive witness.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- the curated head currently covers the framework claim, verifiability gradient, readable-artifact loop, and coevolution, but it omits this umbrella statement that the open problem is governing behaviour-changing writes rather than merely storing content.
- [Learning theory](../../../../tags/learning-theory-README.md) -- the curated head moves from broad learning definitions to deploy-time adaptation, and this note is a missing bridge from “capacity change” to the multi-form governance problem.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
