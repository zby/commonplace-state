---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/harnessdev-llms-create-and-evolve-agent-harnesses.md"
source_has_frontmatter: true
date: "2026-09-04"
depth: standard
---

# Connection Report: HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

**Source:** [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](../../../../sources/.snapshots/harnessdev-llms-create-and-evolve-agent-harnesses.md)

## Discovery Trace

**Curated heads and description listings:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no `tags:` field, so no tag README or by-tag scan applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over all five authorised local destinations. The scans covered 427 note titles, 161 reference titles, 175 agent-memory-system titles, 16 agentic-system titles, and 373 source titles.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` separately over the same destinations. The scans covered 425 note descriptions, 160 reference descriptions, 173 agent-memory-system descriptions, 14 agentic-system descriptions, and 373 source descriptions.
- Ran `rg -n -i '^description:.*(harness|self-improv|evol|adapt|feedback|held-out|executor|runtime model|benchmark|evaluation|regress|transfer|noise|indetermin|agent loop|tool loop|trajectory)' kb/<destination>/ --glob '*.md'` over each destination. The strongest candidates concerned the deployed system as the unit of learning, diagnostic richness, execution indeterminism, fixed decompositions, proposal-selection loops, trace-aware workflow evaluation, harness-search systems, and existing harness-evolution studies.

**Body search:**

- Identity and prior coverage: `rg -n -i 'HarnessDev|2609\.01437|self-eval|unified-eval|creator.{0,20}executor|executor.{0,20}creator' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. No prior HarnessDev or arXiv-identifier match was found; the remaining hits supplied creator/executor and evaluation vocabulary only.
- Notes: `rg -n -i 'harness|runtime model|executor model|creator model' kb/notes --glob '*.md'`; `rg -n -i 'held-out|feedback set|regression|non-monotonic|overfit|generalization' kb/notes --glob '*.md'`; and `rg -n -i 'execution cost|token cost|dead code|reachable|same commit|noise band' kb/notes --glob '*.md'`. Candidates were kept only where HarnessDev measured the note's mechanism, not merely where both discussed evaluation.
- Reference: `rg -n -i 'trajectory-aware|harness capture|runtime model|executor|held-out|regression|ablation|evaluation noise|same commit|model partition' kb/reference --glob '*.md'`. The trajectory-aware evaluation proposal survived as a method companion; Commonplace-specific harness-capture and sub-agent regression records did not.
- Agent-memory systems: `rg -n -i 'harness evolution|harness optimization|runtime model|executor|feedback|trajectory|regression' kb/agent-memory-systems --glob '*.md'`. Meta-Harness and Agentic Harness Engineering supplied concrete optimisation-loop comparisons, while the trace-learning synthesis supplied the broader evidence destination.
- Agentic systems: `rg -n -i 'self-evolv|self-improv|harness|runtime model|executor|feedback|trajectory|regression' kb/agentic-systems --glob '*.md'`. Autogenesis survived because its versioned mutation and rollback loop gives a specific self-evolution contrast; systems that only expose generic execution or observability primitives did not.
- Sources: `rg -n -i 'Harness Updating|Agent Optimizers|Meta-Harness|Self-Harness|HarnessCompass|same model, different harness|Continual Harness|AutoSaddler' kb/sources --glob '*.md'`. Kept four comparisons with distinct axes: fixed-model harness effects, editor/user separation, held-out cross-model evolution, and sequential optimisation with regression.
- Synthesis check: `rg -n -i 'harness effect|harness.*conditional|executor compatibility|cross-executor|model.?harness|runtime binding|runtime model.*harness|harness.*runtime model' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` and `rg -n -i 'capability.*efficien|efficien.*capability|execution tokens|task success.*cost|cost.*task success|higher.*cost.*better|harness quality' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. These found components of a conditional harness-effect claim but no note that combines executor compatibility, resource regime, and evaluation decomposition.
- External destinations are authorised, but repository-local discovery found no already-known external target that added a distinct traversal need. Open-web prospecting was therefore skipped as required by the connect workflow.

**Link following:**

- Followed [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) into the fixed-decomposition and proposal-selection-loop neighborhood. This separated the paper's system-level evidence from the narrower claim that one creator model improved itself.
- Followed [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) into Meta-Harness, Agentic Harness Engineering, AutoSaddler, and the trace-learning synthesis. The paper's rare use of its dedicated trajectory interface and its successful targeted diagnosis make this an evidence connection, while the inspected systems remain comparisons because HarnessDev does not run a controlled diagnostic-richness ablation.
- Followed the compounding and retained-artifact neighborhoods into Agent Optimizers, Harness Updating, and HarnessCompass. This distinguished operative version selection from the stronger claim that earlier improvements cause later improvements.
- Followed the trajectory-aware evaluation proposal into intended-path health and harness-capture records. HarnessDev's preserved trajectories and reachability audit are method-adjacent, but they do not establish a matched intended-path-versus-fallback-success comparison.
- Followed the source comparison cluster among Same Model, Different Harness; Harness Updating Is Not Harness Benefit; HarnessCompass; Agent Optimizers; Meta-Harness; Self-Harness; and Continual Harness. The four kept source comparisons each expose a separate causal or operational boundary; the others were redundant or operated in materially different online-adaptation regimes.

## Connections Found

- [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: HarnessDev holds executor weights fixed while swapping generated harnesses, then holds a harness fixed while changing its executor model; the large performance and cost shifts in both directions show that learned behavior belongs to the deployed model-harness-runtime combination rather than to model weights alone.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: creators inspected only 0.5% to 40.2% of feedback tasks and used the dedicated trajectory interface only twice, while the strongest documented repair followed targeted diagnosis of false success reports and an end-to-end completion check. This is descriptive cross-lineage evidence for the value of diagnostic evidence, not a controlled diagnostic-richness ablation.
- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- **is-evidence-for**: rerunning an unchanged harness commit produced roughly a ±4.75 pair-score spread, and the benchmark used repeated evaluation to reduce that variation; the measured score is therefore a sample from an execution distribution, not a deterministic property of the commit.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: the mutable harness is optimised inside a fixed seed interface, development environment, evaluator, and task family, and the authors explicitly note that the fixed development environment cannot test continued self-hosted evolution. The experiment can improve choices inside that decomposition without validating the decomposition itself.
- [A proposal-selection loop requires search, evaluation, and retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: each evolution lineage materialises frozen harness versions, evaluates paired downstream tasks, selects whether to retain a revision, and ends with an operative declared version. The result is a concrete code-artifact selection loop even though its noisy feedback often chooses a held-out-suboptimal version.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- **see-also**: HarnessDev retains trajectories, benchmark results, code snapshots, and reachability evidence, then separates task correctness, runtime diagnostics, and artifact-level mechanism checks. The proposal supplies the local controlled-evaluation design for asking whether those richer traces improve judgments about changing workflows.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **compares-with**: both optimise persistent runnable harness code from execution evidence and evaluate frozen candidates, but Meta-Harness implements a trace-driven frontier search with explicit retained candidates while HarnessDev compares six general creator models starting from a weak seed and shows how rarely their evolution runs exploit trajectory diagnostics.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: AHE routes traces through dedicated debugger reports before editing a fixed-model harness, whereas HarnessDev lets general creator models inspect feedback and revise directly. Their contrast isolates a structured diagnostic stage that HarnessDev's failure analysis suggests is often missing.
- [Trace learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **is-evidence-for**: HarnessDev adds nine longitudinal evolution lineages, explicit trajectory-inspection rates, reachable-versus-dead mechanism audits, revision-call correlations, and held-out regressions to the survey's evidence about how outer loops turn traces into persistent changes.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: both maintain versioned agent artifacts under benchmark feedback, but Autogenesis makes promotion, rollback, and frozen-version recovery part of the operative mutation lifecycle. HarnessDev instead freezes externally edited harness versions and empirically shows why monotonic promotion cannot be assumed.
- [Same Model, Different Harness, Different Coding Agent Results](../../../../sources/same-model-different-harness-different-coding-agent-results.ingest.md) -- **compares-with**: the coding study estimates a fixed-model harness effect while tracking context and tool-use regimes; HarnessDev broadens that question to generated harnesses, cross-domain capability and cost, and the separate effect of transferring one harness across executor models.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: both distinguish the model that creates or edits a harness from the model that must execute it. Harness Updating tests whether a user agent loads and follows another agent's written artifact, while HarnessDev executes runnable code directly and measures creator-to-executor portability.
- [HarnessCompass: Guiding Automatic Harness Evolution](../../../../sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md) -- **compares-with**: both optimise harnesses from visible benchmark feedback and then test held-out tasks and cross-model transfer; both find that feedback gains can regress outside the optimisation setting, but HarnessDev compares general creator models and complete code harnesses rather than a dedicated evolution method.
- [Do Agent Optimizers Compound Terminal-Bench Performance?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both study sequential harness revision, retained versions, regressions, and transfer under repeated task feedback. Agent Optimizers organises a phased continual programme around one optimiser, whereas HarnessDev runs one evolution trajectory per creator-runtime cell and finds that only 2 of 9 declared final versions are held-out-optimal.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) -- rejected because HarnessDev does audit dormant and unreachable mechanisms, but it does not compare successful runs that used the intended mechanism against successful fallback runs; the paper therefore cannot establish this note's path-health contrast directly.
- [Harness sub-agent model selection regression](../../../../reference/harness-sub-agent-model-selection-regression.md) -- rejected because this is a Commonplace-specific execution-provenance incident. Its runtime-binding concern resembles HarnessDev's executor-transfer result, but the deployed-system note carries the general connection without importing incident-specific operational detail.
- [Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- rejected as an additional outbound edge because its same-model failure mining and regression gates are already reached through the more discriminating diagnostic and held-out-evolution routes above; another generic self-improvement comparison would add little traversal value.
- [Continual Harness: Online Adaptation for Foundation-Model Agents](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- rejected because it studies reset-free online adaptation with direct adoption of changes during a continuing task stream, whereas HarnessDev performs offline code revision and frozen-version evaluation. That regime difference is larger than the remaining shared vocabulary.

## Index Membership

None

## Synthesis Opportunities

- HarnessDev, [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and [Same Model, Different Harness, Different Coding Agent Results](../../../../sources/same-model-different-harness-different-coding-agent-results.ingest.md) together suggest a missing operational claim: a measured harness effect belongs to a model-harness-runtime-regime pairing, not to the harness alone. Executor compatibility, context and resource limits, and the evaluator's fixed decomposition should therefore travel with any reported harness-quality result.

## Maintenance Observations

None

## Flags

- The target is an immutable snapshot and no matching `kb/sources/harnessdev-llms-create-and-evolve-agent-harnesses.ingest.md` exists. All outbound candidates belong on that future authored ingest surface, never on the snapshot.
- This source is a split candidate for later note promotion: its creator/executor portability result, diagnostic-feedback result, and held-out evolutionary-generalisation result are independent claims and should not be collapsed into one omnibus methodology note.
- Preserve the study boundary when using its results: each creator-runtime cell has one evolution trajectory, the held-out evaluation is limited to SWE-Pro, the development environment is fixed, and the authors do not estimate population-level uncertainty across independent creation or evolution runs.
