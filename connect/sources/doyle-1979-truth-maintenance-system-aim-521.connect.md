---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/doyle-1979-truth-maintenance-system-aim-521.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: A Truth Maintenance System (Doyle, MIT AI Memo 521, 1979)

**Source:** `kb/sources/.snapshots/doyle-1979-truth-maintenance-system-aim-521.md` (A Truth Maintenance System; not linked because the snapshot is Git-ignored and no paired ingest exists yet)

The source is an immutable snapshot (uncorrected OCR of the full memo). No tracked ingest exists for it yet; the name-paired authored surface would be `kb/sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md`. Every outbound candidate below is a recommendation for that future ingest. The short IJCAI-79 version already has an ingest ([Glimpse ingest](../../../../sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md)) with a full connection set. This report therefore concentrates on what the memo adds beyond the short paper:

- §1.1: rational thought as finding reasons for attitudes, including desires, intentions and actions, with attitudes having "no independent existence" apart from the reasons.
- §5: summarizing arguments into levels of detail through conditional-proof justifications.
- §6: dialectical argumentation, where argument steps become challengeable assumption nodes and the argument store is additive.
- §7: models of other agents' beliefs.
- §8: control encoded in patterns of assumptions, explicit choice rules for revision, and a sketched reflexive interpreter.
- §9: experience and extensions, including signalling the problem solver when a node's argument changes.
- §10: the "opinion revision system" remark, following Dennett.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md` outbound section. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` and `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). The snapshot is never the link author; the ingest is.
- `kb/types/connect-report.md`.
- Target memo read in full: §§1–4 in detail, §§5–10 read through the discussion. Garbled OCR in the justification formulas and the end table was noted.
- Known context: [Glimpse ingest](../../../../sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md), read fully. Its existing connections were treated as the baseline for the memo.

**Description / title listing scan:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (444 titles), then filtered with `rg -i 'retract|revis|belief|assum|backtrack|criticis|reason|justif|supersed|stale|lineage|depend|explan|summar|contradic|debat|dialect|argument|default|defeat|provisional|withdraw|warrant|support|tentative|blame|failure|level of detail|abstraction|control|choice|deliberat|intention|commit'`. Flagged:
  - "Explicit retention provides direct targets for selective revision": kept, for the §6 justification-as-node move.
  - "Revision guided by rationale needs faithfulness, not just legibility": kept, because §1.1 makes reasons operative.
  - "A knowledge base should support fluid resolution-switching": kept, for §5.
  - "Claim notes should use Toulmin-derived sections for structured argument": kept, for §6.
  - Glimpse-baseline notes kept: backtracking, failure explanation, cost-sensitive formalisms, superseded choices, make-like staleness, lineage.
  - "Source changes should surface downstream review targets…": kept, for the §9 change-signal.
  - "Lightweight search control allocates further search without licensing adoption": rejected, see below.
  - "Intent controls a local choice only when it distinguishes its live alternatives": rejected.
  - "Commitment, not derivation, creates new ground truth": rejected.
  - "Theory warrant should be tracked at the finest granularity evidence licenses": rejected.
  - "Reasoning production is not reasoning evaluation": rejected.
  - "Ad hoc explanation can be rational when error is cheap and local": rejected.
- Resolved paths with `rg -l -F -x '# <title>' kb/theory/` and read their descriptions.
- `ls kb/theory/definitions/`. Flagged `reflective-system.md`, for the §6 and §8 self-representation of justifications and control state, and `theory-builder.md`, already used by the Glimpse ingest.
- Source descriptions read with `rg -m1 '^description:'` on candidate ingests: Bratman–Israel–Pollack, BDI survey, ATMS, base contraction, reflective equilibrium, SEP practical reason, introspective multistrategy learning, Bacchus–van Run, Popper EWKS, RuleMem, RECV and the RE ontology.

**Topic indexes:**
- `kb/tags/` listing. Heads checked with `rg -m1 '^description:'` and inclusion lines: `learning-theory`, `reflection`, `kb-maintenance`, `claims-and-grounding`. `learning-theory` is the Glimpse ingest's tag. `reflection` fits §§6 and 8, where justifications and control state are represented as beliefs the problem solver reasons about. Source tags do not affect generated listings (sources `COLLECTION.md`).

**Body search:**
- `rg -l -i 'truth maintenance|\bTMS\b|ATMS|dependency-directed|nogood|non-monotonic|nonmonotonic|doyle' kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/reports/state/**'`. Hits:
  - Sources: Glimpse, ATMS, Bacchus–van Run.
  - [A claim without external assessment carries three obligations](../../../../theory/a-claim-without-external-assessment-carries-three-obligations.md): cites the ATMS and base contraction for separating dependency maintenance, warrant and selection policy. This is a reverse-edge candidate.
  - Agent-memory reviews that use "truth maintenance" informally as a contrast term: ace, AriGraph, eidetic, kgai, continuity, sage-wiki. The collection is frozen, so these were not pursued.
  - Keyword-only hits on "non-monotonic" in apex-mem, Morgan's specification statement and widening/narrowing. Rejected.
  - Excluded hits under `kb/work/`.
- `rg -l -i 'Quine|minimum mutilation|web of belief'` over theory, reference, agentic-systems, agent-memory-systems, tags and sources: no hits. The memo's §§6 and 10 Quinean framing of pragmatic belief revision has no KB anchor.
- `rg -l -i 'dialectic|debater'` returned the Popper EWKS and *Conjectures and Refutations* ingests and the reflective-equilibrium ingest. The other hits were ADRs and proposals using "dialectic" loosely; rejected.
- `rg -l -i 'Dennett'`: only the Sutskever list. No anchor for the opinion/belief distinction.
- `rg -l -i 'BDI|Bratman|belief.desire.intention'`: mostly the false match "subdirectory". Real hits were `sep-practical-reason.ingest.md` and the untracked Bratman and BDI ingests found by name.
- `rg -l -i 'levels? of detail'`: Gick–Holyoak, agentic code reasoning, PMI lexicon. Keyword-only; rejected.
- `rg -l -i 'justification graph|explicit reasons?|recorded reasons?'`: [design rationale management](../../../../reference/design-rationale-management.md), introspective multistrategy learning, RuleMem, RECV and agentic-system results. Introspective learning was kept. Design rationale management was weighed and rejected (see below).
- `rg -l -i 'belief revision|AGM'` returned many theory notes using "belief revision" loosely. Only "Commitment, not derivation…" was evaluated, and it was rejected.
- Focused reads:
  - `rg -n -i 'reconsider|truth maint|doyle|belief revision'` on the Bratman and BDI ingests confirmed the intention-reconsideration axis. Neither cites Doyle.
  - `rg -n -i 'blame|trace'` on introspective multistrategy learning confirmed trace-based blame assignment and planned repair.
  - `rg -n -i 'dependen|selective'` on base contraction confirmed the base-versus-consequences dependency argument.
  - Read the opening sections of the explicit-retention, rationale-faithfulness, resolution-switching, Toulmin and reflective-system notes.
  - Read lines 180–192 of the three-obligations note.
  - `rg -n -i 'sources' kb/theory/COLLECTION.md`: theory → sources is authorised via `evidenced-by`, `abstracted-from`, `derived-from` and `see-also`.
  - `kb/agent-memory-systems/COLLECTION.md` outbound section: sources are reachable via `derived-from`, `evidenced-by` and `see-also`. The collection is frozen per `AGENTS.md`.

**Link following:**
- From the Glimpse ingest, followed its theory and source links. The cluster is ATMS, base contraction, Bacchus–van Run, cost-sensitive formalisms, failure explanation, backtracking-provisional, make-like staleness, correction propagation, superseded choices, lineage and fixed decomposition. These are the baseline. Each was re-checked for memo-specific content; Bacchus–van Run and fixed decomposition add nothing beyond the Glimpse edge.
- From the three-obligations note, followed the ATMS and base-contraction pairing. A third citation of Doyle on the in/out-versus-truth separation fits there.
- From the explicit-retention note, followed its link to "Reflection buys addressability". It confirms that the addressability axis is the one the §6 move instantiates.

### Candidate origins

- kb/sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md — known, body-search
- kb/sources/an-assumption-based-tms.ingest.md — known, body-search, link-following
- kb/sources/in-defense-of-base-contraction.ingest.md — known, link-following
- kb/sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md — known, descriptions, body-search
- kb/sources/sep-practical-reason.ingest.md — body-search, descriptions
- kb/sources/introspective-multistrategy-learning.ingest.md — body-search, descriptions
- kb/sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md — body-search, descriptions
- kb/sources/making-reflective-equilibrium-precise.ingest.md — body-search, descriptions
- kb/theory/only-explicit-retention-is-durable-writable-and-addressable.md — titles, descriptions
- kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md — titles, descriptions
- kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md — titles, descriptions
- kb/theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md — titles, descriptions
- kb/theory/definitions/reflective-system.md — titles, curated-head
- kb/theory/cost-sensitive-formalisms-for-tentative-theory-search.md — known, titles
- kb/theory/failure-explanation-changes-later-branch-decisions.md — known, titles
- kb/theory/backtracking-keeps-lightweight-search-control-provisional.md — known, titles
- kb/theory/superseded-choices-are-retained-superseded-beliefs-are-not.md — known, titles
- kb/theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md — titles, descriptions
- kb/theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md — known, titles
- kb/agentic-systems/comparisons/memory/correction-propagation.md — known
- kb/theory/a-claim-without-external-assessment-carries-three-obligations.md — body-search

## Connections Found

All edges are recommendations for a future `doyle-1979-truth-maintenance-system-aim-521.ingest.md`.

**Sources**

- [Glimpse ingest](../../../../sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md) -- **compares-with**: the same mechanism in the condensed IJCAI-79 version. Compare on coverage. The memo adds §§1.1 and 5–10 and gives readable forms for the Step 2/3 justification formulas that the Glimpse capture garbles. The Glimpse ingest's Limitations section explicitly defers exact notation to "the full memo".
- [ATMS ingest](../../../../sources/an-assumption-based-tms.ingest.md) -- **compares-with**: compare on support representation, as in the Glimpse edge. The memo sharpens one point. §9 lists "multiple supporting-justifications whenever several well-founded arguments can be found" as a wanted extension, which is close to the ATMS's labelled environments, and names circularity and incrementality costs that motivated the ATMS.
- [Base contraction ingest](../../../../sources/in-defense-of-base-contraction.ingest.md) -- **compares-with**: compare on what the revisable representation is. In §6 the store of arguments only grows ("all changes to beliefs occur by adding new arguments to a monotonically growing store of arguments"), and the current belief set is derived from it. That is a base-versus-consequences design taken further than Hansson's belief bases: nothing is contracted, and a belief is defeated by an added challenge.
- [Bratman–Israel–Pollack ingest](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md) -- **compares-with**: compare on how intentions are revised. §§1.1 and 8 treat desires and intentions as reason-backed attitudes that the same TMS revises, so revision is event-driven by new reasons or contradictions. IRMA instead holds intentions stable and adds a cost-bearing filter override that decides when to reconsider. Both answer the occasion's question about who starts reconsideration.
- [SEP practical reason ingest](../../../../sources/sep-practical-reason.ingest.md) -- **compares-with**: compare on what practical reasoning is. §1.1 claims that "rational thought is the process of finding reasons for attitudes (belief, desire, intent, or action)". That is a reason-construction account with no weighing step, against the survey's deliberation as weighing reasons for and against options. In Doyle the weighing reappears only as §8's explicit choice rules.
- [Introspective multistrategy learning ingest](../../../../sources/introspective-multistrategy-learning.ingest.md) -- **compares-with**: compare on blame assignment from recorded reasoning. The TMS blames structurally through justifications. §8 proposes "revision plans" indexed by problem-solver state, each "a specialization of the general dependency-directed backtracking procedure". Meta-AQUA implements a similar move: matching a stored explanation to a reasoning trace and planning a repair sequence.
- [Popper EWKS ingest](../../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) -- **compares-with**: compare on criticism of objective arguments. §6 mechanizes dialectical criticism. Each argument step becomes an explicit assumption that any module can challenge, and arguments are never discarded. This makes criticism of stated argument content, rather than of the arguer, a data-structure operation. It also states the limit: which revision to choose is a separate, pragmatic question.
- [Reflective equilibrium ingest](../../../../sources/making-reflective-equilibrium-precise.ingest.md) -- **compares-with**: compare on choosing which commitments to give up. §6 cites Quine's view that any belief can be rejected at the cost of other changes, and asks for "pragmatic belief revision rules". §10 cites Rescher's "minimum mutilation" framework. The reflective-equilibrium model formalizes one such choice criterion; the TMS deliberately supplies none.

**Theory**

- [Explicit retention provides direct targets for selective revision](../../../../theory/only-explicit-retention-is-durable-writable-and-addressable.md) -- **is-evidence-for**: §6 is a clean mechanized case of the addressability point. Before justifications were reified as nodes, "we were powerless to do this [reject a belief by argument] … other than physically removing justifications". Making each argument step an explicit assumption node gives every step a direct revision target. The case supports the note's claim within a symbolic system and does not test natural-language artifacts.
- [Revision guided by rationale needs faithfulness, not just legibility](../../../../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) -- **is-evidence-for**: the memo bounds the note with a case where rationale is faithful by construction. In §1.1, "the only real component of thought is the current set of reasons — the attitudes … have no independent existence", so the belief state is computed from the justifications. The faithfulness gap the note warns about exists only where the rationale is separate from the operative basis. The memo shows that closing the gap means making the rationale the mechanism.
- [A knowledge base should support fluid resolution-switching](../../../../theory/a-knowledge-base-should-support-fluid-resolution-switching.md) -- **compares-with**: compare on multi-level explanation. In §5, CP-justification summaries hide low-level nodes so an explanation can be read at the level of totals, then states, then precincts; the election example illustrates this. Doyle adds a constraint the note lacks. Summarization needs to know the desired form in advance, and argument structure is cheapest when introduced at creation, through internal/external role nodes.
- [Claim notes should use Toulmin-derived sections for structured argument](../../../../theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md) -- **compares-with**: compare on making the warrant an explicit, challengeable object. §6 reifies each argument step (the inference from grounds to claim) as an assumption node with an explicit "is challenged" outlist entry. That is a mechanized rebuttal slot, where the Toulmin note proposes prose sections.
- [Reflective system](../../../../theory/definitions/reflective-system.md) -- **compares-with**: compare on what the self-representation covers. §6 makes the problem solver's own argument steps beliefs, which is causally connected because challenging one changes what is believed. §8 sketches a "reflexive interpreter" that represents its control state and plans among its beliefs. The §8 part is a proposal deferred to a thesis, so it is weaker evidence than §6.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: carried over from the Glimpse edge, with memo-specific additions. §4 says outright that the "current implementation picks the culprit and denial randomly … blind search is inadequate". §8 offers two remedies: control "canned" into justification patterns (defaults, ordered alternatives, equivalence-class representatives) and explicit choice rules computed on demand.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) -- **is-evidence-for**: the nogood shapes the second backtrack in the §4 room/time example. §6 adds that the additive argument store "guides future debates by keeping them from repeating past debates".
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) -- **is-evidence-for**: §8.2's "sequences of alternatives" and the PA/NSA/RO structure encode ordered provisional choices whose rejection advances to the next alternative. The §8.2 remark that the simple encoding "allows no direct way … to reconsider previously rejected alternatives" bounds how provisional a rejection stays.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md) -- **is-evidence-for**: the §6 dialectical TMS "never discards arguments". Challenged arguments stay as defeated records with operational standing, and the nogood persists by design, as in the Glimpse edge.
- [Source changes should surface downstream review targets](../../../../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -- **is-evidence-for**: among the extensions in §9 is "use of the TMS to signal the problem solver whenever the argument for some node changes". That is a mechanized change-surfacing signal driven by recorded dependencies, which is the push side of the note's lineage claim.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- **compares-with**: carried over from the Glimpse edge. Exact validity conditions on justifications decide whether a dependent still holds, while links and timestamps can only flag it. §9 adds that the TMS itself was built as an extension of Stallman and Sussman's "fact garbage collector".

**Agentic systems**

- [Correction propagation comparison](../../../../agentic-systems/comparisons/memory/correction-propagation.md) -- **compares-with**: carried over from the Glimpse edge. The memo adds nothing new on this axis, but the ingest should keep the edge if it replaces the Glimpse ingest as the primary Doyle citation.

## Bidirectional Candidates

- [Glimpse ingest](../../../../sources/doyle-1979-glimpse-of-truth-maintenance.ingest.md) <-> source -- **compares-with**: the Glimpse ingest's Limitations section says exact notation "need[s] the page images or the full memo". Once the memo ingest exists, a return link from the Glimpse ingest tells a reader where the fuller treatment lives. Its Recommended Next Action (the deliberative-learning workshop) could also cite §§1.1, 6 and 8 for the "who starts reconsideration" and "choosing what to believe" questions.
- [Bratman–Israel–Pollack ingest](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md) <-> source -- **compares-with**: same occasion (deliberative learning). The return link gives the IRMA ingest a contrasting reconsideration policy: event-driven revision of reason-backed intentions.

## Reverse-edge Candidates

- [A claim without external assessment carries three obligations](../../../../theory/a-claim-without-external-assessment-carries-three-obligations.md) → source -- **evidenced-by**: the "Which dependencies must survive revision" bullet already pairs the ATMS and base contraction to show that dependency maintenance, evidential warrant and selection policy are separate. Doyle states that separation outright: in/out versus truth in §1.1 and §10's "opinion revision system", and §6's demand for separate pragmatic choice rules. The edge should target the future memo ingest, or the existing Glimpse ingest if no memo ingest is written. The theory note's five-unquoted-source limit must be checked before adding it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Bacchus–van Run ingest](../../../../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) -- the non-chronological backtracking comparison is already carried by the Glimpse ingest; the memo adds nothing on this axis.
- [BDI survey ingest](../../../../sources/bdi-agent-architectures-a-survey.ingest.md) -- plausible axis (§8's choice between rejecting an action and rejecting a world assumption, against BDI failure recovery), but the Bratman edge already carries the intention-revision comparison more directly. Keep it out unless the ingest develops §8's planning/execution distinction.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- the Glimpse ingest's interpretive edge holds equally for the memo, which adds no new evidence beyond §8.1's "external mechanism" for new defaults, already cited there.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) -- TMS default and sequence patterns do license adoption of a belief (a node goes in), so they are not lightweight control in the note's sense. Linking would mislead.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) -- the §8 "PREFER" nodes superficially resemble intent controlling choice among alternatives. But the note concerns stated intent in delegation; keyword-level overlap.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- the TMS distinction between assumption and derivation has a tempting resemblance, but the note is about artifact authority after derivation from sources, not belief support. The mapping would confuse.
- [Design rationale management](../../../../reference/design-rationale-management.md) -- only `see-also` is authorised to reference. The adjacency (recorded reasons for choices) is generic and would not help a reader of a TMS ingest.
- Non-monotonic keyword hits in apex-mem, Morgan's specification statement and widening/narrowing -- different senses of "non-monotonic" (benchmark trade-offs, refinement monotonicity, fixpoint iteration).

## Index Membership

- [learning-theory tag head](../../../../tags/learning-theory-README.md) -- the Glimpse ingest carries `tags: [learning-theory]`. The memo ingest should carry it for the same reasons, plus §6's additive argument store and §8's revision plans.
- [reflection tag head](../../../../tags/reflection-README.md) -- candidate source tag. §6 makes justifications explicit beliefs that change what is believed when challenged, and §8 represents control state and plans as beliefs. Apply only if the ingest analyses this self-representation substantively rather than mentioning it.

## Synthesis Opportunities

The memo's §1.1 ("attitudes arise from the set of reasons and have no independent existence") together with the explicit-retention note and the rationale-faithfulness note suggests a higher-order claim. Rationale is faithful exactly when it is the operative mechanism, and only reified reasons are revisable targets. The TMS, belief-base contraction and the ATMS are three cases where the explicit dependency record is what the system computes from, not an annotation beside it. No current note states this as the condition under which a KB's recorded reasons can support mechanical revision. Commonplace links are annotations of this kind, and the make-like staleness note already gestures at the gap. This is a candidate for `kb/theory/`, not for this report.

## Maintenance Observations

- No KB artifact cites Quine's web of belief or Rescher's "minimum mutilation". This memo and the reflective-equilibrium ingest are the closest anchors. If the deliberative-learning workshop needs a revision-choice criterion, it lacks a source.
- Agent-memory reviews (ace, AriGraph, eidetic, kgai, continuity, sage-wiki) use "truth maintenance" as an informal contrast term without citing a source. The collection is frozen, so no edges are proposed. Any successor analyses using the term could cite a Doyle ingest.
- The Bratman, BDI and Glimpse-adjacent ingests named here are untracked in the working tree at the time of this report. Edges to them assume they will be committed.

## Flags

- No tracked ingest exists for this snapshot. All Connections Found entries are inert until `cp-skill-ingest kb/sources/.snapshots/doyle-1979-truth-maintenance-system-aim-521.md` produces the authored surface. That ingest should decide whether it supersedes the Glimpse ingest as the primary Doyle citation or complements it with the memo-only sections.
- Split candidate (for the future ingest, not the snapshot): the memo makes several independent assertions across five or more targets and three or more topic areas: belief revision mechanics, explanation summarization, dialectical criticism, belief modelling of others, and control and reflection. One ingest can hold them, but its Extractable Value should separate them.
- OCR caveat: the §§4, 6 and 8 justification formulas are partly garbled. Any edge relying on exact notation (the §8.2 PA/NSA/RO structure, the §8.3 CP selection) should be checked against the page images.
