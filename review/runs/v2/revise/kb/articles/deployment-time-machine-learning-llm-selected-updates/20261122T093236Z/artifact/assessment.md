# Assessment: Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

## Proposed purpose

No purpose was named, so this assessment uses the following one. ML researchers and agent builders who are new to the KB should finish the article able to state its two claims and how the bet would be tested and could fail. The two claims are: (1) selecting updates to a deployed system's retained instructions or criteria needs a comparison, not a single score; (2) the bet that a fixed-weight LLM can build the preference model from a stated purpose and make the robust comparison. The operator corrects this purpose if it is wrong.

## What reads well

The routing-line walkthrough comes before the abstraction. The evidence section is candid: it reports no completed run, names five hazards and states a failure condition. Together they make the bet concrete and falsifiable.

## The sentence a hostile reviewer would attack first

"Third, no single scalar metric had to be invented to compare saved misfilings against diffuse context load." The critique, composition-friction and premise reports all reach this sentence on their own. The example is constructed ("Suppose…"), yet the summary says it "establishes" its lessons. The trial beats permanent adoption under every compatible measure. The trial against leaving the file alone is not shown to be robust: a measure that weights context load heavily prefers no change. So the example shows a bounded decision taken under reversibility. It does not show a robust comparison deciding. As written, a judge using a hidden scalar weighting would produce the same narrative.

## Ranked changes (highest value against the purpose first)

1. **Narrow five overclaims that a technical reader would catch** — pass: `narrow-overclaims`. Cost: about six sentences, applied in place. Targets:
   - The worked-example summary ("That sequence establishes three things", "the system adapted", and the third lesson). Recast these as what the illustration shows. Say that the trial beat permanent adoption robustly, and that the choice of the trial over no change was a bounded decision under reversibility. Sources: finding-9 epistemic-status-blur; critique, friction and premise reports.
   - "Those reasons can be checked and challenged one at a time." Restore the cited necessary-preference note's limit: the factual parts can be checked, but the weighing cannot be checked independently. Source: critique.
   - "Once a language model supplies the comparison … the system sits on the computation side of the Bitter Lesson." Make it conditional on results scaling with compute, which the bootstrap paragraph already requires. Sources: friction and premise reports.
   - "Unlike proof-gated switches, empirical admission admits harmful changes." The article's own Gödel paragraph concedes that a proved switch can be harmful under an inadequate formalization. Contrast what each filter can certify instead. Source: finding-13 framing-mismatch.
   - "…is equivalent to no set of value functions." Restrict the statement to strict preferences under a fixed set, so that decisions on open cases and newly raised criteria are not counted as cycles. Sources: friction and premise reports.
   - "Pre-training by gradient descent works the same way" and the direct-update paragraph. Restrict to plain gradient steps. Trust-region steps that are rejected and checkpoint rollbacks are selection under the article's own definition. Source: premise report.
2. **Teach the robust-comparison mechanism once and remove the opening's duplicate disclaimer** — pass: `readability-and-flow`. Cost: one judgment pass over most of the article. Targets:
   - Cut "The loop itself is not new." (findings 3, 5 and 15 and the synthesis). One novelty disclaimer survives. The readable-store scope restriction stays early.
   - Merge the three overlapping paragraphs after the robust-comparison definition into one paragraph on what the model must do instead of computing value functions. Keep these content points: "This says what the judge must do…", "Even consistent answers can neglect a cost…", the claim that a trial with a cheap way back can close an otherwise open comparison, and the fact that an objection can widen the set. Sources: finding-5 and synthesis opportunity 2.
   - Remove the second statement of the narrowing effect. Keep stochastic dominance as the familiar anchor for ML readers. Source: finding-4.
   - Compress the Gödel machine paragraph and drop its closing recap. Keep the point that the machine can rewrite its utility under proof (findings 4 and 5).
   - Give a forward reference for "the three precedents". Place the consistency caveat after the consistency paragraph (finding-3 info).
   - Split the clause-packed sentences outside excluded passages (finding-12).
   - Split the compound "Where to go next" bullet (finding-16).
3. **Acknowledge removals in the operative-dependence test** — pass: `fix-strategy-taxonomy` with finding-8 (strategy: boundary-case-acknowledged). Cost: one clause. The article defines a change to include removals and recommends pruning, but the test presupposes a retained entry to withhold. Restoring the removed entry is the counterpart test.
4. **Make figurative and coined words literal** — pass: `plain-wording`. Cost: a per-item stop for the operator. Targets: "hard-oracle extreme" (findings 1 and 3), "honest" in both places (finding-6), "act as a bounded decision" and "a third change revises the review check" (finding-14 info).
5. **Gloss "addressable" at first mention and keep the deployed-system framing at the head** — pass: `opening-and-title`. Cost: one judgment pass over the two opening paragraphs. Keep the title as it is (operator must-keep). The opening should say that the deployed system learns by changing retained instructions or criteria, without making fixed weights the headline (finding-1; operator must-keep).

Run order follows depth: narrow-overclaims (2), fix-strategy-taxonomy (2), readability-and-flow (4), plain-wording (5), opening-and-title (6).

## Overclaim classification (support or divergence)

Support (may be narrowed): the items in change 1.

Divergence (must be kept; added to the plan's must-keep):
- Selecting an update needs a comparison among the candidates at hand, including no change, not a single score.
- A robust comparison can select changes without anyone choosing one scalar weighting.
- The bet: a fixed-weight language model can build the preference model from a stated purpose, make the robust comparison and decide the cases it leaves open, including revising its working criteria while the declared objective stays fixed.
- The deployed system, not the model alone, is the unit of learning.
- No completed end-to-end automated run is reported.
- Letting a change stand while its verdict is open is a decision, not a demonstrated gain.

## Passages excluded from every pass (open claim questions)

- The PRODIGY, EURISKO and Harness Evolution paragraphs (grounding).
- The faithfulness sentences in the costs paragraph and the "Unfaithful rationales" hazard bullet.
- The closing falsification paragraph ("If controlled runs show…").
- The sentence that opens "Proof, formula, judgment" ("If selection-based learning over readable stores is not new, why did…").

## Claim questions for the operator

1. **Grounding (defect in support, not in wording).** Source: `kb/reports/state/review/results/kb/articles/deployment-time-machine-learning-llm-selected-updates.md/semantic/grounding-alignment.md`, outcome fail. The PRODIGY and Harness Evolution ingests retain no quotes. EURISKO's retained quotes do not cover the claims that a heuristic "could gain credit by influencing how credit was awarded" and that Lenat corrected judgments of worth. Before editing these paragraphs, run `cp-skill-ground` on each of the three source-side claims. The episode is widely reported in Lenat's EURISKO papers, but verify it from the source. After grounding, two deferred wording fixes become safe:
   - the attachment ambiguity in "a quarter of runs that never reached the proposer" (finding-14)
   - the clause-packed Harness sentence (finding-12)
2. **Faithfulness transfer (defect, one sentence).** Same result file, warn. The linked note concerns a rationale that is unfaithful to a theory's basis. The article uses it for a different claim: that a written rule is not what causally drove behaviour. State that step, or link a note that makes the causal claim. Decide in the same commit whether the hazard bullet should point back to the costs paragraph rather than restate it (finding-3, finding-5 info).
3. **Basis of the falsification condition (defect: two readings).** Source: `.../semantic/underspecified-assertions.md`. "…keep false-positive acceptance, unfaithful rationales, and accretion below the gains it finds" supports two readings:
   - Reading A: net loss on one scale, which is the single score the article rejects.
   - Reading B: the state after the loop is not robustly better than the state before it.

   An open outcome refutes the bet under A but not under B. Reading B is recommended. Also give "those domains" an antecedent (finding-14).
4. **Implied history (defect, one sentence).** Source: `kb/reports/state/review/results/kb/articles/deployment-time-machine-learning-llm-selected-updates.md/kb/instructions/composition-friction-gate.md`; finding-9 info. "Why did earlier AI systems not turn it into a general machine learning paradigm?" implies that the judge was the bottleneck. The article itself later names credit assignment without a chain rule as "the hard problem" and weak proposals as a hazard. Reframe the sentence as a question about how each system decided, or state the bottleneck as a hypothesis.
5. **Independence of the compatible set (choice; no defect shown).** Source: `kb/reports/state/review/results/kb/articles/deployment-time-machine-learning-llm-selected-updates.md/kb/instructions/critique-note.md`; premise report. The reports ask:
   - what, apart from the judging model, fixes which measures are compatible
   - which observable would separate a robust-comparison judge from an LLM judge with one hidden weighting
   - who supplies the measures in the success test

   As scoped, the bet stands without these answers, but its testability depends on them. They may belong in the testing article. Not ranked first.
6. **How much of selection robust comparison decides (choice or extension).** Source: premise-decomposition report. If most selections are decisions on open cases, "without a single score" rests on the judge's open-case decisions more than on agreement across the set. The operator's must-keep says the phrase describes update selection, so the title stays. Whether to say how often reversibility-reshaped alternatives close a comparison is the operator's call.
7. **Dependent's wording (outside this artifact).** `kb/index.md` says the note "argues that" an LLM can supply the comparison. The note presents this as an untested bet, and narrowing the Bitter Lesson sentence keeps the note conditional. Consider a separate commit to the index (role report: `kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/role`). No dependent's relied-on claim is altered by the planned passes.

No stale qualifications were found. The "last three rows … two carry limits" sentence matches the table and the paragraph after it, "five hazards" matches the list, and the companion-drafts status cannot be checked from here.

## Findings and proposals not acted on

- finding-2 (AlphaGo Zero unidentified): the intended technical readers know the system, and adding a factual identification is an addition the passes do not make. The infos on Sutton and Javed are not acted on for the same reason.
- finding-7 (proportion: building the preference model is never illustrated): an extension. It would add worked content (named value functions that disagree on permanent adoption but agree on the trial). The bet stands as scoped. It is a strong candidate for an author revision alongside claim question 5.
- finding-10: routed to claim questions 1 and 2, not to a pass. A fix pass with write scope limited to the article could only weaken or cut the precedents, when the remedy is to retain quotes.
- finding-11: claim question 3.
- finding-13 infos (table row "Training or fine-tuning runs"; the near-limit context framing): these emphasise the typical case without excluding others.
- finding-1 infos (double-loop and representational-form links at first mention; gloss for "harness"): the double-loop term is glossed inline and linked in the reading list. Representational form is recoverable from context. "Harness" sits in the excluded Harness paragraph.
- finding-8 infos (EURISKO-style capture of criteria, the tie case): extensions. Capture of criteria is also raised by the premise report. It is worth an author decision on whether the hazard list needs it, but it is not a pass edit.
- finding-15 info ("belong on the ledger" sentence): it marks the turn from payoffs to costs, so it stays.
- finding-16 infos (reversibility pairing; the weak-proposals scope sentence): both are tied to their lead idea.
- finding-12 info (workshop appositive): readable as narrative.
- Premise report, local comparisons under a drifting preference set: an extension. The accretion hazard already points at whole-store comparison.
- Premise report, LLM-judge bias evidence: an extension.
- Premise report, prevalence of targeted credit assignment: the article already concedes it ("a later failure rarely identifies which entry should change").
- Critique, secondary: the human-supplied purpose under the Bitter Lesson is partly answered by the conditional narrowing in change 1. The rest is an extension.
- Critique, "mixed evidence label" on the title: a choice. The title is kept by the operator's must-keep.
- Synthesis opportunity 1, moving the bet's fuller form (open-case decisions, double-loop, fixed objective) into the opening: a scope choice that changes what the opening promises. Only the duplicate disclaimer is cut. The author may decide to relocate the bet.
