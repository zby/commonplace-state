---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 7f93a4da2702212e99df1dc11c85119dc8050b09020512b4bcaadf6f8ac41929
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 83b0772e8ccc44e7a507e7f3b9b27092
completed-at: '2026-11-23T11:40:02Z'
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: The main predicate is close to a truism. Few informed readers would deny
    that a lesson helps only when someone can tell when it applies. The contestable
    points the note makes are elsewhere. First, the rule need not change as incidents
    accumulate. Second, applicability follows a structural feature of the earlier
    failure rather than surface matches such as source names. The first point is only
    presupposed in the subject ('A fixed review rule can use lessons'); the second
    is absent. Moving one of these points into the main claim would strengthen the
    title.
  level: warn
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/7cab57d7191567ee83ec69bd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/outputs/review-claim-strength.md
raw-output-sha256: 44a492eee16ac2a634166bd53ed6d3a908c38ad358d3c14aceea2b8ff0e665b6
---

# Review

Opposite-argument test: could someone informed reasonably argue that a fixed rule can use incident lessons *without* anyone identifying when they apply? Hardly. Applying a lesson already involves recognizing that it applies, so the "only if" condition is nearly analytic.

The note does make contestable claims, but the title does not. One is that a standing "check past incidents" instruction can stay fixed while its effective content grows; someone could argue that each incident should add a specific checklist item. The other is that a lesson transfers through a structural feature, such as two sources sharing an origin when the claim depends on their independence, and not through name-based lookup. The title presupposes the first claim in its subject and leaves the second out. This matches the gate's presupposed-claim pattern: the hard point sits in the subject and the predicate is weak.
