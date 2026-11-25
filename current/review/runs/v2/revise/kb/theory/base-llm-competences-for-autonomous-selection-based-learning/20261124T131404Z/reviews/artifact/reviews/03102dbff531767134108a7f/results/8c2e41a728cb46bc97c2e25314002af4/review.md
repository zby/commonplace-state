---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - three irreducible semantic competences remain on the frozen base LLM
  reason: 'DOUBTFUL — (universal, unstated) the irreducible semantic residue must
    sit on one frozen base LLM, the same model that executes the loop — the note''s
    own grounding note on semantic work says a meaning-dependent judgment can be offloaded
    to another processor, and the source the note cites runs exactly that split: a
    fixed Kimi K3 proposer reads the evidence package and proposes edits while Qwen
    4B/9B executes the tasks. Diagnosis and candidate synthesis (competence 2) and
    acceptance judgment can therefore sit on a different, stronger model, a judge
    ensemble or a verifier, while interpretation under load (competence 1) stays on
    the executor. The residue is irreducible for the system, not necessarily for one
    model — LOCAL (restate the floor per role or as ''the models the loop uses'';
    the three-competence mechanism survives) — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — (universal, unstated) the three competences exhaust the semantic
    residue the loop needs once harness code takes the mechanical work — at least
    two candidates fall outside the list. First, relevance selection for novel material:
    the note assigns ''routing and loading the relevant artifacts'' to harness code,
    but rule-based routing needs a pre-existing signal, so deciding what is relevant
    to a new failure or a new task is a semantic judgment that none of the three competences
    names. Second, object-level task competence: the cited source''s floor is weak
    executors whose freed trajectories land in poor plans, which is neither interpretation
    of a procedure, diagnosis nor trade-off judgment. The Scope bullet already allows
    bottlenecks to be added, so the count is the fragile part, not the split — LOCAL
    — instance'
- scope: passage
  quotes:
  - Clearing these competences is proposed as necessary for operating the loop autonomously
  reason: 'DOUBTFUL — (necessity, conditioned on open-ended work) each competence,
    including causal diagnosis, is necessary for an autonomous loop to operate — variant-and-select
    loops run autonomously and produce held-out gains without a formulated diagnosis:
    the cited source''s proposer saw metrics and worst cases, not a stated causal
    account, and still lifted 4B and 9B. Such loops run on fixed benchmarks, so they
    may sit outside the note''s open-ended condition; but there the necessary part
    of competence 2 shrinks to candidate generation, with diagnosis acting as a quality
    lever (as the linked diagnostic-richness note frames it) rather than a precondition
    — LOCAL (split competence 2 into necessary generation and quality-raising diagnosis,
    or state that necessity holds only where new failure modes arrive) — instance'
- scope: passage
  quotes:
  - the three weakest tested models produced no held-out gains under the same harness-evolution
    loop that improved stronger models
  reason: 'DOUBTFUL — (bounded illustration) the cited weak-model null shows a base-model
    floor of the kind the three competences describe — in that loop the proposer was
    a fixed strong model across all lines, so the weak models did not perform diagnosis,
    candidate synthesis or acceptance judgment. Their floor lies in task execution:
    delivery rose while the freed trajectories landed as poor plans. The ingest also
    flags that seed plan quality and general capability are confounded in those three
    lines. The datum supports ''an inadequate executor blocks harness learning'',
    not a floor on competences 2 or 3 — LOCAL (say which role the illustration bears
    on, or limit it to competence 1 and task capability) — instance'
- scope: passage
  quotes:
  - routing and loading the relevant artifacts
  reason: DOUBTFUL — (stated as a capability harness code can take over) context assembly,
    including relevance routing, is mechanical machinery — routing is mechanical only
    when a rule-ready signal (a path, a tag, a typed field) already exists. In open-ended
    work, the condition the note invokes for its residue, new failure modes arrive
    without such signals, so deciding which artifacts bear on them is semantic work
    paid by some model at use-time or earlier. Loading, budget enforcement and schema
    validation are offloadable; relevance judgment for novel cases is not — LOCAL
    (restrict the harness item to signal-driven routing and move novel relevance into
    the LLM column) — instance
- scope: passage
  quotes:
  - reduces to competences 2 and 3 applied to the store and its criteria
  reason: DOUBTFUL — (universal) store maintenance and criterion revision need no
    competence beyond diagnosis/synthesis and trade-off judgment — competence 2 is
    defined as turning an unanticipated failure and its trace into a diagnosis. Refactoring
    prose rules into a cleaner abstraction or noticing a latent conflict between two
    rules often has no triggering failure or trace; it is unprompted synthesis or
    compression over the store. Either competence 2 must be widened beyond failure-triggered
    work, or this is a further competence — LOCAL (widen competence 2's definition
    to synthesis without a failure trigger) — instance
- scope: passage
  quotes:
  - These three competences can fail independently and sit at different capability
    thresholds.
  reason: DOUBTFUL — (possibility, used as the basis for a per-competence bootstrap)
    the competences are separable enough that transfer tests can identify which one
    binds — 'can fail independently' survives as a possibility, but the bootstrap
    needs separation to be common, not just possible. LLM capabilities usually correlate
    strongly with general capability, and the cited source shows that confound in
    exactly this setting (weak lines are weak on everything). If failures move together
    across most models, separate transfer tests mostly measure one general factor,
    and the 'which competence binds' question gets no stable answer — LOCAL (state
    that separability is conjectured and the tests must control for general capability)
    — prevalence
- scope: passage
  quotes:
  - the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head
  reason: HOLDS — (stated as a consequence of harness offloading) once budgets, traces
    and regression suites are enforced or recorded by code, the model does not need
    to keep them in its working context — the hunt looked for cases where the model
    must still hold this state itself. Enforced budgets and recorded traces need no
    model memory. Where the model must notice and heed a tool's output, that is interpretation
    under load, already covered by competence 1, so the premise does not leak a further
    requirement.
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/8c2e41a728cb46bc97c2e25314002af4/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/03102dbff531767134108a7f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 8c2e41a728cb46bc97c2e25314002af4
completed-at: '2026-11-24T13:20:45Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/8c2e41a728cb46bc97c2e25314002af4/outputs/review.md
raw-output-sha256: f7cf9b771bb0bec3e5f0f3893fc77ffde6e9a5e156b459e00ab0db8f5d677f60
format: 2
---

# Premise decomposition: Harness offloading leaves three base LLM competences

**Register:** claim
**Central commitment (one sentence):** In open-ended autonomous selection-based learning, harness code can absorb enforcement, evidence capture and store bookkeeping, and three irreducible semantic competences remain on the frozen base LLM as necessary conditions: interpreting uncodified text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs.

## Premises and counterexamples

The commitment has two halves, and each consumes its own premises. The offloading half needs the harness column to be truly mechanical: relevance routing must be signal-driven, and bookkeeping must leave no residue the model must hold. The residue half needs four things: the leftover semantic work sits on one model; the three competences exhaust it; each is necessary for autonomous operation; and they are separable enough to bootstrap one at a time. Two subsidiary premises carry particular sentences: the reduction of store maintenance and criterion revision to competences 2 and 3, and the cited weak-model null as an illustration of the floor.

The strongest pressure comes from the note's own sources rather than from outside. The relocation note it cites for irreducibility explicitly allows offloading a judgment to another processor. The cited harness-evolution source uses a different, stronger proposer model, so its weak-model null bears on executor capability, not on the diagnosis or judgment competences. None of the dents breaks the core mechanism: harness code takes the mechanical work and a semantic residue stays with the models. Each dent is repaired by a boundary condition or a restated role. The note's "working hypothesis" framing and its Scope bullet already invite those changes. No premise was found `DEFEATED` and none routes `GLOBAL`.

## For the human

Look first at the unstated single-model premise: the note's own grounding note and its own evidence source both place diagnosis on a different model from the executor, and stating the floor per role would also repair the misaimed illustration.
