---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Harness code can relocate mechanical and structural work, yet [semantic work can be relocated without being eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md). In open-ended work where new failure modes, commitments, and remedies keep arriving, our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "UNSUPPORTED — Relocation-not-elimination says a meaning-dependent judgment must be paid somewhere; it does not say where. It could be paid upstream at authoring time, by a human, or by a different model, so it does not put the residue on the frozen base LLM. Nor does it show that the residue splits into exactly these three competences. The note never derives the partition: the three are listed, not obtained by subtracting the harness's three job families from the loop's functions. 'Irreducible' also overstates a claim that the Scope section says any offloadable sub-task can shrink and any new bottleneck can enlarge."
  - scope: passage
    quotes: ["These three competences can fail independently and sit at different capability thresholds. A model may follow clear prose procedures while still misdiagnosing noisy traces or overclaiming certainty on incomplete records."]
    reason: "UNSUPPORTED — The supporting sentence is a hypothetical. At most, it suggests that competence 1 can come apart from competences 2 and 3 together. It offers no case where 2 and 3 come apart from each other. 'Different capability thresholds' gets no grounds at all. Diagnosing why a check failed and recognizing that a check is misleading may be the same capacity, so the independence that motivates isolating 'which competence currently binds' is asserted rather than shown."
  - scope: passage
    quotes: ["Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."]
    reason: "THIN — The linked ingest reports that the three no-gain lines were also the three weakest models. It also says that seed plan quality and general capability are confounded, so the result may reduce to 'the harness lever needs a capable enough model'. That supports some base-model floor. It does not show that the floor is semantic rather than a matter of plan quality. It does not map the floor to any of the three competences, and it does not establish 'before the store itself saturates', since the evidence observes no saturation point."
  - scope: passage
    quotes: ["spotting semantic conflicts between prose rules, refactoring them into a cleaner abstraction, or proposing a revised check reduces to competences 2 and 3 applied to the store and its criteria"]
    reason: "THIN — The reduction holds largely because competence 3 was written to absorb it: 'recognize when an existing check is misleading' already names criterion revision. That makes the claim definitional rather than a finding. Refactoring prose rules into a cleaner abstraction is neither diagnosing a failure nor judging a trade-off. Calling it synthesis of 'candidates' stretches competence 2 without an argument that no separate abstraction-forming competence is needed."
  - scope: passage
    quotes: ["Because an LLM that writes code can also build new harness tools for those jobs, the frozen model does not need to keep track of budgets, traces, or regression suites in its head."]
    reason: "HOLDS — The listed jobs are bookkeeping that code can carry once written, and the note credits the tool-building itself to competence 2 ('executable harness code'). The inference is coherent. Its unstated condition is that the harness tools are written correctly; if they are not, the work returns to the model's diagnostic competence."
outcome: report
---

# Friction check: Harness code may offload much of a selection loop, leaving three base LLM competences

**Central claim (one sentence):** In an autonomous selection-based learning loop, harness code can take over enforcement, evidence capture and store bookkeeping, leaving the frozen base LLM responsible for three semantic competences: interpreting unformalized text into action, diagnosing novel failures and synthesizing remedies, and judging unformalized trade-offs.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent partition: mechanical work goes to harness code, and semantic residue stays on the model. "Autonomous" means no human supplies that residue. The note's own wording creates one tension. It calls the competences "irreducible" while its Scope section says the column is revisable in both directions. That is overstatement, not a contradiction, because the note frames the split as a working hypothesis. A second possible conflict also resolves: the model builds the harness that offloads its bookkeeping, but the note assigns that tool-building to competence 2.

## Thinnest joints
The weakest joint carries the note's main step. It moves from "semantic work cannot be eliminated" to "exactly three competences remain on the base LLM". The cited principle supports neither where the work sits nor how many competences there are. The independence claim ranks next. It motivates the human-assisted bootstrap, but its only support is a hypothetical, and that hypothetical does not separate competence 2 from competence 3. The empirical illustration is honestly bounded, but the note's conclusion from it goes beyond the source's own confound. The store-maintenance reduction is thin because the competence definitions were drawn to make it true. The harness-offloading inference holds.

## For the human
Look first at the joint between relocation-not-elimination and "three irreducible semantic competences". Derive the three by subtracting the offloaded functions from an explicit list of loop functions, or drop "irreducible".
