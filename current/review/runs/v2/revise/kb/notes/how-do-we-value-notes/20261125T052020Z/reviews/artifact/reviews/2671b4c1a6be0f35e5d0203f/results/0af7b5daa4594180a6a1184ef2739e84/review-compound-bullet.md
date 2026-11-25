---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Similarly, [a claim's test record does not determine its fit in a working theory]
  reason: 'The ''Validity separate from value'' bullet joins two cited claims with
    ''Similarly'': validity versus learning value, and test record versus fit in a
    working theory. The second claim could stand as its own bullet. Both support the
    bullet''s one lens, though, so the second reads as a parallel instance rather
    than a buried, separable point. It is borderline, not a defect.'
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0af7b5daa4594180a6a1184ef2739e84/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/2671b4c1a6be0f35e5d0203f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 0af7b5daa4594180a6a1184ef2739e84
completed-at: '2026-11-25T05:22:33Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0af7b5daa4594180a6a1184ef2739e84/outputs/review-compound-bullet.md
raw-output-sha256: 200633774be38ab7417b7359900362fef7110064386f166aaa6e203d7774126a
format: 2
---

# Review

## Summary

I checked each bullet over about 30 words. Each one develops a single idea with supporting detail:

- **Admission and answerability** states one admission condition and spells out what answerability requires.
- **Reader update and comparative work gain** names two aspects in its label. Its second sentence grounds the first sentence's test in downstream work and a cheaper alternative, so the second sentence elaborates the first rather than adding a separate claim.
- **Root questions versus sub-questions inside notes** builds one problem in steps: link-based reuse captures sub-questions, root questions go unrepresented, which leads to orphaned or closed-loop failures, and there is no current mechanism for them.
- **Asymmetric selection pressure**, **Cold-start selection** and **Combining dimensions** each state one open problem.

The only borderline item is the "Validity separate from value" bullet, recorded as INFO. It does not bury a second, independent point.
