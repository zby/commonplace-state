---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: UNSUPPORTED — the preceding ground, that semantic work can be relocated
    but not eliminated, establishes only that some semantic work remains somewhere.
    It does not establish that this work must stay on the frozen base LLM rather than
    move to a human, a second model, a trained verifier or an accumulated library
    of codified checks. Nor does it show that the remainder partitions into exactly
    three competences. 'Irreducible' also conflicts with the Scope section, which
    lets any sub-task shown to be offloadable leave the LLM column; the note does
    not say which sense of irreducible it means.
- scope: passage
  quotes:
  - spotting semantic conflicts between prose rules, refactoring them into a cleaner
    abstraction, or proposing a revised check reduces to competences 2 and 3 applied
    to the store and its criteria
  reason: UNSUPPORTED — the reduction is asserted, not shown. Competence 3 weighs
    consequences 'against stated commitments', but double-loop criterion revision
    changes those commitments, so judging against them does not cover revising them.
    Competence 2 is framed around diagnosing an unanticipated failure and its trace,
    while refactoring prose rules into a cleaner abstraction need not start from any
    failure. Without that bridge, criterion revision could be a fourth competence
    or a different use of the existing three.
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs,
    the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head
  reason: THIN — the ability to write tool code does not establish that the model
    can tell when a new tool is needed, specify it correctly or trust its output.
    The 'because' moves bookkeeping off the model only by assuming that tool building
    succeeds. The note later classes harness-code synthesis under competence 2, so
    this joint depends on the competence it is meant to set aside without saying so.
- scope: passage
  quotes:
  - These three competences can fail independently and sit at different capability
    thresholds. A model may follow clear prose procedures while still misdiagnosing
    noisy traces or overclaiming certainty on incomplete records.
  reason: THIN — the example shows only that competence 1 can be present while 2 or
    3 is absent. It does not show the other dissociations, such as sound diagnosis
    with poor prose-following, which independence requires. The next step also assumes
    that transfer tests can isolate one competence's decisions, although diagnosis
    and synthesis in competence 2 both depend on interpreting text through competence
    1.
- scope: passage
  quotes:
  - an inadequate base model can block outer-loop learning before the store itself
    saturates
  reason: 'HOLDS — the bounded claim follows from the cited contrast: the same loop
    improved stronger models, so the store had not saturated, while the weakest models
    gained nothing held-out. The joint supports only a general base-model floor. It
    does not identify that floor with the three named competences, and the note does
    not claim that it does.'
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/3f502d053bff4382a3ce1ec2b2aeeec9/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/bc573e55ccd94be223f6a4a5/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 3f502d053bff4382a3ce1ec2b2aeeec9
completed-at: '2026-11-24T13:19:02Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/3f502d053bff4382a3ce1ec2b2aeeec9/outputs/review.md
raw-output-sha256: 51335d995daa44503a7aecf938b55be2206d4e1e6e25a349d2c9ccd3d8ad8197
format: 2
---

# Friction check: base LLM competences for autonomous selection-based learning

**Central claim (one sentence):** In an autonomous selection-based learning loop, harness code can take over enforcement, evidence capture and store bookkeeping, leaving three semantic competences on the frozen base LLM: interpreting unformalized text, diagnosing failures and synthesizing remedies, and judging unformalized trade-offs.

## Filter
**Filter:** SURVIVES

The note can be built as one consistent thing: a division of labour with three model-side competences, presented as revisable. The nearest tension is between "irreducible" and the Scope rule that any reliably offloadable sub-task leaves the LLM column. Under a provisional reading, "currently not known to be offloadable", the two can coexist, so the claim does not dissolve. The note should still use one sense of the word.

## Thinnest joints

The two `UNSUPPORTED` joints carry the note's distinctive content: why the remainder stays on the base LLM and splits into exactly three parts, and why criterion revision adds no fourth part. Both are stated without argument. The cited relocation note only shows that semantic work persists, and the competence 3 definition judges against commitments rather than revising them. The two `THIN` joints are supporting moves: tool building assumes the competence it sets aside, and independence rests on one dissociation. The evidence joint is the strongest because the note limits it to a generic floor and does not claim it validates the three-part split.

## For the human

Look first at the step from "relocated, not eliminated" to "three irreducible competences on the frozen base LLM". The note needs to say why the remainder cannot move off the base model, and what makes the count three rather than two or four.
