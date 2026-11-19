---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Change the premise and the conclusion moves, which is where the claim earns its
    boundaries.
  reason: Throat-clearing opener for the Scope section. It announces that a boundary
    follows instead of stating one; the next sentence already does the boundary work.
    Deleting it loses nothing the reader can understand, decide or verify.
  level: warn
- scope: passage
  quotes:
  - The claim bites exactly where capture is lossy, which is to say wherever the sources
    are long.
  reason: Closing restatement of the paragraph's own opening condition (short sources
    capture losslessly, so the bound goes vacuous). It adds no admission, boundary
    case or decision rule beyond what the paragraph already established, and the next
    paragraph supplies the practical stance. Cut it, or fold 'wherever the sources
    are long' into the preceding sentence if the positive phrasing is wanted.
  level: warn
- scope: passage
  quotes:
  - recoverable only by returning to the authoritative artifact and capturing again
  reason: Third statement of the re-capture remedy (the opening paragraph already
    says 'The only operation that raises fidelity is re-capture', and the Scope section
    repeats it operationally). The link to the general rule and 'The one chance here
    is ingest' do real work; this trailing clause may be reinforcement or may be pure
    repetition. Unsure whether it earns its place.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/5f19016a8f48cbb8f0ad4cbe/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/5f19016a8f48cbb8f0ad4cbe/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 47cc4c8654e749309269fb524cb24844
completed-at: '2026-11-16T22:10:56Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/47cc4c8654e749309269fb524cb24844/outputs/review.md
raw-output-sha256: 172b098a44b3dbea9b76e6747b994165b2ca684fe56ee52a71e5f3fb117090ec
format: 2
---

# Review

## Summary

The note is mostly tight. The opening thesis, the fidelity/authority contrast, the three-layer list, the derivation-rule argument in "Why notation cannot repair it", the locator corollary, the practical-consequence paragraph and the evidence footer each do distinct work. Deleting any of them would weaken the argument or remove grounding.

The redundancy sits in the Scope section's first paragraph. That paragraph has one real job: to state the lossless-capture case and the locator boundary that follows from it. An announcing opener and a recap closer wrap that job and add nothing to it. Removing both leaves the boundary intact and shorter.

A non-obvious pass: "Notation can *express* the fidelity bound. It cannot move it." restates the section's conclusion. It still earns its place because it turns the derivation argument into a memorable stance that the corollary then builds on. The second Scope paragraph also passes. It repeats the ingest-time condition, but it converts that condition into an operational rule: promote load-bearing passages at capture time or re-mine the authoritative artifact.
