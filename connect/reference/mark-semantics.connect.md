---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/reference/mark-semantics.md"
source_has_frontmatter: true
date: "2026-06-10"
depth: standard
---

# Connection Report: Mark semantics

**Source:** [Mark semantics](../../../reference/mark-semantics.md)

## Discovery Trace

**Source already-authored edges (excluded from candidates):**
- Inline: [ADR 026](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md), [navigation.md](../../../../reference/navigation.md), [stale-indexes](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), type spec `kb/types/tag-readme.md`.
- Footer: stale-indexes (rationale), ADR 026 (part-of), [maintain-curated-indexes](../../../../instructions/maintain-curated-indexes.md) (procedure).

**COLLECTION.md outbound rules (reference):** destinations = reference, notes, notes/definitions, sources, agent-memory, instructions. Do NOT link into `kb/work/`. `rationale` -> notes is the primary theory-ward edge; sources/agent-memory edges are uncommon. Labels: part-of/contains, implements, supersedes, rationale, defined-in, derived-from, evidence, procedure, see-also.

**Description listing scan:**
- `rg '^description:' kb/reference/ --glob '*.md'` -- flagged: navigation.md (already linked), adr/025 (recovery path / scoped rg), adr/026 (already linked), adr/003 (connect discovery, superseded), adr/004 (curated+generated split). adr/025 kept as candidate; others already linked or superseded.
- `rg '^description:' kb/instructions/` -- maintain-curated-indexes already linked (procedure). No new instruction candidate (declaring/fixing/dropping marks all live there).
- `rg '^description:' kb/notes/definitions/` -- scanned lineage.md, retained-artifact.md, operative-part.md; none names the cache/accelerator-over-recoverable-query property. No defined-in candidate (mark, accelerator, complete, covered_by are all glossed inline in the source).

**Topic indexes:**
- `kb/reference/README.md` -- mark-semantics not yet listed under Type system / Decision history sections; surfaced as an Index Membership item, not an edge.
- `kb/notes/kb-maintenance-README.md`, `kb/notes/document-system-README.md` -- source carries no `tags:`, so no tag-README is authoritative; read kb-maintenance for routing signal toward index/staleness notes.

**Body search:**
- `rg -n "complete: true|covered_by|tag-readme|weight gate|stale.index|accelerator|cache" kb/notes/ kb/reference/ kb/instructions/ -l` -- hits: stale-indexes (linked), index-curation, navigation (linked), ADR 025/026 (linked), context-engineering-README, kb-maintenance-README.
- `rg -li "cache|derived|stale|invalidat|regenerat|recover" kb/notes/` -- surfaced keep-compiled-views-aligned, link-graph-plus-timestamps, index-curation. Evaluated each below.

**Link following:**
- From index-curation -> stale-indexes (shared with source) and 004-replace-areas-with-tags. Confirms index-curation sits in the same staleness cluster but argues a different axis (orientation vs membership-completeness).
- From keep-compiled-views-aligned -> always-loaded-context-mechanisms, designing-agent-memory-systems. The "rebuildable index should not become a policy / detect stale compiled views" framing generalizes the mark = cache-over-query rule exactly.

## Connections Found

- [keep-compiled-views-aligned](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) -- **rationale**: the mark is a compiled view over the membership query; this note states the general requirement (a rebuildable index must not become an independent source of truth; the system must detect stale compiled views after source changes), which is the theory the source's "a cache must never be the only copy" rule instantiates.
- [025-complete-generated-indexes-are-build-time-only](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) -- **part-of**: ADR 025 establishes the scoped-`rg` membership recovery path that the source names as ground truth. The source's design sequence ("guarantee the query path, then add the mark as an optimization on top") rests on the recovery path ADR 025 decided; situating mark-semantics against that decision shows where the recoverable-query precondition came from.

## Bidirectional Candidates

- [navigation.md](../../../../reference/navigation.md) <-> source -- the return edge already exists: navigation.md line 30 links to mark-semantics for "full semantics," and the source links to navigation.md for the membership sweep. Backlink is computed; no authoring needed. Recorded so a future writer does not double-author it.

## Reverse-edge Candidates

- [maintain-curated-indexes](../../../../instructions/maintain-curated-indexes.md) -> source -- under the instructions COLLECTION.md rules, the procedure for declaring/fixing/dropping marks could carry a reference link to mark-semantics for the why-behind-the-rule. The source already links *to* the instruction (procedure); whether the instruction should link back is the instruction author's call.
- [index-curation-adds-orientation-that-generation-cannot-produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -> source -- this note's "stale curation is costly, but the alternative is worse" / fallback-to-generated argument is the same trusted-stale trap the marks defend against. Under notes COLLECTION.md it could reference mark-semantics as the shipped enforcement of the completeness guarantee it discusses. Notes-side authoring decision.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [link-graph-plus-timestamps-enables-make-like-staleness-detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- adjacent on "detect staleness" but the mechanism differs: marks are enforced reactively by the validator's membership check, not by timestamp comparison. Keyword overlap only; following the link would mislead about how mark enforcement works.
- [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) -- already authored inline and in the footer (rationale). Re-surfacing would duplicate.
- [adr/003-connect-skill-discovery-strategy](../../../../reference/adr/003-connect-skill-discovery-strategy.md) -- the index-first discovery it proposed is superseded by ADR 025; linking from mark-semantics would point at retired design.
- [adr/004-replace-areas-with-tags](../../../../reference/adr/004-replace-areas-with-tags.md) -- introduces the curated/generated split but predates the mark mechanism; the relevant lineage is ADR 026 (already linked), not 004.

## Index Membership

- [kb/reference/README.md](../../../../reference/README.md) -- mark-semantics is not yet listed. A future writer could add it under "Type system and collection model" (alongside link-vocabulary / available-types) or beside the ADR 026 entry under "Decision history," since it carries the per-consumer mark contract that ADR 026 decided. Connect does not edit the index.

## Synthesis Opportunities

None. The cache-over-recoverable-query rule is already the source's own higher-order claim; keep-compiled-views-aligned generalizes it but no third note is needed to bridge them.

## Maintenance Observations

- The "a cache must never be the only copy" general form appears in three places now (mark-semantics, keep-compiled-views-aligned, and implicitly in storage-architecture's derived-indexes framing) without a single named home. Not a connection candidate; flag for a maintainer deciding whether this principle deserves its own note or a definition.

## Flags

- None. Source makes a single coherent assertion (marks are accelerators over a recoverable query); not a split candidate.
