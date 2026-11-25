---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Those goals decide what a collection admits in principle, but they do not exhaust
    how to rank, keep, or reject candidate notes.
  reason: The note's opening point (collection goals govern admission but not ranking
    or retention) arrives only after the first sentence spends itself on example quality
    bars and an inline parenthetical gloss of explanatory-reach. The claim is findable,
    but the setup delays it. Leading the paragraph with this sentence and folding
    or dropping the explanatory-reach gloss and examples would make the stakes land
    faster.
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/8f216919f97b49c0b945e79002d69c7e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/f5f323ab9563f3c1f8b63d06/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 8f216919f97b49c0b945e79002d69c7e
completed-at: '2026-11-25T05:23:34Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/8f216919f97b49c0b945e79002d69c7e/outputs/review.md
raw-output-sha256: b1142087c15776990f64443be6a0cda91bb21242a09258319b74399980c37187
format: 2
---

# Review

## Summary

The note is a standing query, so its core commitment is a two-part answer: Commonplace values notes through five partial lenses rather than one rule, and no tested selection mechanism yet decides between valid and valuable notes under autonomous production. In one sentence: *Commonplace judges note value through five partial lenses (answerability, validity-versus-value, reader update, counterfactual use and structural proxies) without a tested way to combine them, which matters because autonomous production can accumulate valid but low-value notes faster than curation removes them.*

The structure makes that sentence easy to recover. The title states the question. The Stakes section names the risk of well-formed clutter and the retirement condition. The Current answer opens with a plain thesis line ("spreads note valuation across five partial lenses rather than one rule"), and bolded lens labels keep each bullet subordinate to it. The Unsettled bullets follow from that answer: cold start, combining signals and asymmetric selection pressure. They do not compete with it.

The one drag is the first Stakes paragraph. Its first sentence gives examples of collection quality bars and an inline gloss before the paragraph says what those goals fail to cover. This makes the opening slightly less memorable but does not hide the claim, so the outcome is PASS with an INFO finding.

A possible revision target is the asymmetric-selection-pressure point in Unsettled: validity is checked more strongly than value. It is arguably the sharpest mechanism behind the note's urgency. Stakes already gestures at it ("high-value notes from merely valid ones"), so naming it there would tie the stakes to the Unsettled bullet. That change is optional and does not affect this check's outcome.
