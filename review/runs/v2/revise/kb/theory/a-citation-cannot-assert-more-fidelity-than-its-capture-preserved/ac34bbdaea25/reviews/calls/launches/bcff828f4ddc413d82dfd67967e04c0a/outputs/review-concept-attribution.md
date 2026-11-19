---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The layering is not a design choice"
    reason: "The sentence uses the boundary-preserving-rival note as support for concluding that the layering is not a design choice, because no rival capture design preserves the commitments. The target's title and opening paragraph say the test cuts one way only: 'If no rival is found, the rule is only undemoted — not proven inherited.' Its Scope section repeats that 'the test demotes; it does not certify.' So the target's concept rules out the inference attributed to it. The note's own reasons (finite context window, copyright) could be a positive derivation from the invariants, but the sentence attributes the conclusion to the rival test, not to that derivation."
    level: warn
  - scope: passage
    quotes:
      - "This is the citation-fidelity instance of a general rule"
    reason: "The target ('History has one chance to become checkable') is about an artifact's production history: how it was produced and what was consulted. After production, that history is unrecoverable because a reviewer sees only carried state. Here the relevant 'history' is a captured passage's fidelity to its source. The note itself says that fidelity is recoverable by returning to the authoritative artifact and capturing again. That matches the target's re-checking against a source that still exists (its 'decay gradually' boundary), not its one-chance loss. The identity holds only if the instance is restated as recording the passage's layer at ingest, which is the target's records route. As written, 'one chance' and 'recoverable' pull against the target's concept."
    level: warn
  - scope: passage
    quotes:
      - "found eighteen of eighty-seven"
    reason: "The figures match ADR 046 (18 mismatches among 87 candidates, no false mismatch on manual audit). But the ADR says the mismatches are dominated by editorial omission, bracketed substitution, case changes and moved punctuation. Those are edited quotations, not paraphrase-layer passages marked verbatim. The ADR therefore supports 'naive verbatim marking fails', but it supports the layering less directly than the footer implies."
    level: info
outcome: warn
---

# Review

The note makes four identity or attribution claims about linked notes. The trace-extracted-memory attribution holds: the target places authority in post-capture verification, abstraction and consultation, and calling the two claims complements is fair. The derived-copy attribution also holds: the target's first precondition is a mechanical derivation rule, natural-language summaries explicitly lack one, and the target uses the phrase 'with a stronger trust signal attached'. The two flagged attributions use a target's concept for something it disclaims or describes differently. The rival test cannot certify a rule as non-chosen. The one-chance note concerns unrecoverable production history, but this note says fidelity can be restored by recapture. The footer links to structure inference and collection prototypes add no identity claims; the prototype target does describe a grounding marker.
