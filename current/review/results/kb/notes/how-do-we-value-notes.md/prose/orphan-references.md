---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/prose/orphan-references.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: d4b831b9fa124e7cbef658de301f7070
completed-at: '2026-11-25T05:21:24Z'
findings:
- scope: passage
  quotes:
  - Structural validation, source grounding, and critique gates check validity more
    strongly than anything checks learning value or reader update.
  reason: This is a comparative empirical claim about Commonplace's own checks, and
    the note gives no source or evidence for it. It is legible to a Commonplace reader,
    and the next sentence frames the consequence as conditional on a linked conjecture,
    so it does not mislead. A pointer to the gate inventory or review architecture
    would let a reader check it.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/d4b831b9fa124e7cbef658de301f7070/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/cf62b28f1acffaeb970ff744/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/d4b831b9fa124e7cbef658de301f7070/outputs/review-orphan-references.md
raw-output-sha256: b023fb40c4874a4c6a72a1a679e0fb0c22cfee0beaa85709af6d8a5258c6970e
---

# Review

## Summary

The note contains no figures, percentages or named studies. Its claims about which signals Commonplace uses are each tied to a linked note: answerability, the validity and learning-value gates, warranted reader update, system use, and quality scores. The one unsupported comparative claim about the relative strength of existing checks is recorded as INFO. It describes the reader's own system, and the note keeps its consequence conditional.
