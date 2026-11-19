---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
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
  - Two spans at the same file offset can differ in provenance quality by a full layer
  reason: 'Within one snapshot, a single file offset identifies one passage. That
    passage lies either in the verbatim block or in the paraphrase summary, so two
    spans at the same offset cannot come from different layers. The real mechanism
    is different: a bare position does not show the consumer which layer it falls
    in. Spans that look alike as positions, such as nearby offsets or the same section,
    can sit in different layers, and the consumer cannot tell them apart without resolving
    the snapshot. The current framing places the problem in an impossible collision
    rather than in what the locator exposes.'
  level: warn
- scope: passage
  quotes:
  - The claim bites exactly where capture is lossy, which is to say wherever the sources
    are long.
  reason: This equates lossy capture with long sources. The note's own mechanism covers
    cases that framing excludes. The second-hand layer arises from intermediaries,
    such as a news article quoting an order that is no longer served, whatever the
    source length. Copyright trims can also apply to short sources. Saying the claim
    applies 'wherever the sources are long' leaves out those cases.
  level: warn
- scope: passage
  quotes:
  - If a source is short enough to capture losslessly
  reason: This is the same narrowing seen from the other side. The text says a short
    source collapses the layers to one, but brevity removes only the verbatim/paraphrase
    split. A short capture can still be second-hand, so the bound does not become
    vacuous merely because the source is short.
  level: warn
- scope: passage
  quotes:
  - Any framework whose consumer is an LLM and whose sources are real documents faces
    both
  reason: The copyright barrier applies to copyrighted sources, not to all 'real documents'.
    Public-domain material, much court and government material, and a project's own
    documents do not face it. The framing overstates the generality of one of the
    two forcing reasons. This matters to the section's 'forced' claim, but it does
    not exclude cases the mechanism covers.
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/de83b6a3abc20aa0d8935d60/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/de83b6a3abc20aa0d8935d60/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-framing-mismatch.md
raw-output-sha256: 59db6b08ca16a43efac620728432e03d493f028b5aa88e7a52ee0298e7dd90f7
---

# Review

The core mechanisms are framed at the right level. Fidelity is non-increasing because only verbatim text has a mechanical derivation rule. Notation can express the bound but cannot move it, and re-capture is the only repair. The problems appear where the note maps its mechanism onto concrete cases. The locator corollary places the problem in a same-offset collision that cannot happen within one snapshot. The Scope section uses source length as a stand-in for lossiness, which drops the second-hand layer and short copyrighted sources from a claim whose mechanism covers them.
