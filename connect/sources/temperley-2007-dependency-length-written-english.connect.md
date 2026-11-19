---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Minimization of dependency length in written English

**Source:** [Minimization of dependency length in written English](../../../../sources/.snapshots/temperley-2007-dependency-length-written-english.md)

The source is an immutable snapshot. It never authors links, and no durable link may target it. Every outbound candidate below is for the future tracked ingest `kb/sources/temperley-2007-dependency-length-written-english.ingest.md`, which does not exist yet.

Source claim, read in full at the abstract, section 1, section 4 summary, and section 5: in the WSJ (and mostly the Brown) portion of the Penn Treebank, English writers choose constructions that shorten syntactic dependencies. Examples are short-long ordering of postmodifying adjuncts and conjuncts, longer object NPs than subject NPs, longer postmodifying than premodifying adverbial clauses, and shorter subjects after premodifying adjuncts. The proposed mechanism is Gibson's Dependency Locality Theory (DLT): integration cost grows with the distance between a word and its head, because activation decays as intervening words accumulate. The author leaves open whether a "short-first" principle explains the same data. The evidence is about human writers and human processing only.

## Discovery Trace

**Setup:**
- Source collection `sources`; `kb/sources/COLLECTION.md` read. Its outbound section authorises `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/` and other sources, plus `external`. It excludes `kb/work/` and `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- The snapshot carries no `tags:`, so no tag-head by-tag pass applied. `kb/tags/document-system-README.md` was read as the nearest curated head because writing conventions are its scope. Its Writing Conventions and Testing groupings point to the notes evaluated below.

**Body search (whole KB, excluding work/instructions/reports in the filter):**
- `rg -il "dependency length|dependency locality|Gibson|Temperley|Futrell|short-long|heavy.?NP|end-weight|garden.?path|syntactic complexity|word order|sentence length|long sentences|readability" kb` -- no psycholinguistic hits. Hits were on "readability" in the generic sense: `structured-output-is-easier-for-humans-to-review`, `human-writing-structures-transfer-to-llms-because-failure-modes`, `human-llm-differences-are-load-bearing-for-knowledge-system-design`, the simplification evidence notes and agentic-system reviews. The agentic-system and agent-memory review hits were keyword-only and were rejected without further reading.
- `rg -il "ASD-STE|simplified technical english|plain language|plain english|Pinker|Strunk|style guide|sentence structure|garden path|subordinat|modifier attachment|left-branching|parsing load|parse" kb` (excluding work/instructions/reports) -- hits were parser/code senses in ADRs, proposals and reviews. None concerned prose syntax. Rejected as keyword-only.
- `rg '^description:' kb/sources --glob '*.ingest.md' | grep -iE 'writ|prose|sentence|readab|language|style|linguist|psycholing|reading'` -- no linguistics ingests. The hits concern writing as thinking (Karlsson, Borretti, Grunewald) or AI prose detection. None addresses sentence-level processing cost.
- `rg -il "dependency length|temperley|gibson|word.order" kb/work kb/log.md` -- no hits. No workshop context was found to explain the capture.

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | grep -iE 'writ|sentence|prose|read|style|order|local|near|adjacen|plain|clar|condition|syntax|language|word|human'` -- flagged `two-rewrites-exposed-a-syntax-or-repetition-tradeoff`, `three-simplification-passes-exposed-different-tradeoffs`, `human-writing-structures-transfer-to-llms-because-failure-modes`, `human-llm-differences-are-load-bearing-for-knowledge-system-design`, `local-materialization-should-outperform-distant-declarations`, `writing-styles-are-strategies-for-managing-underspecification`, `design-for-the-first-time-human-except-on-access-cost` and `warranted-reader-update-is-the-objective-of-substantive-writing`.

**Candidate evaluation:**
- `two-rewrites-exposed-a-syntax-or-repetition-tradeoff` -- read in full. Kept (see below).
- `human-writing-structures-transfer-to-llms-because-failure-modes` -- read in full. Kept.
- `local-materialization-should-outperform-distant-declarations` -- read in full. Kept as a bounded comparison.
- `human-llm-differences-are-load-bearing-for-knowledge-system-design` -- read in full. Rejected as a separate edge (see Rejected).
- `three-simplification-passes-exposed-different-tradeoffs`, `writing-styles-are-strategies-for-managing-underspecification`, `design-for-the-first-time-human-except-on-access-cost`, `structured-output-is-easier-for-humans-to-review`, `warranted-reader-update-is-the-objective-of-substantive-writing` -- description plus a grep for `sentence|syntax|parse|word order|reading cost|working memory`. Rejected (see Rejected).

**Sibling captures:**
- `ls -t kb/sources/.snapshots/ | head` showed four snapshots captured in the same batch: `futrell-dependency-length-minimization.md`, `gibson-2019-how-efficiency-shapes-language.md`, `gibson-dependency-locality-theory.md` and `futrell-levy-gibson-dependency-locality.md`. `ls kb/sources/*.ingest.md | grep -iE 'futrell|gibson|temperley'` returned nothing. None of the batch has a tracked ingest yet, so none is a valid link target (see Flags).

**Link following:**
- From `two-rewrites...`: its footer leads to `kb/reports/retained/asd-ste100-inspired-rewrite.md` (read the head) and to the excluded instruction `kb/instructions/asd-ste100-inspired-rewrite.md`. The report lists "shorter sentences can make a note longer" as an idea to test. Neither target is an authorised sources destination.
- From `human-writing-structures-transfer...`: it links up to `human-llm-differences...` and `why-notes-have-types`. These confirmed the per-convention transfer test as the governing methodology, and they surfaced no further candidates.

**Reference, agent-memory-systems, agentic-systems, tags:**
- No candidate. The source makes no claim about Commonplace's shipped system or about any external agent system. `document-system` is the only plausible tag head, and its membership rules apply to theory/reference artifacts, not ingests.

**External:**
- Prospecting skipped by rule. The already-known external target is the DOI in the snapshot frontmatter.

## Connections Found

All candidates below are for the future `.ingest.md`, not the snapshot.

- [https://doi.org/10.1016/j.cognition.2006.09.011](https://doi.org/10.1016/j.cognition.2006.09.011) -- **derived-from**: the ingest analysis is worked out from Temperley (2007), Cognition 105:300-333, which is already in hand as the snapshot's `source`.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: the comparison axis is how to lower parsing load without losing relations carried by syntax. The note finds only two routes, splitting with relation loss or restating with repetition (+4.9% words). Temperley documents a third route in human writing: keep the relations but reorder the constituents, placing heavy material last, adjuncts short-before-long and long adverbial clauses after the clause. This shortens dependencies without adding words. The paper measures human writers' choices, not comprehension gains or LLM readers. The ingest should present reordering as an untested candidate, not as evidence against the note's tradeoff.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: the source supports the note's human-side premise at sentence scale. A writing convention (dependency-shortening word order) tracks a named human processing failure (integration cost from activation decay over distance). The note's method then requires the LLM-side check: does a transformer reader pay a distance-dependent integration cost? The source cannot answer that check. The context phrase must say that the source bears only on the human side.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: the comparison axis is the distance between a dependent element and what it depends on, treated as a cost. Temperley and DLT give a human sentence-scale mechanism in which cost grows with intervening words. The note poses a document-scale LLM conjecture and explicitly declines to assume a monotonic decline with distance. The comparison helps a reader keep the two scales and the two consumers apart, and it shows the note's distance and intervening-content arms in a tested human analogue. It must not be read as support for the conjecture.

## Bidirectional Candidates

None. The useful return direction runs from theory notes to the future ingest under the theory contract's `evidenced-by` label. That is listed under Reverse-edge Candidates, not as a mirror of a sources-side edge.

## Reverse-edge Candidates

Both depend on the ingest existing first. Under the theory contract's "origin is not corroboration" rule, either `evidenced-by` phrase must say that the source qualifies or bounds the claim. It does not corroborate.

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → future ingest -- **evidenced-by** (theory → sources): this bounds the note's Inference section. Human writers reduce dependency length by reordering constituents, a third option beside splitting and repetition. The note's limits section already admits that no comprehension task was measured. This is the strongest reverse edge.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) → future ingest -- **evidenced-by** (theory → sources): this bounds the note. The source is a human sentence-scale case in which distance-dependent cost is established, which sharpens the note's caveat that LLM distance effects are not assumed. It is weaker than the edge above. Add it only if the note's "Why local materialization might help" section gains a sentence on human locality effects.

## Off-authorisation Candidates

- `kb/reports/retained/asd-ste100-inspired-rewrite.md` -- the experiment log of the ASD-STE100-inspired rewrite. Its "Ideas to test later" section is the natural place to record "test constituent reordering (short-before-long, heavy-last) as a relation-preserving simplification". `kb/reports/` is not an authorised destination in `kb/sources/COLLECTION.md`. The useful edge is a reverse one: a future entry in that report would cite the ingest under the reports contract. Recommend no sources-contract change.
- `kb/instructions/asd-ste100-inspired-rewrite.md` and `kb/instructions/simplification-passes/readability-and-flow.md` -- reordering rules derived from this paper could become a rule in these procedures. Sources may not link into instructions, and instructions are frontloaded, so a rule would have to be stated in the instruction itself. Recommend rejecting the link and treating this as possible later operationalization through a theory note.

## Raw Text Candidates

None.

## Rejected Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- it states the per-convention transfer methodology, and the source's mechanism (human activation decay) is exactly the kind of human-specific property it warns about. `human-writing-structures-transfer...` already carries that methodology and links up to this note, so a second edge would duplicate the route. Reject to avoid a spray.
- [Three simplification passes exposed different tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- it compares style-guidance treatments at whole-article scale. Word ordering is not one of its axes, so the link would be topical only.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- "styles" there means context-file instruction styles (descriptive, prescriptive and so on), not sentence syntax. Keyword collision.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- it concerns access-path cost over artifacts, not within-sentence processing cost. Different scale and mechanism.
- [Structured output is easier for humans to review](../../../../theory/structured-output-is-easier-for-humans-to-review.md) -- section-level separation for review. No syntactic-distance content.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- it concerns contribution selection, not surface form.
- Agentic-system and agent-memory review hits on "readability"/"parse" -- keyword-only in code or document-format senses.

## Index Membership

None for the snapshot. A future ingest has no collection index to join beyond the generated listing. The `document-system` tag head admits theory and reference artifacts, not ingests.

## Synthesis Opportunities

Possibly: `two-rewrites-exposed-a-syntax-or-repetition-tradeoff` plus this source, together with the four sibling dependency-locality captures once ingested, could support a theory note on prose simplification. Candidate claim: for agent-read prose, constituent reordering is a candidate simplification that preserves relations, and it competes with splitting and restating. Its LLM-side benefit is an open empirical question, because the locality evidence covers human processing only. The note should wait for the sibling ingests and for at least one measured rewrite trial. Do not create it during connect.

## Maintenance Observations

- Five dependency-locality snapshots (this one, `futrell-dependency-length-minimization`, `gibson-2019-how-efficiency-shapes-language`, `gibson-dependency-locality-theory`, `futrell-levy-gibson-dependency-locality`) exist under `kb/sources/.snapshots/` without tracked ingests. Until ingests exist, `commonplace-validate kb/sources` may warn that no ingest matches these snapshots, and no KB artifact can cite them.

## Flags

- **The ingest does not exist yet.** All Connections Found entries need `kb/sources/temperley-2007-dependency-length-written-english.ingest.md` as their author. Rerun connect on the ingest once it exists, for reverse-edge confirmation and sibling `compares-with` edges.
- **Sibling `compares-with` edges are deferred.** Once ingested, the siblings are natural `compares-with` targets for this source. Axes: Gibson DLT is the mechanism this paper tests. Futrell et al. (37 languages) generalize the effect cross-linguistically, while Temperley is English, written and construction-specific. Futrell, Levy and Gibson dissociate grammar from usage, which bears on Temperley's open question of DLT versus short-first. Gibson 2019 places locality within broader efficiency pressures. The sources contract forbids durable links to snapshots, so none are proposed now.
- **The transfer gap must be stated.** Every edge from this source into agent-facing writing theory rests on a human working-memory mechanism. The ingest should state that no evidence here concerns LLM readers.
