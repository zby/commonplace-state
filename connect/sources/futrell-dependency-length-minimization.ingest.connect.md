---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/futrell-dependency-length-minimization.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Large-scale evidence of dependency length minimization in 37 languages

**Source:** [Ingest: Large-scale evidence of dependency length minimization in 37 languages](../../../../sources/futrell-dependency-length-minimization.ingest.md)

The source already carries four footer links (one `derived-from` external, two `compares-with` theory, one `rests-on` theory). This run confirms those three internal edges and adds four new `compares-with` candidates to sibling dependency-locality ingests written on the same occasion. The search found no LLM-reader distance evidence in the KB that would fill the ingest's stated reader gap.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` "Outbound links". The authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. External links are authorised but were not prospected: the only external target is the paper URL, already present. The authorised labels are `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions) and `see-also`. The source has no `tags:`, and `sources` is not a tags-participating collection (`kb/tags/COLLECTION.md` `participating:`), so the source cannot be a tag member.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "writ|prose|human|llm read|distance|local|syntax|sentence|condition|qualif|read"` flagged these candidates:
  - two-rewrites (already linked);
  - three-simplification-passes;
  - local-materialization (already linked);
  - human-writing-structures (already linked);
  - human-llm-differences;
  - design-for-the-first-time-human;
  - writing-styles-are-strategies-for-managing-underspecification.
- `ls kb/sources/ | grep -iE 'futrell|gibson|temperley|depend|locality|readab|plain|psycho|syntax'` found four sibling ingests from the same occasion: futrell-levy-gibson-dependency-locality, gibson-2019-how-efficiency-shapes-language, gibson-dependency-locality-theory and temperley-2007-dependency-length-written-english. All four are untracked in the working tree. Their descriptions and summaries were read.

**Topic indexes:**
- `kb/tags/document-system-README.md` was read. Its "Writing Conventions" section lists only title-as-claim. Its dual-audience anchor, human-llm-differences, was evaluated below.

**Body search:**
- `rg -il "dependency length|dependency locality|psycholinguist|working memory|garden.path|sentence length|readability|plain language|word order"` over theory, reference, sources, agentic-systems, agent-memory-systems and tags. Outside the sibling ingests, all hits used "readability" or "working memory" in the agent-memory sense. None concerned syntactic distance.
- `rg -il "lost in the middle|positional bias|position bias|long.context|distance.*(token|fact)|attention dilution" kb/sources kb/theory`. The query looked for LLM-side distance evidence. Hits: position-bias.ingest (order effects in pairwise judging), gsm-dc (distractor count), longmemeval (memory benchmark). None varies distance between linked elements with content held fixed.
- `rg -n -i "next to (their|its) claim|necessary conditions|qualifier|attachment|ASD-STE|simplified technical english|short sentences|plain english" kb/theory kb/reference` found only incidental uses of "qualifier" and "attachment", plus a pointer to the excluded `asd-ste100-inspired-rewrite` instruction.
- `rg -n -i "dependency|word order|syntax|psycholing" kb/agentic-systems kb/agent-memory-systems kb/reference` found only software-dependency senses. No candidate came from these three destinations.
- `rg -n -i "futrell.{0,40}2015|37 languages|futrell-dependency-length" kb/`, excluding the source itself, returned no hits. Nothing in the KB links to this ingest yet, and no sibling ingest cites it.

**Link following:**
- Read the bodies of two-rewrites and three-simplification-passes. two-rewrites reports that splitting severed modifier attachments and shared qualifiers. That is the restructuring lever the paper excludes, which confirms the existing `compares-with` edge.
- Read the body of local-materialization. Its proposed experiment varies "token or section distance", which confirms the existing word-scale versus section-scale comparison.
- Read human-writing-structures. Its per-convention test is the premise the ingest's Recommended Next Action depends on, which confirms `rests-on`.
- Followed human-writing-structures to human-llm-differences. The latter states the same per-convention evaluation as a design premise. It is the upstream claim, not a separate need, so it was rejected.

## Connections Found

Existing edges, confirmed:

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: keep as authored. Both treat distance between linked elements as a cost traded against other desiderata. The rewrite changed structure, while the paper holds the tree fixed.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: keep as authored. The shared axis is distance cost between a dependent element and its governor: word scale for human readers versus section scale for LLM readers.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **rests-on**: keep as authored. The ingest's candidate prose rule for LLM readers depends on this note's per-convention transfer test.

New candidates:

- [Temperley 2007: dependency length in written English](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: the shared axis is evidence for writer-level ordering rules. This paper's stated limits are that it cannot separate grammar from speaker choice and that its corpus is multilingual. Temperley studies English writers' choices among grammatical alternatives directly: short subjects, heavy material last, short-before-long adjuncts. A writer drafting the short-before-long rule from Extractable Value 2 needs this comparison most.
- [Futrell, Levy and Gibson 2020: dependency locality in 53 languages](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: the shared axis is the strength of the corpus regularity against random-reordering baselines. The 2020 paper extends this 37-language test to 53 UD languages and six baselines and adds formalism-robustness checks. A reader citing the corpus regularity should cite the stronger replication beside this one.
- [Gibson's Dependency Locality Theory](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: the shared axis is the distance-to-processing-cost mechanism. This ingest says the memory-cost link is "cited from prior work, not tested here". DLT is that prior mechanism, with distance counted in new discourse referents rather than words. Following the link tells a writer where the cost claim actually comes from and that its distance metric differs.
- [Gibson et al. 2019: how efficiency shapes human language](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- **compares-with**: the shared axis is the framing of dependency length minimization (DLM) as one efficiency pressure balanced against others. That matches this ingest's Extractable Value 3, "locality is a pressure, not a target to maximize". This candidate is weaker than the other three. Keep it only if the other three are authored and the review framing adds context.

## Bidirectional Candidates

- [Temperley 2007](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) <-> source -- **compares-with**: Temperley's own analysis can use this paper's cross-language scale as the population-level backdrop for its single-language writer-choice finding.
- [Futrell, Levy and Gibson 2020](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) <-> source -- **compares-with**: the 2020 paper is the methodological successor to this one. A return link lets its reader see which baselines and languages were added.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- **evidenced-by** (an authorised theory→sources label): the context phrase must say the link bounds the claim, not corroborates it. The paper gives a human-corpus precedent that locality is a pressure stopping short of the optimum and is traded against other needs. It excludes restructuring, which is the lever the rewrite used. The paper did not test the note's claim, so under the theory collection's "Origin is not corroboration" rule the link can only qualify or bound it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- relevant to prose revision, but its tradeoff concerns compression versus precision across whole-article passes. It has no distance or ordering axis. two-rewrites already carries the specific attachment-severing comparison.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- states the same per-convention evaluation premise at a higher level. The existing `rests-on` edge to human-writing-structures already gives the operational test, so a second edge would duplicate it.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- concerns instruction style (prescriptive versus descriptive), not sentence-internal order. Keyword match only.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- concerns artifact-level access ergonomics, not syntactic distance.
- [GSM-DC: irrelevant-context distraction](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) -- the only nearby LLM-reader evidence, but it varies distractor count, not the distance between linked elements. Linking it as "the LLM half" would overstate what it measures.
- [Position bias benchmark](../../../../sources/position-bias.ingest.md) -- measures order effects in pairwise judging, not head-dependent distance.

## Index Membership

None. Sources do not participate in tags, and `kb/sources/` has no curated topic index for this area.

## Synthesis Opportunities

The five dependency-locality ingests (this one, Temperley 2007, Futrell-Levy-Gibson 2020, Gibson DLT and Gibson 2019), together with the two-rewrites evidence note, jointly support the theory note this ingest's Recommended Next Action proposes. Its claim would be that short-before-long ordering after the head and modifier adjacency are corpus-supported human-reader rules, that locality is a bounded pressure, and that transfer to LLM readers is untested. Connect does not create that note.

## Maintenance Observations

- The four sibling ingests are untracked in the working tree at report time. Before this source's new `compares-with` edges are authored, check that the siblings are committed, or commit them together, so the links do not point at uncommitted files.
- No KB artifact supplies LLM-reader evidence about distance between linked elements with content held fixed. All five ingests name this gap. It is the evidence the proposed synthesis note would need in order to move beyond conjecture.

## Flags

- No split candidate: the source makes one assertion cluster, a corpus regularity with stated bounds, and its candidate links span only two topic areas.
- No tensions found among the candidates.
