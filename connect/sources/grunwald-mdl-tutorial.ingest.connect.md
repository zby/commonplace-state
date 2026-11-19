---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/grunwald-mdl-tutorial.ingest.md"
source_has_frontmatter: true
date: "2026-11-03"
depth: standard
---

# Connection Report: A Tutorial Introduction to the Minimum Description Length Principle

**Source:** [Ingest: A Tutorial Introduction to the Minimum Description Length Principle](../../../../sources/grunwald-mdl-tutorial.ingest.md)

The ingest already carries an inline `## Connections Found` prose section with ten targets (four theory, six sources). All ten paths resolve. None carries an explicit authorised label, because the sources contract allows inline links with a connective word. The candidates below add targets the ingest does not yet name, and record labels for the existing ones so that a future editor can convert them to labelled footer entries.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` § Outbound links. Destinations to prospect: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting was skipped. The only known external target is the arXiv URL, which the ingest already cites inline as its `derived-from` basis.

**Existing-link verification:** all ten inline targets exist: `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`, `information-value-is-observer-relative.md`, `epiplexity-by-example-what-entropy-and-complexity-miss.md`, `first-principles-reasoning-selects-for-explanatory-reach-over.md`, plus the source ingests for Bennett, DreamCoder (short), 08-simplicity, epiplexity, Popper and No Free Lunch.

**Topic indexes:**
- `kb/tags/learning-theory-README.md`, matching the source's `tags: [learning-theory]`. It declares `complete: true`, so the by-tag `rg` was skipped. Sources do not participate in tag membership, so the head gives routing context only. Its "Start here" and child-area lists contain no compression or MDL anchor.
- `kb/sources/README.md` exists. `rg -n -i 'learning|simplic|complex'` on it found no topical grouping where the ingest would slot.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'simpl|compress|observer|vocabular|representation|explan|hypothes|decompos|regular|noise|fit|occam|cost|bound|search|parameter|model select|length|minimal|cheap'` flagged these candidates:
  - `minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md`: kept (vocabulary-relative cost for a bounded observer)
  - `cost-sensitive-formalisms-for-tentative-theory-search.md`: rejected (search-budget formalisms, not description length)
  - `weight-resident-methodologies-compress-behavior-in-context.md`: rejected ("compression" is a context-cost metaphor)
  - `reverse-compression-is-when-llm-output-expands-without-adding.md`: rejected (informal compression; MDL does not sharpen it)
  - `ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md`: rejected (cost of error, not explanation length)
  - `addressability-grain-sets-a-matched-selective-read-floor.md`: rejected (title keyword only)

**Body search:**
- `rg -il 'MDL|minimum description length|description length|kolmogorov|two-part code|compressib|solomonoff|occam' kb/ --glob '*.md'` (excluding `kb/work/` and the cache). Theory hits: `epiplexity-by-example…` and `information-value…`, both already linked. `two-context-boundaries…` and `quality-signals…` are keyword-only hits on "description length" and were rejected. Source hits: Bennett, FunSearch, epiplexity, DreamCoder (short and full), self-revising discovery systems, generalization/holdout reuse, error-centric intelligence, Gödel machines, compression progress, Gick–Holyoak, text optimization, 08-simplicity, and the Sutskever book chapters. Agentic-system-analyses hits were incidental and lie outside the authorised destinations anyway.
- Per-hit context was checked with `rg -n -i -o '.{80}(MDL|minimum description length|description length|kolmogorov|two-part|compressib).{80}'` on each source hit. Results:
  - `self-revising-discovery-systems-agentic-ai.ingest.md` (MDL/AIC gates): kept
  - `driven-by-compression-progress.ingest.md`: kept
  - `we-should-take-text-optimization-more-seriously.ingest.md` (Kolmogorov-style prior for text updates): kept
  - `error-centric-intelligence-beyond-observational-learning.ingest.md` (hypothesis-space change; speculative alternative to description length): kept
  - `dreamcoder-wake-sleep-full-paper.ingest.md` (Bayesian/MDL objective): kept as a sibling of the already-linked short DreamCoder ingest
  - `generalization-adaptive-data-analysis-holdout-reuse.ingest.md`: rejected (description length used as an information budget on transcripts, a different use)
  - `mathematical-discoveries-program-search-large-language-models.ingest.md`: rejected (one passing remark on a low-Kolmogorov bias)
  - `goedel-machines-schmidhuber.ingest.md`: rejected (reaches MDL only through the self-revising ingest)
  - `gick-holyoak-analogical-problem-solving.ingest.md`: rejected (false positive)
- `rg -l -i 'compression|algorithmic information|simplicity prior' kb/sources kb/agentic-systems kb/agent-memory-systems --glob '*.md' -g '!**/sutskevers-list/**'`. Many hits; most use "compression" in the context-compaction sense. The hits evaluated:
  - `superarc-ait-benchmark-llm-compression-abstraction.ingest.md` (AIT/BDM benchmark): kept
  - `beyond-fixed-representations-vocabulary-verifier-gaps.ingest.md` ("primitive usefulness through amortized compression"): kept
  - `theory-refinement-analytical-empirical-methods.ingest.md` (inverse-resolution compression inside a fixed Horn hypothesis class): rejected as weaker than the theory edge already present
  - `01-what-did-ilya-see.ingest.md`: rejected, because `08-simplicity` is the chapter-level ingest already linked
  - `interpolation-extrapolation-hyperpolation.ingest.md`: rejected ("vocabulary" in a different sense)
  - Agent-memory-system and agentic-system reviews: all hits are context or memory compaction, not description-length theory. No candidate.
- `rg -n -i 'grunwald|grünwald' kb --glob '*.md' -l` matched only this ingest and `sources/sutskevers-list/full.md` (§8.3 covers the tutorial). The theory collection has no existing inbound edge.
- `herbert-simon-architecture-of-complexity.ingest.md` (an untracked ingest from the same session) was checked with `rg -n -i -o '.{80}(descri|redundan|compress).{80}'`. It quotes "how complex or simple a structure is depends critically upon the way in which we describe it". Kept.

**Reference destination:** nothing about MDL or description length. Only `see-also` is authorised, and no adjacent companion was found. Skipped.

**Link following:**
- `minimum-viable-vocabulary…` → `information-value-is-observer-relative.md` and the epiplexity prequential-coding mention. This confirms MVV sits in the same observer-relative cluster and that it names a measure ("a measure of extraction … and a fixed observer") which MDL partly supplies.
- `epiplexity-by-example…` links only the epiplexity ingest among sources. Its table goes Shannon → Kolmogorov → epiplexity, which supports the "middle rung" reverse edge.
- `learning-inside-a-fixed-decomposition…` cites ACM, Lane 1990 and co-harness among sources. It has no compression-based case, so §1.2.2 and §2.10.1 would add a formal one.
- `goedel-machines-schmidhuber.ingest.md` → `self-revising-discovery-systems…`. That ingest already treats MDL/AIC as one point on a "what licenses a self-revision" axis, so Grünwald's account of crude versus refined MDL can sharpen that comparison.

## Connections Found

Labels for the ten existing inline links, for a future footer conversion. These are not new edges:

- [learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): **is-evidence-for**. A restricted code class C is a hypothesis class fixed in advance. Grünwald says some regular sequences will always stay incompressible under it (§1.2.2), and that carving the class into models is unavoidably arbitrary (§2.10.1).
- [information value is observer-relative](../../../../theory/information-value-is-observer-relative.md): **is-evidence-for**, qualifying. In MDL, regularity is relative to the description method and noise is relative to the model (§1.5). This narrows the note's claim that classical information theory "abstracts away the observer".
- [epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md): **compares-with** on how each measure fixes the observer. Practical MDL fixes a restricted, computable code class, which sits between Kolmogorov's universal machine and epiplexity's time-bounded learner.
- [first-principles reasoning selects for explanatory-reach over adaptive fit](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md): **compares-with** on the selection criterion. MDL is the formal version of fit penalized by complexity, and it explicitly disclaims truth.
- [Bennett: optimal choice of hypothesis is the weakest, not the shortest](../../../../sources/optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md): **compares-with** on what simplicity criterion should select hypotheses. Grünwald states the baseline Bennett argues against.
- [DreamCoder wake-sleep (short)](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md): **compares-with** on library-growth scoring, which is a crude two-part code with an ad hoc L(H).
- [08 simplicity hidden in complexity](../../../../sources/08-simplicity-hidden-in-complexity.ingest.md): **compares-with** on representation dependence. Grünwald concedes the critique for crude MDL and claims refined MDL escapes it only inside a restricted class.
- [From entropy to epiplexity](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md): **compares-with** on two-part and prequential coding. Epiplexity adapts both machineries to time-bounded observers.
- [Popper, Logic of Scientific Discovery](../../../../sources/popper-logic-of-scientific-discovery.ingest.md): **compares-with** on what simplicity is. Popper ties it to falsifiability and parameter dimension, while Grünwald ties it to the ability to fit random data (Example 1.4).
- [No Free Lunch theorem](../../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md): **compares-with** on whether a simplicity preference can be justified without distributional assumptions.

New candidates:

- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md): **compares-with** on vocabulary-relative cost. MVV ranks vocabularies by how much structure a fixed observer can extract and asks for "a measure of extraction". Practical MDL makes description cost explicitly relative to a chosen code class. Grünwald's warning also applies to MVV: the ranking inherits the code choice (§1.4, §2.4.2), and comparisons across vocabularies are not code-neutral. This is the closest theory neighbour to the ingest's occasion that the ingest does not yet name.
- [Simon, The Architecture of Complexity](../../../../sources/herbert-simon-architecture-of-complexity.ingest.md): **compares-with** on representation-dependent simplicity. Simon says complexity "depends critically upon the way in which we describe it", and that compact description needs the right representation. Practical MDL formalizes the same dependence as a choice of code class C, and refined MDL removes it only inside a restricted model class. This is a same-session ingest that is not yet tracked, so check that it is committed before authoring the link.
- [Beyond fixed representations: vocabulary and verifier gaps](../../../../sources/beyond-fixed-representations-vocabulary-verifier-gaps.ingest.md): **compares-with** on scoring new primitives by compression. That paper measures primitive usefulness as amortized compression. Grünwald shows that a vocabulary-relative code is crude two-part MDL whose L(H) code is chosen, not derived. So that paper's compression score for invented primitives carries the arbitrariness §1.4 and §2.10.1 describe.
- [Self-revising discovery systems (MDL/AIC gates)](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md): **compares-with** on MDL as an acceptance gate. That paper commits regime transitions under MDL gates. Grünwald's crude/refined split says which MDL such a gate can actually compute for a novel, non-parametric interaction type: crude, with its arbitrariness.
- [DreamCoder full paper](../../../../sources/dreamcoder-wake-sleep-full-paper.ingest.md): **compares-with**, the same axis as the existing short-DreamCoder link. Its fixed-component list includes the "Bayesian/MDL objective", so the crude two-part reading applies directly. Add it only if the editor wants both DreamCoder ingests named. Otherwise replace the short link with this fuller analysis.
- [SuperARC AIT benchmark](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md): **compares-with** on computable approximations to algorithmic complexity. SuperARC scores models with CTM/BDM estimates of Kolmogorov complexity. Grünwald explains why practical MDL abandons that target for a restricted, computable code class. The comparison shows which quantity the benchmark claims to approximate.
- [Driven by compression progress](../../../../sources/driven-by-compression-progress.ingest.md): **compares-with** on compression as the learning signal. Schmidhuber treats the first derivative of compressibility under a learning compressor as interestingness. MDL is a single selection over fixed data with no carried state. This marks the static/dynamic contrast the ingest's Learning Claims section draws ("nothing … is carried into the next one except the data").
- [Error-centric intelligence beyond observational learning](../../../../sources/error-centric-intelligence-beyond-observational-learning.ingest.md): **compares-with** on what changes the hypothesis space. Thomas proposes error-driven revision of the hypothesis space and offers a speculative task-cost alternative to description length. Grünwald concedes that MDL leaves the choice of class to the modeller (§2.10.1). The two sources mark opposite answers to who revises C.

## Bidirectional Candidates

- [information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) <-> source: the note should carry an `evidenced-by` link that qualifies or bounds its claim (theory label). Its claim that Kolmogorov "deliberately abstracts away the observer" holds only through the invariance theorem in the long-sequence limit. Practical MDL is a classical-lineage counterexample at finite samples (§1.2.1, §1.5). The context phrase should say it qualifies the claim, not that it corroborates it.

## Reverse-edge Candidates

- [epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) → source: **evidenced-by** (bounds), or a body-hosted citation in the comparison table. The table jumps from Kolmogorov to epiplexity. A practical-MDL row (a restricted, computable code class) would cite this ingest as the source of that row. Note that theory sources must be cited in the body (theory COLLECTION § Source grounding).
- [learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source: **evidenced-by**. MDL is a formal case where the hypothesis class is fixed before learning and improvement is confined to it, by the method's own admission. Grünwald did not construct this to test the note, so it bounds or illustrates the claim rather than corroborating it.
- [minimum viable vocabulary…](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) → source: **evidenced-by** (qualifies). The note's testability paragraph needs "a measure of extraction … and a fixed observer". MDL supplies a vocabulary-relative measure and warns that it is code-relative, which qualifies any cross-vocabulary ranking.
- [first-principles reasoning selects for explanatory-reach over adaptive fit](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) → source: **evidenced-by** (bounds). MDL gives the adaptive-fit pole a precise form. Its justification is predictive and conditional on consistency, and it disclaims truth (§1.6).
- [self-revising discovery systems](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) and [beyond fixed representations](../../../../sources/beyond-fixed-representations-vocabulary-verifier-gaps.ingest.md) → source: **compares-with** under the same sources contract. Each uses an MDL- or compression-based criterion without distinguishing crude from refined MDL.

## Off-authorisation Candidates

None.

## Raw Text Candidates

- [Sutskever's list (full text)](../../../../sources/sutskevers-list/full.md): potential **see-also**. §8.3 summarizes this same tutorial, including the polynomial underfit/overfit figure that Grünwald authorized. It is a frontmatter-free text capture. The chapter-level ingest [08 simplicity hidden in complexity](../../../../sources/08-simplicity-hidden-in-complexity.ingest.md) is already linked and is the better authored surface.

## Rejected Candidates

- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md): prices search budgets, not description length. MDL is not one of its model families.
- [Weight-resident methodologies compress behavior in context](../../../../theory/weight-resident-methodologies-compress-behavior-in-context.md): uses "compression" for context cost. Following the link would conflate the two senses.
- [Reverse compression](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md): uses informal compression of prose. MDL would over-formalize it.
- [Generalization in adaptive data analysis](../../../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md): uses description length as an information budget on analysis transcripts, not for model selection.
- [Gödel machines](../../../../sources/goedel-machines-schmidhuber.ingest.md): reaches MDL only through the self-revising discovery ingest, which is kept instead.
- [FunSearch](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md): only a passing remark on a low-Kolmogorov-complexity bias.
- [Theory refinement (EITHER)](../../../../sources/theory-refinement-analytical-empirical-methods.ingest.md): has compression operators inside a fixed Horn class. The fixed-decomposition theory edge already covers this axis.
- [We should take text optimization more seriously](../../../../sources/we-should-take-text-optimization-more-seriously.ingest.md): invokes a "Kolmogorov-style compression prior" for short text updates. MDL could qualify it, but the manifesto states this loosely, and the ingest's occasion gains little from the link. A weak candidate, kept here so a future editor can see why it was left out.

## Index Membership

None. The `learning-theory` tag head is `complete: true` over participating collections, and sources do not participate. The source already carries `tags: [learning-theory]`, which is enough for source-scoped search.

## Synthesis Opportunities

- MVV, `information-value-is-observer-relative`, `epiplexity-by-example`, Simon's representation-dependence claim, and this ingest together imply a sharper claim. Every vocabulary-relative measure of simplicity or extraction cost inherits its code choice, and only a restricted, refined construction (NML over a parametric class) makes within-class comparison non-arbitrary. The ingest's Recommended Next Action ("Description length over a chosen vocabulary is MDL's crude two-part code, not Kolmogorov complexity") is the natural host. Connect does not create it.
- Three sources gate new structure by compression without distinguishing crude from refined MDL: DreamCoder's library gate, beyond-fixed-representations' amortized-compression score, and the self-revising discovery systems' MDL gates. Grünwald's split classifies all three as crude two-part with an ad hoc L(H).

## Maintenance Observations

- Two DreamCoder ingests exist: `dreamcoder-wake-sleep-bayesian-program-learning.ingest.md` and `dreamcoder-wake-sleep-full-paper.ingest.md`. They overlap on the MDL library objective. Sources that cite DreamCoder may need a rule for which one to link.
- `herbert-simon-architecture-of-complexity.ingest.md` and this ingest are both untracked in the working tree. Any edge between them should be authored only after both are committed.

## Flags

- Tension between candidates: `information-value-is-observer-relative` says classical theory abstracts away the observer, while this ingest documents an observer-relative (code-relative) branch of the same lineage. The ingest leaves it to the note's author whether this qualifies the claim or narrows its scope. Connect does not resolve it.
- Not a split candidate: the ingest makes one analytical contribution, on the occasion, and reaches several areas through it.
