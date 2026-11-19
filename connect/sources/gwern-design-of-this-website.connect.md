---
description: "Connection discovery for Gwern’s website design, with tag navigation and maintenance as the ingest occasion."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/gwern-design-of-this-website.md
source_has_frontmatter: true
date: "2026-09-22"
depth: standard
---

# Connection Report: Design Of This Website

Source: Gwern’s captured website-design article. The paired ingest is the authored connection surface.

## Discovery Trace

- Read the source snapshot, sources collection contract, report type, and the README entry points for notes, reference, sources, agent-memory-systems, and agentic-systems. Read the notes tag hub and links head. The snapshot has no tags, so no tag-specific completeness shortcut applied.
- Generated the H1 listing using `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`; the broad output exceeded the display budget, so filtered it with `rg -i 'tag|index|curat|navigation|resolution|backlink|gwern|moc'`.
- Filtered the five collections’ `^description:` listings with `rg -i 'tag|curat|navigation|progressive disclosure|transclu|backlink|MOC|gwern'`. This identified the semantic-contract and tag-scope proposals, navigation reference, resolution-switching note, checked-MOC note, and Milo ingest.
- Read the semantic-contract proposal’s predicate, head, coverage, and free-choice sections; inspected the tag-scope proposal’s ownership and migration concerns. Read the backlink proposal. These are candidate designs, not descriptions of shipped Commonplace.
- Followed navigation’s authored links to the tag-readme contract and the access-cost note; followed the checked-MOC note to the editorial-orientation note. Kept the resolution-switching and MOC comparisons; did not interpret generated membership as editorial quality.
- Searched `rg -n 'tag|Tags|gwern|transclu'` in the Napkin review, Semantic Engine review, and Milo ingest. Napkin supplies an agent-facing comparison but is less direct than Commonplace’s own navigation contract. Semantic Engine concerns ingest staging rather than a maintained tag design. Neither warrants a retained system edge here. Other system-title hits concerned execution stages, not tags.
- Read notes and reference outbound contracts for inbound candidates. Existing external targets are the source and its implementation links; external prospecting was skipped.

## Connections Found

- [Resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) — **is-evidence-for**: nested tag previews, annotations, and full pages provide a practitioner example of moving among scopes and levels of detail; they do not establish agent performance.
- [Checked tag heads and MOCs](../../../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — **compares-with**: both combine topic orientation with links; Gwern’s generated annotation lists do not supply Commonplace’s checked completeness and coverage marks.
- [Editorial orientation](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) — **compares-with**: generated tag lists and the proposed clustering interface separate membership from choices about organization and reading order.
- [Navigation](../../../../reference/navigation.md) — **see-also**: the current human-build and agent-query split bounds transfer of browser-oriented tag pages.
- [Semantic contract for tags and tag heads](../../../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md) — **see-also**: Gwern’s taggable tag pages and filesystem hierarchy are useful alternatives to the proposed separation between members and tag heads.
- [Tag scope](../../../../reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md) — **see-also**: tagging arbitrary annotated URLs raises scope and identity questions already being considered for Commonplace.
- [Backlink surfacing](../../../../reference/proposals/backlink-surfacing.md) — **see-also**: Gwern supplies a concrete contextual-backlink implementation to compare with the proposed generated inbound views.

## Bidirectional Candidates

None. Outbound comparison alone does not justify a reciprocal link.

## Reverse-edge Candidates

- [Semantic contract proposal](../../../../reference/proposals/semantic-contract-for-tags-and-tag-heads.md) → paired ingest — **evidenced-by**: qualify the option space with an external implementation where tag pages can themselves carry tags, while cross-references do not imply recursive membership. A future author must name the compared choice and use `(snapshot required)` unless quotes are retained.
- [Backlink surfacing proposal](../../../../reference/proposals/backlink-surfacing.md) → paired ingest — **evidenced-by**: contextual source-link previews provide an implementation example for deciding whether inbound lists should expose context. The source does not establish Commonplace’s benefit.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Napkin](../../../../agent-memory-systems/reviews/napkin.md): useful access-interface comparison, but adds a second system without improving the immediate tag-design question beyond the navigation reference.
- [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md): embeddings and ingest staging do not establish tag maintenance or taxonomy semantics.
- [Milo MOC definition](../../../../sources/nick-milo-mocs-definition.ingest.md): the checked-MOC note already provides the precise comparison; a further source edge would duplicate it.

## Index Membership

None. The source collection is searchable by its tracked ingest; theory tag heads should not acquire a broad website-design entry by default.

## Synthesis Opportunities

None established. The existing resolution-switching and editorial-orientation notes already state the closest transferable claims.

## Maintenance Observations

The sources README still describes a WebFetch fallback, while the invoked snapshot skill prescribes Trafilatura. This did not block capture.

## Flags

- The article is broader than the tag-system occasion. Keep its independent design claims visible in the ingest without creating several new notes solely from this discovery pass.
- The capture is partial: interactive demonstrations are absent and extractor fragment links can point to the site root. Use the article’s section names and canonical source URL as locators.
- Distinguish existing semantic sorting of similar links from the broader proposed tag-maintenance interface. The future-work heading contains some reported experiments, not an entirely unimplemented block.
