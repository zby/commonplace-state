---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/duguid-on-rereading-suchman-situated-action.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: On rereading. Suchman and Situated Action

**Source:** [Ingest: On rereading. Suchman and Situated Action](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md)

The ingest already carries a full inline Connections Found section (Dittrich ingest, two-layer execution, fails-soft interpreter, underspecified instructions, actionable methodology, the two bitter-lesson notes, Naur, Argyris, Norman). All ten targets exist. This report lists only candidates not already linked, plus reverse edges.

## Discovery Trace

**Linking rules:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (sparingly), `derived-from` (external only). External prospecting skipped; the source URL is already in frontmatter.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (source's tag; `complete: true`, so by-tag rg skipped for theory). Flagged: two-layer execution (already linked), intent-framed delegation, fix-what-the-executor-cant-determine, methodological-and-computational-closure, specification-strategy, borrowed-patterns.
- By-tag listing for sources: `rg -l '^tags:.*method-guided-action' kb/` -- sibling sources: pd-of-hci Suchman summary, Haynes checklist, CMMN, Church-Turing SEP, Dittrich. Flagged pd-of-hci and Haynes.

**Body search** (over `kb/theory kb/sources kb/agentic-systems kb/reference`, excluding proposals/ADRs):
- rg -i "Suchman" -- only the three Suchman ingests (Dittrich, pd-of-hci, this one). pd-of-hci not linked from the source: kept.
- rg -i "situated action|situated" -- actionable-methodology (linked), marine-corps MCDP-1 ingest, Argyris (linked), design-rationale note, information-value note; latter two only use "situated" loosely: rejected.
- rg -i "Orr\b|Julian Orr" ; "Taylor|Babbage" ; "Dreyfus|Winograd|Heidegger" -- no KB artifacts besides this ingest (and Sutskever reference lists). Confirms the ingest's "no artifact on this lineage" claim.
- rg -i "workaround" -- fails-soft note (linked), final-task-success-does-not-establish-intended-path-health, specification-strategy, soft-degradation, Norman (linked), Borretti. Kept final-task-success.
- rg -i "ritual compliance|apparent conformity|conformity" -- Argyris (linked), MCDP-1 ("act in conformity with the intent of the senior"). Kept MCDP-1 on the control axis.
- rg -i "tacit|cannot all be made explicit|inexplicit" -- two-layer (linked), boundary-of-automation-is-boundary-of-verification, soft-bound-traditions, operationalism-sep. Evaluated, rejected (see below).
- rg -i "resource for action|plans as resources" -- only the Suchman ingests.
- rg -i "Moore.s Law|principled" -- wikipedia-bitter-lesson ingest and scattered "principled" uses; bitter-lesson theory notes already linked. Rejected the rest.

**Link following:**
- pd-of-hci ingest -> silent-disambiguation-is-the-semantic-analogue-of-tool-fallback and human-analogies notes. Followed silent-disambiguation: its description (silent repair hides that the contract failed) matches Duguid's surreptitious routinization at the human level. Kept.
- final-task-success note: read body. Its three-state model (primary success / fallback success / hard failure) and "outcome cannot identify path health" is the computational form of Orr's technicians, whose record shows the plan followed. Kept.
- two-layer execution note lines 16-26: promotion is driven by recurrence of fallback; confirms the reverse edge (visibility is a precondition the note does not state).
- Workshop `kb/work/operationalization-executability-automation/exploration.md` §5 table and §6.6: lists Suchman, Dittrich, Haynes; Duguid and pd-of-hci not yet listed.

## Connections Found

- [PD of HCI summary of Suchman](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**: third secondary pointer to Suchman; axis is coverage of the book. Duguid gives the plans-as-resources claim and its reception (Simon and Vera misreading, Orr, Moore's Law); the 1997 summary gives the 1987 argument structure (copier breakdown typology, three design problems). Readers reconstructing Suchman need both, and the Dittrich comparison in the ingest is incomplete without this third leg.
- [Haynes 2009 surgical safety checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) -- **compares-with**: axis is whether pressure toward procedure conformity improves practice or hides its gaps. Duguid/Orr: conformity demand produces surreptitious routinization; Haynes: a read-aloud checklist adjusted to local flow improved outcomes. The ingest's Limitations already names "the Haynes checklist ingest" without linking it; this would make that counter-case followable.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) -- **compares-with**: axis is outcome-indistinguishable fallback. The note argues that when intended-path and fallback success share a terminal state, the outcome cannot reveal path health; Orr's technicians are a human case where the record shows the plan followed while improvisation carried the work. Compare-with rather than is-evidence-for, because the note's mechanism is a tool loop and the transfer is analogy (as the ingest already says of the fails-soft note).
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: axis is invisible repair of an inadequate specification. The note: an agent silently resolves spec ambiguity and success hides the contract's failure; Duguid: workers make the world appear to follow the plan, hiding the plan's inadequacy and the repair's insight. Gives a reader of Extractable Value item 2 the KB's closest named mechanism.
- [Marine Corps MCDP-1 Warfighting](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) -- **compares-with**: axis is how a plan governs a competent executor. Duguid's Taylorist framing replaces interpretation with obedience to a plan; MCDP-1 binds the subordinate to intent and leaves the means to situated judgment. Useful for Extractable Value item 3 (Taylor vs Babbage), which currently has no KB counterpart. Moderate strength; the Taylor claim is unargued in Duguid.

## Bidirectional Candidates

- [PD of HCI summary of Suchman](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) <-> source -- **compares-with**: the summary links Dittrich but not Duguid; Duguid supplies the reception history and the conformity/routinization point the summary lacks. Both files are currently untracked, so the pair could be connected before commit.
- [Dittrich rereading of Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) <-> source -- **compares-with**: Duguid links Dittrich; Dittrich's Limitations say it cannot establish "plans as resources", which Duguid states. A return link would point Dittrich readers to the claim's best available secondary statement.

## Reverse-edge Candidates

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) → source -- under theory's own rules (an evidence/qualification edge to a source): Orr's case, via Duguid, names a precondition for recurrence-driven promotion the note does not state: fallback must be visible, and conformity pressure suppresses it. Could join the note's Open Questions on fallback traffic.
- [A goal-holding interpreter fails soft; workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) → source -- human analogue of unrecorded workarounds absorbing an inadequate procedure; analogy only.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) → source -- a non-software illustration of the same observability gap, marked as analogy.
- `kb/work/operationalization-executability-automation/exploration.md` → source -- the §5 source table and §6.6 still treat Dittrich as the only Suchman stand-in; the ingest's own Recommended Next Action asks for this entry. (Workshop may link to sources; sources may not link to work.)

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- matched on "tacit"; its axis is verification cost, which Duguid does not address.
- [Soft-bound traditions as sources for context-engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- survey-level adjacency; situated action is not among its assessed traditions in a way the ingest could use.
- [Operationalism SEP](../../../../sources/operationalism-sep.ingest.md) -- "operations fix a concept only partially" is a different partiality (concept meaning, not plan execution); keyword-level.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- tempting for Taylor vs Babbage (what the method settles vs who executes), but the essay's lineage claim is unargued and the mapping would be the reader's construction. Revisit if the workshop develops item 3.
- [Intent-framed delegation is a control regime](../../../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) -- same axis as MCDP-1 but MCDP-1 is the closer, source-level comparison; linking both would duplicate.
- [Borrowed patterns transfer only over shared mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- the ingest already applies its analogy caveat; a link adds little.
- [Wikipedia bitter lesson ingest](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- the theory-level bitter-lesson notes already linked carry the identification problem better.

## Index Membership

- [method-guided-action tag head](../../../../tags/method-guided-action-README.md) -- source already carries the tag; sources do not participate in generated membership, so no head entry needed.

## Synthesis Opportunities

Three KB claims and two sources converge on one mechanism: final-task-success (tool fallback hides path health), silent-disambiguation (semantic repair hides spec failure), the fails-soft interpreter note (workarounds tax a budget), Norman (silent autopilot compensation) and Argyris/Orr-via-Duguid (control pressure produces ritual or surreptitious compliance). Candidate higher-order claim: competent executors compensate for inadequate instructions by default, and the compensation erases the evidence that the instruction needs repair unless deviation is recorded separately from outcome. The human-side cases add a cause the computational notes lack: pressure to appear conforming actively suppresses the deviation record. Belongs in the workshop first, not as a note yet.

## Maintenance Observations

- The ingest's Limitations names "the Haynes checklist ingest" in prose without a link; a reader cannot follow it.
- Two of the three Suchman ingests (this one and pd-of-hci) are untracked and not cross-linked; the workshop table still lists only Dittrich as the stand-in.

## Flags

- Split candidate: no. The ingest has many connections across several areas, but it is a source analysis, not a single-claim note.
- Tension: Duguid's conformity-hides-gaps argument vs Haynes's checklist success. Not resolved here; the workshop is the place to name conditions under which enforced procedure helps or hides.
