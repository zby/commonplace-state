---
description: "Discovery report for possible KB connections from Tom Zahavy's position paper on abductive scientific invention"
type: kb/cache/types/connect-report.md
source: kb/sources/llms-cant-jump.md
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: LLMs can’t jump

**Source:** [LLMs can’t jump](../../../sources/llms-cant-jump.md)

## Discovery Trace

**Description listing scan:**

- Read the curated heads for `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. The source has no `tags`, so no matching tag-README was required; the discovery and learning-theory heads were read because the title/description scan placed the paper in that cluster.
- Generated each authorized destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, then screened it with `rg -i 'discover|abduct|induct|deduct|world model|explan|first.princip|hypothes|experiment|simulation|ground|compression|causal|conject|axiom|theory|novel|invention|search'`. This kept the discovery-lifecycle, fixed-decomposition, proposal-selection, formal-symbolic, world-model, and automation-boundary notes; it found no reference artifact whose shipped-system subject matched the paper.
- Enumerated descriptions with `rg '^description:' kb/<destination>/ --glob '*.md'`, screened by the same concept family. In `kb/sources/`, this surfaced the Model Discovery Agent, DiscoverPhysics, FALSIFYBENCH, self-revising discovery, hyperpolation, V-JEPA 2, and weakest-hypothesis reports. In `kb/agent-memory-systems/`, it surfaced AriGraph and several trace-learning systems only through the overloaded phrase “world model”; their retained semantic/task-state graphs are not the physically grounded simulators at issue here.
- The supplied external target was evaluated under the authorized `external` destination. It is already preserved in the snapshot's `source` field and should remain the matching ingest report's `derived-from` provenance; no open-web prospecting was performed.

**Topic indexes:**

- [Discovery](../../../../tags/discovery-README.md) (`complete: true`) supplied the lifecycle, known-target, explanatory-reach, and oracle cluster. Because the source itself carries no `discovery` tag, no by-tag `rg` was due; the complete mark was nevertheless treated as authoritative for the curated discovery neighborhood.
- [Learning theory](../../../../tags/learning-theory-README.md) routed into discovery through its `covered_by` children. [Computational model](../../../../tags/computational-model-README.md) yielded the formal/parametric representation split, while [Evaluation](../../../../tags/evaluation-README.md) added no candidate beyond the experiment and oracle notes already surfaced.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) and [Agentic Systems](../../../../agentic-systems/README.md) were checked as authorized destinations. Neither collection has a system analysis whose subject is the paper's proposed sensory-to-axiom mechanism.

**Body search:**

- `rg -n -i 'abduct|abduction|induction|deduction' kb/notes/ --glob '*.md'` — kept [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md); rejected [claim modality](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md), which classifies refutation modes rather than hypothesis generation.
- `rg -n -i 'scientific discovery|discovery lifecycle|open-ended discovery|known-target|hypothesis (generation|construction|proposal)|conjecture' kb/notes/ --glob '*.md'` — kept the known-target and proposal-selection notes and exposed the search-versus-evaluation distinction.
- `rg -n -i 'world model|action-conditioned|counterfactual|intervention|simulation|sensory|embodied|physical prior|symbol grounding' kb/notes/ --glob '*.md'` — kept the world-model and formal-symbolic notes; it also showed that the source uses world models for candidate generation, while the existing world-model note uses them for reach-assessment.
- `rg -n -i 'compression|minimum description|\bMDL\b|explanatory-reach|adaptive fit' kb/notes/ --glob '*.md'` and `rg -n -i 'axiom|premise generation|generate.{0,20}premise|grounding' kb/notes/ --glob '*.md'` — kept the fixed-decomposition and automation-boundary candidates; first-principles and theory-mediated-learning hits were rejected as weaker transfers from one disputed historical reconstruction.
- `rg -n -i 'abduct|scientific discovery|world model|sensory grounding|embodied|creativity as compression|minimum description|axiom' kb/reference/ --glob '*.md'` — only [source adoption policy](../../../../reference/source-adoption-policy.md) and incidental formal-axiom text matched. The policy is about how Commonplace adopts cognitive analogies, not about scientific invention, so no reference connection was retained.
- The same query over `kb/agent-memory-systems/` found AriGraph, Playground, and trace-learning summaries; all were rejected because “world model” means retained semantic or task state there, not action-controllable physical simulation. Over `kb/agentic-systems/`, it found Eigenius only through verification under supplied axioms; the general theoretical connection is already captured more cleanly by the formal-symbolic note.
- `rg -n -i 'abduct|abduction|induction|deduction' kb/sources/ --glob '*.md'`, `rg -n -i 'scientific discovery|open-ended discovery|model discovery|known-target|insight anticipation|hypothesis (generation|construction|proposal)' kb/sources/ --glob '*.md'`, `rg -n -i 'world model|action-conditioned|counterfactual|interactive simulation|embodied|sensory grounding|symbol grounding|physical prior' kb/sources/ --glob '*.md'`, and `rg -n -i 'creativity as compression|compression progress|minimum description|\bMDL\b|off-subspace|hyperpolat' kb/sources/ --glob '*.md'` — retained the seven source comparisons below and rejected generic induction-bias, memory-compression, and causal-discovery hits whose mechanisms did not bear on novel scientific axiom formation.

**Link following:**

- Followed [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) to recognition, consequence derivation, testing, and its Peircean source boundary. Zahavy supplies a worked historical application of the same abduction → deduction → test partition, but not evidence that the KB's six phases are exhaustive.
- Followed [known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) through GIANTS and FALSIFYBENCH. This confirmed the paper's useful boundary: supplying the target axiom or rule turns the task into downstream reachability, while it does not establish prospective axiom invention.
- Followed [a proposal-selection improvement loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) to the fixed-decomposition note. The paper's strongest KB-level contribution is a proposed instance of their shared limitation: a verifier cannot choose an axiom that the effective search/update space cannot express.
- Followed [world models assess explanatory-reach](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) to V-JEPA 2 and the formal-symbolic route. This revealed a useful role distinction rather than simple support: the existing note uses interventions to assess a retained model's reach; Zahavy proposes interactive simulation to generate candidate premises.
- Followed the Model Discovery Agent report to DiscoverPhysics, FALSIFYBENCH, and agentic automata learning. MDA is the sharpest comparison because it does generate mechanistic hypotheses, but within supplied domain grammars, likelihoods, intervention spaces, and simulators.

## Connections Found

- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **is-evidence-for**: the paper applies a Peircean abduction → deduction → empirical-test cycle to Einstein's development of general relativity, giving the lifecycle a scientific-invention case while leaving the KB-specific acceptance and integration phases untouched.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **is-evidence-for**: the paper's distinction between deriving consequences from supplied axioms and generating the axioms themselves supports the note's warning that recovering a known target does not close the prospective discovery loop.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: its central claim is a scientific-invention instance of “evaluation cannot select a candidate that search never reaches”: formal deduction may be strong while the premise-generating search remains absent.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **is-evidence-for**: Zahavy argues that symbolic search over inherited concepts and axioms cannot repair a missing sensory-grounded representation, an instance of a required correction lying outside an effective hypothesis/update space.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — **is-evidence-for**: the paper independently marks the same formalization boundary—proof can unfold consequences from axioms but does not establish that the axioms were generated from or faithfully ground physical experience.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — **compares-with**: both require action-conditioned counterfactual prediction, but the note uses it to assess an existing commitment's reach whereas Zahavy proposes it as the substrate for generating new physical premises.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **compares-with**: Zahavy proposes a generation-side boundary—no abductive candidate enters consideration—even when downstream deduction and verification are available, directly testing the note's “typically oracle construction” qualification.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) — **compares-with**: the note finds candidate generation cheap for cross-note natural-language synthesis; Zahavy restricts the harder claim to premise invention without symbolic precedent or a data gradient, clarifying that the binding function depends on the kind of novelty sought.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: MDA assigns mechanistic hypothesis proposal to an LLM and Bayesian machinery to selection, but fixes domain grammars, likelihoods, intervention spaces, and simulators; it is the closest implemented challenge to Zahavy and also exhibits the fixed-representation boundary his argument targets.
- [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — **compares-with**: agents actively experiment in counterfactual physical worlds and sometimes recover novel laws, while failures concentrate on latent structure; this is direct empirical pressure on the categorical “can’t jump” claim without reaching unconstrained real-world axiom invention.
- [FALSIFYBENCH](../../../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) — **compares-with**: LLMs do form and revise hypotheses from sparse interactive evidence when the hidden-rule space and oracle are controlled, locating a bounded capability below the paper's stronger sensory-grounded abduction target.
- [Self-Revising Discovery Systems for Science](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) — **compares-with**: it defines discovery as a verified change to the admissible artifact schema, while Zahavy defines the missing jump as generating physical axioms from simulated experience; both put novelty beyond search in a fixed schema but propose different mechanisms for crossing it.
- [Interpolation, Extrapolation, Hyperpolation](../../../../sources/interpolation-extrapolation-hyperpolation.ingest.md) — **compares-with**: hyperpolation offers a geometric account of novelty outside the data's represented subspace, while Zahavy offers an embodied-abductive account of how a scientist reaches a new representational dimension.
- [Meta V-JEPA 2 action-conditioned world model](../../../../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md) — **compares-with**: V-JEPA 2 is a concrete action-conditioned latent predictor of the kind Zahavy proposes, but its short-horizon robot control evidence falls far short of showing premise or axiom invention.
- [The Optimal Choice of Hypothesis Is the Weakest, Not the Shortest](../../../../sources/optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md) — **compares-with**: both challenge compression as a sufficient account of intelligent generalization; Bennett supplies a formal induction-side rival to MDL inside a fixed language, while Zahavy argues that compression cannot explain abductive invention of the language's premises.

## Bidirectional Candidates

- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) <-> source — **evidenced-by**: the note would gain a bounded scientific case for its abduction/consequence/test core; the ingest surface should in turn locate the paper in the lifecycle vocabulary.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) <-> source — **evidenced-by**: the paper gives a premise-level explanation for why supplying a target turns discovery into downstream reachability.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) <-> source — **evidenced-by**: the scientific-invention case makes search-range failure vivid even when deductive evaluation is strong.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) <-> source — **evidenced-by**: Zahavy's proposed missing sensory-to-symbol mapping is a candidate hypothesis-class/information omission outside text-only learning.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) <-> source — **evidenced-by**: the paper sharply separates valid deduction from the unverified translation that establishes the premises.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) <-> source — **evidenced-by**: add it as a position-paper challenge showing that candidate generation can be the first binding function even when a downstream verifier exists.

## Reverse-edge Candidates

- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) → source — **evidenced-by**: cite the snapshot as a modern worked application of the Peircean core, explicitly not as validation of the full six-phase KB construction.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source — **evidenced-by**: cite the supplied-axioms versus axiom-generation distinction as conceptual support for the benchmark boundary.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source — **evidenced-by**: cite the paper as a scientific-invention case where search range, not evaluator strength, is alleged to bind.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source — **evidenced-by**: cite the text-only-to-physical-axiom gap as a proposed example, preserving that the impossibility conclusion is argued rather than experimentally demonstrated.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → source — **evidenced-by**: cite the paper's deduction/grounding split as an independent formulation of the formalization boundary.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source — **evidenced-by**: cite it in Caveats as a direct generation-boundary challenge rather than as corroboration of the title-level claim.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — the Einstein reconstruction is suggestive of explanation preceding data fit, but the paper's author disclaims historical expertise and the single retrospective case cannot bear the note's transferable KB-design claim.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — scarce observations in the Einstein narrative are not a controlled shift, a retained-theory comparison, or a sample-efficiency measurement.
- [Claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) — shared deduction/induction/abduction vocabulary is insufficient: that note classifies how claims are refuted, while this source concerns how explanatory premises are generated.
- [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) — its backcast insight reconstruction is already connected through the known-target note; a direct source-to-source edge would duplicate that more discriminating route.
- [SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — it measures recursive algorithmic compression in single-turn sequence programs, not whether compression can generate scientific axioms from sparse physical evidence.
- [When is it better to think without words?](../../../../sources/when-is-it-better-to-think-without-words.ingest.md) — the shared appeal to Einstein and non-verbal human thought is adjacent, but the essay provides no evidence that wordlessness is embodied abduction or transfers to AI architecture.
- [Source adoption policy](../../../../reference/source-adoption-policy.md) — its mention of humans as embodied explains Commonplace's caution about cognitive analogies; it does not describe the paper's discovery mechanism or a shipped-system dependency.
- [AriGraph](../../../../agent-memory-systems/reviews/AriGraph.md) — its “world model” is a task-local knowledge graph assembled from text-game observations, not the physically consistent, action-controllable simulator the source proposes.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — it verifies proof terms under supplied axioms and therefore exemplifies the downstream side only; the theoretical formal-symbolic note is the more useful target for the source's claim.

## Index Membership

None. The snapshot should remain discoverable through its matching ingest analysis and evidence edges rather than being inserted directly into a note tag index or a system roster.

## Synthesis Opportunities

- Zahavy, [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md), [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), and [Self-Revising Discovery Systems](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) jointly sharpen an existing distinction: hypothesis search inside a supplied representation and invention of the representation itself are separate capability boundaries. This should first be evaluated as an extension or worked case for [learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), not assumed to require a new note.
- Read with [the boundary of automation](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) and [the proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), the source suggests a task-relative bottleneck rule: verification limits selection only after search can express a candidate. The proposal-selection note already states the components' independence; the automation-boundary note may need this generation-first case in its Caveats.

## Maintenance Observations

- [Model Discovery Agent](../../../sources/model-discovery-agent-bayesian-experiment-design.md) cites this paper only through a generic `https://openreview.net/` reference. The new canonical snapshot provides a resolvable local target and source URL for any future citation repair.
- The paper uses “abduction” both for Peirce's Rule + Result → Case pattern and for generation of a novel rule or axiom. [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) uses it more broadly for any ampliative conjecture. Future authoring should state which sense is intended rather than treating the labels as definitionally identical.

## Flags

- The categorical wording “structurally incapable” is a position-paper conclusion supported by one retrospective historical reconstruction, not a controlled impossibility result. Connections should preserve it as a proposed generation-side boundary.
- DiscoverPhysics, FALSIFYBENCH, and MDA are important pressure against a blanket reading of “LLMs can’t abduct,” but their supplied simulators, target rules, hypothesis languages, and oracles do not directly test Zahavy's stronger claim about inventing physical axioms without symbolic precedent.
