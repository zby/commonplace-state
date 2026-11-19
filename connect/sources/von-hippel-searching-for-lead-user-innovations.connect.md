---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/von-hippel-searching-for-lead-user-innovations.md"
source_has_frontmatter: true
date: "2026-08-29"
depth: standard
---

# Connection Report: Application: Searching for Lead User Innovations

**Source:** [Application: Searching for Lead User Innovations](../../../../sources/.snapshots/von-hippel-searching-for-lead-user-innovations.md)

## Discovery Trace

**Description and title scans:**
- Read the curated heads for `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`, plus the foundations, discovery, context-engineering, and evaluation tag heads. Generated each destination's complete title surface with `rg -N --no-heading -m1 '^# ' <destination> --glob '*.md'` (386 note artifacts, 157 reference artifacts, 174 agent-memory artifacts, 12 agentic-system artifacts, and 335 source artifacts at discovery time).
- `rg -n -i '^description:.*(analog|borrow|transfer|problem match|method search|mechanism match|recognition|search|cross-domain|cross domain|extreme)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` surfaced the problem-match, mechanism-bounded transfer, recognition, experimental-contrast, enriched-search, and three analogy-source candidates.

**Body search:**
- `rg -n -i 'problem match|method search|mechanism match|source[- ]method|candidate responses' ...` -- kept the problem-match note as the closest existing theoretical landing: von Hippel's advanced-analog search uses a related but more extreme problem to select source fields without itself supplying a general transfer warrant.
- `rg -n -i 'analogical|analogy|relational structure|surface similarity|shared mechanism' ...` -- kept the mechanism-boundary note and the Gick-Holyoak and Shannon source comparisons; rejected model-internal analogy work as a different object.
- `rg -n -i 'cross[- ]domain|out[- ]of[- ]field|outside (the )?(target )?market|similar problems?.*extreme|extreme.*constraints|lead user' ...` -- confirmed no existing use of von Hippel's term and no matching whole-system analysis.
- `rg -n -i 'pyramiding|snowballing|network(ing)?.*expert|expert.*network(ing)?' ...` -- found no existing KB artifact that names pyramiding as a research-search method.

**Link following:**
- Followed the problem-match note to the mechanism-bounded transfer note and the soft-bound-traditions survey. The chapter is a concrete industrial search method for finding source responses; its same-need/more-extreme criterion does not displace the KB's separate mechanism and target-side checks.
- Followed the recognition note to the discovery head. Von Hippel explicitly treats discovering a relevant analog as a creative act and offers pyramiding through expert nominations as an operational aid, giving the recognition bottleneck a source-side instance.
- Read the experimental-contrast note against the chapter's 3M account. The observed treatment is the lead-user process as a bundle, including trend research, pyramiding, target-market users, advanced-analog users, workshops, and team synthesis; the comparison does not independently vary advanced-analog search.
- Read the Gick-Holyoak, transformer-analogy, and Shannon ingests. Gick-Holyoak and Shannon provide useful contrasts for recognizing and deliberately seeking remote analogies. The transformer paper studies learned relational-role alignment rather than source-field search and was rejected as too remote for this ingest.

**Per-destination result:**
- `notes`: five useful candidates spanning source-method search, transfer bounds, recognition cost, experiment scope, and enriched search.
- `reference`: no outbound candidate beyond the theory links; `source-adoption-policy.md` restates the mechanism gate but adds no source-specific reader path.
- `agent-memory-systems`: skipped after the curated head, title surface, and focused body searches exposed no implementation-review trigger.
- `agentic-systems`: skipped after the curated head, complete 12-title surface, and focused body searches exposed no whole-system analysis trigger.
- `sources`: two useful comparisons with human analogical problem solving and Shannon's analogy operator; the transformer analogy ingest was rejected as a different mechanism and object.
- `external`: authorized but not prospected; the captured chapter is the only supplied external target.

## Connections Found

- [Problem matches guide method search; mechanism matches bound transfer](../../../../notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md) -- **is-evidence-for**: von Hippel operationalizes a problem match as a related need faced more extremely, often under different constraints, and uses that relation to select lead users and source fields worth examining; the chapter supports the search half without establishing the KB's broader transfer rule.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **compares-with**: the chapter searches by need correspondence and adapts out-of-field solutions, while the note supplies the stricter downstream test needed before treating an analog-field solution as warranted in the target.
- [Recognition, not linking, is the hard problem in knowledge systems](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -- **is-evidence-for**: von Hippel calls discovery of a relevant analog a creative act and uses pyramiding through increasingly expert nominations to help locate relationships that ordinary target-market search misses.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **compares-with**: the 3M natural experiment compares a bundled lead-user process with conventional projects, so its results cannot isolate advanced-analog search from target-user search, pyramiding, workshops, team composition, or synthesis.
- [Brainstorming how to enrich web search](../../../../notes/brainstorming-how-to-enrich-web-search.md) -- **compares-with**: advanced-analog search is an established domain-search pattern that redirects inquiry by a problem relation and expert referrals, while the KB proposal redirects web search through inter-result structure; the chapter does not test the web-search transfer.
- [Analogical Problem Solving](../../../../sources/gick-holyoak-analogical-problem-solving.ingest.md) -- **compares-with**: both sources treat noticing a remote analogy as difficult, but Gick and Holyoak experimentally vary relevance cueing in human problem solving whereas von Hippel offers an industrial search procedure using lead-user nominations.
- [Creative Thinking](../../../../sources/creative-thinking-by-claude-shannon.ingest.md) -- **compares-with**: Shannon names analogy as a general creative operator for finding a similar solved problem; von Hippel supplies a narrower operational method for finding fields where the same need is more extreme.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Problem matches guide method search; mechanism matches bound transfer](../../../../notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md) → source -- **evidenced-by**: cite the advanced-analog-field definition and pyramiding method as an industrial instance where a discriminating problem relation guides source search without itself settling target adoption.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → source -- **evidenced-by**: use the 3M account as a bundled-treatment case if the note needs a non-agent example of why successful compound methods do not identify the contribution of one named component.
- [Brainstorming how to enrich web search](../../../../notes/brainstorming-how-to-enrich-web-search.md) → source -- **evidenced-by**: use advanced-analog search and pyramiding as prior method shapes for query redirection, explicitly leaving web-search effectiveness untested.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md) -- rejected: it studies learned relational-role alignment inside transformer representations, not deliberate search for a source field whose users face a related but more extreme need.
- [Source-adoption policy](../../../../reference/source-adoption-policy.md) -- rejected: its mechanism gate is already represented by the stronger note-level candidate, and a `see-also` edge would add little traversal value.
- [Soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- rejected: it is an instance of problem-guided source search already synthesized by the problem-match note; a second edge would duplicate that route.

## Index Membership

None.

## Synthesis Opportunities

None. The useful synthesis -- a problem match guides analog-field search while a mechanism match bounds transfer -- already exists in the problem-match note.

## Maintenance Observations

None.

## Flags

- The chapter's 3M evidence concerns a bundled lead-user process and mostly forecast outcomes. Treat advanced-analog search as one component of the observed method, not as an independently identified cause of the reported advantage.
- The retained source is the complete standalone Chapter 10 PDF but an excerpt from the book. It does not include the book's bibliography or earlier chapters that establish lead-user theory.
