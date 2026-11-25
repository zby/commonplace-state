---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/structural/general-before-specific.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 0af7b5daa4594180a6a1184ef2739e84
completed-at: '2026-11-25T05:22:33Z'
findings: []
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0af7b5daa4594180a6a1184ef2739e84/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/7d2d857a0cf942edf442b831/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0af7b5daa4594180a6a1184ef2739e84/outputs/review-general-before-specific.md
raw-output-sha256: f0e8c584131df866291da73b20eced54559739577bf1fa4606c155740ba57046
---

# Review

## Summary

The note has three body sections: "Stakes", "Current answer" and "Unsettled". It then has a "Relevant Notes" footer.

- **Stakes → Current answer:** "Stakes" sets out the question and why it matters. "Current answer" gives the general lenses Commonplace uses now. Neither section is a specific case of a rule that the other states.
- **Current answer → Unsettled:** "Unsettled" lists open problems and tensions with the current answer. It comes after the general statement it qualifies, so the order already runs from general to specific.

No adjacent pair puts a specific case, exception or tension before the general pattern it illustrates.
