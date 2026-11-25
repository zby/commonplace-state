---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - where the three weakest tested models produced no held-out gains under the same
    harness-evolution loop that improved stronger models
  reason: 'DOUBTFUL — The cited case illustrates a floor on the base model''s outer-loop
    competences, which is how the note uses it as an illustration for this split.
    — In the linked ingest, a separate strong proposer (Kimi K3) did the diagnosis
    and edit proposal. The weak models only executed tasks under the harness. Their
    ceiling was poor plan quality (F4) among delivered plans, and the ingest notes
    that model weakness and seed plan quality are confounded. The case therefore shows
    a floor on task execution, or at most on competence 1. It does not show a floor
    on diagnosis (2) or judgment (3), and the loop was not run autonomously by the
    weak model. Fix: say which competence the case bears on, or describe it as a task-capability
    floor. — LOCAL — instance'
- scope: passage
  quotes:
  - spotting semantic conflicts between prose rules, refactoring them into a cleaner
    abstraction, or proposing a revised check reduces to competences 2 and 3 applied
    to the store and its criteria
  reason: 'DOUBTFUL — Store maintenance and criterion revision need no competence
    beyond 2 and 3 (stated universally). — Competence 2 is defined as starting from
    an unanticipated failure and its trace. Consolidation is different work. Merging
    overlapping prose rules into a cleaner abstraction, or compressing a store that
    has no failing case, means generalizing across many entries with no failure or
    trace as input. Competence 3 weighs trade-offs and spots misleading checks, so
    it does not cover synthesizing the abstraction either. Either competence 2 is
    widened to cover synthesis without a triggering failure, or consolidation is a
    residue that is not listed. Fix: widen the wording of competence 2. — LOCAL —
    instance'
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: DOUBTFUL — The three competences exhaust the semantic residue in open-ended
    work (working hypothesis; Scope concedes additions). — Exploration and task selection
    have no clear place. This means choosing which uncovered situation to probe next,
    or generating new test tasks so that latent failures surface before they occur
    in use. It is not interpreting given text (1), it is not diagnosing an observed
    failure (2), and it is only loosely judging a trade-off (3). Under the note's
    own condition that new failure modes keep arriving, finding them is a recurring
    semantic job. The Scope bullet already allows additions, so the gap revises the
    list and leaves the mechanism intact. — LOCAL — instance
- scope: passage
  quotes:
  - Clearing these competences is proposed as necessary for operating the loop autonomously,
    not sufficient for sustained continual learning.
  reason: 'DOUBTFUL — Each competence is a necessary threshold for autonomous operation
    (stated as a necessary condition). — Variant-and-select loops with a fixed automatic
    scorer produce held-out gains without stated diagnoses. The linked ingest describes
    its loop as this kind, and it still improved 4B and 9B. In such loops a weak competence
    2 or 3 lowers the quality and efficiency of learning rather than blocking operation.
    Necessity therefore holds only where no fixed check settles selection, which is
    the note''s open-ended condition. The condition fails outside it, not the premise
    inside it. Fix: say the competences are graded, or restrict necessity explicitly
    to work where selection is not settled by a fixed scorer. — LOCAL — instance'
- scope: document
  quotes: []
  reason: DOUBTFUL — One frozen base LLM supplies all three competences (unstated;
    the note says the frozen base LLM throughout). — Loops often split the roles across
    models. In the linked ingest, a strong proposer model diagnoses and proposes,
    while a weaker model executes the procedures (competence 1). A trained verifier
    or a different model can act as the selector (competence 3). Different models
    can then clear different competences. The relevant floor is set per role, not
    per base model, which also changes how a bootstrap identifies which competence
    currently binds. — LOCAL — instance
- scope: passage
  quotes:
  - running codified validators and schemas, routing and loading the relevant artifacts,
    and enforcing token budgets
  reason: DOUBTFUL — The listed machinery is mechanical enough for harness code (hedged
    as much of the loop). — Several listed items carry semantic judgment. Routing
    and loading relevant artifacts requires a relevance judgment, and in KBs an LLM
    routinely makes it from descriptions. Annotating telemetry coverage gaps overlaps
    competence 3's recognizing missing evidence. Flagging rising failure rates requires
    classifying failures. In the linked ingest the automated F1–F4 checker could not
    separate F4 from a healthy run. These items split into a mechanical part and a
    semantic part. The hedge 'much of' absorbs this, but the bullets put the semantic
    parts on the harness side. — LOCAL — instance
- scope: passage
  quotes:
  - These three competences can fail independently and sit at different capability
    thresholds.
  reason: DOUBTFUL — The competences are separable enough that transfer tests can
    identify which one binds (the premise says can, but the bootstrap use needs measurable
    separation). — The competences are causally chained. A misdiagnosis (2) can come
    from misreading the governing procedure (1), and a bad trade-off judgment (3)
    can come from a wrong diagnosis (2). Shared capacities such as long-context reading
    also make their failures correlate. A test of competence 3 that is not fed a correct
    diagnosis measures 2 and 3 together. The bootstrap therefore needs controlled
    inputs per competence, such as a supplied correct diagnosis, before failures can
    be attributed. — LOCAL — instance
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs
  reason: HOLDS — An LLM that writes code can build harness tools for budgets, traces
    and regression suites, so it need not track them in context. — No defeater found.
    Building those tools is itself covered by competence 2 (synthesizing executable
    harness code), so the premise does not hide an extra competence. Once built, the
    tools run outside the model's context.
- scope: passage
  quotes:
  - semantic work can be relocated without being eliminated
  reason: HOLDS — In open-ended work some semantic residue cannot be codified away
    and must land on the model (working hypothesis, conditioned on new failure modes,
    commitments and remedies continuing to arrive). — Under the stated condition,
    attempts to codify each residue only move it. Codifying a prose rule moves interpretation
    to the author of the code (2). A new check moves judgment to the decision that
    the check fits (3). Within the condition, no case was found where the residue
    disappears. Outside it, see the necessity finding.
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/34d39ab755934e4abfc96134d1aa7d27/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/03102dbff531767134108a7f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 34d39ab755934e4abfc96134d1aa7d27
completed-at: '2026-11-24T13:20:58Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/34d39ab755934e4abfc96134d1aa7d27/outputs/review.md
raw-output-sha256: 0d36c97fe780dc2169139feea3c763163f229db3fea31bda6accfaa987234255
format: 2
---

# Premise decomposition: harness offloading leaves three base LLM competences

**Register:** claim
**Central commitment (one sentence):** In open-ended work, harness code can take over much of an autonomous selection-based learning loop's machinery, but three semantic competences remain on the frozen base LLM: interpreting unformalized text into action, diagnosing novel failures and synthesizing remedies, and judging unformalized trade-offs and missing evidence. These are necessary for running the loop autonomously, and store maintenance and criterion revision reduce to them.

## Premises and counterexamples

The commitment has two parts, and the premises split the same way.

- **Offloading.** One set of premises says what can move to harness code. The machinery is mechanical, and the LLM can build the tools itself.
- **Residue.** A second set says what stays on the model. Some semantic residue is irreducible, the three named competences exhaust it, the other loop functions reduce to them, and one frozen model holds them.

Two further premises carry the note's practical uses. The competences must be separable enough that a bootstrap can tell which one binds. The cited source must show a floor on these competences. Finally, the Scope's necessity claim is itself a premise of the autonomy framing.

Every inference between the premises was assumed valid. The hunt found no global defeater. The core mechanism holds within the note's open-ended condition: mechanical work moves to the harness, while semantic residue relocates rather than disappears.

The failures sit in where the boundaries are drawn. Some semantic sub-steps are placed on the harness side. Consolidation and exploration have no home in the list. The roles are assumed to sit on one model. The cited evidence bears on task execution, not on the outer-loop competences. Each of these can be repaired by rewording a competence, adding a boundary condition, or adding to the list. The Scope's concession that bottlenecks can add to the list already anticipates most of them.

## For the human

Look first at the Harness Evolution illustration. Its proposer was a separate strong model, so the weak-model floor it shows is on task execution, not on the diagnosis or judgment competences that the note's split is about.
