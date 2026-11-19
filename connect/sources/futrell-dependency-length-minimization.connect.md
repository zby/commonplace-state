---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/futrell-dependency-length-minimization.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Large-scale evidence of dependency length minimization in 37 languages

**Source:** [Large-scale evidence of dependency length minimization in 37 languages](../../../../sources/.snapshots/futrell-dependency-length-minimization.md)

The source is an immutable snapshot. Every outbound candidate below is for the future `kb/sources/futrell-dependency-length-minimization.ingest.md`, which does not exist yet. No durable link may target the snapshot.

**Source claim used for judging.** Futrell, Mahowald and Gibson (PNAS 2015) use parsed corpora of 37 languages to show that summed head-dependent distance is shorter than in random projective reorderings of the same trees. This holds against both free-order and fixed-order random baselines. Observed lengths stay above the optimal baseline. The authors attribute the gap to competing desiderata, such as incremental recoverability of structure. The proposed mechanism is memory cost: a parser must hold a head or dependent until its partner arrives. Head-final, case-marking languages minimize less, and the authors suggest morphology makes long dependencies easier to identify. The paper does not separate grammar from usage. Its texts are mostly edited prose, and it says nothing about LLM readers.

## Discovery Trace

**Contract reads:**
- `kb/sources/COLLECTION.md` outbound section. Prospected destinations: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/` and other `kb/sources/` ingests. Excluded: `kb/work/` and `kb/instructions/`. The `external` destination is authorised only for `derived-from` and `see-also`. It was not prospected because no external target was supplied.
- Labels for theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` (theory/definitions), `see-also`. Labels for sources: `compares-with`, `see-also`. Labels for reference: `see-also` only. The label table names no label for `kb/tags/`.
- `kb/theory/COLLECTION.md` outbound section, read for reverse edges. Theory notes may link to `kb/sources/` ingests as `evidenced-by`, `abstracted-from`, `derived-from` or `see-also`. "Origin is not corroboration" applies: an `evidenced-by` phrase must say whether the source corroborates the claim or only qualifies or bounds it.
- `kb/tags/COLLECTION.md`: `sources` is not a participating collection, so a source cannot carry tags.

**Topic indexes:**
- `kb/tags/README.md` listing and tag-head descriptions. Writing and processing-cost topics map to `document-system` and `context-engineering`.
- `kb/tags/document-system-README.md`, "Writing Conventions" section. It contains only the title-as-claim entry and no sentence-level prose guidance. No candidate was added.
- `kb/sources/README.md` describes the collection and lists no per-source entries.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 427 titles, filtered with `rg -i "writ|prose|sentence|read|condition|claim|term|style|plain|language|near|adjacent|distance|attention|memory|working|comprehen|lingu|grammar|syntax"`. Flagged: `two-rewrites-exposed-a-syntax-or-repetition-tradeoff`, `local-materialization-should-outperform-distant-declarations`, `human-writing-structures-transfer-to-llms-because-failure-modes`, `writing-styles-are-strategies-for-managing-underspecification`, `natural-language-meaning-is-coordination-among-learned-approximations`. The last two were rejected after reading.

**Body search:**
- `rg -n -i "dependency length|futrell|gibson|psycholinguist|garden.path|sentence processing|word order|locality" kb` excluding `kb/work` and `kb/reports`. Hits were locality in the module or storage sense (metaobject protocols, mempalace, ModularRSI) and the Sutskever's List book text ("Architectures that minimize dependency length..."). None was a linguistics match. All were rejected as keyword-only.
- `rg -l -i "futrell|dependency length|dependency-length" kb src` found only the Sutskever's List text. No ingest of this paper or its siblings exists yet.
- `rg -n -i "working memory|parsing load|parse its attachments|attachment|keep necessary conditions|next to their claims|beside the claim|qualifier" kb/theory kb/reference kb/sources` surfaced `soft-bound-traditions-as-sources-for-context-engineering-strategies` (Working memory row and "Chunk related information"). The `qualifier` hits referred to theory-builder qualifiers and Toulmin qualifiers, not syntactic attachment, and were rejected.
- `rg -l -i "short sentence|one main point|ASD-STE100|plain language|simplified technical english" kb` excluding `kb/work` and `kb/reports/cache`. Hits: the two-rewrites evidence note, `kb/instructions/asd-ste100-inspired-rewrite.md` (an excluded destination), `kb/reports/retained/asd-ste100-inspired-rewrite.md` (not an authorised destination) and accessibility review gates under `kb/instructions/` (excluded).
- `rg -n -i "proximity|close to (the|its) (claim|use)|distance between|far from (the|its)" kb/theory kb/sources kb/reference` matched only `local-materialization-should-outperform-distant-declarations` among relevant hits.
- `rg -n -i "lost in the middle|distance.*(degrad|reliab)|position.*context.*(degrad|reliab)" kb/theory` returned `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits`. Rejected: that note concerns position within a long context, not the distance between two related elements.
- `rg -l -i "dependency length|psycholinguist|sentence processing|word order|syntactic" kb/agentic-systems kb/agent-memory-systems kb/reference`. Hits were "syntactic" in the code or schema sense inside system reviews and archived reports. No candidate.
- `ls kb/sources/ | rg -i "ste100|plain|writ|lost|middle|readab|lingu|sutskever|prose|style|gibson|attention|position"` found `position-bias.ingest.md` (judge display order, rejected), `how-to-think-in-writing.ingest.md` (writing as conjecture testing, rejected) and `sutskevers-list/` (raw text, see below).
- `ls kb/sources/.snapshots/ | rg -i "futrell|gibson|dependency"` found four sibling snapshots from the same batch, none ingested yet: `futrell-levy-gibson-dependency-locality.md`, `gibson-2019-how-efficiency-shapes-language.md`, `gibson-dependency-locality-theory.md` and `temperley-2007-dependency-length-written-english.md`.

**Link following:**
- From the two-rewrites evidence note: `frontloading-spares-execution-context` (subject of the rewrite, not of distance cost, so no edge), `short-composable-notes-maximize-combinatorial-discovery` (word-count cost, no edge), and the operationalized instruction `kb/instructions/asd-ste100-inspired-rewrite.md` (excluded).
- From local materialization: `links-encode-conditional-possibilities-not-obligations` and `llm-context-is-composed-without-scoping`. Both concern dereference and scope, not linear distance. No edge.
- From human-writing-structures: `claim-notes-should-use-toulmin-derived-sections-for-structured` and `structured-output-is-easier-for-humans-to-review`. Neither concerns sentence-level structure. No edge.

## Connections Found

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: the shared axis is the cost of distance between linked elements, traded against other desiderata. In the rewrite experiment, a failed pass moved a temporal qualifier away from the definition it limited. The successful pass kept the attachment local by restating the condition at each use, at a cost of 4.9% more words. Futrell et al. find that languages shorten head-dependent distance well below chance but stop short of the optimum because competing pressures resist it. Following this link shows the reader the KB's only measured case where moving or splitting attached elements cost meaning or length.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: the shared axis is whether distance between a dependent element and its governing element raises the cost of correct use. The note conjectures, without testing, that placing a fact beside its use site beats a distant declaration for LLMs. It explicitly does not assume that reliability falls monotonically with distance. Futrell et al. give large-scale human-language evidence for distance cost at word scale, with a memory-store mechanism. The comparison should not be read as LLM evidence: the scale (words versus sections) and the reader (human versus model) both differ.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **rests-on**: use this only if the ingest argues that dependency locality should guide prose that LLMs read, such as the AGENTS.md rule "keep necessary conditions next to their claims". That transfer depends on this note's per-convention test. The test asks what failure the convention prevents for humans (memory-store cost for unresolved dependencies, per the paper's left-corner parser account) and whether LLMs show that failure. The paper supplies only the human half. If the ingest only summarises the linguistics, drop this edge.

## Bidirectional Candidates

None. Theory-side return links are listed below as reverse edges because they are authored under `kb/theory/COLLECTION.md` labels, not the sources labels.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → future ingest -- **evidenced-by** (qualifies, not corroborates): the note's Inference section says syntax carries semantic relations and that flattening it costs either meaning or repetition. Corpus evidence that human languages keep linked words close, but not maximally close, bounds that inference. Distance between linked elements is a measured processing cost for human readers, and minimizing it competes with other desiderata. The paper was not a test of the note's claim and says nothing about LLM readers, so the context phrase must not present it as corroboration.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) → future ingest -- **evidenced-by** (qualifies): this would add a human-language precedent and a candidate mechanism to the "Why local materialization might help" section. The phrase must state the scale and reader mismatch so that the edge does not read as support for the LLM conjecture.

## Off-authorisation Candidates

- [kb/tags/document-system-README.md](../../../../tags/document-system-README.md) -- sources COLLECTION.md names `kb/tags/` as a scan target, but its label table has no row for tags, and `sources` is not a participating tag collection. No authorised edge exists. Suggest rejecting this as off-scope. A tag-level route would come from a theory note that cites the ingest, not from the ingest itself.

## Raw Text Candidates

None worth recording. `kb/sources/sutskevers-list/chapters/11-appendix-design-patterns-for-engineers.md` uses "minimize dependency length" for gradient path length in neural architectures. That is a different concept, and the file is a local, unpublishable book conversion. It is listed under Rejected Candidates.

## Rejected Candidates

- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- this was the closest near miss. DLM fits the note's frame of a bounded processor (a memory store) adapting under selection pressure (word order). However, the note catalogues traditions, not linguistics findings, so a `see-also` would be an adjacency spray. Better routed as a possible synthesis (see below) after the sibling ingests exist.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- concerns directive style (prescriptive or descriptive), not syntactic arrangement. Keyword match only.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- concerns semantics and coordination. DLM is a claim about processing cost of linear order. No shared mechanism.
- [Soft degradation often binds before the hard cap when evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- "lost in the middle" concerns absolute position in long context, not the distance between a head and its dependent. Linking would invite a false analogy.
- [position-bias ingest](../../../../sources/position-bias.ingest.md) -- display order of judged candidates, unrelated to within-sentence locality.
- [how-to-think-in-writing ingest](../../../../sources/how-to-think-in-writing.ingest.md) -- writing as conjecture testing, unrelated to sentence-level processing cost.
- `kb/sources/sutskevers-list/` -- gradient-path "dependency length" in neural network architecture is a homonym. The material is also a raw, unpublishable local conversion.
- Locality hits in metaobject-protocols, ModularRSI, mempalace and ADR 042 -- module, edit or storage locality, not linear distance between related words.

## Index Membership

None. `kb/sources/README.md` keeps no per-source index, and sources do not carry tags.

## Synthesis Opportunities

Possibly later, not now. Once the sibling ingests exist, they and this paper could support a theory note on a locality principle for KB prose. Futrell 2015 shows DLM across 37 languages. Futrell, Levy and Gibson 2020 separate grammar from usage. Gibson's DLT gives a cost model of integration distance plus storage. Temperley 2007 derives operational ordering rules for written English. The candidate note would cover when keeping a condition next to its claim reduces reader cost, and why full minimization is not the target. The two-rewrites evidence note supplies the competing-desiderata case. Such a note must apply the per-convention transfer test from `human-writing-structures-transfer-to-llms-because-failure-modes`, because none of these sources measures LLM readers.

## Maintenance Observations

- The AGENTS.md quality-bar rule "Keep necessary conditions next to their claims" is the KB's most direct analogue of dependency locality. It lives in the control plane, not in a linkable collection, and no theory note states its warrant. This is a candidate gap for a later theory note. It is not a connection candidate.
- Four sibling snapshots from the same batch are not yet ingested. When they are, each pair of ingests has a natural **compares-with** edge in sources. The axes are: corpus-universal evidence (this paper) versus grammar-usage dissociation (Futrell, Levy and Gibson 2020); versus the cost model (Gibson DLT); versus construction-level rules for written English (Temperley 2007); and versus the broader efficiency review (Gibson 2019). Re-run connect after those ingests land.

## Flags

- Transfer caution: every KB-facing use of this paper crosses two gaps, from word scale to section scale and from human readers to LLM readers. Any edge that presents it as evidence for an LLM-reader claim must say so in its context phrase.
- No split candidate: the source makes one central empirical assertion.
