---
description: "Discovery report for connections between ScienceFlow and Commonplace notes on recoverable work state, bounded context, orchestration, and fixed decompositions"
type: kb/cache/types/connect-report.md
source: "kb/sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection report: ScienceFlow

**Source:** [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](../../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.md)

## Discovery Trace

- Read the source collection contract and the report type contract before searching. The source collection authorizes links to notes, references, agent-memory-system reviews, agentic-system reviews, and other sources.
- Scanned every Markdown title under `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` with `rg -N --no-heading -m1 '^# ' ...`.
- Read the curated entry points for notes, reference documentation, agent-memory systems, and agentic systems.
- Searched titles and descriptions for `long-horizon`, `workspace`, `checkpoint`, `restore`, `re-anchor`, `trajectory`, `state`, `resource`, `execution`, `research`, `memory`, `archive`, `evidence`, `evaluation`, `retention`, `selection`, and `feedback`.
- Searched bodies for recoverable or executable workspaces, checkpointing, archived-state restoration, trajectory branching, evidence-aware resource allocation, stage gates, validation signals, and context folding.
- Followed authored links from the strongest candidates into adjacent notes on workshop state, bounded context, evidence retention, verification, oracle strength, and automation boundaries.
- Applied the fixed-decomposition experiment lens because ScienceFlow reports learned or model-selected actions inside a designed state, action, evaluator, and orchestration structure.
- Evaluated each destination separately. The strongest matches were theoretical notes, two prior source ingests, and the Exo agentic-system review. No shipped-system reference target or agent-memory-system review was a close enough fit.

## Connections Found

- **rests-on:** [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — ScienceFlow optimizes tool actions and re-anchoring decisions inside fixed task adapters, evaluators, checkpoint triggers, memory operations, worker topology, and a two-axis ESTRA action vocabulary. Its ablations test selected mechanisms, not the surrounding decomposition.
- **is-evidence-for:** [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — the system represents live research state as an executable workspace plus structured memory, validation evidence, and resource records, then restores that compound state rather than reconstructing it from chat alone.
- **is-evidence-for:** [Preserve evidence without loading history](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — raw Stage records and content-addressed workspace objects remain available while folding and anchor selection determine the bounded view presented to the model.
- **is-evidence-for:** [Agent runtimes decompose into scheduler, context engine, and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — ESTRA and stage transitions schedule work, memory assembly constructs bounded context, and workspace tools, snapshots, and resource control form the execution substrate.
- **is-evidence-for:** [A proposal-selection loop requires search, evaluation, and retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — workers generate candidates, the Gate can reject them, and accepted Stages become retained anchors. This is a concrete loop implementation, though the paper does not validate every fixed design choice in that loop.
- **compares-with:** [ACM: Agentic Context Management for Long-Horizon Tasks](../../../../sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md) — both externalize detailed history behind a bounded context. ACM focuses on within-episode archive/query operations; ScienceFlow binds bounded memory to exact executable-state restoration and resource records.
- **compares-with:** [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) — the harness advice uses progress files and version control for continuity, while ScienceFlow formalizes continuity as validated checkpoints over workspace, evidence, memory, and resources.
- **compares-with:** [Exo](../../../../agentic-systems/reviews/exo.md) — both restore mutable workspace state while preserving a record outside the restored state. Exo keeps an event log around self-modification rewinds; ScienceFlow keeps archived evidence and cumulative resource accounting around research-state restoration.

## Bidirectional Candidates

None. The source snapshot is immutable, and no editable artifact already contains an authorized forward edge that should be paired in the same change.

## Reverse-edge Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) could cite the ScienceFlow ingest as a worked example of strong results and narrow ablations inside a larger untested decomposition.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) could cite ScienceFlow as an implemented compound work-state design.
- [Preserve evidence without loading history](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) could cite its raw-ledger plus bounded-fold design.
- [Agent runtimes decompose into scheduler, context engine, and execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) could cite ScienceFlow as a full-system instance of the decomposition.
- [A proposal-selection loop requires search, evaluation, and retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) could cite its Gate and accepted-Stage archive as an implemented selection loop.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) is a broad runtime analogue, but Exo supplies the sharper recovery-boundary comparison.
- [Orchestration strategies and run state have opposite persistence](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) is adjacent, but ScienceFlow does not show cross-task promotion of selected strategies into durable orchestration policy.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) is plausible because ScienceFlow stores structured evidence, but its experiments do not isolate diagnostic richness.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) is related to context folding, but ScienceFlow does not evaluate learning the folding policy itself.
- [Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) varies the harness across tasks; ScienceFlow holds the harness largely fixed and varies task artifacts within it. The fixed-decomposition note captures this contrast more directly.
- No `kb/reference/` target was retained because ScienceFlow is external-system evidence rather than documentation of the shipped Commonplace system.

## Index Membership

None. A future whole-system analysis could be added to the agentic-systems index, but a source ingest does not itself belong there.

## Synthesis Opportunities

None. The strongest cross-system point—restore mutable state without rewinding the evidence record—is already explicit in the Exo comparison and does not yet justify a separate note.

## Maintenance Observations

None.

## Flags

- An official implementation is available and supports a future code-grounded whole-system analysis.
- The paper is an experiment-bearing preprint; interpret its gains within the fixed task, evaluator, action, memory, and worker decomposition.
- Static code availability is not reproduction. The repository contains implementation, tests, configurations, and task packages, but no inspected paper-run artifact bundle that independently establishes the reported results.
