---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/autogenesis-a-self-evolving-agent-protocol.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Autogenesis: A Self-Evolving Agent Protocol

**Source:** [Autogenesis: A Self-Evolving Agent Protocol](../../../sources/autogenesis-a-self-evolving-agent-protocol.md)

## Discovery Trace

**Collection rules and curated heads:**

- Read `kb/sources/COLLECTION.md`; it authorizes prospecting notes, reference, agent-memory systems, agentic systems, and sources, with snapshots remaining immutable and the ingest report carrying outbound edges.
- Read `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, and `kb/notes/deploy-time-learning-README.md`; the strongest clusters were proposal-selection, readable-artifact learning, diagnostic richness, and fixed update spaces.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Reference had no direct Commonplace implementation analogue strong enough to justify a source-side `see-also`; agent-memory had no good target because the paper specifies Memory as a resource but does not independently evaluate memory evolution; agentic systems yielded Exo as a code-grounded comparison.

**Full title and description scans:**

- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# '` over each authorized local destination: notes (326 lines), reference (125), agent-memory systems (171), agentic systems (8), and sources (415).
- Ran `rg '^description:'` over each destination and filtered for `self-improv|self-evol|reflect|proposal|evaluation|retention|rollback|version|trace|fixed decomposition|update space|diagnostic|objective|resource|artifact|harness|protocol`. This retained the proposal-selection, diagnostic-richness, fixed-decomposition, readable-artifact, Exo, Symbolic Learning, and Self-Harness candidates.

**Body searches:**

- `rg -n -i 'proposal[- ]selection|search, evaluation|operative retention|reject-capable' kb/notes/ --glob '*.md'` -- kept the proposal-selection anatomy because Autogenesis names distinct proposal, evaluation, commit, and rollback operations.
- `rg -n -i 'effective update space|fixed decomposition|learnability mask|trainable subspace' kb/notes/ --glob '*.md'` -- kept the fixed-decomposition note because Autogenesis explicitly defines a binary learnability mask and trainable subspace, then evaluates only selected coordinates.
- `rg -n -i 'diagnostic richness|execution traces|causal failure|reflection.*trace|trace.*reflection' kb/notes/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- kept diagnostic richness because the reflection optimizer's search context consists of traces and inferred causal failures, but rejected memory-system reviews that merely mention traces.
- `rg -n -i 'rollback|versioned|auditab|lineage' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- kept Exo as the strongest code-grounded system comparison; rejected general freshness and lineage documentation because shared vocabulary alone did not yield a useful source-to-reference edge.
- `rg -n -i 'prompts?.*tools?.*memory|tools?.*prompts?.*memory|resource substrate|evolvable resource' kb/notes/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- kept the readable-artifact loop; rejected memory reviews because Autogenesis's Memory entity is specified but not tested.

**Link following and candidate evaluation:**

- Followed the self-improving-systems head to [proposal-selection](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [self-improvement relative to an objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md), and [reflection buys addressability](../../../../notes/reflection-buys-addressability.md). Kept proposal-selection; rejected the objective note as true but too generic for traversal, and rejected addressability because the paper demonstrates versioned inspection and rollback but not later semantic criticism or transfer of retained commitments.
- Followed the deploy-time-learning head to [diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [learning inside a fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). All three passed with distinct reader needs: search evidence, mixed-form retained targets, and experimental scope.
- Followed the agentic-system index to [Exo](../../../../agentic-systems/reviews/exo.md). Kept it because both systems separate a protected/versioned substrate from editable agent resources, but Exo exposes a live code-grounded self-rebuild and weaker semantic gates while Autogenesis presents a typed protocol plus benchmarked, narrower update targets.
- Followed related-source descriptions to [Symbolic Learning](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) and [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md). Kept Symbolic Learning as the closest earlier whole-readable-harness comparison; rejected a durable Self-Harness edge as duplicative of the proposal-selection and fixed-decomposition notes.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: Autogenesis implements candidate generation, reject-capable evaluation, versioned commit, and rollback as explicitly typed operations rather than an analyst-imposed reconstruction.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **rests-on**: the reflection optimizer maps execution traces to causal failure hypotheses before selecting edits, so its search quality depends on the distinctions retained in those traces even though the paper does not ablate trace representations.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: prompts, tool code, agent code, configurations, and memory are lifted into versioned, inspectable resources that an LLM-mediated loop can edit and re-evaluate.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: Autogenesis names its update boundary unusually clearly through a binary learnability mask, while the experiments vary prompts, solutions, or agents inside a fixed resource ontology, orchestration, evaluator, benchmark, and three-round loop.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: both designs put mutable agent machinery over a protected state/versioning substrate, but Exo is a code-grounded live self-rebuild harness and Autogenesis is a typed protocol evaluated through narrower resource edits.
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- **compares-with**: both treat prompts, tools, and their organization as a readable optimization surface; Symbolic Learning emphasizes language-mediated backward credit assignment, while Autogenesis emphasizes lifecycle, versioning, and optimizer-independent operator interfaces.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: the typed Reflect/Select/Improve/Evaluate/Commit loop is a clean empirical-system instance of the note's three functions.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: the explicit learnability mask and trainable subspace supply a particularly legible worked case of an effective update boundary.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- **evidenced-by**: the experiments add a mixed natural-language/symbolic, versioned-resource case, subject to the fixed-decomposition caveat.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) -- Autogenesis has an explicit objective and evaluator, but this is definitional overlap already carried by the more discriminating proposal-selection edge.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- version inspection and rollback provide mechanical addressability, but the paper does not test later rounds reading a retained change as a criticizable commitment or transferring its rationale.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- both describe reflective update loops, but the Commonplace case is implementation-specific and the authorized source-to-reference `see-also` would be too weak to help traversal.
- [Exo agent memory system review](../../../../agent-memory-systems/reviews/exo.md) -- Autogenesis declares Memory a first-class resource but does not independently evaluate its capture, activation, authority, or lifecycle behavior, so a memory-system comparison would overstate the evidence.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- a genuine comparison, but it repeats the fixed-outer-loop and proposal-selection relationships already expressed more directly through theory notes.

## Index Membership

None

## Synthesis Opportunities

None. The source operationalizes existing proposal-selection, readable-artifact, diagnostic-richness, and update-space claims more than it implies a new higher-order claim.

## Maintenance Observations

None

## Flags

- Experiment-bearing source: reported gains establish improvement inside the declared learnability masks and fixed benchmark configurations; they do not validate the five-entity resource ontology, the bus orchestration, the operator algebra, or the protocol as a whole.
- Tension: the paper calls interface-mediated evolution "safe-by-construction," but the experiments do not evaluate safety invariants, behavioral drift, semantic rollback criteria, or alignment; versioning proves reversibility of state, not correctness of the acceptance oracle.
