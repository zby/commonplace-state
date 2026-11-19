---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A pin records identity
  reason: '"Pin" appears here for the first and only time with no gloss. A reader
    can guess that it means the recorded checksum of a capture, but the sentence states
    that a pin records identity, so the reader needs the definition to evaluate the
    claim. Add a gloss, for example "A pin (the recorded checksum of a capture) records
    identity", or replace it with the plain phrase.'
  level: warn
- scope: passage
  quotes:
  - trade-off between checking cost and reliance risk
  - not a universal rule for retained results
  reason: '"Reliance risk" and "retained results" are KB-specific framings that are
    carried only by the link. The next sentence partly recovers the meaning ("reuse
    the check''s result, accepting the risk of changes since it ran"). A short inline
    gloss would let the sentence stand alone, for example retained results as stored
    check outcomes reused later, and reliance risk as the cost of acting on an outcome
    that has gone stale or is wrong.'
  level: info
- scope: passage
  quotes:
  - Quotations the extractor never recognized
  reason: '"The extractor" is used with a definite article but is never introduced.
    Context implies it is the component that finds quote candidates in text, but naming
    that role once would remove the guess.'
  level: info
- scope: passage
  quotes:
  - A locator the check does not test supplies context but is not evidence
  reason: '"Locator" is not defined. The preceding line-range example makes it inferable,
    so this is minor. An example such as "(a line range or page number)" would make
    it explicit.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/9e4a5b5f6a7eda9a4a1a1158/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/9e4a5b5f6a7eda9a4a1a1158/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 43caaa8c7b73402d91127314b490cc97
completed-at: '2026-11-18T16:01:57Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/43caaa8c7b73402d91127314b490cc97/outputs/review-undefined-terms.md
raw-output-sha256: cb155bf978893208eec9b416726d43ad741ab92c3acd784ce5abf85d3ae7b457
format: 2
---

# Review

## Summary

Most technical terms are introduced with enough context. "Capture" is glossed at its first body use, "exact" gets its own definition section, and the four citation questions are each stated in one line. The note uses no active vocabulary term from `AGENTS.md` in its technical sense.

One term fails the test. "Pin" arrives unexplained in a sentence that makes a claim about what a pin does, and the reader has to infer its meaning from the earlier checksum sentence. The other gaps are minor: "reliance risk" and "retained results" depend on a link, while "the extractor" and "locator" are left for the reader to infer. Context mostly recovers these, so they are recorded as info.
