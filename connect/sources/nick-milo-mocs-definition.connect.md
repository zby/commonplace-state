---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/nick-milo-mocs-definition.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: MOCs (defn)

**Source:** [MOCs (defn)](../../../../sources/.snapshots/nick-milo-mocs-definition.md)

## Discovery Trace

**Curated heads:**

- Read [top-level note navigation](../../../../tags/README.md), [document system](../../../../tags/document-system-README.md), [KB maintenance](../../../../tags/kb-maintenance-README.md), [links](../../../../tags/links-README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), and [agentic systems](../../../../agentic-systems/README.md). The document-system and KB-maintenance heads exposed the tag-README, completeness, and editorial-orientation cluster. The other collection heads supplied no closer target.

**Full title listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`, then filtered the combined surface for MOC, map, index, orientation, curation, navigation, grouping, and context terms. The strongest candidates were [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) and [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md). Broader navigation and context titles did not gain a source-dependent premise from this short definition.

**Description listing scan:**

- `rg -n "^(title|description):.*(MOC|map|index|orient|curat|navigation|Zettel|complet|group|cluster|context)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!**/dir-index.md' --glob '!**/*-README.md'` reinforced the same two note candidates and surfaced the new [Luhmann Archive ingest](../../../../sources/luhmann-archive-schlagwortregister.ingest.md) as a useful bounded comparison.

**Body search:**

- `rg -n "Nick Milo|Map of Content|Maps of Content|\\bMOC\\b|boring index|cartograph|map-maker" kb/notes kb/reference kb/instructions kb/sources --glob '*.md'` found one live note that attributes the MOC pattern to Milo and no existing ingest for this page. It also exposed unsupported claims in that note about selectivity, completeness promises, human behavior, and maintenance economics; none follows from the source.

**Link following:**

- Followed [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) to [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md), [indexes lower recall](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), and [a derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). Milo's page directly supports the MOC definition as contextual mapping, navigation, and grouped links. It does not support the tag-README identity as an exact equivalence, the completeness-contract history, or the agent-versus-human mechanism.
- Compared the source with the [Luhmann Archive keyword-register ingest](../../../../sources/luhmann-archive-schlagwortregister.ingest.md). The two sources establish distinct bounded facts: Milo describes MOCs as contextual maps with clustered links, while the Archive describes Luhmann's keyword registers as non-exhaustive entry-point indexes. Neither source identifies Luhmann's registers as MOCs or licenses merging the traditions.

## Connections Found

- [an enforced tag-README is a MOC with a machine-checked contract](../../../notes/an-enforced-tag-readme-combines-a-moc-pattern-with-checked-membership.md) -- **is-evidence-for**: Milo defines an MOC as a cluster that maps things in context, says it helps gather, develop, and navigate ideas, and gives a grouped-link note as an example. This supports the note's narrow description of the Milo/LYT artifact, not its claims that MOCs are selective by design, that no practitioner promised completeness, or that a Commonplace tag-README is exactly the same artifact.
- [index completeness does not determine editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -- **compares-with**: Milo distinguishes a contextual, customizable map from an index-like list and describes grouped links as one MOC form. This is a practitioner comparison for the note's orientation-versus-enumeration distinction; the source does not establish Commonplace's generated-membership mechanism or the adequacy of any particular editorial map.
- [Luhmann Archive keyword registers](../../../../sources/luhmann-archive-schlagwortregister.ingest.md) -- **compares-with**: the sources describe different navigation artifacts and should remain separate. Milo supplies the MOC terminology and contextual-grouping description; the Archive supplies the Luhmann-specific non-exhaustive-entry-point claim.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [indexes lower recall when they suppress retrieval that would find more](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) -- rejected as unsupported: Milo's page does not test stopping behavior, fallback retrieval, or recall, and its “boring index” contrast is not evidence for that mechanism.
- [a knowledge base should support fluid resolution switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) -- rejected as too broad: a short MOC definition does not establish the target's multi-level KB design criterion.
- [areas exist because useful operations require reading notes together](../../../../notes/areas-exist-because-useful-operations-require-reading-notes-together.md) -- rejected as an analogy: grouped links are compatible with bounded orientation, but the source does not examine Commonplace areas, comparative reading, or collection boundaries.
- [soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- rejected because the page describes an LYT term and does not substantiate that survey's Zettelkasten mechanisms or transfer conditions.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The live MOC note describes Milo's MOC as a “curated, annotated” link set and treats MOCs as “selective by design.” This page supports contextual mapping, customization, navigation, and clustered links, but it does not use “annotated,” assert deliberate incompleteness, or discuss completeness promises.
- Read together, this source and the Luhmann Archive page support two separate source-bounded sentences. They do not support the live note's combined universal claim about Zettelkasten and LYT practitioners.

## Flags

- Treat the page's claims about extending cognition, deeper learning, and unexpected insight as practitioner advocacy, not evaluated effects.
