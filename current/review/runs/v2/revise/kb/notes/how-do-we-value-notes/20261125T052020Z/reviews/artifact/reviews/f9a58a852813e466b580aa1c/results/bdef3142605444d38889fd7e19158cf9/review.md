---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/bdef3142605444d38889fd7e19158cf9/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/f9a58a852813e466b580aa1c/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: bdef3142605444d38889fd7e19158cf9
completed-at: '2026-11-25T05:23:31Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/bdef3142605444d38889fd7e19158cf9/outputs/review.md
raw-output-sha256: 0e9f5b299451ae54599c156d63a9fd2f084a2b48e7e959e2713b15bc9c4f69af
format: 2
---

# Review

## Summary

The note is a standing query: how should a KB note be judged worth keeping or selecting as autonomous production grows, beyond repo and collection goals? Its commitments are a stakes section, a current answer made of five partial lenses, and a list of unsettled problems. No branch competes with that question.

## Main claim and side material

- **Stakes.** The maintenance-capacity link and the retirement condition both say why the question matters and when it closes. They are scope, not branches.
- **Current answer.** Each lens is one or two sentences that point to a theory note. The sentence on a claim's test record versus its theory fit is the closest thing to a side distinction. It still sharpens the "validity separate from value" lens, because it separates being well-tested from being useful to the current theory. It is short enough not to weaken the note.
- **Unsettled.** The root-questions item is the longest, and it brings in query-centered root notes and closed citation loops. It stays on topic because it says exactly where the link-based proxy from the current answer fails as a valuation signal. The other three items (asymmetric selection pressure, cold-start admission, combining signals without Goodharting) each name an open problem in valuation itself. The asymmetric-pressure item partly repeats the urgency from Stakes, but it adds the conjecture about which qualities are underselected, so it is not redundant.

None of the side material needs to be removed, demoted, or moved to its own note.
