---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/huxley-godel-machine-human-level-coding-agent-development.md"
source_has_frontmatter: true
date: "2026-04-24"
depth: standard
---

# Connection Report: Huxley-Gödel Machine

**Source:** [Huxley-Gödel Machine](../../../sources/huxley-godel-machine-human-level-coding-agent-development.md)

## Discovery Trace

**Index scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- snapshots are immutable; active outbound links belong in the matching ingest report. Authorized labels from source analyses into notes include `evidence`, `derived-from`, `rationale`, `defined-in`, and sparing `see-also`; source-to-source / source-to-agent-memory uses `compares-with`.
- Read [notes index](../../../notes/dir-index.md) -- flagged: [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [continual learning's open problem is behaviour](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [the boundary of automation](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and [automating KB learning](../../../../notes/automating-kb-learning-is-an-open-problem.md). Kept the learning/oracle cluster because HGM is a self-improvement loop over readable symbolic artifacts under benchmark feedback; rejected generic context-engineering hits that did not speak to automated artifact mutation or evaluation.
- Read [agent-memory systems file list](../../../agent-memory-systems/dir-index.md) and focused reviews -- strongest architectural relatives are [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md), [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md), [CORAL](../../../../agent-memory-systems/reviews/CORAL.md), and the [trace-derived learning survey](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md). Kept these because they are hard-oracle outer loops or trace-derived artifact-learning systems, not just memory services.

**Topic indexes:**
- Read [learning-theory index](../../../notes/learning-theory-index.md) via search hits around the readable-artifact loop and deploy-time learning. This reinforced the coevolution/readable-artifact path rather than adding a separate candidate.

**Body search:**
- `rg -n "self-improv|self improv|recursive self|self-evolv|Gödel|Godel|metaproduct|DGM|Darwin" kb/notes kb/sources kb/agent-memory-systems --glob "*.md"` -- surfaced HyperAgents, auto-harness, ReasoningBank, the unfaithful self-evolvers source, the trajectory-informed memory ingest, and this new snapshot. Kept HyperAgents/auto-harness/source ingests; rejected generic "self-improvement" mentions in product reviews where the implementation did not actually perform self-editing search.
- `rg -n "coding agent|agent scaffold|SWE-bench|benchmark score|benchmark performance|hard oracle|evaluation score|optimization loop|harness" kb/notes kb/sources kb/agent-memory-systems --glob "*.md"` -- surfaced the hard-oracle automation cluster, Meta-Harness, Natural Language Agent Harnesses, CORAL, and agent runtime notes. Kept Meta-Harness and CORAL as nearby source/system comparisons; rejected general coding-agent component notes because HGM's novelty is search signal, not runtime decomposition.

**Link following:**
- From [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md), followed links to [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [the boundary of automation](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [trace-derived learning techniques](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md), and [automating KB learning](../../../../notes/automating-kb-learning-is-an-open-problem.md). This established the local framing: autonomous self-editing is feasible where hard benchmark oracles exist, but KB learning lacks those oracles.
- From [Meta-Harness ingest](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), followed the diagnostic-richness synthesis into [readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md). HGM belongs next to this source but adds a different axis: archive-selection objective, not diagnostic access.
- From [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) and [Unfaithful Self-Evolvers ingest](../../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md), followed to [distillation](../../../notes/definitions/distillation.md) and deploy-time learning. These are relevant as self-improvement-by-artifact-learning contrasts, but HGM optimizes code/scaffold descendants rather than extracted memories or tips.

## Connections Found

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **evidence**: HGM is a fixed-weight outer loop that mutates coding-agent scaffolds and control logic, then selects future mutation sites from evaluated descendants. It supports the note's claim that prose/symbolic artifacts are a tractable automated-learning substrate.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **evidence**: HGM discovers durable agent implementations during deployment-like search without weight updates; the learned capacity lives in code/prompt artifacts that can be versioned and reused.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **evidence**: HGM explicitly stays at the symbolic/prose layer while leaving model weights fixed, and frames weight-level self-modification as future work. This is a clean data point for separating artifact-class loops.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: HGM's autonomy depends on SWE-bench, Polyglot, and SWE-bench-Live-style benchmark oracles. The method is impressive precisely in a resettable, rewardable coding benchmark regime.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: HGM adds nuance to hard-oracle loops: even with benchmark scores available, immediate score is a misleading proxy for long-term self-improvement potential. Oracle availability is necessary but not sufficient; the selection metric must match the optimization target.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**: HGM changes future behavior by rewriting the system-definition artifacts of a coding agent, not by accumulating facts for lookup.

## Bidirectional Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) <-> source -- **evidence**: HGM is a strong example for the note, but the source also complicates the note by showing that a cheap benchmark oracle can still be the wrong greedy objective for multi-generation improvement.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) <-> source -- **evidence**: HGM can serve as a concrete successor example to Meta-Harness: both mutate readable artifacts, but HGM studies archive policy and lineage-level selection rather than diagnostic context.

## Reverse-edge Candidates

- [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md) -> source -- **compares-with**: HGM is directly comparable to HyperAgents' benchmark-scored self-editing archive, but replaces greedy/scored parent selection with clade-metaproductivity estimation.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) -> source -- **compares-with**: auto-harness uses a narrow one-file hard-oracle loop; HGM is the broader research version where the archive policy itself is the contribution.
- [CORAL](../../../../agent-memory-systems/reviews/CORAL.md) -> source -- **compares-with**: CORAL's multi-agent hard-oracle search accumulates attempt history; HGM provides a lineage-level selection metric that could inform how such systems choose which branches to expand.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -> source -- **compares-with**: HGM should join the survey as a code-lineage / archive-selection case: promotion target is symbolic agent implementation, source signal is benchmarked descendant performance, and reinjection is branch expansion.
- [Meta-Harness ingest](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -> source -- **compares-with**: both are 2026 harness-optimization papers; Meta-Harness varies diagnostic access while HGM varies archive-selection signal.
- [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -> source -- **compares-with**: both learn from prior agent execution under task oracles, but one distills tips into prompt-visible prose while HGM evolves agent code/scaffold lineages.

## Off-authorisation Candidates

- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- HGM modifies coding-agent scaffolds, but the connection is too broad unless a future note needs examples of scheduler/policy search. Reject as off-scope for this ingest.

## Raw Text Candidates

None

## Rejected Candidates

- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -- rejected as a direct connection: it already cites trajectory and faithfulness sources, but HGM is not primarily about memory creation, activation, or storage.
- [Natural Language Agent Harnesses ingest](../../../../sources/natural-language-agent-harnesses.ingest.md) -- rejected as a strong connection: both involve SWE-bench and harnesses, but NLAH studies natural-language harness structure and ablations, while HGM studies self-improvement archive policy.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers ingest](../../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) -- rejected as outbound connection: it is an adjacent empirical caution about memory faithfulness, but HGM's core artifact is code/scaffold evolution rather than condensed memory use.

## Index Membership

- [learning-theory index](../../../notes/learning-theory-index.md) -- HGM is evidence for readable-artifact continual learning and fixed-weight deploy-time behavior change.
- [sources index](../../../sources/dir-index.md) -- generated source index should include the new snapshot and ingest report after refresh.
- [trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- future survey update could add HGM as a code-lineage self-improvement case, although it is a paper snapshot rather than repo-inspected system coverage.

## Synthesis Opportunities

HGM plus Meta-Harness suggests a two-axis view of automated harness search: **diagnostic access quality** (scores only -> summaries -> raw traces) and **archive-selection objective** (immediate score -> lineage-level metaproductivity). Existing KB notes discuss diagnostic richness and oracle strength, but not the archive-objective axis. A future note could argue that outer-loop search quality depends on at least three separable things: oracle strength, diagnostic richness, and selection-target alignment.

## Flags

- HGM's headline claims include future-dated model/benchmark references from a 2026 ICLR paper. Treat leaderboard and "human-level" claims as benchmark-local and potentially unstable; the durable KB value is the metaproductivity-performance mismatch and lineage-level selection metric.
