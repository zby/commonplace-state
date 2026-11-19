---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Minimizing Syntactic Dependency Lengths: Typological/Cognitive Universal?

**Source:** [Minimizing Syntactic Dependency Lengths: Typological/Cognitive Universal?](../../../../sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md)

The source is an immutable snapshot. No tracked ingest `kb/sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md` exists yet. Every outbound candidate below is for that future ingest's authored surface (inline or `Relevant Notes:` footer), never for the snapshot. Reverse-edge candidates must target the ingest once it exists, because `kb/theory/COLLECTION.md` forbids links to `.snapshots/`.

**What the source contributes beyond its sibling captures.** Temperley and Gildea's Annual Review survey is the cluster's only artifact that sets dependency length minimization (DLM) against named rival accounts and reports which contrasts separate them:

- DLM versus Hawkins's Early Immediate Constituents (EIC) theory, separated by three-adjunct constructions, where only DLM predicts that the first adjunct is shorter.
- DLM versus production end-weight, separated by left-branching Japanese, where DLM predicts long-before-short ordering and end-weight predicts short-before-long. The review also reports one English case as indecisive (two premodifying adjuncts).
- DLM versus n-gram predictability, which are only moderately correlated. Observed grammars lie near a frontier that trades the two against each other (Gildea & Jaeger 2015).
- DLT critiques: Demberg & Keller find DLT a small predictor of reading times, antilocality effects run opposite to it, and ACT-R measures decay in time with interference.

It also gives the grammar-versus-choice split in average per-sentence dependency length for English. Observed text measures 47.5. A random projective order measures 82.7 and the projective optimum 33.5. An optimized fixed grammar reaches 42.5, and a corpus-matched fixed grammar 51.4. It closes by declining to settle whether production or comprehension causes DLM.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md` outbound section. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and other sources, plus external. `kb/work/` and `kb/instructions/` are excluded. Labels per destination: theory gets `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also` and `defined-in` (theory/definitions only). Sources get `compares-with` and `see-also`. Reference gets `see-also`. External gets `derived-from` and `see-also`.
- `kb/types/connect-report.md`.
- `kb/theory/COLLECTION.md` was read for reverse-edge labels: `evidenced-by` qualifies or bounds a claim, and the "Origin is not corroboration" rule applies.

**Sibling sources (first pass; five untracked dependency-locality ingests from the same session):**
- `ls kb/sources/ | grep -iE 'temperley|gibson|futrell|dependency'` found futrell-dependency-length-minimization, futrell-levy-gibson-dependency-locality, gibson-2019-how-efficiency-shapes-language, gibson-dependency-locality-theory and temperley-2007-dependency-length-written-english. No temperley-gildea ingest exists.
- Read each sibling's `## Connections Found` and `Relevant Notes:` footer. All five converge on the same theory targets: two-rewrites, human-writing-structures-transfer and local-materialization. Two also cite an-experiment-identifies-only-the-contrast, soft-bound-traditions, human-llm-differences, the attention ingest and skill-and-working-memory.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'writ|prose|sentence|syntax|read|locality|distance|human|order|simplif|clause|local|proxim|position|ambigu|parse|attention|frontload|placement|near'` flagged two-rewrites, three-simplification-passes, human-writing-structures-transfer, local-materialization, human-llm-differences, design-for-the-first-time-human, writing-styles-are-strategies-for-managing-underspecification and link-strength-is-encoded-in-position-and-prose.
- `rg -m1 '^description:'` over the flagged files narrowed the set. Link-strength concerns link placement, not syntax, so it was dropped. Design-for-the-first-time-human concerns access cost, so it was dropped.

**Body search:**
- `rg -il 'dependency length|dependency locality|DLM\b|Gibson|Temperley|Futrell|center-embed|garden.path|working memory|end-weight|heavy.NP' kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/reports/cache/**'`. In theory, only soft-bound-traditions, llm-learning-phases and flat-memory match, all on "working memory" and none on dependency length. Hits in agentic-systems and agent-memory-systems are "working memory" in the agent-runtime sense, so they were rejected as keyword-only. The `kb/instructions/review-gates/sentence/clause-packing.md` and `kb/work/` hits are excluded destinations.
- `rg -n -i 'dependen(cy|t) (length|distance)|locality|parsing load|parse'` over two-rewrites, three-simplification-passes and human-writing-structures confirms that two-rewrites names "parsing load" and attachment loss (lines 10, 30, 34).
- `rg -l -i 'pareto|trade-?off frontier|competing (pressures|objectives)' kb/theory` matched only brainstorming-maintainability-oracles, which is unrelated. No theory note carries the multi-objective frontier the source reports for DLM and predictability.
- `rg -l -i 'predictab|surprisal|expectation-based' kb/theory` matched only unrelated senses (predictable choices, codification). No expectation-based processing note exists.
- `rg -n -i 'garden|greedy|ambiguity resolution|misattach' kb/theory` matched only "greedy" in search-loop notes, which is unrelated to the source's parse-pruning discussion.
- `rg -n -i 'working memory|parsing|dependency|locality'` over soft-bound-traditions, writing-styles and local-materialization. Only soft-bound-traditions has a working-memory row, and it treats count, not distance.

**Reference, tags and descriptive collections:**
- `ls kb/tags/ | rg -i 'writ|prose|human|evidence|llm|cogn'` returned only llm-reliability-README, which is off-topic. No writing or psycholinguistics tag exists.
- `rg -n -i 'sentence|word order|prose style' kb/reference -l` matched routing, validation and ADR files that mention "sentence" incidentally. None treats word order, so the reference destination was skipped.
- agent-memory-systems and agentic-systems were skipped: the source has no plausible match for their reviews of external agent systems.
- External prospecting was skipped by rule. The DOI in the snapshot frontmatter is already in hand as the `derived-from` target.

**Link following:**
- From two-rewrites: three-simplification-passes is a sibling evidence note about the same rewrite program. It concerns rhythm and drift, not attachment, so it is weaker.
- From the contrast note's body (Harness-IF, self-evolver examples) to the source's DLM-versus-EIC and DLM-versus-end-weight discriminations. The fit is structural.
- From the gibson-dependency-locality-theory ingest's limitations ("Rivals underweighted", "antilocality ... from background knowledge") to this source's §5. That §5 supplies those rivals from a citable review, which resolves a gap the sibling ingest flags.

## Connections Found

For the future `temperley-gildea-2018-minimizing-dependency-lengths.ingest.md`:

- [Minimizing Syntactic Dependency Lengths (Annual Review of Linguistics, 2018)](https://doi.org/10.1146/annurev-linguistics-011817-045617) -- **derived-from**: the ingest analysis is worked out from the published review.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **is-evidence-for**: the review separates DLM from EIC and from end-weight only through contrasts where the accounts diverge, namely three-adjunct orderings and left-branching Japanese. It reports the English premodifier case, where no such contrast is available, as "indecisive". This is an external worked case of naming only the effect that the observed contrast identifies.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: the shared axis is lowering attachment cost while preserving syntactic relations. The review adds two levers the note lacks. One is reordering under a fixed tree, which reaches 47.5 against 82.7 random and 33.5 optimal. The other is extraposition, which may cross dependencies to shorten them. It also shows locality traded against predictability rather than maximized. Both are human-reader findings at word scale.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: the review supplies the human half of the per-convention test for locality conventions. It reports convergent typological, corpus and experimental evidence, and it states the limits: DLT is a small predictor of reading times, antilocality cases exist, and expectation partly explains the comprehension benefit. The LLM half remains untested.
- [Gibson's Dependency Locality Theory ingest](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: the shared axis is distance as the human comprehension-cost mechanism. The review supplies the rivals and failures that the DLT ingest lists as "underweighted": Demberg & Keller's small reading-time effect, Levy & Keller's antilocality, ACT-R time-based decay with interference, and the Gibson & Warren and Alexopoulou & Keller cost modifications. It is the citable bound on any use of DLT.
- [Temperley 2007 dependency-length ingest](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: the shared axis is evidence for writer ordering choices. Temperley 2007 is the primary corpus study. The review restates its constructions inside the EIC and end-weight comparison, and it adds the grammar-versus-choice estimate (51.4 against 47.5). Readers should cite 2007 for the constructions and the review for how they discriminate between theories.
- [Futrell 2015 dependency length minimization ingest](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: the shared axis is observed dependency length against random and optimal baselines. The review places Futrell's 37-language result beside Gildea & Temperley's English fixed-grammar optimization and Gildea & Jaeger's predictability frontier. That frontier qualifies the 2015 ingest's reading that locality is "a pressure, not a target", because it names one of the competing pressures.

## Bidirectional Candidates

- [Gibson's Dependency Locality Theory ingest](../../../../sources/gibson-dependency-locality-theory.ingest.md) <-> source -- **compares-with**: the return path is useful because the DLT ingest's Limitations section asserts the rivals "from background knowledge". Once this ingest exists, a footer edge would let the DLT ingest cite them.
- [Futrell 2015 dependency length minimization ingest](../../../../sources/futrell-dependency-length-minimization.ingest.md) <-> source -- **compares-with**: the 2015 ingest attributes the gap to optimal to "competing needs" without naming one. This review names n-gram predictability as a measured independent pressure.

## Reverse-edge Candidates

All of these target the future ingest, not the snapshot.

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source ingest -- **evidenced-by** (theory label, used to qualify or bound): human corpora reorder within a fixed structure and stop short of the optimum because predictability competes. This bounds the note's two-option framing of split versus restate. It is not corroboration, because the review does not test the note's claim. Coordinate with the futrell-2015, gibson-DLT and temperley-2007 ingests, which each recommend an edge from this same note. One consolidated qualifying edge, or a theory note that cites all of them, would avoid four near-duplicate footer lines.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → source ingest -- **evidenced-by**: a field outside agent evaluation applies the same rule, using EIC-versus-DLM and end-weight-versus-DLM discriminations and calling an uncontrasted case indecisive. Under "Origin is not corroboration", the context phrase must say that this is an independent illustration, not a refutation attempt.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Futrell, Levy and Gibson 2020 ingest](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- rejected as a direct edge. Both are reviews with heavily overlapping coverage. The 2020 paper adds its own baseline tests. A `compares-with` edge would need a named axis that the two other source edges do not already serve, and none was found. See Flags on cluster redundancy.
- [Gibson et al. 2019 efficiency ingest](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- rejected. Its centre is information-theoretic efficiency and ambiguity. This review touches ambiguity only through parse-pruning strategy, so the overlap is topical.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- rejected for this source, though the siblings use it. The review adds nothing to the word-scale versus section-scale comparison that the futrell-2015 and temperley-2007 ingests already make. A fourth parallel edge would add no traversal value.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- rejected. The gibson-DLT ingest already carries the count-versus-distance comparison. This review's ACT-R time-decay and interference contrast could sharpen that note's "different failure modes" caveat, but the edge belongs to DLT, and this review is a secondary account of it.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- rejected as redundant with the human-writing-structures edge. The DLT ingest already makes the generic point.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- rejected. It concerns rhythm, drift and review exhaustiveness, not attachment distance.
- [Attention Is All You Need ingest](../../../../sources/05-attention-is-all-you-need.ingest.md) -- rejected. The futrell-levy-gibson ingest already carries the linear-distance comparison with sequence models. This review says nothing about machine readers.
- "Working memory" hits in agentic-systems and agent-memory-systems reviews -- rejected as keyword-only. They use the agent-runtime sense.

## Index Membership

None. No writing, prose or psycholinguistics tag exists, and `kb/sources/` has no curated sub-index for this cluster.

## Synthesis Opportunities

Six captures now share one occasion: whether to add dependency-length guidance to Commonplace writing instructions. They are this review, Temperley 2007, Futrell 2015, Futrell-Levy-Gibson 2020, Gibson DLT and Gibson 2019. Together they imply a bounded theory claim that none of them states. For human readers, keeping dependents near their heads lowers comprehension cost. That claim has three conditions. Locality competes with predictability and other pressures, so it is a pressure rather than a target. The ordering direction is language-specific: short-before-long in head-initial English, the reverse in head-final languages. Distance cost is not universal, given antilocality. Transfer to LLM readers is untested. The futrell-levy-gibson ingest already recommends this note. This review contributes its rival-discrimination evidence and the grammar-versus-choice split. Do not create it during connect.

## Maintenance Observations

- Cluster redundancy: the four ingests already written each recommend a separate edge from [two-rewrites](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md). If every recommendation is followed, that note gains four or five near-parallel `evidenced-by` lines. The synthesis note above would be the better single inbound target.
- The [gibson-dependency-locality-theory ingest](../../../../sources/gibson-dependency-locality-theory.ingest.md) asserts antilocality "from background knowledge" in its Limitations. Once this review is ingested, that assertion has a citable tracked source.

## Flags

- The source has no tracked ingest yet. All candidates wait on `cp-skill-ingest` producing `kb/sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md`. A parallel `cp-skill-ingest` agent is active in this session and may be writing it.
- Tension, unresolved: the review's comprehension evidence for DLM is mixed. DLT is a small predictor of reading times, antilocality effects exist, and the authors suggest expectation may explain part of the comprehension benefit. The sibling ingests lean on DLT as "the human-reader mechanism". Any writing rule should state the mechanism as contested.
- Not a split candidate. The source makes one assertion, that DLM is an important factor, with organized evidence.
