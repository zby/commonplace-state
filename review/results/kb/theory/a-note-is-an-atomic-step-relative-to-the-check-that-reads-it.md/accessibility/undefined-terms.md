---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 4ed1fb58a1664f69922ea8d551eb75d5
completed-at: '2026-11-16T22:36:42Z'
findings:
- scope: passage
  quotes:
  - an ingest's analytical prose
  reason: '"Ingest" is used as a noun for a KB artifact (a tracked source analysis
    that holds retained quotes and the analyst''s own prose), but the note never says
    what an ingest is. A reader without Commonplace context cannot tell why an ingest''s
    prose differs from its retained quotes, and that difference is the point of the
    sentence.'
  level: warn
- scope: passage
  quotes:
  - Commonplace marks those uses `(snapshot required)`
  reason: The marker is explained by its consequence (the source counts fully against
    the step), but "snapshot" itself is not glossed. The reader is not told that it
    means the reviewer must open the full captured copy of the source. The later phrase
    "the snapshot route" relies on that unstated meaning.
  level: warn
- scope: passage
  quotes:
  - the rule for one check, Commonplace's
  reason: '"Grounding check" first appears here without a gloss. The preceding sentence
    hints at it (judging whether quoted passages support a claim), and the next section
    defines it properly, so the gap is short.'
  level: info
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/2c8f90e52ff237debd83c1db/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/2c8f90e52ff237debd83c1db/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/4ed1fb58a1664f69922ea8d551eb75d5/outputs/review-undefined-terms.md
raw-output-sha256: ad0f61cb40aefa4784691d5954527ee4c534edf7250d5a33dd56c341ca1b3b17
---

# Review

## Summary

Most technical terms are glossed where they first appear. "Atomic step" is defined in bold. "Co-loading" is explained by the following clause about how many notes fit in a context together. "Oracle domain" is paraphrased as the range of candidates a checker can assess with the required confidence. The linked theory notes are each introduced by a sentence that states their claim. The note uses no active vocabulary terms from `AGENTS.md` in a technical sense.

Two Commonplace-internal terms are used without a gloss: "ingest" as an artifact kind, and "snapshot" in the `(snapshot required)` marker and "the snapshot route". Both appear in sentences whose argument depends on knowing what they are. "Grounding check" is briefly used before its definition, which is minor.
