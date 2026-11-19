---
description: "Discovery report for possible KB connections from Harness Continual Learning"
type: kb/cache/types/connect-report.md
source: "kb/sources/harness-continual-learning-adaptation-beyond-model-parameters.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Harness Continual Learning

**Source:** [Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.md)

## Discovery Trace

**Source contract and curated heads:**

- Read the sources collection contract. The snapshot is immutable, so its adjacent ingest report is the authored outbound surface. The contract authorizes prospecting in notes, reference, sources, agent-memory systems, and agentic systems; it excludes work and instructions. External targets are authorized only when already known, and none was supplied.
- Read the curated heads at 'kb/notes/README.md', 'kb/reference/README.md', 'kb/sources/README.md', 'kb/agent-memory-systems/README.md', and 'kb/agentic-systems/README.md'. The notes head routed the paper toward deploy-time learning; the memory head routed its trace-to-artifact loop toward code-grounded harness cases; the agentic head exposed Autogenesis as the closest whole-system mutation comparison. The reference and sources heads supplied collection roles but no direct item-level candidate.
- The snapshot carries no topical tags, so no tag-README was selected and no tag-completeness skip applied.

**Complete title and description scans:**

- Ran 'rg -N --no-heading -m1 "^# " kb/<destination>/ --glob "*.md"' once for every authorized local destination: 355 note titles, 136 reference titles, 523 source titles, 173 agent-memory-system titles, and 12 agentic-system titles.
- Ran 'rg "^description:" kb/<destination>/ --glob "*.md"' for the same destinations: 352 note descriptions, 134 reference descriptions, 457 source descriptions, 171 agent-memory-system descriptions, and 10 agentic-system descriptions.
- The title/description surface shortlisted the deployed-system, governed-write, proposal-selection, oracle-domain, fixed-decomposition, and experimental-contrast notes; Self-Harness, Continual Harness, Co-Harness, HarnessCompass, Harness Updating Is Not Harness Benefit, and Agent Optimizers among sources; Meta-Harness and Agentic Harness Engineering in the memory casebook; and Autogenesis in the whole-system casebook.

**Body searches:**

- 'rg -n -i "harness-level forgetting|historical[- ]retention|stability[–-]plasticity|catastrophic forgetting" kb/notes/ --glob "*.md"' found no note using the paper's harness-level-forgetting formulation. The nearest settled theory instead speaks in terms of governed behavior-changing writes, regression, and oracle domain.
- 'rg -n -i "proposal.{0,40}evaluation.{0,40}(commit|retention)|candidate.{0,50}(commit|reject)|behavio(u)?r-changing writes" kb/notes/ --glob "*.md"' confirmed that the optimizer–evaluator–commit path is an exact proposal-selection instance and that deployment-time learning already requires regression-aware write governance.
- 'rg -n -i "deployed system.{0,40}model|model alone|outside (the )?model|frozen (foundation )?model|fixed decomposition" kb/notes/ --glob "*.md"' retained the whole-system learning and fixed-decomposition candidates. It rejected weight-versus-artifact notes that did not address sequential retention.
- 'rg -n -i "harness-level forgetting|historical[- ]retention|stability[–-]plasticity|regression-gat|retention.*anchor|continual harness" kb/sources/ --glob "*.ingest.md"' identified the four closest empirical comparisons. HarnessCompass and Harness Updating Is Not Harness Benefit were read but rejected as primary edges because their distinctive questions are held-out generalization and update uptake, not historical retention across sequential harness states.
- 'rg -n -i "candidate harness|proposal.{0,30}(evaluation|commit)|rollback|regression|historical anchor|continual learning" kb/agent-memory-systems/ kb/agentic-systems/ --glob "*.md"' retained Meta-Harness and Autogenesis. Other trace-learning systems lacked a comparably explicit whole-harness candidate-and-commit boundary.
- 'rg -n -i "proposal.{0,30}(evaluation|commit)|rollback|regression|retention|self-improv" kb/reference/ --glob "*.md"' found Commonplace's reflective-system and review/freshness material, but those are project-specific implementations rather than direct targets for this paper.

**Link following:**

- Followed the neighborhoods of [continual learning requires governing behaviour-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [the deployed system is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), and [the proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). These converged on regression governance, operative retention, oracle domain, and the fixed-decomposition boundary.
- Followed [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md), [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), and [Agent Optimizers](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md). Together they separate direct adoption from reject-capable commitment, fixed-weight from cross-form updating, static regression gates from sequential retention budgets, and retention from causal compounding.
- Followed the code-grounded [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) review and [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md). Meta-Harness supplies the closest executable trace-to-candidate comparison; Autogenesis supplies the closest versioned mutation and rollback comparison but has a weaker semantic retention gate.

## Connections Found

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: HCL independently instantiates candidate selection, current validation, historical regression checking, validity checking, and coordinated operative commitment across mutable prompts, memory, skills, and routing.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the paper holds foundation-model weights fixed while harness changes produce both capability gains and forgetting, directly corroborating the claim that non-model components are part of the behavior-producing learning unit. Its narrower four-component harness boundary also qualifies the note's broader system boundary.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: the Continual Optimizer generates separately represented candidates, the Continual Evaluator can reject them, and only commitment makes a candidate affect later behavior.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: even with zero allowed loss on the finite anchor set, held-out historical forgetting remains nonzero, showing that a strict autonomous gate warrants retention only over the cases its oracle represents.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting the gains requires separating updates expressible through the fixed four-component harness from the frozen model, external capabilities, optimizer/evaluator, anchor policy, task order, objectives, and task representations.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: the component ablations vary update permission, not component presence, and disabling memory also removes its downstream skill source; they support those reported treatment bundles rather than the four-part decomposition as a whole.
- [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both keep model weights fixed and regression-gate harness edits, while HCL adds explicit sequential-task anchors, a tunable historical-loss budget, and whole-candidate commitment over four jointly versioned components.
- [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- **compares-with**: the near-inverse names conceal different architectures—Continual Harness directly adopts online edits and can co-train weights in one persistent game, whereas HCL isolates candidates, freezes weights, and gates commitment against historical behavior.
- [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: Co-Harness alternates regression-gated harness repair with model fine-tuning; HCL isolates harness-state continual learning by keeping the model frozen and varying the retention constraint.
- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both make prior-task loss a selection-time signal, but HCL sweeps a per-candidate loss budget and measures held-out forgetting, while the optimizer study asks whether retained gains transfer and survive another optimization phase.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **compares-with**: both turn retained execution evidence into candidate harnesses around a fixed model; Meta-Harness ranks task-specific code on benchmark frontiers, while HCL defines a persistent four-component state and makes historical behavior a hard commitment condition.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: both isolate candidate mutation from deployment through versioned state and evaluation, but Autogenesis has stronger generic rollback machinery and a weaker default semantic regression oracle than HCL's task-specific historical anchors.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidenced-by**: HCL is a direct frozen-model experiment in coordinated, regression-aware artifact writes.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: the reported capability gains and forgetting arise solely from changes outside model parameters.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: the paper's optimizer, evaluator, and commitment decision realize the three functions explicitly.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) → source -- **evidenced-by**: the gap between zero anchor loss and nonzero held-out forgetting is a measured case of an oracle's limited domain.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- the paper reports a sequential trajectory and speculates that permissive updates weaken later capabilities, but it does not compare later improvement with and without the earlier retained gain.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- HCL retains task anchors, but it does not learn or accumulate failure-derived checks; the evaluator policy and task criteria remain fixed.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- HCL names component loci, but it commits the resulting harness jointly and supplies no explicit dependency graph or bounded impact closure.
- [HarnessCompass](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md) -- useful adjacent evidence on held-out generalization and component partitioning, but less direct than the retained comparisons for sequential historical forgetting.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- its update-versus-uptake ladder is important generally, but HCL's primary novelty is retention across committed harness states rather than model-dependent loading or adherence.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- the project-specific case shares a proposal/evaluation/retention shape, but the general notes already carry that reader need without a weak see-also detour.

## Index Membership

None.

## Synthesis Opportunities

- HCL's finite-anchor result, [warranted autonomy](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), and [governed behavior-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) together imply a sharper operational claim: a historical-loss budget is an oracle-domain parameter, not a global no-forgetting guarantee. Zero observed anchor loss can coexist with regression outside the sampled historical surface.

## Maintenance Observations

- “Harness Continual Learning” and the existing “Continual Harness” paper are distinct, near-inversely named systems. Durable descriptions and an explicit comparison are needed to prevent lexical retrieval from conflating them.

## Flags

- Split candidate: the source independently contributes a system-boundary claim, a proposal/evaluation/commitment architecture, a sampled-retention result, and fixed-decomposition-limited component evidence. Any later promotion should separate these claims rather than turn the paper into one broad theory note.
