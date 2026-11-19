---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/pathway-equations-of-reasoning.ingest.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: Ingest: The Equations of Reasoning (Pathway)

**Source:** [Ingest: The Equations of Reasoning (Pathway)](../../../../sources/pathway-equations-of-reasoning.ingest.md)

The ingest already carries a dense inline connection surface (13 links, all verified to exist). This report lists only candidates the ingest does not yet carry, plus labels for the existing inline links where a footer would sharpen them.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: notes, reference, agent-memory-systems, agentic-systems, tags, sources, and `external` (only `derived-from` and `see-also`). Excluded: `kb/work/`, `kb/instructions/`. The authorised labels are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and `see-also`, each with its authorised destinations. External prospecting was skipped under the skill rule. The ingest already names the BDH arXiv paper inline.

**Existing links verified (all exist):** formal-systems-assess-explanatory-reach-through-causal-and-proof, definitions/reach-assessment, derivation-and-inheritance-give-starting-warrant-earns-scope, bitter-lesson-selects-against-unearned-reach-not-against-structure, warranted-autonomy-is-bounded-by-oracle-domain, first-principles-reasoning-selects-for-explanatory-reach-over, definitions/representational-form, opacity-is-a-scale-threshold, learning-inside-a-fixed-decomposition-inherits-its-mistakes, and the sources einstein-brownian-motion-1905, pathway-beyond-transformers-sudoku-bench, and nested-learning-the-illusion-of-deep-learning-architecture.

**Curated heads:** The source has no `tags:`, only `domains:`, so no tag heads are keyed to it. `kb/tags/COLLECTION.md` participating set is `[notes, reference, instructions, agent-memory-systems, agentic-systems]`. Sources do not participate, so tag heads are not a destination for ingest membership. I skimmed `kb/tags/continual-learning-README.md`, which is `complete: true`. It scopes learning outside weights and so does not fit the source.

**Titles listing (notes):**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i 'reach|proof|formal|deriv|simulat|equivalen|benchmark|scal|axiom|extrapolat|phenomen|fit|safety|parametric|weight|in-context|hebb|memory|continual|opacity|interpret|bitter|oracle|test'`. Flagged:
  - world-models-assess-explanatory-reach-through-action-conditioned
  - goedel-machines-are-a-proof-governed-case-of-self-modification
  - evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs
  - the-bitter-lesson-selects-production-methods-not-representational
  - weight-resident-methodologies-compress-behavior-in-context
  - treat-continual-learning-as-representational-form-coevolution
  - continual-learning-requires-governing-behaviour-changing-writes
  - scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier
  - system-use-provides-evidence-of-theory-fit-not-independent-warrant
  - known-target-discovery-benchmarks-show-reachability-not-discovery
- I read the descriptions of all ten flagged titles, using `rg -N '^description:'` on each.

**Body search:**
- `rg -il 'hebbian|fast weights?|statistical mechanics|dragon hatchling|\bBDH\b|pathway\.com|in-weight|test-time training|titans|state[- ]space model' kb/` (excluding work, reports, sutskevers-list). Hits: recursive-self-improvement-since-1987.ingest (fast weights), superarc-ait-benchmark ingest (mentions BDM, not BDH; a false hit), nested-learning ingest (already linked), pathway-beyond-transformers (already linked), and theory-and-methodology-form-a-two-layer-execution-system (a generic hit that does not bear on the source).
- `rg -il 'phenomenolog|hilbert|carnot|simulation equivalen|expressiv(e|ity) (result|proof|equivalence)'`. Hits: the-geometry-of-forgetting.ingest ("phenomenology" in a reproduce-vs-explain caveat) and adam-mastroianni-infinite-midwit.ingest (generic use of "phenomenology").
- An earlier `rg -il 'pathway'` returned many generic "pathway" hits. I discarded it and narrowed the query to `pathway\.com`.
- `rg -n -i 'locali[sz]ed|sparse|interpretab'` over the-bitter-lesson-selects-production-methods-not-representational and opacity-is-a-scale-threshold. Found line 73 of the bitter-lesson note, which says a learned architecture with "stable semantic modules, explicit scope, and localized update paths" would confirm the mixed-form conjecture in a different substrate. BDH claims to be close to that.
- `rg -n -i 'weight|locali' kb/notes/definitions/theory-builder.md`. Found the "Content located in weights" boundary case at lines 208-213. The ingest paraphrases this case without linking it.
- `rg -n -i 'fast weight|episode'` in the recursive-self-improvement-since-1987 ingest, line 45: "episode-local adaptation does not establish retention across episodes". This is the same point the ingest makes about BDH's fast synaptic state.
- In-search-of-lost-domain-generalization ingest (read lines 2, 22, 39). DomainBed shows that the out-of-distribution advantage claimed for specialized structure vanishes under a declared model-selection protocol.

**Other destinations:**
- agent-memory-systems / agentic-systems: I searched titles with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ kb/agentic-systems/ | rg -i 'parametric|weight|neural|memory layer|continual|test-time|nested|titan|in-model'`, which returned only generic lightweight memory systems. `rg -il 'parametric memory|in-weight|weights as memory|test-time'` returned retrieval and skill memory reviews. BDH is a model architecture, not an agent memory or harness system. No candidates.
- reference: a titles grep for `reach|proof|formal|benchmark` returned ADR 055 (terminology) and ADR 090. Neither is relevant, so there are no candidates.

**Link following:**
- From formal-systems-assess-explanatory-reach-through-causal-and-proof to world-models-assess-explanatory-reach-through-action-conditioned. The world-models note restates the formalization boundary for learned predictors. It is already covered by the existing reach-assessment and formal-systems links.
- From the theory-builder definition's boundary list to the Gödel machine note, which is a proof-governed case that the definition leaves open.
- From the in-search-of-lost-domain-generalization ingest to retained-theories-may-improve-sample-efficiency. That note is a casebook on structured shifts and is not specific to this source.
- `rg -l 'pathway-beyond-transformers|einstein-brownian'`: the only artifact that links either ingest is this one (see Maintenance Observations).

## Connections Found

- [Theory builder](../../../../notes/definitions/theory-builder.md) -- **defined-in**: the ingest judges BDH condition by condition against the theory-builder definition. It also names the definition's "content located in weights" boundary in prose without linking it. A reader of that assessment needs the four conditions and the boundary case, which says whether weights meet condition 1 is an empirical question about the model and method.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **compares-with** (axis: learned localized structure inside the parametric substrate): the note states that a learned architecture with stable semantic modules, explicit scope, and localized update paths would confirm the mixed-form conjecture "in a different substrate". BDH claims sparse, local, edge-level implication state produced by learning. The comparison shows how far BDH is from that confirming case: the essay gives no interpretability evidence, so the architecture is a candidate, not a confirmation.
- [Missing rationale does not exclude a theory builder; weight-only retention excludes one across runs](../../../../notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md) -- **compares-with** (axis: whether weight-resident state contains localized units): that evidence note says of weights that "no unit in them says anything". BDH's claim that edges carry neuron-to-neuron implication strengths is the direct challenge to that premise at the architecture level. The ingest judges the challenge unargued, so the comparison shows the note's premise is untested for BDH-like architectures but not refuted.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- **compares-with** (axis: what a proof licenses relative to its formalization): the Gödel machine's rigor is relative to axioms describing the machine and environment. BDH's simulation proof likewise covers only the formal domain of the equivalence result. The ingest's central limitation is that the safety and extrapolation claims need an unproved correspondence between the axioms and deployed behaviour. The Gödel machine note gives a second, independently analysed instance of that boundary.
- [Recursive self-improvement since 1987 (Schmidhuber retrospective)](../../../../sources/recursive-self-improvement-since-1987.ingest.md) -- **compares-with** (axis: in-run fast-weight adaptation versus retention across runs): the Schmidhuber ingest states that fixed weights can implement fast-weight adaptation, and that "episode-local adaptation does not establish retention across episodes". This ingest's persistence assessment of BDH's Hebbian fast state makes the same distinction. Linking the two lets a reader see BDH as an instance of the older fast-weights lineage rather than a new mechanism.
- [In Search of Lost Domain Generalization (DomainBed)](../../../../sources/in-search-of-lost-domain-generalization.ingest.md) -- **compares-with** (axis: whether structure claimed to generalize beyond tested regimes beats a fitted baseline under a declared protocol): the essay argues that derived structure will predict beyond the benchmark regime where "phenomenological" fit cannot. DomainBed is the KB's captured case where structure-motivated out-of-distribution methods lost their advantage once tested fairly. It supplies the test the essay's extrapolation claim would have to pass and currently lacks.

**Labels for existing inline links.** The ingest's inline links already carry strong commitment. If a footer is added, these labels match the ingest's own prose:
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **is-evidence-for**: a worked, contemporary case where a proof covers simulation equivalence while the prose claims behavioural bounds.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) -- **defined-in**: the essay's complaint about tested regimes is the reach-assessment term.
- [Einstein on Brownian motion (1905)](../../../../sources/einstein-brownian-motion-1905.ingest.md) -- **compares-with** (axis: whether the micro-to-macro derivation yields a refutable macroscopic quantity).
- [Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- **compares-with** (axis: the same vendor's evidential mode, benchmark-led versus anti-benchmark).

## Bidirectional Candidates

- [Recursive self-improvement since 1987](../../../../sources/recursive-self-improvement-since-1987.ingest.md) <-> source -- **compares-with**: the Schmidhuber ingest's line-45 paragraph on fast weights has no concrete modern architecture to point at. BDH's Hebbian fast state is one. `compares-with` is authorised for sources→sources in both directions.
- [Einstein on Brownian motion (1905)](../../../../sources/einstein-brownian-motion-1905.ingest.md) <-> source -- **compares-with**: the Einstein ingest currently has no inbound links. The return path gives it a contemporary counter-case, a micro-to-macro programme that has not yet produced a refutable quantity.

## Reverse-edge Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → source -- **evidenced-by** (notes→sources, authorised in `kb/notes/COLLECTION.md`): this is the ingest's own Recommended Next Action. It is a bounded qualification of 200 words or fewer: a simulation or expressiveness proof establishes representational equivalence, not behavioural bounds, and a micro-to-macro axiomatics earns explanatory-reach only when it yields a refutable macroscopic quantity. It would cite this ingest and the Einstein ingest together. The note currently mentions neither Einstein nor simulation equivalence (`rg -n -i 'brownian|einstein|simulat|equivalen'` returned nothing).
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) → source -- **evidenced-by**: a live case of structure argued against scaling whose reach is asserted, not earned beyond simulation equivalence. This edge has lower priority than the formal-systems edge. Add it only if the note wants a contemporary ML example.
- [Theory builder](../../../../notes/definitions/theory-builder.md) → source -- **evidenced-by**, weak: the "Content located in weights" boundary case could cite BDH as an architecture that claims localized edge-level content without evidence. This is optional. The definition's boundary list works without it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) -- relevant, since it is the test-based alternative route to extrapolation. It adds nothing a reader of this ingest would not already get from the reach-assessment and formal-systems links.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) -- concerns cue-activated methodology in pretrained weights, not in-run weight adaptation.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) and [Continual learning requires governing behaviour-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- the essay does not claim the fast state persists across runs, so it does not bear on deployed continual learning.
- [Scaling absorbs scaffolding at fixed difficulty](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- keyword overlap on "scaling" only.
- [System use provides evidence of theory fit, not independent warrant](../../../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) -- a warrant distinction already better served by the derivation-and-inheritance link.
- [Known-target discovery benchmarks show reachability, not discovery](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- about discovery benchmarks, not about benchmarks versus derivation.
- [The Geometry of Forgetting](../../../../sources/the-geometry-of-forgetting.ingest.md) -- it shares a "reproducing a signature is not the uniquely correct explanation" caveat. The topic is embedding memory, so a link would confuse more than it helps.
- [SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) -- a false hit (BDM, not BDH).
- [The Infinite Midwit](../../../../sources/adam-mastroianni-infinite-midwit.ingest.md) -- a generic use of "phenomenology".
- All agent-memory-systems, agentic-systems, and reference artifacts -- BDH is a model architecture, and none of these collections holds model-architecture analyses.

## Index Membership

None. Sources do not participate in tag heads (`kb/tags/COLLECTION.md` participating set), and the ingest carries no `tags:`.

## Synthesis Opportunities

The formal-systems reach note, the Gödel machine note, and this ingest together imply a compact claim: a proof licenses behaviour only through a separately established correspondence between its formalization and the deployed system. This holds whether the proof governs admission (Gödel machine) or expressiveness (BDH). The formal-systems note's "formalization boundary" may already carry this claim. Fold it there rather than writing a new note.

## Maintenance Observations

- [Einstein on Brownian motion (1905)](../../../../sources/einstein-brownian-motion-1905.ingest.md) and [Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) have no inbound links from any note or source other than this ingest. The Einstein ingest in particular looks like intended grounding for the formal-systems reach note that has not yet been cited.

## Flags

- Tension to keep visible: the theory-builder definition and the missing-rationale evidence note both assert that no unit in weights says anything, with the definition treating this as an empirical question. BDH claims the opposite for its edges without evidence. If a later BDH interpretability result showed stateable edge content, it would qualify the evidence note's premise for that architecture class. This is not a present contradiction.
- Not a split candidate: the ingest makes one main assessment (proof scope versus claimed reach), and its theory-builder mapping is subordinate.
