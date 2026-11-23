---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/critique-note.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: c7d41e53ce8849eda10dc80b710c5711
completed-at: '2026-11-22T09:37:45Z'
findings:
- scope: passage
  quotes:
  - derive the preference model from the declared purpose of the work, make the robust
    comparison, and decide the cases it leaves open.
  reason: 'The bet gives one model three roles: it defines the set of compatible measures,
    asserts that the set agrees, and decides when it does not. Nothing outside the
    model constrains the first role. A judge can make any comparison look robust by
    narrowing the set, which the linked necessary-preference note says ''smuggles
    a weighting back in''. The article should say what independent constraint, beyond
    the model''s own reading of the purpose, fixes which measures count as compatible.
    Without one, ''robust comparison'' adds no checkable content to ''an LLM judge
    decided''.'
- scope: passage
  quotes:
  - Those reasons can be checked and challenged one at a time.
  reason: This overstates the source the article cites. The necessary-preference note
    says the factual parts of such reasons can be checked independently, but 'the
    weighing of whose costs count cannot be checked that way.' The weighing is the
    part that makes a comparison robust rather than a single implicit weighting, so
    the sentence should keep the source's limit.
- scope: passage
  quotes:
  - Consistency is part of the bet. A model that approves a change and then approves
    its reversal on the same evidence is equivalent to no set of value functions
  reason: 'The proposed consistency check is necessary but cannot tell a robust-comparison
    judge from a single-scalar judge: a model that applies one hidden weighting also
    passes it. The article names no observable that would separate the bet''s distinctive
    claim, building the preference model and judging robustly, from ordinary pairwise
    LLM-as-judge preference. One candidate: the judge returns ''open'' on exactly
    those pairs where independently fixed admissible weightings disagree, and names
    a weighting that reverses its choice that checks out.'
- scope: passage
  quotes:
  - The changed behavior must score higher under every compatible measure of the declared
    work, not merely pass the check that admitted it.
  reason: The success test assumes a set of compatible measures but does not say who
    fixes it. If people fix it, the test leaves untested the bet's distinctive part,
    the model building the preference model. If the judging model fixes it, the test
    is circular. The article, or its linked testing article, needs to say which party
    defines the measures in an evaluation run.
- scope: passage
  quotes:
  - Third, no single scalar metric had to be invented to compare saved misfilings
    against diffuse context load.
  reason: In the worked example the judge settles the case by adopting the line on
    trial, which is a bounded, reversibility-based decision. It does not show a robust
    comparison deciding anything. As written, this lesson holds for any LLM judge,
    including one with a hidden scalar weighting. The example therefore does not exercise
    the capability the title advertises. The article should either say so or add a
    case the robust comparison actually decides.
contract: report
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7d41e53ce8849eda10dc80b710c5711/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/d6771a319e57b43b530f6f22/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7d41e53ce8849eda10dc80b710c5711/outputs/review.md
raw-output-sha256: c9aaa692c180d316a7053e796298b3b122b796c31bb99268917866bbe87f0ec6
attack-outcome: partially lands
---

# Critique: Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

**Note:** kb/articles/deployment-time-machine-learning-llm-selected-updates.md
**Central commitment:** A fixed-weight language model can do the selection step of double-loop selection-based learning over a readable store: it can derive a preference model from a declared purpose, make a robust comparison and decide the cases the comparison leaves open, so a deployed system can choose its updates without one scalar score.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

An evaluation researcher working on LLM-as-judge, together with a decision theorist, would argue as follows. Once an LLM does the job, "robust comparison" is a relabeling with no operational content. It amounts to an LLM judge giving pairwise verdicts with reasons.

In the decision-analysis method the article borrows (Greco, Mousseau and Słowiński), two things produce robustness:

1. The set of compatible value functions is fixed by preferences stated outside the procedure.
2. Agreement across that set is computed, not asserted.

The article's bet drops both:

- **The model fixes the set.** The model "derive[s] the preference model from the declared purpose." The purpose is a short natural-language objective, and a stated purpose admits many sets of weightings. Nothing outside the model decides which set is the honest one. The linked necessary-preference note warns that narrowing the set to force agreement "smuggles a weighting back in." Under the bet, only the judge could detect that narrowing.
- **The model asserts agreement instead of computing it.** The article concedes that the model does not write down value functions and compute which option wins under all of them (lines 269–274). It offers "reasons that do the same work" instead. Reasons are not unanimity over a set. They are the stated grounds of a single verdict, and the article itself lists unfaithful rationales as a hazard.

So the distinctive claim, *robust* comparison and not just comparison, has no observable that would separate it from the null hypothesis: an LLM with one implicit, context-dependent weighting that sometimes hedges. The proposed consistency test does not separate them. A single-scalar judge also never approves a change and its reversal. The success test ("higher under every compatible measure") needs a set of compatible measures and does not say who supplies it:

- If people supply it, the bet's novel part, the model building the preference model, goes untested.
- If the model supplies it, the test is circular.

The worked example does not exercise the claim either. The judge resolves the routing line by trial adoption, a reversibility-based decision. Its lesson that "no single scalar metric had to be invented" holds for any LLM judge. The opponent concludes that the title's "without a single score" describes the absence of an *explicit* score, not the presence of a robust comparison. The paradigm then reduces to "use an LLM as judge in an edit loop," which is neither new nor addressed by the decision-theory framing.

## How the note engages it

**Partially engaged.** The note anticipates part of the attack:

- **Model does not compute value functions.** It disclaims that the model computes over value functions and offers checkable reasons instead (lines 269–274).
- **Capability, not mechanism.** It says the procedure "says what the judge must do, not how its weights produce an answer." It concedes that "even consistent answers can neglect a cost the stated purpose requires the judge to count" (lines 276–280).
- **Open verdicts stay open.** It reports open verdicts as decisions, not improvements (lines 283–284 and 352–356).
- **Consistency test.** It proposes testing for cycles (lines 286–288).
- **Hazards.** It lists judgment reliability and unfaithful rationales as hazards (lines 383–391).
- **Empirical framing.** It frames the whole claim as a bet with no completed run (lines 375–378). This blunts any charge that it claims success.

The note does not engage the core of the attack, the independence problem: what fixes the compatible set other than the judge. It also gives no observable that tells a robust-comparison judge from a single-weighting judge. Its claim that the reasons "can be checked and challenged one at a time" is stronger than its own cited source. That source says the weighing part of such reasons cannot be checked independently. The worked example's third lesson credits the absence of a scalar to a decision that was actually settled by reversibility.

The attack does not fully land, because the article states a bet rather than a result and says explicitly that the judge need not compute. The bet as worded is still falsifiable in principle. But because no test separates its distinctive part from plain LLM judgment, the decision-theory framing currently adds vocabulary rather than a testable difference.

## Constructive findings

- **Say what fixes compatibility.** State what, independent of the judging model, constrains which measures are compatible. Candidates: stated preferences elicited from people beforehand, retained precedents, or a separate critic whose objections can widen the set. Then say which parts of the preference model the bet claims the model can supply without that constraint.
- **Separate the bet from the null.** Name an observable that tells the bet apart from a single-weighting LLM judge. For example: the judge returns "open" on exactly those pairs where independently fixed admissible weightings disagree, and the weightings it names as reversing its choice really do reverse it when checked.
- **Keep the source's limit.** Change "Those reasons can be checked and challenged one at a time" to keep the necessary-preference note's limit: factual parts can be checked, but the weighing cannot be checked independently of who offered it.
- **Say who supplies the measures in tests.** In the success test, or by an explicit pointer to the testing article, say who supplies the compatible measures in an evaluation run, and whether that leaves the model's preference-building untested.
- **Fix the worked example.** Either reword the third lesson so it credits the trial decision to reversibility, or add one case in which the robust comparison itself decides. An example would be a change that wins under every plausible loss-to-gain ratio.

## Secondary objections (optional)

- **Bitter Lesson placement.** The Bitter Lesson section places the system "on the computation side" once an LLM supplies the comparison. But the declared purpose, and therefore the first constraints on the preference model, stay human-supplied. The bootstrap condition at lines 335–338 covers hand-written instructions and gates, but not the purpose that seeds every comparison. The article could say whether supplying the purpose counts as human domain knowledge under the lesson.
- **Mixed evidence label.** Calling the paradigm "Deployment-Time Machine Learning" while also saying that software teams maintaining handbooks do the same process invites the reply that the only new element is the LLM judge. That is the element the main attack says the article has not yet made testable.
