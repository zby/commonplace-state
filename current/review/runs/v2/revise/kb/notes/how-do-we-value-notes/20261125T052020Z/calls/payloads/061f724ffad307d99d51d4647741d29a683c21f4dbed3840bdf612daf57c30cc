---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 449bce9eb7ca42999ff7ee92e851d653
completed-at: '2026-11-25T05:23:44Z'
findings:
- scope: passage
  quotes:
  - '[quality signals for KB evaluation](../theory/quality-signals-for-kb-evaluation.md)
    combine structural maturity (type), review verdicts, recency, and link-strength-weighted
    inbound links'
  reason: The sentence leads the reader to expect a note that combines type, review
    verdicts, recency and link-strength-weighted inbound links into a ranking. The
    target is self-described as an 'exploratory question set, not an established scoring
    model'. It catalogues graph-topology signals, content-quality proxies, metamorphic
    relations and LLM-hybrid checks as candidate weak oracles for a learning loop,
    and it does not discuss review verdicts, recency or link-strength weighting. A
    reader who does not follow the link gets the wrong impression of what it supports.
  level: warn
- scope: passage
  quotes:
  - Every retained artifact adds maintenance, navigation, and exposure cost; [maintenance
    capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md).
  reason: The link text accurately names the target's claim, but the sentence cites
    it in support of a per-artifact cost. The target says artifact volume matters
    only through defect incidence, harm, exposure and remediation effort, not by itself.
    Readers following the link find a qualification of the sentence rather than support
    for it.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/a985ea916df817868a071b41/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/outputs/review-misleading-link-text.md
raw-output-sha256: ac2ae7677f7c721c997101e862c7850936a90d7c60cb605e11a486eb884f8b74
---

# Review

## Summary

I checked all 12 distinct link targets in the body and footer. All resolve. Most link texts are the target titles and are used in sentences that match the targets' opening claims: explanatory-reach, answerability, the validity/learning-value split, test record versus fit, warranted reader update, defining improvement (including its add-a-note-or-link case), system use as a selection environment, notes needing quality scores, link vocabulary and the underselection conjecture.

The Quality signals for KB evaluation link misleads. Its sentence credits it with a specific four-signal composite that belongs to the quality-scores note, not to this exploratory catalogue. The maintenance-capacity link has accurate text, but the sentence slightly overstates what the target supports.
