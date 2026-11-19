---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/plans-and-situated-actions-suchman-1985.md"
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: Plans and Situated Actions: The problem of human-machine communication (Suchman 1985, Xerox PARC ISL-6)

**Source:** [Plans and Situated Actions (1985 thesis)](../../../../sources/.snapshots/plans-and-situated-actions-suchman-1985.md)

The source is an immutable snapshot. Every outbound candidate below is for the authored surface `kb/sources/plans-and-situated-actions-suchman-1985.ingest.md`, which does not exist yet. Labels come from the `kb/sources/COLLECTION.md` "Outbound links" table.

Claims identified in the source:

- Plans derive from situated action. They are projective and retrospective accounts, not controllers of action (Ch. 4 propositions, snapshot l.1597-1609).
- Rules and procedures are explicated only when transparent activity breaks down (the "unready-to-hand"). Action is then made accountable to them (l.1700-1708).
- Mutual intelligibility is achieved on each occasion through situation particulars, "rather than being discharged once and for all by a stable body of shared meanings" (l.1609).
- A plan is a map, not a model. Its efficiency depends on the user having access to the terrain at the time of use (§4.6, l.2066-2100).
- Plans are vague by design. Vagueness is not a defect to remedy (Ch. 8).
- Human-machine communication is asymmetric: the machine maps a restricted set of the user's effects onto a prescribed template. The designer can only "engineer alternatives to interaction's situated properties", mainly by substituting "a description of the situation of action, for access to the actual situation" (l.7210-7225).
- Empirical core: a conversation analysis of first-time users with a copier's expert help system. It identifies two breakdown types the machine cannot detect, the false alarm and the garden path (§7.5, l.6638ff).
- Preface: the Trukese navigator starts with an objective rather than a plan, while the European navigator holds to a charted course (l.165).

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, "Outbound links". The authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags, other sources and external. `kb/work/` and `kb/instructions/` are excluded. Authorised labels by destination:

- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; `defined-in` applies to theory/definitions only.
- sources: `compares-with`, `see-also`.
- agentic-systems and agent-memory-systems: `compares-with`, `see-also`; agent-memory-systems also allows `is-evidence-for`.
- reference: `see-also` only.
- external: `derived-from`, `see-also`.

External prospecting was skipped as the skill requires. The only known external target is the source URL itself (bitsavers PDF), which is the ingest's `derived-from` anchor.

**Curated heads:**
- Read `kb/tags/method-guided-action-README.md`. It is the tag carried by all three sibling Suchman ingests. It declares `complete: true`, so the by-tag `rg` for this tag was skipped. From its list, the intent-framed delegation, fix-what-the-executor-can't-determine, two-layer execution and actionable-methodology entries were flagged.
- Listed `kb/tags/` heads. `observability` (Norman ingest's tag) and `llm-reliability` were noted as plausible tag neighbours, but neither was read in full.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` gave 433 titles. These were filtered with `rg -i 'plan|situat|instruct|underspec|interpret|tacit|explicit|repair|context|map|human analog|indexical|vague|precision|specif|fallback|methodolog|actionable|codif|operational|breakdown|naur|ryle|polanyi|knowing'`, which returned about 90 hits. Flagged: underspecified instructions, two-layer execution, silent disambiguation, human analogies, Naur human-only, goal-holding interpreter, specification strategy, writing styles, legal drafting, out-of-spec output, natural-language meaning as coordination.

**Description listing scan:**
- Descriptions were read for the 16 flagged theory notes, 4 method-guided-action notes, 7 sources (Schegloff, Purver, Norman, Argyris, Parasuraman, MCDP 1, Naur/programming-as-theory-building, plus context-as-an-environment, artifacts-as-memory, intention-is-all-you-need, knowledge-engineering) and `kb/agentic-systems/reviews/ai-agent-book.md`.

**Body search:**
- `rg -l -i 'suchman|situated action|situated-action' kb --glob '*.md'` (work excluded) returned the 3 Suchman secondary ingests, Schegloff/Jefferson/Sacks, Purver/Ginzburg/Healey and `definitions/actionable-methodology.md`. On inspection, the actionable-methodology hit is the phrase "situated actionability", not Suchman.
- `rg -n -i 'indexical' kb/theory kb/reference kb/agentic-systems kb/sources` found only the PD-of-HCI summary and Tarski/IEP liar-paradox hits. The Tarski hits concern formal-language indexicals and were rejected as keyword-only.
- `rg -n -i 'ready-to-hand|heidegger|dreyfus|winograd|breakdown and repair|ethnomethodolog|garfinkel'` returned the Duguid ingest (Heideggerian lineage) and Sutskever-list references (Dreyfus citation only). The KB has no Winograd & Flores or Dreyfus ingest.
- `rg -n -i 'terrain|map is not|the map' kb/theory` found no note on the map/terrain relation of plans.
- `rg -l -i '\bbreakdown' kb/theory` matched two-layer execution and specification strategy.
- `rg -n -i 'plans? (are|as) (resources?|interpreted)|vague(ness)? (is|of)' kb/theory` returned no hits, so no theory note yet states plans-as-resources directly.
- `rg -l -i 'situated|plan-following|plans? as resources|human-machine communication|indexical|mutual intelligib'` returned in agentic-systems only `reviews/ai-agent-book.md` (the "situated loop" section, word use only, rejected); in agent-memory-systems only `review-framework-design.md` (incidental, rejected); in reference, nothing.
- `rg -l -i 'human-machine|mutual intelligib|situated|plan recognition|intention recognition|instruction-following|following instructions' kb/sources --glob '*.ingest.md'` returned 30 files. Kept: Norman, Schegloff, Purver, MCDP 1, programming-as-theory-building, Argyris. Rejected: the rest (see Rejected Candidates).
- `rg -n -i 'objective|situation|circumstance|local evidence'` in the intent-framed delegation note confirmed it frames intent against uncertainty that defeats advance specification.
- Snapshot locator check: `rg -n 'Trukese navigator begins|by a stable body of shared meanings|the efficiency of a plan rests|engineer alternatives to interaction|substitute a description of the situation|central design resource|rules and procedures are explicated|false alarm|garden path'`.
- `rg -n -i 'limits of|extend the access|compensat|differential model'` showed that the 1985 thesis does **not** contain the 1987 book's "three design problems" list (see Maintenance Observations).

**Link following:**
- Read the Connections Found and Extractable Value sections of the three secondary ingests (Duguid, Dittrich, PD-of-HCI). Their shared theory targets were underspecified instructions, two-layer execution, actionable methodology, silent disambiguation, human analogies, Naur, the bitter-lesson notes and goal-holding interpreter. Each states that claims attributed to Suchman "need the book". This snapshot is the first primary text the KB has.
- Followed the intent-framed delegation note to the MCDP 1 ingest, which also links that note (`abstracted-from`).
- Followed the Schegloff and Purver ingests' Suchman edges. Both compare with the Dittrich/PD-of-HCI ingests on repair asymmetry and ask for primary grounding.
- Followed the natural-language-meaning note. Its "no stable shared semantics, alignment held by checks among speakers" claim meets Suchman's proposition (v).

## Connections Found

Theory:

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **compares-with**. The shared axis is where the instruction-action gap originates. The note places it in semantic underspecification that constraining can narrow. Suchman, in her own words, places it in indexicality: an instruction's significance depends on circumstances the instruction cannot carry (§4.4, §4.6 "intractable problem for projects that rest on providing in advance for the significance of canonical descriptions-like instructions"). The secondary ingests make this comparison secondhand; this source lets the ingest state it with locators.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- **compares-with**. The shared axis is which layer runs by default. In §4.2, situated action is transparent by default, and rules and procedures are explicated only at breakdown, with action then "made accountable to them". This inverts the note's method-first fast path. The primary text can now ground what the PD-of-HCI ingest flagged as a secondhand qualification.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with**. The shared axis is whether shared meaning is a stable target or an ongoing local achievement. Proposition (v) says mutual intelligibility is "achieved on each occasion of interaction, through recourse to situation particulars, rather than being discharged once and for all by a stable body of shared meanings". This is an ethnomethodological precedent for the note's untested hypothesis, but the mechanism differs: situated repair rather than learned approximations checked by peers. No existing ingest makes this edge.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**. The shared axis is who detects and repairs a communicative breakdown, and whether the repair is visible. The copier could detect neither false alarms nor garden paths (§7.5). An LLM agent repairs ambiguity but silently. This primary case supplies the pre-LLM baseline the secondary ingests proposed.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- **compares-with**. Ch. 8 says the designer's real project is "to engineer alternatives to interaction's situated properties" rather than simulate human interaction. That keeps the function and refuses the human form, in an HCI setting that predates the note's agent setting. This is a comparison, not a test of the note.
- [Intent-framed delegation is a control regime; prompt length does not establish it](../../../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) -- **compares-with**. The shared axis is purpose versus prescribed course when circumstances defeat advance specification. The preface's Trukese navigator "begins with an objective rather than a plan" and responds to conditions as they arise. That parallels the note's doctrinal sources (MCDP 1, ADRP 6-0) from an anthropological rather than military tradition. Suchman gives no control regime (bounds, reporting, authority), so the comparison also shows what intent-framing adds beyond situatedness.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with**. In §4.6 a plan works like a map: "the map does not have to represent all of the terrain's relevant detail" because the traveller has the terrain at the time of use. This is the 1985 form of the note's rule: leave open what execution-time evidence will settle. Suchman offers no rule for what must be fixed, which the note supplies.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **compares-with**. The shared axis is setting-relativity of guidance. Suchman's plans-as-resources is the strong form of the definition's relativity to operator, operations, target and setting. All three siblings use this edge. A `defined-in` label would not fit, because the ingest does not use "actionable" in the technical sense.
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- **compares-with**. The shared axis is the inference from inexplicit practical understanding to machine inability. Suchman's conclusion that the machine's "insensitivity to particular circumstances" is a fundamental limitation is the same kind of step, drawn from a 1980s rule-following system. Like Naur, she needs an extra premise to generalize beyond that system class. Dreyfus sat on her committee (acknowledgements), which supports the shared Heideggerian lineage Duguid relays.

Sources:

- [Duguid, On rereading Suchman](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) -- **compares-with**. The shared axis is what Suchman claims about plans. Duguid is a secondary reading; this thesis lets a reader check his "plans as interpreted resources" attribution against her 1985 wording.
- [Dittrich, Re-re-reading Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) -- **compares-with**. The shared axes are edition and repair asymmetry. Dittrich reads the 2nd edition (2007, p70); this is the 1985 thesis, which precedes the 1987 book. A reader citing Suchman needs to know which version backs which claim.
- [PD of HCI Suchman summary](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**. The shared axis is argument structure. The summary's breakdown typology and plans-as-resources framing are present in the thesis. Its "three design problems" and differential-modelling material were not found in this thesis and may be 1987 additions or the summarizer's framing.
- [Schegloff, Jefferson and Sacks on self-correction and repair](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) -- **compares-with**. The shared axis is repair as organized interactional resource. Suchman's Ch. 5 (communicative resources, locating and remedying trouble) builds directly on this CA tradition and applies it to human-machine exchange.
- [Purver, Ginzburg and Healey on clarification in dialogue](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) -- **compares-with**. The shared axis is undetected breakdowns. Purver gives corpus rates of clarification requests on the human side; Suchman gives the case of a machine that cannot issue or recognize them.
- [Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**. The shared axis is interactional resources a machine lacks. Suchman's machine cannot see the user's situation; Norman's automation cannot report its own state. Both are 1980s diagnoses of the same asymmetry from opposite sides.
- [Marine Corps MCDP 1, Warfighting](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) -- **compares-with**. The shared axis is objective-held action under uncertainty. The Trukese/European navigator contrast is a non-military counterpart to mission-type orders, and it lacks MCDP 1's authority and reporting structure.
- [Programming as Theory Building (Naur)](../../../../sources/programming-as-theory-building.ingest.md) -- **compares-with**. The shared axis is a situated capacity to map between representation and world. Naur's programmer theory maps world affairs to program structure. Suchman's plan user constructs "a correspondence between the plan, and his or her actions under some actual circumstances" at the time of use (§4.6).

External:

- `https://bitsavers.trailing-edge.com/pdf/xerox/parc/techReports/ISL-6_Plans_and_Situated_Actions.pdf` -- **derived-from**. This is the ingest's analysis anchor.

## Bidirectional Candidates

- [Duguid ingest](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md), [Dittrich ingest](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) and [PD-of-HCI ingest](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) <-> source -- **compares-with**. All three say in Limitations that any claim attributed to Suchman "needs the book". A return link from each to the primary ingest closes that gap for readers who land on a secondary first. Under the snapshot-immutability rule these are edits to the siblings' tracked ingests, and the quote pool is append-only.
- [Schegloff ingest](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) <-> source -- **compares-with**. Its current Suchman edge points at Dittrich and asks for primary grounding of the repair-asymmetry synthesis, which this source can supply.

## Reverse-edge Candidates

These would link to the future `kb/sources/plans-and-situated-actions-suchman-1985.ingest.md` under `kb/theory/COLLECTION.md` rules, where theory-to-sources uses `evidenced-by`. The theory contract's "origin is not corroboration" rule applies. Suchman's copier study is one qualitative case. It can **bound or qualify** a claim, but it corroborates only where the claim could have failed against it.

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → source -- **evidenced-by** (qualifies). It bounds the note's implication that constraining can narrow the gap, because it identifies a situational component that more specification does not remove.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) → source -- **evidenced-by** (qualifies). It shows the inverted default (situated first, rules at breakdown) for human operators.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by**. The false alarm and garden path give primary, observed breakdown types for the "no repair" baseline.

## Off-authorisation Candidates

- [Context engineering](../../../../theory/definitions/context-engineering.md) -- Suchman's diagnosis that designers "substitute a description of the situation of action, for access to the actual situation" names the problem context engineering works on: a model sees a constructed description, not the operator's situation. `defined-in` is authorised for theory/definitions but would mean the ingest uses the term, which it would not necessarily do. `compares-with` overstates it, because the definition does not discuss situational access. Suggest rejecting this as a definition link unless a theory note is written on "context as substituted situation description" (see Synthesis Opportunities).

## Raw Text Candidates

None

## Rejected Candidates

- [AI Agent Book review](../../../../agentic-systems/reviews/ai-agent-book.md) -- the "situated loop" heading uses "situated" in its everyday sense with no plans/action claim. Keyword-only.
- [A goal-holding interpreter fails soft](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- Duguid links it via Orr's technicians, but this thesis does not contain Orr's routinization case. The Trukese navigator holds a goal, but Suchman says nothing about workaround cost or budgets. Too weak for the primary source.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and [bitter lesson selects against unearned reach](../../../../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- the Moore's-Law principled-versus-practical frame is Duguid's 2012 framing, not in the 1985 thesis.
- [Argyris on organizational learning and MIS](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) -- its edge to Duguid rests on Orr's routinization case, which is absent here.
- [Model types and levels of human interaction with automation (Parasuraman et al.)](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- function-allocation levels are adjacent HCI. Suchman does not address allocation levels, so this is "related" only.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md), [Legal drafting solves the same problem as context engineering](../../../../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md), [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- all are topically adjacent through underspecification. The underspecified-instructions and fix-what notes already carry Suchman's specific point, so these would be spray.
- Tarski and IEP liar ingests (`indexical` hits) -- formal-semantics indexicals, unrelated to situated indexicality.
- `kb/reference/*` navigation hits for "navigat" -- KB navigation docs, not Gladwin's navigators.

## Index Membership

- [method-guided-action tag head](../../../../tags/method-guided-action-README.md) -- the future ingest could carry `tags: [method-guided-action]`, as its three siblings do. Under `kb/sources/COLLECTION.md`, source tags do not enter the generated member listing or the `complete: true` check, so no head edit follows.

## Synthesis Opportunities

- **Context as a substituted situation description.** Three sources and notes together imply a claim no theory note states: an LLM agent receives a description of the operator's situation in place of access to it, so the context engineer faces Suchman's 1985 design problem. The pieces are this source (Ch. 8, the designer substitutes a description of the situation for access to it), [silent disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) (the agent repairs without visibility) and [fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) (execution-time evidence settles open choices). The difference is that the agent can now repair from tool access, but it has no shared situation with the operator. That would be a candidate theory note. Its mechanism needs stating before it clears the quality bar.
- **Repair-locus inversion** (already flagged by the Dittrich and PD-of-HCI ingests): classic machines detect no breakdown, humans repair collaboratively (Schegloff, Purver), and LLM agents repair silently. This source is the primary grounding those ingests said was missing for the machine side.

## Maintenance Observations

- **Edition mismatch across the Suchman cluster.** This snapshot is the February 1985 PARC thesis (ISL-6), not the 1987 Cambridge book read by PD-of-HCI or the 2007 2nd edition read by Dittrich. The thesis conclusion has "engineer alternatives to interaction's situated properties" but no "three design problems" list (extend access, make limits clear, compensate). `rg` for "limits of", "extend the access" and "differential model" found no match. Claims in the PD-of-HCI ingest's Extractable Value item 2 therefore cannot be grounded in this snapshot. The future ingest should state which edition it covers.
- **Concurrent ingest.** No `.ingest.md` for this snapshot existed at report time, while a `cp-skill-ingest` agent was active in the session. Every outbound edge above is addressed to that pending ingest.
- **No Heideggerian-lineage sources.** Dreyfus (committee member), Winograd and Flores, and Garfinkel are cited by Suchman and named by Duguid, but no ingest exists. The KB has no primary source for the breakdown-and-repair lineage that several theory notes now touch indirectly.

## Flags

- The occasion for the three sibling ingests is the operationalization workshop under `kb/work/`. Linking into `kb/work/` is excluded, so no candidate is listed there. The workshop is the likely consumer of this primary source.
- Tension, unresolved: the underspecified-instructions note treats the gap as narrowable by constraining. Suchman treats it as irreducible in principle for situated action. The comparison should keep both positions rather than resolve them.
- Transfer caveat: Suchman's machine is a 1980s plan-recognizing help system that cannot interpret. Every theory edge that maps her findings to LLM agents is the reader's analogy, which the sibling ingests also note.
