---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: bcff828f4ddc413d82dfd67967e04c0a
completed-at: '2026-11-16T22:11:38Z'
findings:
- scope: passage
  quotes:
  - The layering is not a design choice
  reason: 'The sentence uses the boundary-preserving-rival note as support for concluding
    that the layering is not a design choice, because no rival capture design preserves
    the commitments. The target''s title and opening paragraph say the test cuts one
    way only: ''If no rival is found, the rule is only undemoted — not proven inherited.''
    Its Scope section repeats that ''the test demotes; it does not certify.'' So the
    target''s concept rules out the inference attributed to it. The note''s own reasons
    (finite context window, copyright) could be a positive derivation from the invariants,
    but the sentence attributes the conclusion to the rival test, not to that derivation.'
  level: warn
- scope: passage
  quotes:
  - This is the citation-fidelity instance of a general rule
  reason: 'The target (''History has one chance to become checkable'') is about an
    artifact''s production history: how it was produced and what was consulted. After
    production, that history is unrecoverable because a reviewer sees only carried
    state. Here the relevant ''history'' is a captured passage''s fidelity to its
    source. The note itself says that fidelity is recoverable by returning to the
    authoritative artifact and capturing again. That matches the target''s re-checking
    against a source that still exists (its ''decay gradually'' boundary), not its
    one-chance loss. The identity holds only if the instance is restated as recording
    the passage''s layer at ingest, which is the target''s records route. As written,
    ''one chance'' and ''recoverable'' pull against the target''s concept.'
  level: warn
- scope: passage
  quotes:
  - found eighteen of eighty-seven
  reason: The figures match ADR 046 (18 mismatches among 87 candidates, no false mismatch
    on manual audit). But the ADR says the mismatches are dominated by editorial omission,
    bracketed substitution, case changes and moved punctuation. Those are edited quotations,
    not paraphrase-layer passages marked verbatim. The ADR therefore supports 'naive
    verbatim marking fails', but it supports the layering less directly than the footer
    implies.
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/ebc08b017d55081bc0e97a49/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/ebc08b017d55081bc0e97a49/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-concept-attribution.md
raw-output-sha256: 47372b82c3e79df6efb79e62d3b0c7d2a6fa0d94939e1824e3583670069b39b8
---

# Review

The note makes four identity or attribution claims about linked notes. The trace-extracted-memory attribution holds: the target places authority in post-capture verification, abstraction and consultation, and calling the two claims complements is fair. The derived-copy attribution also holds: the target's first precondition is a mechanical derivation rule, natural-language summaries explicitly lack one, and the target uses the phrase 'with a stronger trust signal attached'. The two flagged attributions use a target's concept for something it disclaims or describes differently. The rival test cannot certify a rule as non-chosen. The one-chance note concerns unrecoverable production history, but this note says fidelity can be restored by recapture. The footer links to structure inference and collection prototypes add no identity claims; the prototype target does describe a grounding marker.
