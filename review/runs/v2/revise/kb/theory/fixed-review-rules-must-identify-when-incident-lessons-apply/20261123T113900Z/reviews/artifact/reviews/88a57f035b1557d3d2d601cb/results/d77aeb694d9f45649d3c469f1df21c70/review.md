---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/d77aeb694d9f45649d3c469f1df21c70/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/88a57f035b1557d3d2d601cb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: d77aeb694d9f45649d3c469f1df21c70
completed-at: '2026-11-23T11:41:22Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/d77aeb694d9f45649d3c469f1df21c70/outputs/review.md
raw-output-sha256: 3c27e9e628c0469a487e960b6700ee8586885e0241eab7f0397209cd800aa675
format: 2
---

# Review

## Summary

The note is three short paragraphs. Each one does a separate job, so none should be deleted or folded. The first paragraph states the claim: the rule says where to look, not which failure bears on the case. The second gives a worked case. Its contrast between a source-name lookup and a reviewer recognizing a shared origin is the part of the argument that would be lost without it. The third paragraph turns the example into a decision rule: success means telling apparent corroboration apart from independent support, not retrieving the incident.

The closing clause "not that the review rule must change" repeats the first paragraph's point that the rule can stay the same. It is a deliberate conclusion, though. It tells the reader that a new incident updates what the reviewer must distinguish, not the rule itself. This is the stance the reader should come away with, and it does not claim more than the note supports. Under the gate's conclusion check, it is not redundant. No clause defends against a misreading that an earlier clause already rules out.
