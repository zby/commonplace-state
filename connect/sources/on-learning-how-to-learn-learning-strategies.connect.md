---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/on-learning-how-to-learn-learning-strategies.md"
source_has_frontmatter: true
date: "2026-04-29"
depth: standard
---

# Connection Report: On Learning How to Learn Learning Strategies

**Source:** [On Learning How to Learn Learning Strategies](../../../sources/on-learning-how-to-learn-learning-strategies.md)

## Discovery Trace

**Index scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- snapshots are immutable; active outbound links belong in the matching ingest report. Authorized labels from source analyses into notes include `evidence`, `derived-from`, `rationale`, `defined-in`, and sparing `see-also`; source-to-source / source-to-agent-memory uses `compares-with`.
- Read [notes index](../../../notes/dir-index.md) -- flagged [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), [memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), [continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md). Kept the oracle/learning/promotion cluster because the paper's central mechanism is reward-gated retention of behavior-changing self-modifications; rejected broad context-engineering hits that did not address promotion, verification, or learned behavior.
- Read [agent-memory systems index](../../../agent-memory-systems/dir-index.md) and [source-only directory](../../../agent-memory-systems/source-only/dir-index.md) -- the strongest existing artifact is [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md), which already covers this exact technical report as source-only lineage.
- Read [sources index](../../../sources/dir-index.md) -- closest sibling source is [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md), which updates the Schmidhuber self-improvement lineage into modern coding-agent scaffold search. Other self-improving-agent sources were weaker because they learn prompt-visible tips or memories rather than self-modifying policy distributions.

**Topic indexes:**
- Read [learning-theory index](../../../notes/learning-theory-index.md) -- reinforced [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). The source sits at the opaque/reward-gated behavior-change edge of the learning-theory area, not inside the KB's preferred readable-artifact loop.
- Read [agent-memory index](../../../notes/agent-memory-index.md) -- surfaced promotion, authority, and trace-derived extraction notes. Kept only [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) as an analogy candidate because the paper's stack-backed rollback makes promotion cost and reversibility explicit.

**Body search:**
- `rg -n "self-modification|self-improvement|learning how to learn|reward-gated|payoff|meta-learning|inductive bias" kb/notes kb/agent-memory-systems kb/sources --glob "*.md"` -- found the existing [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md) note, [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md), [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md), [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md), [OpenSage](../../../../agent-memory-systems/reviews/OpenSage.md), and [trace-derived learning techniques](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md). Kept source-only Incremental Self-Improvement and HGM; rejected generic self-improvement mentions where the mechanism was accumulation or tool growth rather than reward-gated policy mutation.
- `rg -n "oracle|promotion|learning-value|task completion|reward|evaluation signal|hard oracle" kb/notes kb/sources kb/agent-memory-systems --glob "*.md"` -- found [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [automating KB learning](../../../../notes/automating-kb-learning-is-an-open-problem.md), [memory management policy](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [choosing what to learn](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md). Kept these because the paper's `payoff per time` rule is a concrete promotion oracle; rejected general benchmark discussions that did not address persistence or promotion.
- `rg -n "inductive bias|primitive choice|prior bias|reach|adaptive fit" kb/notes kb/sources --glob "*.md"` -- found [first-principles reasoning selects for explanatory reach](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md), [induction bias sequence models ingest](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md), and source text. Kept reach only as an interpretive lens for limitations: the paper is explicit about adaptive fit to benign environments but does not provide a broad empirical theory of transfer.

**Link following:**
- From [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md), followed links to [trace-derived learning techniques](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md), [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md), [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md), and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md). This established the current KB framing: the source is already represented as conceptual lineage for policy-level promotion, not as a modern KB system.
- From [memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), followed to [automating KB learning](../../../../notes/automating-kb-learning-is-an-open-problem.md), [continual learning's open problem is behaviour](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), and [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md). This clarified that the source's contribution is a strong early case of learned behavior policy under a reward oracle, but with an opaque, non-inspectable learned state.
- From [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md), followed to [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md). HGM is the modern sibling: it keeps the hard-oracle self-improvement frame but moves the mutable substrate into inspectable code/prompt artifacts.

## Connections Found

- [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md) -- **compares-with**: existing source-only coverage already summarizes this exact FKI-198-94 report and places it outside repo-inspected agent-memory reviews. The ingest should treat the snapshot as source backing for that note, not as a new system review.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the paper's top-level strategy works only because payoff per time supplies a numeric promotion oracle for self-modifications. It is a concrete early example of the generator/modifier plus verifier pattern under a reward signal.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- **evidence**: the paper shows what an automated learning loop looks like when the promotion oracle is defined, and by contrast clarifies why KB mutations stall where "better future reasoning" lacks an equivalent payoff signal.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **evidence**: Schmidhuber's system learns a policy over future action/self-modification sequences and keeps changes only under reward/time improvement, a stronger but less inspectable predecessor of task-oracle memory-policy learning.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**: the learned state changes future behavior by shifting probabilities over instruction sequences; it is not accumulation of facts for retrieval.
- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **evidence**: the paper collapses validity and value into observed payoff per time. That is viable for rewardable toy tasks but exposes why KB learning needs separate gates for groundedness and future value.
- [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- **compares-with**: HGM is a modern coding-agent descendant of the same self-improvement lineage; it replaces self-modifying probability distributions with benchmark-guided search over durable agent scaffolds and lineage-level selection.

## Bidirectional Candidates

- [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md) <-> source -- **compares-with**: the source-only note should eventually cite the local snapshot as its captured source instead of only the external PDF URL.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) <-> source -- **evidence**: the paper provides a clean historical example of hard reward gating, but also a limitation case because apparent usefulness can be a fluke under single-experience induction.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) <-> source -- **evidence**: the paper extends the note's AgeMem comparison backward to self-referential policy learning; both depend on a reward/task oracle, but Schmidhuber's substrate is less inspectable.

## Reverse-edge Candidates

- [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md) -> source -- **compares-with**: should cite the local snapshot as captured evidence for the source-only coverage note.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -> source -- **compares-with**: the survey can use this as historical source-only lineage for reward-gated policy promotion, but should keep its lower evidence tier because no repository was inspected.
- [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -> source -- **compares-with**: useful historical predecessor; HGM's CMP and scaffold search can be contrasted with FKI-198-94's payoff-per-time stack and opaque probability distribution.

## Off-authorisation Candidates

- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- the analogy is strong: useful self-modification must pay for its own learning/evaluation cost, and stack rollback preserves reversibility. However this is in the `agent-memory-requirements` subarea and the source mostly supports the broader learning-value/oracle notes; use as context in ingest rather than a primary connection.
- [First-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) -- the source explicitly accepts that incremental self-improvement only helps in benign environments with regularities, which is adaptive-fit language. It is a useful limitation lens but not a direct source of the reach claim.

## Raw Text Candidates

None

## Rejected Candidates

- [Designing a Memory System for LLM-Based Agents](../../../../notes/designing-agent-memory-systems.md) -- rejected as a primary connection: the paper is about self-modifying policy, not memory objects, activation, or storage architecture in the KB's current sense.
- [OpenSage](../../../../agent-memory-systems/reviews/OpenSage.md) -- rejected as outbound connection: it has runtime self-modification without comparable reward-gated retention; the contrast is already covered better by the self-modification-oracle discussion.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) and [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md) -- rejected as direct outbound connections from this ingest: they are modern hard-oracle self-improvement systems, but [Huxley-Gödel Machine ingest](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) is the cleaner sibling bridge for this specific historical source.
- [Induction Bias sequence models ingest](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) -- rejected despite the shared phrase "inductive bias"; Ebrahimi studies architectural data-efficiency biases in sequence models, while Schmidhuber studies explicit self-shifting search bias.

## Index Membership

- [learning-theory index](../../../notes/learning-theory-index.md) -- the ingest belongs as historical reference material for oracle-dependent behavior learning and self-improvement.
- [sources index](../../../sources/dir-index.md) -- generated source index should include the new snapshot and ingest report after refresh.
- [agent-memory source-only directory](../../../agent-memory-systems/source-only/dir-index.md) -- no edit from connect, but future source-only coverage can cite the local snapshot.

## Synthesis Opportunities

Schmidhuber 1995 plus AgeMem plus HGM suggest a three-way comparison note: **learned promotion policy requires matching substrate, oracle, and temporal target**. FKI-198-94 uses opaque probability distributions plus payoff-per-time; AgeMem uses weights plus task completion; HGM uses readable code/prompt artifacts plus benchmark/lineage scoring. The synthesis would sharpen when reward-gated learning is viable and when the KB should prefer inspectable artifact promotion with human/semantic gates.

## Flags

- The existing [Incremental Self-Improvement](../../../agent-memory-systems/source-only/incremental-self-improvement.md) note already captures most durable value from this source. The ingest should avoid duplicating that note and instead recommend a narrow update or reference action.
