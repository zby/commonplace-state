---
description: "Recovered standard discovery for the RE 2008 core-ontology snapshot, including belief-change and monitoring boundaries."
type: types/connect-report.md
source: kb/sources/.snapshots/revisiting-core-ontology-requirements-engineering-2008.md
source_has_frontmatter: true
date: "2026-11-16"
depth: standard
---

# Connection Report: Core-ontology snapshot

**Source:** `kb/sources/.snapshots/revisiting-core-ontology-requirements-engineering-2008.md` (immutable RE 2008 reading copy; authored suggestions belong on the matching ingest).

## Discovery Trace

Recovery pass 3 in session `01a1e671-3b1d-7152-987a-71ba5516dc29`, under the fully read connect skill, connect-report type and sources contract. Read the complete snapshot in ranges 1–430 and 431–844, including references. Its speech-act/DOLCE distinctions lead to goals, plans, domain assumptions, quality constraints, softgoals and attitudes. Justified approximation is project-local, requires sufficient correlation and may be defeated. Defeasible consequence and preference handling reformulate acceptability; they do not implement elicitation, justification or iterative learning.

### Heads and breadth

Used the six fully read same-session curated heads: `kb/theory/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/tags/README.md`, `kb/sources/README.md`. Previously read candidate bodies were available for reevaluation; the title/search surfaces below were generated afresh for this target. No target tags, so no by-tag query/completeness shortcut. Read the goal-prioritization tag head as a promising routing lead. Prospected all six local destinations. Theory and sources supply the strongest conceptual comparisons. System ontology is not presumed to mean the same thing. Work/instructions excluded; no external prospecting beyond the supplied source identity.

### Fresh complete titles and actual searches

Two bash results headed `PASS 3` displayed the full unfiltered titles for theory/reference and then historical memory/agentic/tags/sources. For each destination D:

`rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/D/ --glob '*.md' --glob '!*.brief.md'`

Inspected the complete contents, without head caps, keyword selection or title truncation. For each of the six destinations additionally ran:

- `rg -i '^description:.*(proxy|objective|belief|revision|ontology|stakeholder|softgoal)' kb/D/ --glob '*.md'`
- `rg -n -i 'softgoal|justified approximation|jApprox|preference aggregation' kb/D/ --glob '*.md'`
- `rg -l -i 'non.monotonic|belief revision|goal authority|preferences over preferences' kb/D/ --glob '*.md'`

These results were not capped or truncated. No numeric scores: local rg discovery is unranked. Filename hits are candidate leads, not full reads.

### Evaluations and one-hop neighborhoods

- **Theory:** Exact implementation, Objective revision and Proximate target were known from the archived reports and fully read earlier; re-exposed by titles/descriptions and, for the first two, by the goal-prioritization head. Keep the first two outbound: separate approximation warrant from constraint satisfaction, and ranking from authority to change ends. Keep Proximate target inbound only: its reader can inspect an explicitly represented target-to-quality relation. Commitment was fully read and rejected: a communicated intention is not retained free-choice arbitration. Fixed decomposition and Theory builder were also fully read; reserve their more specific mapping for the accepted-ingest assessment rather than attach every learning-related comparison to the raw paper. Read Claim test record versus fit and Warranted autonomy fully while following the proxy/epistemic boundary: the former concerns a claim's problem-relative contribution rather than requirements preference, and the latter limits what an oracle licenses rather than supplying stakeholder authority. Neither earns another edge.
- **Sources:** fully read Four Dark Corners and AGM and retain both. The first is the expressly criticized baseline; its informal-validation caveats must not be erased by the later paper's monotonicity critique. AGM revises deductively closed theories under a fixed consequence operation, not the consequence relation itself. Followed AGM's belief-base contrast to Hansson's In Defense of Base Contraction, newly read in full: reject a third belief-change edge because explicit-base dependency loss is not the paper's approximation mechanism and AGM already exposes the relevant distinction. ATMS (fully read in pass 2) offers assumption-context maintenance, not an adequacy oracle. Awareness Requirements was fully read as a body-search lead and retained: it separates this conceptual approximation relation from instrumented monitoring of adopted requirements. Requirements Reflection, fully read earlier, is weaker here because runtime object synchronization is not approximation warrant.
- **Reference:** read Epistemic stance fully, following the installed goal frame to avoid treating communicated beliefs as established truth. Reject a separate link: the global stance supplies no distinct source-specific comparison. Other title/description hits are workflow requirements and local storage/control selections.
- **Historical memory:** Operational Ontology Framework, Cortex, sage-wiki and EvoOntology are title/description leads. Reused the fully read Operational Ontology Framework review to check the temptation: governed ontology templates are not this paper's speech-act/quality ontology. The other descriptions concern memory organization, not sufficient correlation or preference semantics; no system edge retained.
- **Agentic systems:** all titles and scoped searches inspected. Eigenius, fully read in pass 1, concerns verification under an encoding boundary rather than softgoal approximation or stakeholder aggregation. Other memory/runtime leads supply no closer named mechanism. No agentic-system comparison kept.
- **Tags:** goal-prioritization head routes to the retained goal-position and authority comparisons. No authorized source-to-tag label and no substantive need to propose one. No membership change.

### Independent inbound reader needs

Applied the fully read `kb/theory/COLLECTION.md` source-directed `evidenced-by` permission to qualify or bound, not imply corroboration. Independently assessed Exact implementation and Proximate target: both readers gain an explicit local, defeasible approximation relation and its acknowledged justification gap. Exact implementation's return edge belongs in Bidirectional Candidates; Proximate target has no kept outbound edge and belongs in Reverse-edge Candidates. Objective revision readers do not gain evidence of legitimate authority from represented preferences, so reject a return edge there. Theory builder would receive only another partial/non-working case, not an independently useful definition example. Any future durable citation must target the accepted ingest and obtain Quotes or declare `(snapshot required)`; the current empty quote pool does not substantiate a source-dependent use.

### Candidate origins

- kb/theory/exact-implementation-does-not-validate-a-requirement.md — known, titles, descriptions, curated-head
- kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md — known, titles, descriptions, curated-head
- kb/sources/four-dark-corners-requirements-engineering.ingest.md — known, titles, descriptions, body-search
- kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — known, titles
- kb/sources/awareness-requirements-adaptive-systems.ingest.md — known, titles, descriptions, body-search
- kb/theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md — known, titles, curated-head

## Connections Found

- [Exact implementation](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) — **compares-with**: checking a measurable quality constraint does not warrant its local approximation of a softgoal. The paper represents the additional relation without empirically establishing a particular proxy.
- [Objective revision](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: preferences and preferences over preferences rank choices but do not settle who may replace terminal ends or why that replacement is licensed.
- [Four Dark Corners](../../../../sources/four-dark-corners-requirements-engineering.ingest.md) — **compares-with**: inspect the baseline's environmental satisfaction argument and informal validation beside the later softgoal/preference extension; do not equate monotonic inference with a claim to complete, unrevisable environmental knowledge.
- [AGM](../../../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md) — **compares-with**: distinguish belief-set revision under a fixed consequence operation from defeasible consequence and revisable softgoal approximation; neither supplies discovery or empirical warrant by itself.
- [Awareness Requirements](../../../../sources/awareness-requirements-adaptive-systems.ingest.md) — **compares-with**: follow the conceptual softgoal-to-quality-constraint relation into monitoring of adopted requirements and assumptions; instrumented satisfaction verdicts do not demonstrate criticism or repair of the approximation relation.

## Bidirectional Candidates

- [Exact implementation](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) → matching ingest — **evidenced-by**, qualifying conceptual comparison: its reader gains an explicit project-local approximation obligation distinct from constraint conformance. Not corroboration of the note or a measured working proxy. Source grounding is required before authoring.

## Reverse-edge Candidates

- [Proximate target](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) → matching ingest — **evidenced-by**, bounding comparison: the source names the target-to-quality mapping as a distinct defeasible object; it neither demonstrates a loop testing it nor refutes the note's claim that achievement checks do not warrant it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Base contraction](../../../../sources/in-defense-of-base-contraction.ingest.md) — useful one-hop clarification of AGM, but explicit-base dependencies are not the source's distinctive approximation or preference mechanism.
- [ATMS](../../../../sources/an-assumption-based-tms.ingest.md) — maintaining conditional support is not producing empirical warrant or diagnosing which assumption should change; omit another adjacent machinery edge.
- [Commitment](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) — do not equate communicated intention with the KB's retained resolution of a free choice.
- [Claim test record versus fit](../../../../theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md) — epistemic contribution to a problem is not stakeholder preference ranking.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Five outbound candidates concern approximation, authority and belief change: flag a possible split candidate if a later author develops these into independent claims. This broad discovery map does not itself recommend expanding or splitting a faithful single-source ingest. The accepted-ingest pass evaluates its actual scope separately.
- Identity remains RE 2008/arXiv v1, not the blocked 2009 journal article. Served bytes print October 22, 2018; original-2008 bytes are unestablished. No candidate links were authored.
