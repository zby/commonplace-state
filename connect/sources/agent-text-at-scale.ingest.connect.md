---
description: "Candidate comparisons for Shankar’s dashboard examples: how readers interpret an opening cue and what a missing comparison field means."
type: types/connect-report.md
source: kb/sources/agent-text-at-scale.ingest.md
source_has_frontmatter: true
date: "2026-11-19"
depth: standard
---

# Connection Report: Five Principles for Generating Readable AI Text in Bulk

**Source:** [Shankar ingest](../../../../sources/agent-text-at-scale.ingest.md)

## Discovery Trace

Read the README heads for theory, reference, agent-memory-systems, agentic-systems, tags and sources. For each destination, generated its title listing with `rg -N --no-filename -m1 '^# (.*)' -r '$1'` over Markdown excluding briefs. Filtered titles with `rg -i 'discriminat|structured output|comparison table|readab|near miss|scannab|titles|description[s ]|parallel wording'`. Filtered `rg '^description:'` listings with `rg -i 'side.by.side|scannab|discriminating description|visible prefix|adjacent items|at a glance'`; these surfaced the ingest itself, not a new target. Ran two body searches per destination: `rg -il 'side.by.side|session titles'` and `rg -il 'near misses|distinguishing words|scannable row'`. Searches were lexical, not scored.

- **Theory and tags:** The structured-output title recovered the ingest’s existing companion. The prose-readability head, found by title, led to the note on opening position and from there to Kieras’s experiments. Kept the experiment because it distinguishes two tasks that both seem to reward putting something first. No by-tag search: the ingest has no tags; the prose-readability head is complete for participating collections, which exclude sources.
- **Sources:** The sources landing explains capture, not topic groupings. The body search also hit ingests about metareasoning and technical comprehension; comparing items side by side is not itself a claim about wording. Link following from theory yielded the more specific Kieras comparison.
- **Reference:** Followed the reference head to Navigation and ADR 131. Navigation describes an agent deciding which hit to open; Shankar’s visible-prefix check tests neither destination choice nor agent behavior. ADR 131 allocates responsibility for checking descriptions, not for testing neighboring items together.
- **Agent-memory-systems:** Followed the historical head to the comparison table. Its fixed columns illustrate the already-linked review type; another historical link adds little.
- **Agentic-systems:** Followed the head through Comparisons to the current memory table. Its A-MEM row shows how to retain a comparison field without inventing a value. This is more useful than another review of a single system.
- **External:** The article is already cited where the missing figures matter; no external prospecting. No workshop or instruction targets considered.

### Candidate origins

- kb/sources/kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md — link-following
- kb/agentic-systems/comparisons/memory/memory-systems-table.md — link-following
- kb/theory/structured-output-is-easier-for-humans-to-review.md — known, titles, curated-head

## Connections Found

- [Kieras on initial mention](../../../../sources/kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md) — **compares-with**: What should the first words tell a human reader? Kieras moved the intended theme within a passage and measured which idea readers reported. Shankar wants the action that distinguishes one session title from its neighbors to be visible first. A cue that identifies the topic of every session may still fail to distinguish any pair. The passage experiment does not test list scanning.
- [Memory mechanisms in agentic systems](../../../../agentic-systems/comparisons/memory/memory-systems-table.md) — **compares-with**: Shankar removes a version number that invites a comparison the other cards cannot answer. The table shows the alternative when dropping the field would hide a real distinction: for A-MEM, the push selector for a requested lookup is *inapplicable*, whereas a possible provider-side selector is *uninspected*. Leaving both blank would make them look equivalent.

## Bidirectional Candidates

- [Structured output is easier for humans to review](../../../../theory/structured-output-is-easier-for-humans-to-review.md) → ingest — **see-also**: The ingest already points to the note. The return path would help a reviewer whose individual items pass: separating evidence from reasoning lets the reviewer check each claim, but only placing the cards together reveals the unsupported version comparison. Present this as a distinct review task, not corroboration of the note’s claim. A source-dependent account would need retained quotes or a citation marked `(snapshot required)`.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [ADR 131](../../../../reference/adr/131-conformance-reviews-leave-titles-and-descriptions-to-their-gates.md) — choosing which reviewer owns a check does not establish what that reviewer can detect from one item.
- [Opening position and theme](../../../../theory/position-and-proportion-set-what-a-reader-retains.md) — useful path to Kieras, but its separate conjecture about space devoted to support is unnecessary for the title-prefix comparison.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

The card rewrite changes field order, included detail and count display together. It illustrates a misleading implied comparison; it does not isolate which edit, if any, improves readers’ accuracy.
