---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/futrell-levy-gibson-dependency-locality.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Dependency Locality as an Explanatory Principle for Word Order

**Source:** [Ingest: Dependency Locality as an Explanatory Principle for Word Order](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md)

The ingest already has five footer edges: derived-from (external URL), two-rewrites (is-evidence-for), human-writing-structures (see-also), experiment-contrast (is-evidence-for) and Attention Is All You Need (compares-with). This report covers what is missing. The main gap is the four sibling dependency-locality ingests captured the same day for the same occasion. None of them is linked from this ingest.

## Discovery Trace

**Authorisation read:** `kb/sources/COLLECTION.md` § Outbound links. Prospect in theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. Labels: derived-from (external); is-evidence-for (theory, agent-memory-systems); abstracted-from and rests-on (theory); compares-with (theory, sources, agent-memory-systems, agentic-systems); defined-in (theory/definitions); see-also (theory, reference, sources, agent-memory-systems, agentic-systems, external). No label names `tags` as a destination, so tag heads are a routing aid only. `kb/tags/COLLECTION.md` lists participating collections as theory, reference, instructions, agent-memory-systems, agentic-systems and reports. Sources is not one of them, so tag membership is moot. External prospecting was skipped: the only external target is the derived-from URL that is already present.

**Description/title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ kb/reference/ kb/agentic-systems/ kb/tags/ --glob '*.md' | rg -i 'writ|prose|sentence|locality|distance|reader|human|baseline|contrast|experiment|attention|position|condition|qualif|syntax|word|order|readab|legal|working memory|null'` returned about 80 titles. Flagged: local-materialization (via sibling ingests), human-llm-differences, writing-styles-are-strategies, design-for-the-first-time-human, competing-causal-theories, an-experiment-identifies-only-the-contrast (already linked), two-rewrites (already linked), human-writing-structures (already linked), and ablation-baselines-for-the-declared-objective (reference proposal; title matched only "baseline").
- Read `rg -m1 '^description:'` for local-materialization, human-llm-differences, writing-styles, soft-bound-traditions, design-for-the-first-time-human and competing-causal-theories.

**Topic indexes:**
- `ls kb/tags`: no writing or psycholinguistics tag head exists. The `document-system` head covers writing conventions, but sources do not participate in tags. No candidates came from tag heads.

**Body search:**
- `rg -l -i 'dependency length|dependency locality|word order|head.dependent|short.before.long|Behaghel|null baseline|random baseline|lost in the middle|positional' kb/theory kb/reference kb/agentic-systems kb/tags kb/sources` returned mostly "positional" noise (software dependencies and positional encodings). The real hits were the four sibling ingests: `futrell-dependency-length-minimization`, `gibson-dependency-locality-theory`, `gibson-2019-how-efficiency-shapes-language` and `temperley-2007-dependency-length-written-english`. No theory note mentions dependency locality.
- `rg -l -i 'lost in the middle|position bias|positional bias|long.range|long-distance' kb/sources kb/theory` returned position-bias.ingest (an LLM judge order effect), title-as-claim and others. None measures the distance between syntactically linked words in LLM reading.
- `rg -l -i 'lost in the middle|distance between|attachment error|misattach|modifier' kb/theory kb/sources` returned two-rewrites (already linked), the siblings, paulsen-MECW and soft-degradation. None of the new hits is on the locality axis.
- `rg -n -i 'necessary conditions next|next to (their|its) claim|sentence length|short sentences|literal sentences' kb/reference kb/theory kb/agentic-systems` returned only `kb/theory/text-testing-framework.md:27`. No reference doc states the condition–claim rule, which confirms the ingest's statement that the rule has no backing theory note.
- `rg -n -i 'dependency|locality|word.order' kb/agentic-systems -l` returned software-dependency hits only (beads-rust, swamp and others). Rejected wholesale.

**Link following:**
- Read the Connections Found and Relevant Notes sections of the four sibling ingests. Futrell 2015 and Temperley both use compares-with to [local-materialization](../../../../theory/local-materialization-should-outperform-distant-declarations.md). Gibson DLT uses compares-with to [human-llm-differences](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md), [soft-bound-traditions](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) and [skill-and-working-memory](../../../../sources/skill-and-working-memory.ingest.md). All four siblings link two-rewrites and human-writing-structures, which this ingest already does.
- Read the head of [competing-causal-theories](../../../../theory/competing-causal-theories-can-guide-distinguishing-experiments.md) and evaluated it against the ingest's open question (see Rejected).
- Read [automated-tests-for-text](../../../../theory/automated-tests-for-text.md) and the raw [text-testing-framework](../../../../theory/text-testing-framework.md) to check whether dependency length fits as a deterministic text check (see Raw Text and Rejected).

## Connections Found

- [Large-scale evidence of dependency length minimization in 37 languages (ingest)](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: the shared axis is the strength of the null baseline behind a DLM claim. The 2015 PNAS study compares observed trees with random reorderings of those trees. The 2020 paper stacks six independently motivated baselines across 53 languages, claims only the residual and adds a grammar-versus-usage split. The ingest already names "the authors' own 2015 study" as prior work, so a reader judging how much the evidence moved needs this link.
- [Minimization of dependency length in written English (ingest)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: the shared axis is evidence for operational English word-order rules. Extractable Value 2(c) cites short-before-long as a reviewed derivation with English corpus support. Temperley is that direct English written-corpus evidence (short subjects, heavy-last, short-before-long adjuncts). Linking it lets the planned theory note cite construction-level evidence rather than this paper's review.
- [Gibson's dependency locality theory (ingest)](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: the shared axis is distributional evidence versus a processing-cost mechanism. This paper tests distributions and only reviews cost, and the ingest names Gibson as the originator of DLT. The DLT ingest supplies the integration and storage cost account that Extractable Value 1 says this paper does not test. A writer stating "reviewed, not tested" needs to know where the reviewed mechanism is analysed.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: the shared axis is distance between a dependent element and what governs it as a cost of correct use. The human evidence works at word scale within sentences. The note's conjecture concerns LLM readers at section scale. That is exactly the scale boundary in Extractable Value 4, which currently names no theory target beyond the sentence. Both siblings carry this edge. It is not is-evidence-for, because both scale and reader differ.

## Bidirectional Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) <-> source -- **is-evidence-for** (existing outbound): the evidence note has no link to any dependency-locality ingest. A return link would give its "moved a temporal qualifier away from the definition it limited" failure a named human-side mechanism, scoped as not tested for LLM readers. Check the theory COLLECTION.md for an authorised theory→sources label before authoring. Prefer one representative ingest, or the planned theory note, over five near-parallel inbound links.

## Reverse-edge Candidates

- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source: that note's per-convention test needs a named human failure for each convention. The dependency-locality cluster supplies one for "keep linked elements adjacent". The inbound edge is better authored once, from the planned locality theory note, than from each ingest. Check the theory COLLECTION.md for the label.
- [Gibson's dependency locality theory (ingest)](../../../../sources/gibson-dependency-locality-theory.ingest.md), [Futrell 2015 (ingest)](../../../../sources/futrell-dependency-length-minimization.ingest.md) and [Temperley 2007 (ingest)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) → source: the inverse of the three compares-with edges above, under the same sources→sources authorisation. It is most useful from Futrell 2015, whose readers should learn that the 2020 paper strengthens the baselines.

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Text testing framework — source material](../../../../theory/text-testing-framework.md) -- potential **see-also**: its Level A deterministic checks list "sentence length". A parser-based dependency-length metric would be a measurable addition, and this paper supplies the measure (intervening words plus one). The file has no frontmatter, so it is not a regular connection target. See also the rejection of its frontmatter companion below.

## Rejected Candidates

- [Competing causal theories can guide distinguishing experiments](../../../../theory/competing-causal-theories-can-guide-distinguishing-experiments.md) -- the paper leaves memory, search-time and information-theoretic motivations unresolved. The ingest's dual-audience question (does locality help attention-based readers, or does it only prevent attachment errors?) is a pair of rival warrants. That fits the note's theme, but the paper runs no intervention that separates its rivals, and the KB has no experiment yet. The link would point at a design the source does not supply. Reconsider it for the planned theory note, where the rival warrants would be stated.
- [Automated tests for text](../../../../theory/automated-tests-for-text.md) -- the note says checks should be "built from real failures not taxonomy". No KB failure has yet been measured as a dependency-length problem; two-rewrites is qualitative. A link now would push a metric ahead of its failure evidence.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- it is on topic, and Gibson DLT carries a compares-with to it. This ingest already states the human-only limit through the human-writing-structures and Attention edges, so another generic dual-audience link adds nothing concrete. Keep it on the DLT ingest, which is the mechanism-bearing source.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- its working-memory capacity axis belongs to the DLT mechanism, which this paper only reviews.
- [Skill and Working Memory (ingest)](../../../../sources/skill-and-working-memory.ingest.md) -- the fixed-capacity question is a DLT axis, not a corpus-distribution one.
- [Gibson et al. 2019, How efficiency shapes human language (ingest)](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- this is a review that covers the same DLM evidence at a broader level. Next to the three sibling edges it would be a see-also spray with no distinct axis. Add it only if the planned theory note does not consolidate the cluster.
- [Position bias (ingest)](../../../../sources/position-bias.ingest.md) and [Paulsen MECW (ingest)](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- these cover LLM order and context-length effects, not the distance between syntactically linked words. They do not fill the LLM-reader gap the ingest names.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- a keyword-only match on "baseline".
- agentic-systems reviews (beads-rust, swamp, compound-engineering-plugin, autogenesis, semantic-engine) -- the "dependency" hits are about software dependencies.
- Writing-styles-are-strategies and design-for-the-first-time-human -- both concern writing, but at the level of instruction style and audience defaults. Neither treats within-sentence word order.

## Index Membership

None. Sources do not participate in tag heads, and no sources landing index curates the psycholinguistics cluster.

## Synthesis Opportunities

The five dependency-locality ingests (this one, Futrell 2015, Gibson DLT, Gibson 2019 and Temperley 2007) and [two-rewrites](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) jointly imply a theory note. It would hold that within-sentence locality rules (attach a modifier or condition to its head, keep the subject near the verb, put long constituents last in English) are warranted for human readers by distribution plus mechanism evidence. For LLM readers they would be warranted only, if at all, by attachment-error prevention during rewriting. The ingest's Recommended Next Action already names this note. That note, not five parallel ingest links, should carry the inbound edges into human-writing-structures and two-rewrites.

## Maintenance Observations

- Five same-occasion ingests were created on 2026-10-26 (currently untracked). They link the same three theory notes in parallel and do not link one another. This one has no sibling links at all. The cluster needs a consolidating artifact (see Synthesis) before each ingest gains more theory edges.
- Label inconsistency across the siblings for the same target: human-writing-structures is **see-also** here, **rests-on** in Futrell 2015, and **is-evidence-for** in Temperley and Gibson DLT. The reader-need here (the paper supplies the human half of the per-convention test) matches is-evidence-for better than see-also. Futrell 2015's rests-on reverses the direction of dependence. Reconcile them when the cluster is consolidated.
- The AGENTS.md rule "Keep necessary conditions next to their claims" has no theory or reference backing note (`rg` over kb/reference and kb/theory found nothing). This confirms the ingest's own observation.

## Flags

- Tension within the sibling set: two-rewrites carries **is-evidence-for** from this ingest and Gibson DLT but **compares-with** from Futrell 2015 and Temperley. The ingests disagree about whether human locality evidence bears on an agent-read rewrite failure. Do not resolve this in the ingests; the planned theory note should decide.
