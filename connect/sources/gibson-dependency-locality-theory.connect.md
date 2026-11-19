---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/gibson-dependency-locality-theory.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: The Dependency Locality Theory: A Distance-Based Theory of Linguistic Complexity

**Source:** [The Dependency Locality Theory](../../../../sources/.snapshots/gibson-dependency-locality-theory.md)

This report regenerates the earlier same-day run. The source is an immutable snapshot. Its authored connection surface is the tracked ingest [gibson-dependency-locality-theory.ingest.md](../../../../sources/gibson-dependency-locality-theory.ingest.md), which now exists (untracked). Every Connections Found item is a recommendation for that ingest's `## Connections Found` section. No candidate links to `.snapshots/`.

What changed since the earlier run: the ingest now carries five edges, which this run re-confirmed. Four sibling ingests now exist in the same dependency-locality batch. They are Futrell et al. 2015, Futrell, Levy and Gibson, Gibson et al. 2019, and Temperley 2007. They make **compares-with** edges to `kb/sources/` available. The sibling ingests also surfaced two theory and source targets that the first run missed.

Source reading used for judging candidates: Gibson models sentence-comprehension resources as two costs drawn from one fixed pool. **Integration cost** grows with the number of new discourse referents between a word and its head or antecedent. **Storage cost** is one unit per syntactic head still predicted. The theory explains nesting difficulty, the pronoun-subject contrast, subject- versus object-extracted relative clauses, and some ambiguity preferences. The chapter calls its linear metric a simplification and leaves the storage-integration relation open. All evidence concerns human readers.

## Discovery Trace

**Collection contract:** read the `kb/sources/COLLECTION.md` section "Outbound links". The ingest is the link author. Permitted scan targets are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. Authorised labels by destination:
- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
- theory/definitions: `defined-in`
- sources: `compares-with`, `see-also`
- agentic-systems and agent-memory-systems: `compares-with`, `see-also`, and `is-evidence-for` for agent-memory-systems only
- reference: `see-also` only
- external: `derived-from`, `see-also`

There is no frontloading posture. External prospecting was skipped because no external target was supplied. The source URL is carried in the ingest frontmatter.

**Prior coverage / inbound check:**
- `rg -l -i 'gibson|dependency locality|dependency length' kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/reports/**'` returned the DLT ingest, the four sibling ingests, and incidental hits in `sutskevers-list` and `gavel-graph-world-models.ingest.md`. No theory, reference or tag artifact cites any locality source yet.
- `rg -n -i 'DLT|dependency locality theory|Gibson 2000|integration cost|storage cost'` over the four sibling ingests found the following. Temperley tests DLT's predictions directly, at lines 31-63, 148-166 and 208. Both Futrell ingests name Gibson as DLT's originator. None of them links to the DLT ingest.
- `ls kb/sources/.snapshots/ | grep -i gibson` showed `gibson-1998-linguistic-complexity-locality.md` with no tracked ingest. It is not a link target (see Flags).

**Sources (sibling ingests):** read the descriptions and `## Connections Found` sections of `futrell-dependency-length-minimization`, `futrell-levy-gibson-dependency-locality`, `gibson-2019-how-efficiency-shapes-language` and `temperley-2007-dependency-length-written-english`. All four were kept as **compares-with**, with distinct axes (below). Their own outbound edges were mined for targets the DLT ingest lacks:
- `local-materialization-should-outperform-distant-declarations.md` was kept.
- `05-attention-is-all-you-need.ingest.md` was kept.
- `an-experiment-identifies-only-the-contrast-it-actually-runs.md` was rejected.
- `agentic-systems-interpret-underspecified-instructions.md` and `legal-drafting-...` were rejected. They match Gibson 2019's ambiguity argument, which DLT does not make.

**Theory (titles listing):** `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` was filtered first with the earlier run's filter `rg -i 'sentence|prose|writ|read|locality|distance|nest|working memory|attention|context|condition|clarity|style|plain|syntax|parse|comprehen|load|proxim|adjacen|order|token|span|reference|pronoun|anaphor'`, then with `rg -i 'locality|distance|near|adjacen|first.mention|gloss|one term|referent|given|crucial|minimal pair|falsif|refut|critic|conjecture'`. The second filter flagged only epistemics notes (claim modality, refutation, guards). None bears on DLT beyond generic falsifiability, so all were rejected. The first-run keeps were re-confirmed: two-rewrites, human-writing-structures, soft-bound-traditions and human-llm-differences.

**Topic indexes:** `kb/tags/document-system-README.md` has a Writing Conventions section with no prose-comprehension entry. No linguistics or readability tag exists. Source ingests are not tag members.

**Body search (carried from the first run, still valid; no new theory notes since):**
- `rg -l -i -e 'working memory'` kept the soft-bound-traditions note and `skill-and-working-memory.ingest.md`. The other hits use agent-session senses and were rejected.
- `rg -l -i -e 'center-embed|centre-embed|garden'`, `-e 'long-distance|far from'`, `-e 'antecedent'`, `-e 'syntax'` and `-e 'locality'` returned only keyword-only hits in other senses.
- `rg -l -i -e 'next to (its|their|the) claim|beside the claim|adjacent to'` found no theory grounding for the AGENTS.md condition-adjacency rule.
- `rg -l -i 'lost.in.the.middle|position(al)? bias|recency|distance between'` returned Paulsen MECW and position-bias. Both were rejected.
- This run added `rg -n -i 'distan|far from|scale|section' kb/theory/local-materialization-should-outperform-distant-declarations.md`. It confirmed that the note's planned experiment varies "token or section distance" and "intervening competing content" independently.
- This run added `rg -n -i 'path length|distance|long-range|revers' kb/sources/05-attention-is-all-you-need.ingest.md`. It confirmed the path-length and input-reversal framing.

**Reference / agentic-systems / agent-memory-systems:** reference allows only `see-also`, and the earlier `rg -l -i 'psycholinguist|sentence comprehension|readability|plain english'` found only incidental mentions. The source describes no agent system, so these destinations were skipped.

**Link following:** from two-rewrites to three-simplification-passes. From human-llm-differences to human-writing-structures and model-resolved-indirection. From the Temperley ingest's Extractable Value to DLT's metric choices (referents versus words, peak versus sum) and the failed fronted-adjunct prediction. From futrell-levy-gibson to its review of antilocality and surprisal, the rivals the DLT ingest currently cites only "from background knowledge".

## Connections Found

Re-confirmed (already in the ingest):

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **is-evidence-for**: DLT is a mechanism for that note's "parsing load". In the note's failed first pass, a displaced temporal qualifier and a detached appositive both lengthened dependencies. The edge must stay bounded to human readers, as the ingest already says.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: DLT names the human-side failure that locality conventions prevent (integration and storage cost). The note's per-convention test still needs the LLM half.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- **compares-with**: the shared axis is the shape of a bounded processor's limit. The note's working-memory row has a chunk-count bound. DLT has held-items storage plus distance-dependent integration drawn from one pool.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- **compares-with**: DLT is a quantified human-reader cost model, exactly the kind of inherited assumption the note says must be re-checked for LLMs.
- [Skill and Working Memory](../../../../sources/skill-and-working-memory.ingest.md) -- **compares-with**: the shared axis is whether comprehension capacity is a fixed pool. Gibson assumes one. Chase and Ericsson show learned expansion.

New candidates:

- [Temperley 2007: dependency length in written English](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: the shared axis is DLT's predictions tested on production data. Temperley derives four dependency-length rules from DLT and confirms most of them in the WSJ and Brown corpora. One prediction fails: for two fronted adjuncts, DLT predicts long before short, but writers put short first. Temperley also uses a different metric, counting words and summing distances, while Gibson counts new referents and takes the peak. This is the strongest new edge. It gives the DLT ingest an independent test that the theory partly failed, which its Contribution assessment can cite instead of relying on background knowledge.
- [Futrell, Levy and Gibson: dependency locality as a word-order explanation](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: the shared axis is distance cost as a cause of processing difficulty versus its imprint on word order. DLT is the comprehension-cost theory. This paper shows corpus minimisation in 53 languages and reviews the cost evidence, including antilocality in verb-final languages and lossy-context surprisal, without choosing a mechanism. The DLT ingest's claims about "rivals underweighted" and antilocality come from background knowledge. They can point here for a tracked citation.
- [Futrell, Mahowald and Gibson 2015: dependency length minimization in 37 languages](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- **compares-with**: the shared axis is the same distance pressure measured in two ways, cross-linguistic treebank distances against DLT's human reading cost. This edge is weaker than the Futrell-Levy-Gibson edge because the newer paper supersedes much of its coverage. Prefer one Futrell edge if the ingest's footer should stay short.
- [Gibson et al. 2019: how efficiency shapes human language](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- **compares-with**: the shared axis is the scope of the locality claim. DLT (2000) is the sentence-processing mechanism. The 2019 review by the same lead author places dependency locality inside a broader efficiency-and-learnability account. It shows how the theory's author later framed DLT: as one efficiency pressure among several, not a complete cost model.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- **compares-with**: the shared axis is whether distance between a dependent and what governs it raises the cost of using it correctly. The note's planned experiment separates "token or section distance" from "intervening competing content". DLT is a human precedent for that split, because it counts intervening *new referents*, not words, and finds that given material costs less. Two caveats should go in the context phrase: DLT works at sentence scale and the note at section scale, and DLT is not LLM evidence.
- [Attention Is All You Need (Sutskever list chapter)](../../../../sources/05-attention-is-all-you-need.ingest.md) -- **compares-with**: the shared axis is the cost of linear distance between dependent elements. Human comprehension cost grows with integration distance. Attention gives a constant path length between any two positions, so the ingest's limitation that "Transformer attention is not obviously distance-limited" can cite a tracked source. This edge is weaker. Keep it only if the ingest's Limitations section gains this sentence.

## Bidirectional Candidates

- [Temperley 2007](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) <-> source -- **compares-with** (sources to sources): Temperley's Extractable Value item 2 tells writers of guidance to "cite comprehension evidence, such as Gibson's DLT studies, for the cost claim". The DLT ingest is that citation, so a return edge from Temperley closes the loop. Without it the corpus and comprehension halves stay unlinked.
- [Futrell, Levy and Gibson](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) <-> source -- **compares-with**: the paper reviews DLT as one candidate motivation. A return edge lets a reader of the corpus result reach the mechanism it presupposes.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → ingest -- **evidenced-by** (theory label, qualifying or bounding, not corroboration): the note's Inference section names "parsing load" without a mechanism. This matches the DLT ingest's own Recommended Next Action. All five locality ingests nominate this note, so see Maintenance Observations on the source bound.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) → ingest -- **evidenced-by** (qualifying): a sentence-comprehension row or a refined working-memory row could cite DLT for the storage/integration split.
- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) → ingest -- **evidenced-by** (qualifying): weak. Add it only if the note is revised to name a readability measure. DLT's two named checks (open predictions and attachment reach) are one candidate.
- [Local materialization should outperform distant natural-language declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) → ingest -- **evidenced-by** (bounding): the experiment-design paragraph could cite DLT as the human precedent for treating intervening competing content as a separate factor from raw distance.

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Text testing framework](../../../../theory/text-testing-framework.md) -- potential **see-also**: its Level A sentence-length check is the crude proxy that DLT shows to be inadequate, because cost tracks dependency distance and nesting. Temperley's word-versus-referent metric choice sharpens this. The file is frontmatter-free text.

## Rejected Candidates

- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- Futrell-Levy-Gibson is evidence for it because that paper explicitly bounds its conclusions to the baselines it ran. DLT's pronoun-subject minimal pair is only an illustration of a well-chosen contrast. The ingest rates that value as just-a-reference.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) and the legal-drafting note -- these fit Gibson 2019's ambiguity argument. DLT says nothing about ambiguity tolerance.
- [Paulsen: Maximum Effective Context Window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- whole-input span degradation is not intra-sentence integration distance, so an edge would invite a false analogy.
- [LLM Position Bias Benchmark](../../../../sources/position-bias.ingest.md) -- a keyword match on "position". It measures judging order effects.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md), [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md), [Model-resolved indirection adds interpretation work to LLM execution](../../../../theory/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) -- rejected as in the first run. The first is about interpretation space, the second about access cost, and the third about harness placeholders.
- Agent-session "working memory" ingests (`recursive-experiential-working-memory-evolution`, `components-of-a-coding-agent-raschka`, `slate-moving-beyond-react-and-rlm`) -- keyword-only matches.

## Index Membership

- [Document system tag](../../../../tags/document-system-README.md) -- not a direct fit, because source ingests are not tag members. A future theory note on locality in prose would belong in its Writing Conventions section.

## Synthesis Opportunities

The five locality ingests now jointly support a candidate theory note. It would claim that keeping each dependent near its head, measured in intervening new referents, lowers human parse cost, and that reordering can achieve this without the repetition cost of splitting. The roles divide as follows:
- DLT supplies the comprehension mechanism.
- Temperley supplies writer-level rules and the failed fronted-adjunct case, which tempers mechanical application.
- Futrell-Levy-Gibson supplies cross-linguistic minimisation plus its rivals (antilocality, surprisal).
- Gibson 2019 supplies the efficiency frame.
- The two-rewrites note supplies the KB-local failure.

The note would also give the AGENTS.md rule "Keep necessary conditions next to their claims" its missing rationale. The LLM half stays a conjecture, so the note would be at most a tentative human-side mechanism with an explicit transfer test. Do not write it during connect.

## Maintenance Observations

- Source-bound pressure: all five locality ingests recommend a return edge from `two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md`. The theory collection bounds a note at five unquoted tracked sources, and none of the five ingests has retained quotes. Adding all five would hit the bound. A synthesis note (above) or quote retention via `cp-skill-ground` should precede any bulk back-linking.
- The AGENTS.md quality-bar rule on condition adjacency still has no grounding theory note (unchanged from the first run).
- The sibling ingests do not link to each other or to the DLT ingest, except for Temperley's unlinked prose mention of "Gibson's DLT studies". The batch is currently five islands joined only through theory targets.

## Flags

- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` (the *Cognition* paper that the DLT ingest names as the primary experimental report) has no tracked ingest. If it is ingested, it should take the comparison role for DLT's empirical weight.
- Transfer tension: every edge rests on human-reader evidence and lands on agent-read prose. Each context phrase should keep the "human only, LLM untested" bound.
- Metric tension: DLT (new referents, peak) and Temperley (words, sum) can rank sentences differently. Any rule or lint check built from the batch must choose one.
- Capture quality: the pdftotext capture is scrambled in several regions. When retaining quotes, prefer the clean prose of §5.3 and §5.3.5.
