---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/temperley-2007-dependency-length-written-english.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Minimization of dependency length in written English (Temperley 2007)

**Source:** [Ingest: Minimization of dependency length in written English (Temperley 2007)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md)

The ingest already carries three KB edges (two-rewrites, human-writing transfer, local materialization) and the external `derived-from` edge. This run checks them and adds candidates. The main gaps are the four sibling dependency-locality ingests captured for the same occasion. The ingest names Gibson's DLT as the source of its cost claim but does not link that ingest.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` § Outbound links. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. Labels per destination: theory gets `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`, with `defined-in` for theory/definitions. sources gets `compares-with` and `see-also`. reference gets `see-also` only. agent-memory-systems and agentic-systems get `is-evidence-for` (agent-memory-systems only), `compares-with` and `see-also`. external gets `derived-from` and `see-also`. The contract states no frontloading posture or reverse-edge hint.

**Titles listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (427 titles), filtered with `rg -i 'writ|prose|read|syntax|sentence|simplif|style|convention|human|parse|distance|local|proximity|order|rewrite|plain|clarity|controlled|ste|working memory'`. Flagged: two-rewrites (already linked), three-simplification-passes (new), human-writing-structures-transfer (already linked), local-materialization (already linked), human-llm-differences, writing-styles-are-strategies, design-for-the-first-time-human, warranted-reader-update.

**Description listing scan:**
- `rg -N --no-heading '^description:' kb/sources --glob '*.md' -g '!.snapshots'` filtered with `rg -i 'writ|prose|style|plain|read|sentence|syntax|working memory|psycholing|attention is|linguist|language'`. Flagged: the four sibling dependency-locality ingests (gibson-dependency-locality-theory, gibson-2019-how-efficiency-shapes-language, futrell-dependency-length-minimization, futrell-levy-gibson-dependency-locality). No other sentence-level linguistics source exists. Writing-process sources (Karlsson, Graham, Lamport, Borretti) concern composition or proof structure, not syntax, and were set aside.
- `rg -N --no-heading '^description:' kb/reference kb/agentic-systems --glob '*.md' | rg -i 'writing|prose|style|readab|plain'`. Only ADRs about the writing guide and vocabulary (ADR 002, 116), with no sentence-level content. No candidate.

**Topic indexes:**
- `kb/tags/document-system-README.md`: the "Writing Conventions" section lists only title-as-claim. The tag does not cover sentence-level syntax. `kb/tags/COLLECTION.md` lists participating collections as theory, reference, instructions, agent-memory-systems, agentic-systems and reports, so sources does not participate. The ingest has no `tags:` field, so no by-tag `rg` was run.
- `ls kb/tags | rg -i 'writ|read|human|context'`: only context-engineering is relevant, and it covers context assembly, not prose syntax.

**Body search:**
- `rg -il 'dependency length|dependency locality|center-embed|centre-embed|word order|heavy-NP|heavy np|end-weight|garden.path|left-branching|right-branching' kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/cache/**'`: only the five dependency ingests, sutskevers-list chapters (bibliography and design patterns, incidental) and two agentic-system-analyses retained files (incidental "word order" uses). No theory or reference note treats syntactic dependency distance.
- `rg -il 'temperley|gibson|futrell|hawkins' kb ...`: only the sibling ingests, gavel-graph-world-models (unrelated Gibson), and a `kb/work/` file (excluded).
- `rg -n -i 'parsing load|parse load|syntactic|subject.{0,20}verb|appositive|heavy|clause order|reorder' kb/theory kb/reference kb/tags kb/agentic-systems`: every hit is "judgment-heavy" or "reorder evidence" in an unrelated sense (metamorphic checks, relaxing-candidate signals). No new candidate.
- `rg -n -i 'temperley|production|short.before.long|short-first|easy.first|given|heavy'` over the four sibling ingests: this locates the overlaps used below. Gibson 2019 Extractable Value 2 has the heavy-last rule. Futrell-Levy-Gibson Extractable Value 3 names given-before-new and easy-first as competing pressures. Gibson DLT Extractable Value 2 says distance counts in new referents, not words.

**Link following:**
- two-rewrites: read in full. Its tradeoff is between compressed syntax and restatement. Temperley's reordering is a third route that keeps relations and adds no words. The existing `compares-with` edge holds. Its Related Notes led to `kb/reports/retained/asd-ste100-inspired-rewrite.md`, which the ingest's Recommended Next Action names (it has an "Ideas to test later" section at line 17).
- three-simplification-passes: read in full. It is a sibling evidence note on how prose-revision instruments trade clarity against relation preservation. Kept (see below).
- Sibling ingests: read the Connections Found and Extractable Value sections of all four. They connect to each other's theory targets but not to Temperley.
- gibson-dependency-locality-theory → skill-and-working-memory and soft-bound-traditions: followed. Both concern working-memory capacity, which Temperley does not model. Rejected for this source.
- futrell-levy-gibson → 05-attention-is-all-you-need: followed. Its axis is distance cost in sequence models. Temperley gives no LLM-side material for that comparison. Rejected.
- human-llm-differences: read the opening. Rejected as redundant with the human-writing-transfer edge (see below).

**External:** No external prospecting. The existing `derived-from` DOI edge is the only external target in hand.

## Connections Found

Existing edges, confirmed:

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with**: kept as authored. Constituent reordering is an untested third way to lower parsing load. Unlike splitting and restating, it keeps the relations that syntax carries and adds no words.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: kept as authored. Its scope is the human half only.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: kept as authored. The axis is distance as cost. The ingest already states that the scale and the reader differ.

New candidates:

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- **compares-with**: shared axis is whether a prose-revision instrument lowers reading load without losing technical relations. That note found that a compact style cue lost relations, broad style guidance kept them by adding words, and exhaustive local review barely changed the text. Temperley's construction-level rules (heavy last, short subjects, long adverbial clauses after the main clause) are a candidate instrument that changes order but not relations or length. The note's design (fresh agents on a fixed baseline, a blind anonymized judge, word counts) is also the ready template for the reordering test that the ingest recommends.
- [Ingest: Gibson's Dependency Locality Theory](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: shared axis is how dependency distance and its cost are measured. The ingest says the cost claim must be cited from Gibson's comprehension work and that the two works use different metrics: Temperley counts words and sums distances, while Gibson counts new discourse referents and takes peak integration cost. This is the link an agent most needs, because the ingest names this source as its cost warrant but does not link it. Temperley gives production evidence for the theory; Gibson gives the comprehension mechanism.
- [Ingest: Futrell, Levy and Gibson on dependency locality](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: shared axis is which English word-order rules corpus evidence supports, and which rival pressures bound them. Both support short-before-long after a head for English. Futrell et al. name given-before-new and easy-first production as competing biases. These are the discourse confounds that Temperley controls only in Test 3. They also bear on the "short-first" rival that explains Temperley's failed fronted-adjunct prediction.
- [Ingest: Futrell et al. 2015 large-scale dependency length minimization](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: shared axis is order-only locality evidence at two grains. Futrell measures whole-treebank distance against random reorderings in 37 languages. Temperley tests specific English constructions with free order. Futrell's "between random and optimal" result and Temperley's documented failures (fronted adjuncts, left-branching conjuncts, Turkish) together bound any rule that applies dependency-length arithmetic mechanically.
- [Ingest: Gibson et al. 2019, how efficiency shapes language](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- **compares-with**: shared axis is the writer rules each ingest derives for English prose. Gibson 2019 states head-dependent adjacency and heavy-last as tendencies of fluent production. It recommends a theory note that would state those rules. Temperley supplies the construction-level corpus effects, with effect sizes and one failed prediction, that such a note would need for the heavy-last and short-subject rules. Weaker than the three edges above, because this source is a review that partly duplicates them. Include it if the ingest gets a sibling-sources cluster.

## Bidirectional Candidates

- [Ingest: Gibson's Dependency Locality Theory](../../../../sources/gibson-dependency-locality-theory.ingest.md) <-> source -- **compares-with**: the return path is useful too. The DLT ingest has no production-side evidence for its theory, and Temperley's Tests 9 and 10 (subjects shorten after a fronted adjunct, objects do not) are the cleanest production test of DLT's distance cost among the captured sources.
- [Ingest: Futrell, Levy and Gibson on dependency locality](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) <-> source -- **compares-with**: Futrell-Levy-Gibson's rule (c), short before long after a head with English corpus support, could cite Temperley's Tests 7 and 11 as construction-level corroboration.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) <-> source -- only if a reordering experiment is run. The note would then compare its three instruments with a fourth. Until then the theory-side return edge has no evidence to carry. Do not author it now.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- under `kb/theory/COLLECTION.md` rules. The note could name reordering as an unexplored third option in its Inference section, citing this ingest. Defer this until the recommended reordering test exists; until then the edge would add an untested option to an evidence note.

## Off-authorisation Candidates

- [ASD-STE100-inspired rewrite report](../../../../reports/retained/asd-ste100-inspired-rewrite.md) -- the ingest's Recommended Next Action targets this report's "Ideas to test later" section, and the report is the retained record of the experiment the reordering pass would extend. `kb/reports/` is not an authorised destination for sources outbound links. The ingest already names the path in code, which serves the reader. Recommend rejecting this as an edge: a Recommended Next Action pointer is a work instruction, not a durable connection, so the contract need not be extended.

## Raw Text Candidates

None

## Rejected Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- relevant to the "no evidence about LLM readers" limitation. The ingest already routes that limitation through the human-writing-transfer note, which applies this note's per-convention test. A second edge would repeat it.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- its styles concern how instructions are framed (prescriptive, explanatory and so on), not sentence syntax. It is a keyword match on "writing".
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- this is a dual-audience heuristic at artifact-access grain. Temperley adds nothing at that grain.
- [Ingest: Skill and Working Memory](../../../../sources/skill-and-working-memory.ingest.md) -- the Gibson DLT ingest compares with it on fixed-capacity pools. Temperley does not model capacity, and its "habit" remark is a passing suggestion, not a skill-acquisition claim.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- the axis is the shape of working-memory bounds, which DLT addresses and Temperley does not.
- [Ingest: Attention Is All You Need chapter](../../../../sources/05-attention-is-all-you-need.ingest.md) -- its distance-cost axis needs LLM-side material, and Temperley supplies none. The sibling Futrell-Levy-Gibson ingest already carries that comparison.
- [Document-system tag head](../../../../tags/document-system-README.md) -- sources does not participate in tags, and the tag's writing conventions do not cover sentence syntax. Not a link target for this ingest.

## Index Membership

None. Sources is not a tag-participating collection. No index currently gathers the dependency-locality ingests.

## Synthesis Opportunities

The five dependency-locality ingests (Temperley, Gibson DLT, Gibson 2019, Futrell 2015, Futrell-Levy-Gibson 2020) imply together a claim none of them states: human evidence supports a small set of English word-order rules (head-dependent adjacency, heavy last, short pre-verbal subjects, conditions adjacent to the claims they limit) as conventions of skilled practice with a named comprehension mechanism, while their benefit for LLM readers is untested. Gibson 2019's Recommended Next Action proposes such a theory note. Temperley adds what it lacks: construction-level effect sizes and one documented failure of mechanical DLM (fronted adjuncts), which bounds the rule set. Do not create the note during connect. Its gate is the reordering experiment the Temperley ingest recommends.

## Maintenance Observations

- Five ingests from the same occasion recommend different next actions. Gibson 2019 recommends writing a theory note now. Temperley recommends recording a reordering experiment in the ASD-STE100 report first and gating any writing rule on it. This is a sequencing conflict for whoever acts on the occasion, not a contradiction between sources.
- A separate connect report already exists for the snapshot of this source: `kb/reports/cache/connect/sources/temperley-2007-dependency-length-written-english.connect.md`, with `source` set to `.snapshots/...`. This report targets the ingest. The sibling pairs follow the same `.connect.md` / `.ingest.connect.md` split. A consumer should treat this ingest report as the one tied to the authored surface.

## Flags

- No split candidate. The ingest makes one bounded assertion: Temperley's production evidence supports writer word-order rules as human practice.
- Tension, not resolved: the ingest says its rules preserve relations and so fit the gap in the two-rewrites note. Gibson DLT measures distance in new referents, under which reordering given material may not change cost. The proposed reordering test should name which metric it uses.
