---
description: "Post-ingest connection discovery for the accepted RE 2008 core-ontology analysis, separating conceptual approximation comparisons from outcome evidence."
type: types/connect-report.md
source: "kb/sources/revisiting-core-ontology-requirements-engineering-2008.ingest.md"
source_has_frontmatter: true
date: "2026-11-16"
depth: standard
---

# Connection Report: Accepted core-ontology ingest

**Source:** [Revisiting the Core Ontology and Problem in Requirements Engineering](../../../../sources/revisiting-core-ontology-requirements-engineering-2008.ingest.md)

## Discovery Trace

This is a separate post-publication pass. Read the accepted ingest fully and applied the sources collection's outbound rules. It is an authored analysis of one theoretical conference paper, not an implementation study or empirical learning result. No external search, source edit or authored library link.

- Reused the same-run curated-head reads and fresh complete title surfaces for theory, reference, agent-memory-systems, agentic-systems, tags and sources from snapshot discovery. Commands were `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`. Heads read: each destination's README and `kb/tags/goal-prioritization-README.md`. No source tags are present, so no by-tag listing or completeness skip applies.
- Theory description scan was `rg '^description:' kb/theory/ --glob '*.md' | rg -i 'proxy|requirement|objective|belief|revision'`; other substantive destinations used description listings filtered by `requirement|stakeholder|softgoal|goal authority|belief revision|ontology`. These surfaces yielded exact implementation, objective revision, proximate target and generic ontology systems. Read the first three fully; reject generic ontology system comparisons because the retained paper has no matching runtime mechanism to compare.
- Post-publication query: `rg -l -i 'justified.approximation|softgoal|defeasible consequence|preference aggregation' kb/theory kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/tags --glob '*.md'` returned the new ingest and Awareness Requirements. The latter is an adjacent monitoring application, not a necessary new outbound edge. Existing source-family titles had also exposed Four Dark Corners and AGM; both were read fully during the prepass and remain useful optional comparisons.
- Tested inbound articulation using `rg -n -i 'softgoal|approximation|preference|defeasib'` on exact implementation, proximate target, objective revision, Four Dark Corners and AGM. Objective revision contains an explicit preference-versus-epistemic-standard distinction, but the paper does not independently test that claim. Do not recommend an evidence edge there just because the ingest links it.
- Newly followed the accepted ingest's links to `kb/theory/definitions/theory-builder.md` and `kb/theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`; read both fully. The first is needed to interpret the partial learning mapping, not a promising reciprocal source example. The second provides a concrete comparison axis: revising plans under one quality constraint differs from revising the constraint-to-softgoal relation.
- Theory reverse pass uses its fully read `COLLECTION.md`: `evidenced-by` can qualify or bound a claim, but this conceptual source is not a survived attempted refutation of either target. For each kept inbound candidate, the reader need is the independently useful local-approximation model, not reciprocal navigation. Prospective source use must obtain suitable Quotes or declare `(snapshot required)`; the current empty Quotes block is not changed by discovery.
- Reference head and descriptions yielded no distinct source-specific companion beyond the installed epistemic frame; no reference candidate retained. System heads, titles, filtered descriptions and focused query yielded no mechanistically grounded comparison. Tags are routing surfaces with no source-to-tag label; no membership proposed. Other sources were scoped through titles, descriptions, focused queries and one-hop source comparisons. No open-web prospecting under `external`; the canonical arXiv source was already in hand. Work and instructions remain excluded destinations.

### Candidate origins

- kb/theory/exact-implementation-does-not-validate-a-requirement.md — known, titles, descriptions, curated-head, link-following
- kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md — known, titles, descriptions, curated-head, link-following
- kb/theory/definitions/theory-builder.md — known, link-following
- kb/theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md — known, link-following
- kb/sources/four-dark-corners-requirements-engineering.ingest.md — titles, descriptions
- kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — titles
- kb/theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md — titles, descriptions, curated-head, link-following

## Connections Found

- [Exact implementation](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) — **compares-with**: retain the existing comparison between satisfying a measurable constraint and separately warranting its project-local approximation of a softgoal. The paper is conceptual support for distinguishing obligations, not outcome evidence.
- [Objective revision](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: retain the existing distinction between representing preferences and establishing authority to change ends. Stakeholder inputs and aggregation remain presupposed rather than legitimated by the paper.
- [Theory builder](../../../../theory/definitions/theory-builder.md) — **defined-in**: retain the existing definition link so readers can check why localized content and anticipated revision are not enough to demonstrate a working criticism-and-iteration process.
- [Learning inside a fixed decomposition](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: retain the existing comparison between improving plans under a fixed constraint and revising the approximation mapping itself; the paper permits the latter conceptually but demonstrates no learning process.
- [Four Dark Corners](../../../../sources/four-dark-corners-requirements-engineering.ingest.md) — **compares-with**, optional additional edge: the earlier environmental satisfaction obligation helps readers inspect the baseline against which this paper argues. Check its informal-validation obligations before accepting the later critique of monotonic consequence.
- [AGM](../../../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md) — **compares-with**, optional additional edge: closed-theory revision under a fixed consequence operation differs from defeasible inference and a locally revisable approximation. Neither by itself supplies empirical warrant or discovery.

## Bidirectional Candidates

- [Exact implementation](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) → [this ingest](../../../../sources/revisiting-core-ontology-requirements-engineering-2008.ingest.md) — **evidenced-by**, qualifying conceptual comparison: readers gain an explicit model requiring local justification and sufficient correlation for softgoal approximation, separate from constraint conformance. This is not corroboration of the note or evidence that a particular proxy works. The return path serves that reader need independently of the existing outbound link; its source-dependent use needs suitable grounding before authoring.

## Reverse-edge Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) → [this ingest](../../../../sources/revisiting-core-ontology-requirements-engineering-2008.ingest.md) — **evidenced-by**, bounding conceptual comparison: the source explicitly represents the target-to-quality mapping as defeasible and project-local. It provides a contrast to unexamined target achievement, not a demonstrated mechanism for testing those links or an empirical refutation of the note. The linking note must preserve that distinction and satisfy its source-grounding contract.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Objective revision](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md), proposed return evidence edge: representing preferences does not test the note's licensing claim; the outbound comparison is enough.
- [Theory builder](../../../../theory/definitions/theory-builder.md), proposed reciprocal source example: the paper's merely anticipated revision would add a weak partial case to a definition already explicit about its conditions.
- [Awareness Requirements](../../../../sources/awareness-requirements-adaptive-systems.ingest.md): downstream monitoring makes a plausible later comparison, but adds less than the direct baseline/approximation distinctions for this ingest.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Six retained outbound candidates cross only two local collections; no automatic three-topic split finding. The two optional source comparisons need not be added to the already compact accepted ingest.
- No candidate edge was authored. Bibliographic identity remains the 2008 conference preprint, arXiv v1, with the served-2018-byte caveat; this is not the blocked 2009 journal article.
