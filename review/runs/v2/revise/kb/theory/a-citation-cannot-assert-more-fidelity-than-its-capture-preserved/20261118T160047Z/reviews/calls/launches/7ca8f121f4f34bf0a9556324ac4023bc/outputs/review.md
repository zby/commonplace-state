---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A pin records identity, and change is detected only when a later check compares current bytes with it. Checking current bytes catches a changed or removed passage at the next check"
    reason: "The two sentences say twice that change is detected only at a later check against current bytes. The second sentence's only new job is the blind spot: changed surrounding context when the quoted words survive. Fold them into one sentence, for example: 'A pin records identity; a later check against current bytes catches a changed or removed passage but misses changed surrounding context when the quoted words survive.'"
    level: warn
  - scope: passage
    quotes:
      - "A mismatched or unreadable file is a failure, not an invitation to find another copy."
      - "A silent fallback to whatever copy is present would make one citation pass or fail with ambient cache state, without declaring that dependency (ADR 073)."
    reason: "The no-fallback rule is stated twice in adjacent paragraphs. 'Not an invitation to find another copy' and 'a silent fallback to whatever copy is present' state the same prohibition; only the second gives the reason (ambient cache state decides the outcome). State the rule once, with its reason, in one place, and keep the separate point that missing bytes report as unverified."
    level: warn
  - scope: passage
    quotes:
      - "an inexpensive occurrence check can justify treating mismatch as failure rather than warning"
    reason: "This partly repeats the previous paragraph, which already says wording agreement is cheap and can block while support judgment cannot. The paragraph's distinct work is the link to the cost/reliance trade-off and the reuse remark, so it may earn its place. It could also be folded into the end of the preceding paragraph. Unsure whether the separate paragraph is needed."
    level: info
outcome: warn
---

# Review

The note is mostly compact. The four-question list, the normalization and occurrence paragraphs, the multi-read paragraph and the scope bullets each add a distinct condition or boundary. The closing sentence on verified source extracts turns the preceding mechanism into an operational recommendation, so it is not flagged as recap.

The section "Which evidence a pass is relative to" has two local redundancies. First, the pin sentences repeat when change gets detected before they add the one new limit. Second, the rule against falling back to another copy appears in the source-identity paragraph and again in the following paragraph. Each case calls for a fold, not a deletion: in both, one clause carries information the other lacks.

The cost argument for treating a mismatch as a failure overlaps with the preceding paragraph's cheap-and-binary point. It may still earn a separate paragraph because of the trade-off link, so it is recorded as INFO only.
