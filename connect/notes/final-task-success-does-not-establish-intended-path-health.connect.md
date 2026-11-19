---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/final-task-success-does-not-establish-intended-path-health.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Final task success does not establish intended-path health

**Source:** [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md)

## Discovery Trace

No semantic-search service or open-web search was used. Candidate judgments came from repo-local curated heads, complete title and description surfaces, source-tag listings, focused body searches, exact and conceptual reverse-edge searches, and one-hop link following. No search surface supplied scores.

**Curated heads:**

- Read `kb/notes/README.md` and all six matching source-tag heads: `computational-model-README.md`, `kb-maintenance-README.md`, `learning-theory-README.md`, `observability-README.md`, `tool-loop-README.md`, and `deploy-time-learning-README.md`. None declares `complete: true`, so no by-tag search was skipped; `learning-theory-README.md` uses `covered_by` only.
- Read every authorised destination head: `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The destination collection contracts were also read to judge inbound labels.

**Complete title, description, and tag surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` over each of the seven authorised local destinations: `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- For each source tag in each destination, ran `rg -l '^tags:.*\bTAG\b' kb/<destination>/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` for `computational-model`, `kb-maintenance`, `learning-theory`, `observability`, `tool-loop`, and `deploy-time-learning`. The `xargs -r` guard preserved zero-match destinations rather than widening them to the repository.

**Focused body searches:**

- Across every authorised destination, ran `rg -n -i 'fallback|workaround|route around|rerout|re-rout|recovery'`, `rg -n -i 'path deviation|primary path|intended path|execution path|trajectory'`, `rg -n -i 'final (task )?success|final outcome|outcome alone|task outcome|output-only|successful runs'`, `rg -n -i 'degraded execution|weaker guarantees|guarantee degradation|provenance|fidelity'`, `rg -n -i 'broken helper|broken tool|missing binary|bad path|credential failure|hidden failure|silent failure'`, and `rg -n -i 'observability|telemetry|durable events|tool-attempt|execution signal'`, all scoped with `--glob '*.md'`.
- Ran the narrower cross-collection inventory `rg -l -i 'path deviation|primary path|intended path|degraded execution|guarantee degradation|weaker guarantees|broken helper|successful recovery|outcome-only|final success|final outcome|execution signal|tool-attempt'` to re-check vocabulary-matched artifacts without relying on tag membership.

**Per-destination evaluations:**

- `kb/notes/`: the source already encodes the tight outcome/process, soft-failure, diagnostic-richness, semantic-fallback, and recovery neighborhood, so those existing edges were not re-proposed. [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) was kept because it generalizes the source's hidden-loop condition into a governance-surface consequence. [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) was kept because tool dispatch and result return are the exact crossings where durable attempt events can be captured. [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) was kept as the architectural response that exposes application control and dispatch-side observation hooks; it already links back to the source. The theory/methodology fallback note was rejected because its fallback is a recognised, expected coverage route rather than evidence that an intended execution path broke. The reasoning-production note was rejected because the already-linked checked-outcome note states the result/process distinction more generally and directly.
- `kb/types/`: the complete surfaces and focused searches produced no global type contract that clarifies a term or bears on the runtime-health inference. No candidate passed the articulation test.
- `kb/reference/`: [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) was kept because it turns the source's detection problem into a controlled output-only versus trajectory-aware comparison. Review telemetry and freshness documents were rejected because their telemetry concerns execution provenance or cost accounting, not alternate-path health.
- `kb/agent-memory-systems/`: HALO, Agentic Harness Engineering, the trace-learning survey, and Trajectory-Informed Memory Generation were evaluated. HALO and Agentic Harness Engineering are already reached through the source's diagnostic-richness edge; another direct link would duplicate that path. Trajectory-Informed Memory Generation classifies inefficient-but-successful trajectories but does not establish hidden infrastructure failure, so it was rejected.
- `kb/agentic-systems/`: [Eigenius](../../../../agentic-systems/reviews/eigenius.md) was kept as a concrete fixed-recovery case: startup recovery can mark a task complete without the normal output-and-trace commit path or `result_layer_head`, so terminal completion and intended-path provenance come apart. Agno AgentOS was rejected because it provides rich trace and checkpoint surfaces but does not itself document the source's same-terminal-state ambiguity. Exo and Claude Code dynamic workflows expose adjacent recovery or loop-control concerns without a comparably precise path-health case.
- `kb/sources/`: immutable snapshots were judged through their authored ingest companions. The already-linked [Self-Healing Agent Harness ingest](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) remains the most precise source-side corroboration because it separates final-outcome grading from trajectory monitoring. The agent-harness survey and trajectory-informed-memory ingest were rejected as broader or less direct, and no new source candidate improved on the existing edge.
- `kb/instructions/`: no procedure adds ordering, defaults, or stopping conditions for path-deviation reporting, guarantee comparison, or asynchronous event sweeps. Because `operationalized-from` requires those procedural choices, no instruction candidate was kept.
- `external`: authorised for already-known targets only. No unlinked external target was supplied or present in loaded context, so external prospecting was skipped.

**Reverse-edge search:**

- Ran `rg -n 'apparent-success-is-an-unreliable-health-signal-in-framework-owned|Final task success does not establish intended-path health|Apparent success is an unreliable health signal'` across every authorised local destination. It found existing curated-head entries and inbound links from the optional-tool-loop, goal-holding-interpreter, structured-recovery, silent-disambiguation, and Self-Healing Agent Harness artifacts; encoded edges were not re-listed as new candidates.
- Conceptual reverse searches used the same focused query strings above and the outbound contracts of `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`. The trajectory-aware proposal can author `rests-on`, Eigenius can author rare `is-evidence-for`, and the Commonplace agent-memory gap plan can author `rests-on`; no other reverse candidate passed its source collection's reader-need test.

**Link following:**

- Followed the optional-tool-loop candidate through the bounded-context orchestration model, LLM-mediated scheduler, session-history, host-language scheduler, harness survey, and Claude Code dynamic-workflow neighborhood. Those links explain the architectural cluster, but only the optional-loop note gives this source's reader the direct design response.
- Followed the runtime-governance candidate through agent-runtime decomposition, methodology enforcement, inspectable artifacts, and review architecture. The source already links the decomposition and enforcement neighbors; the governance note adds the distinct claim that hidden structure limits when governance can act.
- Followed the trajectory-aware proposal through reasoning-production, checked-outcome, the harness-survey ingest, and the review-batch procedure. The checked-outcome note is already linked; the others are either proposal evidence or implementation context rather than additional source connections.
- Followed Eigenius through its task storage, startup-recovery, trace-authority, and cache-visibility neighborhood. The startup-recovery path supplied the unique case; the authority and cache notes concern different guarantees and were not retained.
- Followed HALO and the trace-learning survey to confirm that their trace-preservation contribution is already reachable through diagnostic richness, avoiding a redundant direct edge.

## Connections Found

- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) — **extends**: generalizes the source's framework-owned-loop condition into the broader rule that hidden scheduling and execution structure constrain whether governance can inspect a decision or only react after the final output.
- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) — **enables**: identifies the tool-dispatch and result-return crossings where the source's durable attempt, path-deviation, and guarantee evidence can be captured before a fallback collapses into terminal success.
- [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) — **extends**: develops an architectural response to the source's diagnosis by exposing the bounded call for application-owned progression while retaining dispatch hooks for observability; the target already links back to the source as a consequence.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: turns the source's non-identifiability claim into a controlled comparison between output-only and trajectory-aware workflow judgments, including successful-looking artifacts that conceal failed tool calls or invalid recovery.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — **evidenced-by**: its startup-recovery path can mark a task complete without the normal output-and-trace commit or populated result layer, a code-grounded case where terminal completion does not certify the intended path or its provenance guarantees.

## Bidirectional Candidates

- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → source — **rests-on**: the proposed output-only versus trace-aware contrast depends on the source's premise that final completion cannot distinguish intended-path health from successful recovery.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) → source — **is-evidence-for**: its code-grounded startup-recovery behavior is a concrete system case bearing materially on the source's claim that terminal success and path health can diverge.

## Reverse-edge Candidates

- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) → source — **rests-on**: the plan's trace-capture and candidate-extraction steps explicitly target silent failures, fallback paths, and weakened guarantees, whose value depends on the source's argument that successful completion does not expose those facts.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — rejected because it concerns evaluator route reconstruction, while the source already links the more general checked-outcome distinction between accepted results and their producing processes.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — rejected because its fallback is expected handling after a recognised coverage miss, not a broken intended path hidden by a common terminal state.
- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) — rejected because its inefficient-but-successful category shows the value of trajectory analysis but does not establish masked infrastructure failure or guarantee degradation.
- [HALO](../../../../agent-memory-systems/reviews/halo.md) — rejected as a redundant direct edge because its bounded trace-analysis pattern is already reached through the source's authored link to diagnostic richness.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — rejected because its rich traces, checkpoints, and durable runs improve observability but do not themselves document intended-path and fallback success collapsing into one terminal health signal.
- [Agent Harness for Large Language Model Agents ingest](../../../../sources/agent-harness-large-language-model-agents-survey.ingest.md) — rejected because it supplies general trajectory-evaluation context already carried by the trajectory-aware proposal and does not sharpen the source's conditional inference.

## Index Membership

None. The source is already listed in the `kb-maintenance`, `observability`, `tool-loop`, and `deploy-time-learning` curated heads; `computational-model` routes through the tool-loop head, and `learning-theory` routes through its validator-backed `deploy-time-learning` child.

## Synthesis Opportunities

None. The candidate cluster supplies mechanism, instrumentation, design response, evaluation, and a concrete case for the source's existing claim rather than implying a higher-order claim not yet captured.

## Maintenance Observations

- The source H1 is now “Final task success does not establish intended-path health,” while its filename and four curated-head entries still use the former “apparent success” title. All links resolve, but a later navigation-maintenance pass should decide whether to align the display titles and path.
- `observability-README.md` says that `designing-agent-memory-systems.md` turns hidden fallback paths and degraded execution into memory-extraction targets, but the current note body does not make that claim. The curated context phrase should be refreshed or the intended bridge restored.

## Flags

None.
