---
type: types/edit-result.md
outcome: changed
changes:
- Replaced the near-truism H1 ('... can use lessons from new incidents only if it
  can identify when they apply') with 'Fixed review rules apply incident lessons by
  recognition, not retrieval'.
- Rewrote the description to state that the rule need not change as incidents accumulate
  and that a lesson applies through a recognized structural feature (shared origin),
  not a lookup by source name.
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/repair-claim-title.md
  on kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
format: 1
operation: kb/instructions/simplification-passes/repair-claim-title.md
operation-sha256: 536b81aa6104ba1ec7d2d92e3f48a5efebb971d78384a8b1040322a7da02df60
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
input-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/calls/launches/5feb4735390a481f9792d3a7150376c6/outputs/candidate.md
candidate-sha256: 17840712dbccefe4ff6f161decca5902ec45c3eef892ebc2415f20ed475f8e11
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/artifact/edits/0c693e784168e9492002aad7/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z
launch: 5feb4735390a481f9792d3a7150376c6
completed-at: '2026-11-23T11:50:16Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/calls/launches/5feb4735390a481f9792d3a7150376c6/outputs/result.md
raw-output-sha256: d43c71905f63f78c8bb828f53661f4d2a412e9d0b62858218a303a8687e0fd96
---

# Report

The finding still applies: the old main predicate ("only if it can identify when they apply") is nearly analytic, while the contestable points sat in the subject or were missing.

The title now states that a fixed review rule applies incident lessons by recognition, not retrieval. That is the contrast the body draws and the one the purpose asks the note to make: finding an incident versus recognizing when its lesson applies. Supporting passages: "The test is not whether the reviewer retrieved the incident. It is whether the reviewer distinguishes apparent corroboration from independent support on the new page." and "A lookup by source name would miss that connection. A reviewer following the original instruction could still recognize it."

The description carries the other contestable point. A standing rule need not change as incidents accumulate. This rests on "can remain the review rule even as new incidents accumulate" and "not that the review rule must change". The description also names the mechanism: a structural feature such as a shared origin, which a lookup by name misses. It keeps the body's force: "need not change" matches the body's "can remain" and does not claim that the rule never changes.

The new slug, `fixed-review-rules-apply-incident-lessons-by-recognition-not-retrieval`, has 70 characters. I did not move the file. The body and the other frontmatter are unchanged, and all must-keep claims remain in the body.

Not applied, for the operator: the kb-role report says that inbound links cite this path, under an older title, for a claim about continual learning as governed behaviour-changing writes. The current body does not support that claim, and the old H1 did not either. A title-only repair cannot reconcile them. Retargeting the inbound links or relocating this note is a separate decision.
