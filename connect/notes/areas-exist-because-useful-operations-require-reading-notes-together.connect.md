---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: Areas exist because useful operations require reading notes together

**Source:** [Areas exist because useful operations require reading notes together](../../../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md)

## Discovery Trace

**Notes destination (`kb/notes/`):**
- Read curated head: [Notes](../../../../notes/README.md).
- No tag-README pass: source has `tags: []`, so there were no source-tag curated heads to read or `complete: true` skips to claim.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`
  - Flagged [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md) and [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) immediately from title overlap.
  - Flagged [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md), [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md), [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md), [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md), [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md), and [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md).
- Description listing: `rg '^description:' kb/notes/ --glob '*.md'`
  - Kept [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md): description matches the source note's "orientation needs one surface, comparison another" split.
  - Kept [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md): description operationalizes the source note's expected-yield criterion by ranking candidate notes before costly evaluation.
  - Kept [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md): description explains when orientation-level summaries really substitute for source reads.
  - Downgraded [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), and [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): useful navigation theory, but still one level above the source note's "which notes belong in a joint pass?" question.
- Body search: `rg -n "orientation|comparative reading|read(?:ing)? together|joint[- ]reading|cohort|expected yield|resolution-switch|tag-readme|tags|index|discovery" kb/notes/ --glob '*.md'`
  - Confirmed [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md) as the closest existing neighbor; inspection showed the source already links to it and the target already links back, so it is not a new candidate.
  - Confirmed [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) as a missing orientation-side extension: it repeatedly uses "orientation" and relies on curated-vs-generated index roles without naming the source note's orientation/comparative-reading split.
  - Confirmed [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) as a missing mechanism note: its orientation/accuracy distinction explains when a compressed surface can replace a full read, matching the source's compact-orientation/full-body-comparison distinction.
  - Confirmed [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) as a reverse-edge candidate: it names "orientation" and "synthesis setup: assemble the subset worth reading together" but does not link to the source note that turns those categories into an operational cohort rule.
  - Confirmed [A theory must scope a named system choice, not necessarily quantify it](../../../notes/a-theory-may-name-a-choice-only-as-a-bound-variable.md) already cites the source as evidence; no action needed.
  - Confirmed [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) mentions comparative reading only as a consumer of fixed descriptions, not as a note-selection rule; rejected.
- Link following:
  - Read [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md) first; followed its citations to [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) and compared its already-authored return edge.
  - Read [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md); source already links to it, but the target lacks the concrete read-together-cohort rationale, so only a return-link candidate remains.
  - Read [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) and [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md); both articulate reader gain beyond topical overlap.

**Reference destination (`kb/reference/`):**
- Read curated head: [Reference](../../../../reference/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`
  - Flagged [Navigation](../../../../reference/navigation.md), [004-Replace areas with tags](../../../../reference/adr/004-replace-areas-with-tags.md), [025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md), and [003-connect-skill-discovery-strategy](../../../../reference/adr/003-connect-skill-discovery-strategy.md).
- Description listing: `rg '^description:' kb/reference/ --glob '*.md'`
  - Kept [025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md): description matches the source note's claim that orientation and broader coverage may need separate surfaces.
  - Downgraded [Navigation](../../../../reference/navigation.md): useful current-system consumer of the theory, but the missing edge is more valuable from the reference note back into the theory than from the theory out to the reference doc.
  - Rejected [003-connect-skill-discovery-strategy](../../../../reference/adr/003-connect-skill-discovery-strategy.md) for this pass: it is historically important to the broader cluster, but ADR 025 is the cleaner current-state witness and the source already has an ADR 004 witness.
  - Confirmed [004-Replace areas with tags](../../../../reference/adr/004-replace-areas-with-tags.md) is already authored in the source note and therefore not a new connection candidate.
- Body search: `rg -n "areas|tags|comparative|orientation|index|discovery|navigation|resolution|scope|cohort" kb/reference/ --glob '*.md'`
  - [Navigation](../../../../reference/navigation.md) explicitly separates curated heads, scoped `rg`, and full reads, and already cites [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md); kept as a reverse-edge candidate under reference's `rests-on` rule.
  - [025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) explicitly records the current system's split between curated orientation heads and exhaustive generated listings; kept as an outbound `evidenced-by` candidate.
- Link following:
  - Read [Navigation](../../../../reference/navigation.md), [004-Replace areas with tags](../../../../reference/adr/004-replace-areas-with-tags.md), and [025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md).
  - Read [kb/reference/COLLECTION.md](../../../../reference/COLLECTION.md) to confirm that a reverse edge from a reference artifact to this note would use `rests-on`, not an invented theory-ward label.

**Types destination (`kb/types/`):**
- Read curated head: [Types](../../../../types/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`
- Description listing: `rg '^description:' kb/types/ --glob '*.md'`
- Evaluated [Tag README](../../../../types/tag-readme.md) and [Index](../../../../types/generated-index.md) as nearby structure, but rejected them: the source note is about when a bounded operational cohort is useful, not about the structure contract of a curated head or generated listing.

**Instructions destination (`kb/instructions/`):**
- Read curated head: [Instructions](../../../../instructions/README.md).
- Search pass shared with other lower-probability destinations: `rg -n "areas|tags|comparative|orientation|index|discovery|navigation|resolution|scope|cohort" kb/instructions/ kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`
- Evaluated hits in workflow docs and local skills; found no concrete procedure that adds ordering/defaults/stopping conditions to this specific methodology note, so there is no clean `operationalized-from` or `see-also` candidate from the source.

**Sources destination (`kb/sources/`):**
- Read curated head: [Sources](../../../../sources/README.md).
- The shared search only surfaced generic mentions of `/connect`, indexes, or discovery inside ingest reports; no already-known source in loaded context gave a direct witness for bounded read-together cohorts beyond the internal ADRs already inspected. No local-source candidate kept.
- External destination skipped: source `COLLECTION.md` authorizes `external`, but no user-supplied or already-loaded external target was in context, and open-web prospecting is out of scope for connect.

**Agent-memory-systems destination (`kb/agent-memory-systems/`):**
- Read curated head: [Agent Memory Systems](../../../../agent-memory-systems/README.md).
- Shared search produced broad discovery/indexing mentions but no review whose claim turns on bounded note cohorts for orientation versus comparative reading. No candidate kept.

**Agentic-systems destination (`kb/agentic-systems/`):**
- Read curated head: [Agentic Systems](../../../../agentic-systems/README.md).
- Shared search surfaced [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) on discovery vs commitment, but the articulation failed: it is about corpus triage infrastructure, not why useful operations require reading notes together. Rejected.

## Connections Found

- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -- **extends**: the source note says orientation and comparative reading need different surfaces; this note develops the orientation side by showing what curated grouping and context phrases add beyond a complete listing.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- **mechanism**: the source note says orientation can often use compressed representations while comparative reading usually needs fuller bodies; this note explains the stopping condition that makes an orientation summary substitutive instead of merely additive.
- [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) -- **extends**: the source note's expected-yield rule implies candidate notes should be filtered before expensive comparison; this note turns that implication into a concrete scaling strategy for `/connect`.
- [025-Complete generated indexes are build-time only; agents read curated heads plus scoped rg](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) -- **evidenced-by**: Commonplace's current design explicitly separates curated orientation surfaces from exhaustive generated listings instead of forcing one artifact to serve both jobs.

## Bidirectional Candidates

- [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) <-> source -- **grounds**: the target treats indexes and notes as resolution levels, but the return path to the source would explain why one of those levels exists as a bounded read-together cohort rather than as a generic abstraction layer.
- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) <-> source -- **grounds**: the target's curation-vs-generation distinction assumes orientation is a distinct operation from comparative reading; the source note states that operational split directly.

## Reverse-edge Candidates

- [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → source -- **grounds**: it names "orientation" and "synthesis setup" as distinct navigation tasks, and this source note is the cleanest local argument for why synthesis setup needs a bounded, operation-relative cohort.
- [Navigation](../../../../reference/navigation.md) → source -- **rests-on**: the navigation stack separates curated heads, scoped search, and full reads, and the source note explains why broad discovery surfaces do not replace later joint-reading selection.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -- strong pointer-level navigation theory, but it does not answer the source note's cohort question: why some operations need several notes processed together.
- [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) -- explains pointer metadata by navigation mode, but stops before the operation-relative note selection rule the source claims.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) -- useful burden decomposition, but it diagnoses retrieval versus derivation work rather than expected-yield membership in a joint-reading pass.
- [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) -- relevant to orientation materializations, but it lacks a specific claim about comparative-reading cohorts or operation-relative membership.
- [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) -- mentions comparative reading and index building as consumers of fixed pointers, but does not articulate why those operations require bounded related note sets.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- the discovery/commitment distinction is adjacent, but the review does not complete the sentence "this source note connects because..." without stretching from corpus triage into note-cohort theory.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) -- the note is a scoping-and-loading argument under bounded context: discovery surfaces propose candidate notes, but comparison needs its own bounded cohort.
- [Foundations](../../../../tags/foundations-README.md) -- the note turns finite attention plus expected yield into a general design-space claim about KB structure rather than a local maintenance tactic.

## Synthesis Opportunities

The source note, [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), and [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) together suggest a higher-order claim: discovery and joint-reading should use different selection policies. Orientation surfaces should stay high-recall and visibly partial so they do not suppress fallback search, while comparative passes should aggressively rank by expected yield because every extra note consumes bounded joint attention.

## Maintenance Observations

- The source note has `tags: []` even though the traversal strongly suggests at least `context-engineering` and possibly `foundations`; that weakens curated-head discovery and forces lexical/path search for this cluster.
- Several nearby notes reuse the orientation/comparison distinction with incomplete cross-linking, so the cluster is easiest to reach through [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md) and harder to reach from broader access/index notes.

## Flags

- None
