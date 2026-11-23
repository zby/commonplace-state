---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: A Truth Maintenance System (Doyle, MIT AI Memo 521, 1979)

**Source:** [Ingest: A Truth Maintenance System (Doyle, MIT AI Memo 521, 1979)](../../../../sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md)

## Discovery Trace

**Setup:**
- Read `kb/sources/COLLECTION.md` outbound section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for`, `abstracted-from`, `rests-on` (theory); `compares-with` (theory, sources, agent-memory-systems, agentic-systems); `defined-in` (theory/definitions); `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external); `derived-from` (external only).
- External prospecting skipped: no external target was supplied, and the ingest's `source` URL is already its provenance.
- The ingest already carries 15 inline links (6 sources, 9 theory). Every existing target was checked and resolves. This report proposes only edges the ingest does not yet carry.
- Loaded prior reports as context: `doyle-1979-truth-maintenance-system-aim-521.connect.md` (a run on the snapshot, made before this ingest existed) and `doyle-1979-glimpse-of-truth-maintenance.ingest.connect.md`. Each candidate they named was re-checked against the ingest as written, not carried over on their word.

**Curated heads:**
- `kb/tags/learning-theory-README.md` (`complete: true`) and `kb/tags/reflection-README.md` (`complete: true`): read for routing. By-tag `rg` was skipped for both because they are complete. The reflection head surfaced the explicit-retention note and the reflective-system definition, which the ingest already links. It also surfaced "Reflection makes retained lessons second-order", which was rejected (see below).

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' theory/ --glob '*.md' --glob '!*.brief.md' | rg -i 'critic|revis|retract|belief|defeas|argument|assumption|contradict|withdraw|append|supersed|reason|rationale|choice|choose|backtrack|dialect|objection|challeng|stale|retire'`. Flagged: "Backtracking keeps lightweight search control provisional", "Claim notes should use Toulmin-derived sections", "Retire, Redact, Supersede, And Relax Memory", "Reasoning production is not reasoning evaluation", "Design rationale must preserve decision premises", "Link graph plus timestamps", "An objection can show where to split an on-balance judgment". The already-linked superseded-choices and rationale-faithfulness notes also appeared.
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' sources/ --glob '*.ingest.md' | rg -i 'belief|revision|contraction|argument|truth|reason|criticism|popper|...|deliberat'`. Flagged: "On the Logic of Theory Change" (AGM), "Practical Reason (SEP)", "Introduction to Deliberative Democracy", "Toulmin Argument", "Principles of Metareasoning", "Agentic Note-Taking 23: Notes Without Reasons", "BDI Agent Architectures: A Survey".
- `ls sources | rg -i 'contraction|agm|theory-change|reiter|mcdermott|pollock|dung|toulmin|lakatos|popper'`. Confirmed AGM and Toulmin paths. No McDermott–Doyle non-monotonic logic, Reiter default logic, Pollock or Dung ingest exists.

**Description listing:**
- `rg -m1 '^description:'` on the flagged theory and source candidates, plus `theory/definitions/theory-builder.md`, `theory/definitions/tentative-theory.md`, `theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md`, `theory/evolving-understanding-needs-holistic-rewrite-not-composition.md`, `reference/proposals/repair-dispositions-for-defeated-claims.md` and `reference/design-rationale-management.md`.

**Body search:**
- `rg -l -i 'truth maintenance|truth-maintenance|\bTMS\b|JTMS|ATMS|doyle' --glob '*.md' .`. Hits: the two Doyle ingests, the ATMS and Bacchus–van Run ingests, `theory/a-claim-without-external-assessment-carries-three-obligations.md`, about 25 frozen agent-memory reviews using "truth maintenance" loosely, and two agentic-systems retained-archive results. No live artifact links either Doyle ingest.
- `rg -n -i 'quine|minimum mutilation|rescher|web of belief'` over theory, sources, reference and agentic-systems, excluding Doyle: no hits. This confirms the ingest's claim that it is the KB's first anchor for Quinean pragmatic revision.
- `rg -n -i 'dialectic|defeat(ed|er|s)? |append-only|only grows|never discard|monotonic' theory`: no theory note discusses dialectical argument stores. Hits were ordinary "defeats" usages, the domain-pricing note's "defeated crisp claims" and the program-refinement monotonicity section, which uses a different sense.
- `rg -l -i 'append|criticism.*(retain|kept|record)|retain.*critic' theory`: surfaced the holistic-rewrite note (a tension, see Flags), the theory-builder definition and the test-record note.
- `rg -l 'an-assumption-based-tms|in-defense-of-base-contraction|logic-of-theory-change-partial-meet|making-reflective-equilibrium-precise'` over theory, reference, agentic-systems, tags and sources: the only theory citer is the three-obligations note (lines 185–189). That passage pairs the ATMS and base-contraction ingests to show that dependency maintenance, warrant and selection policy are separate. The Fishkin ingest links the reflective-equilibrium ingest on the meaning of "weighing".
- `rg -n -i 'selection function|minimal|tms|doyle|epistemic entrenchment|choice'` in the AGM ingest: line 42 treats the selection function as "an unresolved governance input". This is the same gap Doyle leaves open.
- `rg -n -i 'truth maintenance|belief revision|dependency-directed|justification'` over agentic-systems: the Eigenius review's justification certificates and the correction-propagation comparison. See Rejected.
- `rg -l -i 'retract|defeated|withdraw' reference`: ADR 066, ADR 091 and the repair-dispositions proposal. Only `see-also` is authorised to reference, and none of these hits carries a mechanism-level adjacency.
- `rg -n 'aim-521'` in the Glimpse, ATMS, Bratman and base-contraction ingests: none links the memo ingest yet.

**Link following:**
- Three-obligations note, from its ATMS/base-contraction pairing at line 187: this led to a reverse-edge candidate.
- Glimpse ingest, line 60 (premises and rules "are never revised") and line 78 (notation "need[s] the page images or the full memo"): the memo ingest corrects both, which makes the return link a bidirectional candidate.
- AGM ingest, line 36: AGM's selection function does not show condition 3 of the theory-builder definition. This parallels the memo ingest's own grading of condition 3, so the AGM edge is kept.
- Theory-builder definition, lines 40–58: criticism "is itself stated, so it can be criticized in turn". The memo ingest's condition 3 relies on exactly this point without linking the definition.

### Candidate origins

- kb/theory/definitions/theory-builder.md — known, body-search, link-following
- kb/theory/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md — known, descriptions
- kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md — body-search, descriptions
- kb/theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md — known, titles
- kb/theory/backtracking-keeps-lightweight-search-control-provisional.md — known, titles
- kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — titles, body-search, link-following
- kb/sources/sep-practical-reason.ingest.md — known, titles
- kb/sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md — titles, body-search
- kb/sources/introspective-multistrategy-learning.ingest.md — known, descriptions
- kb/sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md — known, body-search, link-following
- kb/sources/an-assumption-based-tms.ingest.md — known, body-search
- kb/sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md — known
- kb/theory/a-claim-without-external-assessment-carries-three-obligations.md — body-search, link-following
- kb/theory/cost-sensitive-formalisms-for-tentative-theory-search.md — known

## Connections Found

All edges are recommendations for a future edit of `doyle-1979-truth-maintenance-system-aim-521.ingest.md`.

**Theory**

- [Theory builder](../../../../theory/definitions/theory-builder.md) -- **defined-in**: the Learning Claims section grades the system against "Theory-builder conditions" 1–4 but links only the addressable-theory definition. A reader cannot interpret "Criticism: substantially stronger … the challenge can itself be challenged, which matches the definition's point" without the definition. That point is the definition's statement that a criticism is stated and can be criticized in turn.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../theory/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- **is-evidence-for**: a nogood records only that a set of assumptions is jointly inconsistent. Doyle calls random culprit choice within that set "blind search". Section 6 makes it worse: reifying every step multiplies the assumptions behind each node. This mechanized case shows that joint failure does not identify the failing component, as the note claims. It bounds the note rather than corroborating it, since it is a symbolic system that was not built to test the claim.
- [A claim's test record does not determine its fit in a working theory](../../../../theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md) -- **compares-with**: compare on what standing an accepted claim has. Doyle's in/out status is support by currently valid reasons, and he explicitly excludes truth from it ("opinion revision system", "narrowly psychological rationality"). That is a prior design that separates current acceptance from truth. It has no counterpart to the note's test record. The note says the three-way separation is its own analysis, so the comparison shows which half has precedent.
- [Claim notes should use Toulmin-derived sections for structured argument](../../../../theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md) -- **compares-with**: compare on making the inference step an explicit, challengeable object. Section 6 gives each step a node J and a "challenged" node ¬J, which works as a mechanized rebuttal slot. The Toulmin note proposes prose sections for warrant and caveats. The ingest's Extractable Value item 3 (appending criticism rather than overwriting) needs this comparison to land in Commonplace's claim format.
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) -- **is-evidence-for**: the ingest names Section 8's canned control patterns (defaults, ordered alternatives). These encode provisional choices whose rejection advances to the next alternative through dependency-directed backtracking. This bounds the note: Doyle also notes that the simple sequence encoding gives no direct way to reconsider rejected alternatives. Verify that wording against the page images before quoting, because the Section 8 formulas are garbled in the OCR.

**Sources**

- [On the Logic of Theory Change (AGM) ingest](../../../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md) -- **compares-with**: compare on who supplies the revision-choice criterion. AGM's partial meet contraction depends on a selection function that the paper leaves as "an unresolved governance input". Doyle likewise requires "explicit ways to choose what to believe" and supplies none of his own. Both ingests grade theory-builder condition 3 as unestablished for this reason. Rescher's "minimum mutilation", which the ingest mentions, is the informal ancestor of AGM's minimal-change postulates.
- [SEP practical reason ingest](../../../../sources/sep-practical-reason.ingest.md) -- **compares-with**: same occasion (the deliberative-learning workshop). Compare on what practical reasoning is. Doyle's Section 1.1 holds that "rational thought is the process of finding reasons for attitudes", a reason-construction account with no weighing step. The SEP entry describes deliberation as weighing reasons for and against options. In Doyle, weighing reappears only as the unsupplied choice rules of Section 8.
- [Fishkin and Mansbridge deliberative democracy ingest](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) -- **compares-with**: same occasion. Compare on group argument. Section 6's debater modules form a multi-party argument in which any step can be challenged and nothing is discarded. Fishkin and Mansbridge's deliberation weighs competing arguments under conditions that decide which arguments are heard. Doyle has the challenge structure but no weighing and no conditions on participation. This sharpens the ingest's finding that the choice mechanism is the gap.
- [Introspective multistrategy learning ingest](../../../../sources/introspective-multistrategy-learning.ingest.md) -- **compares-with**: compare on blame assignment and repair from recorded reasoning. Doyle's Section 8 proposes revision plans indexed by problem-solver state, each a specialization of dependency-directed backtracking, and defers the mechanism to a thesis. Meta-AQUA implements a related step: it diagnoses failure from an explicit reasoning trace and plans a sequence of repairs. It shows what the deferred mechanism might look like when built.

## Bidirectional Candidates

- [Glimpse ingest](../../../../sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md) <-> source -- **compares-with**: the memo ingest **corrects** two Glimpse statements: that premises and rules "are never revised" (Glimpse line 60), and the implied indifference to choosing well. The Glimpse Limitations section also defers exact notation to "the full memo". Without a return link, a reader of the Glimpse ingest takes the uncorrected reading.
- [An assumption-based TMS ingest](../../../../sources/an-assumption-based-tms.ingest.md) <-> source -- **compares-with**: the ATMS was defined against Doyle's single-context JTMS. The memo ingest records Doyle's own admission that relaxation is blind and sometimes non-incremental, and his Section 9 wish for "multiple supporting-justifications". These are the costs that motivated the ATMS. The ATMS ingest links neither Doyle ingest.
- [Bratman–Israel–Pollack ingest](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md) <-> source -- **compares-with**: same occasion. A reader of IRMA's filter-override policy gains the contrasting design, in which intentions are reason-backed attitudes revised whenever new reasons arrive and reconsideration is never a separate decision.

## Reverse-edge Candidates

- [A claim without external assessment carries three obligations](../../../../theory/a-claim-without-external-assessment-carries-three-obligations.md) → source -- **evidenced-by**: the "Which dependencies must survive revision" bullet uses the ATMS and base-contraction ingests to show that dependency maintenance, evidential warrant and selection policy are separate. Doyle states that separation in his own terms. He separates support from truth (Sections 2.1 and 10), and Sections 6 and 8 demand separate pragmatic choice rules. Check the note's source-link budget before adding a third parenthetical source.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) → source -- **evidenced-by**: the ingest links the note, but the note does not cite either Doyle ingest. The memo supplies the conflict-directed family's founding admission that random culprit choice "relies on blind search". It also supplies two named remedies (canned control patterns, explicit choice rules) that bound how cheap culprit selection can be.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Correction propagation comparison](../../../../agentic-systems/comparisons/memory/correction-propagation.md) -- a valid axis, wired versus host-led repair of dependents, but the Glimpse ingest's coverage already serves it. The memo adds reasoned retraction, which bears on reinstatement, not propagation. A reader reaches it through the Glimpse link.
- [Eigenius review](../../../../agentic-systems/reviews/eigenius.md) -- its justification certificates gate admission at commit. There is no non-monotonic withdrawal, so "justification" is a keyword match only.
- [Toulmin Argument ingest](../../../../sources/purdue-owl-toulmin-argument.ingest.md) -- the theory note on Toulmin sections carries the comparison at the level a Commonplace reader needs; the pedagogical source adds nothing on challengeable warrants.
- [Principles of Metareasoning ingest](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) -- Section 8 treats revision choice as a control problem, but Doyle values no computation. The axis would be speculative.
- [Agentic Note-Taking 23: Notes Without Reasons ingest](../../../../sources/agentic-note-taking-23-notes-without-reasons-202689418851669643.ingest.md) -- "reasons" there means propositional link semantics versus embedding adjacency, not recorded justifications that determine belief status.
- [BDI survey ingest](../../../../sources/bdi-agent-architectures-a-survey.ingest.md) -- same occasion, but the Bratman edge already carries the intention-revision contrast. The ingest does not develop Section 8's choice between rejecting an observation and rejecting a prior belief far enough to need BDI failure recovery.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) and [Source changes should surface downstream review targets](../../../../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -- the snapshot report proposed both. The ingest mentions the Section 9 change-signal only as evidence about who initiates reconsideration, not as staleness detection. Linking them would pull the reader off the occasion.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) -- reasoned retraction (Extractable Value item 6) resembles reversible supersession. The note is a requirements list without a reinstatement mechanism, and the ingest already links the superseded-choices note.
- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) -- the reflective-system definition link already covers Section 6's partial reflectivity. A second reflection link adds no distinct reader gain.
- [Tentative theory](../../../../theory/definitions/tentative-theory.md) -- in/out is support status, not Popperian tentativeness. Linking it would invite the conflation the ingest's Limitations section warns against.
- [Repair dispositions for defeated claims](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- only `see-also` is authorised, and the proposal concerns idealization pricing, not retraction mechanics.

## Index Membership

None. Sources sit outside tag participation. The ingest already carries `tags: [learning-theory, reflection]`, and both fit: Section 6's reified argument steps are analysed substantively as a partial reflective system.

## Synthesis Opportunities

The memo ingest, the [AGM ingest](../../../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md), the [base contraction ingest](../../../../sources/in-defense-of-base-contraction.ingest.md) and the [reflective equilibrium ingest](../../../../sources/making-reflective-equilibrium-precise.ingest.md) jointly imply a claim that no theory note states. Revision frameworks specify *what can be withdrawn*, but leave *which withdrawal to choose* as an exogenous policy: Doyle's pragmatic choice rules, AGM's selection function, Hansson's base ordering, reflective equilibrium's fixed weights. Doyle adds a cost: widening what can be criticized multiplies candidate withdrawals and makes blind selection useless. The [three-obligations note](../../../../theory/a-claim-without-external-assessment-carries-three-obligations.md) gestures at the separation but not at the cost. This is a candidate for the learning-method-name workshop's condition 3, before any theory note.

## Maintenance Observations

- `kb/reports/state/connect/sources/doyle-1979-truth-maintenance-system-aim-521.connect.md` was written against the snapshot before this ingest existed. It is now superseded by this report and may confuse a later reader looking for the memo's connect state. The Glimpse ingest similarly has two reports (`.connect.md` and `.ingest.connect.md`).
- The Glimpse ingest (line 60) asserts that premises and rules "are never revised" in a way the memo ingest explicitly corrects for Doyle's design. Until the Glimpse ingest links the memo, the two tracked ingests disagree without a pointer between them.
- The Bratman, BDI, Zollo–Winter and both Doyle ingests are untracked in the working tree. Edges among them assume they will be committed together.

## Flags

- Tension: the memo's monotonically growing argument store (Extractable Value item 3) conflicts with [Evolving understanding needs holistic rewrite, not composition](../../../../theory/evolving-understanding-needs-holistic-rewrite-not-composition.md), which favours reconciled rewrites over appended logs for whole-picture consumers. The two may serve different consumers: Doyle derives the current belief set mechanically from the store, while the holistic-rewrite note concerns an LLM reconciling prose. The tension is left unresolved here, but any experiment on Item 3 should name which consumer it serves.
- Split candidate check: the ingest spans belief-revision mechanics, explanation summarization, dialectical criticism and control/reflection, across more than five targets. It is held together by one occasion (condition 3), and Extractable Value already separates the threads, so no split is recommended.
- OCR caveat: the Backtracking and Toulmin edges lean on Section 6 and Section 8 constructions whose notation is partly garbled. Confirm the wording against the page images before quoting.
