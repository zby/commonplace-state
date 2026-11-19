---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/agent-workflow-memory.md"
source_has_frontmatter: true
date: "2026-05-08"
depth: standard
---

# Connection Report: Agent Workflow Memory

**Source:** [Agent Workflow Memory](../../../sources/agent-workflow-memory.md)

## Discovery Trace

**Source and rules:**
- Read [source snapshot](../../../sources/agent-workflow-memory.md): arXiv paper introducing Agent Workflow Memory (AWM), a method that induces reusable web-agent workflows from annotated or successful trajectories and injects them into future web-navigation contexts; evaluated on WebArena and Mind2Web.
- Read [sources collection rules](../../../../sources/COLLECTION.md): snapshots are immutable; authored links belong in the ingest report or future source review. Authorised labels for source analysis include `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and sparse `see-also`. Do not link into `kb/work/` or `kb/instructions/`.

**Index scan:**
- Read [sources index](../../../sources/dir-index.md) -- flagged adjacent source/ingest candidates: [Memory Intelligence Agent](../../../../sources/memory-intelligence-agent.ingest.md) for workflow memory plus test-time planner learning; [Trajectory-Informed Memory Generation](../../../sources/trajectory-informed-memory-generation-self-improving-agents.md) for trajectory-to-tip learning; [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md) for raw-vs-condensed experience utilization.
- Read [agent-memory systems README](../../../../agent-memory-systems/README.md) and [agent-memory systems dir-index](../../../agent-memory-systems/dir-index.md) -- found direct prior coverage: [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md), [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md), [SkillX](../../../../agent-memory-systems/reviews/SkillX.md), [SkillWeaver](../../../../agent-memory-systems/reviews/SkillWeaver.md), [Voyager](../../../../agent-memory-systems/reviews/voyager.md), and [OS-Copilot](../../../../agent-memory-systems/reviews/OS-Copilot.md).
- Read [notes dir-index](../../../notes/dir-index.md) -- flagged candidate notes: [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [Distillation is transformation, not selection](../../../notes/distillation-is-transformation-not-selection.md), [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md), [Claw learning loops must improve action capacity not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md), [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), and [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md).

**Body search:**
- `rg -n "workflow|workflows|agent memory|trajectory|sub-routine|skill|skills|online|offline|generalization|experience" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md" --glob "!kb/sources/agent-workflow-memory.md"` -- confirmed the AWM neighborhood is already present in source reviews and trace-derived learning notes. Kept candidates where AWM adds evidence about trajectory-to-procedure learning or the benchmark-oracle boundary; rejected generic skill/harness hits without an AWM-specific mechanism.
- `rg -n "Agent Workflow Memory|trajectory-to-workflow|workflow memory|AWM" kb/notes kb/agent-memory-systems kb/sources --glob "*.md" --glob "!kb/sources/agent-workflow-memory.md"` -- found direct prior coverage in [Agent Workflow Memory review](../../../../agent-memory-systems/reviews/agent-workflow-memory.md), [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md), [ReasoningBank review](../../../../agent-memory-systems/reviews/reasoning-bank.md), and [Memory Intelligence Agent ingest](../../../../sources/memory-intelligence-agent.ingest.md).

**Link following:**
- Followed [Agent Workflow Memory review](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) relevant notes: [distillation](../../../notes/definitions/distillation.md), [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [automating KB learning](../../../../notes/automating-kb-learning-is-an-open-problem.md), and the files-not-database thread. The review already carries the code-grounded system analysis; this paper snapshot should not duplicate it, but can serve as the canonical source/ingest for the paper's empirical claims.
- Followed [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- AWM is already catalogued as a trajectory-run, readable-artifact learner whose maintenance path is workflow-file replacement. This source can strengthen that survey with paper-level claims about abstract subroutines, small-data learning, and online/offline comparison.
- Followed [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) and [Claw learning loops must improve action capacity not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- AWM is a concrete positive case for action-capacity learning under tight oracles, but the same tight-oracle condition limits transfer to open-ended KB learning.

## Connections Found

- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) -- **compares-with**: the local review is the code-grounded system analysis; the paper snapshot is the authored scientific source with reported WebArena/Mind2Web results, ablations, and workflow-representation claims.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- **evidence**: AWM is a clean trajectory-run learner where successful or annotated web-task traces become reusable prompt workflows, giving the survey a benchmarked example of readable artifact learning.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**: online AWM updates durable workflow artifacts between test tasks without changing weights, matching the deploy-time timing/substrate pattern.
- [Distillation is transformation, not selection](../../../notes/distillation-is-transformation-not-selection.md) -- **evidence**: AWM turns concrete action trajectories into abstract subroutines with variables, which is a shape change rather than a shorter trace.
- [Claw learning loops must improve action capacity not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- **evidence**: AWM evaluates memory by future web-agent action success, not by recall or question answering, making it a concrete action-capacity memory loop.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- **evidence**: AWM shows extraction and reuse can be automated when task boundaries and evaluators exist; it also sharpens why KB learning remains harder without comparable oracles.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **evidence**: AWM keeps the learned behavior in readable prompt workflows and optional action syntax, showing a non-weight artifact loop with measurable effects.

## Bidirectional Candidates

- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) <-> source -- **compares-with**: the review should remain the code-grounded local analysis, while the ingest can point readers back to the review for implementation/lifecycle caveats.

## Reverse-edge Candidates

- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -> source -- **evidence**: cite the paper snapshot or ingest where the survey states AWM writes website-scoped workflow prompt files and uses workflow-file replacement as its maintenance path.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -> source -- **evidence**: cite AWM as a paper-level example of deployment-timed artifact update under a benchmark oracle.
- [Distillation is transformation, not selection](../../../notes/distillation-is-transformation-not-selection.md) -> source -- **evidence**: cite AWM as trajectory-to-workflow shape change, especially the abstraction of example-specific values into variables.
- [Claw learning loops must improve action capacity not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -> source -- **evidence**: cite AWM as evidence that procedure/workflow memories can be evaluated by action success.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -> source -- **evidence**: cite AWM as a positive case on the easy-oracle side of the automation boundary.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- rejected as too local to the commonplace skill packaging model; AWM workflows are prompt payloads, not user-invocable skills with tool policy.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) -- plausible but broad; the direct contribution is better captured through action-capacity memory and the AWM review's lifecycle caveat.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) -- relevant as a baseline/comparison implementation, but the direct link belongs more naturally in the trace-derived learning survey or future synthesis than in this ingest.
- [Memory Intelligence Agent](../../../../sources/memory-intelligence-agent.ingest.md) -- sibling workflow-memory paper, but the connection is comparative rather than needed for understanding this source; keep as synthesis material unless writing a cross-system note.

## Index Membership

- [agent-memory systems README](../../../../agent-memory-systems/README.md) -- already has AWM review coverage; no new index entry needed unless the source snapshot should be linked from the review.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- could add the paper ingest as a source citation beside the code-inspected review where AWM's empirical claims matter.
- [Learning theory index](../../../notes/learning-theory-index.md) -- possible future source citation under deploy-time / trace-derived artifact learning, but not urgent because the AWM review already anchors the topic.

## Synthesis Opportunities

AWM, Trajectory-Informed Memory Generation, ReasoningBank, ExpeL, SkillX, SkillWeaver, Voyager, and OS-Copilot together suggest a higher-order note: "Trace-to-procedure learning works when task boundaries, success oracles, and reusable subgoals coincide." The source adds two important details: abstract subroutines can outperform concrete examples, and online induction can beat offline workflows as train-test domain gaps widen.

## Flags

- The KB already has a code-grounded AWM review. The ingest should not restate implementation findings as if newly discovered from the paper; its new value is the paper's empirical/ablation evidence and the authors' framing around abstract subroutines, online/offline induction, and workflow representation.
