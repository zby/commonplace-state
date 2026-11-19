---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/gibson-1998-linguistic-complexity-locality.ingest.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Ingest: Linguistic complexity: locality of syntactic dependencies (Gibson 1998)

**Source:** [Ingest: Linguistic complexity: locality of syntactic dependencies (Gibson 1998)](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md)

The ingest already authors eight footer edges: `derived-from` the DOI, `is-evidence-for` two theory notes, `compares-with` two theory notes and three sibling ingests. All seven local edges are the "kept" set of the earlier snapshot connect run ([gibson-1998-linguistic-complexity-locality.connect.md](./gibson-1998-linguistic-complexity-locality.connect.md)). This run re-checks them against the written ingest and looks for what is new: siblings committed or written after that run, and theory-side reverse edges.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, "Outbound links". Destinations: `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels per destination as in the table (`is-evidence-for` theory/agent-memory-systems; `compares-with` theory/sources/agent-memory-systems/agentic-systems; `see-also` broad, sparingly). External prospecting skipped; the only external target is the DOI already present as `derived-from`.

**Prior report reused:** the snapshot-run report's trace (titles listing, theory/reference body searches, `kb/tags/document-system-README.md`, link following through feasibility and soft-degradation). Its conclusions were not re-derived; the new searches below target gaps.

**Sibling ingests:** read `description:` of all six sibling ingests and grepped each for `gibson-1998|SPLT|1998`. Only the DLT ingest names "Gibson 1998" (line 22, as primary-report pointer). No sibling links to this ingest yet.
- `rg -n -i "peak|maximal|saturat|heav|end-weight|EIC|comprehension|Hawkins|predictab|expectation|surprisal" kb/sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md` -- substantive hits at lines 45-55 (EIC and end-weight as rivals to DLM; expectation may explain part of comprehension benefit), 163, 200-206 (production evidence is not comprehension evidence; weak naturalistic comprehension effect). Kept: this supplies exactly the rivals the SPLT ingest's Limitations say heaviness "is not tested against".
- `rg -n -i "peak|maximal|saturat|heav|SPLT|comprehension|surprisal|nest|center" kb/sources/gibson-2019-how-efficiency-shapes-language.ingest.md kb/sources/futrell-dependency-length-minimization.ingest.md` -- Futrell 2015 line 25 (summed length; head-final case-marking languages minimize less, morphology conjecture) and line 42 (short-before-long after head). Gibson 2019 lines 177-190 (review restates locality and heavy-last). Evaluated below.

**Body search (theory, tags, reference, agentic-systems):**
- `rg -l -i "dependency length|dependency locality|center-embed|right-branching|heavy-last|heavy constituent|end-weight" kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/**'` -- only the seven sibling ingests, a Sutskever-list chapter, and one meta-harness analysis file (keyword-only, no syntactic content). No theory note carries the topic.
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "sentence|prose|syntax|reader|readab|writing|nest|peak|working memory|parse"` -- 13 titles; new relative to prior run: link-strength-in-position-and-prose, warranted-reader-update (both about link/claim placement, not syntax; rejected).
- `rg -l -i "sentence length|short sentences|long sentences|word count" kb/theory kb/reference kb/agentic-systems --glob '*.md'` -- `text-testing-framework.md` (line 27, "Length / reading time / sentence length" as a deterministic check), `three-simplification-passes-exposed-different-tradeoffs.md` (line 46, against judging a simplifier by word count), two-rewrites (already linked); agentic-systems hits are archived run results (rejected, keyword-only).
- Followed `text-testing-framework.md` to its condensed note `automated-tests-for-text.md` (line 17, deterministic checks include "length"). Kept as compares-with.
- `rg -n "gibson|futrell|temperley" kb/theory kb/tags kb/reference --glob '*.md'` -- no hits. No theory note yet cites any source in this cluster, so every theory-side edge is still only authored from the source side.
- `rg -n "sources/" kb/theory/human-writing-structures-transfer-to-llms-because-failure-modes.md` -- no source links at all; relevant to the reverse-edge bound below.
- `kb/theory/COLLECTION.md` outbound table read for the reverse direction: theory → sources uses `evidenced-by` (corroborates, qualifies or bounds), with the five-unquoted-source limit (ADR 082/122).

**Re-check of existing edges:** all seven local targets exist and each context phrase matches the target's actual claim. None is redundant with a sibling-held edge except as noted in Flags.

## Connections Found

All are candidates for a future edit of `kb/sources/gibson-1998-linguistic-complexity-locality.ingest.md`.

- [Temperley and Gildea 2018 review (ingest)](../../../../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) -- **compares-with**: the shared axis is rival explanations of heavy-last ordering and of comprehension benefit. The SPLT ingest's Limitations say its section 4 heaviness account "is not tested against those alternatives" and that expectation-based accounts are engaged only for ambiguity. That review names the alternatives concretely (Hawkins's EIC, production end-weight, n-gram predictability) and reports where DLM wins only where predictions diverge and where comprehension evidence is weak or confounded with expectation. A writer of the planned rules note gets the test the SPLT heaviness rule still owes. This is the main new edge; it did not exist at the snapshot run.
- [Automated tests for text](../../../../theory/automated-tests-for-text.md) -- **compares-with**: the shared axis is what a cheap deterministic prose check should measure. That note lists "length" among deterministic checks. SPLT section 2.5 argues that length and average load do not predict difficulty; the peak parse state does, and saturation means only overlapping long dependencies overload. Extractable Value 3 and 4 already state the lint consequence, so the edge tells an agent building a text check that sentence length is a weak proxy, for human readers. Lower priority than the Temperley-Gildea edge.

## Bidirectional Candidates

- [Temperley and Gildea 2018 review (ingest)](../../../../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) <-> source -- **compares-with**: that ingest presents DLT as the comprehension mechanism (line 48) and attacks its evidence. A return link would let its reader find the earlier, peak-based model whose heaviness derivation is the comprehension-side account it tests. The ingest is untracked, so its author can add the edge before commit.
- [The Dependency Locality Theory (ingest)](../../../../sources/gibson-dependency-locality-theory.ingest.md) <-> source -- **compares-with** (carried over from the snapshot run, still unauthored): the DLT ingest names Gibson 1998 only as a primary-report pointer and says Gibson does not commit to the storage-integration relation. The return link shows the committed SPLT version and its section 6 self-critique.
- [Temperley 2007 (ingest)](../../../../sources/temperley-2007-dependency-length-written-english.ingest.md) <-> source -- **compares-with** (carried over, still unauthored): its "referents and the peak" option should point to its primary argument here.

## Reverse-edge Candidates

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) → source -- **evidenced-by** under `kb/theory/` rules, phrased as bounding, not corroborating: human-reader theory says a rewrite need only lower the sentence's peak, and right-branching reordering is a relation-preserving third option beside splitting and repeating. The source predates the note and did not test it, so the context phrase must not claim corroboration.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source -- **evidenced-by** (qualifies): names the human failure mode behind no-nesting and heavy-last conventions. The note has no source links today, and seven sibling ingests compete for the same slot; under the five-unquoted-source limit, the note should cite at most one or two cluster ingests (DLT plus this one for peak and saturation is a reasonable pair) or quote them via `cp-skill-ground`.

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Text testing framework — source material](../../../../theory/text-testing-framework.md) -- potential **compares-with**: lists "Length / reading time / sentence length" as a Level A deterministic check (line 27). Same payload as the Automated tests for text edge; the frontmatter-free file should not receive a regular edge. Link the condensed note instead.

## Rejected Candidates

- [Futrell 2015, dependency length minimization (ingest)](../../../../sources/futrell-dependency-length-minimization.ingest.md) -- a head-final/Japanese axis exists (SPLT's Japanese stacking versus Futrell's weaker minimization in case-marking head-final languages), but neither ingest makes that axis load-bearing for writing rules, and the production-versus-comprehension axis is already held through the Futrell-Levy-Gibson edge. A second edge would duplicate traversal.
- [Gibson et al. 2019 review (ingest)](../../../../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) -- restates locality and heavy-last at review level; reaching it from the primary SPLT ingest adds nothing a reader of the DLT or Futrell-Levy-Gibson ingests lacks. Reconsider only if the planned rules note routes through the review.
- [Three simplification passes exposed different tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) -- argues against judging a simplifier by word count, which parallels SPLT's peak-not-length point, but its evidence is about rewrite procedures and relation drift, and the two-rewrites edge already carries the syntax payload. Weak analogy.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- still held by the DLT ingest with the same payload (rejected again, as in the snapshot run).
- [Skill and Working Memory (ingest)](../../../../sources/skill-and-working-memory.ingest.md) -- fixed-pool axis already held by the DLT ingest.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../../../theory/feasibility-is-the-heaviest-forks-net-load.md) -- peak-not-total is an abstract analogy only; left in Synthesis Opportunities.
- `kb/theory/link-strength-is-encoded-in-position-and-prose.md`, `kb/theory/warranted-reader-update-is-the-objective-of-substantive-writing.md` -- title hits on "prose"/"writing"; they concern link placement and claim value, not sentence syntax.
- `kb/reference/`, `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/tags/` -- no artifact concerns sentence-level processing cost; hits were keyword-only.

## Index Membership

- [document-system tag](../../../../tags/document-system-README.md) -- not directly: tag heads list notes, not ingests. The future dependency-locality writing-rules theory note would belong in its Writing Conventions area and cite this ingest.

## Synthesis Opportunities

- **Writing-rules theory note.** The seven-ingest cluster now has rivals (Temperley-Gildea), production regularities (Futrell 2015, Temperley 2007, Futrell-Levy-Gibson), and two comprehension models (SPLT, DLT). SPLT's distinct contributions are the peak measure, saturation, and relation-preserving right-branching reordering. The note must choose or stay agnostic on the storage model and keep LLM-reader benefit as untested.
- **Peak load sets feasibility on bounded processors** (carried over): SPLT section 2.5, feasibility-is-the-heaviest-fork, and soft degradation share a max-over-states shape. Analogy only until a shared mechanism is shown.

## Maintenance Observations

- No theory, tag or reference artifact links to any of the seven dependency-locality ingests. The cluster is entirely source-side until the planned theory note exists.
- The five-unquoted-source limit on theory notes will bind the planned rules note and any reverse edge into `human-writing-structures-transfer-to-llms-because-failure-modes.md`; the cluster's ingests all have empty Quotes sections, so quoting through `cp-skill-ground` will likely be needed.

## Flags

- **No split candidate.** One unified theoretical claim.
- **Tension carried, not resolved:** SPLT's distance-based, saturating storage cost versus DLT's fixed cost; and SPLT's peak aggregate versus Temperley's summed distance. The ingest already states both.
- **Existing edges sound:** all seven local footer edges re-checked; no change recommended. The ingest's `is-evidence-for` edges keep the human-only qualifier, as they should.
