---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - an autonomous [selection-based learning](./definitions/selection-based-learning.md)
    loop
  reason: Selection-based learning is an active vocabulary term in AGENTS.md. Its
    first mention has a link but no inline gloss. The reader cannot tell what makes
    a loop selection-based (for example, that candidates are generated and kept or
    discarded by a selection step) without following the link. The note's title and
    argument depend on this term. Add a short gloss beside the link.
  level: warn
- scope: passage
  quotes:
  - Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
  reason: '''Scheduler–LLM separation'' is a KB-internal principle. Here it is used
    as the justification for offloading work to harness code, but the sentence does
    not say what is separated from what or why. A short clause would let the reader
    follow the argument without the link, e.g. that deterministic code handles scheduling
    and bookkeeping while the model handles semantic interpretation, because code
    errors are easier to detect and correct.'
  level: warn
- scope: passage
  quotes:
  - can block outer-loop learning before the store itself saturates
  reason: '''Outer-loop learning'' is not defined in the note. The reader can roughly
    infer that it means improvement from updating the store rather than the weights,
    but the note never states this. Consider glossing the term or replacing it with
    ''learning through store updates''.'
  level: info
- scope: passage
  quotes:
  - while transfer tests check each kind of decision on its own
  reason: '''Transfer tests'' is not explained. The reader cannot tell what is transferred,
    or from where to where. A short phrase saying what such a test checks would make
    the bootstrap procedure clear.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/4da2438451d4416fb7ea1b63da196908/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/17a719a9398d6f2f4d3b51d2/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 4da2438451d4416fb7ea1b63da196908
completed-at: '2026-11-24T13:15:07Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/4da2438451d4416fb7ea1b63da196908/outputs/review-undefined-terms.md
raw-output-sha256: cac215b5abdfff09e9690554292f497939b9054bd6ce1a2dedc6a56352529224
format: 2
---

# Review

## Summary

Most of the technical vocabulary is either standard (LLM, harness, token budgets, held-out gains, ablations) or glossed by its surrounding sentence. For example, the list item for competence 1 effectively explains "operative change": prose must "govern its behavior under realistic context loads". "Criterion revision" is also clarified later in the same paragraph as "proposing a revised check". "Human-assisted bootstrap" is explained by the clause that follows it.

The main gaps are in the opening paragraph. The note's central term, "selection-based learning", is an active vocabulary term, and its first mention has a link but no gloss. The note also uses "scheduler–LLM separation" as the reason for its whole split without saying what that separation is. Either gap forces a first-time reader to follow a link before the argument makes sense. Two later terms, "outer-loop learning" and "transfer tests", are less critical but would also benefit from a brief gloss.
