---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - epistack casebook work in the sibling `epistack-casebooks` repository
  reason: '"Epistack" and its casebooks are named as the note''s evidence base, but
    the note never says what epistack is or what a casebook contains. Is it a project,
    a method, or a corpus of legal cases? "Sibling repository" gives only its location.
    The surrounding text hints at court documents and news articles, but it does not
    identify the project. The author should add a brief inline identification; this
    review does not supply one, because neither the note nor its links state it.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/accessibility/unidentified-references.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/accessibility/unidentified-references.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 422847c587793f494bfa140e10c46772cc1decaf72d3a611ec83daa39da288c3
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/7fa9d1add64b305bc9389e1a/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/7fa9d1add64b305bc9389e1a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 34a169f7cfd749d29f051fb42e043cd9
completed-at: '2026-11-16T22:09:03Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/34a169f7cfd749d29f051fb42e043cd9/outputs/review-unidentified-references.md
raw-output-sha256: 544d4718cc94d9c283cb34460a8778354444ad1a9cc6b69c6b163bb151559fa0
format: 2
---

# Review

## Summary

Most named references are identified. ADR 046 is described inline as "the shipped verbatim-quote checker". The footer links carry short descriptions or titles that say what they are.

The exception is the evidence paragraph's "epistack casebook work in the sibling `epistack-casebooks` repository". This is the only named external project in the note, and it supplies the empirical support (eighteen of eighty-seven mismatched spans). Yet a first-time reader cannot tell what kind of project it is. A short gloss on first mention would fix this.
