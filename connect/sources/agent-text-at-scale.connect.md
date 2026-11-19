---
description: "Candidate connections for Shankar’s checklist: distinguish what helps humans compare generated items from what helps them check a claim or choose a link."
type: types/connect-report.md
source: kb/sources/.snapshots/agent-text-at-scale.md
source_has_frontmatter: true
date: "2026-11-19"
depth: standard
---

# Connection Report: Five Principles for Generating Readable AI Text in Bulk

**Source:** `kb/sources/.snapshots/agent-text-at-scale.md`, a local capture of [Shreya Shankar’s article](https://fsdatalab.github.io/blog/agent-text-at-scale/). The examples concern a human comparing several generated items, not an agent reading one document. The article describes the original and rewritten items; the capture omits the figures. It reports no timed comparison of the rewrites.

## Discovery Trace

Standard repo-local pass with `cp-skill-connect` (gpt-6.2-astra). Read the README of each of theory, reference, sources, tags, agent-memory-systems and agentic-systems. The capture has no tags, so no by-tag search applied. Generated each collection’s titles with `rg -N --no-filename -m1 '^# (.*)' -r '$1'` over Markdown excluding briefs. Filtered titles with `readab|readers|vocabulary|scann|titles|descriptions|comparison table|prose|sentence|naming|terminology|parallel structure`. Filtered each `rg '^description:'` listing with `scan(nable|ning)|one term|one name|first words|discriminating (title|description)|controlled vocabulary|side.by.side|parallel structure` (case insensitive). Body searches included `readability|parallel phrasing|controlled vocabulary|skim(ming)?|one word per concept` and `fsdatalab.github.io/blog/agent-text-at-scale|first two words|side.by.side|lead tokens`. These searches produce matches, not scores.

- **Theory and tags:** The description search surfaced scanning titles to reconsider hypotheses: a different reader decision. The body search found the structured-output note and the opening-position note (including its brief). Followed the [prose-readability head](../../../../tags/prose-readability-README.md) to both. The former compares two ways to organize checks; the latter explicitly separates theme identification inside a passage from scanning a title before opening it. No by-tag expansion of this complete head.
- **Reference:** ADR 116 appeared in titles and body results. Checked its decision against principle 3: stable terms are shared, but identifier spelling and enforcement are KB choices, not findings from the article.
- **Sources:** The landing describes custody, not topics. Body search surfaced Pirolli; its analysis of selection from a visible cue complements the sidebar example. An exact URL search among `*.ingest.md` found no matching ingest.
- **Agent-memory-systems:** Followed the historical survey landing to its review type. `rg -n 'lead token|lead with'` distinguished a deliberate omission for an inapplicable field from an incomplete review. That distinction addresses the article’s most consequential example of inconsistent detail.
- **Agentic-systems:** Checked the memory comparison table surfaced by the body search and the landing’s account of its evidence boundary. Rows show the result of classification, but not an evaluation of how readers scan them. The historical type makes the comparison rule clearer; no second table link.
- **External and inverse directions:** Considered only the article URL already in the capture. The original is useful for its missing figures; no open-web search. Checked theory’s source-link rules against the two readability notes: neither claim originated here, and the dashboard rewrites did not test either claim. No reverse citation to the ignored capture. Excluded work and instructions from prospecting.

### Candidate origins

- kb/theory/structured-output-is-easier-for-humans-to-review.md — body-search, curated-head, link-following
- kb/agent-memory-systems/types/agent-memory-system-review.md — curated-head, body-search, link-following
- kb/sources/pirolli-proximal-information-scent-distal-content.ingest.md — body-search
- kb/reference/adr/116-one-word-per-concept-across-prose-and-code.md — known, titles, body-search
- https://fsdatalab.github.io/blog/agent-text-at-scale/ — known

## Connections Found

Candidates for a future ingest, not edits to the capture:

- [Structured output is easier for humans to review](../../../../theory/structured-output-is-easier-for-humans-to-review.md) — **compares-with**: Both designs give a reader one question per part. A repeated theme card lets the reader compare what users said separately from the example offered; Evidence and Reasoning sections let a reviewer check facts separately from the inference. The former is a check across items, the latter within one argument.
- [Historical memory review type](../../../../agent-memory-systems/types/agent-memory-system-review.md) — **compares-with**: A version number on just one bug card leaves the reader guessing whether other versions were checked. The review contract shows an alternative to dropping that detail: state the value is undetermined when an axis applies but evidence is missing, and omit the field only under a declared condition. Its immediate purpose was reliable matrix extraction, not faster human reading.
- [Pirolli on choosing an unseen target from a visible cue](../../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md) — **compares-with**: For a session sidebar, ask two different questions: can the reader see a difference in the first words, and does that difference predict which session is worth reopening? Shankar addresses cue placement; Pirolli addresses cue validity and selection, not word order.
- [ADR 116: One word per concept across prose and code](../../../../reference/adr/116-one-word-per-concept-across-prose-and-code.md) — **see-also**: The Notion rows alternate between issue and page for the same object. The ADR shows where to intervene when that variation comes from upstream names rather than sentence generation: use the same term in data, prompts and displayed text.
- [Shankar’s original article](https://fsdatalab.github.io/blog/agent-text-at-scale/) — **derived-from**: Inspect the original figures to compare the items side by side; the local capture preserves the author’s descriptions, not the layouts.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Opening position can signal a human reader’s theme](../../../../theory/position-and-proportion-set-what-a-reader-retains.md) — identifying a passage’s theme is not distinguishing adjacent items by their first words. The card examples do not establish a recall or proportion effect.

## Index Membership

None. Sources are outside participating tag collections; do not add the snapshot to the prose-readability head.

## Synthesis Opportunities

None

## Maintenance Observations

No name-paired ingest was present during discovery. Until one exists, retain the suggestions here rather than pointing library artifacts at the local capture.

## Flags

The article extrapolates from human-facing lists to generated artifacts generally. Neither its feed examples nor the cited sentence-processing studies establish that a model reading a single KB note benefits from the same edits.
