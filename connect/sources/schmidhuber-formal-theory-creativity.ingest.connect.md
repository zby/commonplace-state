---
description: "Post-ingest discovery for the formal creativity and intrinsic motivation paper"
type: types/connect-report.md
source: kb/sources/schmidhuber-formal-theory-creativity.ingest.md
source_has_frontmatter: true
date: "2026-11-06"
depth: standard
---

# Connection Report: Formal Theory of Creativity, Fun, and Intrinsic Motivation

**Source:** [Accepted ingest](../../../../sources/schmidhuber-formal-theory-creativity.ingest.md)

## Discovery Trace

- Read the accepted ingest fully and applied the sources collection's outbound rules. Read the connect-report type and theory collection's inbound-authoring rules. This is a separate discovery pass on the authored analysis, after its checksum and validation guards passed.
- Reused this run's fresh title surfaces and curated landing reads for theory, reference, historical memory systems, agentic systems, tags, and sources. The pre-draft scan used `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` filtered with `curios|compress|explor|learn|surpris|reward|progress|predict|creativ|know|autonom|econom|experiment|problem`, plus description reads on selected candidates. No source tags require tag-head traversal.
- Ran a new post-ingest search: `rg -l -i 'predictor|compression progress|intrinsic reward|learning progress' kb/theory kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`. This broadened recall to predictor consumption and world-model notes; most new hits used predictors in unrelated senses, so no keyword-only edges were retained.
- Ran `rg -n 'schmidhuber-formal-theory-creativity|Driven by Compression Progress|fixed.decomposition'` on the six curated landing files; no new routing entry was found.
- Followed and fully read the ingest's fixed-decomposition note and theory-builder definition. Evaluated their source-directed reader needs independently of the ingest's outbound links. The former's discussion of update spaces offers a plausible comparison, not a reported test of its claim. The definition is a vocabulary authority, not a destination needing every assessed example as an inbound citation.
- Re-evaluated the earlier compression-progress ingest, search-allocation note, and objective-relative improvement note read during initial discovery. They remain useful outbound comparisons, but the existing companion source already provides the central mechanism to their readers.
- No close match emerged in reference, historical systems, current system reviews, or tags that warranted adding an edge. External searching was not performed; only the supplied primary PDF was considered. Workshop and instruction destinations were excluded.

## Connections Found

These are candidate connections, including some already present in the accepted ingest; no edits are made by this report.

- [Driven by Compression Progress](../../../../sources/driven-by-compression-progress.ingest.md) — **compares-with**: existing companion link correctly distinguishes this paper's explicit typology from an independent replication of the shared compression-progress mechanism.
- [Learning inside a fixed decomposition](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: the paper's predictor/interface/reward distinctions make the effective update-space question concrete, while the ingest explicitly avoids claiming that the reviewed studies compare alternative decompositions.
- [Theory builder](../../../../theory/definitions/theory-builder.md) — **defined-in**: supplies the four conditions used in the ingest's learning-claims assessment, including why fitted prediction errors alone do not establish stated criticism.
- [Search allocation before decisive evaluation](../../../../theory/open-ended-improvement-allocates-search-before-evaluation.md) — **compares-with**: predicted progress selects experiments before measured progress becomes available; useful for a later discussion of exploration control rather than claim acceptance.
- [Objective-relative improvement](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) — **compares-with**: intrinsic model improvement and external task benefit can diverge, as the paper expressly allows.
- [Original PDF](https://people.idsia.ch/~juergen/ieeecreative.pdf) — **derived-from**: primary source for the formal framework and retrospective claims.

## Bidirectional Candidates

None. The existing companion and definition links do not independently justify return links; no distinct reader need for this second treatment was established.

## Reverse-edge Candidates

None. The fixed-decomposition note could use a future implementation-level comparison, but this theoretical overview does not supply that test. Search-allocation and objective-relativity readers already have a route to the earlier compression-progress source; a second citation needs a distinct argumentative job.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Adding this paper to the theory-builder definition as a settled positive example: the ingest explicitly leaves stated criticism and its retention unestablished.
- Treating the fixed-decomposition note as empirically corroborated by this overview: the paper reviews different supplied configurations without a matched decomposition comparison.
- Predictor keyword matches in sentence-processing sources and model benchmarks: no shared exploration-control mechanism was established.

## Index Membership

None.

## Synthesis Opportunities

None. The existing compression-progress companion already connects intrinsic progress, search allocation, and external objectives.

## Maintenance Observations

None.

## Flags

- No inbound links are recommended or authored by this pass. Keep the source-only recommendation; new KB learning-loop designs still need experiments rather than importing the paper's broad human-creativity interpretation as established fact.
