---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A fixed review rule can use lessons from new incidents only if it can identify when they apply"
    reason: "The title puts the identifying capacity in the rule: grammatically, 'it' is the fixed review rule. The body puts it in the reviewer. The instruction 'does not tell the reviewer which earlier failure bears on the page', 'A reviewer following the original instruction could still recognize it', and the rule need not change. The mechanism is the reviewer recognizing the relevant feature of an earlier incident, not the rule identifying applicability. So the title points the reader toward a requirement on the rule's content, which the closing sentence ('not that the review rule must change') rejects. Reframe the condition around the reviewer, or around rule plus reviewer, e.g. 'only if the reviewer can identify when they apply'."
    level: warn
outcome: warn
---

# Review

The body's sentences correctly identify the mechanism. A standing instruction says where to look. The reviewer must recognize which feature of an earlier failure, here a shared origin behind apparent independence, bears on the new case. The test is whether the reviewer draws that distinction, not whether it retrieves the incident.

The title frames the same condition as a capacity of the rule ("it can identify when they apply"). That misdirects the reader. It suggests the rule's text must encode applicability conditions, the reading the last paragraph explicitly denies. The framing excludes the case the body actually describes: an unchanged rule whose reviewer supplies the recognition. Under this gate's severity rule, that is a WARN.
