---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'This is not a partition into codified versus learned: an adopted model package
    can itself be a codified reference.'
  reason: The opening states only the unidentifiability premise and the hybrid conclusion,
    then ends on an adoption caveat. The title's operative claim (code extraction
    as a bet, then relaxing when scale makes a general component viable) arrives only
    in paragraph five and the second section, and the adoption and prose-convention
    caveats recur three and two times; rewrite the opening to state the codify-and-relax
    thesis plainly, and consolidate the codification-scope caveats once in the definition
    paragraph, keeping only the relaxing paragraph's distinct 'reverses the extraction,
    not symbolic membership' use.
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget.
  reason: 'The formal-results paragraphs pull against the note''s own premise: epiplexity
    implies an advance criterion for which regime a regularity is in, while the note
    says you cannot reliably tell until scale tests it, and the Ebrahimi paragraph
    carries κ measurements and a closing restatement that the argument never uses.
    The author must first decide how epiplexity relates to the unidentifiability premise;
    then cut it, recast it as an open question or partial advance signal, or move
    it out, and reduce Ebrahimi to one sentence of support for the arithmetic regime.'
- scope: passage
  quotes:
  - 'In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution
    is algorithmically determined.'
  reason: The 'bet' section reopens by restating both regime bullets and the opening's
    can't-tell claim, and its link to the proxy-scope conjecture carries a duplicate
    hedge, so the reader rereads the regime analysis before reaching the new contribution
    (vision researchers bet without a working system; spec mining bets from one).
    Fold the safe/risky-bet framing into the regime bullets or the first sentence
    of the vision-researcher paragraph, and keep the conjectural status in a single
    clause, so the section starts at the composition-versus-load-bearing contrast.
outcome: report
description: Retained report review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
criterion-sha256: 0639a8d235bbdf791feaa2f1eae21d28a4131c0fe56e0a15fefe51fa524835cf
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/synthesis/calls/launches/b90403bc245543f38a426b247929e652/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/synthesis/artifact/reviews/f8eda738dc4395c2360568f3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/synthesis
launch: b90403bc245543f38a426b247929e652
completed-at: '2026-11-20T09:18:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/synthesis/calls/launches/b90403bc245543f38a426b247929e652/outputs/review.md
raw-output-sha256: 4538a40407c73b0590c8177c3175b455c9a79ab01d576fda25d69d13045ff7f2
format: 2
---

# Simplification synthesis: Codification and relaxing navigate the bitter lesson boundary

The four checks agree that the core argument is sound and roughly proportionate. Three larger moves would materially improve how fast a reader gets the thesis and how cleanly the argument runs. The first is a front-loading move: surface the thesis and gather the scattered scope caveats. The second requires an authorial decision about the formal-results section before any compression is safe. The third is a fold that removes a recap layer between the regime analysis and the spec-mining contribution.

## Opportunities

### 1. Surface the codify-and-relax thesis and consolidate the codification-scope caveats

- Location: opening paragraph ("This is not a partition into codified versus learned…") through the definition paragraph under "The trade-off depends on which regime you're in", plus heuristic 1's last sentence ("Merely writing the convention in natural language constrains without codifying it.").
- Reader problem: The opening gives the premise and the "hybrids" conclusion but not the title's operative claim. Relaxing, a title term, first appears in the fifth paragraph, and the bet framing waits for the second section. In front of the regime trade-off, the reader instead meets a model-package adoption caveat (stated three times in the note) and a prose-convention caveat (stated twice).
- Direction: Make the opening state the full claim. One possible resolution, not a settled rewrite: "Because you can't tell which regime a decomposition is in until scale tests it, each code extraction is a bet: codify for current leverage, relax when scale makes a general component viable, and prefer specs mined from a working system." Then state the adoption and prose-convention boundaries once, in the definition paragraph, and drop their repeats in the opening and heuristic 1.
- Combines: core-claim-obscured (opening caveat; definitional scope work ahead of the claim; late arrival of relaxing); detail-overhang (repeated codification scope caveats); marginal-value-redundancy (model-package caveat stated three times; prose-convention caveat in heuristic 1).
- Preserve or decide: Preserve the distinction between codification by adoption and the code-extraction case this note covers. Preserve the relaxing paragraph's claim that relaxing reverses the extraction, not symbolic membership; that sentence does distinct work and should stay. Preserve the point that practical systems are hybrids rather than a codified/learned partition, even if the adoption sentence that currently carries it moves. Decide whether the "constrains without codifying" contrast in heuristic 1 adds a distinction (constraining versus codifying) that the definition paragraph lacks; if it does, move it there instead of deleting it.

### 2. Resolve how the formal results relate to the unidentifiability premise, then compress them

- Location: "Every code-extraction codification is a bet", the two paragraphs beginning "Two formal results help bound when codification bets are safe" and "The induction bias results", plus the matching Sources annotations.
- Reader problem: The note's founding premise is that you cannot reliably tell which regime you are in until scale tests it. The epiplexity paragraph offers an information-theoretic criterion that would, in principle, separate structural regularities from accidents in advance. The note never reconciles the two, so the reader cannot tell whether the premise has been weakened. The Ebrahimi paragraph supports the arithmetic regime, but its κ values, supervision-format sweep and CoT figure go unused. Its closing sentence restates the paragraph's opening claim, and the Sources footer makes the same translation a third time.
- Direction: Once the author has decided, either cut the epiplexity paragraph, recast it as an open question ("could a computational-learnability measure separate structural from accidental regularities before scale tests them?"), or move it to a separate note or workshop lead on advance criteria for codification bets. Reduce Ebrahimi to one sentence: architectural step-by-step bias stays an advantage for calculator-class tasks, so arithmetic-regime bets persist under scaling. Leave the measurements to the source.
- Combines: branch-bloat (epiplexity branch works against the premise; Ebrahimi experimental detail); detail-overhang (κ measurements); core-claim-obscured (κ figures as apparatus); marginal-value-redundancy (Ebrahimi closing restatement).
- Preserve or decide: This is a prerequisite choice, not a compression edit. The author must decide whether the note claims that regimes are unidentifiable in advance, or only that they are hard to identify and that partial advance signals such as epiplexity may exist. These are materially different theses. Keeping epiplexity as an advance criterion softens the premise and the description's "can't identify"; cutting it keeps the premise intact. Whatever happens to the detail, preserve the Ebrahimi claim that arithmetic-regime structure persists under scaling, since it is the note's only evidence that the "safe" side of the bet is more than safe-for-now.

### 3. Fold the regime recap so the bet section opens on its new contribution

- Location: "Every code-extraction codification is a bet", from "That scale in fact selects on this property is conjectural, not established." through "Most practical codification happens in the blurry zone between them, where you can't tell which regime you're in."
- Reader problem: Between the bet framing and the vision-researcher contrast, the section restates both regime bullets as safe versus risky bets, then repeats the opening's can't-tell claim. The conjecture link also adds a second hedge to a sentence that already calls the diagnosis a conjecture. The reader rereads the regime analysis before reaching the section's actual contribution: the vision researchers bet on composition without a working system, while spec mining bets from one, which narrows the bet.
- Direction: Carry "safe/risky bet" as a clause on the regime bullets, or in the first sentence of the vision-researcher paragraph, and delete the recap paragraph. Keep the conjectural status in one clause, for example "conjecturally", inside the sentence that cites the proxy-scope diagnosis. The section then runs: bet defined → vision researchers lost the composition bet → spec mining narrows it → relaxing signals detect losing bets.
- Combines: marginal-value-redundancy (regime recap; duplicate hedge); core-claim-obscured (bet framing delayed relative to the regime setup).
- Preserve or decide: Preserve the "blurry zone" sentence's prevalence claim that most practical codification sits between the regimes. The opening does not say this; it says only that the regimes cannot be told apart. Move the claim if the paragraph goes. Preserve the explicit epistemic status that scale selecting on proxy scope is conjectural, not established. Only the duplicate wording should go, not the hedge itself.
