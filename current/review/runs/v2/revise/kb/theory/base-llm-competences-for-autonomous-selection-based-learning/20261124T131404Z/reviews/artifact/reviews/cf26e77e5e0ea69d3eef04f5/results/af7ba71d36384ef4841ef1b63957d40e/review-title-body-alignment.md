---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Harness code may offload much of a selection loop, leaving three base LLM competences
  reason: 'Scope drift: the H1 does not say the loop is autonomous. The body limits
    its claim to an autonomous selection-based learning loop in open-ended work. It
    also says that a human-assisted bootstrap can have ''people temporarily supply
    the missing semantic step'', and its Scope section proposes the competences as
    ''necessary for operating the loop autonomously''. So the body establishes that
    harness code can take over much of the loop''s mechanical and structural machinery
    and that, for autonomous operation in open-ended work, three semantic competences
    remain on the frozen base LLM. Without ''autonomous'', the H1 implies the competences
    stay on the base LLM in any selection loop, including human-assisted ones where
    the body says people can supply them. The filename slug and description both say
    ''autonomous''; the H1 drops it.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: e5848132157b8e12c27c8a339438b91f09fe510eb1674eb156ba80f5d37c590b
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/af7ba71d36384ef4841ef1b63957d40e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/cf26e77e5e0ea69d3eef04f5/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: af7ba71d36384ef4841ef1b63957d40e
completed-at: '2026-11-24T13:15:03Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/af7ba71d36384ef4841ef1b63957d40e/outputs/review-title-body-alignment.md
raw-output-sha256: da0c2ae4d0c813e25581cdb98107f63e543eafebade7195b1fc8e5553a0bcbc4
format: 2
---

# Review

## Summary

The body mostly supports the title. It lists three groups of work that harness code can offload: enforcement and context assembly, evidence capture and replay, and store bookkeeping. It then names three semantic competences that remain on the base LLM. It also argues that store maintenance and criterion revision reduce to competences 2 and 3 rather than adding a fourth. That supports the count of three. The hedge "may" matches the body's framing of the split as a working hypothesis.

The mismatch is scope. The body conditions the residue on autonomous operation in open-ended work, where new failure modes keep arriving. It says plainly that humans can supply the missing semantic steps during a bootstrap. The H1 says only "a selection loop," which is broader than what the body establishes. Adding "autonomous" to the H1 would align it with the body, the description and the filename.
