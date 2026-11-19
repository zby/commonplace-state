---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/towards-a-science-of-scaling-agent-systems.md"
source_has_frontmatter: true
date: "2026-04-20"
depth: standard
---

# Connection Report: Towards a Science of Scaling Agent Systems

**Source:** [Towards a Science of Scaling Agent Systems](../../../sources/towards-a-science-of-scaling-agent-systems.md)

## Discovery Trace

**Index scan:**
- Read [sources index](../../../sources/dir-index.md) first. Flagged [What Survives in Multi-Agent Systems](../../../../sources/voooooogel-multi-agent-future.ingest.md), [Structured Test-Time Scaling](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md), and [MAKER](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md). Rejected [Multi-Agent Memory from a Computer Architecture Perspective](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) as memory-consistency focused rather than architecture-selection evidence.
- Read [notes index](../../../notes/dir-index.md). Flagged [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md), [decomposition-heuristics-for-bounded-context-scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md), [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md), [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels](../../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md), [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md), [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), and [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md).
- Read [reference index](../../../reference/dir-index.md) and [agent-memory-systems index](../../../agent-memory-systems/dir-index.md). No durable source connections kept; reference files are about the shipped commonplace system, and agent-memory-system reviews are either storage/retrieval focused or too system-specific for this paper.

**Topic indexes:**
- Source frontmatter has `tags: [academic-paper]`. No curated `academic-paper` tag index was found in the notes hub, so topic-index discovery was skipped.

**Semantic search:** grep-only fallback.
- `qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed` failed with `SQLITE_CANTOPEN`, so semantic search could not be run through qmd.

**Keyword search:**
- `rg -n "multi-agent|coordination|orchestration|scheduler|bounded-context|decomposition|error amplification|verification|voting|decorrel|topology|agent scaling|scaling" kb/notes kb/sources kb/reference kb/agent-memory-systems --glob '*.md'` surfaced the strongest cluster around orchestration, decomposition, verification, synthesis, and coordination guarantees. Kept candidates where Kim et al. contributes empirical architecture-selection or error-dynamics evidence. Rejected broad hits where "scaling" or "verification" referred to validation, indexing, or unrelated memory-system engineering.
- `find kb/notes -name '*agent*' -o -name '*orchestration*' -o -name '*scheduler*' -o -name '*decomposition*' -o -name '*error*' -o -name '*synthesis*'` confirmed the candidate note set and surfaced no stronger path candidates.

**Link following:**
- Followed [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md). It already cites Kim et al. as evidence and connects the paper to error correction, bounded scheduling, decomposition, oracle strength, MAKER, and topology/isolation/verification.
- Followed [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md). It treats Kim et al.'s 17.2x amplification as evidence consistent with missing decomposition, scoping, and voting, but not decisive about which missing mechanism dominates.
- Followed [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels](../../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md). It frames synthesis failure as amplification from missing adjudication, a direct fit for Kim et al.'s topology-dependent error data.
- Followed [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md) and [decomposition-heuristics-for-bounded-context-scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md). Kim et al. adds empirical limits on when additional bounded calls help: decomposable analysis tasks improve, sequential planning tasks degrade, and coordination overhead can dominate.
- Followed [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md). The paper's 58%-515% overhead range and tool-coordination trade-off are concrete context-cost evidence.

## Connections Found

- [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md) -- **grounds**: Kim et al.'s Independent topology reports 17.2x error amplification under synthesis-only aggregation, which is the central evidence for distinguishing error-propagating synthesis from error-correcting voting. The target note is `seedling`, but the relationship is evidence for the distinction, not a sole foundation.
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **extends**: the paper quantifies how verification-bearing topologies reduce but do not eliminate error amplification (centralized 4.4x, decentralized 7.8x, hybrid 5.1x), while also showing that identical-prompt multi-agent systems can retain correlated failure modes.
- [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels](../../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) -- **exemplifies**: the architecture comparisons show that changing coordination channels is insufficient unless the topology supplies a matching guarantee, especially adjudication/verification for output aggregation.
- [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md) -- **grounds**: the controlled comparison across single-agent, independent, centralized, decentralized, and hybrid architectures provides empirical evidence for treating orchestration as scheduler design over bounded calls, including the finding that selection/decomposition is task-contingent.
- [decomposition-heuristics-for-bounded-context-scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -- **extends**: Kim et al. adds measurable stopping-condition evidence for decomposition: Finance-style analysis benefits from centralized/decentralized coordination, while PlanCraft-style sequential reasoning degrades by 39-70% under multi-agent variants.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **grounds**: the paper's coordination overhead measurements (58%-515%), success-per-token collapse, and tool-coordination trade-off are concrete evidence that context/communication budget can dominate agent-system performance.
- [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) -- **extends**: Kim et al. supplies a controlled empirical case where topology changes performance through error amplification and verification strength, while leaving open whether decomposition, isolation, and verification are independent or a dependency chain. The target note is `speculative`; this source supports the question but does not settle it.
- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) -- **exemplifies**: hybrid coordination's 515% overhead and lowest efficiency show what happens when coordination state and semantic work consume the same bounded communication substrate.
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **grounds**: the paper operationalizes several independent dimensions at once: topology, coordination form, verification strength, model capability, task type, and overhead.

## Bidirectional Candidates

- [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md) <-> source -- **evidence**: the note should keep pointing to this source because it depends on Kim et al.'s error-amplification data and the Independent topology's synthesis-only aggregation.
- [decomposition-heuristics-for-bounded-context-scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) <-> source -- **evidence**: Kim et al.'s task-contingent results are useful empirical support for adding stopping-condition heuristics around decomposition overhead.
- [agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels](../../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) <-> source -- **evidence**: the source gives quantitative examples for the amplification row of the coordination-guarantee table.

## Raw Text Candidates

None

## Rejected Candidates

- [Multi-Agent Memory from a Computer Architecture Perspective](../../../../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) -- adjacent multi-agent source, but its main concern is shared/distributed memory consistency, not performance scaling across coordination topologies.
- [What Survives in Multi-Agent Systems](../../../../sources/voooooogel-multi-agent-future.ingest.md) -- useful contrast source and index neighbor, but it is better treated as a source-to-source tension in the ingest report than as a durable connection target.
- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- relevant architecture vocabulary, but Kim et al. does not directly analyze runtime component boundaries.
- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -- superficially related through sub-agent orchestration, but the paper does not study REPL-written orchestrators or ephemeral generated schedulers.
- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- coordination-medium overlap only; the paper's stronger contribution is topology, overhead, and verification effect, not conversation versus prompt handoff.

## Index Membership

- [computational-model-index](../../../notes/computational-model-index.md) -- the source contributes empirical evidence about scheduler topology, bounded-call decomposition, context overhead, and verification as architecture variables.
- [evaluation-index](../../../notes/evaluation-index.md) -- the source is a controlled agent-system evaluation with quantitative comparisons across models, tasks, and coordination structures.
- [tool-loop-index](../../../notes/tool-loop-index.md) -- optional membership if the index tracks when framework-owned or multi-agent loops should yield to explicit scheduler design.

## Synthesis Opportunities

- Kim et al. plus [MAKER](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) and [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md) imply a higher-order claim: multi-agent scaling should be evaluated by matching aggregation operation to decomposition structure, not by counting agents. Redundant calls need voting/adjudication; complementary calls need synthesis.
- Kim et al. plus [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) imply a test agenda: hold topology constant while varying isolation and verification to determine whether the causal-chain account beats the simpler decomposition account.

## Flags

- Several load-bearing target notes are `seedling` or `speculative`. Treat Kim et al. as strong empirical evidence for the questions those notes pose, not as sufficient proof of their broader theoretical claims.
- The source itself has a current note already derived from it, [synthesis-is-not-error-correction](../../../../notes/synthesis-is-not-error-correction.md), so the ingest report should recommend updating existing notes rather than creating a duplicate broad note unless the new note has a narrower thesis.
