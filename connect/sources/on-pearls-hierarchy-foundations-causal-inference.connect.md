---
description: "Connection discovery for Pearl's hierarchy: assumption-relative identification, action prediction, and limits of causal attribution in KB evaluation."
type: types/connect-report.md
source: kb/sources/.snapshots/on-pearls-hierarchy-foundations-causal-inference.md
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: On Pearl’s Hierarchy and the Foundations of Causal Inference

**Source:** [On Pearl’s Hierarchy and the Foundations of Causal Inference](../../../../sources/.snapshots/on-pearls-hierarchy-foundations-causal-inference.md)

Discovery-only output of `cp-skill-connect`, produced by GPT-6. The immutable snapshot was read in full. Recommendations below belong on its future authored ingest, not on the snapshot. Mathematical results concern the source's finite, recursive structural causal models; KB applications below are target-side interpretations, not tested results from the paper.

## Discovery Trace

- **Contracts and routing:** Read the source and reports collection contracts, `types/connect-report.md`, and the notes outbound rules. Sources authorize prospecting notes, reference, agent-memory systems, agentic systems, tags, and other sources. Instructions and workshops are excluded. The external source URL was already present in the snapshot; no external discovery was performed.
- **Curated surfaces:** Read `README.md` for all six permitted local destinations, plus the evaluation, discovery, and theory-builder tag heads. Discovery and theory-builder declare `complete: true`; no by-tag search was needed. The source itself has no tags. Evaluation's experiment-design cluster nominated the retained-theory intervention note. Theory-builder's formal and world-model entries nominated the main pair of candidates.
- **Title scans:** Generated fresh `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` listings for notes, reference, sources, agent-memory systems, agentic systems, and tags. Inspected title surfaces and focused subsequent reading on causal assessment and experiment interpretation. Large combined outputs were truncated; focused queries and candidate reads supplied the evidence for retained candidates. This is selective standard discovery, not exhaustive evaluation of every listed artifact.
- **Notes descriptions and body searches:** Ran `rg '^description:.*(causal|counterfactual|intervention|confound|mechanis|identif)' kb/notes/ --glob '*.md'` and `rg -n 'Pearl|counterfactual|identifiab|do-calculus' kb/notes/ --glob '*.md'`. Formal causal/proof assessment, world-model assessment, and retained-theory interventions passed. General theory-builder membership and symbolic representation were too broad to retain separately.
- **Cross-collection descriptions:** Ran `rg '^description:.*(causal|counterfactual|ablation|assumption)' kb/reference/ kb/agentic-systems/ kb/agent-memory-systems/ kb/sources/ --glob '*.md'` with a bounded displayed result. DoWhy and invariant prediction supply concrete comparisons; the ablation proposal supplies a practical companion. No direct system-characterization evidence follows from this general causal-inference paper.
- **Reference:** The title scan nominated the ablation-baselines proposal; `rg -n 'causal|counterfactual|confound' kb/reference/proposals/ablation-baselines-for-the-declared-objective.md` exposed its operator and contamination confounds. Read the proposal fully. Retained a sparse companion edge because source semantics help distinguish an observed operating configuration from an intervention on that configuration.
- **Agent-memory systems:** The README and title scan showed memory-system implementation reviews rather than causal-inference systems. `rg -n 'causal|counterfactual|confound' kb/agent-memory-systems/reviews/hindsight.md` found extracted causal links and causal recall. Rejected that hit: a relation called causal in a retrieval graph does not establish SCM semantics, intervention identification, or a useful specific comparison here.
- **Agentic systems:** Ran `rg -n 'causal|counterfactual|confound|identif' kb/agentic-systems/ --glob '*.md'`. Most hits describe evidential limits or use causal connection in the reflection sense. Eigenius was also reached from the formal-assessment note's existing links; its proof route is outside the mathematical contribution of this source. No system edge retained.
- **Sources and one-hop following:** The formal-assessment note already links DoWhy and invariant prediction; both ingests were read fully. They distinguish tool-level assumption declaration and statistical invariance testing from this paper's logical separation and graphical identification results. These two comparisons were retained. Broader source hits on scientific discovery and reflection were rejected as thematic overlap.
- **Tags:** The tag title scan and three heads provided navigation, not direct source-to-tag edges: the sources contract lists tags as a prospecting destination but supplies no tag-target relationship label. Existing formal-assessment and intervention notes already route readers into the relevant topic areas.
- **Candidate verification:** All linked local candidate paths were checked to exist. No search scores are applicable to these lexical scans.

## Connections Found

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — **is-evidence-for**: the source materially bounds the causal route. The hierarchy separates observational, interventional, and counterfactual information; causal Bayesian networks and do-calculus support identification only with supplied causal constraints. This supports the note's assumption boundary, not the broader proposition that causal formalization validates arbitrary KB theories. Source anchors: Sections 1.3–1.4, Theorem 1, Definition 17, and Theorem 5.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — **compares-with**: compare the question a predictor answers. Predicting candidate actions concerns intervention distributions when the action semantics justify that interpretation; conditioning alternative outcomes on what actually happened requires additional counterfactual information. The hierarchy helps prevent treating every imagined rollout as Layer 3 evidence. It does not assess JEPA or prove this note's reach claim.
- [A retained-theory intervention isolates one surface, not the whole program theory](../../../../notes/retained-theory-intervention-isolates-one-explicit-surface.md) — **compares-with**: compare a defined intervention with broader causal attribution. The paper's operation replaces designated mechanisms while preserving the others, and its identifiability condition asks whether compatible models agree on the target quantity. The KB note must separately justify whether its actual manipulation and controls meet those semantics; the paper does not validate that protocol.
- [DoWhy: Expressing and validating causal assumptions](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) — **compares-with**: the hierarchy paper supplies the logical and graphical basis for why assumptions are needed; DoWhy organizes modeling, identification, estimation, and partial validation as an operational pipeline. Neither identification rules nor an API make the supplied causal assumptions true.
- [Causal inference using invariant prediction](../../../../sources/causal-inference-using-invariant-prediction.ingest.md) — **compares-with**: compare generic cross-layer underdetermination with a particular assumption-relative route to causal information from multiple environments. Invariance assumptions and valid statistical tests add the knowledge that the hierarchy says cannot come from arbitrary observational fit alone; the methods are compatible rather than contradictory.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — **see-also**: a concrete KB application for separating outcome statistics under existing use from the effect of deploying or withholding a framework. Its operator-inclusion and contamination concerns identify background influences a causal interpretation must handle. This is a proposed application, not a paper-derived experimental recipe.
- [Original technical report R-60](https://causalai.net/r60.pdf) — **derived-from**: original source of the authored ingest analysis.

## Bidirectional Candidates

None. Useful note-to-source directions are specified below rather than mechanically mirrored.

## Reverse-edge Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → this source's future tracked ingest — **evidenced-by**: qualifies and bounds the causal route by distinguishing layer separation, effect identifiability, and assumption-relative graphical inference. Do not characterize this as an empirical corroboration of Commonplace's assessment practice. The authored destination must be the tracked ingest once it exists, never this local snapshot.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) → this source's future tracked ingest — **evidenced-by**: bounds the phrase “counterfactual test surface” by distinguishing prospective action prediction from cross-world attribution conditional on actual evidence. This is a terminology and claim-scope refinement, not a refutation of the note's conditional world-model claim.

## Off-authorisation Candidates

None. Tag routing was considered, but no direct tag edge offered enough value to justify a contract-extension request.

## Raw Text Candidates

None.

## Rejected Candidates

- [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md) — extracted causal relations used for recall are not enough to establish the formal causal assumptions studied here; the shared word alone is not a useful connection.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — reached through the formal-assessment note, but the review's relevant contribution is proof validity and translation fidelity. The existing note carries that comparison more precisely than a direct edge from this paper would.

## Index Membership

None. Relevant notes already sit in the evaluation and theory-builder heads. Retain this source through their specific claim-level citations rather than widening the heads with a general causal-inference reading list.

## Synthesis Opportunities

None. The existing formal-assessment, world-model, and intervention notes already own the useful distinctions; source-grounded refinements are preferable to a new umbrella note.

## Maintenance Observations

The world-model note's phrase “counterfactual test surface” can denote ordinary hypothetical action testing, while the hierarchy uses counterfactual for a stronger cross-world query. A future revision should state which meaning is intended. No library edit was made here.

## Flags

- Do not turn the Causal Hierarchy Theorem into a blanket claim that causal inference from observational data is impossible. The paper explicitly develops inference from observational data plus causal assumptions. Its measure-zero result concerns collapse of whole layers in the stated model space, not whether every individual higher-layer query is unidentifiable.
- Distinguish the paper's theorem statements from empirical prevalence claims. “Almost all” is measure-theoretic under its encoding, not a measured rate among deployed agent systems.
- The snapshot's text extraction drops diagram structure and some mathematical typography. Claims requiring exact graphical separation, subscripts, or proof details need the PDF. Several complete proofs and constructions are referred to appendices in a separate cited version; this captured chapter does not include those appendices.
- No split recommendation: retained candidates center on one topic, causal evidence and its inferential limits, even though the paper develops several mathematical results.
