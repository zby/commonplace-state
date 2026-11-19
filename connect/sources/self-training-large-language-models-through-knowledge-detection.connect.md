---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/self-training-large-language-models-through-knowledge-detection.md"
source_has_frontmatter: true
date: "2026-04-20"
depth: standard
---

# Connection Report: Self-training Large Language Models through Knowledge Detection

**Source:** [Self-training Large Language Models through Knowledge Detection](../../../sources/self-training-large-language-models-through-knowledge-detection.md)

## Discovery Trace

**Target read:**
- Read the captured PDF snapshot. Core mechanism: generate Wikipedia-grounded questions, SFT the model on self-answers plus reading-comprehension examples, build DPO preferences from with-document versus without-document answers, then filter preference examples by consistency and knowledge-gap scores using contradiction scoring. Main claims: selective training on unknown samples improves Wiki-Test truthfulness and reduces forgetting versus unfiltered DPO.

**Index scan:**
- Read [sources index](../../../sources/dir-index.md) -- flagged [Into the Unknown ingest](../../../../sources/into-the-unknown-self-learning-large-language-models.ingest.md) because it is the closest prior self-learning/unknown-detection paper already ingested; flagged [Continual Learning in Token Space ingest](../../../../sources/continual-learning-in-token-space.ingest.md) as a substrate contrast; flagged [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) as a trace-derived learning contrast with inspectable artifacts.
- Read [notes index](../../../notes/dir-index.md) -- flagged [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), and [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md).
- Read [agent-memory-systems index](../../../agent-memory-systems/dir-index.md) -- flagged [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md). Keyword search later found [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md), the code-grounded review for this exact repository.
- Read [reference index](../../../reference/dir-index.md) and [instructions index](../../../instructions/dir-index.md) -- no durable candidate beyond command/procedure context.
- Read definitions/research/evidence directory indexes; no direct candidate beyond [distillation](../../../notes/definitions/distillation.md), rejected below because the paper uses ML context-distillation vocabulary rather than the KB's source-to-artifact distillation claim.

**Topic indexes:**
- Source tag `academic-paper` has no curated tag index.
- Read [learning theory index](../../../notes/learning-theory-index.md) because the index scan placed the source in the continual-learning cluster. Curated sections confirmed the strongest neighborhoods: deploy-time learning, substrate analysis, oracle/verification, and memory architecture.

**Semantic search:** grep-only fallback.
- Attempted `qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed`; qmd was installed but failed with `SQLITE_CANTOPEN: unable to open database file`. No qmd scores available.

**Keyword search:**
- `rg -n -i "self-training|self training|knowledge detection|unknown|unknowns|hallucination|truthfulness|catastrophic forgetting|continual|DPO|preference|fine-tun|training|distillation|context distillation|token space|memory" ...` -- surfaced the learning-theory cluster, the prior Into the Unknown source, and the same-repo Self-Training-LLM review.
- `rg -n -i "self-training|self learning|self-learning|self-train|self-improv|learn from.*output|own output|own outputs" ...` -- confirmed that existing self-learning coverage is concentrated in the Into the Unknown source and trace-derived system reviews rather than general notes.
- `rg -n -i "trajectory|trace-derived|tips|memory management policy|oracle-dependent|closed learning loop|task-completion oracle" ...` -- confirmed the relevant contrast set: AgeMem, trajectory-informed memory, Pi Self-Learning, ExpeL, and the trace-derived learning survey.

**Link following:**
- Followed [Into the Unknown ingest](../../../../sources/into-the-unknown-self-learning-large-language-models.ingest.md) to the oracle and substrate notes it already connects to.
- Followed [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) to trace-derived learning, oracle strength, and continual-learning notes.
- Followed [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) to compare task-completion-oracle policy learning with contradiction-score unknown selection.
- Followed [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) to confirm it is a contrast, not a primary connection: same learning-loop family, different trace source and inspectable output substrate.

## Connections Found

- [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) -- **grounds**: the review inspects the repository for this paper and names the same mechanism in code terms: generated Wikipedia QA traces, NLI/SelfCheck-style unknown scoring, SFT/DPO dataset construction, and weight-checkpoint promotion rather than durable memory. The paper supplies the experimental claims; the review supplies implementation-level constraints and caveats.
- [Ingest: Into the Unknown: Self-Learning Large Language Models](../../../../sources/into-the-unknown-self-learning-large-language-models.ingest.md) -- **extends**: this paper narrows the prior PiU/self-question/search/train frame into a concrete DPO preference construction method over a supplied knowledge source, adding two filtering stages and stronger forgetting evaluation.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **evidence**: the source is a weight-side behaviour-change loop; it changes future model behavior through SFT/DPO rather than merely adding retrievable facts, so it is a useful contrast case for the note's readable-artifact alternative.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **contrasts**: the paper freezes the readable staging artifacts as temporary data and promotes into opaque weights, making it a clean opaque-substrate example against the KB's prose/symbolic coevolution agenda.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **extends**: AgeMem learns when to use memory operations from task-completion reward; this paper learns which QA traces should become preference examples from contradiction/knowledge scores. Both show that selection policy is the hard part and that the policy quality depends on the oracle.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- **extends**: the source adds a batch corpus-grounded trace-to-weights case: generated questions, context documents, sampled answers, contradiction scores, and pairwise judgments become SFT/DPO data. It is trace-derived learning without live agent trajectories.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **exemplifies**: the paper's consistency score, knowledge score, and LLM judge are soft oracles used to make promotion decisions. The with-document chosen answer strengthens the oracle but does not make it hard.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **exemplifies**: the paper automates a learning loop only where verification is locally available: Wikipedia context can anchor answers and NLI contradiction can approximate answer disagreement. Its limits show why broader self-learning stalls when the verifier is weaker.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- **extends**: the paper cleanly separates input validity filtering from learning-value filtering. That decomposition transfers to KB mutation pipelines even though the specific hallucination/contradiction scores do not.

## Bidirectional Candidates

- [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) <-> source -- **grounds**: the code review should probably link back to this paper snapshot/ingest as the published-method counterpart to the inspected implementation.
- [Ingest: Into the Unknown: Self-Learning Large Language Models](../../../../sources/into-the-unknown-self-learning-large-language-models.ingest.md) <-> source -- **extends**: the two sources should be traversable together as adjacent work by overlapping authors on unknown-driven self-learning.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) <-> source -- **extends**: if the survey adds source-only exemplars, this paper is a clear batch-generation-to-weights case alongside the Self-Training-LLM repo review.

## Raw Text Candidates

None.

## Rejected Candidates

- [Continual Learning in Token Space ingest](../../../../sources/continual-learning-in-token-space.ingest.md) -- useful substrate contrast, but the source being connected is a weight-update scientific paper, while Letta's piece is a conceptual token-space argument. Keep as background in the ingest report rather than a direct connection.
- [Trajectory-Informed Memory Generation ingest](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- same broad trace-derived learning family, but the trace source, oracle, and promotion target differ enough that [Trace-derived learning techniques](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) is the better bridge.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- rejected as too broad for a direct link. The paper is not constraining through readable artifacts; it is a contrast to that mechanism.
- [Distillation](../../../notes/definitions/distillation.md) -- rejected to avoid terminology collision. The paper discusses context distillation / self-training in ML terms; the KB definition concerns directed context compression into artifacts.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- rejected because the paper is not an agent-memory system; it is trace-derived weight learning over generated QA data.

## Index Membership

- [Learning theory](../../../notes/learning-theory-index.md) -- good reference-material candidate under Memory & Architecture or Deploy-time Learning as an opaque-substrate, unknown-selection, trace-to-weights counterexample.
- [Sources directory](../../../sources/dir-index.md) -- should include the new snapshot after index regeneration.
- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- source-only mention may be warranted if the survey wants to distinguish batch corpus-grounded generation traces from live session and benchmark trajectories.

## Synthesis Opportunities

- **Unknown selection should separate candidate validity from learning value.** This source, [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md), and [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) jointly imply a reusable design pattern: first filter whether a candidate is well-formed and grounded, then separately filter whether it is worth promoting because the current system is weak on it.
- **Soft oracles can support bounded self-learning when anchored by reference context.** This paper and [Into the Unknown ingest](../../../../sources/into-the-unknown-self-learning-large-language-models.ingest.md) suggest that hallucination/contradiction signals become more useful when a reference context or searched answer constrains the chosen side. The reach is limited to factual/referenceable domains.

## Flags

- qmd semantic search failed with `SQLITE_CANTOPEN`; this report uses index and grep discovery only.
- The snapshot was newly created and was not yet present in the generated sources index at discovery time.
