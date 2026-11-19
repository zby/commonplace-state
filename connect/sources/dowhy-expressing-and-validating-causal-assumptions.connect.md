---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/dowhy-expressing-and-validating-causal-assumptions.md"
source_has_frontmatter: true
date: "2026-07-16"
depth: standard
---

# Connection Report: DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions

**Source:** [DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions](../../../sources/dowhy-expressing-and-validating-causal-assumptions.md)

## Discovery Trace

**Description listing scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- snapshots are immutable; durable interpretation belongs in the matching ingest report.
- `rg -n "^description:.*(reach|causal|invariant|structured shift|representation|proof|oracle|self-modification|generalization|discovery)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- kept [reach assessment](../../../../notes/definitions/reach-assessment.md), [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md), and [warranted autonomy is bounded by oracle reach](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).

**Topic indexes:**
- Used the search-result cluster rather than broad index traversal; the source's role is narrow, grounding assumptions and partial validation for causal inference.

**Body search:**
- `rg -n "causal discovery|invariant prediction|causal representation|do-calculus|counterfactual|intervention semantics|structural causal|causal model|observational data" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- confirmed the source's closest local role: it limits formal reach assessment by making causal assumptions explicit and only partially testable.

**Link following:**
- Followed [warranted autonomy is bounded by oracle reach](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) because the source's "no global validator" point mirrors the note's oracle-boundary claim. Kept as evidence for the limitation, not as a source for self-improving-system autonomy.

## Connections Found

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) -- **evidence**: the source grounds the limitation that causal reach assessment depends on declared assumptions and cannot be globally validated from observed data.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) -- **evidence**: the source supplies the assumption-declaration and partial-validation boundary for treating causal inference as formal reach assessment.

- [Warranted autonomy is bounded by oracle reach](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **evidence**: the source is a causal-inference instance of the oracle-boundary claim: causal effect estimates can be automated only as far as assumptions can be declared, identified, estimated, and partially refuted.

## Bidirectional Candidates

- [Causal-learn: Causal Discovery in Python](../../../sources/causal-learn-causal-discovery-in-python.md) <-> source -- **compares-with**: causal-learn supplies discovery methods; DoWhy emphasizes the assumption surface and validation/refutation workflow needed before and after discovery.

- [Causal inference using invariant prediction](../../../sources/causal-inference-using-invariant-prediction.md) <-> source -- **compares-with**: invariant prediction uses one invariance assumption to infer causal predictors; DoWhy generalizes the need to express and partially validate causal assumptions.

## Reverse-edge Candidates

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) → source -- **evidence**: the definition's "causal discovery is not assumption-free induction" warning should cite this source.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) → source -- **evidence**: the new note should cite this source for the formal-assumption boundary of the causal route.

- [Warranted autonomy is bounded by oracle reach](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) → source -- **evidence**: the note could cite this as a domain-specific example of a high-value automation surface bounded by missing global validation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- rejected: both discuss validation limits, but this source is about causal inference assumptions, not KB mutation or synthesis oracles.

## Index Membership

- Source index regeneration candidate only. No hand-authored index edit recommended.

## Synthesis Opportunities

None beyond the already-created formal-systems reach note.

## Maintenance Observations

None

## Flags

None
