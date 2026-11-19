---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/the-self-healing-agent-harness-2048912026018484317.md"
source_has_frontmatter: true
date: "2026-04-29"
depth: standard
---

# Connection Report: The Self-Healing Agent Harness

**Source:** [The Self-Healing Agent Harness](../../../sources/the-self-healing-agent-harness-2048912026018484317.md)

## Discovery Trace

**Collection rules:**
- Read [sources collection rules](../../../../sources/COLLECTION.md). Snapshots are immutable; the active authoring surface is the matching ingest report. Authorised ingest-report/source-review labels are `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and sparse `see-also`. Sources should scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and other `kb/sources/`; they should not link into `kb/work/` or `kb/instructions/`.
- Read [notes collection rules](../../../../notes/COLLECTION.md) for reverse edges. Notes may link to sources with `evidence` or `derived-from`.

**Index scan:**
- Read [notes index](../../../notes/dir-index.md). Flagged candidates: [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md), [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md), [Apparent success is an unreliable health signal in framework-owned tool loops](../../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md), [Automated tests for text](../../../../notes/automated-tests-for-text.md), and [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md).
- Read [reference index](../../../reference/dir-index.md). No durable reference target fits; [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) mentions behavioral evaluation and trace capture, but the source is external practice rather than a description of the shipped commonplace system.
- Read [agent-memory systems index](../../../agent-memory-systems/dir-index.md). The root [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) is adjacent, but the source is an operational QA/release harness rather than an agent memory system review.
- Read [sources index](../../../sources/dir-index.md). Strong companion sources: [Ingest: Harness Engineering: Leveraging Codex in an Agent-First World](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md), [Ingest: Harness Engineering Is Cybernetics](../../../../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md), [Ingest: The Anatomy of an Agent Harness](../../../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md), [Ingest: The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md), and [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md). Also evaluated the local snapshot [What is an Agent Harness](../../../sources/what-is-an-agent-harness-2046980769747533830.md), which exists but has no ingest report yet.

**Body search:**
- `rg -n "agent harness|Agent Harness|harness engineering|self-healing|grade|grader|evaluation|QA|quality drop|release gate|grey rollout|gray rollout|trajectory|ticket|Linear|score" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -- found the harness-ingest cluster, oracle/evaluation notes, review-system references, and memory-evaluation requirements. Kept candidates where the source adds a concrete production loop rather than merely sharing vocabulary.
- `rg -n "oracle|verification|verify|gated|gate|rollout|regression|production|live traffic|feedback loop|closed loop|triage|fix" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -- surfaced verification-boundary, spec-mining, review-gate, and trace-derived learning material. Kept oracle/spec-mining notes; rejected commonplace review-system references as shipped-system docs not directly informed by this source.
- `rg -n "outcome|trajectory|path|tool calls|transcript|human review|judge|panel|calibration|rubric" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -- surfaced outcome/effects evaluation, LLM judge calibration, and trajectory-derived learning. Kept the notes on phase-gated evaluation and decorrelated oracles; rejected generic structured-output/human-review matches.

**Link following:**
- Followed [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) to [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md). This cluster is the strongest fit: the source reports a mature production loop where live failures become rubrics, clusters, tickets, fixes, re-grading, and release gates.
- Followed harness companion ingests to [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md). The source suggests evaluation/release gating may be an additional runtime control layer, but that is a synthesis opportunity rather than a direct edit target.

## Connections Found

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **evidence**: the source describes the later-stage case where a calibrated category router, rubric, tri-judge panel, human spot checks, and production feedback let evaluation drive engineering rather than merely produce dashboards.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the bridge component makes verification explicit: new agent variants are promoted, held, or rolled back based on live grader scores and error-cluster signals.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **evidence**: the tri-judge panel deliberately uses different model families, category-conditioned rubrics, quorum handling, persisted disagreement, and periodic human calibration to make LLM judging more decorrelated and auditable.
- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) -- **evidence**: low-scoring production responses are clustered, investigated, routed into tickets, turned into code fixes, verified with telemetry, and re-graded, which is the observe -> classify -> codify -> verify loop in an operational QA setting.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**: the harness improves during production by updating prompts, code, tests, telemetry rules, and release gates rather than weights, making adaptation durable and inspectable across sessions.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- **evidence**: the described loop narrows future system behavior through durable engineering artifacts: bug tickets, PRs, blocked rollouts, regrade windows, and release thresholds.
- [Apparent success is an unreliable health signal in framework-owned tool loops](../../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) -- **evidence**: the source treats failed integrations, infra flakes, tool-contract drift, context plumbing, and deploy regressions as indistinguishable to the user and grader unless a separate triage loop works backward from the quality drop.
- [Harness Engineering: Leveraging Codex in an Agent-First World](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- **compares-with**: Lopopolo describes the constraining/informing/verifying/correcting harness for agent-written code; this source describes a product-facing analogue where live agent responses become the sensor signal for QA, fixes, and release gates.
- [Harness Engineering Is Cybernetics](../../../../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) -- **compares-with**: both frame harness engineering as feedback-loop design; this source supplies the concrete sensor/actuator loop for production agent quality.
- [The Anatomy of an Agent Harness](../../../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) -- **compares-with**: the earlier taxonomy covers loop, context, skills, subagents, hooks, and permission layers; this source adds a QA/evaluation/release-control layer that the taxonomy does not foreground.
- [The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md) -- **compares-with**: both sources argue generic self-review misses production failures; the earlier source emphasizes explicit failure probes, while this one closes the loop by turning production quality drops into tickets, fixes, and gated rollouts.
- [Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: both use rich diagnostic signals to improve harness behavior, but Meta-Harness optimizes benchmark harness code under hard oracles, while this source operates on live product traffic under soft calibrated graders.

## Bidirectional Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) <-> source -- **evidence**: the note already has the phase model; this source is a strong mature-loop example after comprehension/specification have produced a usable production grader.
- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) <-> source -- **evidence**: the source is a clean non-KB, non-Codex example of spec mining from production failures into durable fixes and release gates.

## Reverse-edge Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -> source -- **evidence**: add as a mature production case that qualifies the note's "manual comprehension first" framing with an automated-but-calibrated loop.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -> source -- **evidence**: add as practitioner evidence for cross-model judge panels plus calibration as a decorrelation strategy.
- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) -> source -- **evidence**: add as an operational example where production failures are mined into tickets, code fixes, regression checks, and rollout gates.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -> source -- **evidence**: add as a product-agent example where automation extends only because a soft-but-calibrated verifier governs releases.

## Off-authorisation Candidates

- [Agent runtimes decompose into scheduler context engine and execution substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- the source suggests evaluation/release gating may deserve explicit placement in the runtime decomposition, but this is more than a source edge: it needs synthesis across multiple harness sources rather than a direct `evidence` link alone.

## Raw Text Candidates

None

## Rejected Candidates

- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- overlaps on trace capture and behavioral evaluation, but the source does not describe the shipped commonplace system and should not be used as a reference-doc target.
- [Automated tests for text](../../../../notes/automated-tests-for-text.md) -- shares the "test pyramid from real failures" idea, but the source is about production agent QA and release gating, not text artifacts specifically.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- "grade the outcome, not the trajectory" is analogous, but the source is not about memory evaluation; a direct link would likely confuse traversal.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- adjacent pattern, but the source is not an agent memory system and should not enter the agent-memory review landscape from a snapshot ingest alone.
- [What is an Agent Harness](../../../sources/what-is-an-agent-harness-2046980769747533830.md) -- relevant as same-month harness taxonomy but currently only a raw snapshot with no ingest analysis; use later once ingested.

## Index Membership

- [Sources directory](../../../sources/dir-index.md) -- after ingest/index refresh, this source should appear near the harness-engineering and agent-evaluation cluster.

## Synthesis Opportunities

- The harness-source cluster now has four roles: anatomy (components), cybernetics (control-loop frame), Codex practice (constrain/inform/verify/correct for code generation), and this source (production QA/release gating for agent outputs). A synthesis note could argue that modern harnesses need not just scheduler/context/substrate, but also an evaluation-control loop that turns soft user-facing quality signals into engineering actions.

## Flags

- The source is a practitioner report with strong operational detail but no public data, no independent replication, and likely high survivorship/vendor-context bias.
