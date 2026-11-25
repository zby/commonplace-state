---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "three irreducible semantic competences"
    reason: "DOUBTFUL — Premise (tentative, but stated as the exhaustive residue): after harness offloading, the semantic work left on the model is exactly interpretation, diagnosis/synthesis, and trade-off judgment. — Counterexample: object-level task competence, meaning doing the domain work well enough that selection has successes to select, is in none of the three. Competence 1 covers following stored procedures, not producing a good plan or patch. The note's own cited evidence shows this: in the Harness Evolution ingest the unreduced failure class is F4, a delivered plan that is poor, and the weak lines gained delivery while the freed trajectories landed in F4. That floor is on what the actor model writes, not on any of the three loop competences. The Scope bullet allows the list to grow, so this is a missing item, not a broken mechanism. — LOCAL — instance"
  - scope: passage
    quotes:
      - "remain on the frozen base LLM"
    reason: "DOUBTFUL — Premise (unstated, universal): the semantic residue falls on one frozen base model, the same one that acts. — Counterexample: the linked relocation note says a judgment can be offloaded to another processor. The cited paper's loop does exactly that. Kimi K3 is the proposer that reads evidence and synthesizes edits (competence 2), while Qwen 4B/9B act under the harness (competence 1). In an autonomous system the competences can sit on different models, so the floor is per role, not one floor on 'the' base LLM. The repair is to name the role that carries each competence. The mechanism stays semantic work on some model. — LOCAL — instance"
  - scope: passage
    quotes:
      - "routing and loading the relevant artifacts"
    reason: "DOUBTFUL — Premise (stated plainly as something harness code can take over): context assembly, including choosing the relevant artifacts, is mechanical harness work. — Counterexample: relevance for a novel task is a meaning-dependent judgment. The linked relocation note says rule-based selection works only where a pre-existing signal encodes semantic work already paid upstream. In the open-ended regime the note invokes, where new failure modes keep arriving, no such signal exists for the new case, so someone has to judge relevance on the model side. The same applies to 'annotating telemetry coverage gaps', which overlaps competence 3's 'recognizing missing evidence'. The offload list needs the condition 'given an upstream-paid signal', or relevance selection needs to move into the LLM column. — LOCAL — instance"
  - scope: passage
    quotes:
      - "Clearing these competences is proposed as necessary for operating the loop autonomously"
    reason: "DOUBTFUL — Premise (proposed necessity): each of the three competences, including competence 2's causal diagnosis of novel failures, is necessary for an autonomous loop. — Counterexample: variant-and-select loops learn autonomously without a formulated causal diagnosis. The linked ingest classifies its harness loop as 'variant-and-select with a bare failure signal', with no stated theory of the task, and it still produced held-out gains (+0.133 for 4B, +0.119 for 9B). The KB's own conjecture is that diagnosis yields more learning, not that learning requires it. The open-ended qualifier blunts this but does not remove it: a blind proposer under competence-3 selection could still make progress. A repair would recast diagnosis as a condition for efficient learning, or define 'diagnosis' loosely enough to include implicit proposal from worst cases. — LOCAL — instance"
  - scope: passage
    quotes:
      - "reduces to competences 2 and 3 applied to the store and its criteria"
    reason: "DOUBTFUL — Premise (stated without hedge): store maintenance and criterion revision need no competence beyond 2 and 3. — Counterexample: refactoring prose rules into a cleaner abstraction is generative compression with no failure to start it. Competence 2 is defined as turning 'an unanticipated failure and its trace' into a diagnosis and remedies. Competence 3 weighs and withholds rather than abstracts. Proactive consolidation of a store that is not yet failing falls between the two definitions. The repair is to widen competence 2's trigger beyond failures, or to add the case. — LOCAL — instance"
  - scope: passage
    quotes:
      - "an inadequate base model can block outer-loop learning before the store itself saturates"
    reason: "DOUBTFUL — Premise (bounded illustration): the cited weak-model null lines show a base-model floor relevant to these competences, reached before store saturation. — Counterexample: in that paper the loop competences (diagnosis, edit synthesis, judgment) ran on the proposer and the fixed judge, not on the weak models. What the weak models lacked was object-level plan quality. The ingest also flags that the no-gain lines are confounded with general model weakness, and that the paper places the ceiling in the loop's evidence package. The evidence supports 'some base-model floor exists'. It does not support a floor on the three named competences. — LOCAL — instance"
  - scope: passage
    quotes:
      - "These three competences can fail independently and sit at different capability thresholds"
    reason: "DOUBTFUL — Premise (possibility claim): the three competences can fail independently, so transfer tests can isolate the binding one. — Reason: the dissociation holds in one direction only. Competences 2 and 3 both consume competence 1's operation: reading unformalized traces, commitments and procedures. A model that fails competence 1 under realistic context load will also show up as failing 2 and 3, so tests of 2 and 3 are confounded unless competence 1 is controlled first. The note's example (follows procedures, misdiagnoses traces) is the direction that does dissociate. The repair is to state the dependency order for the bootstrap. — LOCAL — instance"
  - scope: passage
    quotes:
      - "semantic work can be relocated without being eliminated"
    reason: "HOLDS — Premise (imported from the linked note): a meaning-dependent judgment can be placed but not removed at the point of use, except where it was paid upstream for the case or its regularity. — The hunt for a defeater found only amortization: regularities paid once upstream so that use-time work becomes mechanical. The note blocks this by limiting its claim to open-ended work where new failure modes, commitments and remedies keep arriving. Under that condition the residue cannot be fully pre-paid, so the premise holds as applied."
  - scope: passage
    quotes:
      - "the frozen model does not need to keep track of budgets, traces, or regression suites in its head"
    reason: "HOLDS — Premise: once harness tools exist, bookkeeping state such as budgets, traces and regression suites can live outside the model's context. — The hunt for a defeater turned up the case where a model-written tool is buggy and reports false state. That case is caught by competence 3's 'recognize when an existing check is misleading', so it moves the semantic load to a named competence rather than defeating the premise. Ordinary harness practice (budget enforcement, trace logging, regression runners) confirms that the state can be externalized."
outcome: report
---

# Premise decomposition: Harness code may offload much of a selection loop, leaving three base LLM competences

**Register:** claim
**Central commitment (one sentence):** In open-ended autonomous selection-based learning with frozen weights, harness code can absorb enforcement, evidence capture and store bookkeeping, and the semantic residue that remains on the base LLM is exactly three necessary competences: interpreting unformalized text into action, diagnosing novel failures and synthesizing remedies, and judging unformalized trade-offs and missing evidence. Store maintenance and criterion revision reduce to the last two.

## Premises and counterexamples

The claim is a working hypothesis, and its Scope concedes that items can move between the harness and LLM columns. So no premise is read as an impossibility result, and every failure found is LOCAL. The commitment still consumes four kinds of premise, and each kind has at least one doubtful node:

- **Offload boundary.** What harness code can take over. The offload list includes relevance-based context assembly, which by the KB's own relocation note needs an upstream-paid signal that the open-ended regime lacks.
- **Residue.** Exactly three competences, all on one model. The residue omits object-level task competence. It also assumes the semantic roles sit on a single frozen model, though the cited system splits them across a proposer and an actor.
- **Necessity and reduction.** Each competence is necessary, and the store-level and criterion-level work needs no other competence. Necessity is dented for diagnosis by variant-and-select loops that learn without it. Reduction is dented by proactive refactoring with no failure to start it.
- **Separability and evidence.** The three competences dissociate, and the cited paper illustrates a floor. Separability holds in one direction only. The empirical illustration supports a general base-model floor, not a floor on the named competences.

The two premises that hold are the relocation principle, as limited by the open-ended qualifier, and the externalization of bookkeeping state.

## For the human

Look first at the residue's completeness. Both the object-level-competence counterexample and the note's own evidence paragraph point to a floor on the acting model's task output, not on the three loop competences. Fixing that also clarifies which model each competence sits on.
