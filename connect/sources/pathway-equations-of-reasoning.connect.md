---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/pathway-equations-of-reasoning.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: The Equations of Reasoning

**Source:** [The Equations of Reasoning](../../../../sources/.snapshots/pathway-equations-of-reasoning.md)

The source is an immutable snapshot. No tracked ingest (`kb/sources/pathway-equations-of-reasoning.ingest.md`) existed when this report was written, so every candidate below is for the future ingest's authored connection surface. Per the sources contract, durable links must target that ingest, never the snapshot.

Source reading: a Pathway research-blog essay (2026-08-06) arguing that AI lacks an "axiomatics", meaning local microscopic rules from which macroscopic reasoning behaviour can be derived, in the manner of statistical mechanics and Hilbert's sixth problem. It presents the BDH paper's "Equations of Reasoning" (Hebbian and modus-ponens neuron-synapse dynamics, with a proven simulation chain attention -> BDH-GPU -> local dynamics) as that axiomatics. It claims this enables extrapolation beyond benchmark-tested regimes and "safety as a design property": restricting deployment to regimes where memory dominance, error amplification, and sparsity collapse stay bounded. The formal result it cites is an expressiveness and simulation reduction. The extrapolation and safety claims are programmatic; the essay derives no macroscopic law or stability bound.

## Discovery Trace

**Contract and setup:**
- Read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: notes, agent-memory-systems, agentic-systems, sources, reference (see-also only), and external. Excluded destinations: `kb/work/` and `kb/instructions/`. `kb/tags/` is named as a scan surface, but no label row authorises it as a destination.
- Sources do not participate in tags (`kb/tags/COLLECTION.md` participating: notes, reference, instructions, agent-memory-systems, agentic-systems). The snapshot has no `tags:`, so no tag-head pass was keyed from the source.

**Title listing and description scans:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, then filtered by `grep -i -E 'reach|benchmark|evaluat|extrapol|test|predict|explan|mechanism|theory|law|formal|oracle|safety|warrant|scal|bitter|param|weight|memory|induct|verif|first.princ|deriv'`. Flagged: first-principles/explanatory-reach, reach-assessment, causal-and-proof routes, world models, warranted autonomy, opacity scale threshold, bitter-lesson-unearned-reach, derivation-and-inheritance, known-target benchmarks, fixed-client benchmark, scaling-absorbs-scaffolding, and retained-theories sample efficiency.
- `rg -m1 '^description:'` over flagged sources: nested-learning, induction-bias (Ebrahimi), einstein-brownian-motion-1905, einstein-heuristic-light, world-models-life-mind-continuity, when-is-it-better-to-think-without-words, superarc, towards-a-science-of-scaling-agent-systems, and towards-faithfully-interpretable-nlp-systems.
- Tag heads read for descriptions: continual-learning (complete: true, scoped to learning *outside* weights), computational-model, learning-theory (complete: true), and evaluation.

**Body search:**
- `rg -il 'BDH|dragon hatchling|pathway\.com|hebbian|fast.weight' kb` (excluding work) found `pathway-beyond-transformers-sudoku-bench.ingest.md` (same vendor, same model), `superarc-...ingest.md` (cites the Sudoku post only), and `recursive-self-improvement-since-1987.ingest.md` (false hit on "pathways").
- `rg -n -i 'axiomat|hilbert|statistical mechanics|thermodynamic|carnot|micro-?foundation|phenomenolog'` over notes, sources, agent-memory-systems, agentic-systems, and reference found `definitions/reach-assessment.md` ("Proof reaches only across its axiomatized domain; observed predictive fit reaches only across the tested shift class"), `formal-systems-assess-explanatory-reach-through-causal-and-proof.md`, `theory-and-methodology-form-a-two-layer-execution-system.md` (a physics effective-theory analogy), `goedel-machines-schmidhuber.ingest.md`, the two Einstein ingests, and a Zikkaron review hit on "thermodynamic" (a neuroscience-vocabulary memory system).
- `rg -l -i 'state.space model|\bSSM\b|linear attention|test-time (training|learning)|titans|atlas|in-weight|synaptic|neuroscien|spiking'` found nested-learning, induction-bias, world-models editorial, and several agent-memory reviews (synapptic, Zikkaron, atlas, beever-atlas). The agent-memory hits are name or vocabulary collisions, not model-internal dynamics.
- `rg -n -i 'benchmark|scaling law|beyond the (tested|benchmark)|extrapolat' kb/notes -l` confirmed the benchmark-limit cluster (known-target, fixed-client, compounding-is-tested-later).

**Link following:**
- `first-principles-reasoning...` -> `definitions/reach-assessment.md` -> `formal-systems-assess-explanatory-reach...` -> `warranted-autonomy-is-bounded-by-oracle-domain.md` and `goedel-machines-...`. This chain is the KB's account of what proof and derivation license beyond tested cases. It is where the source's central claim lands.
- `formal-systems...` -> `derivation-and-inheritance-give-starting-warrant-earns-scope.md` (proof earns scope only within its formal domain; inheritance gives conditional starting warrant).
- The Sudoku ingest -> induction-bias and superarc form the "architectural limits" cluster. It was evaluated and judged not to be the landing site for this essay, which makes no benchmark-limit claim.

## Connections Found

External:
- [The Equations of Reasoning (Pathway)](https://pathway.com/research/the-equations-of-reasoning) -- **derived-from**: the ingest analysis is worked out from this original essay.
- [BDH paper (arXiv 2509.26507)](https://arxiv.org/pdf/2509.26507) -- **see-also**: the formal reduction and proofs (Table 1; Appendices A, C.1, C.3, C.4) that the essay only summarises. Any claim about what is actually proved should be checked there, not in the blog.

Notes:
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **compares-with** on the axis *what a derivation from formal rules licenses beyond tested cases*: the essay is a proof-route programme for ML architectures. Its proved content (attention is simulable by local dynamics within complexity bounds) is an expressiveness result. The extrapolation and safety claims would additionally need the note's formalization boundary, the correspondence between the axiomatized dynamics and deployed behaviour, which the essay does not address.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **is-evidence-for**: an independent ML-research restatement of the fit-versus-explanation polarity. The essay calls benchmarks, scaling laws, and interpretability findings "phenomenological" regularities and asks for laws that "predict behavior outside familiar conditions". Scope: this corroborates that the polarity is live outside Commonplace. It does not support the note's claim about KB methodology.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **compares-with** on the axis *structure versus scale*: the essay argues against brute-force scaling (the "hardware lottery") and for structured, derived architecture. The note locates the lesson's force in asserted-versus-earned reach. That makes the essay a test case: its cross-scale extrapolation is currently asserted, earned only for simulation-equivalence.
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](../../../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md) -- **compares-with** on the axis *provenance of an axiom set's warrant*: BDH's axioms are chosen by inheritance from neuroscience (the brain as "existence proof") and then linked to attention by proof. The note separates the conditional starting warrant from inheritance and the formal-domain-only scope from proof, which is the distinction the ingest needs to state what the essay has and has not earned.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **compares-with** on the axis *how a warranted deployment domain is fixed*: the essay proposes fixing it by analysing dynamics ("restrict deployment to regimes where these quantities remain bounded") rather than by testing. The note's Gödel-machine limiting case shows the cost structure of proof-bounded warrant that such a programme would inherit.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) -- **defined-in** (conditional): use it only if the ingest adopts the KB's term to describe the essay's benchmark-versus-law contrast. The definition's line "observed predictive fit reaches only across the tested shift class" is the KB's statement of the essay's central complaint.
- [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) -- **compares-with** on the axis *structural affordances that delay opacity in parametric representations*: the essay claims sparse, local graph dynamics make computation "observable at [its] natural resolution". That would be a structural affordance raising the threshold at which distributed-parametric state becomes opaque. The essay asserts this without demonstration beyond a sparsity figure, so treat it as a conjecture to compare, not evidence.

Sources:
- [Einstein, Brownian motion (1905)](../../../../sources/einstein-brownian-motion-1905.ingest.md) -- **compares-with** on the axis *micro-to-macro derivation yielding a discriminating observable prediction*: Einstein's molecular-kinetic derivation produced a testable macroscopic quantity (root-mean-square displacement). Pathway invokes the same statistical-mechanics programme but has not yet produced a macroscopic law or bound that a test could refute. This is the sharpest available yardstick for the essay's analogy.
- [Pathway, Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- **compares-with** on the axis *evidence posture*: same vendor, same BDH model. The earlier post argued from a benchmark result; this essay argues that benchmarks cannot establish behaviour outside tested regimes. The pair shows the vendor using both evidential modes, and the Sudoku ingest's commercial-incentive caveats carry over.
- [Nested Learning: The Illusion of Deep Learning Architecture](../../../../sources/nested-learning-the-illusion-of-deep-learning-architecture.ingest.md) -- **compares-with** on the axis *memory as a timescale-separated part of computation*: both recast memory as update dynamics at different frequencies inside the model (NL's nested associative memories; BDH's fast synaptic state over a slow trained graph). Neither treats memory as a separate module, and both argue from within weight-level architecture.

## Bidirectional Candidates

- [Pathway, Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) <-> source -- **compares-with**: the Sudoku ingest lists "BDH architecture is completely undisclosed" as a limitation. This essay and the BDH paper it cites partly discharge that limitation, so a return link would update a reader of the older ingest.
- [Einstein, Brownian motion (1905)](../../../../sources/einstein-brownian-motion-1905.ingest.md) <-> source -- **compares-with**: optional return path. The Einstein ingest is framed as a historical comparison for discriminating predictions, and this essay is a modern case that invokes the same programme without the prediction.

## Reverse-edge Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -> future ingest -- **evidenced-by** (notes contract): a contemporary ML-architecture instance of the proof route that illustrates the formalization boundary. The proof covers simulation-equivalence; the extrapolation claims fall outside it. Author this only once the ingest states that reading explicitly.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -> future ingest -- **evidenced-by**: an explicit anti-scaling, pro-derivation position whose reach claims are programmatic. It is a live case for the note's historical-prediction section. Weak until BDH's cross-scale claims are tested one way or the other.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) -- shares only the thermodynamics-over-statistical-mechanics analogy. The note uses it for effective versus fundamental theory layers, not for micro-to-macro derivation. Keyword match.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) -- the essay's route is formal derivation, not learned prediction. The formal-systems note already carries the comparison.
- [Known-target discovery benchmarks show reachability, not discovery](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) and [A benchmark that holds the client fixed exports the least-warrantable decisions](../../../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) -- both analyse specific benchmark constructions. The essay's complaint concerns finite-regime coverage generally, which reach-assessment states more directly.
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- concerns external scaffolding around a model. The essay concerns model-internal architecture.
- [Induction bias in sequence models (Ebrahimi 2026)](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) and [SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) -- the architectural-limits cluster reached through the Sudoku ingest. This essay makes no empirical capability-limit claim, so the link belongs to the Sudoku ingest.
- [Einstein, heuristic viewpoint on light](../../../../sources/einstein-heuristic-light-emission-transformation.ingest.md) -- an entropy-analogy-to-prediction case. Brownian motion is the closer micro-to-macro derivation; including both would duplicate the comparison.
- [Towards a science of scaling agent systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- shares the "science of scaling" phrase but studies multi-agent coordination. Keyword match.
- agent-memory-systems reviews (Zikkaron, synapptic, atlas, beever-atlas) -- neuroscience-vocabulary or name collisions. They are agent-level memory systems, not model-internal dynamics.
- [continual-learning tag head](../../../../tags/continual-learning-README.md) -- scoped to learning outside model weights. The essay's continual adaptation is in-weight. The tag head is also not an authorised destination for sources.

## Index Membership

None. Sources do not participate in tags, and `kb/sources/README.md` is a collection landing without per-source curation.

## Synthesis Opportunities

The reach-assessment chain (definition, formal-systems note, derivation-and-inheritance) combined with the Einstein Brownian-motion ingest and this essay implies a candidate claim: *a micro-to-macro axiomatics earns explanatory-reach only when the derivation yields a macroscopic quantity a test could refute; a simulation or expressiveness proof establishes representational equivalence, not behavioural bounds.* This would fold into the formal-systems note as a bounded qualification (per the KB's fold-don't-spawn preference) rather than become a new note, unless a second ML-axiomatics source appears.

## Maintenance Observations

- No tracked ingest exists for this snapshot. Until one is written, `commonplace-validate kb/sources` will likely warn that the snapshot has no matching ingest.

## Flags

- Tension to record in the ingest, not resolve here: the same vendor argues from benchmarks (Sudoku post) and against benchmark sufficiency (this essay).
- Evidence caveat: the essay's formal claims are secondhand summaries of the BDH paper, and its equation symbols were lost in capture (Trafilatura dropped the math). Claims about exactly what is proved need the arXiv paper.
