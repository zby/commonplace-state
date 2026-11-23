---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/frontmatter/title-composability.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 7f93a4da2702212e99df1dc11c85119dc8050b09020512b4bcaadf6f8ac41929
criterion: kb/instructions/review-gates/frontmatter/title-composability.md
criterion-sha256: f8cac17c0f9608c444b3115f63e8e2458abf21903cb5a82a4e41d74dbf629e52
outcome: pass
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
  reason: The title composes grammatically, but when embedded in another note's sentence
    the pronoun 'it' can bind to the surrounding subject instead of to 'a fixed review
    rule'. Naming the identifier (for example 'the reviewer') would make the linked
    fragment self-contained.
  level: info
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/535b61707706e8b38f9608eb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/outputs/review-title-composability.md
raw-output-sha256: fbca9301bbdf4378e8d24e0611ccd8005e7f77780d82685b2a1c7ecbefd90998
---

# Review

Placed in sentence frames, the title reads naturally: "since a fixed review rule can use lessons from new incidents only if it can identify when they apply, …" and "because a fixed review rule can use lessons … only if it can identify when they apply, …". It is a full clause with a clear subject and predicate, and it needs no grammatical repair when linked. The only friction is the pronoun noted in the info finding, which is minor and does not cause a failure.
