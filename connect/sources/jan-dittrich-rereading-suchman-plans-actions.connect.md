---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/jan-dittrich-rereading-suchman-plans-actions.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Re-re-reading Lucy Suchman's Plans and Situated actions

**Source:** [Re-re-reading Lucy Suchman's Plans and Situated actions](../../../../sources/.snapshots/jan-dittrich-rereading-suchman-plans-actions.md)

The source is an immutable snapshot. Every outbound candidate below is a recommendation for the matching ingest, `kb/sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md`. That file did not exist when this report was written. Per the sources contract, durable links point to that ingest, never to the snapshot.

Source reading: a 2023 personal blog reflection (Jan Dittrich), secondary to Suchman. It makes five usable points.

1. Written prescriptions ("ways to do something") diverge from practice. Practitioners use design methods opportunistically, if at all.
2. Methods may serve partly to claim rationality to peers, not only to improve outcomes.
3. Suchman's situated action: "every course of action depends in essential ways on its material and social circumstances" (p70), against plans-in-cognitive-science as to-be-executed actions.
4. The photocopier analysis showed one-sided interaction: the machine tracks the user "through a very small keyhole".
5. Later notes (Wilf 2023; Adam, *Artificial Knowing*) describe an "interpretative asymmetry": humans repair machine output, machines do not repair human input.

The essay's own stance is distance from Suchman's plan concept and her language-centred method. It offers no new empirical evidence.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` "Outbound links". The authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and sources, plus external. `kb/work/` and `kb/instructions/` are excluded. The labels are `derived-from` (external); `is-evidence-for` (theory, agent-memory-systems); `abstracted-from`, `rests-on` (theory); `compares-with` (theory, sources, agent-memory-systems, agentic-systems); `defined-in` (theory/definitions); and `see-also` (most destinations, sparingly). External prospecting was skipped. The only known external target is the source URL itself, which belongs in the ingest as `derived-from`.

**Existing Suchman coverage:**
- `rg -il 'suchman|situated action' kb/ --glob '*.md'` (excluding snapshots) found `kb/theory/definitions/actionable-methodology.md` (the phrase "situated actionability" only, no Suchman citation) and `kb/work/operationalization-executability-automation/{exploration,README}.md`. The workshop lists Suchman (1987) as "the highest-value missing source", blocked on OCR. It warns not to substitute another edition silently. No ingest of Suchman or Dittrich exists in `kb/sources/`.
- `rg -l -i 'agre\b|ethnomethodolog|garfinkel|jean lave|akrich|woolgar|conversation analysis|interpretive asymmetry|keyhole' kb` found only an unrelated agentic-system analysis file. None of the authors Dittrich cites is ingested.

**Curated heads:**
- `kb/tags/method-guided-action-README.md` is `complete: true`, so the by-tag rg was skipped. Its members gave the main theory candidates: two-layer execution, actionable methodology, methodological/computational closure, fix-what-the-executor-can't-determine and specification strategy.
- `kb/tags/observability-README.md` (via body search) links silent disambiguation as "the runtime repaired it locally". That is the repair angle.

**Title listing:** `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles), filtered with `rg -i 'plan|method|procedur|instruct|spec|interpret|executor|underspec|situat|tacit|practice|legitim|ritual|follow|ground|disambig|human-llm|human'`. Flagged:
- agentic-systems-interpret-underspecified-instructions
- theory-and-methodology-form-a-two-layer-execution-system
- naur-equates-machine-execution-with-formulated-criteria
- fix-what-the-executor-cant-determine-not-what-it-will
- methodological-and-computational-closure-track-different-changes
- silent-disambiguation-is-the-semantic-analogue-of-tool-fallback
- specification-strategy-should-follow-where-understanding-lives
- skills-derive-from-methodology
- a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget
- traditional-software-can-bracket-executor-conformance-llm-systems

**Description reads:** I read the descriptions of all flagged notes plus `norman-problem-of-automation-inappropriate-feedback.ingest`, `cmmn-1-1-specification.ingest` and `operationalism-sep.ingest`. I also read the bodies of two-layer execution, Naur, interpret-underspecified-instructions and actionable-methodology, and the Norman ingest's summary and implications.

**Body search:**
- `rg -n -i 'plans? (are|as|vs|versus)|plan execution|execut\w+ (a|the) plan|situated|tacit|practice diverges|follow(ed)? (the )?method|opportunistic|claim(s|ing)? (of )?rationality|ritual|cargo|procedur\w+ (are|is) (not )?followed|repair' kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags`. Hits were mostly "repair" in unrelated senses (review repair, claim repair). Kept: specification-strategy ("silently repairing the plan in code") and the observability head's silent-disambiguation line. Rejected: ai-agent-book's "situated loop" heading (word coincidence).
- `rg -l -i 'legitimac|performativ|theat(re|er)|signal(ling)? rigou?r|appear(ance)? of rigou?r|ceremon' kb/theory kb/reference kb/agentic-systems`. Found no note on methods as legitimacy display. The "claim rationality" point has no landing site.
- `rg -n -i 'opportunistic|do not follow|don.t follow|deviat\w+ from (the )?(method|procedure|plan)' kb/theory kb/agentic-systems kb/sources/*.ingest.md`. Only statistical "opportunistic sampling" uses. None is about method use.

**Link following:**
- Norman ingest → Ironies of Automation and final-task-success-does-not-establish-intended-path-health. These confirm a "hidden compensation / silent repair" cluster that the interpretive-asymmetry point bears on.
- Workshop exploration → CMMN, operationalism and Naur ingests (the workshop's source table). These are candidate peer sources.

**Reference, agent-memory-systems, agentic-systems:** I scanned these within the body searches above. No candidate passed the articulation test. The source makes no claim about Commonplace mechanisms, memory systems or a specific agent runtime.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **compares-with**: both explain why written instructions do not determine the action taken. Suchman, via Dittrich, puts the gap in the material and social circumstances of action. The note puts it in the semantic underspecification of natural-language specs. A reader gains a second, older account of the same gap that does not depend on the spec language.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- **compares-with**: the shared axis is whether departing from a prescribed method is failure or expected operation. Dittrich reports that practitioners use methods opportunistically and know prescriptions diverge from practice. The note treats fallback outside coverage as normal. The source adds one thing the note lacks: methods may be kept for social legitimacy ("claim rationality"), not coverage.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **compares-with**: Dittrich's critique targets "the assumption that there are right ways of doing something outside of a particular situation and value context". The definition makes actionability relative to operator, operations, target and setting. The shared axis is the setting-relativity of prescriptions. Use `compares-with`, not `defined-in`, because the source does not use or need the term.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: the shared axis is who repairs an interaction breakdown and whether the repair is visible. The "interpretative asymmetry" in Dittrich's notes (citing Wilf and Adam) says humans repair machine output and machines do not repair human input. LLM agents now repair underspecified human input themselves, and the note's problem is that this repair is silent. The source supplies the HCI baseline that the note's situation inverts.
- [Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**: these are near-contemporary 1980s critiques of the same deficit. Suchman's photocopier tracks the user "through a very small keyhole" and cannot repair. Norman's autopilot cannot give the continual feedback a human co-worker would. The shared axis is what interactional resources a machine lacks relative to a human partner. Suchman's version is about interpreting the user. Norman's is about reporting one's own state.

## Bidirectional Candidates

- [Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) <-> source -- **compares-with**: a sources-to-sources comparison is useful from both ends. A reader of Norman's feedback argument benefits from the asymmetric-repair framing of the same period. Author it only after the Dittrich ingest exists.

## Reverse-edge Candidates

- [Operationalization workshop exploration](../../../../work/operationalization-executability-automation/exploration.md) → source -- **evidenced-by** (work contract, loose): the workshop's source table marks Suchman as blocked. This blog supplies a short, citable paraphrase and one page-cited quote (p70) of Suchman's situated-action claim. The workshop may record it as a secondary pointer only. It must not stand in for the primary source, which matches the workshop's own "do not substitute silently" rule.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source ingest -- **evidenced-by** (theory contract): only as qualifying context for the interpretive-asymmetry baseline, and the context phrase must say it is not corroboration. The source reports no test the note could have failed. A primary Suchman, Wilf or Adam ingest would be the better target.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- rejected because the source gives no rule for what a prescription should fix. It only observes that prescriptions diverge from practice.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- rejected because the source does not distinguish what a method settles from who executes the residue. The overlap is topical only.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- rejected because its "silently repairing the plan" line is a keyword match. The source says nothing about choosing a specification strategy by phase.
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) and [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) -- rejected for now. Naur (theory not expressible as rules) and Suchman (plans do not determine action) are a real pairing. But this blog does not argue the rules-versus-competence point, so the comparison would rest on Suchman's book, not this source. Revisit with a primary Suchman ingest.
- [CMMN 1.1](../../../../sources/cmmn-1-1-specification.ingest.md) -- rejected. CMMN's discretionary items and run-time planning are arguably an engineering answer to the situated-action critique, but the source never discusses plan formalisms. The link would be the connector's analogy, not the source's content.
- [Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md) -- rejected. Partial fixing of concepts by operations is a different question from plans versus situated action.
- [Ironies of Automation](../../../../sources/ironies-of-automation.ingest.md) -- rejected as redundant with the Norman comparison, which already links to it.
- [AI Agent Book review](../../../../agentic-systems/reviews/ai-agent-book.md) -- rejected. Its "situated loop" heading is a word coincidence about harness responsibilities.
- [A goal-holding interpreter fails soft](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- rejected. Its mechanism (goal-holding re-routing) is not in the source.

## Index Membership

- [method-guided-action](../../../../tags/method-guided-action-README.md) -- the ingest could carry `tags: [method-guided-action]` for source-scoped search, following the CMMN ingest's use. The condition requires substantive treatment of "where that guidance ends". The source does address this at the level of practitioners' opportunistic method use and situated action. It is thin and secondary, so the ingest writer should confirm the analysis treats it substantively. Source tags do not affect the complete head's member listing.

## Synthesis Opportunities

- **Inverted interpretive asymmetry.** Three artifacts together suggest a claim no note states. They are this source (pre-LLM machines do not repair human input; humans do the repair), [silent disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) (agents repair underspecified specs invisibly) and [Norman](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) (silent compensation hides a growing fault). The candidate claim: LLM agents reverse the classic HCI repair asymmetry. Once the machine repairs the human's input, the design problem moves from the machine's narrow keyhole to making its repairs visible. This needs primary grounding (Suchman, Wilf or Adam), not this blog, before it is written as a note.

## Maintenance Observations

- The operationalization workshop's highest-value missing source (Suchman 1987) is still unretained. This secondary blog does not close that gap. A primary capture (OCR of the archived scan, or a user-supplied text) remains the blocking follow-up.
- The KB has no landing site for the "methods kept for legitimacy or display of rationality" mechanism. It is a possible gap for method-guided action, but one blog mention is below the quality bar. Leave it to the log if it recurs.

## Flags

- Evidential weight: the source is a personal reflective blog. Prefer `compares-with` for all outbound edges. Do not use `is-evidence-for` against theory claims unless a primary Suchman or Adam ingest is added.
- The ingest does not exist yet. All Connections Found target the future `jan-dittrich-rereading-suchman-plans-actions.ingest.md`.
