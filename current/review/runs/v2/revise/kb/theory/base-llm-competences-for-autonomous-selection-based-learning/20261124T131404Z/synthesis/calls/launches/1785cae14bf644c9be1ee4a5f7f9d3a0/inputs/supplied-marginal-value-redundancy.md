---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 91f6ec94052944b6929426f8142c51a6
completed-at: '2026-11-24T13:17:43Z'
findings:
- scope: passage
  quotes:
  - not an established impossibility result
  reason: 'The first Scope bullet labels the split a working hypothesis for the third
    time: the bold lead-in says ''Working hypothesis'' and the competence paragraph
    says ''our working hypothesis is''. The trailing ''not an established impossibility
    result'' guards against a misreading that ''working hypothesis'' already rules
    out, so it is defensive redundancy. The bullet''s useful part is its revision
    rule: offloadable sub-tasks leave the LLM column, and newly found bottlenecks
    can join it. Cut the label and the contrast clause, and keep the revision rule
    as the bullet, or fold it into the sentence that introduces the three competences.'
  level: warn
- scope: passage
  quotes:
  - the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head
  reason: 'This consequence clause restates the three bullets just above it, which
    already assign budgets, traces and replay or regression work to harness code.
    The sentence adds one new point: an LLM that writes code can build further harness
    tools. Keep that point, in a shorter clause or in the lead-in to the bullets,
    and drop the restated consequence so the paragraph turns directly to the semantic
    remainder.'
  level: warn
contract: verdict
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/91f6ec94052944b6929426f8142c51a6/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/61228b484c8594aea6edaaf9/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/91f6ec94052944b6929426f8142c51a6/outputs/review.md
raw-output-sha256: dc044a2abc34dd976671eb1230cfb7b9d15c9a90ba23fb5767acf49257a50bfc
---

# Review

## Summary

Most of the note earns its space. Each of the three competences states a distinct requirement and links to the note that develops it. The store-maintenance paragraph does necessary work: it explains why there is no fourth competence for criterion revision or store upkeep. The independence paragraph turns the split into a diagnostic use, and the empirical paragraph supplies the note's only evidence. The second Scope bullet (necessary, not sufficient) adds a boundary that appears nowhere else. The open questions are new.

Two passages fail the deletion test in their current form. The first Scope bullet repeats the "working hypothesis" label a third time and adds a defensive contrast clause; only its revision rule is new. The bridge sentence after the harness bullets restates what those bullets assign to harness code; only the point that the LLM can build new harness tools is new. In both cases, keep the new point in a shorter form and cut the recap.
