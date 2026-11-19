---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/gibson-2019-how-efficiency-shapes-language.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: How Efficiency Shapes Human Language

**Source:** [Ingest: How Efficiency Shapes Human Language](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md)

The ingest already has 12 inline links in `Connections Found`, `Learning Claims` and `Limitations`. All of them resolve. It has no labelled footer and no `derived-from` edge to the external paper. The four sibling dependency-locality ingests (created in the same session, untracked) are not linked. This report recommends a footer for the inline links that carry the most weight, the missing external edge, and the sibling `compares-with` cluster.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` § Outbound links. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags, sources and external. Excluded are `kb/work/` and `kb/instructions/`. Labels by destination:
- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
- theory/definitions: `defined-in`
- sources: `compares-with`, `see-also`
- external: `derived-from`, `see-also`

**Description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'writ|prose|sentence|read|language|word|simplif|ambigu|human|style|natural|clarity|syntax|linear'` flagged these candidates:
  - three-simplification-passes (kept)
  - two-rewrites (kept; already inline)
  - human-llm-differences (kept)
  - human-writing-structures-transfer (kept; already inline)
  - writing-styles-are-strategies (rejected)
  - local-materialization (rejected)
  - design-for-the-first-time-human (rejected)
  - warranted-reader-update (rejected)
  - natural-language-meaning (already inline)
- Descriptions of all flagged files were read with `grep -m1 '^description'`.

**Topic indexes:**
- The source has no `tags:` field (it uses `domains`). By domain, I read `kb/tags/document-system-README.md`. Its Foundations section names human-llm-differences as the dual-audience premise, which supports keeping that candidate. No tag head covers psycholinguistics or writing style. Its Writing Conventions section has one entry.

**Body search** (paths: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags`):
- `rg -l -i 'dependency length|dependency locality|working.memory'`: no theory note treats dependency locality. Hits are agent "working memory" component names in system reviews (keyword-only, rejected) and llm-learning-phases (human learning modes, off-axis).
- `rg -l -i 'ambigu'`: mostly reference/ADR uses of the ordinary word. Theory hits that matter (agentic-systems-interpret, legal-drafting, silent-disambiguation) are already inline in the ingest.
- `rg -l -i 'information.theor|mutual information|source coding|channel coding'` found 2 notes:
  - information-value-is-observer-relative: already inline.
  - minimum-viable-vocabulary-is-the-naming-set-that-most-reduces: read in full and kept as `compares-with`.
- `rg -l -i 'compositional'`: natural-language-meaning (already inline). The other hits use "compositional" in a software or context-composition sense and were rejected.
- `rg -l -i 'readab|reading cost|sentence length|plain language'`: no psycholinguistic treatment. The hits are about review readability or ergonomics.
- `rg -l -i 'lost in the middle|position bias|distance in context'` found soft-degradation-often-binds-before-the-hard-cap plus brainstorming notes. Soft-degradation was evaluated for the ingest's LLM-transfer limitation and rejected (see below).
- `rg -l -i 'counterfactual baseline|null baseline|random baseline'`: 0 hits. The only home for the baseline point is an-experiment-identifies-only-the-contrast (already inline).
- `rg -l -i 'redundan'` and `rg -l -i 'clarif'`: generic uses only. specification-strategy and llm-context-is-composed-without-scoping were skimmed by description. Neither treats cheap repair as a condition for ambiguity.
- Sources: `rg -l -i 'lost in the middle|ste100|simplified technical english|plain language|readability|psycholinguist|working memory|sentence processing|garden.path|surprisal|information.theor|shannon' sources --glob '*.ingest.md'`. Evaluated by description:
  - the four dependency-locality siblings (kept)
  - paulsen-maximum-effective-context-window-mecw (rejected)
  - skill-and-working-memory (rejected)
  - lamport-how-to-write-a-21st-century-proof (rejected)
  - this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology (rejected, see MVV note)
  - we-should-take-text-optimization-more-seriously (rejected)
- `rg -n 'gibson-2019|futrell|temperley|gibson-dependency' sources/*.ingest.md theory`: none of the siblings links any other sibling. Their only footer edge is their own `derived-from` external.
- reference, agentic-systems, agent-memory-systems: no plausible match. The source's trigger, which is writing and processing cost, does not match any shipped-system or external-system description. I skipped these destinations after the searches above.
- external: the source's own `source:` URL is already in hand. I did no web prospecting.

**Link following:**
- three-simplification-passes → its footer cites two-rewrites as grounds. This confirms a two-note writing-experiment cluster that the source's locality-versus-length point bears on.
- human-llm-differences → human-writing-structures-transfer (per-convention transfer test) and design-for-the-first-time-human. This confirms the dual-audience framing that the ingest's LLM-transfer limitation needs.
- MVV note → information-value-is-observer-relative. Both apply information theory to bounded observers, and the source's lexicon tradeoff (informativeness against complexity) sits on the same axis.
- theory/COLLECTION.md labels: theory notes may link sources via `evidenced-by` and `abstracted-from`. This sets the reverse-edge labels below.

## Connections Found

- [https://socsci.uci.edu/~rfutrell/papers/gibson2019efficiency.pdf](https://socsci.uci.edu/~rfutrell/papers/gibson2019efficiency.pdf) -- **derived-from**: the analysed review manuscript. The sibling ingests all carry this footer edge, and this ingest lacks it.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **is-evidence-for**: dependency locality supplies the mechanism for the pass that lost relations by moving a qualifier away from its head. The separate length cost explains why restating relations added 4.9% more words. This is already inline; a footer label would make it the primary edge.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- **is-evidence-for**: the source treats dependency length as an effort cost "beyond utterance length". This bears on the note's inference that a simplifier cannot be judged by word count alone. The note's Churchill-pass regressions, such as dropping "later" from a definition, are qualifier-locality failures.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **compares-with**: on the axis of transfer warrant. Locality is a human writing convention whose mechanism, working-memory retrieval, has no shown LLM failure-mode counterpart. It is a test case for the note's per-convention rule. Already inline.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- **compares-with**: on the axis of dual-audience prose. The source's mechanism holds for the human half of the audience. Its unknown LLM transfer is the case the note's dual-audience table predicts. The note also says source materials assume "tolerance for ambiguity that will be resolved by understanding", which matches the source's account of efficient ambiguity.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: on the axis of a repair channel. The source's efficiency argument for ambiguity assumes cheap clarification, and the note describes the agent case where that channel is missing. Already inline; a footer label would make the bounding condition explicit.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) -- **compares-with**: on the axis of vocabulary size as a tradeoff between informativeness and complexity. The source reports lexical partitions (kinship, colour) near an informativeness–complexity frontier, with empirical measures. The note frames vocabulary choice as optimization for a bounded observer but has no measure of its own. New candidate; not currently linked.
- [Theory builder](../../../../theory/definitions/theory-builder.md) -- **defined-in**: Learning Claims uses the term condition by condition. Already inline.
- [Ingest: Dependency Locality Theory (Gibson 2000)](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: on the axis of evidence grain for processing cost. DLT is the primary statement of the integration-distance cost that this review relays without effect sizes. A writer needing the mechanism's quantitative form should go there.
- [Ingest: Large-scale evidence of dependency length minimization in 37 languages](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: on the axis of corpus evidence. This is the primary 37-language study behind the review's corpus claim, with its random-reordering baselines specified. That specification is what the ingest's limitation "corpus minimization is not reader benefit" needs to check.
- [Ingest: Dependency Locality as an Explanatory Principle for Word Order](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: on the axis of counterfactual baselines. It tests locality beyond null baselines, which addresses the review's own concession that baselines are "often the most challenging part".
- [Ingest: Minimization of dependency length in written English (Temperley 2007)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: on the axis of English written prose. It gives direct written-English evidence for the short-before-long and heavy-last rules, which the review states only cross-linguistically. It is the closest grounding for Extractable Value item 2.

## Bidirectional Candidates

- [Ingest: Dependency Locality Theory (Gibson 2000)](../../../../sources/gibson-dependency-locality-theory.ingest.md) <-> source -- **compares-with**: DLT readers gain the review's generalization of DLT into information locality and its cross-linguistic corpus context.
- [Ingest: Large-scale evidence of dependency length minimization in 37 languages](../../../../sources/futrell-dependency-length-minimization.ingest.md) <-> source -- **compares-with**: the review places the 37-language result inside the broader efficiency framework and reports the 50-language replication figure.
- [Ingest: Dependency Locality as an Explanatory Principle for Word Order](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) <-> source -- **compares-with**: the review is the same authors' integrative summary of the program, including information locality.
- [Ingest: Minimization of dependency length in written English (Temperley 2007)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) <-> source -- **compares-with**: the review supplies the working-memory mechanism and the cross-linguistic scope (the head-final reversal) that bound Temperley's English-only rules.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- **evidenced-by** (theory label): the source qualifies the note's tradeoff by naming dependency length and utterance length as separate costs. The context phrase must say it qualifies rather than corroborates, because the source did not test the note's claim.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) → source -- **evidenced-by**: this bounds the "not by word count alone" inference with a psycholinguistic cost that is independent of length. It qualifies the note; it does not corroborate it.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by**: the efficient-ambiguity argument's dependence on cheap repair explains why removing the repair channel turns tolerable ambiguity into silent resolution. This bounds the note.
- A future theory note, recommended by the ingest's Recommended Next Action ("locality of related words lowers reading cost for human readers"), would link this ingest via `abstracted-from`. The note does not exist yet, so there is no path.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- concerns context-file instruction styles (prescriptive, prohibitive and so on), not sentence-level word order. Keyword overlap only.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- a document-level "keep it close" claim for agents. Linking it would invite exactly the extension beyond sentence grain that the ingest's Limitations section rules out.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- about access cost and ergonomics, not processing cost within a sentence. human-llm-differences already covers the dual-audience framing.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) -- about what contribution to select, not how to encode it.
- [Soft degradation often binds before the hard cap](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- LLM degradation at context scale. The ingest explicitly says distance effects in LLMs "may exist for other reasons" and that this source offers no evidence. A link would suggest an analogy that the source does not support.
- [Ingest: Maximum effective context window (Paulsen)](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- same reason. This is window-scale LLM evidence, not within-sentence distance.
- [Ingest: Skill and working memory](../../../../sources/skill-and-working-memory.ingest.md) -- covers expert memory structures, not sentence-processing retrieval cost. The shared phrase "working memory" is the only link.
- [Ingest: Lamport, How to write a 21st-century proof](../../../../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) -- covers document structure for checkability. No shared mechanism.
- Agent-memory and agentic-system reviews that hit `working.memory` (for example phantom, openviking, virtual-context) use it as a component name. Keyword-only.

## Index Membership

- [Document system tag](../../../../tags/document-system-README.md) -- not applicable. The tags collection admits notes, not ingests. Once the recommended locality theory note exists, it would belong under Writing Conventions.

## Synthesis Opportunities

The two simplification evidence notes, this review, Temperley 2007 and Gibson 2000 together imply a claim the KB lacks. That claim is the theory note the ingest already recommends: prose revision trades two separable costs, dependency length and utterance length, so a simplification rule that minimizes one degrades the other unless it states a tie-break. Do not create it during connect.

## Maintenance Observations

- The five dependency-locality ingests (this one and four siblings, all untracked) form a cluster with no edges between its members. Each has only its own `derived-from` edge or inline theory links. If they are ingested as a batch for one occasion, a single pass over the cluster's links would be cheaper than five separate edits.
- This ingest is the only member of the cluster with no `derived-from` footer to its external source.

## Flags

- Tension to keep visible: the ingest links [Human writing structures transfer to LLMs](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) as the transfer test. Any reverse edge from LLM context-degradation notes would blur that test, and that is why those candidates were rejected.
- Not a split candidate. The source makes several assertions (ambiguity, lexicon, word order, compositionality), but it is a review ingest, and the occasion routes its value to one theory note.
