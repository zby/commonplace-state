---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/pearl-a-probabilistic-calculus-of-actions-1994.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: A Probabilistic Calculus of Actions

**Source:** [A Probabilistic Calculus of Actions](../../../../sources/.snapshots/pearl-a-probabilistic-calculus-of-actions-1994.md)

## Discovery Trace

**Description listing scan:**

- Ran `rg '^description:'` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; focused the source scan with `causal|interven|observ|identif|action.?condition|world model|mechanism|policy|invariant|experiment|confound|counterfactual`. Kept the formal causal-reach, world-model, causal-representation-learning, and DoWhy candidates. Generic action and counterfactual matches did not pass the articulation test.

**Topic indexes:**

- Read the authorized destination README files and the learning-theory, discovery, and self-improving-systems heads. The snapshot has no tags, so no tag-completeness shortcut applied.

**Full title scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over all five authorized local destinations: notes, reference, agent-memory-systems, agentic-systems, and sources.

**Body search:**

- Searched for `Judea Pearl`, `do(`, `causal conditioning`, observation/intervention orderings, `back-door`, identifiability, mechanism replacement, action-conditioned models, partial causal theories, conditional actions, stochastic policies, and passive observation.

**Link following:**

- Followed one-hop neighborhoods around the formal-systems reach note, reach-assessment definition, world-model note, causal-representation-learning ingest, DoWhy ingest, invariant prediction, causal-learn, and V-JEPA 2. No target in reference, agent-memory-systems, or agentic-systems survived the articulation test.

## Connections Found

- [Formal symbolic systems assess explanatory-reach through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **is-evidence-for**: Pearl is the primary source for deriving intervention effects from a supplied causal graph, while also bounding the result by assuming graph topology and allowing only the probabilities to be partially specified.

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) -- **compares-with**: Pearl represents an action by replacing one explicit causal mechanism while preserving the others, providing the symbolic causal-graph route to compare with latent action-conditioned rollout prediction.

- [Towards Causal Representation Learning](../../../../sources/towards-causal-representation-learning.ingest.md) -- **compares-with**: Pearl assumes causal variables and topology and solves action-effect derivation, whereas the later review treats discovery of causal variables and reusable mechanisms as the hard front end.

- [DoWhy: Addressing Challenges in Expressing and Validating Causal Assumptions](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) -- **compares-with**: Pearl supplies the core action calculus and identification logic; DoWhy operationalizes a later model-identify-estimate-validate workflow and emphasizes that graph assumptions are only partly checkable.

## Bidirectional Candidates

- [Towards Causal Representation Learning](../../../../sources/towards-causal-representation-learning.ingest.md) <-> future ingest -- **compares-with**: its existing separation between causal learning and causal reasoning gains Pearl as the reasoning-side primary exemplar.

## Reverse-edge Candidates

- [Formal symbolic systems assess explanatory-reach through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -> future ingest -- **evidenced-by**: the note currently states what do-calculus does and would benefit from the foundational primary paper plus its supplied-topology boundary.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- Pearl demonstrates symbolic inference from a partial causal theory, but not theory learning, retained-theory reuse across shifts, or comparative sample efficiency.

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- Pearl concerns action semantics and inference, not whether a retained model is activated with behavioral authority.

- [Meta V-JEPA 2 action-conditioned world model review](../../../../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md) -- a direct comparison is valid but redundant because the curated world-model note already provides the symbolic-versus-latent bridge.

## Index Membership

None

## Synthesis Opportunities

- Pearl together with causal-representation learning suggests a claim not yet stated directly: mechanism-factorized action models can compose unanticipated interventions by selectively overriding stable mechanisms instead of enumerating one distribution per action.

## Maintenance Observations

None

## Flags

None

