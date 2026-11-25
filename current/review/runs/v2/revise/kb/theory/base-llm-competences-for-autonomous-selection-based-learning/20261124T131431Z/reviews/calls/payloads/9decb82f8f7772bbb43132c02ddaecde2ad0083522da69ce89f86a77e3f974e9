---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "where the three weakest tested models produced no held-out gains under the same harness-evolution loop that improved stronger models"
    reason: "The cited evidence shows a different floor from the one the note claims. In the linked ingest, the loop's diagnosing and proposing were done by a frontier proposer (Kimi K3), and acceptance used fixed judge thresholds. The weak Qwen/Gemma models were the task executors. The ingest also says their harness gains raised delivery while 'the freed trajectories landed in F4' (poor plan content). So the evidence shows that a strong loop operator could not lift a weak executor's object-level plan quality. It does not show a floor in any of the three loop competences, which the paper's design held at frontier strength. The ingest also notes that 'model too weak' is confounded with the paper's rule, and that the paper places the ceiling in the loop's evidence package. Either recast the paragraph as evidence of an executor-capability floor, and say whether that floor is a fourth binding constraint or outside the note's scope, or drop it as support for the three-competence split."
  - scope: passage
    quotes:
      - "These three competences can fail independently and sit at different capability thresholds."
    reason: "This is the split's main empirical content, and the note asserts it without evidence or a stated test. The rival view holds that LLM capabilities vary mostly along one general factor, as in observational-scaling analyses that place benchmark results in a low-dimensional capability space. On that view, competences 1–3 rise and fall together, and the split only says that the model must be strong enough. The single example ('follow clear prose procedures while still misdiagnosing noisy traces') is hypothetical. Name the dissociation that would support the split: matched tasks on which one model clears one competence and fails another. Also name what would count against it: the competences track one capability ordering across models. Otherwise, hedge the sentence as a conjecture in its own right."
  - scope: passage
    quotes:
      - "our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"
    reason: "The linked note on semantic work supports only that these judgments must be paid for by some semantic processor, upstream or elsewhere. It explicitly allows offloading 'onto another processor'. It does not support the claim that they must sit on the base LLM. A separately trained diagnostic model, an ensemble of other models, or a human checkpoint could also hold them. State the boundary condition that puts the competences on this model, such as a single frozen model as the only semantic processor inside the autonomous boundary. Otherwise, 'irreducible' and 'on the frozen base LLM' claim more than the cited grounding supports."
  - scope: passage
    quotes:
      - "spotting semantic conflicts between prose rules, refactoring them into a cleaner abstraction, or proposing a revised check reduces to competences 2 and 3 applied to the store and its criteria"
    reason: "Competence 3 is defined as weighing consequences 'against stated commitments'. Criterion revision changes what governs later decisions. The reduction therefore holds only in the KB's narrower double-loop sense, in which the working criterion changes and the declared objective stays fixed and serves as the reference. Say so; otherwise a reader taking double-loop in Argyris's sense will see competence 3 judging the very commitments it is defined against."
outcome: report
attack-outcome: partially lands
---

# Critique: Harness code may offload much of a selection loop, leaving three base LLM competences

**Note:** kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
**Central commitment:** Once harness code takes over enforcement, evidence capture and store bookkeeping, an autonomous selection-based learning loop still needs three separable semantic competences from the frozen base LLM. These are interpreting unformalized text into action, diagnosing novel failures and synthesizing candidate remedies, and judging unformalized trade-offs while recognizing when evidence is missing.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

An informed opponent would take the general-capability-factor position. Observational-scaling work finds that LLM benchmark performance lies in a low-dimensional capability space, with one principal component explaining most of the variance across models. On that view, the three-way split records no discovery about where the base model binds. It renames the generic anatomy of any proposal-selection loop: consuming retained content, proposing changes and evaluating them. Every semantic step a loop could need falls into one of those three bins by construction. The bins therefore cannot be shown incomplete, and naming them adds no information. The only empirical claim the split makes is that the competences "can fail independently and sit at different capability thresholds". That claim is what would give the split diagnostic value for a human-assisted bootstrap, and the note gives no evidence for it.

The opponent then turns the note's own evidence against it. The cited Harness Evolution paper kept the loop-operating competences at frontier strength: a Kimi K3 proposer did the diagnosis and proposals, and acceptance used fixed judge thresholds. The weak models were only task executors. Their harness gains raised delivery, so they apparently followed the process instructions. The added trajectories then failed on plan content (F4). So the one floor the note can point to involves none of the three competences. It is the executor's object-level capability, which a strong loop could not raise through harness edits. The ingest adds that the paper places the ceiling in its evidence package, a property of the harness, and that its no-gain lines are confounded with general model weakness. That cuts both ways for the note. A single "too weak" factor explains the data without three competences. The data also point to a binding constraint the list omits.

## How the note engages it

Partially engaged. The note calls the split a **working hypothesis** in the opening and in Scope. It allows that sub-tasks may move into harness code and that bottlenecks found in practice may add to the list. It asks "which of the three competences binds first" as an open question. These hedges answer the charge that the list is meant to be exhaustive. They do not address the single-factor alternative. The independence sentence is stated as fact, and its one illustration is hypothetical. The note also does not engage the mismatch between its evidence and its claim. The illustration paragraph reads the cited paper as showing a base-model floor for the loop, but the paper's design kept the loop operator strong. The "irreducible … on the frozen base LLM" wording also goes beyond its grounding note, which explicitly allows semantic work to move to another processor.

## Constructive findings

- Recast or drop the Harness Evolution paragraph. As cited, it shows a floor in executor plan quality under a frontier proposer, not a floor in competences 1–3. If the executor floor matters, either name it or explicitly scope it out of the note.
- Make the independence claim testable or hedge it. Name the dissociation that would support it, such as matched tasks where one model clears one competence and fails another. Name the observation that would collapse the split, namely that all three track one capability ordering across models.
- State the boundary condition that places the competences on the base LLM rather than on any semantic processor. An example would be a single frozen model as the only semantic processor inside the autonomous boundary.
- Tie the criterion-revision reduction to the KB's narrower double-loop sense: the declared objective stays fixed as competence 3's reference while the working criterion changes.

## Secondary objections (optional)

- The ingest reports that enforcement components (gates, hard blocks) mostly fell within noise in ablations. The gains came from capability-granting components: a lessons file, a state ledger and invented tools. That fits the note's offloading list less well than the note implies. The harness components that mattered were content the model read, not the enforcement and bookkeeping the note assigns to code. This does not refute the split, but it weakens any implication that offloading machinery to code is what lowers the base-model floor.
- "Clearing these competences is proposed as necessary" uses a threshold image ("clearing") without saying what level counts as clearing for open-ended work. A reader cannot tell when the necessary condition is met.
