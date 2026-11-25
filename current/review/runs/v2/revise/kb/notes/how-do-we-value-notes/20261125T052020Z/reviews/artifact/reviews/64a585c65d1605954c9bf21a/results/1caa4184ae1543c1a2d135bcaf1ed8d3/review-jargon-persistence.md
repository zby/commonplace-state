---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/1caa4184ae1543c1a2d135bcaf1ed8d3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/64a585c65d1605954c9bf21a/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 1caa4184ae1543c1a2d135bcaf1ed8d3
completed-at: '2026-11-25T05:21:20Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/1caa4184ae1543c1a2d135bcaf1ed8d3/outputs/review-jargon-persistence.md
raw-output-sha256: ad1dc80a40a64e20de397ef3d91f05a6b9b1a8746971e39053e8d9f3e7c2e6b9
format: 2
---

# Review

## Summary

No KB-internal term is defined once and then reused so often that later uses lose their grounding.

The candidate terms are "answerable", "explanatory-reach", "reader update", "counterfactual use" and "root questions". "Answerable" and "explanatory-reach" each appear once in the body, with a gloss. "Reader update" is glossed where it is introduced ("what nontrivial change the note warrants relative to the intended reader"). Its later uses ("learning value or reader update", and the final list of signals) are close to plain English and still read correctly without scrolling back. "Counterfactual use" is glossed as whether withholding or replacing a note changes search, diagnosis, decisions or recovery. Its two later mentions sit in short lists where the qualifier carries meaning, so this gate's exception for meaningful qualifiers applies. "Root questions" is introduced and reused within one bullet, so the grounding stays in view.

Terms that never receive a definition, such as "subroutines" and "demand-root coverage", are a definition problem rather than a persistence problem, so this gate does not cover them.
