---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Clearing these competences is proposed as necessary for operating the loop autonomously
  reason: 'The threshold is unresolved. Reading A: the model must have each competence
    at some above-chance level. Reading B: the model must have each competence reliably
    enough that the autonomous loop improves rather than degrades the store. Under
    A, the necessity claim is close to trivially true and needs little evidence. Under
    B, it is contestable, needs evidence about net loop outcomes, and sets a different
    bar for when to remove human assistance. The note names no reliability level or
    outcome criterion.'
  level: warn
- scope: passage
  quotes:
  - sit at different capability thresholds
  reason: This could mean the competences emerge at different model scales, or that
    a given task demands different levels of each competence. Both readings support
    the next sentence's 'identify which competence currently binds', so the difference
    may not be material.
  level: info
- scope: passage
  quotes:
  - while transfer tests check each kind of decision on its own
  reason: '''Transfer tests'' could mean held-out tests of each model competence,
    or tests of whether a step humans supplied can transfer to the model. The intended
    bootstrap procedure differs somewhat between the readings, but the sentence is
    illustrative.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/4e675fada9d510b5263bc9ab/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: cccda05d8a25440b842c04af9c04b834
completed-at: '2026-11-24T13:17:58Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/outputs/review-underspecified-assertions.md
raw-output-sha256: 06d04a7b894b1bfabe4080aaa712af9fe46af9d161999d43f8a19afbff30ec1b
format: 2
---

# Review

## Summary

Most load-bearing assertions are adequately specified for a working-hypothesis note. The harness column is concrete, and each competence has a stated scope. "Irreducible" is resolved by the Scope section as a revisable hypothesis, not an impossibility claim. The one material gap is in the necessity claim. The note does not say what clearing a competence means, so readers cannot tell whether necessity is a near-tautology or a substantive, testable bar on loop outcomes.
