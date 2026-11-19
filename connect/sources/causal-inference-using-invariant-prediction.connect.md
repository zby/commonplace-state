---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/causal-inference-using-invariant-prediction.md"
source_has_frontmatter: true
date: "2026-07-16"
depth: standard
---

# Connection Report: Causal inference using invariant prediction

**Source:** [Causal inference using invariant prediction](../../../sources/causal-inference-using-invariant-prediction.md)

## Discovery Trace

**Description listing scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- source snapshots stay immutable; ingest reports carry authored links.
- `rg -n "^description:.*(reach|causal|invariant|structured shift|representation|proof|oracle|self-modification|generalization|discovery)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- kept [reach assessment](../../../../notes/definitions/reach-assessment.md), [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md), [reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md), and [first-principles reasoning selects for explanatory reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md).

**Topic indexes:**
- Read the relevant notes directly from search results. No complete generated index was consulted.

**Body search:**
- `rg -n "causal discovery|invariant prediction|causal representation|do-calculus|counterfactual|intervention semantics|structural causal|causal model|observational data" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- kept the formal reach-assessment cluster and companion causal sources. Rejected unrelated counterfactual-evaluation hits in agent-memory reviews as evaluation-method overlap, not causal-theory reach grounding.

**Link following:**
- Followed [reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md) to its structured-shift argument. Kept it because invariant prediction supplies a formal version of "stable mechanism across shift"; rejected broader self-improving-system notes that mention Gödel machines but not causal mechanisms.

## Connections Found

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) -- **evidence**: the source states the core causal reach criterion: causal predictors should keep working under interventions or environment changes where non-causal predictors may fail.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) -- **evidence**: invariant prediction is a worked formal acceptance signal for causal reach, selecting candidate models by cross-environment invariance.

- [Reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md) -- **evidence**: the source supplies a formal causal-inference account of the note's "stable structure under shift" condition.

- [First-principles reasoning selects for explanatory reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **evidence**: invariant prediction operationalizes the distinction between an explanation that survives a changed environment and a predictor fitted only to one setting.

## Bidirectional Candidates

- [Towards Causal Representation Learning](../../../sources/towards-causal-representation-learning.md) <-> source -- **compares-with**: both use causal mechanisms to explain robustness and transfer, but invariant prediction gives a specific statistical identification method while causal representation learning gives the broader ML research agenda.

- [Causal-learn: Causal Discovery in Python](../../../sources/causal-learn-causal-discovery-in-python.md) <-> source -- **compares-with**: one is a method paper centered on invariance, the other is a library/survey surface for multiple causal discovery families.

## Reverse-edge Candidates

- [Reach assessment](../../../../notes/definitions/reach-assessment.md) → source -- **evidence**: the definition can cite this source for invariant prediction as a formal reach-assessment route.

- [Formal systems can assess reach through causal and proof obligations](../../../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) → source -- **evidence**: the new note should cite this source as the strongest grounding for invariance across interventions and environments.

- [Reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md) → source -- **evidence**: the note already uses causal mechanisms under shifts; this source gives a more precise invariant-prediction method to support that premise.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Known-target discovery benchmarks show reachability, not discovery](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- rejected: both discuss discovery, but this source is about causal identification from environments, not retrospective target-insight benchmarks.

## Index Membership

- Source index regeneration candidate only. No hand-authored index edit recommended.

## Synthesis Opportunities

None beyond the already-created formal-systems reach note.

## Maintenance Observations

None

## Flags

None
