---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/meta-v-jepa-2-world-model.md
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Introducing the V-JEPA 2 world model

**Source:** [Introducing the V-JEPA 2 world model](../../../../sources/.snapshots/meta-v-jepa-2-world-model.md)

## Discovery Trace

**Description listing scan:**
- Generated the full `# ` title surface for `kb/notes/` and filtered the notes description listing for `world model|action-conditioned|prediction|causal|reach assessment|physical`. Kept the action-conditioned reach note and action-model consumption note.
- Reference, agent-memory-system, and agentic-system destinations had no source-specific trigger after the cross-collection body search and were skipped.

**Topic indexes:**
- Read `kb/notes/README.md` and `kb/sources/README.md`; the existing world-model/reach thread is the relevant route.

**Body search:**
- `rg -n -i 'V-JEPA|action-conditioned|world model|latent predictor|physical reasoning' kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` found the grounded world-model note, the legacy combined review, and model-mediated-action comparisons.

**Link following:**
- Followed the action-conditioned note through reach-assessment and formal symbolic comparison, then followed Craik and Pearl as conceptual and symbolic counterpoints.

## Connections Found

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — **is-evidence-for**: the release describes candidate-action prediction, goal-distance ranking, replanning, unseen environments, and measured benchmark gaps.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: the predictor affects behavior through model-predictive control rather than remaining a passive representation.
- [Craik, Hypothesis on the Nature of Thought](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) — **compares-with**: both use simulated consequences to choose actions, but V-JEPA 2 implements the route through learned embeddings and receding-horizon control.
- [Pearl, A Probabilistic Calculus of Actions](../../../../sources/pearl-a-probabilistic-calculus-of-actions-1994.ingest.md) — **compares-with**: Pearl changes an explicit causal mechanism under intervention; V-JEPA 2 predicts action-conditioned latent trajectories without an explicit causal graph.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) → future ingest — **evidenced-by**: replace the combined legacy review with this blog ingest and its separate publication-page ingest.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [AriGraph](../../../../agent-memory-systems/reviews/AriGraph.md) — its in-run graph is an executable world model in a different sense and would blur physical prediction with memory representation.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The legacy V-JEPA 2 review merges two external URLs. Each URL needs its own immutable snapshot and tracked ingest.

## Flags

None
