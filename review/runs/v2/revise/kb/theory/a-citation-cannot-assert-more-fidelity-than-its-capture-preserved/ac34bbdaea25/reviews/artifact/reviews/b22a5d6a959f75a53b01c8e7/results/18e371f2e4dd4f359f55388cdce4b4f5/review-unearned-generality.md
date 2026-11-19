---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: f2419977ea2ca2adc64b5e1cec80307125cef1c3ddcd35727b8c85310517f854
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/b22a5d6a959f75a53b01c8e7/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/b22a5d6a959f75a53b01c8e7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-unearned-generality.md
raw-output-sha256: fac12ff08275b4ece007a6ad4b8236c7acaabd81ffc87e370839c79bf3109a63
format: 2
---

# Review

The central claim's abstract terms are "citation", "fidelity" and "capture".

- **"Capture" for "snapshot/ingest".** Downgrading the title to "A KB note citing a snapshot cannot assert more fidelity than the snapshot preserved" leaves the argument intact. The mechanism, however, does not depend on the KB snapshot format. It turns on whether a mechanical derivation rule exists from a captured passage back to its source, which is a property of the relation between a capture and its source, not of markdown snapshots. The general term therefore forbids more: it rules out raising fidelity downstream for any lossy capture, not only Commonplace snapshots. The forbidding force is argued, not merely covered.
- **"Fidelity".** The note defines it narrowly as the grade of provenance evidence a passage carries, and sets it explicitly against "authority". The term is precise, not inflated.
- **"Citation".** This is the ordinary concrete term.

Distribution is healthy. The abstraction is concentrated in the title and opening, and the body works in concrete terms: verbatim block, paraphrase summary, sibling PDF, substring match and file offset. No defensive widening was found.
