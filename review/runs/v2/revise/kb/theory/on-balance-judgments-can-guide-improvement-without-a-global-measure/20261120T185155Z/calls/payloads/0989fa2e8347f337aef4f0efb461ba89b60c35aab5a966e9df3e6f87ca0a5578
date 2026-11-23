# Assessment: On-balance judgments can guide improvement without a global measure

Purpose (as supplied): Explain how on-balance judgments guide decisions without a global measure, and where analysis helps or stops.

## What reads well

The worked cases are distinct and well matched to the claim: the `random.py` message comparison against the whole-release 3.11 judgment shows how changing the alternative changes what evidence can settle, and the `AGENTS.md` line turns the reversal rule into a decision with three outcomes.

## Ranked changes

1. **Make the claim visible before the cases pile up, and put the library case where it does its work.** Readability-and-flow. Cost: one paragraph moved, one sentence added, two sentences cut.
   - After the opening Python 2/3 example, add one general sentence stating both halves of the claim. First half: reasons naming what changed, for whom and why can justify a preference without a global score. Second half: an unknown is worth investigating when a plausible answer could reverse the preference. The sentence must keep the reversal rule scoped to the decision at hand, as the body does. Sources: synthesis opportunity 2; `structural/general-before-specific` (finding-10); `kb/types/note` info item.
   - Move the library-hours paragraph out of the 3.11 section into "What analysis can settle", as the illustration for "Who gains, and who bears the loss?". Shorten that bullet's gloss so it refers back to the case. Cut "Asking for another month of counts would miss the disagreement." Fold the transfer gloss into a clause, but keep an explicit marker that the case is hypothetical. Keep both purpose-dependent branches. Sources: synthesis opportunity 1; `detail-overhang` (finding-3).
   - Fix sentences that need a second reading. "even on the first name" collides with the idiom for a given name: say the ASCII name. "a longer table … Compare the whole table" has no antecedent in the `AGENTS.md` paragraph: name the `AGENTS.md` table. Delete the signpost "This distinction guides a decision." Sources: `sentence/parsing-ambiguity` (finding-8); `sentence/stock-phrases` (finding-9).
2. **Narrow two overclaims.** Narrow-overclaims. Cost: two sentences.
   - "Those reasons can be checked independently of who offered them." This is true of the factual reasons, which work changed and for whom. It is not true of the weighing, including "whose costs count", which can be criticized but not verified. The next sentence ("makes a judgment criticizable") already has the accurate form. Sources: critique report; premise-decomposition report.
   - "The compatibility cost falls on identifiable callers". Narrow this to the losses a team can find by testing its dependencies before moving. Untested paths and downstream users are not identifiable this way. Source: premise-decomposition report.

## Sentence a hostile reviewer would attack first

"A partial order can represent the preferences we can defend under a consistent set of priorities." Pairwise on-balance judgments need not be transitive, and a partial order requires transitivity. The hedge that follows concedes instability, not intransitivity. See the claim questions below.

## Overclaim candidates: support or divergence

- "Those reasons can be checked independently of who offered them." Support. It may be narrowed (change 2).
- "The compatibility cost falls on identifiable callers". Support. It may be narrowed (change 2).
- "**On balance, yes.**" (the 3.11 default). Divergence. Keep it: it is the note's worked judgment, and its defeating condition is already stated.
- The objective sentence, "For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance." Divergence. Keep it verbatim: four dependents rely on it through the section anchor (role report).
- "This is a practical commitment about the work we value, not a claim that every project should use the same measure." Divergence. The operator's must-keep list already covers this distinction.
- "For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice." Divergence. It is on the operator's must-keep list.
- "Even a perfect attendance count would not decide which hours to keep." Divergence. This is the library case's point.

## Stale qualifications

None found. The body still uses the words its qualifications refer to, and no cross-note reference points at the wrong item.

## Claim questions for the operator

Each of these is a defect or a choice that one or two sentences could address, or a choice I do not rank first. The passes are scoped away from these passages.

1. **The partial order needs transitivity.** Passage: "A partial order can represent the preferences we can defend under a consistent set of priorities. It describes the limits of the ranking; it does not do the weighing or guarantee that a single stable ranking exists." Case: each pairwise judgment can turn on the dimension that differs most for that pair. Speed favours A over B, compatibility favours B over C, and library support favours C over A. That is a cycle, not a partial order. One of two sentences would fix it: state transitivity as a condition for the representation, or describe the judgments as defended pairwise preferences that need not compose. Kind: defect, correctable in one sentence. Reports: `kb/reports/state/review/results/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md/kb/instructions/premise-decomposition-gate.md` and `.../composition-friction-gate.md`.
   - In the same paragraph, the redundancy finding proposes trimming "does not do the weighing" (`.../kb/instructions/compression-bundle/marginal-value-redundancy.md`). The synthesis asks whether the paragraph should move next to "What analysis can settle". I hold both until this question is decided.
2. **Some reversing unknowns cannot be investigated, and some reversals come from the weighting.** Passage: "**For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice.**" and "If the evidence supports only the routing gain, leave the overall judgment open." Case: the note itself says an estimate of future use "cannot settle" it. An unknown can reverse the choice and still be beyond investigation, and "leave the overall judgment open" does not say what to do when a decision is due. Separately, whether an answer reverses the choice depends on the weights. A preference that flips between acceptable weightings is a value disagreement to escalate, not an unknown to investigate; the library case already shows this. One or two sentences would close both gaps. The rule itself stays, as the must-keep list requires. Kind: a defect at the boundary the description promises to cover. Sources: `.../semantic/completeness-boundary-cases.md` (finding-7, warn; it responds to `fix-strategy-taxonomy`, but the fix adds a claim, so I leave it to the operator rather than planning a pass); critique report `.../kb/instructions/critique-note.md`.
3. **The objective reads as a ratio.** Passage: the objective sentence. Case: "knowledge work for the human judgment spent" reads as output per unit of judgment, a scalar in form, which the title disclaims. A separate following sentence could say that the objective fixes the direction of preference and is not computed as a score. The objective sentence itself must stay unchanged for its four dependents. The premise report raises a related point: antecedence comes from the per-judgment reasons, not from the objective's wording. Kind: choice; no contradiction is shown. Reports: `.../kb/instructions/critique-note.md` and `.../kb/instructions/premise-decomposition-gate.md`.
4. **Where the priorities are recorded.** The critique and premise reports ask the note to say where the "consistent set of priorities" is fixed before a change is judged, and that reversing an earlier judgment must name the priority that changed (the oscillation case). Kind: extension that borders on a defect. It connects the note to the antecedence condition in its grounding note. Raise it with item 1.
5. **Move the Commonplace declaration to `kb/reference/`.** `kb/theory/COLLECTION` (finding-5, `.../kb/theory/COLLECTION.md`) proposes this. Kind: choice, a split; no defect is shown. I do not rank it first. The section anchor is on the must-keep list, and four dependents link to it (role report `kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/role`). The operator may decline it.

## Findings not acted on

- `accessibility/undefined-terms` (finding-1, "marked heads"). The gloss would help, but the sentence's point (who relies on the heads to stop searching) survives without the mechanism. The fitting pass, abstractions, ends the run for per-item decisions before the higher-value flow pass. This is a cheap later fix.
- `accessibility/unidentified-references` (finding-2, Commonplace unidentified). The note is a Commonplace theory note read inside this KB, and the first mention is the heading and the objective sentence that dependents rely on. The value is low against the purpose.
- `compression-bundle/marginal-value-redundancy` (finding-4). Its first item, cutting the "practical commitment … not a claim that every project should use the same measure" sentence, conflicts with the must-keep list. Its second item, the "does not do the weighing" trim, is held under claim question 1. Its info item, the bullet glosses, is partly handled by the library move.
- `compression-bundle/detail-overhang` info item (timing protocol). Kept: the protocol is what makes a local measurement credible.
- `kb/types/note` (finding-6, `## Scope` section). Gathering the limits under one heading would separate each qualification from the claim it qualifies, against the KB's rule to keep conditions next to their claims. No plan entry is available for this finding.
- `semantic/completeness-boundary-cases` (finding-7). This is claim question 2.
- Friction report, 3.11 prevalence ("On balance, yes" rests on rare blockers). Extension. The note already states the defeating condition and says the checks illustrate rather than survey. The critique report also judges this answered.
- Friction report, the library transfer is asserted, not shown (asks for a KB case where a higher total hides a party's loss). Extension. The library move folds the transfer gloss into a clause.
- Premise report, investigation-rule plausibility ranges (bounding the range is often the first investigation). Extension. Handle it with claim question 2 if the operator takes it up.
- Synthesis opportunity 3 (consolidate the weighting limit, relocate the partial-order paragraph). Held under claim question 1.

## Dependents

The role report shows that dependents rely only on the anchor section's heading, the objective sentence, its rationale, the automation sentence and the factory-requirement boundary. No planned pass touches those passages. The library move, the thesis sentence and the two narrowings reach no dependent.
