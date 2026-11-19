---
description: "Local connection discovery for Purdue OWL's revision-priority guidance before isolated ingest drafting, preserving its lower-order-first exceptions."
type: types/connect-report.md
source: "kb/sources/.snapshots/purdue-higher-order-lower-order-concerns.md"
source_has_frontmatter: true
date: "2026-11-13"
depth: standard
---

# Connection Report: Higher Order Concerns (HOCs) and Lower Order Concerns (LOCs)

**Source:** `kb/sources/.snapshots/purdue-higher-order-lower-order-concerns.md`, captured from the [Purdue OWL original page](https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html).

This is discovery context for isolated ingest drafting, not an instruction to incorporate local claims into the source summary. The snapshot is immutable. All outbound recommendations below belong to the future `kb/sources/purdue-higher-order-lower-order-concerns.ingest.md`, which was absent at discovery time. No edges have been authored.

The source recommends prioritizing thesis/focus, audience/purpose, organization and development over sentence structure and grammar. It explicitly allows movement between the two levels and lower-order-first repair when surface errors prevent readers from reaching the thesis. It is institutional writing advice, not a comparative experiment on revision order or evidence about agent execution.

## Discovery Trace

### Setup and search surfaces

Read the connect skill, global connect-report type, complete snapshot, source collection contract and reports collection contract. The source contract authorizes prospecting theory, reference, agent-memory-systems, agentic-systems, tags and other sources. It excludes work and instructions as connection destinations. Neither was prospected, including workshop links encountered in candidates. The snapshot has frontmatter but no tags; there was no source-tag query to run.

For each of the six authorized local collections, generated the complete title surface once using:

`rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`

The combined title output was truncated by the tool; recovered its missing opening portion from the tool's full-output file. Resolved the three initial theory title candidates using `rg -l -F` with their exact `# ` title strings. Read all six collection `README.md` heads in full. These heads mostly route rather than enumerate the relevant revision claims.

Ran the following exact search patterns for each destination, substituting its collection path:

- Description scan: `rg -n -i '^description:.*(writ|revis|edit|readab|concern|audience|purpose|organiz|polish)' kb/<destination>/ --glob '*.md'`.
- Direct-concept search: `rg -n -i 'higher.order|lower.order|HOCs|LOCs|revision order|structural revision|surface polish' kb/<destination>/ --glob '*.md'`.
- Adjacent-concept search: `rg -l -i 'revision|revising|copyedit|audience and purpose|sentence.level|sentence.by.sentence' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`.

Recovered the truncated beginning of the description/body output from the tool's full-output file. No semantic-search service, MCP tool, external browsing or numerical relevance score was used. Brief hits, if any, were treated as document context rather than separate destinations.

### Theory

The title surface first exposed the low-degree-of-freedom ordering note, warranted-reader-update note, human-writing-transfer note and simplification comparison. Descriptions confirmed their different jobs. Fully read the first three and the simplification evidence note. Kept the first three as comparisons or transfer context, not as claims Purdue empirically establishes.

The direct-concept query yielded no theory account specifically defining Purdue's HOC/LOC distinction. Generic higher-order revision hits concern self-improvement rather than prose priorities. The adjacent query re-exposed the simplification evidence note; rejected it as direct ordering evidence because its treatments compare editing instruments, not HOC-first versus LOC-first sequences.

Followed the warranted-reader-update note one hop to the bare-writing-prompt note, and the low-degree note one hop to decomposition heuristics; read both fully. The former adds commission underspecification rather than a new revision-order relation; the latter repeats the option-count ordering already represented by the low-degree note. Neither was retained as another edge. Read the theory collection contract to distinguish advice from corroborating tests and to assess possible return links. No theory reverse edge was retained: Purdue does not test these theory claims.

### Reference

The title surface first exposed the one-improvement-procedure proposal. Its description and the direct-concept body query re-exposed it; lines 80–83 explicitly prescribe higher-order checks before editing. Read the complete proposal and reference collection contract. Kept a sparse ingest-to-proposal companion edge and a separately justified proposal-to-source qualification edge.

The reference README exposed review architecture, full-pass closure and review-system operations. Rejected these as additional connections: the source offers no specific machinery for result freshness, publication approval or workflow closure. The proposal is the precise local place where the revision-order comparison matters. It is a live proposal, not shipped behavior; current working-tree modifications were present and were read without alteration.

### Agent memory systems

Read the historical collection README; scanned its complete titles, matching descriptions and both body-query result sets. The direct query's secure-wiki higher-order-summary hit concerns promotion of retained knowledge, not revision of thesis versus grammar. Agent-R's revision trajectories and agentic-harness-engineering descriptions concern training or runtime adaptation. Rejected these at title/description/snippet screening: no named shared revision-priority mechanism justifies a link from Purdue. No candidate warranted full-document follow-up or reverse-edge authoring in this destination.

### Agentic systems

Read the collection README; scanned complete titles, matching descriptions and both body-query result sets. The academic-research-skills curated entry suggests a research pipeline, but supplies no HOC/LOC sequencing match. Dynamic Cheatsheet's format-only admission and skill-optimizer revision hits concern admission or optimization, not an editorial ordering rule. Rejected these screening matches rather than equating all staged workflows with higher-order-first writing. No retained outbound or reverse-edge candidate.

### Tags

Read the tags index, then its prose-readability and document-system heads in full. The prose-readability head re-exposed the human-writing-transfer and simplification-comparison notes. It has `complete: true`; no by-tag search was run for that tag. The snapshot carries no tags in any case. The document-system head supplies useful scope context but no closer revision-order claim.

The source contract names tags as a prospecting surface but authorizes no source-to-tag relationship label. Used these heads for navigation, not as manufactured footer edges. Sources are outside tag-participating collections, so no member-list insertion is proposed.

### Other sources

Read the sources README; scanned complete titles, matching descriptions and both body-query result sets. The title surface first exposed *The Levels of Edit*; its description confirmed the distinction between commissioned scope and execution order. Read the entire ingest and retained it as the strongest source-to-source comparison. It also re-exposed the low-degree note and one-improvement proposal through existing links.

Other description hits about writing-as-thinking, dependency locality and AI-voice rejection concern different mechanisms. Rejected these at description screening: they do not independently help distinguish the source's priority rule and exceptions. No additional source was retained merely because it concerns prose.

### External

No external prospecting. The original Purdue page was already present in the snapshot metadata and body and is retained as the future ingest's derivation target. The snapshot's paragraphing and punctuation handouts are already-known but rejected: they elaborate individual writing tasks without adding the revision-priority distinction this discovery serves.

### Candidate origins

- kb/theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md — titles, link-following
- kb/theory/warranted-reader-update-is-the-objective-of-substantive-writing.md — titles, descriptions
- kb/theory/human-writing-structures-transfer-to-llms-because-failure-modes.md — titles, descriptions, curated-head
- kb/reference/proposals/one-improvement-procedure-over-atomic-instructions.md — titles, descriptions, body-search, link-following
- kb/sources/levels-of-edit-1980.ingest.md — titles, descriptions, body-search
- https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html — known

## Connections Found

These are candidate edges from the future ingest, never additions to the snapshot.

- [The Levels of Edit ingest](../../../../sources/levels-of-edit-1980.ingest.md) — **compares-with**: Purdue distinguishes revision priorities and permits exceptions; JPL's cumulative editing levels commission sets of services rather than prescribe execution order. The comparison prevents a future writer from treating every editorial hierarchy as the same sequencing rule.
- [Solve low-degree-of-freedom subproblems first](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — **compares-with**: both discuss order, but the theory note ranks decisions by remaining viable options, whereas Purdue ranks writing concerns by their role in the paper and reader access. A thesis can have many possible revisions and still deserve early attention. Purdue does not count alternatives or test the option-preservation mechanism.
- [Warranted reader update is the objective of substantive writing](../../../../theory/warranted-reader-update-is-the-objective-of-substantive-writing.md) — **compares-with**: Purdue's audience, purpose, focus and development checks compare with Commonplace's selection of an intended reader update before optimizing polish. The local theory adds relevance and warrant requirements that are not Purdue's HOC/LOC definition. Following the link helps translate writing advice into KB contribution selection without attributing that translation to Purdue.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **see-also**: use its per-convention failure-mode test before turning Purdue's human revision advice into an agent procedure. Purdue supplies neither agent-task results nor evidence that experienced-human switching behavior transfers to LLM editing.
- [One improvement procedure over atomic instructions](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) — **see-also**: the proposal's default composition is the concrete local application to inspect. It extends higher-order concerns to existence, boundaries and placement, and justifies ordering by potentially discarded editing work. Purdue includes organization among HOCs and explicitly permits LOC-first repair; the comparison exposes choices the proposal should not present as inherited unchanged from Purdue.
- [Purdue OWL original page](https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html) — **derived-from**: the future ingest analyzes this already-known original source; it should preserve both the default priority and exceptions rather than derive its source account from local proposals.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [One improvement procedure over atomic instructions](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) → [Purdue OWL original page](https://owl.purdue.edu/owl/general_writing/mechanics/hocs_and_locs.html) — **evidenced-by** under the reference collection's external authorization: Purdue qualifies the proposal's appeal to composition-field wording. Its default is not an unconditional ban on early lower-order repair; organization is explicitly higher-order and surface defects can block access to the thesis. This is a source-boundary qualification, not evidence that Purdue tested or refuted the Commonplace proposal. After an ingest exists, prefer citing that tracked ingest for Commonplace's analysis, with appropriately grounded source support. Never author a durable link to the ignored snapshot. No derivational lineage is asserted without evidence that the proposal was actually worked out from this source.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — useful local editing evidence, but it does not compare revision orders. The source neither explains those results nor supplies evidence that a different HOC/LOC schedule would improve them.
- [A bare writing prompt does not determine its intended contribution](../../../../theory/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) — audience/purpose overlap is real, but the commissioned-prompt ambiguity mechanism is distinct. The warranted-reader-update comparison already provides the useful contribution-selection path.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — duplicates the retained low-degree comparison while adding unrelated context-budget machinery.
- The memory-system and agentic-system screening hits named in the trace — revision, hierarchy and staging alone do not establish an editorial-priority connection.

## Index Membership

None. Do not index the ignored snapshot. A future ingest may use source-scoped topical tags after judging its authored analysis, but source tags do not add it to participating-collection member lists. No tag assignment is made by this report.

## Synthesis Opportunities

A possible comparison frame combines Purdue, the [JPL ingest](../../../../sources/levels-of-edit-1980.ingest.md), the [low-degree ordering note](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) and the [improvement proposal](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md): distinguish commissioned service scope, concern priority, option-count order and downstream invalidation. These axes need not rank work identically. The JPL ingest already articulates much of this distinction, so a future writer should extend or test that comparison rather than create a duplicate synthesis. Neither Purdue nor JPL establishes an optimal agent-editing schedule.

## Maintenance Observations

The report template's source hyperlink into the ignored snapshot triggered `validation.base.snapshot-link`. The source is therefore identified by its exact repo-root path in metadata and prose, with navigation to the original URL. The paired ingest does not yet exist; no placeholder link or ingest was created.

## Flags

- Keep discovery context separate from source reconstruction during isolated drafting. Local invalidation and option-count rationales are comparisons, not explanations attributed to Purdue.
- Preserve the source's two qualifications: movement between HOCs and LOCs can be natural, and lower-order errors can require early repair when they obstruct reading. A strict universal HOC-first rule would misrepresent it.
- The proposal's treatment of framing and flow as lower-order should be mapped explicitly against Purdue's treatment of organization as higher-order; do not silently unify the categories.
- This is not a split candidate: the kept links concern one revision-priority question, not three independent topic areas.
- The JPL ingest was untracked and the improvement proposal modified in the current working tree. These findings describe local discovery state, not a commit-pinned corpus. No source, library, index or workshop artifact was changed.
