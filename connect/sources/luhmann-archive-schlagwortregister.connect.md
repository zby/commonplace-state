---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/luhmann-archive-schlagwortregister.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Schlagwortregister

**Source:** [Schlagwortregister](../../../../sources/.snapshots/luhmann-archive-schlagwortregister.md)

## Discovery Trace

**Curated heads:**

- Read [top-level note navigation](../../../../tags/README.md), [KB maintenance](../../../../tags/kb-maintenance-README.md), [document system](../../../../tags/document-system-README.md), [links](../../../../tags/links-README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), and [agentic systems](../../../../agentic-systems/README.md). The KB-maintenance and document-system neighborhoods exposed the completeness/curation cluster; the system heads supplied no credible target.

**Full title listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`. The note surface flagged [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md), [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md), [indexes lower recall when they suppress retrieval that would find more](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), and [soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md). No reference, external-system, or existing-source title was a closer target.

**Description listing scan:**

- `rg -n "^(title|description):.*(index|complet|entry|hub|MOC|map|Zettel|Luhmann|orientation|curat)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' --glob '!**/dir-index.md' --glob '!**/*-README.md'` reinforced the same four candidates. Generic index and completeness descriptions were rejected unless the page's explicit non-exhaustive-entry-point statement changed how a reader could assess the target.

**Body search:**

- `rg -n "Luhmann|Zettelkasten|MOC|Map of Content|completeness|exhaustive|entry point|entry-point|keyword register" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!kb/sources/.snapshots/**'` found named-but-unrouted Luhmann claims in the MOC note and the soft-bound-traditions survey, plus the index-completeness cluster. It found no existing ingest for this Archive page.

**Link following:**

- Followed [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) to [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md), [indexes lower recall](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), and [a derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). The page directly supports only the Luhmann register's non-exhaustiveness and entry-point function. It does not support the note's MOC identity, claims about all practitioners, human need, maintenance cost, or agent behavior.
- Followed [soft-bound traditions](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) into its Zettelkasten transfer claims. The Archive page says nothing about atomicity, attention bounds, or judgment-based linking, so that match was rejected despite the shared name.

## Connections Found

- [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) -- **is-evidence-for**: the Archive states that Luhmann's own keyword registers explicitly made no claim to complete term locations and named only relevant entry points into the collection. This directly supports the narrow Luhmann-side non-exhaustive-entry-point claim, not the note's broader MOC identification or its claims about all Zettelkasten and LYT practitioners.
- [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -- **compares-with**: Luhmann's register is an authoritative historical example of an index that deliberately exposes entry points without asserting complete membership. The target separately explains Commonplace's distinction between generated membership and editorial grouping; the source does not establish that mechanism.
- [indexes lower recall when they suppress retrieval that would find more](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) -- **compares-with**: the Archive describes a partial register whose non-exhaustiveness is explicit, matching the note's defense of making partiality visible. It does not measure whether readers continue searching or what recall results.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- rejected as name-only overlap: this page does not support atomic notes, attention bounds, or judgment-based linking.
- [a derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) -- rejected as a category mismatch: Luhmann's register disclaims completeness instead of retaining and enforcing a recomputable completeness claim.
- Generic index and entry-point hits in reference and external system reviews -- rejected because they do not gain a useful comparison from this specific archival statement.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The live MOC note's phrase “no Zettelkasten or LYT practitioner” remains a universal negative. This source supports only Luhmann's registers and cannot carry that wider claim.

## Flags

- The snapshot is a user-supplied rendered-page transcription because the prescribed automated capture returned only the site's JavaScript placeholder. Scope quote-level use to the exact retained text.
