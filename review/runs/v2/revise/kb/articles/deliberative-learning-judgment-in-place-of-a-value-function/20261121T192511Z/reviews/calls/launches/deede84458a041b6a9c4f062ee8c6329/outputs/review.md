---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Looking at three precedents shows that the bottleneck was always"
      - "What is new is not the loop, but a machine judge that can weigh trade-offs in prose and code without a formal utility function"
    reason: "The historical argument for where novelty sits uses only pre-LLM precedents (Gödel machine, PRODIGY, EURISKO) and skips the contemporary LLM-driven self-editing systems that are the closest rivals for the same territory: OPRO, DSPy, TextGrad, Promptbreeder, Reflexion/Voyager-style skill libraries, ADAS, and the Darwin Gödel Machine. Several of these automate proposal, diagnosis and retention of edits to prompts or code while selecting with a fixed benchmark score, so they are evidence that a capable LLM proposer plus a fixed formula already makes self-editing work as an automated loop. Until the article names this family and says what an on-balance judge adds over it, the claim that the judge slot was 'always' the bottleneck and is the new ingredient is asserted rather than argued."
  - scope: passage
    quotes:
      - "located the stall in what the proposer was not shown"
    reason: "The article's own cited empirical evidence places the bottleneck on the proposer's inputs, not on the judge. Used as it is now, the citation rebuts Sutton/Javed's weights-only conclusion, but it also cuts against the article's thesis that what played the value-function role was the limiting factor. The article should acknowledge this tension or explain why a proposer-side stall is consistent with a judge-side thesis."
  - scope: passage
    quotes:
      - "The changed behavior must score higher across reasonable measures of the declared work"
    reason: "The success test brings back the family of value functions that the judge is said to work 'in place of'. That makes the on-balance judge a cheap proxy for a dominance check over a set of defensible measures, which is multi-objective (Pareto) acceptance with an LLM estimating dominance. The article should say this explicitly and then state what remains distinct as a paradigm, rather than leaving 'in place of a value function' to suggest the judge escapes measures altogether."
  - scope: passage
    quotes:
      - "Second, an on-balance judgment played the role a scalar loss or value function plays in weight training"
      - "Because the edit is one identifiable line and cheap to revert if trouble appears, the judge approves it."
    reason: "The worked example's admission is a bounded decision under an open verdict, justified by reversibility. That is not an on-balance verdict that every reasonable measure favors the change. The later section says this ('the verdict stays open—and the system can still act as a bounded decision'), but the example's takeaway credits 'an on-balance judgment' with deciding admission. That blurs the article's own distinction between judging an improvement and deciding to act."
outcome: report
attack-outcome: partially lands
---

# Critique: Deliberative Learning: Judgment in Place of a Value Function

**Note:** kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
**Central commitment:** Learning by proposed, rejectable edits to a readable, addressable store is a distinct learning paradigm in which an on-balance judgment works in place of a value function, and putting a fixed-weight language model in that judge slot (the empirical bet) makes it an automated machine-learning paradigm compatible with the Bitter Lesson.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent comes from the LLM-as-optimizer literature, such as OPRO, DSPy, TextGrad, Promptbreeder, ADAS and the Darwin Gödel Machine. Their position is that this is not a distinct paradigm. It is black-box optimization over a discrete text or code parameter space, which already exists, and the "on-balance judgment" is a relabelled evaluator.

1. **The judge is a value function under another name.** Any procedure that accepts or rejects candidate edits induces a preference ordering over store states, and that ordering does the selection. The article concedes the role identity: the judgment "played the role a scalar loss or value function plays in weight training." The article's difference is that the judge does not commit to *one* scalar weighting. It accepts only when "every value function defensible from its purpose" agrees. That is Pareto-dominance acceptance over a family of objectives, which is standard multi-objective decision-making, with an LLM estimating dominance. The success test confirms the reduction: a learned change "must score higher across reasonable measures of the declared work." So measures settle the question in the end, and the judge is a cheap, fallible proxy for checking them. This does not make it a new kind of learning signal.

2. **The judge was not the bottleneck; the proposer was.** The article argues that "the bottleneck was always what played the value-function role" from three pre-LLM systems. The contemporary record points the other way. The systems that made automated self-editing of prompts and code work, such as the Darwin Gödel Machine on coding benchmarks and OPRO and DSPy on task metrics, use an LLM to *propose* and *diagnose* while selecting with a fixed benchmark score. That is PRODIGY's "fixed formula" slot. The Harness Evolution study the article cites also "located the stall in what the proposer was not shown." If capable proposers plus fixed formulas already give automated learning, then what is new since 1988 is the proposer. An on-balance judge is an optional refinement, not what turns the loop into a paradigm.

3. **So the two-level claim divides badly.** The first level, a distinct paradigm, reduces to "multi-objective search over a readable parameter space." The second level, that the LLM judge is the enabler, does not engage the evidence that the enabler was elsewhere.

This attack cannot be dismissed in one sentence. The article never names this family of systems, and its own evidence supports point 2.

## How the note engages it

**Partially engaged.**

- The article pre-empts the "not new" charge for the *process*: "The process itself is not new… symbolic learners such as PRODIGY ran a fixed-formula version of it." It also locates novelty only in the machine judge. That correctly concedes the loop. But it argues for the judge's novelty only against pre-LLM precedents (the "Proof, formula, judgment" section), so the contemporary rival in point 2 is unengaged.
- On point 1, the article gives the strongest available answer, though implicitly. The on-balance section explains that many scalar value functions are defensible from one goal and that the judgment leaves the choice open, with open verdicts handled by reversibility. Its definition section also treats a fixed criterion as "the special case." This is a real answer to "just a value function": the asserted difference is refusing to scalarize, not avoiding measures. But the article never states that its success test is a dominance check over measures. The title's "in place of a value function" therefore overstates the difference and invites the reduction.
- The double-loop element partly answers point 2. The article bets on an LLM that revises "the working criteria", meaning gates, validators and review checks, which benchmark-selected systems like the Darwin Gödel Machine do not do. If developed, this is the article's best ground: a fixed benchmark cannot revise itself, and the article's "revising an improvement objective" link marks that limit. But the article presents double-loop revision as part of the bet, not as the explicit differentiator from contemporary benchmark-driven loops.
- The Harness Evolution citation is used only against the weights-only rival. Its proposer-side implication goes unaddressed.

## Constructive findings

- Name the contemporary LLM-driven self-editing family (OPRO/DSPy/TextGrad, Promptbreeder, ADAS, the Darwin Gödel Machine, skill-library agents). State what an on-balance, criterion-revising judge adds over proposer-plus-fixed-benchmark loops. The likely answer is criterion revision and work where no adequate fixed benchmark exists. Without this, "the bottleneck was always what played the value-function role" is unargued.
- State that the on-balance judgment is a non-scalarizing dominance judgment over a family of defensible measures, and that the success test checks it against those measures. Then say why that still counts as a distinct paradigm rather than multi-objective search with an LLM evaluator. Candidate grounds are the readable addressable substrate, targeted correction, and criterion revision inside the loop.
- Reconcile the Harness Evolution evidence with the judge-side thesis. Either acknowledge that proposer inputs can be the binding constraint, or explain why the judge slot remains the paradigm-defining one even so.
- Make the worked example's takeaway match its mechanism. The admission was a reversibility-justified bounded decision under an open verdict, not an on-balance verdict of improvement.

## Secondary objections (optional)

- **Inspectability moves rather than disappears.** The store is legible, but the selection signal is now an opaque fixed-weight network. The article lists "judgment reliability" and "unfaithful rationales" as hazards, but the comparison table still credits deliberative learning with direct inspectability, and it does not note that the judge's reasons are subject to the same faithfulness limit the article cites for stored rules.
- **Bitter Lesson placement.** The judge's competence comes entirely from pretraining, which is weight learning. The article's compatibility argument rests on deployment-time compute buying more proposals and criticism. That is defensible, but a weights-only advocate would say the scaling term that matters still sits in the weights. The article's bootstrap condition answers human scaffolding, not this point.
- **Falsification condition is one-sided.** "The bet fails—and weights-only continual learning wins those domains" treats the two as exclusive. The bet could also fail because proposer-plus-fixed-benchmark loops suffice, leaving the judge unnecessary rather than inadequate.
