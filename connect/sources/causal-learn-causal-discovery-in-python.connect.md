---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/causal-learn-causal-discovery-in-python.md"
source_has_frontmatter: true
date: "2026-07-16"
depth: standard
---

# Connection Report: Causal-learn: Causal Discovery in Python

**Source:** [Causal-learn: Causal Discovery in Python](../../../sources/causal-learn-causal-discovery-in-python.md)

## Discovery Trace

**Description listing scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- source snapshots are immutable; the matching ingest report carries the authored connection surface with `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, or sparse `see-also`.
- `rg -n "^description:.*(reach|causal|invariant|structured shift|representation|proof|oracle|self-modification|generalization|discovery)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- kept [reach assessment](../../../../notes/definitions/reach-assessment.md), [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md), and [reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md). Rejected reflective-system causal-connection sources as using "causal" in the reflection sense rather than causal inference.

**Topic indexes:**
- Read notes collection rules and the curated foundations/self-improving-system area indirectly through the existing notes opened during the task. No generated index was used as authoritative navigation.

**Body search:**
- `rg -n "causal discovery|invariant prediction|causal representation|do-calculus|counterfactual|intervention semantics|structural causal|causal model|observational data" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- confirmed this source is the direct local grounding for the observational-causal-discovery clause in reach assessment; also surfaced the companion invariant prediction, causal representation, and DoWhy assumptions snapshots.
- `rg -n "formal systems.*reach|symbolic.*reach|reach assessment.*formal|causal theories.*reach|do-calculus|causal discovery" kb/notes --glob "*.md"` -- found no duplicate note beyond the new formal-systems reach note and the reach-assessment definition.

**Link following:**
- Followed [reach assessment](../../../../notes/definitions/reach-assessment.md) to [representational form](../../../../notes/definitions/representational-form.md), [Gödel machines](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md), and [reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md). Kept only the formal reach-assessment cluster; representational form is background vocabulary, not a direct source connection.

## Connections Found

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) -- **evidence**: the source grounds the claim that causal theories can be inferred from observational data, but only through explicit method assumptions rather than raw correlation.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) -- **evidence**: causal-learn is a concrete system-family example for the causal-discovery half of the formal reach-assessment route.

## Bidirectional Candidates

- [DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions](../../../sources/dowhy-expressing-and-validating-causal-assumptions.md) <-> source -- **compares-with**: causal-learn focuses on graph discovery methods, while DoWhy emphasizes declaring, identifying, estimating, and partially validating assumptions for causal effects.

- [Causal inference using invariant prediction](../../../sources/causal-inference-using-invariant-prediction.md) <-> source -- **compares-with**: invariant prediction is one causal-discovery strategy built around cross-environment invariance; causal-learn is a library-level survey and implementation surface for multiple discovery families.

## Reverse-edge Candidates

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) → source -- **evidence**: the definition's observational-discovery exception should cite this source when it states that causal theories can be learned from observations under assumptions.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) → source -- **evidence**: the new claim note should cite this source as the concrete grounding for causal discovery from observations.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflective system](../../../../notes/definitions/reflective-system.md) -- rejected: its "causal connection" requirement concerns self-representation affecting system behavior, not causal-inference theory.

- [The tag-readme change as an observed causal-connection trace](../../../../notes/evidence/tag-readme-trace-observed-causal-connection.md) -- rejected for the same reason; it is a reflection trace, not a causal-discovery source.

## Index Membership

- Source index regeneration candidate only. No hand-authored index edit recommended.

## Synthesis Opportunities

None beyond the already-created formal-systems reach note.

## Maintenance Observations

None

## Flags

None
