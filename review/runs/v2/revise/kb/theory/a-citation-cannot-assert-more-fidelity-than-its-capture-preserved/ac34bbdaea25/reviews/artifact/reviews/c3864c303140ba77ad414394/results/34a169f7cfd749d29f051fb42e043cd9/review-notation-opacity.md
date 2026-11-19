---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/notation-opacity.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/notation-opacity.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 1169b01cde2019fc32462be33de88364d0eebd8a030621ab4fd4143257dc17fe
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/c3864c303140ba77ad414394/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/c3864c303140ba77ad414394/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 34a169f7cfd749d29f051fb42e043cd9
completed-at: '2026-11-16T22:09:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/34a169f7cfd749d29f051fb42e043cd9/outputs/review-notation-opacity.md
raw-output-sha256: 415c3f933b982ab9665544189b248fb211d7db28ac7e1ca138863aaeafb130f2
format: 2
---

# Review

## Summary

The note uses no formal notation or variable names from another note. The only backtick-marked token in the prose is `verbatim`, used as a marker value: "marking a paraphrase-layer passage `verbatim`", "naive `verbatim` marking", "`verbatim`-marked spans". Each sentence shows that it is a label attached to a span to claim verbatim status. The note has already defined the verbatim layer itself. A reader can decode these sentences without the linked ADR or any other note. `epistack-casebooks` is a repository name, not notation; this gate does not judge it. No symbol needs a local definition or a plain-language replacement.
