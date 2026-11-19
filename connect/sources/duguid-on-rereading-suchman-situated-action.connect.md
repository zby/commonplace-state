---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/duguid-on-rereading-suchman-situated-action.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: On rereading. Suchman and Situated Action

**Source:** [On rereading. Suchman and Situated Action](../../../../sources/.snapshots/duguid-on-rereading-suchman-situated-action.md)

The source is an immutable snapshot. No tracked ingest exists yet; the authored surface for every candidate below is the future `kb/sources/duguid-on-rereading-suchman-situated-action.ingest.md`. The sources contract forbids durable links to `.snapshots/`, so reverse edges must target that ingest once it exists.

Source claims used for judging candidates:
1. Suchman did not offer situated action as an alternative to planning. Plans are "discursive tools" that need interpretation through situated action, one resource among many, not a preordained controller of action (pp. 4-5).
2. Moore's Law lets principled objections (the task is misconceived) pass as practical ones (not enough compute yet), and the two are hard to tell apart in advance (p. 4).
3. Under demand for conformity, workers "routinize": they make the world appear to follow the plan. This conceals the plan's inadequacy and the insight gained by improvising (Orr's Xerox technicians, p. 6).
4. Instruction regress: more detailed instructions overwhelmed users; a second instruction set to explain the first was proposed (p. 4).
5. Heideggerian lineage via Dreyfus and Winograd & Flores: "implicit assumptions cannot all be made explicit"; practical understanding precedes theoretical; breakdown and repair surface unseen assumptions (p. 7).
6. Design and use resemble writing and reading: designers, like authors, cannot control the uses their artifacts are put to (p. 8).

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels per destination: theory {is-evidence-for, abstracted-from, rests-on, compares-with, defined-in (theory/definitions), see-also}; sources {compares-with, see-also}; agentic-systems {compares-with, see-also}; reference {see-also}; external {derived-from, see-also}. External prospecting skipped (no open-web search); the external `source` URL is already in the snapshot frontmatter and will be the ingest's `derived-from` target, which the ingest skill handles.

**Context:** sibling ingests read in full: [Dittrich's rereading of Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) and the Connections/Extractable sections of [Haynes 2009](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md). Both were ingested for the operationalization workshop (HEAD commit 6e721073d); the workshop itself is not a link target.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles), filtered with `rg -i 'plan|situat|instruction|method|tacit|explicit|underspecif|interpret|compute|scale|bitter|principl|practical|breakdown|repair|routin|deviat|improvis|conform|workaround|taylor|codif|operationali|executor|cannot all|reader|author'`. Flagged: two-layer execution system, goal-holding interpreter workarounds, agentic systems interpret underspecified instructions, fix-what-the-executor-can't-determine, methodology enforcement is constraining, Naur note, three bitter-lesson notes, actionable methodology, writing styles manage underspecification.

**Description listing:** `rg -m1 '^description:'` on the 13 shortlisted files; kept or rejected as below.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` read; `complete: true`, so the by-tag rg was skipped. Its defining note is actionable methodology; its "Control and transfer" section lists the two-layer note and enforcement note. The source fits the tag's inclusion condition ("where that guidance ends"); Dittrich and Haynes ingests already carry it.

**Body search** (scope: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources`):
- `rg -l -i 'Suchman|situated action'` -- only actionable-methodology (uses "situated actionability", not Suchman) and the Dittrich ingest.
- `rg -l -i "Moore.s Law|more compute|scaling will"` -- bitter-lesson-selects-against-unearned-reach, wikipedia-bitter-lesson ingest, Sutskever's-list chapters, two other ingests. Kept the bitter-lesson notes; Sutskever chapters are narrative, rejected.
- `rg -l -i 'Heidegger|Dreyfus|Winograd'` -- only Sutskever's-list references. No KB treatment of this lineage.
- `rg -l -i 'tacit|cannot all be made explicit|Polanyi'` -- 15+ hits; most relevant: Argyris ingest, two-layer note, operationalism-sep ingest. Naur note found by title instead.
- `rg -l -i '\bOrr\b|workaround|surreptitious'` -- goal-holding interpreter, final-task-success, Norman ingest, specification-strategy note; others are keyword-only (memory requirements, monkey-patch, Borretti).
- `rg -l -i 'Taylor|scientific management'` -- no hits.
- `rg -l -i 'resource for action|plans as resources|plans are resources'` -- only the Dittrich ingest (in its Limitations, saying the post cannot establish this).
- `rg -l -i 'principled (objection|limit|problem)'` -- no hits.
- `rg -l -i 'plan-and-execute|replann|plan as (a )?resource' kb/agentic-systems kb/reference` -- swarmworld review archive only; keyword-level, rejected.
- `rg -n -i 'workaround|conceal|hidden|silent|invisible'` in goal-holding and final-task-success notes; `rg -n -i 'hidden compensation|compensat'` in Norman ingest; `rg -n -i 'espoused|theor(y|ies)-in-use|self-sealing|ritual compliance|withhold'` in Argyris ingest; `rg -n -i 'compute|scale|moore'` in the unearned-reach note -- passages read to confirm the axes below.

**Link following:**
- Goal-holding interpreter -> final-task-success -> silent disambiguation: a cluster on repairs that hide failure. Orr's routinization is the human-organizational version and adds a cause the cluster lacks (a demand for conformity motivates the concealment).
- Norman ingest -> final-task-success and LLM-generation-relaxes-goals: same hidden-compensation axis.
- Unearned-reach note -> codification-and-relaxing-navigate-the-bitter-lesson-boundary: the "not identifiable until scale tests it" claim is the closest match to Duguid's principled-vs-practical point.
- Naur note -> programming-as-theory-building ingest: Naur's inexpressible theory is the KB's nearest relative of the Heideggerian "implicit assumptions cannot all be made explicit".

## Connections Found

All edges are for the future Duguid ingest.

- [Dittrich's rereading of Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) -- **compares-with**: both are secondary readings of *Plans and Situated Actions* on the axis of what the book claims about plans. Dittrich gives the edition and page anchor but, by its own Limitations, cannot establish "plans as resources for action"; Duguid states that claim directly and rejects the Simon/Vera "alternative to planning" reading. Together they still stand in for the uncaptured book.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- **is-evidence-for**: Suchman as relayed here treats departure from the plan as normal operation, which agrees with the note's "fallback is an expected operation". Orr's case qualifies the note's learning step: "recurrence is the learning signal" needs fallback to be visible, and surreptitious routinization under conformity pressure hides both the plan's gaps and the improvised handling that should be promoted.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- **is-evidence-for**: Orr's technicians are a human instance of goal-holding executors absorbing an inadequate procedure through unrecorded workarounds while the visible record shows the procedure followed. Duguid names the two losses the note predicts: the plan's inadequacy is concealed, and the repair insight is never harvested.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **compares-with**: shared axis is whether a limitation can be identified as compute-curable before scale tests it. Duguid's "running out of computing power" vs "driving down a dead end" is the same identification problem from the critic's side; the note holds it is not identifiable until scale tests it, while Duguid (2012) asserts that NLP failures were principled. LLM progress since then partly tests his example, so this comparison should record the tension rather than resolve it.
- [The bitter lesson selects against unearned reach, not against structure](../../../../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **compares-with**: axis is what scale defeats. The note says scale replaces claims whose reach was asserted rather than earned; Duguid says scale cannot rescue a misconceived task. Both reject "more compute settles it" as a blanket answer, from opposite directions.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **compares-with**: axis is where the gap between a written plan and action comes from. The note places it in semantic underspecification of the instruction; Suchman/Duguid place it in the changing material and social context, which more specification cannot remove ("pre-ordained plans are rigid but context ever changing"). Duguid's photocopier instruction regress (a second instruction set to explain the first) is a vivid case of specification failing to close that gap.
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- **compares-with**: axis is whether "practical understanding cannot be fully made explicit" implies human-only competence. Duguid relays the Winograd & Flores premises ("implicit assumptions cannot all be made explicit") and the Suchman claim that humans and machines are not reducible to one another; the note argues such a conclusion needs an extra premise linking unformulated judgment to computational inability. Same missing bridge, different tradition.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **defined-in**: the ingest will need the KB term for a method's use being relative to operator, operations, target and setting; "plans as one resource among many, interpreted in context" is the critique-side statement of that relativity.
- [Ingest: Argyris, Organizational learning and MIS](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) -- **compares-with**: axis is how control pressure corrupts the evidence of how work is done. Argyris: tighter control induces withholding and ritual compliance; Duguid/Orr: demand for conformity induces surreptitious routinization that conceals plan inadequacy. Argyris supplies the organizational-learning mechanism; Duguid supplies the field case lineage (Orr, Suchman).
- [Ingest: Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**: axis is hidden compensation. Norman's autopilot compensates silently for a fault; Orr's technicians compensate silently for inadequate instructions. Also shares the 1980s HCI frame of what a machine partner lacks relative to a human one. Dittrich's ingest already uses Norman as its peer; a three-way comparison is available.

## Bidirectional Candidates

- [Dittrich's rereading of Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) <-> source -- **compares-with**: the Dittrich ingest's Limitations explicitly say it cannot establish Suchman's plans-as-resources claim; a return link to the Duguid ingest tells a reader where that claim is stated. Authorised (sources -> sources).

## Reverse-edge Candidates

Targets are the future Duguid ingest, not the snapshot. Labels are from `kb/theory/COLLECTION.md` (`evidenced-by` permits sources).

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -> Duguid ingest -- **evidenced-by** (qualifies, not corroborates): the recurrence-driven promotion step depends on fallback being visible; Orr/Duguid show an organizational condition (conformity demand) under which it is not.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -> Duguid ingest -- **evidenced-by** (qualifies): a human-executor analogue of workarounds consuming the failure event; transfer is analogy until the mechanism is shown shared, per [borrowed patterns transfer only over shared mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- already reached through the goal-holding and Dittrich edges; Duguid does not discuss repair of ambiguous input (that is Dittrich's Wilf/Adam point).
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) -- the Orr case fits, but Norman is already its anchor case and the goal-holding note carries the workaround mechanism; a third hidden-success link adds little.
- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) -- Duguid does not discuss activation or response enforcement; Haynes is the right source for this note.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- related in spirit (leave choices to situated execution) but Duguid gives no decision rule; keyword-level fit.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- the design-as-writing/reading point concerns authors' loss of control over readings, not style choice.
- [Haynes 2009 surgical checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) -- a plan-vs-execution comparison is possible, but Duguid discusses no checklist or adherence data; the shared workshop occasion makes the link tempting rather than informative.
- [Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md) -- "operations fix a concept only partially" is a different topic (concept meaning), keyword match on partiality.
- [Wikipedia: The Bitter Lesson](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- the theory notes above carry the comparison with more precision; linking the encyclopedia capture adds nothing.
- `kb/sources/sutskevers-list/` chapters -- Moore's-law/scaling narrative only.
- `kb/agentic-systems/reviews-archive/swarmworld.md` -- keyword hit on planning; no situated-action content.
- No reference or agent-memory-systems candidates: Duguid describes no Commonplace mechanism or memory system.

## Index Membership

- [method-guided-action tag](../../../../tags/method-guided-action-README.md) -- the future ingest qualifies for `tags: [method-guided-action]`: it substantively explains where a plan's guidance ends and why plans need situated interpretation. Sources are outside the tag's participating collections, so this is a source-scoped search tag only, not a head entry.

## Synthesis Opportunities

Duguid/Orr routinization, Argyris ritual compliance, Norman's silent autopilot compensation, and the KB's goal-holding-workaround and final-task-success notes together suggest a claim the KB does not yet state: when an executor is held to apparent conformity with a fixed procedure, its adaptive repairs become invisible, and the procedure stops receiving the failure signals it needs to improve. The KB states the LLM-runtime mechanism (fail-soft workarounds) but not the control-pressure cause. The Orr case is reported here secondhand; any note needs Orr (1996) or Argyris quotes retained first.

## Maintenance Observations

- No tracked ingest exists for this snapshot. Every connection here is blocked until `cp-skill-ingest` produces `kb/sources/duguid-on-rereading-suchman-situated-action.ingest.md`.
- The KB has no artifact on the Heidegger/Dreyfus/Winograd-Flores critique of AI, despite the Naur note treating a closely related premise. If the operationalization workshop needs that lineage, Winograd & Flores (1986) is the primary source Duguid points to.

## Flags

- Tension: Duguid's 2012 claim that NLP failures are principled rather than compute-limited is partly tested by later LLM progress. The ingest should date the claim and keep the principled-vs-practical distinction separate from his NLP example.
- Duguid is still a secondary reading of Suchman. It supplies the plans-as-resources claim that Dittrich lacks, but claims attributed to Suchman herself still need the book.
