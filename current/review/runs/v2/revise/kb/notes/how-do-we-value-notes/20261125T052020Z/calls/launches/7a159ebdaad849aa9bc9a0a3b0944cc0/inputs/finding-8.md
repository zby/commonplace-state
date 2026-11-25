---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
findings:
- scope: passage
  quotes:
  - Commonplace currently spreads note valuation across five partial lenses rather
    than one rule
  reason: 'Unresolved mechanism and scope. Reading A: Commonplace''s operating workflows
    (admission contracts, review gates, ranking) apply these five lenses when deciding
    about notes. Reading B: the KB''s theory notes articulate five lenses, some of
    them only proposals not yet used in selection (for example the quality score).
    The readings need different evidence: A needs shipped mechanisms, B only needs
    the linked notes. They also change what follows. Under A, the Stakes retirement
    condition (''relies on ad-hoc judgment rather than a tested valuation practice'')
    is partly met. Under B, selection is still almost entirely ad hoc. The bullets
    mix shipped and proposed items, so nearby context does not decide between the
    readings.'
  level: warn
- scope: passage
  quotes:
  - it would narrow or retire once Commonplace adopts and validates an explicit selection
    mechanism
  reason: '''Validates'' leaves the retirement threshold open. It could mean passing
    review, or showing counterfactual benefit in live use as the system-use lens describes.
    The choice affects when the query retires. This is not shown to be material to
    the note''s current argument, so it is INFO.'
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/1a96ddd78a2e89f999db4913/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-underspecified-assertions.md
raw-output-sha256: a89cdcbe6ef22425b99fd7f4d634a5fdc9b3f93c09b1b37451108617863753fa
---

# Review

## Summary

Most load-bearing assertions are specific enough. Each lens bullet names its test, and the conjecture states its condition ("if production favors fluent local additions"). The root-question item explains its closed-loop failure. The cold-start item names the timing gap.

The main underspecified assertion is the sentence that frames Current answer. It does not say whether "spreads note valuation" describes what Commonplace's machinery does or what its notes argue. The bullets combine a shipped invariant (answerability) with proposed mechanisms (quality scores). The two readings need different evidence and imply different distances from the Stakes retirement condition. That is the WARN.

The retirement condition's "validates" is open in a similar way, but it does not drive the current argument, so it is recorded as INFO.
