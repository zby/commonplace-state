---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - no rival capture design drops the layering while preserving the commitments the
    framework has already made
  - provider-contingent rather than inherited
  reason: 'The section''s argument that layering is forced depends on the linked note''s
    technical sense of an "inherited constraint" and a "boundary-preserving rival".
    Neither term is glossed inline; the link title stands in for the definition. The
    later contrast "provider-contingent rather than inherited" also needs that sense.
    A reader who has not opened the linked note cannot tell what test makes a constraint
    inherited. Add a short gloss, for example: a constraint is inherited when no alternative
    design avoids it while keeping the framework''s existing commitments.'
  level: warn
- scope: passage
  quotes:
  - Fidelity is fixed at ingest
  reason: '"Ingest" is a KB-specific step name. The preceding sentence''s "capture
    step" lets a reader infer that ingest is when the source is captured, so this
    is minor. Saying "at ingest (the capture step)" once would remove the inference.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dbaef9ee63e11c06cc93e23f/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dbaef9ee63e11c06cc93e23f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 34a169f7cfd749d29f051fb42e043cd9
completed-at: '2026-11-16T22:09:03Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/34a169f7cfd749d29f051fb42e043cd9/outputs/review-undefined-terms.md
raw-output-sha256: 2417ac7b5faadce2261c0ea16ac80de725d7e2e5d798dfa0f6b403bdb5992712
format: 2
---

# Review

## Summary

The note defines its central terms well. *Fidelity* and *authority* get explicit inline definitions. The three capture layers are defined in a list. "Mechanical derivation rule" is made concrete at once with substring match as the example. "Source-span locator" is clear from the surrounding sentences.

The main gap is in "Capture is layered because it is forced to be". The section claims layering is not a design choice and supports that by citing the linked note's notions of an *inherited* constraint and a *boundary-preserving rival*. The sentence uses those terms in their technical sense but does not gloss them. "Provider-contingent rather than inherited" later relies on the same distinction. So the reader has to follow the link to see why the section's conclusion holds.

"Ingest" is a smaller case: the reader can infer it from the adjacent "capture step".
