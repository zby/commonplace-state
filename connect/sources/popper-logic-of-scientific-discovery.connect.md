---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/popper-logic-of-scientific-discovery.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: The Logic of Scientific Discovery (Popper, Routledge Classics 2002)

**Source:** [The Logic of Scientific Discovery](../../../../sources/.snapshots/popper-logic-of-scientific-discovery.md)

The source is an immutable snapshot, so it never carries links itself. Its authored surface is the matching ingest, `kb/sources/popper-logic-of-scientific-discovery.ingest.md`, which **does not exist yet**. Every "Connections Found" item below is a candidate for that ingest's analysis and footer. Section locators (`sec N`, snapshot line numbers) point into the snapshot for whoever grounds the claims later.

Main content the candidates below rely on, with snapshot locations:

- **sec 2 (l. 396–414):** the psychology of knowledge (how ideas are conceived) is kept separate from the logic of knowledge (how ideas are tested); "there is no such thing as a logical method of having new ideas".
- **sec 18–20 (l. 1048–1160):** modus tollens on levels of universality; conventionalist stratagems (ad hoc auxiliary hypotheses, ad hoc changes of definition, doubting the observer, refusing to acknowledge falsifying experience). Rule: an auxiliary hypothesis is acceptable only if it *raises* falsifiability (l. 1138). Changing a definition is a modification of the system, which "has to be re-examined as if it were new".
- **sec 22 (l. 1190–1208):** falsification requires a reproducible effect, not stray contradicting basic statements.
- **sec 29–30 (l. ~1554–1586):** basic statements are accepted by decision; "Science does not rest upon solid bedrock … a building erected on piles".
- **sec 31–36 (l. 1608–1775):** empirical content is the class of potential falsifiers; degrees of falsifiability are compared by the subclass relation; higher content means lower logical probability. Sec 36 covers universality and precision: a statement that is more universal but less precise than another is *not comparable* with it (the q/r case).
- **sec 20, 38–46:** simplicity is identified with degree of falsifiability, and ad hoc hypotheses cannot be compared on testability (l. 2101–2113).
- **sec 65–68 (l. 3013–3111):** probability statements are not falsifiable. They can be *used* as falsifiable only through a methodological decision.
- **sec 79–85 (l. 3748–4150):** corroboration is not probability. The degree of corroboration depends on the severity of tests, not on the number of instances (l. 3962). "Science is not a system of certain, or well-established, statements" (l. 4112).

## Discovery Trace

**Setup:**
- Source collection is `sources`. `kb/sources/COLLECTION.md` exists. Its "Outbound links" section gives these destinations and labels: notes (`is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; `defined-in` for notes/definitions); sources (`compares-with`, `see-also`); agent-memory-systems (`is-evidence-for`, `compares-with`, `see-also`); agentic-systems (`compares-with`, `see-also`); reference (`see-also` only); external (`derived-from`, `see-also`). It excludes `kb/work/` and `kb/instructions/`. The snapshot is never the link author; the ingest carries the links.
- The external destination was not prospected. The only external target already in hand is the snapshot's `source` URL (Routledge product page), which the future ingest's `derived-from` footer line would carry.
- The source is 8,806 lines. I read its heading structure and then targeted passages (lines listed above). I did not read the probability, quantum-theory, or starred-appendix chapters in full.

**Existing-surface scan:**
- `rg -l -i "popper" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'` returned 51 files, including 24 notes, 23 sources, 1 reference proposal, and 2 tag heads.
- `rg -n -i "logic of scientific discovery|logik der forschung" kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/work/**'` found only two artifacts: `generality-bought-to-avoid-counterexamples-is-paid-for-in.md` (cites the book by title with no link) and `the-logic-of-scientific-discovery-wikipedia.ingest.md` (whose Recommended Next Action asks for this primary text).
- `rg -n -i "popper" <candidate notes>` showed which notes attribute doctrine to Popper without a primary-source link. These are claim-modality (probability treatment; context of discovery), the notes COLLECTION modality paragraph, ad-hoc-explanation (narrow Popperian sense), and generality.

**Body search (all over `kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources`, excluding snapshots):**
- `corroborat`: mostly incidental English. The relevant hit is `definitions/tentative-theory.md`, which says corroboration strengthens reliance without reducing tentativeness.
- `severe test|severity of|severe(ly)? test`: the C&R ingest, scaffold-not-vocabulary, and HEP. Scaffold-not-vocabulary and HEP were rejected (see below).
- `basic statement`, `demarcation`: only the Wikipedia ingest.
- `conventionalis`, `potential falsifier`, `logical probability|improbab`: no hits. The KB has no vocabulary for these; see Maintenance Observations.
- `problem of induction|inductivis|inductive logic`: only Sutskever's-list book chapters (irrelevant).
- `empirical basis|empirical content`: four incidental hits, none kept.
- `falsifiab`: 25 files. Kept: claim-modality and the AHE review. Examined and rejected: `reference/scenario-architecture.md` and `reference/adr/009` (ordinary-English use).
- `ad hoc`: 25 files, mostly the everyday sense. Kept: `ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md` (explicitly separates the Popperian narrow sense).
- `immuniz|immunis`: domain-pricing, candidacy-evidence, a-framework-rule-with-a-boundary-preserving-rival, ADR 066, ADR 080. Kept: domain-pricing. Reverse-edge only: ADR 066.
- `universality`: kept the generality note. The others use "universal" in the software-factory sense and were rejected.
- `simplicity`: no hit uses simplicity as testability. The Mooney abduction/induction ingest treats simplicity as an accuracy-side criterion; rejected (see below).
- Snapshot greps used to check claims: `conventionalist stratagem`, `swamp`, `reproducible effect`, `class of potential falsifiers`, `levels of universality|degree of precision`, `logical probability`, `probability statements`, `methodological rule|methodological decision`, `degree of corroboration`, `severity of`, `ad hoc`, `does not diminish`, `not falsifiable`, `orbits of`, `illusory aim|system of certain`, `psychology of knowledge`.

**Description listings read:** descriptions of 28 candidate artifacts, printed with `rg -N -m1 '^description:' <file>`.

**Full bodies or relevant sections read:** claim-modality, notes/COLLECTION.md "Claim modality" paragraph, generality, narrowing, ad-hoc-explanation (sense section and regime), domain-pricing (immunization lines), first-principles (negative test), mechanistic-constraints (opening sections), discovery-lifecycle (opening), the Wikipedia ingest (whole), and the C&R ingest (Connections through Recommended Next Action). For the AHE review I read the falsifiable-edits and falsification-loop paragraphs.

**Link following:**
- claim-modality links to domain-pricing, narrowing, candidacy-evidence, and ADR 066. This is the refutation/repair cluster, and it is where the book lands hardest.
- narrowing links to generality. generality links to abstract-an-experience and first-principles.
- The C&R ingest already connects narrowing and candidacy-evidence with Popper's *later* text. This book is the earlier primary statement of the same rules.
- The Wikipedia ingest already links claim-modality, discovery-lifecycle, C&R, and the POPPER system ingest. Each of those links rests on quotations this book supplies first-hand.

**Destinations skipped or thin:**
- agentic-systems: `rg -n -i "falsif|popper|refut" kb/agentic-systems` returned only EvoOntology's "falsifiable hypothesis" in its host method, which is a keyword match. Nothing kept.
- reference: only `see-also` is authorised. ADR 066 is a real neighbour but is better reached through claim-modality. Listed as a reverse-edge candidate only.
- tags: the label table authorises no tag destination. The source has no `tags:`, so no tag-head reads were triggered by tags. I scanned `kb/tags/foundations-README.md` and `kb/tags/kb-maintenance-README.md` through the Popper grep.

## Connections Found

Candidates for the future `popper-logic-of-scientific-discovery.ingest.md`:

- [claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) -- **is-evidence-for**: The note makes two Popper attributions with no primary link, and this book is the primary text for both. (1) The statistical mode's stated-refuter requirement is "Popper's treatment of probabilistic claims — strictly unfalsifiable until a methodological decision fixes the refuting frequency". That treatment is sec 65–68 (l. 3105–3111). (2) Conjecture is "abduction in the context of discovery, which Popper deliberately left unregulated". That is sec 2 (l. 410–414). The book also supplies the universal mode's refuter: modus tollens (sec 18), made conditional on a reproducible effect (sec 22). This is the strongest candidate: it replaces the Wikipedia ingest as grounding for the note's "genuine instance".
- [narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) -- **is-evidence-for**: The note's central move is that narrowing by redefinition empties a claim. Sec 20 names ad hoc change of definition as a conventionalist stratagem and rules that a changed definition makes the system one that "has to be re-examined as if it were new". Sec 36 supports the honest-narrowing half: lowering universality lowers content ("q says less than p"). The auxiliary-hypothesis rule (l. 1138: acceptable only if it raises falsifiability) is a stricter guard than the note's refuter test. It says a repair should *add* what the claim forbids, not merely keep some refuter.
- [generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- **is-evidence-for**: The note builds on sec 36 (levels of universality and degrees of precision; content as what a claim rules out, sec 31–35) and names the book without a link. There is one tension; see Flags. Popper says a statement that is more universal but less precise than another is *not comparable* with it by the subclass relation. The note's "content stays flat" is therefore the note's own extension, not Popper's.
- [ad hoc explanation can be rational when error is cheap and local](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) -- **is-evidence-for**: The note's "narrow sense … associated with Popper" (a content-reducing rescue from refutation) is exactly sec 19–20's ad hoc auxiliary hypothesis and the l. 1138 rule. Sec 46 adds that ad hoc hypotheses cannot be compared on testability (l. 2113). This primary text would anchor the sense distinction the note depends on.
- [domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- **is-evidence-for**: The note separates an idealization from "an immunized claim — an adjustment that makes refuting cases stop biting". Pricing blocks "the immunizing move of labelling a counterexample an edge case after it lands". Sec 19–20's catalogue of conventionalist stratagems is the original taxonomy of those immunizing moves. Popper's concession (l. 1126) that falsifiability alone cannot classify a system, so a methodological decision must exclude the stratagems, matches the note's point that the adequacy record, not the logic of the claim, blocks immunization.
- [tentative theory](../../../../notes/definitions/tentative-theory.md) -- **is-evidence-for**: The definition says corroboration strengthens later reliance without making a theory less tentative. Sec 79–85 is the primary statement of this: corroboration is not probability (l. 3748–3758), corroboration depends on test severity (l. 3962), and "Science is not a system of certain, or well-established, statements" (l. 4112). The definition currently cites only the 1966 essay and C&R.
- [Popper, Conjectures and Refutations](../../../../sources/popper-conjectures-and-refutations.ingest.md) -- **compares-with**: The axis is the earlier versus the later statement of the repair rules. LScD sec 20 states the anti-ad-hoc rule as a condition on each auxiliary hypothesis (it must raise falsifiability). C&R ch. 10 turns it into the requirement of independent tests and new successful predictions. That C&R ingest's extractable item 1 ("repair should face consequences beyond the failures that prompted it") can then cite its origin.
- [The Logic of Scientific Discovery (Wikipedia)](../../../../sources/the-logic-of-scientific-discovery-wikipedia.ingest.md) -- **compares-with**: The axis is primary versus tertiary fidelity for the same book. The Wikipedia ingest's two quotations (asymmetry; reproducible effect, sec 22 l. 1190) can be checked here in context. Its Limitations section flags a risk that sec 22 read alone licenses dismissing counterevidence, and sec 22 in context shows that reading is wrong. This is also a bidirectional candidate (below).
- [POPPER: automated hypothesis validation with sequential falsifications](../../../../sources/automated-hypothesis-validation-sequential-falsifications.ingest.md) -- **compares-with**: The axis is how a probabilistic hypothesis becomes refutable. Sec 65–68 makes it refutable through a methodological decision about which frequency deviations count. POPPER makes it refutable through sequential statistical tests with Type-I error control. That ingest already says "the Popperian mapping is partial". This book supplies the side of the comparison that ingest lacks.
- [sound agentic science requires adversarial experiments](../../../../sources/sound-agentic-science-requires-adversarial-experiments.ingest.md) -- **compares-with**: The axis is severity versus quantity of tests. Sec 82–83 makes the degree of corroboration depend on "the severity of the various tests" rather than "the number of corroborating instances" (l. 3962). This matches that paper's distinction between discriminating experiments and repeated statistical reanalysis, which the ingest treats as its methodological point.
- [agentic harness engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: The axis is whether a repair must predict something testable. AHE requires each harness edit to carry a `change_manifest.json` of predicted fixes and risk tasks, which the next iteration scores. That is an operational version of the sec 20 rule that an auxiliary change is acceptable only if it raises testability. The review's own caveat ("benchmark flips … cannot fully explain why … root cause was right") matches Popper's point that corroboration is not verification. Moderate strength; keep only if the ingest discusses the auxiliary-hypothesis rule.

## Bidirectional Candidates

- [The Logic of Scientific Discovery (Wikipedia)](../../../../sources/the-logic-of-scientific-discovery-wikipedia.ingest.md) <-> source -- **compares-with**: Its Recommended Next Action asks for exactly this primary text and says the Wikipedia ingest is only a fallback grounding target. A return link would mark that the action is done. It would also tell a reader to prefer the primary ingest for the p. 19 and p. 66 quotations.
- [Popper, Conjectures and Refutations](../../../../sources/popper-conjectures-and-refutations.ingest.md) <-> source -- **compares-with**: C&R repeatedly refers back to LScD for falsifiability and content. A return link gives that ingest a primary source for the doctrines it takes for granted.

## Reverse-edge Candidates

Artifacts that should link *to the future ingest* under their own collection rules. The notes-side links would cite `../sources/popper-logic-of-scientific-discovery.ingest.md`, with "(snapshot required)" in the link text until cp-skill-ground retains quotes.

- [claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) → source -- **evidence**: Needs a primary citation for sec 2 (context of discovery left unregulated) and sec 65–68 (probability hypotheses become refutable only through a methodological decision). The highest-priority grounding target.
- [notes COLLECTION.md, "Claim modality"](../../../../notes/COLLECTION.md) → source -- **evidence**: The collection contract repeats the "Popper's treatment of probabilistic claims" attribution. As a system-definition artifact it may prefer to cite only through the claim-modality note. The operator should decide.
- [generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) → source -- **evidence**: Replaces the bare-title citation "*Logic of Scientific Discovery*, on levels of universality and precision" with a link to sec 36. The Flags tension should be resolved at the same time.
- [narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) → source -- **evidence**: Sec 20's definition-change rule is the primary warrant for the redefinition failure.
- [ad hoc explanation can be rational when error is cheap and local](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) → source -- **evidence**: Would ground the Popperian narrow sense in sec 19–20.
- [tentative theory](../../../../notes/definitions/tentative-theory.md) → source -- **evidence**: Would add sec 79–85 beside the 1966 and C&R citations for the corroboration sentence.
- [066 — Claims declare modality in text](../../../../reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) → source -- **see-also**: The ADR's deciding force is that "an idealization form must not become an immunizing stratagem". That is Popper's conventionalist-stratagem concept. Low priority, because the ADR is a decision record and reaches Popper through claim-modality.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Scaffold, not vocabulary? A Popperian code-generation skill](../../../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md) -- It mentions severe tests and a description-length rule against ad hoc rescue. But it evaluates a prompt, not Popper's account, and it tests the procedure, not the doctrine. A compares-with edge would carry no named axis beyond "uses Popperian words".
- [HEP: hypothesis evolution protocol](../../../../sources/hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md) -- The severe-test grep hit is incidental. HEP's support/refutation thresholds are agent-supplied probabilities, which sec 80–83 would reject as a measure of corroboration. That is a real critique, but it belongs in HEP's ingest, not as an edge from this book.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) -- Popperian in framing, but its argument comes from KB mechanics (bounded context, oracle quality) and cites no Popper doctrine that this book would ground. A link would be topical only.
- [Title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) -- "Popper's criterion applied to knowledge management" is a loose appeal to falsifiability. The book could ground it, but the note makes no load-bearing claim about Popper's content. Too generic.
- [First-principles reasoning selects for explanatory-reach](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- Its "should rule out at least one plausible alternative" echoes content as prohibition. The note is Deutsch-derived and already routes criticism through the falsifier-blocks note, so adding this book would be a second-order echo.
- [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) -- The Wikipedia ingest already links it for the sec 22 reproducible-effect routing. The definition's lineage is Peircean, so the primary Popper text adds nothing beyond that existing moderate edge.
- [theory builder](../../../../notes/definitions/theory-builder.md) and [theory building has distinct precedents](../../../../notes/theory-building-has-distinct-precedents.md) -- Both rest on the P1→TT→EE→P2 schema and objective knowledge (1966/1968 essays). LScD does not state that schema, so it would be a weaker citation than the ones already there.
- [candidacy evidence licenses escalation, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- The C&R ingest already covers its Popperian comparison (ch. 10: candidacy requirements versus empirical success). LScD's closest analogue, basic statements accepted by decision (sec 29–30), bears on a different distinction.
- [Integrating abduction and induction in ML (Mooney)](../../../../sources/integrating-abduction-and-induction-in-machine-learning.ingest.md) -- The simplicity hit uses simplicity as a learning bias. Sec 41–46 identifies simplicity with falsifiability, which could support a compares-with edge. But the ingest's point is explanatory reach, so the axis would be forced.
- `kb/agentic-systems/reviews/evoontology.md` -- "falsifiable hypothesis" is a keyword match in a host-method checklist.

## Index Membership

None. The sources collection has no curated topical index for ingests, and tag heads are not an authorised destination from sources. When the ingest exists, the Popper cluster (three existing Popper ingests plus this one) could be surfaced from [foundations](../../../../tags/foundations-README.md) by that head's own maintainer, if the head wants primary-source pointers.

## Synthesis Opportunities

The KB has three repair-escape notes, each with its own guard: [generality](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) (widening; forbids-test), [narrowing](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) (redefinition; refuter test), and [domain pricing](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) (idealization; adequacy record). [Ad hoc explanation](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) separates off the Popperian rescue sense. Together these are an unassembled version of Popper's sec 19–20 catalogue of conventionalist stratagems plus his single counter-rule: a modification is admissible only if it raises what the system forbids. That suggests a possible higher-order claim: every defensive repair of a claim is one of a small number of stratagems, and one content-monotonicity guard (the repair must not lower what the claim forbids unless it drops scope honestly) would replace the per-escape guards. Per the fold-claims preference, this should be tested by folding it into one of the existing notes before anyone considers a new note.

## Maintenance Observations

- **Bare-title citation.** [generality](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) cites the book by title with no ingest link. This violates the sources contract ("a durable source-dependent claim links the tracked ingest"), and the ingest to link to did not exist until now.
- **Unlinked Popper attributions.** [claim-modality](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) and the "Claim modality" paragraph in [notes/COLLECTION.md](../../../../notes/COLLECTION.md) attribute the probability-treatment doctrine to Popper with no source link. The same applies to claim-modality's context-of-discovery attribution.
- **Missing vocabulary.** The KB has no vocabulary for "conventionalist stratagem", "potential falsifier", or "empirical content". It uses "immunizing", "forbids", and "content" instead. If the ingest introduces Popper's terms, it should map them onto the KB's existing words rather than add parallel terms (one term per concept).

## Flags

- **Tension (generality note versus sec 36).** The note says universality and precision "can be traded against each other with content held constant", and it attributes the two-dials account to Popper. Sec 36 (l. 1761–1771) says that when one statement is more universal and the other more precise (Popper's q versus r), they are *not comparable* by the subclass relation, and neither is derivable from the other. Popper therefore does not support "content held constant"; he supports "content not comparable by his measure". The note's claim may still hold as its own conjecture, but the attribution should be separated from it. I am flagging this, not resolving it.
- **Authored surface missing.** No `kb/sources/popper-logic-of-scientific-discovery.ingest.md` exists. All Connections Found are provisional until cp-skill-ingest writes it. A cp-skill-ingest agent is active in this session and may be producing it.
- **Scope of the source.** The book makes several independent assertions: demarcation, basic statements, content and testability, simplicity, probability, corroboration, and quantum theory. An ingest analysis should concentrate on the refutation/repair cluster (sec 2, 18–22, 29–36, 65–68, 79–85), where the KB already has live claims. The probability formalism, quantum-theory chapter, and most starred appendices have no KB landing.
