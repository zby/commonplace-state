---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: PD of HCI - Plans and Situated Actions (summary of Suchman)

**Source:** [Ingest: PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md)

The ingest already authors seven outbound links (Dittrich ingest, two-layer execution system, interpret-underspecified-instructions, actionable methodology, silent disambiguation, Norman ingest, human analogies). All seven paths exist. This report proposes only additions to that set and reverse edges into it.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (sparingly). External prospecting skipped (no supplied external target; the `source` URL is already in frontmatter).

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (source's tag; `complete: true`, so by-tag rg skipped). Candidates flagged: methodology-enforcement-is-constraining (activation vs response), fix-what-the-executor-cant-determine, specification-strategy-should-follow-where-understanding-lives, two-layer execution system (already linked).

**Body search** (all over `theory reference agentic-systems agent-memory-systems tags sources`, `rg -il`):
- `suchman` -- only the three Suchman ingests (this, Dittrich, Duguid). Duguid ingest is new and unlinked from this source.
- `situated` -- hits in actionable-methodology (already linked), design-rationale-must-preserve-unregenerable-decision-premises (Naur's "situated programmer"; keyword), information-value-is-observer-relative (TODO mention; keyword), `agentic-systems/reviews/ai-agent-book.md` ("the agent is the situated loop"; keyword, different sense), various sources (keyword).
- `indexical` -- only Gibson linguistics ingest (different sense); rejected.
- `breakdown` -- specification-strategy note and memory-system reviews; all task/work breakdown sense, not interactional breakdown; rejected.
- `after-the-fact|post hoc|post-hoc rationali` -- structure-inference-needs-capture-at-the-decision-surface and others; checked descriptions, none treats plans as retrospective accounts of action.
- `controlling structure|resources? for action|plans as` -- Dittrich and Duguid ingests; SkillX and compound-engineering reviews (keyword only).
- `ethnometh`, `mutual intelligib|common ground`, `garden path|false alarm`, `user model` -- no theory hits; `false alarm` hits in gate-calibration proposal and hidden-failures ingests are the detection-error sense, not Suchman's communicative breakdown; rejected.
- `decision autonomy|function-level automation|levels of automation` -- sibling workshop-occasion ingests (Haynes, Norman, Duguid, Dittrich, operationalism, Church-Turing, CMMN, Plotkin). Haynes kept; others share only the occasion string.
- `transparent activity|ready-to-hand|present-at-hand|heidegger|winograd` -- Duguid ingest (Heideggerian premise); kept via Duguid.
- `clarifying question|ask the user|...|limits of (its|the machine)` over theory -- design-for-the-first-time-human-except-on-access-cost; access-cost sense, rejected.

**Link following:**
- Duguid ingest Connections Found: links Dittrich, two-layer, goal-holding interpreter, interpret-underspecified, actionable methodology, bitter-lesson notes, Naur note, Argyris ingest, Norman ingest. Naur note and goal-holding interpreter followed.
- Haynes ingest Connections Found: links methodology-enforcement-is-constraining, promotion-selects-for-unreliable-activation, knowledge-storage-does-not-imply-contextual-activation, actionable methodology, Norman ingest. methodology-enforcement-is-constraining read (activation rule vs response rule).
- `naur-equates-machine-execution-with-formulated-criteria.md` read: human-only conclusion needs a bridge premise from unformulated judgment to computational inability.
- Grep for `pd-of-hci` in Dittrich, Duguid, Haynes, Norman ingests: no inbound links exist yet.

## Connections Found

- [Ingest: Duguid, On rereading. Suchman and Situated Action](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) -- **compares-with**: the third secondary reading of the same book, on the axis of what each establishes about plans. Duguid states "plans as resources" directly and adds Orr's copier technicians (hidden workarounds) to the summary's copier users (undetected breakdowns); the summary gives the 1987 chapter structure and the three design problems Duguid does not. The current ingest frames itself as the "second secondary pointer" beside Dittrich only; that framing is now stale.
- [Ingest: Haynes 2009, WHO surgical safety checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) -- **compares-with**: on the axis of when a plan is consulted. Suchman, as summarized, has the plan consulted when "otherwise transparent activity becomes in some way problematic"; the checklist forces consultation at fixed junctures whether or not anything has gone wrong. Together they bracket the workshop's operationalization question: breakdown-triggered versus scheduled plan use.
- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) -- **compares-with**: the note separates an activation rule from a response rule. The summary's plans-as-resources position is a claim about both: activation is breakdown-driven (the executor recognises trouble) and response is interpreted, never a controlling structure. It names the routed-instruction row's latitude as the normal human condition rather than a weak enforcement level. Hold at secondary-summary strength.
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- **compares-with**: the summary's objection that world models cannot hold common-sense background knowledge, and that background assumptions are generated in interaction, is the same move from inexplicit understanding toward machine inability; the note's missing-bridge-premise analysis applies to it. Duguid's ingest already draws this comparison for the Heideggerian premise; this source supplies the planning-model version.

## Bidirectional Candidates

None beyond the reverse edges below.

## Reverse-edge Candidates

- [Ingest: Duguid, On rereading. Suchman and Situated Action](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) → source -- **compares-with**: Duguid's Connections Found compares itself with Dittrich only; the summary is the sibling that supplies the copier-study breakdown typology and design problems Duguid relays only in part.
- [Ingest: Dittrich rereading Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) → source -- **compares-with**: Dittrich's Limitations say it cannot establish the argument's structure; this summary is the ingest that does, on the edition axis (2nd vs 1st).
- [Ingest: Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) → source -- **compares-with**: this source already links Norman on the axis of interactional resources the machine lacks (Suchman's second design problem vs Norman's feedback); the return edge is useful for a reader starting from Norman. Optional.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) → source -- **evidenced-by** (theory label; qualifies, not corroborates): the situated-default/plan-fallback inversion is a candidate qualification. Prefer citing the Duguid ingest, which states the claim with an author; cite this summary only alongside it, and only after the book is checked, given the uncredited-summary caveat.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Argyris on organizational learning and MIS](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) -- Duguid's comparison rests on Orr's hidden workarounds, which this summary does not cover.
- [A goal-holding interpreter fails soft](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- same: the fit runs through Orr's technicians in Duguid, not the copier-user study here.
- [Promotion selects for unreliable activation](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) -- adjacent via Haynes, but the summary says nothing about promotion or recall failure; would be a two-hop association.
- [An author should fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- topical (plans can't fix situated action), but the summary gives no decision rule to compare; the link would assert more than the source supports.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- "breakdown" hit is task decomposition, not interactional breakdown.
- [Design rationale must preserve unregenerable decision premises](../../../../theory/design-rationale-must-preserve-unregenerable-decision-premises.md) -- "situated" keyword only (Naur's programmer).
- `kb/agentic-systems/reviews/ai-agent-book.md` -- "situated loop" is a different sense.
- `kb/reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md`, hidden-failures ingests -- "false alarm" in the detection-error sense.

## Index Membership

None (sources do not participate in tag membership; `method-guided-action` tag on the ingest is already present and fits the plans-as-resources analysis).

## Synthesis Opportunities

The three Suchman secondaries plus Haynes and Norman imply a workshop-level distinction: plan consultation can be breakdown-triggered (Suchman), schedule-triggered (Haynes), or absent with silent compensation (Norman's autopilot, Orr via Duguid). This maps onto the activation axis of methodology-enforcement-is-constraining. Candidate material for the operationalization workshop, not a note yet; the Suchman leg still needs the book.

## Maintenance Observations

- The source's "second secondary pointer" framing predates the Duguid ingest (same day, currently untracked); the Connections Found prose and Recommended Next Action should be updated to a three-secondary set.
- No inbound links to this ingest exist from any sibling Suchman/automation ingest.

## Flags

- Tension: the source treats Dittrich as the complementary sibling; Duguid now supplies the plans-as-resources claim more authoritatively. A future editor should decide which secondary carries which Suchman claim to avoid citing the uncredited summary where Duguid suffices.
