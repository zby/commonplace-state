---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Once a language model plays the value-function role inside an automated deliberative loop, the system sits on the computation side of the Bitter Lesson."]
    reason: "UNSUPPORTED — Putting an LLM in the judge slot makes the loop automated. Automation alone does not put the loop on the computation side of the Bitter Lesson. That side requires performance that keeps improving as compute grows. The judge's weights are fixed, so its reliability is a ceiling. More proposals, traces and criticism help only if that fixed judge can still tell better from worse edits as the candidate pool grows. Otherwise extra compute mainly adds false-positive admissions, which the note later lists as a hazard. The next sentence lists what compute buys but shows no gain per unit of compute. A second gap goes unaddressed: the judge's competence is itself a product of weight training. A rival reading is that the weights do the Bitter-Lesson work and the store is only a cache."
  - scope: passage
    quotes: ["the bet fails—and weights-only continual learning wins those domains"]
    reason: "UNSUPPORTED — The failure condition supports only one conclusion: a fixed-weight LLM judge cannot keep the hazards below the gains. It does not show that weights-only continual learning wins. Human-in-the-loop deliberative learning, hybrid weight-plus-store systems, stronger future judges and plain non-learning baselines all remain possible. The sentence turns the failure of one bet into a win for one named rival. The note never argues that these two exhaust the options."
  - scope: passage
    quotes: ["That sequence establishes three things."]
    reason: "UNSUPPORTED — The sequence is a hypothetical ('Suppose agents repeatedly misfile...'), so it illustrates the three points but establishes none of them. The first point, that the system adapted, is offered as an established outcome. Yet the note's own later section says such a verdict stays open until later episodes arrive. The third point, that no scalar metric had to be invented, does not follow from the story either. The judge may have weighed the routing fix against context load by an implicit scalar. A narrated outcome cannot show that it did not."
  - scope: passage
    quotes: ["three precedents shows that the bottleneck was always"]
    reason: "THIN — Three selected precedents cannot establish 'always'. The note's own account of EURISKO blames brittle symbolic heuristics and repeated need for Lenat's intervention. That points at the proposer and the substrate, not at the judge. The precedents also leave out other bottlenecks that LLMs removed at the same time: generating proposals in natural language and reading a prose store at all. If those changed too, then the judge being the bottleneck is one hypothesis among several, not what the precedents show."
  - scope: passage
    quotes: ["yet its own data located the stall in what the proposer was not shown"]
    reason: "THIN — The study's data locates the stall in an information gap. That makes 'the stall was not a ceiling of the paradigm' plausible but does not show it. Nothing shows that closing the gap would have resolved the failures the study deferred to weight training. Gains from a lessons file also do not show that those hard failures can be learned the same way. This joint weakens the rival conclusion more than it supports the article's own."
outcome: report
---

# Friction check: Deliberative Learning: Judgment in Place of a Value Function

**Central claim (one sentence):** Learning by proposed, rejectable edits to a readable, addressable store is a distinct learning paradigm, and a fixed-weight language model acting as its on-balance judge makes it an automated machine-learning paradigm that is compatible with the Bitter Lesson.

## Filter
**Filter:** SURVIVES

The claim wants to hold these properties together:
- It is a distinct paradigm, but not a new process.
- It carries no guarantee of improvement.
- Its judge has fixed weights, yet it can revise its own working criteria.
- It is compatible with the Bitter Lesson, yet bootstrapped from hand-written scaffolding.

Each apparent conflict is resolved explicitly:
- Novelty belongs to the machine judge, not to the loop.
- Success is judged separately, through the definition of "learned".
- Criterion revision stays below a fixed declared objective.
- Bitter-Lesson fit is made conditional on outgrowing the bootstrap.

The unanimity requirement in the on-balance definition ("every reasonable measure ... favors it") seems to conflict with acting before a verdict exists. The note reconciles the two by allowing bounded, reversible decisions while the verdict stays open. So one consistent thing remains to be built. Its weak points are the inferences that hold it up.

## Thinnest joints

The two UNSUPPORTED joints rank first because the second level of the thesis rests on them. The computation-side inference is what makes the bet a machine-learning paradigm rather than automated maintenance. The failure condition is what makes the bet falsifiable against a named rival. Both reach their conclusion without arguing for it: the first assumes that a fixed judge's quality scales with compute, and the second assumes only two options exist.

The "establishes three things" joint ranks next. It is local, but it presents an illustration as evidence, and the note's own "open verdict" doctrine contradicts that use.

The precedents joint and the Harness Evolution joint are THIN rather than UNSUPPORTED. Each offers relevant evidence; each overstates what that evidence settles.

A near miss did not make the list: "what lost spanned both forms because what decided the outcome was how the content was made." It shows that weight form did not protect hand-made content. It does not show that readable, computation-made content can win. That gap partly overlaps the first finding.

The example's reversibility licence and the payoffs of an addressable store hold under the skeptical default. Both are scoped and linked to supporting notes.

## For the human
Look first at the Bitter Lesson section's step from "an LLM judges" to "the system sits on the computation side". State what scales with compute when the judge's weights are fixed, and what evidence would show that it scales.
