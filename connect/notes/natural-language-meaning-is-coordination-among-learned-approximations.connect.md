---
description: "Connections for the revised meaning hypothesis: classical and subsymbolic accounts, vocabulary controls, public norms, and limits of reviewer agreement as a test"
type: types/connect-report.md
source: kb/notes/natural-language-meaning-is-coordination-among-learned-approximations.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: Natural-language meaning as coordination

**Source:** [Natural-language meaning is coordination among learned approximations](../../../../notes/natural-language-meaning-is-coordination-among-learned-approximations.md).

This pass reads the revision that cites Fodor and Pylyshyn directly and leaves its relation to their structural requirements open. All entries below are candidates; no library links were authored. Existing links to Lampinen, Fodor–Pylyshyn, constraining, codification, the deviation taxonomy, progressive constraining, and oracle strength are not proposed again.

## Discovery Trace

**Contracts and navigation.** Read the source in full, the notes outbound contract, the connect-report type, and the reports contract. Read the notes, sources, agent-memory-systems, agentic-systems, instructions, types, and tags landings; inspected the reference landing's workflow and navigation material. Read the learning-theory, constraining, and llm-reliability tag heads. Learning-theory declares `complete: true`, so its by-tag sweep was skipped. The other two heads have no completeness mark. Read the tags, instructions, reference, and sources outbound rules for inbound candidates. Notes permits source comparisons through `see-also` or qualifying evidence through `evidenced-by`; its `contrasts` label applies only to notes.

**Fresh title scan.** Generated the full H1 surface once with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ kb/instructions/ kb/types/ kb/tags/ --glob '*.md'`. Scanned all returned titles. Strong leads were the Smolensky ingest, vocabulary-collision note, public-meaning/conformance note, shared-prior note, and representational-form definition. Minimum viable vocabulary, legal drafting, calibration fixtures, and EvoOntology received narrower evaluation.

**Notes searches.** Ran `rg -n -i '^description:.*(semantic|vocabular|natural.language|interpret|disagreement)'` across the authorized collections, then `rg -n -i 'shared (meaning|norm|prior)|public meaning|correction pressure|registered (term|definition)|semantic (drift|target)' kb/notes --glob '*.md'`. Ran `rg -l '^tags:.*\b(constraining|llm-reliability)\b' kb/notes --glob '*.md'`. These searches separated public norm formation from executor conformance, and vocabulary agreement from independent correctness. Read candidate arguments and relevant scope sections; retained the specific comparisons below. Minimum viable vocabulary concerns extraction cost rather than alignment, so it remains a secondary lead rather than another outbound link.

**Sources searches.** Ran `rg -l -i 'systematicity|compositionality|learned approximation|interpretation variance|semantic coordination'` over notes, sources, reference, both system collections, instructions, and types. Read the Smolensky ingest in full. It already links to the meaning note and identifies a missing step from individual competence to a population account. Its Quotes section is empty, so it is a discovery lead, not ready retained evidence for a new source-dependent claim. Lampinen and Fodor–Pylyshyn are already cited by the target.

**Reference and types.** Evaluated ADR 022's active-vocabulary decision, the opening and fixture-design discussion of the semantic-gate calibration proposal, and the definition type. These specify an operating policy, a proposed evaluation method, and a writing contract; none tests the population hypothesis. The calibration proposal offers a concrete next evaluation design, retained as a limited companion. The other two are recorded under rejected candidates.

**External-system collections.** The landings and full title surface supplied EvoOntology as the closest candidate. Scoped `rg -n -i 'semantic|ontolog|vocabular'` over its current and legacy reviews. The current review explicitly separates recalled semantics, supplied evaluation scores, and demonstrated benefit. Rejected it as evidence for the proposed meaning mechanism; ontology storage and evolution do not establish population alignment under correction. No other system title or scoped description justified a deeper pass.

**Instructions.** Inspected the instruction landing and title surface; searched review-gate descriptions and then resolved the concrete `accessibility/undefined-terms` gate with `rg --files kb/instructions/review-gates | rg 'termin|vocab|defin'`. Read that gate. It checks whether a reader receives a gloss, not whether correction creates shared meaning. Under the exceptional-link posture, no procedure should depend on this untested hypothesis merely because it enforces vocabulary practices.

**Link following and inbound search.** Followed minimum viable vocabulary to recognition/extraction-cost context, vocabulary collisions to the opening and mechanism of context without scoping, and the reliability head to the public-meaning and prompt-variation notes. Read the representational-form, constraining, and codification definitions to keep cognitive architecture separate from artifact classification. Ran `rg -n -F 'natural-language-meaning-is-coordination-among-learned-approximations.md' kb --glob '*.md'`: current inbound library links are in the Fodor–Pylyshyn and Smolensky ingests. Those existing edges are not new candidates. No external search was run; known external papers are reached through tracked ingests. Workshop artifacts were excluded.

## Connections Found

1. [On the proper treatment of connectionism](../../../../sources/smolensky-proper-treatment-connectionism.ingest.md) — **see-also**: a historical comparison for the difference between individual learned competence and publicly stated knowledge. It helps identify what additional argument the population-level semantics claim needs. Use the ingest as an analytical companion; ground the relevant primary passages before adding any claim attributed to Smolensky. Its retained article excludes commentary and the author's response.
2. [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — **mechanism**: supplies concrete controls behind the note's KB-vocabulary consequence: explicit clause frames, distinct terms, and validator-defined positions have different binding strength. It also bounds the claim: merely having a definition does not enforce correct interpretation. These controls are a candidate implementation of alignment pressure, not corroboration of the population hypothesis.
3. [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md) — **contrasts**: distinguishes the origin and precision of public norms from whether an executor conforms to them. The target treats shared linguistic norms as weak but usable; the meaning hypothesis questions when their valid set is determinate. A reader needs this distinction before inferring that lack of a perfect semantic target removes ordinary error attribution.
4. [Decorrelated reviewers still share the field's prior](../../../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — **contrasts**: qualifies the proposed review-disagreement proxy. Agreement can arise from a shared training prior without correction having improved discrimination. The experiment should distinguish convergence in interpretation from correctness against an independently specified local use; neither is established by a lower disagreement rate alone.
5. [Representational form](../../../../notes/definitions/representational-form.md) — **defined-in**: fixes the KB's artifact-level use of symbolic, natural-language, and distributed-parametric. This prevents the comparison with Fodor–Pylyshyn from treating their classical cognitive architecture as identical to the KB's category of artifacts with fixed operational semantics.
6. [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — **contrasts**: separates varying phrasing under an agreed task meaning from changing the correction conditions that might stabilize meaning. This prevents the proposed experiment from reading ordinary prompt sensitivity as a test of the population hypothesis.
7. [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — **see-also**: supplies a concrete proposed route from reviewer agreement to an independent test of detection and false alarms. It distinguishes known-case regression from field calibration. This is a design proposal, not a shipped evaluation or evidence that registered vocabulary improves semantic alignment.

## Bidirectional Candidates

- [Vocabulary-collision note](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) → source — **contrasts**: its readers can compare concrete controls for local sense binding with the broader, untested explanation that correction maintains meaning. This reverse link should preserve that difference in warrant and scope.
- [Executor-conformance note](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md) → source — **contrasts**: its public-meaning premise has a boundary where readers cannot agree on admissible interpretations. The source develops that boundary as a hypothesis; it does not invalidate the target's clear-constraint cases.

## Reverse-edge Candidates

- [Lampinen ingest](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) → source — **compares-with**, authorized by the sources contract: directs a reader from the essay's account of mathematical competence to Commonplace's explicit extrapolation to natural language. The context phrase must say that the extension is ours and untested, so the new link cannot make Lampinen appear to have asserted it.

The Fodor–Pylyshyn and Smolensky ingests already contain inbound links. Tag-head possibilities are listed under Index Membership.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Minimum viable vocabulary](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md): a useful distinction between extraction efficiency and alignment, but the vocabulary-collision candidate already follows into this neighborhood. Another link would add less than the selected controls-and-limits comparison.
- [Legal drafting](../../../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md): concrete institutional examples fit the source's discussion of legal definitions, but the analogy alone would not support its population account. The selected vocabulary and norm comparisons are more direct; do not import the legal note's broad jurisdictional generalizations as evidence for this hypothesis.
- [EvoOntology](../../../../agentic-systems/reviews-archive/evoontology.md): retained business semantics and ontology evolution do not demonstrate semantic alignment across speakers or agents. Its review expressly leaves controlled recall effects and trustworthy evaluation provenance unresolved.
- [Definition type](../../../../types/definition.md): explains the contract of a definition artifact, not its measured effect on reader agreement. Existing definition links supply the necessary vocabulary without turning the type spec into empirical support.
- [ADR 022](../../../../reference/adr/022-active-vocabulary-and-write-path-first-mentions.md): records the active-vocabulary policy already named in the source. It supplies no test of the proposed mechanism; a policy-history link would dilute the present argument.
- [Undefined-terms gate](../../../../instructions/review-gates/accessibility/undefined-terms.md): checking first-mention glosses is not a test of the theory, and the gate does not need that theory as a premise. No inbound `rests-on` edge is warranted.

## Index Membership

- [Constraining head](../../../../tags/constraining-README.md): candidate selective entry as an **untested interpretation of why definitions and correction narrow readings**. The source substantively addresses the head's inclusion condition; its existing tag is sufficient, so this would improve navigation rather than assign a new tag.
- [LLM-reliability head](../../../../tags/llm-reliability-README.md): candidate entry beside the deviation taxonomy as an **open question about when public meaning is determinate enough to diagnose interpreter failure**. Keep the hypothesis label visible.
- No separate learning-theory entry is needed: its complete head already routes through the two child tags the source carries.

## Synthesis Opportunities

A bounded vocabulary experiment could combine the source's prediction, the vocabulary-collision controls, the shared-prior caveat, and the calibration proposal. Compare explicit definition alone with locally repeated glosses and correction feedback on matched uses. Measure both disagreement and independently labelled application errors; distinguish gains on corrected examples from held-out uses. This could test the local KB-vocabulary consequence. Even a positive result would not establish the broader claim that natural language has no external semantic target. This is a possible investigation, not a new theory or an experiment performed by this pass.

## Maintenance Observations

- The [Fodor–Pylyshyn ingest](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md), in Connections Found, still says the meaning note “currently presents Fodor and Pylyshyn through Lampinen.” The source note now cites the primary ingest directly, and the ingest's Recommended Next Action describes the revision already completed. Those analytical sections need a later authorized refresh; preserve the Quotes section and immutable snapshot checksum. No ingest was edited here.

## Flags

- **Inference boundary:** the new historical qualification leaves a separate gap: a learned account of individual competence does not by itself entail the absence of an external semantic target. Smolensky is a useful comparison for investigating that inference, not evidence that settles it.
- **Operational tension:** the source says that a perfect semantics does not exist and that this is why diagnosis needs three questions. The conformance note derives those questions from distinct norms and sampling even where a local public meaning is clear enough. A future revision should distinguish semantic indeterminacy from executor non-conformance rather than making the latter depend on the former.
- **Split candidate:** this source connects to more than five notes across cognitive representation, vocabulary design, and reliability/evaluation, while separately asserting a population semantics, a claim about formal semantics, and an implication for LLM semantics. Preserve the central hypothesis as one note, but consider separating those consequences if they acquire independent arguments or tests. No split was performed.
- **Grounding before source use:** Smolensky's ingest currently retains no quotes. Run `cp-skill-ground` for the exact source-side proposition before authoring a substantive attribution; do not use its analytical sections as retained primary evidence.
