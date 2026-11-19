---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - So marking a paraphrase-layer passage `verbatim` does not make it verbatim
  reason: 'The body establishes that a citation can assert higher fidelity, as in
    the eighteen of eighty-seven falsely marked spans, but cannot validly hold or
    raise it: the assertion leaves the fidelity bound unchanged. Read literally, ''cannot
    assert'' conflicts with this evidence of over-assertion. The intended sense, ''cannot
    validly assert'' or ''cannot raise'', is clear from the body, so this is a wording
    point and not drift.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: f2794cf7200130c59d6861dd3f9c8c36930637b5b1504b40911cb5e1c3fca013
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/d854eddb6d9c18cf41c6a829/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/d854eddb6d9c18cf41c6a829/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 2b0b48af273645b5b65754ed36a6ff44
completed-at: '2026-11-16T22:08:51Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/2b0b48af273645b5b65754ed36a6ff44/outputs/review-title-body-alignment.md
raw-output-sha256: 2fbebf31828e3167c329acf41daaa86244ff035adbeb8d1e6125f7d54baaef5e
format: 2
---

# Review

The body supports the H1 claim directly:

- The opening paragraph states the claim: fidelity is fixed at ingest and does not increase downstream.
- The layering section explains why the bound exists.
- The notation section explains why citation syntax cannot move it.
- The corollary section applies the bound to locator design.
- The Scope section limits the claim's practical effect to lossy capture of long sources. It also says the bound is vacuous, not false, when capture is lossless, so the title's unqualified scope remains accurate.

The fidelity/authority distinction and the locator corollary go beyond the title, but they develop the claim rather than replace it. No claim or scope drift is present. One info finding notes that the verb "assert" is looser than what the body establishes.
