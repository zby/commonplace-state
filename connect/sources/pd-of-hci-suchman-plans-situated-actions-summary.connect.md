---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/pd-of-hci-suchman-plans-situated-actions-summary.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: PD of HCI - Plans and Situated Actions (summary of Suchman)

**Source:** [PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/.snapshots/pd-of-hci-suchman-plans-situated-actions-summary.md)

The source is an immutable snapshot (a 1997 student-written course-page summary of Suchman 1987, not Suchman's text). No tracked `.ingest.md` exists for it yet (`kb/sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md` is absent). Every outbound candidate below is a recommendation for that future ingest report, which is the authored surface under `kb/sources/COLLECTION.md`. Labels are restricted to the sources-collection table: theory -> `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; theory/definitions -> `defined-in`; sources -> `compares-with`, `see-also`.

What this summary carries beyond the existing Dittrich ingest: the 1987 argument structure (planning-model critique; intentions as uncompleted plan parts; background assumptions generated during interaction; indexicality and per-occasion mutual intelligibility; conversation-analytic resources), the breakdown typology (conditional relevance, false alarm, garden path), the three design problems for interactive machines, the differential-modelling remedy, and the conclusion "engineer alternatives to the situated properties of interaction" rather than simulate human communication.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md` outbound section: destinations theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded `kb/work/` and `kb/instructions/`; `external` authorised only for `derived-from`/`see-also` (no external targets supplied, so external prospecting skipped).
- `kb/types/connect-report.md`.
- Sibling ingest `kb/sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md` read fully; its Connections Found section was followed one hop (agentic-systems-interpret-underspecified-instructions, two-layer execution, actionable-methodology, silent-disambiguation, Norman ingest).

**Description / title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` filtered by `instruction|underspec|interpret|methodolog|plan|context|human|situat|execut|operational|silent|disambig|ambigu|repair|clarif|codif|tacit|user|dialog|convers|agent` -- flagged human-analogies-suggest-functions-not-component-boundaries, specification-strategy-should-follow-where-understanding-lives, naur-equates-machine-execution-with-formulated-criteria, fix-what-the-executor-cant-determine-not-what-it-will, underspecification-and-indeterminism-complicate-programming-for, traditional-software-can-bracket-executor-conformance-llm-systems, human-llm-differences-are-load-bearing-for-knowledge-system-design.
- `rg -m1 '^description:'` on each flagged theory note to judge fit (results in Connections / Rejected below).

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (the Dittrich ingest's tag; `complete: true`, so by-tag rg skipped). Its defining note is actionable-methodology and its "where guidance ends" scope matches Suchman's plans-as-resources claim, so a future ingest may carry `tags: [method-guided-action]`.

**Body search** (scope `kb/theory kb/sources kb/tags kb/reference kb/agentic-systems`, `-l -i`):
- `suchman` -- only the Dittrich ingest.
- `situated action|situatedness` -- actionable-methodology definition, Dittrich ingest.
- `situated` -- adds information-value-is-observer-relative, use-tests-a-decomposition..., design-rationale..., several unrelated sources; keyword-only, rejected.
- `indexical` -- only gibson-1998 linguistic-locality ingest (psycholinguistic sense; rejected).
- `garden path` -- no hits; `false alarm` -- calibration proposal, hidden-failures ingests, geometry-of-forgetting (detector-error sense, not interactional breakdown; rejected).
- `plans? (are|as) (a )?resources?` -- Dittrich ingest only.
- `mutual intelligibility|common ground` -- no hits.
- `background (assumptions|knowledge)` -- human-llm-differences, theory-builder definition, several sources; human-llm-differences evaluated and rejected (see below).
- `user model` -- no hits.
- `tutoring|intelligent tutor` -- skill-acquisition-compilation, knowledge-refinement sources (ITS/ML lineage, no situated-action content; rejected). `ELIZA` -- only sutskevers-list chapters (rejected).
- `ethnomethodolog` -- Dittrich only.
- `written instructions?|instructions are generic` -- a-methodology-governs-its-own-extension..., underspecification-and-indeterminism..., Dittrich.
- `after the fact|retrospective(ly)? (account|rational)` -- Argyris, why-llms-cant-make-your-code-simpler, others; no claim about plans as post-hoc accounts of action.
- `interpretive asymmetry|repair asymmetry` -- Dittrich only.
- `ls kb/sources | grep -i -E 'duguid|norman|suchman|dittrich|haynes|checklist'` -- Dittrich ingest, Norman ingest, Haynes checklist ingest; Duguid exists only as a snapshot.

**Link following:**
- Read human-analogies-suggest-functions-not-component-boundaries (full) -- strong match to Suchman's conclusion about not simulating human communication.
- Read first section of naur-equates-machine-execution-with-formulated-criteria -- shares the "rule following is not exhausted by formulated rules" theme.
- `rg -i 'clarif|ask|repair|human'` in silent-disambiguation -- confirms "agent repairing a contract gap" framing; one hop to final-task-success-does-not-establish-intended-path-health (rejected as already reached through silent-disambiguation).
- `rg -i 'situat|circumstanc|setting'` in actionable-methodology -- setting-relativity confirmed (line 11, 26).
- Checked `kb/theory/COLLECTION.md` outbound table for reverse-edge labels toward sources (`evidenced-by`, `abstracted-from`, `see-also`).

## Connections Found

All are candidates for the future `pd-of-hci-suchman-plans-situated-actions-summary.ingest.md`.

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: axis = who detects and repairs an interactional breakdown, and whether the repair is visible. Suchman's copier could detect neither the "false alarm" nor the "garden path" (user error the user does not notice); LLM agents now repair underspecified input but silently. The breakdown typology is detail the Dittrich ingest lacks.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **compares-with**: axis = locus of the instruction-action gap. The note places it in semantic underspecification of the text; the summary places it in indexicality (meaning conditional on the situation of use, mutual intelligibility achieved per occasion), which more specification does not remove.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- **compares-with**: axis = which layer is default and when the other is invoked. Suchman's plans are representations consulted "only when otherwise transparent activity becomes in some way problematic", i.e. situated action is the default and the plan the fallback; the note runs the methodology fast path by default with theory as fallback.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- **is-evidence-for**: the summary's claim that background assumptions "are generated during the course of the interaction" rather than held prior to action bears on the note's "understanding discovered during execution" phase. Weak evidence: secondary summary, not tested.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- **is-evidence-for**: Suchman's conclusion that interaction design should "engineer alternatives to the situated properties of interaction" rather than simulate human communication, and gains more from understanding human/machine differences than from assuming similarity, is an early HCI instance of keeping the function while refusing the human form. Bears on the note; does not test it.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **compares-with**: axis = setting-relativity of guidance. The definition makes actionability relative to operator, operations, target and setting; Suchman denies that any plan determines action outside the particular situation. Same relativity, different strength. (Dittrich ingest already draws this edge; repeat only if the new ingest says something the Dittrich one does not, e.g. plans as event-driven resources rather than controlling structures.)
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- **compares-with**: axis = limits of formulated representation. Naur argues program theory is not exhausted by rules; the summary reports Suchman's claim that intentions are "diffuse and tacit" and that common knowledge does not fit any world model. Both critique the "formulated rules suffice" premise from different traditions (Ryle vs ethnomethodology).
- [Ingest: Re-re-reading Lucy Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) -- **compares-with**: axis = coverage and edition of two secondary readings of the same book. Dittrich reads the 2nd edition (page anchor p70, interpretive asymmetry, scripts/ordering-devices chapter); this summary reads the 1987 argument structure (planning model critique, indexicality, breakdown types, three design problems, differential modelling).
- [Norman's "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**: axis = interactional resources a machine lacks. Suchman's second design problem ("how to make clear to the user the limits on the machine's access to basic interactional resources") is close to Norman's missing continual feedback; both are late-1980s diagnoses of machine-side deficits.
- [Haynes et al. 2009 surgical safety checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) -- **compares-with**: axis = plan as resource versus controlling structure. A checklist read aloud at three junctures is a plan used as a coordinating resource at defined breakpoints, not a program that determines action. This pairing is the connect run's inference, not a claim either source makes.

## Bidirectional Candidates

- [Ingest: Re-re-reading Lucy Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) <-> source -- **compares-with**: the Dittrich ingest's Limitations section says it "cannot establish what Suchman argues about plans as resources for action, the role of plans after the fact"; this summary covers exactly those points, so a return link from the Dittrich ingest to the new ingest would tell a reader where the complementary coverage is.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md` labels (`evidenced-by`, `abstracted-from`, `see-also` toward sources), once the ingest exists:

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -> future ingest -- **evidenced-by** (qualifies/bounds, not corroboration): the false-alarm / garden-path typology gives the pre-LLM baseline in which the machine could not repair at all.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -> future ingest -- **evidenced-by** (qualifies): an HCI precedent for "engineer alternatives rather than simulate". Per theory "Origin is not corroboration", the context phrase must not claim corroboration.

## Off-authorisation Candidates

None

## Raw Text Candidates

- `kb/sources/.snapshots/duguid-on-rereading-suchman-situated-action.md` -- potential **compares-with** (third secondary reading of Suchman). It is a snapshot with no tracked ingest, and durable links into `.snapshots/` are forbidden; once its ingest exists, the three Suchman readings (Dittrich, Duguid, this summary) should cross-link on edition/coverage.

## Rejected Candidates

- [Underspecification and indeterminism complicate programming for prompts](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -- overlaps the agentic-systems-interpret-underspecified-instructions candidate without adding a distinct axis.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) -- reached one hop through silent-disambiguation; linking both would be redundant.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- plausible (leave bounded choices to execution), but the plans-as-resources point is better carried by the two-layer and specification-strategy candidates.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- concerns dual-audience documents; Suchman's human/machine differences are about interaction, not documents. Keyword match on "background knowledge".
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- relevant to how an ingest should transfer the copier analysis to LLMs, but generic; any source analogy would qualify.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- keyword-only "situated" match.
- [Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md) -- partial fixing of concepts by operations is a measurement-theory point, not situated action.
- Tutoring/ITS sources (skill-acquisition-compilation, recap-early-work-theory-knowledge-refinement) -- share WEST/ITS lineage only, no situated-action content.

## Index Membership

- [Method-guided action tag head](../../../../tags/method-guided-action-README.md) -- source-scoped `tags: [method-guided-action]` on the future ingest (as on the Dittrich ingest): Suchman's plans-as-resources claim is substantively about where method guidance ends. Source tags do not affect the head's `complete: true` membership.

## Synthesis Opportunities

- Repair-locus inversion: Suchman's copier (machine detects neither false alarm nor garden path), Norman's automation (machine does not report its state), and silent-disambiguation (LLM agent repairs but hides it) together suggest that the classic HCI design problem "make clear to the user the limits on the machine's access" has turned into "make visible the repairs the machine now performs". The Dittrich ingest already flags this as a deep-dive needing primary grounding; this summary adds the breakdown typology and the three design problems, but is still secondary.

## Maintenance Observations

- No tracked ingest exists for this snapshot or for the Duguid snapshot; `commonplace-validate kb/sources` should report both as snapshots without an ingest match.
- The snapshot's own metadata lists "Mikael Jakobsson (page maintainer; summary author not explicitly stated)" and a 1997 date; the original URL is an informatik.umu.se page mirrored at uni-koeln.de. A future ingest should record the mirror as the observation and keep the authorship uncertainty.

## Flags

- Source weight: a 1997 anonymous student summary of a book, reached via a mirror. All `is-evidence-for` candidates above are weak and should be phrased as "bears on", never as corroboration; any KB claim attributed to Suchman still needs the book.
- The operationalization workshop (`kb/work/operationalization-executability-automation/`) cites Suchman, but `kb/work/` is an excluded destination; the workshop's source table, not this report, is where the new ingest gets recorded.
