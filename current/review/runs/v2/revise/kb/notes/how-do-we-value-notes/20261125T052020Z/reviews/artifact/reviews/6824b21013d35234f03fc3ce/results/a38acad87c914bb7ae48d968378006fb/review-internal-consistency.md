---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Autonomous production needs a way to filter, quarantine, or trial new candidates
    before those downstream signals exist
  reason: 'Possible tension with Current answer. Three of the five lenses already
    operate before downstream signals exist: answerability at admission, the validity
    versus learning-value gates, and the reader-update comparison. The cold-start
    item treats admission-time selection as lacking a method. It is probably consistent
    if the lack is operational, meaning those lenses have no adequate check (as the
    asymmetric-selection item implies). The note does not state that link, so the
    tension needs human confirmation.'
  level: info
- scope: passage
  quotes:
  - subroutine reuse
  reason: Likely term drift. The root-questions item calls what inbound links measure
    'reuse when one note answers a local sub-question raised inside another note',
    then mentions 'answering notes and their subroutines'. The combining item lists
    'subroutine reuse' and 'demand-root coverage' as signals. These seem to refer
    to the sub-question reuse and root-question coverage described earlier, but the
    vocabulary shifts without saying so.
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/6824b21013d35234f03fc3ce/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-internal-consistency.md
raw-output-sha256: 21e18857faf987aeb7dae386ed02fcc02e8f85a1fa29d5aa3a8b55015c684504
format: 2
---

# Review

## Summary

Key claims by section:

- **Stakes.** Collection goals set admission in principle but do not exhaust valuation. Volume growth makes valuation urgent. The query stays open while selection relies on ad-hoc judgment.
- **Current answer.** Valuation is spread across five partial lenses.
- **Unsettled.** Inbound links miss root questions. Gates select for validity more than for value. Admission lacks cold-start selection. Combining signals is unresolved.

There is no pairwise contradiction. "Partial lenses rather than one rule" agrees with the Stakes condition that selection still relies on ad-hoc judgment. The structural-proxy lens and the root-questions limitation agree: Unsettled qualifies what Current answer offers.

Two items need human confirmation. The cold-start item may understate the admission-time lenses that Current answer lists. The combining item renames sub-question reuse as "subroutine reuse" and root-question coverage as "demand-root coverage".
