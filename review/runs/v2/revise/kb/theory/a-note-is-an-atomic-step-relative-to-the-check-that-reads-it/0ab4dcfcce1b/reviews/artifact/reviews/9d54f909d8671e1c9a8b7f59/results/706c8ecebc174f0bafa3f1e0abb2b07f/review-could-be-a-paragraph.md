---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/9d54f909d8671e1c9a8b7f59/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/9d54f909d8671e1c9a8b7f59/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 706c8ecebc174f0bafa3f1e0abb2b07f
completed-at: '2026-11-16T22:36:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/706c8ecebc174f0bafa3f1e0abb2b07f/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 1ce8a31eb59a6edfb27c95f66330948900a3070fcde8720980c58d42d1def533
format: 2
---

# Review

## Summary

A one-paragraph version would lose several non-obvious claims, support paths and failure conditions. The section structure is warranted.

## What a paragraph would lose

A one-paragraph rewrite could keep the headline: there are two independent bounds, and atomicity is relative to a check. It would drop load-bearing content that the headline does not imply:

- **The placement argument.** A review-side budget fails silently: a capped pass is indistinguishable from a full one. A validator-held artifact bound does not have this failure mode.
- **The derivation of the cost unit.** The unit is the unquoted source because a verbatim-quote validator discharges the finding step. This derivation has two stated limits: occurrence is not representativeness, and some sources require a snapshot.
- **The joint-support corollary.** Quote jointly supporting sources rather than split them. This is the point where the two bounds couple through the remedy.
- **The corpus evidence.** Notes that cite eight or nine sources are single-claim but not atomic. The rereading of the five-link experiment turns two findings into validator results.
- **The account of N.** N is not a capacity threshold, because there was no observed loss at 22 artifacts. N is a convention chosen for auditability, motivated by measured verdict instability.
- **The precedents.** The Descartes and Lamport precedents are explicitly scoped as analogy rather than evidence.

Each item would need its own sentence chain to survive, and several carry boundary or failure conditions. The note is not over-complex for its content.
