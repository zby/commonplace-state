---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/notes/addressability-grain-sets-a-matched-selective-read-floor.md
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Addressability grain, not compression ratio, sets a matched selective-read floor

**Source:** [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md)

## Discovery Trace

**Authority and contracts:**

- Read `kb/instructions/cp-skill-connect/SKILL.md`, `kb/cache/types/connect-report.md`, the source artifact, and `kb/notes/COLLECTION.md` completely before prospecting.
- Read the curated heads used by standard-depth discovery: `kb/notes/README.md`, `kb/notes/document-system-README.md`, `kb/notes/context-engineering-README.md`, `kb/reference/README.md`, `kb/types/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- The source collection authorizes local prospecting into `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `kb/work/` is excluded. `external` is reserved for already-known targets and none was supplied, so external prospecting was skipped.
- The source carries tags `document-system` and `context-engineering`. Both tag READMEs were read. Neither declares `complete: true`, so no by-tag `rg` sweep was skipped on completeness grounds.

**Title and description listing scan:**

- Ran the full title surface for the principal destinations with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. The fresh scans covered 359 `notes`, 140 `reference`, 10 `types`, 47 `instructions`, 173 `agent-memory-systems`, 12 `agentic-systems`, and 289 `sources` titles.
- Ran description listings with `rg '^description:' kb/<destination>/ --glob '*.md'`. The scans covered 356 `notes`, 139 `reference`, 13 `types`, 171 `agent-memory-systems`, and a combined 398 lines across `agentic-systems`, `sources`, and `instructions`.
- The note-title surface and the two tag heads immediately confirmed that the source is already indexed in the two strongest local areas (`document-system` and `context-engineering`), so index-membership work focused on missing cross-links rather than missing landings.

**Body search and articulation checks:**

- `notes`: ran `rg -n 'addressability|summary|progressive disclosure|description|read-back|retriev|resolution|scoped rg|frontmatter|metadata' kb/notes/ --glob '*.md'`. This surfaced the existing linked cluster plus nearby unlinked candidates `type-system-enforces-metadata-that-navigation-depends-on.md`, `link-following-and-search-impose-different-metadata-requirements.md`, and `a-knowledge-base-should-support-fluid-resolution-switching.md`. The first two passed because they explain why description-level routing exists and how that routing behaves; the third was rejected as broader framing already covered more directly by the source's existing `two-context-boundaries` link.
- `notes`: ran `rg -n 'raw read volume|semantic reconstruction|transformation burden|access burden|read-volume|selective read|retrieval floor|sufficiency' kb/notes --glob '*.md'`. This surfaced `access-burden-and-transformation-burden-are-distinct-query-dimensions.md` as the strongest missing ledger-separation companion: the source explicitly brackets semantic reconstruction and other non-volume costs, and that note names the broader access/transformation split.
- `notes`: ran `rg -n 'an-insufficient-summary-precedes-the-source-rather-than-replacing|types-give-agents-structural-hints-before-opening-documents|pointer-design-tradeoffs-in-progressive-disclosure|rule-based-context-selection-needs-a-pre-existing-signal|opposed-recompute-factors-do-not-decide-documentation-segmentation|type-system-enforces-metadata-that-navigation-depends-on|link-following-and-search-impose-different-metadata-requirements|linked-note-durable-payload-is-what-consumption-path-cannot-supply|localized-retention-pays-where-change-is-sparse-in-a-matching|a-knowledge-base-should-support-fluid-resolution-switching' kb/notes --glob '*.md'` to check the current neighborhood and avoid re-proposing already-authored edges.
- `reference`: ran `rg '^description:' kb/reference/ --glob '*.md' | rg 'index|navigation|description|search|connect|review|type|summary|module|generated|read|scoped rg|context'`. This surfaced `navigation.md`, `lib-modules.md`, `adr/025-complete-generated-indexes-are-build-time-only.md`, `collections-and-types.md`, and `link-vocabulary.md`. Only `lib-modules.md` passed as a new outbound candidate because the source's negative Commonplace case measures that exact artifact. `adr/025` is already linked from the source, while `navigation.md` stayed better as a reverse-edge candidate than as a second outbound evidence edge.
- `reference`: ran `rg -n '025-complete-generated-indexes-are-build-time-only|navigation.md|lib-modules.md|adr/003-connect-skill-discovery-strategy|collections-and-types.md|link-vocabulary.md' kb/reference --glob '*.md'` and then read `kb/reference/navigation.md`, `kb/reference/adr/025-complete-generated-indexes-are-build-time-only.md`, and `kb/reference/lib-modules.md` fully. `navigation.md` and ADR 025 both already express the human-vs-agent access-path consequence; the source now supplies a sharper one-unit comparison they could point back to.
- `types`: read `kb/types/README.md` and checked the description surface. `kb/types/note.md` is part of the mechanism, but the stronger articulated explanation of enforced descriptions lives in the note [Type system enforces metadata that navigation depends on](../../../../notes/type-system-enforces-metadata-that-navigation-depends-on.md), so no source→type edge passed.
- `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`: ran `rg -n 'addressability|summary|progressive disclosure|description|retriev|resolution|frontmatter|metadata' kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'`. The matches were broad but not well-matched to the source's claim. The source is about a matched one-unit raw read-volume comparison over recoverable content; the retrieved artifacts mostly discussed progressive disclosure in general, read-back policy, or source-analysis workflows rather than this narrower addressed-unit floor. No candidate from these destinations passed the articulation test more strongly than the retained `notes` and `reference` candidates below.

**Link following:**

- Reverse-link scan with `rg -n 'addressability-grain-sets-a-matched-selective-read-floor|Addressability grain, not compression ratio, sets a matched selective-read floor' kb` found existing inbound links from [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md), [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md), and the two tag READMEs. These were recorded as existing edges, not repeated as new candidates.
- Followed the source's current note links through `an-insufficient-summary`, `opposed-recompute`, `rule-based-context-selection`, `two-context-boundaries`, `types-give-agents-structural-hints`, `pointer-design`, `frontloading-spares-execution-context`, and `llm-recompute-cost`. That confirmed the current graph already covers sufficiency, fan-out, pre-existing signals, pointer tiers, and the broader cache-value ledger; the new work is to expose the missing enabling and cross-register surfaces.

**Destination outcome:**

- `notes`: three new outbound candidates and two return-link candidates.
- `reference`: one new outbound evidence candidate and two reverse-edge candidates.
- `types`, `instructions`, `sources`, `agent-memory-systems`, and `agentic-systems`: no new candidates passed the articulation-and-authorisation test.

## Connections Found

- [Type system enforces metadata that navigation depends on](../../../../notes/type-system-enforces-metadata-that-navigation-depends-on.md) — **enables**: the source's helpful frontmatter-description case only lowers the read floor when descriptions reliably exist and remain validated; this note explains why that addressable routing layer exists at all.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **contrasts**: the source isolates one matched access-side floor and explicitly leaves semantic reconstruction, sufficiency, and other non-volume costs for a separate ledger; this note names that broader access-versus-transformation split.
- [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) — **extends**: the source explains one cost reason descriptions can beat opening a full note during candidate triage, while this note broadens that into the navigation-mode distinction between long-range search and local follow-on traversal.
- [Commonplace library (`commonplace.lib`)](../../../reference/lib-modules.md) — **evidenced-by**: the source's negative Commonplace example is an exact size comparison against the `type_resolver` section of `lib-modules.md`, so linking the inspected reference artifact makes that snapshot-bound case auditable.

## Bidirectional Candidates

- [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) <-> source — **extends**: that note compares pointer tiers by specificity, cost, and reliability; the source adds the matched addressed-unit comparison that explains when a higher layer actually lowers raw read volume.
- [Types give agents structural hints before opening documents](../../../../notes/types-give-agents-structural-hints-before-opening-documents.md) <-> source — **mechanism**: the existing target explains what description/type hints do for routing; the source would give it the explicit addressed-unit comparison that explains when those hints beat reading the body.

## Reverse-edge Candidates

- [Navigation](../../../../reference/navigation.md) → source — **rests-on**: the reference note says descriptions are the important middle layer and complete inventories are linear context debt for agents; this source supplies the more exact one-unit read-volume comparison behind that practical guidance.
- [025-Complete generated indexes are build-time only](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) → source — **rests-on**: ADR 025 already states the human-versus-agent access-mode asymmetry, and the source sharpens that operational decision into a matched addressed-unit floor rather than a whole-artifact compression intuition.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A knowledge base should support fluid resolution-switching](../../../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) — useful adjacent framing, but it is a broader abstraction-motion claim. The source already links [Two context boundaries govern collection operations](../../../../notes/two-context-boundaries-govern-collection-operations.md) for the relevant collection-scale contrast, so this would add breadth without a sharper reader need.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — it concerns what local rationale and recognition anchors must remain retained, not the source's narrower matched one-unit raw read-volume comparison.
- [Navigation](../../../../reference/navigation.md) — as a direct source→reference edge it was weaker than the retained `lib-modules.md` evidence edge and redundant with the source's existing ADR 025 link. It is more useful as a reverse-edge candidate.
- [Note](../../../../types/note.md) — the type contract requires descriptions, but it does not itself explain the navigation consequence. The explanatory note on type-system enforcement is the stronger target.

## Index Membership

None

## Synthesis Opportunities

- [Type system enforces metadata that navigation depends on](../../../../notes/type-system-enforces-metadata-that-navigation-depends-on.md), [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), and the source together suggest a missing synthesis note: agent navigation needs three separate conditions to pay off cleanly — the metadata must exist reliably, each navigation mode needs the right pointer shape, and the pointer's addressed unit must actually beat the body read it replaces. No current note states those three conditions as one routing rule.

## Maintenance Observations

- The source's negative Commonplace example cites exact 2026-08-23 byte counts for `lib-modules.md` versus code search, but the source currently links only ADR 025 and not the inspected reference artifact. The retained `lib-modules.md` candidate would at least surface the mutable artifact being measured; no immutable measurement packet was found during traversal.
- All paths named in this report were checked with `test -f`. No source artifact, index, library artifact, or log was edited.

## Flags

None
