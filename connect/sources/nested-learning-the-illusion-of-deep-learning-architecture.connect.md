---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/nested-learning-the-illusion-of-deep-learning-architecture.md"
source_has_frontmatter: true
date: "2026-07-31"
depth: standard
---

# Connection Report: Nested Learning: The Illusion of Deep Learning Architecture

**Source:** [Nested Learning: The Illusion of Deep Learning Architecture](../../../sources/nested-learning-the-illusion-of-deep-learning-architecture.md)

The target is an immutable source snapshot and has no matching `.ingest.md` companion at discovery time. `Connections Found` therefore recommends links for the ingest report that will carry the source's authored surface; `Reverse-edge Candidates` records the primary note-side authoring signal declared for snapshots.

## Discovery Trace

**Collection contract:**
- Read `kb/sources/COLLECTION.md` before prospecting. It authorises local destinations `notes`, `reference`, `agent-memory`, `agentic-systems`, and `sources`; excludes `kb/work/` and `kb/instructions/`; and makes reverse-edge discovery toward library notes first-class for immutable snapshots. Applicable authored-surface labels are `is-evidence-for`, `abstracted-from`, and `rests-on` toward notes; `defined-in` toward note definitions; `compares-with` toward notes, sources, agent-memory, and agentic-systems; and sparing `see-also` toward all authorised destinations.
- Read `kb/notes/COLLECTION.md` to evaluate reverse edges under the candidate note's own rules. Notes may link to source snapshots with `evidenced-by`, `derived-from`, `abstracted-from`, or sparing `see-also`.

**Curated heads and full title surfaces:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no `tags`, so no tag-README pass applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over all five authorised destinations: `notes` (324 titles), `reference` (124), `agent-memory-systems` (171), `agentic-systems` (8), and `sources` (408). Title-level candidates clustered around continual learning, fixed decompositions, representational form, in-context learning, self-modification, and the already-captured Sleep paper.

**Description listing scan:**
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised destination. In `notes`, the strongest candidates were `learning-inside-a-fixed-decomposition-inherits-its-mistakes`, `continual-learning-open-problem-is-behaviour-not-knowledge`, `treat-continual-learning-as-representational-form-coevolution`, and `only-explicit-retention-is-durable-writable-and-addressable`. `deploy-time-learning-is-the-missing-middle`, `llm-learning-phases-fall-between-human-learning-modes`, and `in-context-learning-presupposes-context-engineering` were evaluated but did not add a distinct reader path beyond that set.
- The source descriptions scan, refined with `rg -i 'continual|in-context|model weights|parametric|self-modif|memory consolidation|learning how to learn|optimizer|test-time|adaptive'`, surfaced the prior Sleep, token-space continual-learning, Transformers-as-gradient-descent, Co-Harness, MIA, and self-evolving-agent ingests. The first three survived articulation testing; the others concern different update inputs or system boundaries.
- Reference descriptions produced only Commonplace-specific ablation and behavioral-authority proposals. Agent-memory descriptions produced trace-learning systems and a historical reward-gated self-modifier. Agentic-system descriptions produced harness-level self-modification systems. These were evaluated and rejected below rather than forced into source-level comparisons.

**Body search:**
- `rg -n -i "fixed decomposition|effective update space|ablation" kb/notes/ --glob '*.md'` -- kept the fixed-decomposition note because Hope's ablations vary DGD, momentum, weight decay, CMS, projections, level count, and frequency while leaving the overall NSAM/CMS partition and weight-only update substrate outside the tested choices.
- `rg -n -i "distributed-parametric|continual learning|in-context learning" kb/notes/ --glob '*.md'` -- kept the continual-learning, representational-coevolution, and explicit-retention notes; rejected generic context-engineering hits that do not bear on the paper's retained state.
- `rg -n -i "continuum memory system|multi.?timescale|memory consolidation|sleep-time" kb/sources/ --glob '*.ingest.md'` -- kept the Sleep ingest as the same authors' offline continuation of Hope/CMS and the token-space ingest as a competing retention substrate.
- `rg -n -i "in-context.*gradient descent|gradient descent.*in-context|token space|representational.form" kb/sources/ --glob '*.ingest.md'` -- kept the Transformers/gradient-descent ingest because it supplies a narrower mechanistic claim and explicit boundary conditions for the target's broader ICL-as-nested-learning account.
- `rg -n -i "continual learning|model weights|parametric|weight-learning|self-modif" kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i "continual learning|model weights|parametric|self-modif|memory consolidation" kb/agentic-systems/ --glob '*.md'`, and `rg -n -i "continual learning|model weights|parametric|fixed decomposition|ablation" kb/reference/ --glob '*.md'` -- found no candidate with a more specific reader benefit than the note/source links retained here.

**Link following:**
- Followed `treat-continual-learning-as-representational-form-coevolution.md` one hop to `continual-learning-open-problem-is-behaviour-not-knowledge.md`, `deploy-time-learning-is-the-missing-middle.md`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, and the Co-Harness ingest. The first note is the strongest landing for Hope as a distributed-parametric behavior-change case; coevolution supplies the useful contrast; the other two would duplicate that route.
- Followed `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` to the decomposition-transfer and ablation-bounds notes. They confirm that the target's local ablations cannot validate adjacent fixed choices, but the fixed-decomposition note already packages that reader need.
- Followed the Sleep ingest to `continual-learning-in-token-space.ingest.md`, `llm-learning-phases-fall-between-human-learning-modes.md`, and the fixed-decomposition note. This established a compact comparison neighborhood: online multi-frequency weights (this source), offline upward weight consolidation (Sleep), and editable natural-language context (token space).
- Followed the Transformers/gradient-descent ingest to `in-context-learning-presupposes-context-engineering.md` and the sequence-model induction-bias source. The former covers the external context-selection layer rather than this paper's internal mechanism, while the retained source comparison directly bounds the broader mechanistic claim.

## Connections Found

Recommendations for the future `kb/sources/nested-learning-the-illusion-of-deep-learning-architecture.ingest.md`:

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting Hope's reported gains requires separating what the experiments vary from the fixed NSAM/CMS decomposition, knowledge-transfer directions, update objectives, and distributed-parametric retention form that remain outside the effective update space.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: Hope/CMS is a concrete distributed-parametric behavior-change design, and its own conclusion preserves the branch's central limitation by saying catastrophic forgetting is reduced on tested tasks rather than solved.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **is-evidence-for**: the paper makes weights and optimizer states durable and writable at several frequencies but offers no claim-level retrieval, criticism, provenance, or selective rollback; retained behavior remains readable only through probes.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: Nested Learning adds levels and update frequencies inside the distributed-parametric form, whereas the note asks how distributed-parametric, natural-language, and symbolic improvement loops should relate; the comparison prevents timescale hierarchy from being mistaken for cross-form coevolution.
- [Ingest: Language Models Need Sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) -- **compares-with**: the later paper by overlapping authors extends Hope's online multi-frequency memory with offline upward distillation and dreaming, making online versus offline consolidation the named comparison axis rather than treating the papers as duplicate continual-learning claims.
- [Ingest: Continual Learning in Token Space](../../../../sources/continual-learning-in-token-space.ingest.md) -- **compares-with**: both reject a static train/test boundary, but Nested Learning retains adaptation in multi-timescale weights while the Letta essay makes editable natural-language context the primary durable substrate, exposing different inspection, rollback, and memory-policy costs.
- [Ingest: Transformers Learn In-Context by Gradient Descent](../../../../sources/transformers-learn-in-context-by-gradient-descent.ingest.md) -- **compares-with**: the earlier paper gives an explicit construction and controlled regression evidence for one gradient-like in-context mechanism; Nested Learning generalizes the optimizer/associative-memory framing across architectures and training levels, so the comparison supplies the narrower evidence boundary its broad ICL claim needs.

## Bidirectional Candidates

None. For this immutable snapshot, candidate note-side return links are recorded under `Reverse-edge Candidates` rather than duplicated here.

## Reverse-edge Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: Hope's ablation table is a clean worked case where local components are varied while the representation, partition, knowledge-transfer scheme, and update family around them remain fixed; the note can cite it without claiming the fixed choices failed.
- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidenced-by**: Hope operationalizes the note's distributed-parametric branch during continual use and reports both gains and continuing catastrophic-forgetting limits.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) → source -- **evidenced-by**: frequency-ordered neural memories and optimizer states supply a current example of durable writable tacit retention whose individual commitments remain non-addressable.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None. Every evaluated candidate has frontmatter.

## Rejected Candidates

- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- Hope is relevant to the note's acknowledged deployment-pace parametric cell, but the target does not evaluate a deployed system operating across real sessions; the continual-learning and coevolution notes state the connection more precisely.
- [LLM learning phases fall between human learning modes rather than mapping onto them](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) -- the neuroscience analogy creates tension, but the target's empirical results test engineered frequency/update mechanisms rather than the brain mapping; no separate link is needed after the representational-form comparison.
- [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) -- covers the external selection and organization of context; the target analyzes internal adaptation once token or gradient context is already available, and the Transformers/gradient-descent source provides the sharper peer comparison.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- matched on distributed-parametric promotion, but Hope learns from tokens and gradients rather than agent traces and does not implement the surveyed memory-ingestion lifecycle.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) -- both use self-modification language, but Schmidhuber's system is a reward-gated policy over explicit modification choices; Nested Learning is a neural architecture/optimizer decomposition without that promotion gate.
- [Exo](../../../../agentic-systems/reviews/exo.md) and [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- matched on self-modification and dream-cycle vocabulary, but their operative targets are versioned harness code, prompts, skills, and control surfaces; they are not peer neural-memory architectures, and the coevolution note already carries the meaningful substrate contrast.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- shares the causal-evaluation concern, but it is a Commonplace-specific proposal for measuring useful and warranted knowledge work, not a target whose use is clarified by this ML experiment.
- [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) and [Ingest: Memory Intelligence Agent](../../../../sources/memory-intelligence-agent.ingest.md) -- both include weight updates, but their distinctive claims concern cross-form harness/weight coevolution and trajectory-derived planner memory; neither is as close a comparison as Sleep, token-space learning, or mechanistic ICL.

## Index Membership

None. `kb/sources/README.md` describes the snapshot/ingest structure rather than enumerating sources, and the note tag READMEs do not index source snapshots.

## Synthesis Opportunities

None. The apparent synthesis -- update cadence and representational form are independent axes -- is already stated by the representational-form coevolution and deploy-time-learning cluster; this source supplies another worked parametric case rather than a missing higher-order claim.

## Maintenance Observations

- **Vocabulary collision:** the paper defines any input-caused neural update as “memory” and calls architectures and optimizers associative memories. In this KB, agent memory also includes explicit retained artifacts with retrieval, activation, authority, lineage, and lifecycle operations. The future ingest should scope the paper's “memory” as distributed-parametric state and optimizer state so it does not silently imply artifact-level addressability.

## Flags

- **Experimental-scope flag:** the paper's broad benchmark and ablation suite supports the compound Hope/CMS design and the specific coordinates varied. It does not by itself validate the universal Nested Learning decomposition, the claim that modern architectures and optimizers are best understood as NSAMs, or adjacent fixed choices such as the memory partition and knowledge-transfer direction.
- **Not a split candidate:** the source makes several technical assertions, but the durable KB connections converge on one continual-learning/representational-form cluster rather than five or more notes across three independent topic areas.
