---
description: "Post-ingest connection discovery for Gwern’s tag design and its remaining inbound-link opportunities."
type: kb/reports/types/connect-report.md
source: kb/sources/gwern-design-of-this-website.ingest.md
source_has_frontmatter: true
date: "2026-09-22"
depth: standard
---

# Connection Report: Gwern’s website-design ingest

**Source:** [Accepted ingest](../../../../sources/gwern-design-of-this-website.ingest.md)

## Discovery Trace

- Read the accepted ingest in full and checked it against the source collection’s outbound contract and the connect-report type.
- The same-session discovery read README entry points for notes, reference, sources, agent-memory-systems, and agentic-systems, plus the notes tag hub and links head. The ingest uses domains rather than tags; no by-tag completeness shortcut applies.
- Generated the five collections’ H1 listing with `rg -N --no-heading -m1 '^# ' ... --glob '*.md'`; inspected a focused `rg -i 'tag|index|curat|navigation|resolution|backlink|gwern|moc'` view after the broad listing exceeded the display budget. Inspected `^description:` listings filtered by `tag|curat|navigation|progressive disclosure|transclu|backlink|MOC|gwern`.
- After acceptance, repeated the description scan with `tag maintenance|tag contract|tag pages|membership predicate|backlink surfacing|resolution-switching|negative.*tag`. Read the newly authored tag-maintenance proposal and the new comparison section in the semantic-contract proposal. Both now cite the ingest; neither is an outstanding inbound-link candidate.
- Followed navigation to the tag-readme contract and access-cost note, and the checked-MOC note to editorial orientation. The ingest already carries its strongest edges to navigation, checked MOCs, editorial orientation, resolution-switching, and the semantic-contract proposal; those are existing authored links, not new recommendations below.
- Read the backlink-surfacing proposal and inspected the tag-scope proposal’s ownership and migration concerns. Kept two optional outgoing candidates because they answer different next questions: URL membership scope and contextual inbound views.
- Searched `rg -n 'tag|Tags|gwern|transclu'` across the Napkin and Semantic Engine reviews and the Milo ingest. Rejected a further systems comparison because it adds less than the current navigation contract. Sources’ description and title scans yielded Milo as the closest comparison, already mediated by the checked-MOC note.
- Consulted notes and reference outbound contracts for inbound directions. Existing source URLs and code links were available context; no external prospecting was performed for connection discovery.

## Connections Found

- [Tag-scope proposal](../../../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md) — **see-also**: useful if pursuing Gwern’s URL-wide membership model, because the Commonplace proposal owns which artifacts participate and how projections constrain membership.
- [Backlink-surfacing proposal](../../../../reference/proposals/backlink-surfacing.md) — **see-also**: the ingest’s occurrence-addressed backlink mechanism offers a concrete implementation comparison for the proposal’s inbound views.

## Bidirectional Candidates

None. Existing outgoing links do not independently justify return links.

## Reverse-edge Candidates

- [Backlink-surfacing proposal](../../../../reference/proposals/backlink-surfacing.md) → ingest — **evidenced-by**: a bounded comparison could use Gwern’s source-occurrence IDs and contextual previews to distinguish a list of referring pages from an inspectable explanation of each reference. The benefit for Commonplace remains untested. A future author must use `(snapshot required)` unless supporting quotes are retained.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Napkin](../../../../agent-memory-systems/reviews/napkin.md): its agent-shaped CLI is relevant generally, but the current navigation reference supplies the needed consumer distinction more directly.
- [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md): ingest staging and embeddings do not establish a maintained tag-navigation mechanism.
- [Milo MOC definition](../../../../sources/nick-milo-mocs-definition.ingest.md): an additional direct comparison would duplicate the ingest’s checked-MOC route.

## Index Membership

None. Keep this broad source discoverable through its description and the design proposals that use it.

## Synthesis Opportunities

None established beyond the existing resolution-switching and editorial-orientation claims.

## Maintenance Observations

The sources README’s WebFetch description differs from the invoked Trafilatura capture workflow. The snapshot also exposes link-parser warnings on angle-bracketed Wikipedia URLs containing parentheses; its immutable bytes were retained.

## Flags

- The ingest characterizes the captured article, not a code audit. The new browsing proposal separately cites the inspected code at a pinned revision, including tag-page semantic grouping already implemented beyond what the future-work heading alone suggests.
- No connection recommendations in this report were automatically authored. The two proposal citations were authored as part of the separately requested design consideration before this pass.
