---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: 'The title puts the identifying capacity in the rule: grammatically, ''it''
    is the fixed review rule. The body puts it in the reviewer. The instruction ''does
    not tell the reviewer which earlier failure bears on the page'', ''A reviewer
    following the original instruction could still recognize it'', and the rule need
    not change. The mechanism is the reviewer recognizing the relevant feature of
    an earlier incident, not the rule identifying applicability. So the title points
    the reader toward a requirement on the rule''s content, which the closing sentence
    (''not that the review rule must change'') rejects. Reframe the condition around
    the reviewer, or around rule plus reviewer, e.g. ''only if the reviewer can identify
    when they apply''.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 6b9410142685c447424f1bfcc9f187405069541a6a0006b521ec43e2daea610e
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/2021ef15d4474341b7b3eafc0e8aa06b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/19f775c06f339065e28357a9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 2021ef15d4474341b7b3eafc0e8aa06b
completed-at: '2026-11-23T11:40:31Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/2021ef15d4474341b7b3eafc0e8aa06b/outputs/review-framing-mismatch.md
raw-output-sha256: e1337e9d131808b754c26591fea3166dafc6283356d4890b3a9c66464cdc2cb6
format: 2
---

# Review

The body's sentences correctly identify the mechanism. A standing instruction says where to look. The reviewer must recognize which feature of an earlier failure, here a shared origin behind apparent independence, bears on the new case. The test is whether the reviewer draws that distinction, not whether it retrieves the incident.

The title frames the same condition as a capacity of the rule ("it can identify when they apply"). That misdirects the reader. It suggests the rule's text must encode applicability conditions, the reading the last paragraph explicitly denies. The framing excludes the case the body actually describes: an unchanged rule whose reviewer supplies the recognition. Under this gate's severity rule, that is a WARN.
