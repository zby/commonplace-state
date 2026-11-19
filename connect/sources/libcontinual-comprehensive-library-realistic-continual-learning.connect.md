---
description: "Discovery report for possible KB connections from the LibContinual source snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/libcontinual-comprehensive-library-realistic-continual-learning.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: LibContinual: A Comprehensive Library towards Realistic Continual Learning

**Source:** [LibContinual: A Comprehensive Library towards Realistic Continual Learning](../../../sources/libcontinual-comprehensive-library-realistic-continual-learning.md)

## Discovery Trace

**Curated heads:**
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source carries no topical `tags`, so no tag-README by-tag listing substituted for a search pass.

**Full title and description scans:**
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over each authorised local destination: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- Ran `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'continual|forget|retention|plastic|memory budget|resource|benchmark|evaluation|fixed decomposition|task structure|semantic|stream|replay|deployed system|representational form|update space|shortcut'`. This retained the fixed-decomposition, experimental-contrast, cross-form continual-learning, localized-retention, and memory-policy clusters for closer reading.
- Ran equivalent whole-collection description scans for `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`, filtered by `continual`, `forget`, `retention`, `memory budget`, `resource`, `benchmark`, `evaluation`, `replay`, `semantic homogeneity`, `task structure`, and `harness`. The reference and agentic-system surfaces produced no source-specific candidate. The agent-memory scan produced only generic memory-budget and trace-learning matches. The source scan surfaced HCL and the agentic-adaptation survey as the useful comparison set.

**Body search:**
- `rg -n -i 'continual learning|catastrophic forgetting|stability-plasticity|single-pass|offline data' kb/notes/ --glob '*.md'` -- kept the cross-form continual-learning cluster for scope comparison; rejected the broad deployed-system claim as too strong for this model-only paper.
- `rg -n -i 'memory budget|resource-aware|accuracy per|storage form|replay privilege' kb/notes/ --glob '*.md'` -- kept the resource-normalisation issue; rejected generic agent-memory operational-policy matches because LibContinual measures algorithmic retained-state overhead rather than capture, activation, authority, or lifecycle.
- `rg -n -i 'semantic homogeneity|category-randomized|task structure|semantic shortcut|data ordering' kb/notes/ --glob '*.md'` -- found no existing note that already owns the benchmark-stream claim.
- `rg -n -i 'fixed decomposition|effective update space|experiment identifies|benchmark' kb/notes/ --glob '*.md'` -- kept the fixed-decomposition and experimental-contrast notes as the interpretive basis.
- `rg -n -i 'offline data|memory budget|semantic homogeneity|category-randomized|single-pass|continual learning|catastrophic forgetting' kb/{reference,agent-memory-systems,agentic-systems,sources}/ --glob '*.md'` -- confirmed HCL as the nearest source comparison and found no direct reference or agentic-system landing.

**Link following:**
- Followed [HCL's ingest](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) into the fixed-decomposition and experimental-contrast notes. HCL's finite anchors, fixed task order, and unaccounted harness-state growth make LibContinual's access/resource/stream axes directly useful as evaluation qualifications.
- Followed [continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) into governed behaviour-changing writes and localized retention. LibContinual supplies a distributed-parametric resource-accounting slice, not evidence that a model-only update boundary is the right deployed-system boundary.
- Followed [the agentic-adaptation survey ingest](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md). Its component-counterfactual and dynamics-aware evaluation agenda is compatible with LibContinual, while LibContinual adds concrete data-access, retained-state, and task-composition protocols.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: LibContinual learns and compares within fixed supervised image-classification signals, method families, update operations, task partitions, backbones, metrics, and resource accounting; reported gains and failures do not validate those fixed choices.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: the online analysis contrasts differently pretrained architectures and update spaces without a fully matched offline arm, while category randomization jointly changes semantic co-occurrence, domain mixing, task boundaries, and order; the resulting effects remain bundle-level.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: LibContinual normalizes extra image, feature, model, parameter, and prompt storage for distributed-parametric continual-learning methods, but excludes natural-language and symbolic behaviour-shaping artifacts and their cross-form coordination costs.
- [Ingest: Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- **compares-with**: HCL measures finite-anchor retention while leaving state cost and task-stream construction fixed; LibContinual identifies retained-state budget, data-revisit privilege, and stream composition as evaluation axes that an adaptive-harness benchmark should declare and vary.
- [Ingest: Adaptation of Agentic AI](../../../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) -- **compares-with**: the survey argues for component-counterfactual and dynamics-aware adaptation evaluation, while LibContinual supplies concrete parametric protocols for access, memory, and task-structure sensitivity.

## Bidirectional Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) <-> source -- **evidenced-by**: LibContinual shows method rankings and apparent robustness changing when three formerly conventional evaluation choices are varied, while its remaining fixed choices bound the result.

## Reverse-edge Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: add LibContinual as a benchmark-design case where revising an outer decomposition exposes fragility hidden by the original evaluation space.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Continual learning requires governing behaviour-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- rejected as a direct evidence edge: LibContinual studies model and auxiliary-parameter adaptation but does not test selection, authority, installation, or rollback across a deployed system's full behaviour-changing surface.
- [Localized retention pays when sparse changes have bounded impact](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- rejected as evidence: the low-memory plots compare heterogeneous methods and backbones and do not measure sparse edit matching or bounded behavioural impact closure.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) -- rejected: LibContinual's byte accounting does not evaluate capture, derivation, activation, authority, lifecycle, or downstream memory effects.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- rejected: it is a Commonplace-specific design proposal, whereas LibContinual offers no direct evidence about Commonplace's declared objective or its ablation arms.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected: shared continual-learning vocabulary does not overcome the source's absence of agent trace ingestion, memory activation, or artifact promotion.

## Index Membership

None

## Synthesis Opportunities

- **Evaluation privilege is part of a continual learner's effective environment.** LibContinual's three axes, HCL's finite-anchor boundary, and the agentic-adaptation survey's dynamics-aware evaluation agenda jointly suggest that a continual-learning evaluation should declare and control data-revisit access, total retained-state budget, and task-stream construction before interpreting stability or plasticity. This claim is not yet owned by an existing note.

## Maintenance Observations

None

## Flags

- The paper reports three independent benchmark investigations plus a library architecture. The ingest should keep the resource/access/stream evaluation claim primary and avoid treating the framework's modularity or five-family taxonomy as independently validated contributions.
