---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 449bce9eb7ca42999ff7ee92e851d653
completed-at: '2026-11-25T05:23:44Z'
findings:
- scope: passage
  quotes:
  - relative to the intended reader and existing KB beyond a generic treatment
  reason: 'Modifier attachment: ''beyond a generic treatment'' can attach to ''existing
    KB'' (a KB that goes beyond generic treatment) or to ''change'' (a change beyond
    what a generic treatment would give). Context favours the second reading, and
    the first reading makes little sense, so this is minor. Placing ''beyond a generic
    treatment'' directly after ''nontrivial change'' would remove it.'
  level: info
- scope: passage
  quotes:
  - its contract can name what referent or outcome it answers to
  reason: 'Pronoun reference: ''its contract'' follows both ''A note'' and ''a knowledge
    collection'', so it can be read as the note''s own contract or the collection''s
    contract. The linked definition allows either the artifact or its collection''s
    contract, so neither reading is wrong, but ''its collection''s contract'' would
    match the usual admission mechanism.'
  level: info
- scope: passage
  quotes:
  - a tightly linked cluster can answer each other's sub-questions
  reason: '''Each other''s'' has a singular antecedent (''cluster''). The intended
    reading (notes within the cluster answer one another''s sub-questions) is recoverable,
    but ''the notes in a tightly linked cluster'' would make the reciprocal grammatical.'
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/18f1af4bae6aef6eef2a1692/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/outputs/review-parsing-ambiguity.md
raw-output-sha256: 47ec54529a11c2839d843cc9150cada37567c7e71d40dc3906b5bb6f892f5193
---

# Review

## Summary

No sentence has a plausible unintended reading that changes its claim. The negation scopes in "do not exhaust how to rank, keep, or reject" and "no established way to represent" are clear. The fronted "Where" and "Without" clauses attach unambiguously. "It" in the retirement sentence clearly refers to the query. Three local attachment or reference looseness points are recorded as INFO.
