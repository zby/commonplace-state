---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - and no rival capture design drops the layering while preserving the commitments
  reason: 'The inline link to ''A framework rule with a boundary-preserving rival
    is not an inherited constraint'' is placed as the support for ''The layering is
    not a design choice''. A reader who does not follow it will think the target gives
    a way to establish that a rule is inherited once no rival is found. The target''s
    opening paragraph says the opposite: finding no rival leaves the rule ''only undemoted
    — not proven inherited.'' The link text is accurate, but the sentence gives the
    wrong impression of what the link supports.'
  level: warn
- scope: passage
  quotes:
  - The one chance here is ingest
  reason: The sentence leads the reader to expect a general rule about irreversible
    loss at capture. The target's head is about production history (how an artifact
    was made and what was consulted) becoming checkable only at production time. That
    fits the claim only partly, because this note says lost fidelity can be recovered
    by re-capture.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dd7cd97daa591fc0d9bc185e/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dd7cd97daa591fc0d9bc185e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: bcff828f4ddc413d82dfd67967e04c0a
completed-at: '2026-11-16T22:11:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-misleading-link-text.md
raw-output-sha256: b0015aaaab5ab38e37b569a3d7b20342fe6aa444104ac2771f99d3904153bdbc
format: 2
---

# Review

I checked all seven link targets: trace-extracted memory, the boundary-preserving-rival rule, derived copy, history has one chance, structure inference, ADR 046 and collection prototypes. All resolve. Most link texts are the target titles, and their sentences match the target heads. The trace-extracted-memory note does place authority in post-capture operations. The derived-copy note does require a mechanical derivation rule. ADR 046 does report the 18-of-87 result. The collection-prototypes page does describe the dialectical/evidential prototype's grounding marker. One link is misleading in context: the boundary-preserving-rival rule is used to support a conclusion that its own test disclaims.
