---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"
    reason: "The inference from 'semantic work can be relocated but not eliminated' licenses only that the three competences stay on some semantic processor. The linked note itself names offloading to another processor as a valid placement. The note does not say whether 'the frozen base LLM' means the single model that executes tasks or any frozen model the loop calls. Under the first reading, proposer/executor and separate-judge designs are counterexamples. Under the second, the residence claim says little beyond 'semantic work needs some LLM'. The note should fix the reading and state what follows from it."
  - scope: passage
    quotes:
      - "where the three weakest tested models produced no held-out gains under the same harness-evolution loop that improved stronger models"
      - "Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."
    reason: "In the cited paper, a fixed external proposer (Kimi K3) did the diagnosis and candidate synthesis, and a judge applied fixed thresholds. The weak models only executed tasks under the harness. Their failure therefore bears on task capability, or at most on competence 1, not on competences 2 and 3. The ingest also says weak seed quality and general capability are confounded, and that freed trajectories landed in F4. The illustration supports a task-capability floor. It is not evidence about the loop competences the note lists and should be described that way."
  - scope: passage
    quotes:
      - "reduces to competences 2 and 3 applied to the store and its criteria"
    reason: "If one model proposes revisions (competence 2) and judges them (competence 3), proposal and evaluation share its errors. The linked scheduler-LLM note says error correction requires decorrelated checks. The note treats this concentration as harmless without arguing it. Selection-based learning needs an evaluation that can reject a change, and that evaluation is weak when it shares the proposer's systematic errors. The note should say whether competence 3 must be decorrelated from competence 2, for example by using another model or held-out tests. It should also say whether that changes the claimed floor."
  - scope: passage
    quotes:
      - "These three competences can fail independently and sit at different capability thresholds."
    reason: "The note asserts independence but gives no evidence or example. Its one example contrasts competence 1 with 2 and 3 together. The boundaries also overlap. Competence 3 includes recognizing 'when an existing check is misleading', which is diagnosis (competence 2). Competence 2 also bundles diagnosis with synthesis, and those could fail separately. Without a separating test, the claim that the split lets a bootstrap 'identify which competence currently binds' is not supported."
  - scope: passage
    quotes:
      - "Any sub-task shown to be reliably offloadable to harness code moves out of the LLM column, and concrete bottlenecks discovered in practice can add to it."
    reason: "The body calls the competences 'irreducible', but the Scope lets the list shrink or grow with any observation. Together, these leave no stated observation that would count against the three-way split rather than revise it. The note should name the result that would refute it, such as a loop that runs autonomously while one listed competence is supplied wholly by code."
outcome: report
attack-outcome: partially lands
---

# Critique: Harness code may offload much of a selection loop, leaving three base LLM competences

**Note:** kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
**Central commitment:** In an autonomous selection-based learning loop, harness code can take over enforcement, evidence capture and store bookkeeping. Three semantic competences remain on the frozen base LLM: interpreting unformalized text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs. Store maintenance and criterion revision need no further competence.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a multi-model agent architect. Examples include the designers of proposer/executor harness-evolution loops (Meta-Harness, AHE-style loops), Co-Harness's critic routing and LLM-as-judge pipelines. Their position is that the residence part of the claim does not follow from its premise and does not match how these loops are built.

1. **The premise fixes only that semantic work stays somewhere.** The note gets the residual competences from the note "Semantic work can be relocated but not eliminated" (`kb/theory/semantic-work-can-be-relocated-but-not-eliminated.md`). That note says a judgment can be placed on "another processor", which it calls offloading. Irreducibility therefore says that some semantic processor must do the work. It does not say that the frozen base model must. Diagnosis can move to a stronger proposer model, judging to a separate judge model, and part of the work to codified regularities paid for upstream. In each case the work stays semantic but leaves the executing model.

2. **Working loops do separate these roles.** In the paper the note cites as evidence, Kimi K3 proposes harness edits. A judge applies fixed thresholds and the proposer's rollback conditions. The small Qwen and Gemma models only act through the harness. Consider the competences the note assigns to the frozen base LLM. A different model performs competence 2. Competence 3 is split between that model's rollback conditions and coded thresholds. The executing model needs only competence 1 plus enough task capability. Read as "the model that executes tasks", the note's claim has a counterexample in its own evidence.

3. **The best design may require the split.** In selection-based learning, the evaluation that can reject a change has value only when its errors are not the proposer's errors. The scheduler–LLM note, which this note cites as grounding, says error correction needs discriminating checks and decorrelated errors. If competences 2 and 3 run on one model, proposal and selection share their blind spots. The architect would therefore argue that the floor applies to the system, not to one frozen model, and that competence 3 should be held by a decorrelated evaluator.

4. **The fallback reading says little.** The note could reply that "the frozen base LLM" means whatever frozen models the loop uses. Then the residence claim becomes "semantic work in an autonomous loop needs some LLM". That follows almost directly from "autonomous" plus the relocation note. What remains is the taxonomy of three competences. The note asserts that taxonomy and does not test it: it gives no evidence that the competences fail independently, and the definitions overlap.

The objection cannot be dismissed in one sentence. Answering it requires the note to choose a reading of "base LLM" and to accept the consequence of that choice.

## How the note engages it

**Partially engaged.** The note does reach for the relocation premise. Its Scope says the split is a working hypothesis and that a sub-task shown to be offloadable "moves out of the LLM column". That concedes movement from the LLM to code. It does not consider movement from one LLM to another, or the decorrelation argument. Humans appear only as a temporary bootstrap that supplies "the missing semantic step", which is offloading to another processor. Yet the note does not apply the same reasoning to autonomous multi-model loops. The cited evidence does not test the commitment. The weak models in that paper never had to diagnose or judge, because a fixed external proposer and judge did that work. Their failure fits a task-capability floor, which the ingest itself names as a confound. It is not evidence about competences 2 and 3.

Part of the commitment survives. Harness code can absorb enforcement, evidence capture and bookkeeping. Semantic judgment does not disappear when this happens. Store maintenance and criterion revision reduce to diagnosis and judgment applied to the store. The attack does not touch these points. It lands on two others: the claim that the residue sits on the frozen base LLM, and the claim that three independently failing competences are the right breakdown.

## Constructive findings

- State which reading of "base LLM" the note means. Under the "model that executes tasks" reading, competences 2 and 3 can be offloaded to other models, and the note should say so. Under the "any frozen model the loop calls" reading, say that the floor belongs to the set of semantic processors in the system. Then explain what the three-way split adds beyond that.
- Say whether competence 3 must be decorrelated from competence 2 so that rejection remains a real check. Use the error-correction grounding the note already cites. Decide whether a separate judge model or held-out tests change the floor.
- Re-describe the Harness Evolution evidence correctly. A fixed proposer and judge did the diagnosis and selection. The three weakest *executing* models produced no held-out gains, and that is confounded with general task capability. This bears on competence 1 or task capability, not on competences 2 and 3.
- Support the independence claim or weaken it. Give one case where competence 3 fails while competence 2 holds, or where competence 2 fails while competence 3 holds. Alternatively, separate "recognize when an existing check is misleading" from diagnosis so that the boundaries stop overlapping.
- Name an observation that would refute the split rather than revise it. One example is an autonomous loop that runs with one listed competence supplied wholly by code.

## Secondary objections (optional)

- "Irreducible" in the body conflicts with the Scope's open-ended list. Under the Scope, every observation can be absorbed by moving an item between columns, so the word overstates the epistemic status the note declares.
- The note excludes the object-level task competence the loop is trying to improve. The cited evidence shows that this competence, not any loop competence, was what blocked the weak models. A sentence separating task capability from loop-operating competences would prevent misreading the floor.
- The assignment of tool-building to harness code is circular. Building new harness tools for budgets, replay and bookkeeping is itself competence 2 ("executable harness code"). The offloading the note describes therefore depends on the competence it says remains. This is consistent with the note but should be stated, because the harness column only grows when competence 2 is present.
