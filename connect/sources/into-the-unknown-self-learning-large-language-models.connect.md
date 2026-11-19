---
description: "Discovery report for possible KB connections from the Into the Unknown self-learning LLM paper"
type: kb/cache/types/connect-report.md
source: "kb/sources/into-the-unknown-self-learning-large-language-models.md"
source_has_frontmatter: true
date: "2026-04-16"
depth: standard
---

# Connection Report: Into the Unknown: Self-Learning Large Language Models

**Source:** [Into the Unknown: Self-Learning Large Language Models](../../../sources/into-the-unknown-self-learning-large-language-models.md)

## Discovery Trace

**Index scan:**
- Read [notes directory](../../../notes/dir-index.md) and the learning-theory neighborhood surfaced by current note links. Flagged candidates:
  - [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- the paper is a pure opaque-loop continual-learning proposal, useful as the contrast case for non-opaque substrate loops.
  - [Continuous learning requires durability, not weight updates](../../../notes/continuous-learning-requires-durability-not-weight-updates.md) -- the paper treats self-learning as model training; the note argues durable capacity change is the real criterion, regardless of substrate.
  - [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- the paper automates knowledge acquisition through post-deployment weight adaptation, while the note covers durable symbolic adaptation during deployment.
  - [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- the paper directly attacks the "what to learn" question with a hallucination-derived unknown-selection operator.
  - [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- the paper also depends on an oracle-like selection signal, but its signal is hallucination/self-checking rather than task completion.
  - [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- hallucination scoring is a soft oracle for missing knowledge, with obvious failure modes.
  - [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- the source is nearby but not primarily trace-derived; it uses generated questions and search results as training data rather than mining session traces.

**Topic indexes:**
- [Learning theory](../../../notes/learning-theory-index.md) -- the source belongs in the continual-learning/oracle/substrate cluster because it proposes a closed opaque learning loop and makes unknown selection explicit.

**Semantic search:** qmd
- Query `"self-learning LLM hallucination unknown knowledge continual learning model training"` returned:
  - [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) (90%) -- accepted as the primary substrate contrast.
  - [Learning theory](../../../notes/learning-theory-index.md) (43%) -- accepted as index membership.
  - [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) (36%) -- accepted as a broader oracle/problem-selection connection.
  - [LLM learning phases fall between human learning modes](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) (37%) -- rejected as too broad; the paper is about deployed/self-training loops, not pretraining/in-context taxonomy.
- Query `"points in the unknown hallucination detection knowledge gaps self questioning search training"` returned mostly weak or off-topic hits. [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) appeared at low score and was rejected as indirect; its soft-oracle theme is better routed through [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md).
- Query `"continual learning weights durable knowledge substrate oracle self-assessment"` returned:
  - [Continuous learning requires durability, not weight updates](../../../notes/continuous-learning-requires-durability-not-weight-updates.md) (93%) -- accepted.
  - [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) (56%) -- accepted as a secondary non-weight contrast.
  - [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) (43%) -- accepted.
  - [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) (37%) -- accepted.

**Keyword search:**
- `rg "self-learning|continual learning|knowledge gap|unknown knowledge|hallucination|SelfCheckGPT|curiosity|model training|weight update|oracle" kb/notes kb/agent-memory-systems kb/sources --glob "*.md"` -- surfaced the new snapshot, Letta's [Continual Learning in Token Space](../../../sources/continual-learning-in-token-space.md), [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), and multiple agent-memory reviews where "oracle" is already the bottleneck vocabulary. Most review hits were rejected as generic oracle mentions.

**Link following:**
- Followed [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) to [Continuous learning requires durability, not weight updates](../../../notes/continuous-learning-requires-durability-not-weight-updates.md), [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), and [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md). This confirmed the source is useful as the opaque-loop counterpart to Meta-Harness-style non-opaque loops.
- Followed [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) to [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). This confirmed that the source's value is not "self-learning exists" but "unknown selection is an oracle-construction problem."
- Followed the Letta source to the repo-artifact learning cluster. It provides the closest sibling contrast: Letta argues for learned context/token-space adaptation; this paper argues for hallucination-filtered data followed by weight updates.

## Connections Found

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **contrasts**: the paper is a concrete opaque-substrate loop: identify unknowns, search for facts, train weights. It strengthens the note by showing the mainstream opaque route can make "what to learn" explicit while still leaving prose/symbolic substrates out of the loop.
- [Continuous learning requires durability, not weight updates](../../../notes/continuous-learning-requires-durability-not-weight-updates.md) -- **qualifies**: the paper clearly satisfies durable capacity change if the training succeeds, but it frames durability as model update. The note supplies the broader criterion and prevents overreading "self-learning" as synonymous with weights.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **contrasts**: the paper proposes post-deployment knowledge acquisition through training infrastructure; deploy-time learning proposes durable symbolic artifacts with ordinary versioning, review, and rollback. Same system-level goal, different substrate and operational cost.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- **extends**: Points in the Unknown is a concrete "what to learn" operator. It suggests that a KB analogue would need a way to detect unknown or underdeveloped regions, but also shows why factual hallucination scoring does not solve judgment-heavy note/link/synthesis evaluation.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **parallels**: both sources close a learning loop only after choosing an oracle. AgeMem uses task completion to train memory policy; this paper uses hallucination/self-checking to choose factual questions and external search to create supervision. The common lesson is oracle construction, not weight learning itself.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **exemplifies**: hallucination scoring is a soft oracle for missing knowledge. It is cheap and automatable, but noisy because hallucination can come from prompt ambiguity, decoding variance, conflict, reasoning failure, or bad retrieval rather than absent knowledge.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **exemplifies**: the paper's loop is plausible only where unknown detection and answer verification can be made cheap enough. The source's reliance on GPT-4o answer generation and manual verification in the experiment shows the boundary has not disappeared.
- [Continual Learning in Token Space](../../../sources/continual-learning-in-token-space.md) -- **contrasts**: Letta argues that deployed agents should primarily learn by editing portable context; this paper argues for creating new supervised/preference data and training model weights. Together they form a clean token/artifact versus weight-space contrast.

## Bidirectional Candidates

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source -- **contrasts**: if that note is revised again, this paper is the cleanest recent example of an opaque-loop self-learning proposal that still needs external search, hallucination scoring, and training infrastructure.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) <-> source -- **extends**: the paper's PiU mechanism is a candidate analogy for "unknown region" discovery, but the return link should emphasize why factual hallucination oracles do not transfer directly to KB synthesis and link-quality judgments.
- [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) <-> source -- **parallels**: both notes would benefit from a paired comparison between task-completion oracles and hallucination-as-unknown oracles.

## Raw Text Candidates

None.

## Rejected Candidates

- [Trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- related survey context, but the paper does not primarily mine runtime traces or agent sessions. It generates questions, retrieves answers, and trains, so it should not be added as a trace-derived system without a narrower subtype.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- conceptually nearby through soft oracles, but it is about KB-quality proxies. The hallucination scoring method here is better connected through [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) and [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md).
- [LLM learning phases fall between human learning modes](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) -- broad learning taxonomy only; no direct connection beyond "LLM learning."
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- qmd surfaced it from "unknown/context" vocabulary, but the source is about model knowledge acquisition, not transcript inheritance.

## Index Membership

- [Learning theory](../../../notes/learning-theory-index.md) -- the source belongs near continual learning, substrate choice, oracle construction, and automated improvement loops.
- [Agent memory systems index](../../../../agent-memory-systems/README.md) -- not a repo-backed memory-system review, but it is useful source-only background for the weight-update side of agent learning.

## Synthesis Opportunities

[Into the Unknown](../../../sources/into-the-unknown-self-learning-large-language-models.md), [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), [Memory management policy is learnable but oracle-dependent](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md), and [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) imply a note-sized claim: **unknown-selection is an oracle problem before it is a training problem**. PiU gives a concrete operator for factual weight learning, but KB learning needs a different unknown detector because hallucination is a poor proxy for missing synthesis, stale links, or underdeveloped theory.

[Into the Unknown](../../../sources/into-the-unknown-self-learning-large-language-models.md), [Continual Learning in Token Space](../../../sources/continual-learning-in-token-space.md), and [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) also imply a useful three-way comparison: weight-space self-learning, token/context-space self-learning, and repo-artifact coevolution share the same high-level loop shape but differ in rollback, inspectability, portability, and oracle needs.

## Flags

- The snapshot was captured from arXiv HTML with `lynx`, so the body contains noisy MathML-derived `[MATH: ... :MATH]` spans. The prose sections are readable, but formulas are not clean.
- The paper is an arXiv preprint. Treat its experiments and "self-learning capability" metrics as suggestive until independently replicated.
- The paper's loop is not fully autonomous in its own experiment: answer generation uses `gpt-4o-2024-05-13`, and the authors report manual answer-quality verification for the training dataset.
