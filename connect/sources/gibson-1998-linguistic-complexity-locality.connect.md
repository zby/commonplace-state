---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Linguistic complexity: locality of syntactic dependencies (Gibson 1998)

**Source:** [Linguistic complexity: locality of syntactic dependencies](../../../../sources/.snapshots/gibson-1998-linguistic-complexity-locality.md)

The source is an immutable snapshot. No `gibson-1998-linguistic-complexity-locality.ingest.md` exists yet, so every candidate below is for that future ingest report, which is the authored connection surface under `kb/sources/COLLECTION.md`. The snapshot itself must never author or receive a durable link.

Source summary used for judging candidates: the Syntactic Prediction Locality Theory (SPLT) is the 1998 predecessor of DLT. It states two costs drawn from one working-memory pool (§2.4): integration cost grows with the number of new discourse referents between a word and the head it attaches to (§2.2), and memory cost is paid for each predicted obligatory head while it waits (§2.3). Distinctive points beyond the DLT 2000 chapter:

- Intuitive complexity is the **maximal** memory load at any parse state, not average load or sentence length. Same-length, same-meaning sentences differ sharply, and adding right-branching clauses does not raise complexity (§2.5, examples 13–15).
- The memory-cost function is **non-linear and saturating** (sigmoid, §2.6.7). One very long dependency stays processable; overload needs two or more long unresolved predictions held at once (§3.5).
- Clause-based closure shunts finished clauses out of working memory (§2.6.6).
- Heaviness and short-before-long ordering follow from integration cost, with an explicit conjectured extension to production (§4).
- §6 states an internal tension: in an activation model, if one of the two costs is distance-based the other should not be. This is the motivation for DLT's later fixed storage cost.
- §7 names grammar-style checking and language generation as possible applications.

All evidence concerns human readers (English, Japanese). Nothing tests LLM readers.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, section "Outbound links". Destinations to scan: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). The snapshot is never the link author.

**Context read:** five untracked sibling ingests from the same session (DLT 2000, Futrell et al. 2015, Futrell–Levy–Gibson 2020, Gibson et al. 2019, Temperley 2007). Their shared `occasion` is that Commonplace is considering dependency-length-minimization guidance for its writing instructions. The DLT and Futrell–Levy–Gibson ingests' Connections sections were read in full to avoid duplicating their edges and to find where SPLT adds something they lack.

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "writ|prose|sentence|reader|human|memory|bound|capacity|load|attention|soft|syntax|rewrite|read|locality|distance|order"`. Flagged: two-rewrites evidence note, human-writing-structures transfer, human-LLM differences, soft-bound traditions, soft degradation, feasibility-is-the-heaviest-fork, writing styles / underspecification, design-for-the-first-time-human, human analogies suggest functions.
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md' | rg -i "writ|prose|style|sentence|plain"`. Hits: ADR 116, ADR 022, write-brief proposals. None concern sentence-level syntax. No reference target.

**Description listing:** `rg -m1 '^description:'` over the flagged theory candidates and over `kb/sources/{futrell-*,gibson-2019-*,temperley-*,skill-and-working-memory,simplification-*,05-attention-*}.ingest.md`.

**Tag heads:** `kb/tags/` listing read. There is no writing-conventions or psycholinguistics tag. `kb/tags/document-system-README.md` was read (its Writing Conventions section is the nearest curated area). The snapshot has no `tags:`, so the by-tag rg was not applicable.

**Body search:**
- `rg -n -i "working memory|parse load|parsing load|center-embed|nested|dependency (length|distance|locality)|locality|heaviness|short before long|garden.path|reading time|psycholinguist" kb/theory kb/tags kb/reference kb/agentic-systems kb/agent-memory-systems -l`. About 60 files, mostly the "nested" and "locality" keywords in architecture contexts (directory nesting, freshness locality). The substantive hits were `two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md` ("parsing load", lines 10, 30, 34) and `soft-bound-traditions-as-sources-for-context-engineering-strategies.md` (working-memory row, line 18; "different failure modes", line 77).
- `rg -l -i "working memory|psycholinguist|sentence process|reading time|dependency length|lost in the middle|plain language|readab" kb/sources/*.ingest.md`. Mostly agent "working memory" keyword hits. Kept only `skill-and-working-memory.ingest.md`.
- `rg -l "gibson-1998|SPLT|Syntactic Prediction Locality" kb --glob '*.md'`. No hits. No existing artifact cites SPLT.
- `rg -n -i "storage|1998|SPLT|predecessor" kb/sources/gibson-dependency-locality-theory.ingest.md`. The DLT ingest names Gibson 1998 only as summarized evidence. It does not discuss the SPLT-to-DLT revision of the storage function.
- `rg -n -i "SPLT|1998|maximal|peak" kb/sources/{gibson-2019,temperley-2007,futrell-dependency-length-minimization}*.ingest.md`. Temperley ingest lines 166–167 name the open choice "words and the sum" versus "referents and the peak". SPLT §2.5 is the primary statement of the peak measure.
- `rg -l -i "dependency length|dependency locality|gibson" kb/work kb/log.md`. No hits. There is no workshop for the writing-guidance occasion yet (noted for context only, since `kb/work/` is excluded).

**Link following:**
- `feasibility-is-the-heaviest-forks-net-load.md` was read in full. It links to soft degradation and to context efficiency. The "load is more than token count" paragraph and the soft-degradation Complexity section both parallel SPLT's same-length, different-complexity contrast.
- `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` was read through its three dimensions (volume, interference, complexity). Its "token count alone does not predict usable capacity" claim matches SPLT §2.5 on a human processor. Gibson's footnote 7 (similarity-based interference, after Lewis) maps onto its interference dimension.

**Candidate evaluations:**
- DLT ingest: kept. It is the direct successor, and the comparison axis (storage-cost function) is load-bearing for which version a writing rule cites.
- Temperley ingest: kept. Sum versus peak is an explicitly open choice that this source settles on the Gibson side.
- Futrell–Levy–Gibson ingest: kept as compares-with on production versus comprehension. SPLT §4 is the primary place where the comprehension cost is conjectured to drive production heaviness choices, and Futrell–Levy–Gibson shows the production regularity without testing reader cost.
- Two-rewrites evidence note: kept as is-evidence-for, with a distinct SPLT payload (peak load and right-branching reordering).
- Human-writing-structures transfer note: kept as is-evidence-for (human-side failure for heavy-last ordering), with the LLM gap.
- Soft-degradation note: kept as compares-with on "load is structural, not length".
- Soft-bound traditions note: kept as compares-with (saturating per-item cost versus a count bound).
- Human-LLM differences note: the DLT ingest already holds this edge. Kept as one optional edge only if the future SPLT ingest does not route through the DLT ingest. Listed under Rejected to avoid duplicating the edge.

## Connections Found

All are candidates for the future `kb/sources/gibson-1998-linguistic-complexity-locality.ingest.md`.

- [The Dependency Locality Theory (ingest)](../../../../sources/gibson-dependency-locality-theory.ingest.md) -- **compares-with**: the shared axis is the storage-cost function. SPLT makes memory cost grow, and saturate, with the distance a prediction has been held (§2.3, §2.6.7). Its §6 argues that, under activation, only one of the two costs should be distance-based. DLT is the revision that follows. A writing rule citing "Gibson" must say which storage model it assumes, because the two predict different costs for one long held expectation.
- [Temperley 2007: dependency length in written English (ingest)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) -- **compares-with**: the shared axis is how dependency cost is aggregated. Temperley measures in words and sums. SPLT §2.5 argues from examples 13–15 that judged complexity tracks the peak load at one parse state, not the total or the average. That ingest names the choice as open for any lint check. This source is the primary argument for the peak side.
- [Dependency Locality as an Explanatory Principle for Word Order (ingest)](../../../../sources/futrell-levy-gibson-dependency-locality.ingest.md) -- **compares-with**: the shared axis is production versus comprehension. That paper shows that writers' word orders minimize distance, but it reviews and does not test reader cost. SPLT §4 is where the comprehension-cost model is conjectured to extend to production heaviness choices. The conjecture depends on a stated condition: the producer plans little right-hand structure ahead. The two together show where the link from "writers do this" to "readers benefit" is asserted and where it is tested.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **is-evidence-for**: the note treats "parsing load" as undifferentiated. SPLT adds two points the DLT edge lacks. First, difficulty is set by the heaviest point in the sentence, so a rewrite only needs to lower the peak. Second, reordering a nested sentence into right-branching form removes overload while keeping every word and relation (examples 13 versus 14). That is a third option beside the note's syntax-or-repetition tradeoff. The source covers human readers only and does not corroborate the agent-read result.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: for the "heavy constituent last" and "no nested relative clauses" conventions, SPLT names the human failure each convention prevents. That failure is peak memory load from several simultaneously held predictions. The note's per-convention test can then ask whether LLM readers share it. The source does not answer that question.
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **compares-with**: the shared axis is load that is not predicted by length. In SPLT, two sentences with the same words and meaning differ from easy to unprocessable because of structure (§2.5). Gibson's footnote 7 also names similarity-based interference as a further cost. These parallel the note's complexity and interference dimensions in a well-studied human processor. The mechanisms are different, so the edge gives an analogy and a vocabulary, not evidence about models.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- **compares-with**: the shared axis is the shape of a working-memory bound. That note's row gives a count bound (about four chunks). SPLT §2.6.7 gives a per-item cost that saturates after two or three intervening referents, so overload comes from how many long predictions are held at once (§3.5), not from one very long one. This refines the note's forgetting-versus-dilution caveat further than the DLT edge does.

## Bidirectional Candidates

- [The Dependency Locality Theory (ingest)](../../../../sources/gibson-dependency-locality-theory.ingest.md) <-> source -- **compares-with**: the DLT ingest's Limitations say Gibson "does not commit to the storage–integration relation". The SPLT ingest documents the earlier, committed version and its §6 self-critique. A return link lets a DLT reader see why the storage function changed. The sibling ingest is untracked and still in flight, so its author can add the edge before commit.
- [Temperley 2007 (ingest)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) <-> source -- **compares-with**: Temperley lines 166–167 already contrast "words and the sum" with "referents and the peak" and attribute the peak to Gibson. The return link would point that attribution to its primary argument.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → future SPLT ingest -- under `kb/theory/` rules, the note's Inference section could cite the ingest for "peak, not total, parse load" and for reordering as a relation-preserving alternative. This applies only if the DLT ingest's recommended edit has not already settled on a single source.
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) → future SPLT ingest -- this is weak. The note could cite a human analogue in its Complexity section. Its evidence posture is model benchmarks, so an author may reasonably decline.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- passes the articulation test, but the DLT ingest already holds the same compares-with edge with the same payload (a fixed-capacity human parser whose LLM counterpart must be checked). A second, identical edge from SPLT adds no traversal value. Reconsider it only if the SPLT ingest is written to stand alone.
- [Skill and Working Memory (ingest)](../../../../sources/skill-and-working-memory.ingest.md) -- the fixed-pool-versus-learned-capacity axis is already on the DLT ingest. SPLT's single-pool assumption (§2.4, §2.6.3, King and Just span groups) is the same assumption, so a second edge would be a duplicate.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../../../theory/feasibility-is-the-heaviest-forks-net-load.md) -- the "peak not total" structure parallels SPLT §2.5, but the shared axis is too abstract for a direct edge. A reader following it would get an analogy without a mechanism. Moved to Synthesis Opportunities.
- [Attention Is All You Need (ingest)](../../../../sources/05-attention-is-all-you-need.ingest.md) -- the distance-cost comparison is already authored from the Futrell–Levy–Gibson ingest. SPLT adds nothing specific to the architecture comparison.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- SPLT uses minimal pairs to rule out lexical, plausibility and ambiguity rivals. That is ordinary good practice rather than evidence for the note's specific claims about bundle attribution or unrun treatments. The Futrell–Levy–Gibson ingest already holds the stronger edge.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- this is a caution about architecture, not prose. SPLT does not suggest an agent component boundary.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- it concerns context-file style genres (prescriptive, conditional), not sentence syntax. The overlap is keyword-only.
- `kb/agent-memory-systems/` and `kb/agentic-systems/` reviews matching "working memory" -- these are agent-memory product terms with no shared mechanism. Rejected as keyword-only.
- `kb/reference/` -- no artifact concerns sentence-level writing guidance. ADR 116 (one word per concept) is about naming, not syntax. No see-also is warranted.

## Index Membership

- [document-system tag](../../../../tags/document-system-README.md) -- this does not apply directly: tag heads list notes, not ingests, and no theory note on locality-based writing rules exists yet. Once the theory note recommended by the Futrell–Levy–Gibson ingest exists, it would belong in that head's Writing Conventions section and would cite this source.

## Synthesis Opportunities

- **Peak load, not total load, sets feasibility on bounded processors.** SPLT §2.5 (human parse: breakdown at the heaviest parse state; right-branching additions are free), [feasibility is the heaviest fork's net load](../../../../theory/feasibility-is-the-heaviest-forks-net-load.md) (agent decomposition: the heaviest fork decides), and [soft degradation](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) (load is structural, not token count) all have the same shape. In each, restructuring lowers the maximum without lowering the total. A synthesis would have to show that a shared mechanism exists and not only a shared max-operator. Otherwise it stays an analogy and belongs in the log.
- **Writing-guidance theory note.** The six Gibson/Futrell/Temperley ingests together could support the bounded word-ordering note that the Futrell–Levy–Gibson ingest recommends. SPLT would contribute three things to it: the peak measure, saturation (one long dependency is acceptable, two held at once are not), and the right-branching reordering move. That note would also need to state which storage model it assumes (SPLT or DLT).

## Maintenance Observations

- The five sibling Gibson/Futrell/Temperley ingests are untracked in Git at the time of this run. Edges proposed here into them, and the bidirectional candidates, depend on those files being committed.
- There is no tag for writing conventions or for human reading cost. If the planned theory note and its source cluster grow, the document-system head's Writing Conventions section is the current home. A dedicated tag is not yet warranted.

## Flags

- **Tension to carry, not resolve:** SPLT (storage cost grows with distance and saturates) and DLT (storage cost fixed per predicted head) disagree about one long held expectation. Gibson himself flags the conceptual weakness of making both costs distance-based (§6). Any writing rule that cites this source cluster must choose a storage model or stay agnostic.
- **Transfer gap:** every edge is human-reader-only. The future ingest should keep the LLM-untested qualifier beside each is-evidence-for edge, as the sibling ingests do.
- **Split candidate:** no. The source makes one unified theoretical claim.
