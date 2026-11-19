---
description: "Connection discovery for Jureta, Mylopoulos and Faulkner's RE 2008 core-ontology preprint, with project-local approximation and preference boundaries."
type: types/connect-report.md
source: "kb/sources/.snapshots/revisiting-core-ontology-requirements-engineering-2008.md"
source_has_frontmatter: true
date: "2026-11-16"
depth: standard
---

# Connection Report: Revisiting the Core Ontology and Problem in Requirements Engineering

**Source:** `kb/sources/.snapshots/revisiting-core-ontology-requirements-engineering-2008.md` (immutable local RE 2008 preprint; path recorded as operational context, not a durable snapshot link).

## Discovery Trace

Read the complete snapshot and sources collection contract before discovery. The snapshot is immutable; candidate outbound edges belong on its eventual name-paired ingest, not in the capture. No external search or semantic service was used.

- Curated heads: read `kb/theory/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/tags/README.md`, and `kb/sources/README.md`. The source has no tags. The tags head exposed `goal-prioritization-README.md`, which was read as a routing surface, not a membership recommendation.
- Titles: generated a fresh complete title surface for each of theory, reference, agent-memory-systems, agentic-systems, tags and sources using `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`. Read the truncated beginning from the tool's retained output. Exact implementation, objective revision, commitment, proximate target, Four Dark Corners and AGM titles were promising.
- Descriptions: ran `rg '^description:' kb/theory/ --glob '*.md' | rg -i 'proxy|requirement|objective|belief|revision'`; for reference, agent-memory-systems, agentic-systems and sources ran description listings filtered by `requirement|stakeholder|softgoal|goal authority|belief revision|ontology`. Exact implementation and objective revision remained strong. Operational Ontology Framework, Cortex, sage-wiki and EvoOntology appeared, but mere ontology organization does not establish shared approximation or preference semantics. Reference hits about workflow requirements and coverage did not supply a distinct reader need. Tags have no authorized source-to-tag label and were used only for routing.
- Body search: initial `rg -n -i 'operationaliz|goal authority|softgoal|justified approximation|non.monotonic|stakeholder|preference'` across the six substantive destinations was noisy and truncated. Narrowed to `rg -l -i 'softgoal|justified approximation|goal authority|non.monotonic'` across theory, reference, system reviews and sources. This surfaced the existing requirements-family ingests. `rg -n 'jApprox|justified approximation'` found no local authored hit. Absence in that query is not proof of absence under other wording.
- Theory: fully read exact implementation, objective revision, commitment and proximate target. Keep exact implementation for the separate warrant of a softgoal approximation, and objective revision for the distinction between ranking alternatives and authorizing new ends. Reject commitment as a separate edge: its derivation/commitment maintenance question is not the same as a stakeholder's commissive speech act. Proximate target was also exposed by the goal-prioritization head and description listing, then by links from exact implementation; keep an independently useful inbound candidate rather than another outbound proxy discussion.
- Sources: fully read Four Dark Corners and AGM. A guessed AGM filename failed with ENOENT; resolved the correct path with `rg -l -F 'Ingest: On the Logic of Theory Change' kb/sources`, then read it. Keep both: Four Dark Corners is the expressly criticized baseline; AGM distinguishes revision of closed theories under fixed consequence from this paper's defeasible consequence relation. Awareness Requirements, RELAX and requirements reflection appeared in descriptions/body searches, but are downstream monitoring/adaptation mechanisms rather than necessary companions for this conceptual source; omit to avoid a family-wide link spray.
- Reference: read epistemic stance, linked from the installed goal frame, to check that belief, adopted rule and criticism were not conflated. No separate reference edge retained: it would restate the global frame rather than add source-specific traversal value.
- System collections: curated heads, full titles, description filtering and the focused body query yielded no implementation-grounded comparison whose reader need outweighed the risk of treating a common word, ontology, as a common mechanism. No system candidate retained.
- Reverse pass: read `kb/theory/COLLECTION.md` in full. Its `evidenced-by` label permits a source to qualify or bound a claim without presenting it as corroboration. Exact implementation readers could inspect the paper's explicit local justification and correlation requirements. Proximate target readers could inspect an explicit model of the target-to-quality mapping while retaining the note's distinction between achievement and warrant. These are independent needs, not automatic reciprocals. Source-to-source `compares-with` is separately allowed by the sources contract.
- External: the canonical arXiv URL is already in hand; retain it as the source authority. No open-web prospecting. `kb/work/` and `kb/instructions/` were excluded as source-link destinations.

### Candidate origins

- kb/theory/exact-implementation-does-not-validate-a-requirement.md — titles, descriptions, curated-head, link-following
- kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md — titles, descriptions, curated-head, link-following
- kb/sources/four-dark-corners-requirements-engineering.ingest.md — titles, body-search, descriptions
- kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — titles
- kb/theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md — titles, descriptions, curated-head, link-following

## Connections Found

- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) — **compares-with**: the paper separates satisfaction of a measurable quality constraint from a project-local, revisable justification that it approximates a subjective softgoal. Readers gain a concrete conceptual account of the upstream link; no empirical validation of that mapping is established.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: attitude-based preferences and preferences over preferences make ranking explicit, while taking stakeholders and aggregation as inputs. This distinguishes a represented ranking from authority to replace terminal objectives.
- [Four Dark Corners of Requirements Engineering](../../../../sources/four-dark-corners-requirements-engineering.ingest.md) — **compares-with**: inspect the original environmental satisfaction obligation alongside the later paper's criticism and its addition of attitudes, quality constraints and defeasibility. Do not infer that the baseline claimed all the epistemic assumptions the later critique attributes to monotonic consequence.
- [On the Logic of Theory Change](../../../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md) — **compares-with**: AGM changes a logically closed theory under a fixed consequence operation; this paper proposes defeasible satisfaction and revisable approximation. Neither alone supplies discovery or empirical warrant.

## Bidirectional Candidates

- [Exact implementation](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) → eventual ingest — **evidenced-by**, qualifying comparison only: its reader can inspect the requirement that an approximation have a project-specific justification and sufficient correlation, rather than infer upstream validity from a passed constraint. Read the full source when checking this proposed use; no supporting Quotes are retained at this stage.

## Reverse-edge Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) → eventual ingest — **evidenced-by**, bounding comparison only: the paper explicitly represents the softgoal-to-constraint link and its possible revision, providing a contrast to unexamined target achievement. It does not show a working loop that tests those links or improve the note's empirical support by itself.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md): a source-side plan as communicated intention is not the note's retained free-choice commitment; the shared word would invite an unsupported equivalence.
- [Awareness Requirements](../../../../sources/awareness-requirements-adaptive-systems.ingest.md): a plausible downstream reader route, but monitor semantics are not this source's contribution and the baseline/approximation comparisons are more direct.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Keep the bibliographic boundary explicit: the captured work is the RE 2008 conference preprint, arXiv 0811.4364v1, not the 2009 Applied Ontology journal article. The served text prints a 2018 date despite its v1/2008 identifier; it does not establish original-2008 PDF bytes.
- All links above are discovery candidates only. No inbound or outbound library edges were authored by this run.
