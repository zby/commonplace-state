---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "UNSUPPORTED — the preceding ground, that semantic work can be relocated but not eliminated, establishes only that some semantic residue survives harness offloading. It does not establish that the residue partitions into exactly these three competences, that the list is complete, or that the residue must sit on the frozen base LLM rather than on a human, another model or a retrained one. The note also calls the competences 'irreducible' while its Scope section says any sub-task shown to be offloadable moves out of the LLM column. The note does not reconcile the two, and it never says what would show that one of the three is reducible."
  - scope: passage
    quotes: ["These three competences can fail independently and sit at different capability thresholds."]
    reason: "UNSUPPORTED — the only support is a hypothetical dissociation ('A model may follow clear prose procedures while still misdiagnosing noisy traces'). No observed case, cited result or mechanism shows that the three come apart in practice. The next sentence's payoff depends on this independence: a human-assisted bootstrap can isolate which competence binds only if the competences fail separately. If they share one underlying capability, as the linked ingest's capability confound suggests is possible, the separation buys no diagnostic leverage."
  - scope: passage
    quotes: ["spotting semantic conflicts between prose rules, refactoring them into a cleaner abstraction, or proposing a revised check reduces to competences 2 and 3 applied to the store and its criteria"]
    reason: "THIN — competence 2 is defined around turning an unanticipated failure and its trace into a diagnosis and remedy. Refactoring prose rules into a cleaner abstraction, or noticing that two rules conflict before either causes a failure, has no failure or trace to start from. The reduction therefore depends on reading 'synthesizing candidates' more broadly than the definition states. Criterion revision, the double-loop step, is also asserted to need no separate competence without showing that judging a criterion is the same activity as judging within one."
  - scope: passage
    quotes: ["Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."]
    reason: "THIN — the cited evidence is that the three weakest tested models gained nothing on held-out tasks. The linked ingest notes that seed plan quality and general model capability are confounded there. 'Before the store itself saturates' is not shown: nothing establishes how much headroom the store had for those models. The evidence also maps to no particular competence among the three, so it supports a generic base-model floor rather than the note's three-part split."
  - scope: passage
    quotes: ["Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."]
    reason: "THIN — the conclusion follows from the preceding list of harness responsibilities, whoever writes the harness. The offered 'because', that the LLM can build these tools itself, adds a separate claim: such tools would be built correctly and kept faithful to the store's semantics. That claim moves the burden into competence 2, which the note treats as an open capability threshold rather than a given. The joint holds for a harness that already exists and is thinner for self-built tools."
outcome: report
---

# Friction check: Harness code may offload much of a selection loop, leaving three base LLM competences

**Central claim (one sentence):** In open-ended work, harness code can take over a selection-based learning loop's enforcement, evidence capture and store bookkeeping, but autonomous operation still requires three semantic competences from the frozen base LLM: interpreting unformalized text into action, diagnosing novel failures and synthesizing remedies, and judging unformalized trade-offs and missing evidence.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent picture: mechanical work goes to code, and a semantic remainder stays with the model. Two of its properties pull against each other without contradicting each other. One pair is "irreducible" and "a working hypothesis whose LLM column shrinks as offloading succeeds". Read as "conjectured irreducible", both can hold, although the note's wording does not settle which one it means. The other pair is "autonomous" and "human-assisted bootstrap". This also coexists, because the bootstrap is framed as temporary scaffolding for finding the binding competence, not as part of the autonomous loop.

## Thinnest joints
The two thinnest joints carry the note's distinctive content: the count and placement of the competences, and their separability. The harness-offloading half of the note leans on a linked mechanism note and is comparatively well grounded. The step from "semantic work survives" to "exactly these three, on the base LLM" is not argued in this text. Separability is asserted through a hypothetical, and the bootstrap use case depends on it. The criterion-revision reduction ranks next because it quietly widens competence 2's failure-triggered definition. The empirical illustration is explicitly bounded and offered as illustration, so its confound and its untested saturation clause matter less. The tool-building "because" is thin only for self-built tools; its conclusion holds anyway from the harness list.

## For the human
Look first at the move from "semantic work can be relocated, not eliminated" to "three irreducible competences on the frozen base LLM". Concretize why there are three, why this cut, and what observation would merge, split or relocate one of them.
