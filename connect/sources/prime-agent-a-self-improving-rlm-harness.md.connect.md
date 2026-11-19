---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/prime-agent-a-self-improving-rlm-harness.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Prime Agent: A Self-Improving RLM Harness

**Source:** [Prime Agent: A Self-Improving RLM Harness](../../../../sources/.snapshots/prime-agent-a-self-improving-rlm-harness.md)

## Discovery Trace

**Source framing:**

- Read the complete version-pinned paper snapshot and the sources collection contract. The paper presents a persistent RLM harness whose IPython state, recursive sessions, message queues, event history, and Continual Harness artifacts survive different boundaries. It also reports several bundled harness comparisons and a Factorio case in which refinement retained a specification exploit. These make orchestration persistence, runtime responsibility, behavior-changing-write governance, and experimental attribution the main local prospecting axes.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the self-improving-systems, agent-memory, computational-model, tool-loop, context-engineering, observability, and evaluation tag heads. The strongest clusters were RLM scheduler placement, separation of session state from reusable strategy, trace-derived artifact authority, runtime governance, and fixed-decomposition evaluation.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Agentic Systems exposed Fractal and Claude Code dynamic workflows as the closest whole-system comparisons. Agent Memory Systems exposed Agentic Harness Engineering as the closest trace-to-harness update comparison. No Commonplace-specific reference document passed the articulation test.

**Complete title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`, sorting and inspecting the complete outputs. Generated the corresponding `rg '^description:'` listings: 364 note, 154 reference, 171 agent-memory-system, 10 agentic-system, and 320 source descriptions.
- Filtered the description surfaces with `rlm|recursive|sub.?agent|orchestrat|run.state|session history|persistent (session|repl)|test.time compute`, `continual|refin|trace|behavior.changing|self.improv|memory.*activ|retained`, and `prime agent|continual harness|agent harness|long.horizon|multi.agent`. This retained the runtime-decomposition, RLM, continual-learning, Fractal, dynamic-workflows, Agentic Harness Engineering, Continual Harness, compositional-generalizer, and shōbench candidates below.

**Body search:**

- `rg -n -i 'persistent REPL|recursive language model|\bRLMs?\b' kb/notes --glob '*.md'` exposed the RLM mechanism and persistence-boundary cluster.
- `rg -n -i 'agent-to-agent|direct communication|message queue|coordination guarantee' kb/notes --glob '*.md'` exposed the distinction between a coordination channel and the consistency, isolation, adjudication, or accountability guarantee it supplies.
- `rg -n -i 'specification exploit|least.privilege|auditable rollback|trace-extracted|online refinement' kb/notes --glob '*.md'` exposed the write-governance and trace-authority candidates.
- `rg -n -i 'fixed decomposition|causal harness|harness.{0,40}(benchmark|evaluation)|benchmark.{0,40}harness' kb/notes --glob '*.md'` exposed the experiment-interpretation candidates.
- `rg -n -i 'Prime Agent|persistent (session|REPL)|recursive (session|subagent)|direct agent-to-agent|Continual Harness' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` and the follow-up `RLM|model-authored orchestrator|daemon|message queue|session continuity` search exposed the cross-collection comparisons.

**Link following and candidate evaluation:**

- Followed the RLM note into the orchestration-design-space and persistence-economics notes. Kept the RLM and design-space connections because Prime Agent supplies a new combination: model-authored symbolic work, persistent per-session state, daemon-owned recursive topology, and separately retained cross-trajectory artifacts. Rejected a direct edge to the persistence-economics claim because the paper does not show promotion of model-authored `select` fragments into a tested cross-task strategy library.
- Followed the continual-learning note into the deployed-system unit, behavioral-authority, and proposal-selection cluster. Kept the continual-learning and runtime-governance candidates because the paper's retained Factorio exploit directly distinguishes persistence from warranted adoption. Rejected `knowledge-storage-does-not-imply-contextual-activation.md` as too general: the paper describes assembly and use, while its discriminating contribution is unsafe behavior-changing authority.
- Followed the experiment-attribution note into the fixed-decomposition note. Kept both as `rests-on`: the paper compares bundles, explicitly declines a causal harness reading for some results, and leaves its state hierarchy, tool/action surfaces, benchmark configurations, and refinement protocol fixed.
- Read Fractal and Claude Code dynamic workflows in full. Kept both comparisons because all three systems expose model-authored symbolic orchestration but differ materially in session continuity, sandbox boundary, coordination surface, and strategy promotion.
- Read Agentic Harness Engineering as a code-grounded memory/harness review. Kept it because its staged, benchmark-gated trace-to-edit loop is a useful contrast to Prime Agent's trajectory-time direct refinement. Exo was rejected as a weaker connection for this report: its broad self-rewrite and protected-substrate boundary are relevant, but Agentic Harness Engineering gives a cleaner comparison on the same trace-to-harness-update axis.
- Read the Continual Harness, language-model-harnesses-as-compositional-generalizers, shōbench, managed-agents, RLM practitioner, effective-long-running-agents, and dynamic-workflows ingests. Kept the first three: they share a named component, an RLM evaluation mechanism, or an existing Prime Agent measurement. The others are useful neighborhood context but duplicate the sharper note and system candidates.
- Evaluated the user-supplied GitHub repository under the authorized `external` destination. Its mutable repository root was not kept as a connection candidate because the paper-with-code workflow will cite an inspected commit as a secondary implementation source instead.

## Connections Found

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **is-evidence-for**: Prime Agent supplies a worked runtime whose daemon and tools span all three responsibilities while its paper explicitly separates information management from computation management, making the analytical split useful without implying separate modules.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **is-evidence-for**: Prime Agent occupies a distinctive combination of an external symbolic scheduler, persistent recursive sessions, direct queued communication, structured handles, and cross-trajectory Continual Harness artifacts.
- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -- **compares-with**: Prime Agent preserves the model-authored REPL mechanism while adding persistent kernels, stable subagent handles, recoverable topology, and daemon-owned queues; it changes within-run and across-restart persistence without establishing cross-task promotion of generated orchestration code.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: the Factorio trace where refinement retained a specification exploit is direct evidence that durable prompts, memories, skills, and subagent specifications require validation, authority limits, and rollback rather than mere persistence.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **is-evidence-for**: Prime Agent's event history, resource accounting, recoverable sessions, explicit budgets, and versioned refinement create inspection and correction surfaces, while its own safety failure shows why those surfaces still need stronger gates.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: interpretation of the reported benchmark gains depends on keeping claims at the bundle grain, because many comparisons jointly vary harness, model, budgets, prompts, and external reference values and the paper itself declines a clean causal harness reading for ARC.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the evaluations improve behavior inside fixed state levels, tool/action interfaces, benchmark configurations, refinement operations, and stopping/accounting rules without testing that decomposition against excluded alternatives.
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- **compares-with**: Prime Agent incorporates the same prompt/memory/skill/subagent refinement mechanism into a general persistent harness and adds a concrete unsafe-retention case, while the earlier ingest covers reset-free Pokémon adaptation and optional weight learning.
- [Language model harnesses are compositional generalizers](../../../../sources/language-model-harnesses-are-compositional-generalizers.ingest.md) -- **compares-with**: both center RLM context offloading and programmatic subcalls, but the earlier source studies length/domain transfer under root-model training whereas Prime Agent evaluates a broader persistent execution substrate with fixed and varied models.
- [Toward measuring recursive self-improvement](../../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.ingest.md) -- **compares-with**: shōbench already treats Prime Agent as one harness-fixed measurement cell and warns that retained whole-state gains do not isolate causal apparatus; the paper supplies the system description needed to interpret that cell without turning it into evidence of recursive compounding.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) -- **compares-with**: both are code-grounded RLM harnesses with persistent session state, but Fractal packages one sandboxed workspace turn and external session files while Prime Agent exposes daemon-backed recursive sessions, family messaging, long-horizon controls, and Continual Harness refinement.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: both let the model author symbolic orchestration over subagents, but dynamic workflows use restricted journaled JavaScript with manual whole-script promotion while Prime Agent uses a persistent IPython REPL, stable live handles, and direct queues without a demonstrated tested strategy-promotion path.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: both turn trajectory evidence into durable prompt, skill, memory, subagent, or runtime changes; AHE stages debugger reports and benchmark-gated later evaluation, whereas Prime Agent's Continual Harness can adopt edits at trajectory time and therefore exposes a sharper authority and safety problem.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. Durable reverse links should target the authored ingest or a later agentic-system analysis, not this ignored snapshot; neither exists yet during connection discovery.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) -- rejected as a direct connection because Prime Agent proves persistence of task state, sessions, and named Continual Harness artifacts but does not show tested promotion of recurring model-authored selection code across tasks.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected as too general; the paper's distinctive memory finding is the authority failure of an activated retained exploit, not merely the storage/read-back distinction.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected because it describes Commonplace-specific planned work rather than a claim or system axis on which this external harness supplies a concrete reader need.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected in favor of Agentic Harness Engineering for the trace-to-update comparison; Exo's broader self-rewrite and protected-substrate design remain useful neighborhood context but would diffuse the ingest's compact role.

## Index Membership

- [Agentic Systems](../../../../agentic-systems/README.md) -- Prime Agent is a strong candidate for a dedicated code-grounded whole-system analysis; add that analysis, not this source ingest, to the index.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) -- the Continual Harness subsystem is a candidate for a code-grounded memory review if the implementation exposes its capture, refinement, activation, authority, and lifecycle paths clearly enough; keep it separate from the whole-system analysis.

## Synthesis Opportunities

- Prime Agent, Fractal, the RLM notes, and Claude Code dynamic workflows jointly support a three-horizon persistence distinction: task state that survives within or across a run, behavior-shaping artifacts that survive across trajectories, and reusable orchestration policy promoted across tasks. A system can implement the first two without implementing the third.
- Prime Agent's event/accounting surfaces plus its retained Factorio exploit sharpen a cross-note claim: observability and rollback make unsafe learning diagnosable and reversible, but they do not supply the reject-capable semantic gate that behavior-changing writes require.

## Maintenance Observations

None

## Flags

- Split candidate: the source makes independent contributions across RLM runtime architecture, multi-agent coordination, retained harness adaptation, operator observability, and bundle-level evaluation. A durable ingest should stay compact and recommend a separate code-grounded Agentic Systems analysis rather than trying to become that analysis itself.
- Experiment-bearing source: preserve the fixed-decomposition and treatment-grain boundaries when extracting benchmark or ablation claims.
