---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - return to the authoritative artifact and quote-mine it
  reason: '"Authoritative artifact" is glossed once ("the sibling PDF") in the Paraphrase
    layer bullet, then reused twice later without that gloss. Only two later uses,
    so it stays under the gate''s threshold, but a plain phrase such as "the original
    source document" would carry the meaning without scrolling back.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/af4d726260818f3bad1b6a8b/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/af4d726260818f3bad1b6a8b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 34a169f7cfd749d29f051fb42e043cd9
completed-at: '2026-11-16T22:09:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/34a169f7cfd749d29f051fb42e043cd9/outputs/review-jargon-persistence.md
raw-output-sha256: 9013544310afbc9beaf77caa6349efdf73736a6d7862118620a93e6eb6f66947
format: 2
---

# Review

## Summary

The note's recurring vocabulary mostly keeps its grounding. *Fidelity* and *authority* are defined together in the second paragraph. Later uses either sit in sentences that restate the contrast or are ordinary enough to read alone. The three layer names (verbatim, paraphrase, second-hand) are defined in the note's own list. Their qualifiers carry meaning that plain words would lose, so they fall outside this gate. Each layer name also describes itself, so later mentions such as "paraphrase-layer passage" still read correctly without scrolling back.

"Snapshot", "capture" and "ingest" recur often. These are KB-flavoured words, but their ordinary meanings (a stored copy of a source; the act of saving it; the step that saves it) are close enough that later uses stay readable.

The only term that loses its gloss is "authoritative artifact". It is glossed once as the sibling PDF and then reused twice without that gloss. That is under the gate's more-than-twice threshold, so the finding is informational.
